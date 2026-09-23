#!/usr/bin/env python3
"""
themes.py — which bundle each sound belongs to.

One 22-minute sprite meant every game downloaded 16.8 MB and decoded 258 MB of
audio into memory to play a button click. Safari on a phone is near its per-tab
memory limit at that point, which is why loading took minutes.

Sounds are bundled by THEME, not by category: 92% of the library is category
"game", so category splits nothing, while a racing game wants `car` and will
never want `casino`. A game loads `core` plus the one or two themes it needs.

`core` is what almost any game uses, so it is the default and stays small.
A sound's theme comes from its group (the part before the first dot); a
registry entry can override it with "theme": "...".
"""

THEMES = {
    'core':       'reward match pickup state game impact break coin object voice door',
    'casual':     'puzzle shop idle tower emote',
    'action':     'gun weapon melee explosion stealth',
    'vehicles':   'car moto truck race engine vehicle',
    'world':      'weather ambience water nature fire crowd',
    'animals':    'animal farm creature',
    'fantasy':    'magic rpg med',
    'scifi':      'scifi space',
    'horror':     'horror',
    'sports':     'sport',
    'casino':     'casino',
    'fishing':    'fish',
    'life':       'rest kitchen cook office phone machine tool craft build',
    'platformer': 'plat move step body',
    'holiday':    'holiday',
}

GROUP_THEME = {g: t for t, groups in THEMES.items() for g in groups.split()}
DEFAULT = 'core'


def theme_for(name, definition):
    """Theme of one sound. Registry 'theme' wins, then its group, then core."""
    if definition.get('theme'):
        return definition['theme']
    return GROUP_THEME.get(name.split('.')[0], DEFAULT)


def unknown_groups(names):
    """Groups no theme claims — they silently fall into core, so surface them."""
    seen = {}
    for n in names:
        g = n.split('.')[0]
        if g not in GROUP_THEME:
            seen[g] = seen.get(g, 0) + 1
    return seen
