# Pixelfork SFX Library

Ready-made game sound effects for AI-generated web games. An AI picks a name; it never creates audio.
403 sounds (30 of them music) · 51 made by code, 352 real audio · pairs automatically with the Super Casual UI Kit.

## Use it in a game (no install)

```html
<script src="https://cdn.jsdelivr.net/gh/advme/pixelfork-sfx-library@v0.6.0-A/dist/sfx.js"></script>
<script>SFX.load('casual'); SFX.attach();</script>

<script>SFX.play('coin.collect');</script>
```

- **AI guide (give this to your AI):** [AI-GUIDE.md](AI-GUIDE.md)
- **Hear every sound:** `python3 tools/serve.py 8766` → http://localhost:8766/tools/preview.html
- **Demo with the UI kit:** http://localhost:8766/demo/game.html

## For contributors / AI agents working on the library
Start with `AGENTS.md`, then `STATUS.md`.
