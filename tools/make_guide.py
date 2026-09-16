#!/usr/bin/env python3
"""
make_guide.py — refresh the sound table inside AI-GUIDE.md from the registry.

    python3 tools/make_guide.py casual

Run this after adding or renaming a sound, so the guide an AI reads can never
disagree with the pack it loads.
"""
import json, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
START, END = '<!-- SOUNDS:START -->', '<!-- SOUNDS:END -->'


def main(pack):
    with open(os.path.join(ROOT, 'packs', pack, 'registry.json')) as fh:
        reg = json.load(fh)

    groups = {}
    for name, d in reg['sounds'].items():
        groups.setdefault(name.split('.')[0], []).append((name, d))

    rows = []
    for prefix in sorted(groups):
        rows.append('')
        rows.append('**`{}.*`**'.format(prefix))
        rows.append('')
        rows.append('| Sound | Play it when | Made by |')
        rows.append('|---|---|---|')
        for name, d in sorted(groups[prefix]):
            rows.append('| `{}` | {} | {} |'.format(name, d.get('whenToUse', ''), d.get('source', '?')))

    table = '\n'.join(rows)
    guide_path = os.path.join(ROOT, 'AI-GUIDE.md')
    guide = open(guide_path).read()
    head, _, rest = guide.partition(START)
    _, _, tail = rest.partition(END)
    open(guide_path, 'w').write(head + START + '\n' + table + '\n' + END + tail)
    print('AI-GUIDE.md sound table refreshed ({} sounds).'.format(len(reg['sounds'])))


if __name__ == '__main__':
    main(sys.argv[1] if len(sys.argv) > 1 else 'casual')
