#!/usr/bin/env python3
"""
build_pack.py — turn a folder of raw sounds into the bundle games load.

    python3 tools/build_pack.py casual

What it does:
  1. Reads packs/<pack>/registry.json (the source of truth).
  2. Finds a source file per sound in packs/<pack>/sounds/
       ui.tap.wav              a single sound
       coin.collect.1.wav ...  numbered variations of one sound
     (.wav, .mp3, .m4a, .aiff and .ogg all work)
  3. Trims silence, peak-normalizes, converts to 48 kHz mono.
  4. Glues them all into ONE audio sprite + a JSON of offsets, so a game
     downloads and decodes one file instead of a hundred.
  5. Encodes the sprite twice: .webm (opus, small) and .m4a (aac, works on
     every iPhone). The runtime picks whichever the browser supports.
  6. Writes dist/<pack>.json, dist/<pack>.webm, dist/<pack>.m4a, dist/sfx.js

Sounds with no source file yet are still listed in the manifest — the runtime
plays its built-in synth stand-in for them, so nothing is ever silent.

Needs ffmpeg (brew install ffmpeg). No Python packages required.
"""

import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GAP = 0.25          # seconds of silence between sounds in the sprite
SAMPLE_RATE = 48000
PEAK_TARGET_DB = -1.0
LOW_LEVEL_DB = -20.0        # below this, a generated file is unusable.
                            # Naturally soft sounds (grass, snow, cloth) can lower
                            # their own floor with "minLevelDb" in the registry:
                            # what makes boosting dangerous is a noisy source, and
                            # a clean quiet one survives it fine.
TRIM_BELOW_PEAK_DB = 45.0   # silence = this far under the file's own peak
EXTS = ('.wav', '.mp3', '.m4a', '.aiff', '.aif', '.ogg', '.flac')


def run(args, **kw):
    return subprocess.run(args, capture_output=True, text=True, **kw)


def need_ffmpeg():
    if not shutil.which('ffmpeg'):
        sys.exit('ffmpeg not found. Install it with:  brew install ffmpeg')


def duration_of(path):
    r = run(['ffprobe', '-v', 'error', '-show_entries', 'format=duration',
             '-of', 'default=nw=1:nk=1', path])
    try:
        return float(r.stdout.strip())
    except ValueError:
        sys.exit('Could not read duration of ' + path)


def peak_db(path):
    r = run(['ffmpeg', '-i', path, '-af', 'volumedetect', '-f', 'null', '-'])
    m = re.search(r'max_volume:\s*(-?\d+(?:\.\d+)?) dB', r.stderr)
    return float(m.group(1)) if m else 0.0


def post_fx(fx):
    """Per-sound repair, from registry.json -> postFx.

    Generators bake in room reverb even when the prompt says "dry", which reads
    as the sound being far away, and their output is often dull. These let a
    sound be fixed without regenerating it:
        tighten  seconds — hard-stop the sound here, killing a room tail
        highpass Hz      — cut rumble that reads as distant boom
        bright   dB      — high-shelf lift to restore presence
        presence dB      — mid lift around 2.5 kHz, where "close" lives
    """
    chain = []
    if fx.get('highpass'):
        chain.append('highpass=f={}'.format(fx['highpass']))
    if fx.get('presence'):
        chain.append('equalizer=f=2500:t=q:w=1.2:g={}'.format(fx['presence']))
    if fx.get('bright'):
        chain.append('highshelf=f=5000:g={}'.format(fx['bright']))
    if fx.get('tighten'):
        t = float(fx['tighten'])
        chain.append('afade=t=out:st={:.4f}:d={:.4f}'.format(max(0.0, t - 0.04), 0.04))
        chain.append('atrim=end={:.4f}'.format(t))
    return chain


def prepare(src, dst, warnings, fx=None, low_level_db=None):
    """Trim silence at both ends, repair, peak-normalize, fade edges, 48k mono."""
    src_peak = peak_db(src)

    # A generated file that comes back very quiet is a BAD generation, not a
    # quiet sound. Normalizing it would raise its noise floor and codec
    # artifacts by the same amount and turn it into junk — which is exactly how
    # a -36 dBFS "pistol" once became a laser. Flag it instead of hiding it.
    floor = LOW_LEVEL_DB if low_level_db is None else low_level_db
    if src_peak < floor:
        warnings.append('{} is {:.1f} dBFS at source — too quiet to use; regenerate it '
                        '(normalizing would boost its noise by {:.0f} dB)'
                        .format(os.path.basename(src), src_peak, PEAK_TARGET_DB - src_peak))

    # Trim relative to THIS file's own peak, not an absolute dB value. An
    # absolute threshold leaves a near-silent gap followed by a stray blip
    # whenever a file has a low-level tail, which is heard as a click or a
    # little pitched burst at the very end.
    thresh = max(-60.0, src_peak - TRIM_BELOW_PEAK_DB)
    trim = (
        'silenceremove=start_periods=1:start_silence=0:start_threshold={t}dB:detection=peak,'
        'areverse,'
        'silenceremove=start_periods=1:start_silence=0.01:start_threshold={t}dB:detection=peak,'
        'areverse'
    ).format(t=round(thresh, 1))

    tmp = dst + '.trim.wav'
    r = run(['ffmpeg', '-y', '-i', src, '-af', trim,
             '-ar', str(SAMPLE_RATE), '-ac', '1', '-c:a', 'pcm_s16le', tmp])
    if r.returncode != 0:
        sys.exit('ffmpeg failed on ' + src + '\n' + r.stderr[-800:])

    fx_chain = post_fx(fx or {})
    if fx_chain:
        fixed = dst + '.fx.wav'
        r = run(['ffmpeg', '-y', '-i', tmp, '-af', ','.join(fx_chain),
                 '-ar', str(SAMPLE_RATE), '-ac', '1', '-c:a', 'pcm_s16le', fixed])
        if r.returncode != 0:
            sys.exit('postFx failed on ' + src + '\n' + r.stderr[-800:])
        os.remove(tmp)
        tmp = fixed

    dur = duration_of(tmp)
    if dur <= 0.02:
        warnings.append(os.path.basename(src) + ' trimmed to nothing — regenerate it')
        dur = max(dur, 0.05)

    # Normalize, then fade both edges so no slice can click at its boundary.
    gain = PEAK_TARGET_DB - peak_db(tmp)
    fade_out = min(0.03, dur * 0.25)
    chain = 'volume={:.2f}dB,afade=t=in:st=0:d=0.004,afade=t=out:st={:.4f}:d={:.4f}'.format(
        gain, max(0.0, dur - fade_out), fade_out)
    r = run(['ffmpeg', '-y', '-i', tmp, '-af', chain,
             '-ar', str(SAMPLE_RATE), '-ac', '1', '-c:a', 'pcm_s16le', dst])
    os.remove(tmp)
    if r.returncode != 0:
        sys.exit('ffmpeg failed normalizing ' + src + '\n' + r.stderr[-800:])
    return duration_of(dst)


def silence(path, seconds):
    run(['ffmpeg', '-y', '-f', 'lavfi', '-i',
         'anullsrc=r={}:cl=mono'.format(SAMPLE_RATE),
         '-t', str(seconds), '-c:a', 'pcm_s16le', path])


def sources_for(name, folder):
    """Return the source files for a sound name, variations in order."""
    single, numbered = [], []
    for f in sorted(os.listdir(folder)) if os.path.isdir(folder) else []:
        stem, ext = os.path.splitext(f)
        if ext.lower() not in EXTS:
            continue
        if stem == name:
            single.append(os.path.join(folder, f))
        elif re.fullmatch(re.escape(name) + r'\.\d+', stem):
            numbered.append(os.path.join(folder, f))
    return numbered or single


def build(pack):
    need_ffmpeg()
    pack_dir = os.path.join(ROOT, 'packs', pack)
    reg_path = os.path.join(pack_dir, 'registry.json')
    if not os.path.exists(reg_path):
        sys.exit('No registry at ' + reg_path)

    with open(reg_path) as fh:
        reg = json.load(fh)

    sounds_dir = os.path.join(pack_dir, 'sounds')
    dist = os.path.join(ROOT, 'dist')
    os.makedirs(dist, exist_ok=True)

    warnings = []
    work = tempfile.mkdtemp(prefix='sfxpack-')
    pieces, cursor, built, missing, code_only = [], 0.0, [], [], []

    gap_file = os.path.join(work, '_gap.wav')
    silence(gap_file, GAP)

    for name, definition in reg['sounds'].items():
        files = sources_for(name, sounds_dir)
        if not files:
            # A "code" sound is finished by design — it never wants an audio file.
            if definition.get('source') == 'code':
                code_only.append(name)
            else:
                missing.append(name)
            definition.pop('start', None)
            definition.pop('dur', None)
            definition.pop('variations', None)
            continue

        slices = []
        for i, src in enumerate(files):
            out = os.path.join(work, '{:03d}_{}_{}.wav'.format(len(pieces), name.replace('.', '_'), i))
            dur = prepare(src, out, warnings, definition.get('postFx'),
                          definition.get('minLevelDb'))
            pieces.append(out)
            slices.append([round(cursor, 4), round(dur, 4)])
            cursor += dur + GAP
            pieces.append(gap_file)

        definition['start'] = slices[0][0]
        definition['dur'] = slices[0][1]
        if len(slices) > 1:
            definition['variations'] = slices
        built.append('{} ({})'.format(name, len(slices)))

    manifest = dict(reg)
    if pieces:
        concat_list = os.path.join(work, 'list.txt')
        with open(concat_list, 'w') as fh:
            for p in pieces:
                fh.write("file '{}'\n".format(p.replace("'", r"'\''")))

        sprite_wav = os.path.join(work, 'sprite.wav')
        r = run(['ffmpeg', '-y', '-f', 'concat', '-safe', '0', '-i', concat_list,
                 '-c:a', 'pcm_s16le', sprite_wav])
        if r.returncode != 0:
            sys.exit('ffmpeg concat failed\n' + r.stderr[-800:])

        webm = os.path.join(dist, pack + '.webm')
        m4a = os.path.join(dist, pack + '.m4a')
        run(['ffmpeg', '-y', '-i', sprite_wav, '-c:a', 'libopus',
             '-b:a', '96k', '-vbr', 'on', '-application', 'audio', webm])
        run(['ffmpeg', '-y', '-i', sprite_wav, '-c:a', 'aac',
             '-b:a', '128k', '-movflags', '+faststart', m4a])

        manifest['sprite'] = {'webm': pack + '.webm', 'm4a': pack + '.m4a'}
        manifest['spriteDuration'] = round(cursor, 4)
    else:
        manifest['sprite'] = None
        # No source audio: drop any sprite left over from an earlier build, so
        # dist never ships a file the manifest does not point at.
        for stale in (pack + '.webm', pack + '.m4a'):
            path = os.path.join(dist, stale)
            if os.path.exists(path):
                os.remove(path)
                print('  removed stale ' + stale)

    # The runtime does not need the generation prompts; keep the bundle lean.
    for definition in manifest['sounds'].values():
        definition.pop('prompt', None)
        definition.pop('postFx', None)
        definition.pop('minLevelDb', None)
        definition.pop('variationsWanted', None)

    with open(os.path.join(dist, pack + '.json'), 'w') as fh:
        json.dump(manifest, fh, indent=2)
        fh.write('\n')

    shutil.copyfile(os.path.join(ROOT, 'src', 'sfx.js'), os.path.join(dist, 'sfx.js'))
    shutil.rmtree(work, ignore_errors=True)

    print('Pack "{}" v{}'.format(reg['name'], reg['version']))
    print('  synthesized by code (done, no file needed) : {}'.format(len(code_only)))
    print('  built from real audio                     : {}'.format(len(built)))
    for b in built:
        print('      ' + b)
    print('  still waiting for audio (stand-in playing) : {}'.format(len(missing)))
    for m in missing:
        print('      ' + m)
    if pieces:
        for f in (pack + '.webm', pack + '.m4a'):
            p = os.path.join(dist, f)
            print('  {:<14} {:>8.1f} KB'.format(f, os.path.getsize(p) / 1024))
    print('  dist/{}.json and dist/sfx.js written.'.format(pack))
    if warnings:
        print('\n  PROBLEMS WITH SOURCE AUDIO ({}):'.format(len(warnings)))
        for w in warnings:
            print('    ! ' + w)


if __name__ == '__main__':
    build(sys.argv[1] if len(sys.argv) > 1 else 'casual')
