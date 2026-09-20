# Pixelfork SFX Library

Ready-made game sound effects for AI-generated web games. An AI picks a name; it never creates audio.
403 sounds (30 of them music) · 51 made by code, 352 real audio · pairs automatically with the Super Casual UI Kit.

## Use it in a game (no install)

```html
<script src="https://advme.github.io/pixelfork-sfx-library/dist/sfx.js"></script>
<script>SFX.load('casual'); SFX.attach();</script>

<script>SFX.play('coin.collect');</script>
```

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
