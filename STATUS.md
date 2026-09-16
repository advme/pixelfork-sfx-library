# STATUS

**Last updated:** 2026-09-16 · by **A (Claude)** · version **v0.1.0-A**

## Next task
**Generate the real audio for the 14 core sounds.** Open `packs/casual/SOUND-PROMPTS.md`, work down the checklist in an AI sound generator (ElevenLabs Sound Effects or similar), and save each result as `packs/casual/sounds/<name>.wav`. For `coin.collect` save 3 takes (`coin.collect.1.wav`, `.2.wav`, `.3.wav`). Then run `python3 tools/build_pack.py casual` and listen to the whole board on `tools/preview.html`. Replace anything that sounds wrong before publishing `v0.2.0-A`.

## In progress
_Nothing._

## Done
| # | Piece | Where | Version |
|---|-------|-------|---------|
| 1 | Runtime: load, play, pitch variation, voice cap, throttle | `src/sfx.js` | v0.1.0-A |
| 2 | Per-category mixer + mute, remembered between sessions | `src/sfx.js` | v0.1.0-A |
| 3 | iOS/Android audio unlock on first tap | `src/sfx.js` | v0.1.0-A |
| 4 | Music with crossfade + `SFX.duck()` | `src/sfx.js` | v0.1.0-A |
| 5 | Built-in synth stand-ins (nothing is ever silent) | `src/sfx.js` | v0.1.0-A |
| 6 | Auto-wiring into the Super Casual UI Kit (`SFX.attach()`) | `src/sfx.js` | v0.1.0-A |
| 7 | Pack registry with 14 sounds + generation prompts | `packs/casual/registry.json` | v0.1.0-A |
| 8 | Build pipeline: trim, normalize, sprite, webm + m4a | `tools/build_pack.py` | v0.1.0-A |
| 9 | Generated prompt checklist and AI-guide table | `tools/make_prompts.py`, `tools/make_guide.py` | v0.1.0-A |
| 10 | Listening/approval board | `tools/preview.html` | v0.1.0-A |
| 11 | Working demo with the UI kit | `demo/game.html` | v0.1.0-A |

## Left — after the core 14 sounds
- **Grow the pack to ~120 sounds**, in this order: rest of `ui.*` (swipe, page, unlock, notify) → `game.*` (jump, land, hit, break, shoot, dash, splash, step) → `match.*` (pop, combo1–5, cascade, shuffle) → `state.*` (level-up, countdown, game-over) → `feedback.*` (correct, wrong, warning, boost).
- **Music.** 3 short loops (menu, gameplay, tension). These stay separate streamed files, never in the sprite.
- **Publish.** Create the public GitHub repo `advme/pixelfork-sfx-library`, push, tag, turn on Pages, then check the jsDelivr URLs in `AI-GUIDE.md`, `llms.txt` and `README.md` actually load.
- **Test pages.** A `tools/tests/` runner like the UI kit has, checking: every registry name resolves, the sprite offsets land inside the file, no sound clips, the pack stays under 1 MB.
- **Real phone check.** iPhone + Android: does the first tap unlock audio, does the silent switch behave, does music survive a phone call.

## Links
- Companion UI kit: `../Mobile Game UI Library` · https://advme.github.io/mobile-game-ui-library/
- Preview locally: `python3 tools/serve.py 8766`
