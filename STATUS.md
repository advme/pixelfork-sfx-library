# STATUS

**Last updated:** 2026-09-16 · by **A (Claude)** · version **v0.2.1-A**

## Next task
**Generate the 54 sounds that need real audio.** Open `packs/casual/SOUND-PROMPTS.md` — it lists only those, with a tuned prompt and the exact filename for each. Work down it in ElevenLabs Sound Effects, saving to `packs/casual/sounds/`. Start with the ones a game uses most: `state.win`, `state.lose`, `reward.chest`, the eight `step.*` surfaces, then `break.*` and `weapon.pistol`. Run `python3 tools/build_pack.py casual` as you go and listen on the preview board. The other 51 sounds are finished and need nothing.

## In progress
_Nothing._

## The catalog — 105 sounds
| Group | Sounds | Code | Need audio |
|---|---|---|---|
| `break.*` | 4 | 0 | 4 |
| `coin.*` | 2 | 2 | 0 |
| `door.*` | 2 | 0 | 2 |
| `engine.*` | 2 | 0 | 2 |
| `explosion.*` | 2 | 1 | 1 |
| `fire.*` | 1 | 0 | 1 |
| `impact.*` | 7 | 3 | 4 |
| `magic.*` | 7 | 5 | 2 |
| `match.*` | 5 | 3 | 2 |
| `move.*` | 10 | 7 | 3 |
| `pickup.*` | 7 | 5 | 2 |
| `reward.*` | 4 | 2 | 2 |
| `state.*` | 6 | 1 | 5 |
| `step.*` | 8 | 0 | 8 |
| `ui.*` | 16 | 16 | 0 |
| `vehicle.*` | 2 | 0 | 2 |
| `voice.*` | 4 | 0 | 4 |
| `water.*` | 1 | 0 | 1 |
| `weapon.*` | 15 | 6 | 9 |

**51 made by code** (final, no file, no download) · **54 need generated audio** (118 files including variations).

## Done
| # | Piece | Where | Version |
|---|-------|-------|---------|
| 1 | Runtime: load, play, pitch variation, voice cap, throttle | `src/sfx.js` | v0.1.0-A |
| 2 | Per-category mixer + mute, remembered between sessions | `src/sfx.js` | v0.1.0-A |
| 3 | iOS/Android audio unlock on first tap | `src/sfx.js` | v0.1.0-A |
| 4 | Music with crossfade + `SFX.duck()` | `src/sfx.js` | v0.1.0-A |
| 5 | Auto-wiring into the Super Casual UI Kit (`SFX.attach()`) | `src/sfx.js` | v0.1.0-A |
| 6 | Build pipeline: trim, normalize, sprite, webm + m4a | `tools/build_pack.py` | v0.1.0-A |
| 7 | Layered synth engine (osc / filtered noise / FM, multi-layer, arpeggio) | `src/sfx.js` | v0.2.0-A |
| 8 | Full catalog of 105 sounds, each declaring how it is made | `packs/casual/registry.json` | v0.2.0-A |
| 9 | 51 finished code sounds, loudness-calibrated | `packs/casual/registry.json` | v0.2.0-A |
| 10 | Source-aware tooling (prompts list only what needs audio) | `tools/` | v0.2.0-A |
| 11 | Preview board with per-sound audit | `tools/preview.html` | v0.2.0-A |

## Left — after the audio arrives
- **Music.** 3 short loops (menu, gameplay, tension). These stay separate streamed files, never in the sprite. A music model, not a sound-effects model.
- **Ambience loops.** `fire.crackle` and `engine.loop` are marked loopable but nothing yet checks they loop seamlessly — a generated file almost never does. Needs a crossfade-loop step in `build_pack.py`.
- **Publish.** Create the public GitHub repo `advme/pixelfork-sfx-library`, push, tag, turn on Pages, then check the jsDelivr URLs in `AI-GUIDE.md`, `llms.txt` and `README.md` load.
- **Test pages.** A `tools/tests/` runner like the UI kit has: every registry name resolves, sprite offsets land inside the file, nothing clips, the pack stays under 1 MB.
- **Real phone check.** iPhone + Android: first-tap unlock, the iOS silent switch, music surviving a phone call.
- **Second pack.** The registry format supports more than one pack — an `arcade` or `realistic` pack can reuse the whole runtime.

## Links
- Companion UI kit: `../Mobile Game UI Library` · https://advme.github.io/mobile-game-ui-library/
- Preview locally: `python3 tools/serve.py 8766`
