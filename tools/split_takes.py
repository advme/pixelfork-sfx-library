#!/usr/bin/env python3
"""
split_takes.py — cut one long recording into individual takes.

    python3 tools/split_takes.py step.metal packs/casual/sounds/_seq/step.metal.mp3 5

Some sounds are far better generated as a real sequence than one at a time: a
generator asked for "a single footstep" has to fill the API's half-second floor
and tends to return several steps crammed together, while a 3-second walk comes
out natural and gives a different step every time for free.

This finds each hit in the recording and writes it out as its own take, so the
library still plays ONE footstep per call.

Used automatically by generate_ai.py for any sound with a "sequence" block in
the registry; can also be run by hand on a file you recorded yourself.
"""

import os
import subprocess
import sys

import numpy as np

SR = 48000
HOP = 256


def decode(path):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-f', 'f32le',
                          '-ac', '1', '-ar', str(SR), '-'], capture_output=True).stdout
    return np.frombuffer(raw, dtype=np.float32).copy()


def envelope(x):
    n = max(1, (len(x) - HOP) // HOP)
    return np.array([np.sqrt((x[i*HOP:(i+1)*HOP]**2).mean()) for i in range(n)])


def find_hits(x, want, min_gap_ms=140):
    """Find EVERY hit in the recording, then pick which ones to keep.

    Returns (chosen, all_hits). Both matter: `chosen` are the takes we want,
    but the cut has to end at the next hit in `all_hits`, not the next chosen
    one — otherwise a quieter step between two loud ones gets swallowed into
    the take before it, and that take then contains two footsteps.
    """
    e = envelope(x)
    if len(e) < 3 or e.max() <= 0:
        return [], []
    rise = np.diff(e, prepend=e[0])
    rise[rise < 0] = 0
    if rise.max() <= 0:
        return [], []
    gap = max(1, int(min_gap_ms / 1000 * SR / HOP))

    # Go down to a low threshold so weak hits are found too, then stop as soon
    # as more hits appear than we asked for.
    best = []
    for frac in (0.45, 0.35, 0.25, 0.18, 0.12, 0.08, 0.05):
        thr = rise.max() * frac
        hits, last = [], -10**9
        for i, v in enumerate(rise):
            if v > thr and e[i] > e.max() * 0.10 and i - last > gap:
                hits.append((i, float(v)))
                last = i
        if len(hits) > len(best):
            best = hits
        if len(hits) >= want + 1:
            break
    if not best:
        return [], []

    all_hits = sorted(i for i, _ in best)
    strongest = sorted(best, key=lambda h: -h[1])[:want]
    chosen = sorted(i for i, _ in strongest)
    return chosen, all_hits


def write_take(x, start, end, out_path):
    seg = x[max(0, start): end].astype(np.float32)
    if len(seg) < 256:
        return False
    # normalize, then fade the edges so a slice can never click
    peak = float(np.abs(seg).max())
    if peak > 0:
        seg = seg * (10 ** (-1.0 / 20) / peak)
    fi, fo = int(0.003 * SR), int(0.020 * SR)
    fo = min(fo, len(seg) // 3)
    if fi < len(seg):
        seg[:fi] *= np.linspace(0, 1, fi)
    if fo > 0:
        seg[-fo:] *= np.linspace(1, 0, fo)
    p = subprocess.run(['ffmpeg', '-y', '-v', 'error', '-f', 'f32le', '-ar', str(SR),
                        '-ac', '1', '-i', 'pipe:0', '-c:a', 'pcm_s16le', out_path],
                       input=seg.tobytes(), capture_output=True)
    return p.returncode == 0


def split(name, src, want, out_dir, pre_ms=18, max_ms=380):
    x = decode(src)
    if not len(x):
        sys.exit('Could not decode ' + src)
    chosen, all_hits = find_hits(x, want)
    if not chosen:
        sys.exit('No hits found in ' + src)

    written = []
    for k, h in enumerate(chosen):
        start = int(h * HOP - pre_ms / 1000 * SR)
        # End at the very next hit of ANY strength, so no take can hold two.
        later = [a for a in all_hits if a > h]
        nxt = later[0] * HOP if later else len(x)
        end = int(min(nxt - 0.012 * SR, start + max_ms / 1000 * SR, len(x)))
        out = os.path.join(out_dir, '{}.{}.wav'.format(name, k + 1))
        if write_take(x, start, end, out):
            written.append((out, (end - start) / SR))
    return written, len(x) / SR


if __name__ == '__main__':
    if len(sys.argv) < 4:
        sys.exit(__doc__)
    name, src, want = sys.argv[1], sys.argv[2], int(sys.argv[3])
    out_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
                           'packs', 'casual', 'sounds')
    takes, total = split(name, src, want, out_dir)
    print('Split {:.2f}s into {} takes:'.format(total, len(takes)))
    for p, d in takes:
        print('  {:<44} {:.3f}s'.format(os.path.basename(p), d))
