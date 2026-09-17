#!/usr/bin/env python3
"""
generate_music.py — generate the looping music beds with the ElevenLabs Music API.

    python3 tools/generate_music.py --list
    python3 tools/generate_music.py music.casual.1
    python3 tools/generate_music.py --all
    python3 tools/generate_music.py music.boss.2 --force

Music is not a sound effect and is handled separately throughout:
  * a different endpoint (/v1/music, not /v1/sound-generation),
  * **stereo**, because a mono music bed sounds flat,
  * tens of seconds long rather than under a second,
  * streamed as its own file instead of being packed into the sprite, so a game
    downloads only the track it is actually playing.

Prompts, lengths and loop settings all come from registry.json, same as the SFX.
Existing tracks are skipped unless --force.
"""

import argparse
import json
import os
import re
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENDPOINT = 'https://api.elevenlabs.io/v1/music'
LOW_LEVEL_DB = -20.0


def api_key():
    k = os.environ.get('ELEVENLABS_API_KEY')
    if k:
        return k.strip()
    for path in (os.path.expanduser('~/.config/elevenlabs/key'),
                 os.path.join(ROOT, '.elevenlabs.key')):
        if os.path.exists(path):
            k = open(path).read().strip()
            if k:
                return k
    sys.exit('No ElevenLabs API key found (see tools/generate_ai.py for where it looks).')


def registry():
    with open(os.path.join(ROOT, 'packs', 'casual', 'registry.json')) as fh:
        return json.load(fh)


def peak_dbfs(path):
    r = subprocess.run(['ffmpeg', '-i', path, '-af', 'volumedetect', '-f', 'null', '-'],
                       capture_output=True, text=True)
    m = re.search(r'max_volume:\s*(-?\d+(?:\.\d+)?) dB', r.stderr)
    return float(m.group(1)) if m else None


def compose(key, prompt, seconds):
    body = json.dumps({'prompt': prompt, 'music_length_ms': int(seconds * 1000)}).encode()
    req = urllib.request.Request(ENDPOINT, data=body, method='POST', headers={
        'xi-api-key': key, 'Content-Type': 'application/json', 'Accept': 'audio/mpeg'})
    try:
        with urllib.request.urlopen(req, timeout=600) as r:
            return r.read()
    except urllib.error.HTTPError as e:
        detail = e.read().decode('utf-8', 'replace')[:400]
        hint = {401: 'key rejected', 402: 'out of credits',
                422: 'prompt or length rejected', 429: 'rate limited'}.get(e.code, '')
        sys.exit('Music API returned HTTP {}{}\n{}'.format(
            e.code, ' (' + hint + ')' if hint else '', detail))
    except urllib.error.URLError as e:
        sys.exit('Could not reach the music API: {}'.format(e.reason))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('names', nargs='*')
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--list', action='store_true')
    ap.add_argument('--force', action='store_true')
    args = ap.parse_args()

    reg = registry()
    tracks = {n: d for n, d in reg['sounds'].items() if d.get('music')}
    out_dir = os.path.join(ROOT, 'packs', 'casual', 'music')
    os.makedirs(out_dir, exist_ok=True)

    def path_for(n):
        return os.path.join(out_dir, n + '.mp3')

    if args.list:
        print('{} music tracks:'.format(len(tracks)))
        for n in sorted(tracks):
            have = 'have' if os.path.exists(path_for(n)) else '--  '
            print('  {}  {:<22} {:>3}s  {}'.format(have, n, tracks[n]['music']['seconds'],
                                                   tracks[n]['whenToUse'][:48]))
        return

    targets = sorted(tracks) if args.all else args.names
    if not targets:
        sys.exit('Pass track names, or --all, or --list.')
    unknown = [n for n in targets if n not in tracks]
    if unknown:
        sys.exit('Not music tracks in the registry: ' + ', '.join(unknown))

    todo = [n for n in targets if args.force or not os.path.exists(path_for(n))]
    skipped = len(targets) - len(todo)
    if skipped:
        print('{} already generated, skipping (use --force to redo).'.format(skipped))
    if not todo:
        return

    key = api_key()
    total = sum(tracks[n]['music']['seconds'] for n in todo)
    print('Generating {} track(s), {}s of music.\n'.format(len(todo), total))

    weak = []
    for n in todo:
        spec = tracks[n]['music']
        print('  {:<22} {:>3}s …'.format(n, spec['seconds']), end='', flush=True)
        audio = compose(key, spec['prompt'], spec['seconds'])
        dst = path_for(n)
        with open(dst, 'wb') as fh:
            fh.write(audio)
        lvl = peak_dbfs(dst)
        note = '' if lvl is None else '  peak {:.1f} dBFS'.format(lvl)
        if lvl is not None and lvl < LOW_LEVEL_DB:
            note += '  << too quiet'
            weak.append(n)
        print(' {:.0f} KB{}'.format(len(audio) / 1024, note))

    print('\nWrote {} track(s) to packs/casual/music/'.format(len(todo)))
    if weak:
        print('Too quiet, reword: ' + ', '.join(weak))
    print('Next: python3 tools/build_pack.py casual')


if __name__ == '__main__':
    main()
