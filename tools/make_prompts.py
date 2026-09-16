#!/usr/bin/env python3
"""
make_prompts.py — write SOUND-PROMPTS.md from the pack registry.

    python3 tools/make_prompts.py casual

The registry is the single source of truth. This turns it into a checklist the
owner can work through in an AI sound generator (ElevenLabs Sound Effects,
Stable Audio, …), copying one prompt at a time.
"""

import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def main(pack):
    pack_dir = os.path.join(ROOT, 'packs', pack)
    with open(os.path.join(pack_dir, 'registry.json')) as fh:
        reg = json.load(fh)

    have = set()
    sounds_dir = os.path.join(pack_dir, 'sounds')
    if os.path.isdir(sounds_dir):
        for f in os.listdir(sounds_dir):
            stem = os.path.splitext(f)[0]
            have.add(stem.rsplit('.', 1)[0] if stem.rsplit('.', 1)[-1].isdigit() else stem)

    lines = [
        '# Sound prompts — {}'.format(reg['title']),
        '',
        '_Generated from `packs/{}/registry.json` by `tools/make_prompts.py`. Do not edit by hand —'.format(pack),
        'edit the registry and run the tool again._',
        '',
        '## How to use this',
        '',
        '1. Open your AI sound generator (ElevenLabs Sound Effects, Stable Audio, …).',
        '2. Copy a prompt below, generate it, and pick the best take.',
        '3. Save it as `packs/{}/sounds/<name>.wav` — the file name **must** match the'.format(pack),
        '   sound name exactly (`ui.tap.wav`). For several takes of the same sound use',
        '   `coin.collect.1.wav`, `coin.collect.2.wav`, … and the game will vary them automatically.',
        '4. Run `python3 tools/build_pack.py {}` and listen on the preview page.'.format(pack),
        '',
        '**House style (put this in the generator if it has a style field):**',
        '',
        '> ' + reg.get('style', ''),
        '',
        '**Progress: {} of {} sounds delivered.**'.format(len(have & set(reg['sounds'])), len(reg['sounds'])),
        '',
    ]

    by_cat = {}
    for name, d in reg['sounds'].items():
        by_cat.setdefault(d.get('category', 'ui'), []).append((name, d))

    for cat in sorted(by_cat):
        lines += ['## {}'.format(cat), '']
        for name, d in by_cat[cat]:
            mark = 'x' if name in have else ' '
            takes = d.get('variationsWanted')
            lines += [
                '- [{}] **`{}`** — {}'.format(mark, name, d.get('whenToUse', '')),
                '  - Target length: ~{}s{}'.format(
                    d.get('duration', '?'),
                    ' · generate **{} takes** (`{}.1.wav`, `{}.2.wav`, …)'.format(takes, name, name) if takes else ''),
                '  - Prompt: `{}`'.format(d.get('prompt', '—')),
                '',
            ]

    out = os.path.join(pack_dir, 'SOUND-PROMPTS.md')
    with open(out, 'w') as fh:
        fh.write('\n'.join(lines))
    print('Wrote {} ({} prompts, {} already delivered).'.format(
        os.path.relpath(out, ROOT), len(reg['sounds']), len(have & set(reg['sounds']))))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'casual')
