#!/usr/bin/env python3
"""
generate_ai.py — generate the "ai" sounds with the ElevenLabs Sound Effects API.

    python3 tools/generate_ai.py --list                 what still needs audio
    python3 tools/generate_ai.py state.win reward.chest generate these
    python3 tools/generate_ai.py --first 5              the 5 most useful missing ones
    python3 tools/generate_ai.py step.grass --takes 5   several takes of one sound
    python3 tools/generate_ai.py state.win --force      redo one you did not like

Prompts, durations and take counts all come from packs/casual/registry.json, so
what gets generated is exactly what the library documents.

The API key is read, in order, from:
    1. $ELEVENLABS_API_KEY
    2. ~/.config/elevenlabs/key
    3. ./.elevenlabs.key          (gitignored)
It is never printed and never written anywhere.

Existing files are skipped unless --force, so re-running is safe and free.
"""

import argparse
import json
import os
import sys
import subprocess
import re
import tempfile
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENDPOINT = 'https://api.elevenlabs.io/v1/sound-generation'
MIN_DURATION = 0.5          # the API's floor; build_pack trims the silence back off
HEADROOM = 0.15             # a little room for the tail; more invites a SEQUENCE
                            # (asking 0.65s for 'a single footstep' returns several)
PROMPT_INFLUENCE = 0.5      # higher = follows the prompt more literally
LOW_LEVEL_DB = -20.0        # a take quieter than this is unusable
MAX_ATTEMPTS = 3            # generations vary, so a quiet one is worth retrying


def api_key():
    key = os.environ.get('ELEVENLABS_API_KEY')
    if key:
        return key.strip()
    for path in (os.path.expanduser('~/.config/elevenlabs/key'),
                 os.path.join(ROOT, '.elevenlabs.key')):
        if os.path.exists(path):
            with open(path) as fh:
                key = fh.read().strip()
            if key:
                return key
    sys.exit(
        'No ElevenLabs API key found.\n'
        'Put it in one of these (it is never printed or committed):\n'
        '  export ELEVENLABS_API_KEY=...\n'
        '  ~/.config/elevenlabs/key\n'
        '  ' + os.path.join(ROOT, '.elevenlabs.key'))


def registry():
    with open(os.path.join(ROOT, 'packs', 'casual', 'registry.json')) as fh:
        return json.load(fh)


def existing(name, sounds_dir):
    if not os.path.isdir(sounds_dir):
        return []
    out = []
    for f in sorted(os.listdir(sounds_dir)):
        stem = os.path.splitext(f)[0]
        if stem == name or (stem.startswith(name + '.') and stem[len(name) + 1:].isdigit()):
            out.append(f)
    return out


def peak_dbfs(audio_bytes):
    """Peak level of an in-memory mp3, via ffmpeg. None if it cannot be read."""
    with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as fh:
        fh.write(audio_bytes)
        tmp = fh.name
    try:
        r = subprocess.run(['ffmpeg', '-i', tmp, '-af', 'volumedetect', '-f', 'null', '-'],
                           capture_output=True, text=True)
        m = re.search(r'max_volume:\s*(-?\d+(?:\.\d+)?) dB', r.stderr)
        return float(m.group(1)) if m else None
    finally:
        os.unlink(tmp)


def generate(key, text, seconds):
    body = json.dumps({
        'text': text,
        'duration_seconds': max(MIN_DURATION, round(seconds + min(HEADROOM, seconds * 0.5), 2)),
        'prompt_influence': PROMPT_INFLUENCE,
    }).encode()
    req = urllib.request.Request(ENDPOINT, data=body, method='POST', headers={
        'xi-api-key': key,
        'Content-Type': 'application/json',
        'Accept': 'audio/mpeg',
    })
    try:
        with urllib.request.urlopen(req, timeout=120) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        detail = e.read().decode('utf-8', 'replace')[:400]
        hint = {
            401: 'the key was rejected — check it is correct and active',
            402: 'out of credits on this ElevenLabs plan',
            422: 'the API rejected the prompt or duration',
            429: 'rate limited — wait a moment and run again',
        }.get(e.code, '')
        sys.exit('ElevenLabs returned HTTP {}{}\n{}'.format(
            e.code, ' (' + hint + ')' if hint else '', detail))
    except urllib.error.URLError as e:
        sys.exit('Could not reach ElevenLabs: {}'.format(e.reason))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('names', nargs='*')
    ap.add_argument('--first', type=int, help='generate the N most useful missing sounds')
    ap.add_argument('--takes', type=int, help='override how many takes per sound')
    ap.add_argument('--force', action='store_true', help='regenerate even if a file exists')
    ap.add_argument('--list', action='store_true', help='show what still needs audio')
    ap.add_argument('--dry-run', action='store_true', help='show the plan, call nothing')
    args = ap.parse_args()

    reg = registry()
    sounds = reg['sounds']
    sounds_dir = os.path.join(ROOT, 'packs', 'casual', 'sounds')
    os.makedirs(sounds_dir, exist_ok=True)

    needs = [n for n, d in sounds.items() if d.get('source') in ('ai', 'hybrid')]
    missing = [n for n in needs if not existing(n, sounds_dir)]

    if args.list:
        print('{} sounds need audio, {} still missing:'.format(len(needs), len(missing)))
        for n in missing:
            d = sounds[n]
            print('  {:<20} {:>4}s x{}  {}'.format(
                n, d.get('duration'), d.get('variationsWanted', 1), d.get('whenToUse', '')[:60]))
        return

    # The order a game needs most: results, then the big reward, then textures.
    PRIORITY = ['state.win', 'state.lose', 'reward.chest', 'break.glass', 'weapon.pistol',
                'step.grass', 'step.wood', 'step.stone', 'impact.punch', 'water.splash']
    if args.first:
        ranked = [n for n in PRIORITY if n in missing] + [n for n in missing if n not in PRIORITY]
        targets = ranked[:args.first]
    else:
        targets = args.names

    if not targets:
        sys.exit('Nothing to do. Pass sound names, or --first N, or --list.')

    unknown = [n for n in targets if n not in sounds]
    if unknown:
        sys.exit('Not in the registry: ' + ', '.join(unknown))
    not_ai = [n for n in targets if sounds[n].get('source') == 'code']
    if not_ai:
        sys.exit('These are made by code and need no audio: ' + ', '.join(not_ai))

    plan = []
    for name in targets:
        d = sounds[name]
        takes = args.takes or d.get('variationsWanted', 1)
        have = existing(name, sounds_dir)
        if have and not args.force:
            print('skip   {:<20} already have {}'.format(name, ', '.join(have)))
            continue
        plan.append((name, d, takes))

    if not plan:
        print('Everything requested already exists. Use --force to redo.')
        return

    total = sum(t for _, _, t in plan)
    print('Will generate {} file(s) for {} sound(s):'.format(total, len(plan)))
    for name, d, takes in plan:
        print('  {:<20} {}s x{}'.format(name, d.get('duration'), takes))
        print('      "{}"'.format(d['prompt']))
    if args.dry_run:
        print('\n--dry-run: nothing was called.')
        return

    key = api_key()
    print()
    written, weak = [], []
    for name, d, takes in plan:
        for i in range(takes):
            suffix = '' if takes == 1 else '.{}'.format(i + 1)
            out = os.path.join(sounds_dir, '{}{}.mp3'.format(name, suffix))
            print('  generating {}{} …'.format(name, suffix), end='', flush=True)

            # A take that comes back very quiet is a failed generation. Keeping
            # it would mean build_pack normalizes its noise floor up by 30+ dB,
            # which is how a whisper-quiet pistol turns into a laser. Retry.
            audio, level = None, None
            for attempt in range(1, MAX_ATTEMPTS + 1):
                cand = generate(key, d['prompt'], d.get('duration', 1.0))
                lvl = peak_dbfs(cand)
                floor = d.get('minLevelDb', LOW_LEVEL_DB)
                if lvl is None or lvl >= floor:
                    audio, level = cand, lvl
                    break
                print(' [{:.0f} dBFS, too quiet — retrying]'.format(lvl), end='', flush=True)
                audio, level = cand, lvl

            with open(out, 'wb') as fh:
                fh.write(audio)
            note = '' if level is None else '  peak {:.1f} dBFS'.format(level)
            if level is not None and level < d.get('minLevelDb', LOW_LEVEL_DB):
                note += '  << STILL TOO QUIET, reword the prompt'
                weak.append(name)
            print(' {:.0f} KB{}'.format(len(audio) / 1024, note))
            written.append(out)

    print('\nWrote {} file(s) to packs/casual/sounds/'.format(len(written)))
    if weak:
        print('Too quiet even after retries, reword their prompts: ' + ', '.join(sorted(set(weak))))
    print('Next: python3 tools/build_pack.py casual   then listen on tools/preview.html')


if __name__ == '__main__':
    main()
