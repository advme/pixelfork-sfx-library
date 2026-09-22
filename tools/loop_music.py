#!/usr/bin/env python3
"""
loop_music.py — cut a seamless loop out of a generated music track.

    python3 tools/loop_music.py music.casual.1        one track, report only
    python3 tools/loop_music.py --all --write         every loopable track, save

Why the old way failed. fix_loop.py wraps a clip's tail over its head with a
long crossfade. That is fine for noise and engines, but on music it plays two
unrelated passages on top of each other for up to six seconds: two drum
patterns out of phase, two chords at once. The wrap is click-free and still
sounds broken.

A music loop has to be CUT, not blended. The loop must end at a moment where the
music is about to play exactly what it played at the loop's start: same place
in the bar, same chord, same groove. This searches every (start, length) pair
for the one where the track, around the cut, sounds most like itself around the
start — over several seconds of context, so beat and harmony both have to line
up — then snaps the cut to the sample and joins it with a short crossfade.

The score is the feature distance across the wrap divided by the typical
distance between two unrelated moments of the same track. 0 is a perfect
repeat; 1 is no better than a random jump. Under 0.35 is inaudible on the
tracks here; over 0.6 is a stumble.

Writes registry.json -> postFx.loopRegion = [start_s, length_s]. build_pack.py
cuts the loop from that. No API calls.
"""

import argparse
import json
import os
import subprocess
import sys

import numpy as np

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REGISTRY = os.path.join(ROOT, 'packs', 'casual', 'registry.json')
MUSIC_DIR = os.path.join(ROOT, 'packs', 'casual', 'music')

ASR = 22050          # analysis rate
HOP = 256            # ~11.6 ms per frame
NFFT = 2048
CONTEXT = 2.5        # seconds either side of the cut that must match
XFADE = 0.04         # seconds; the join itself, after sample alignment
MIN_FRACTION = 0.5   # a loop is at least half the usable track
GOOD, BAD = 0.35, 0.6


def decode(path, sr, channels):
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', path, '-f', 'f32le',
                          '-ac', str(channels), '-ar', str(sr), '-'],
                         capture_output=True, check=True).stdout
    x = np.frombuffer(raw, dtype=np.float32)
    return x.reshape(-1, channels) if channels > 1 else x


def features(x):
    """Per-frame timbre (log band energies) + harmony (chroma), standardized."""
    n = 1 + (len(x) - NFFT) // HOP
    idx = np.arange(NFFT)[None, :] + HOP * np.arange(n)[:, None]
    spec = np.abs(np.fft.rfft(x[idx] * np.hanning(NFFT), axis=1)) ** 2
    freqs = np.fft.rfftfreq(NFFT, 1 / ASR)

    edges = np.geomspace(50, 10000, 25)
    bands = np.stack([spec[:, (freqs >= lo) & (freqs < hi)].sum(1)
                      for lo, hi in zip(edges[:-1], edges[1:])], 1)
    bands = np.log(bands + 1e-9)

    sel = (freqs > 65) & (freqs < 4000)
    pc = np.round(12 * np.log2(freqs[sel] / 440.0)).astype(int) % 12
    chroma = np.zeros((n, 12))
    for k in range(12):
        chroma[:, k] = spec[:, sel][:, pc == k].sum(1)
    chroma = np.log(chroma + 1e-9)

    # Onset strength (spectral flux) carries the groove.
    flux = np.maximum(np.diff(bands, axis=0, prepend=bands[:1]), 0).sum(1, keepdims=True)

    F = np.hstack([bands, chroma, flux * 3])
    F = (F - F.mean(0)) / (F.std(0) + 1e-9)
    rms = np.sqrt(spec.sum(1))
    return F, rms


def usable_range(rms):
    """Skip a quiet intro and a fade-out: the loop must live in the full-level body."""
    ref = np.median(rms)
    loud = np.where(rms > 0.35 * ref)[0]
    return int(loud[0]), int(loud[-1])


def find_loop(path):
    x = decode(path, ASR, 1)
    F, rms = features(x)
    n = len(F)
    fps = ASR / HOP
    W = int(CONTEXT * fps)
    lo, hi = usable_range(rms)

    # Typical distance between unrelated moments, for normalizing.
    rng = np.random.default_rng(0)
    a, b = rng.integers(0, n, 4000), rng.integers(0, n, 4000)
    base = np.mean((F[a] - F[b]) ** 2)

    body = hi - lo
    Lmin = max(int(MIN_FRACTION * body), int(8 * fps))
    Lmax = body - 2 * W
    best = []
    for L in range(Lmin, Lmax + 1):
        d = np.mean((F[:n - L] - F[L:]) ** 2, axis=1)          # d[t]: t vs t+L
        c = np.concatenate([[0], np.cumsum(d)])
        s = np.arange(lo + W, hi - L - W)                     # cut context inside body
        if len(s) == 0:
            continue
        score = (c[s + W] - c[s - W]) / (2 * W) / base
        i = int(np.argmin(score))
        best.append((float(score[i]), int(s[i]), L))
    if not best:
        return None

    top = min(b[0] for b in best)
    # Among near-best, take the longest: a longer loop repeats less often.
    score, s, L = max((b for b in best if b[0] <= top * 1.25), key=lambda b: b[2])
    start, length = s * HOP / ASR, L * HOP / ASR
    return {'start': start, 'length': length, 'score': score,
            'track': len(x) / ASR, 'fps': fps, 'F': F, 'base': base}


def old_score(info, cross):
    """Score the previous tail-over-head crossfade on the same scale."""
    F, fps, base = info['F'], info['fps'], info['base']
    n = len(F)
    c = int(cross * fps)
    L = n - c                                   # a[t] is heard over a[t + n - c]
    d = np.mean((F[:c] - F[L:L + c]) ** 2, axis=1) if c else np.array([1.0 * base])
    return float(np.mean(d) / base)


def render(src, dst, start, length, sr=48000):
    """Cut [start, start+length), snap the end to the sample, crossfade the join. Stereo."""
    a = decode(src, sr, 2)
    s, L = int(round(start * sr)), int(round(length * sr))
    X = int(XFADE * sr)

    # Snap: find the lag where the audio after the cut best matches the loop start.
    mono = a.mean(1)
    ref = mono[s:s + 4096]
    span = int(0.012 * sr)
    best, bestc = 0, -np.inf
    for k in range(-span, span + 1):
        seg = mono[s + L + k:s + L + k + 4096]
        if len(seg) < 4096:
            continue
        cc = float(np.dot(ref, seg) / (np.linalg.norm(ref) * np.linalg.norm(seg) + 1e-9))
        if cc > bestc:
            best, bestc = k, cc
    L += best
    if s + L + X > len(a):
        L = len(a) - X - s

    loop = a[s:s + L].copy()
    t = np.linspace(0, 1, X)[:, None]
    fade_in, fade_out = np.sin(t * np.pi / 2), np.cos(t * np.pi / 2)
    # At i=0 the loop continues exactly where its end left off (a[s+L]).
    loop[:X] = a[s + L:s + L + X] * fade_out + a[s:s + X] * fade_in

    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(sr), '-ac', '2',
                    '-i', '-', '-c:a', 'pcm_s16le', dst],
                   input=loop.astype(np.float32).tobytes(), check=True)
    return L / sr, bestc


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('names', nargs='*')
    ap.add_argument('--all', action='store_true')
    ap.add_argument('--write', action='store_true', help='save loopRegion into registry.json')
    args = ap.parse_args()

    reg = json.load(open(REGISTRY))
    sounds = reg['sounds'] if 'sounds' in reg else reg
    names = args.names or [n for n, d in sounds.items() if d.get('music') and d.get('loopable')]

    rows = []
    for name in names:
        src = os.path.join(MUSIC_DIR, name + '.mp3')
        if not os.path.exists(src):
            print('{:28s} no source'.format(name)); continue
        info = find_loop(src)
        if not info:
            print('{:28s} too short to loop'.format(name)); continue
        before = old_score(info, float((sounds[name].get('postFx') or {}).get('loop') or 0))
        verdict = 'ok' if info['score'] < GOOD else ('check' if info['score'] < BAD else 'BAD')
        print('{:28s} {:5.1f}s of {:4.1f}s from {:5.2f}s   score {:.2f} (was {:.2f})  {}'.format(
            name, info['length'], info['track'], info['start'], info['score'], before, verdict))
        rows.append((name, info, before))
        if args.write:
            fx = sounds[name].setdefault('postFx', {})
            fx.pop('loop', None)
            fx['loopRegion'] = [round(info['start'], 4), round(info['length'], 4)]

    if args.write:
        with open(REGISTRY, 'w') as f:
            json.dump(reg, f, indent=2, ensure_ascii=False)
            f.write('\n')
    if rows:
        sc = [r[1]['score'] for r in rows]
        was = [r[2] for r in rows]
        print('\n{} tracks   median score {:.2f} (was {:.2f})   ok {}  check {}  BAD {}'.format(
            len(rows), np.median(sc), np.median(was),
            sum(s < GOOD for s in sc), sum(GOOD <= s < BAD for s in sc), sum(s >= BAD for s in sc)))


if __name__ == '__main__':
    main()
