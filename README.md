# Pixelfork SFX Library

Ready-made game sound effects for AI-generated web games. An AI picks a name; it never creates audio.
659 sounds (96 of them music) · 51 made by code, 608 real audio · pairs automatically with the Super Casual UI Kit.

## Use it in a game (no install)

```html
<script src="https://advme.github.io/pixelfork-sfx-library/dist/sfx.js"></script>
<script>SFX.load('casual'); SFX.attach();</script>

<script>SFX.play('coin.collect');</script>
```

### Themes: load only the sounds your game needs

The library is **15 themed bundles**, not one download. `SFX.load('casual')` fetches the index
(every sound's name and description) plus the small `core` bundle. Any other theme is fetched the
first time a sound from it is played, so the line above keeps working and stays small.

Name the themes up front when you know them — no wait on first play:

```js
SFX.load('casual', { themes: ['core', 'vehicles'] });   // a racing game
SFX.preload(['world', 'animals']);                      // later, e.g. on a loading screen
SFX.preload('all');                                     // everything (16 MB, avoid on phones)
```

| theme | sounds | size (m4a) |
|---|---|---|
| `vehicles` | 52 | 2151 KB |
| `world` | 41 | 2054 KB |
| `life` | 56 | 1887 KB |
| `casual` | 58 | 1598 KB |
| `platformer` | 46 | 1312 KB |
| `core` | 58 | 1266 KB |
| `fantasy` | 38 | 1148 KB |
| `action` | 45 | 1064 KB |
| `scifi` | 26 | 1019 KB |
| `animals` | 29 | 792 KB |
| `casino` | 14 | 518 KB |
| `sports` | 16 | 451 KB |
| `fishing` | 10 | 415 KB |
| `horror` | 12 | 400 KB |
| `holiday` | 11 | 372 KB |

Music is **never** bundled: each track streams on its own, and starts playing immediately
while it downloads.

### Why this matters on phones

One 22-minute sprite was 16.8 MB and became **258 MB of memory** once decoded. Safari decodes
one file at a time and took **78 seconds** on it, with music stuck in the queue behind it — games
were silent for over a minute. Loading `core` + one theme is about 2-3 MB and a few seconds.

- **AI guide (give this to your AI):** [AI-GUIDE.md](AI-GUIDE.md)
- **Hear every sound:** `python3 tools/serve.py 8766` → http://localhost:8766/tools/preview.html
- **Demo with the UI kit:** http://localhost:8766/demo/game.html

## For contributors / AI agents working on the library
Start with `AGENTS.md`, then `STATUS.md`.

## Licence

**Source-available, non-commercial.** Copyright (c) 2026 Pixelfork. All rights reserved.

You may view, fork, modify and use this for personal projects, learning and evaluation.
**You may not use it in anything commercial** — including free games that make money from
ads or in-app purchases — without a written commercial licence from Pixelfork.

See [LICENSE](LICENSE) for the full terms.
