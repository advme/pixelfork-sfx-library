#!/usr/bin/env python3
"""
fix_loop.py — find the crossfade length that makes a loop seamless.

    python3 tools/fix_loop.py music.comedy.2 casino.reel.spin
    python3 tools/fix_loop.py --all          check and fix every loop in the pack

A crossfade only works if it lands on the material's own period. For a klaxon,
a rotor, an engine or a piece of music that means the right overlap is specific
and cannot be guessed — 1.5s can be worse than 3s, which can be worse than 2s.

This tries several lengths against the SOURCE file and writes the best one into
registry.json -> postFx.loop. It never calls the generation API and never
rebuilds the whole pack, which is what makes it fast enough to run over every
loop at once.

A seam is only audible in tonal or rhythmic material; noise has large
sample-to-sample jumps of its own and nothing to phase-match. The score below
compares the jump at the wrap against the clip's own RMS, so a noisy sound that
reads high here is usually fine by ear — judge those by listening.
"""

import argparse
import json
import os
import subprocess
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SR = 48000
CANDIDATES = [0.5, 0.8, 1.2, 1.6, 2.0, 2.5, 3.0, 4.0, 5.0, 6.0]
GOOD = 1.5


def registry_path():
    return os.path.join(ROOT, 'packs', 'casual', 'registry.json')


def source_for(name, d):
    if d.get('music'):
        return os.path.join(ROOT, 'packs', 'casual', 'music', name + '.mp3')
    base = os.path.join(ROOT, 'packs', 'casual', 'sounds')
    for ext in ('.mp3', '.wav'):
        p = os.path.join(base, name + ext)
        if os.path.exists(p):
            return p
    return None


def decode(path, cross=None):
    """Decode, optionally wrapping the tail over the head by `cross` seconds."""
    if cross:
        cmd = ['ffmpeg', '-v', 'error', '-i', path, '-i', path, '-filter_complex',
               '[0:a]atrim=start={c}[a];[1:a]atrim=0:{c}[b];[a][b]acrossfade=d={c}[out]'.format(c=cross),
               '-map', '[out]']
    else:
        cmd = ['ffmpeg', '-v', 'error', '-i', path]
    cmd += ['-f', 'f32le', '-ac', '1', '-ar', str(SR), '-']
    return np.frombuffer(subprocess.run(cmd, capture_output=True).stdout, dtype=np.float32)


def seam_score(x):
    w = int(0.025 * SR)
    if len(x) < 3 * w:
        return None
    jump = float(np.abs(np.diff(np.concatenate([x[-w:], x[:w]]))).max())
    rms = float(np.sqrt((x ** 2).mean()))
    return jump / max(rms, 1e-9)


def best_crossfade(path, total):
    results = []
    for c in CANDIDATES:
        if c * 2.2 > total:        # keep a usable loop after the overlap is consumed
            continue
        x = decode(path, c)
        s = seam_score(x)
        if s is not None:
            results.append((s, c, len(x) / SR))
    return sorted(results)[0] if results else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('names', nargs='*')
    ap.add_argument('--all', action='store_true', help='check every loop in the pack')
    ap.add_argument('--dry-run', action='store_true')
    args = ap.parse_args()

    reg = json.load(open(registry_path()))
    S = reg['sounds']
    targets = ([n for n, d in S.items() if d.get('loopable')] if args.all else args.names)
    if not targets:
        sys.exit('Pass loop names, or --all.')

    changed, skipped, stuck = 0, 0, []
    for name in targets:
        d = S.get(name)
        if not d or not d.get('loopable'):
            print('{:<26} not a loop, skipped'.format(name)); continue
        src = source_for(name, d)
        if not src:
            print('{:<26} no source file'.format(name)); continue

        total = len(decode(src)) / SR
        before = seam_score(decode(src, (d.get('postFx') or {}).get('loop')))
        best = best_crossfade(src, total)
        if not best:
            print('{:<26} too short to loop'.format(name)); continue
        score, cross, loop_len = best

        if before is not None and before <= GOOD and score >= before:
            skipped += 1
            continue

        mark = 'ok' if score <= GOOD else 'best available'
        print('{:<26} {:>6.2f} -> {:>6.2f}  crossfade {:<4} loop {:.1f}s  {}'.format(
            name, before if before is not None else -1, score, cross, loop_len, mark))
        if score > GOOD:
            stuck.append(name)
        if not args.dry_run:
            fx = d.get('postFx') or {}
            fx['loop'] = cross
            d['postFx'] = fx
            changed += 1

    if changed and not args.dry_run:
        json.dump(reg, open(registry_path(), 'w'), indent=2)
        open(registry_path(), 'a').write('\n')
    print('\n{} updated, {} already good.'.format(changed, skipped))
    if stuck:
        print('Still above {} after every crossfade (judge these by ear, and regenerate a'
              ' longer source if they really do click): {}'.format(GOOD, ', '.join(stuck)))


if __name__ == '__main__':
    main()
