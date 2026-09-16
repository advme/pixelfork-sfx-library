# STATUS

**Last updated:** 2026-09-17 · by **A (Claude)** · version **v0.3.0-A**

## Next task
**Publish it.** Create the public GitHub repo `advme/pixelfork-sfx-library`, push, tag `v0.3.0-A`,
turn on GitHub Pages, then check that the jsDelivr URLs in `AI-GUIDE.md`, `llms.txt` and
`README.md` actually load. Until that exists, no game can use the library.

## In progress
_Nothing._

## The pack is complete — 105 sounds, all playable
| Group | Sounds | Code | Audio |
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

**51 made by code** · **54 from generated audio** · **0 waiting**.
Primary bundle `casual.webm` is 891 KB (Opus, what nearly every browser loads);
`casual.m4a` fallback for older iOS is 1311 KB.

## Done
| # | Piece | Where | Version |
|---|-------|-------|---------|
| 1 | Runtime: load, play, pitch variation, voice cap, throttle | `src/sfx.js` | v0.1.0-A |
| 2 | Per-category mixer + mute, remembered between sessions | `src/sfx.js` | v0.1.0-A |
| 3 | iOS/Android audio unlock on first tap | `src/sfx.js` | v0.1.0-A |
| 4 | Music with crossfade + `SFX.duck()` | `src/sfx.js` | v0.1.0-A |
| 5 | Auto-wiring into the Super Casual UI Kit (`SFX.attach()`) | `src/sfx.js` | v0.1.0-A |
| 6 | Build pipeline: trim, normalize, sprite, webm + m4a | `tools/build_pack.py` | v0.1.0-A |
| 7 | Layered synth engine (osc / filtered noise / FM) | `src/sfx.js` | v0.2.0-A |
| 8 | Catalog of 105 sounds, each declaring how it is made | `packs/casual/registry.json` | v0.2.0-A |
| 9 | Tone shaping on the synthesis path only | `src/sfx.js` | v0.2.5-A |
| 10 | `postFx` repair: tighten, highpass, presence, bright | `tools/build_pack.py` | v0.2.5-A |
| 11 | ElevenLabs generator with level gate and auto-retry | `tools/generate_ai.py` | v0.2.2-A |
| 12 | Sequence mode: generate a real walk, cut it into takes | `tools/split_takes.py` | v0.2.8-A |
| 13 | All 54 audio sounds generated | `packs/casual/sounds/` | v0.3.0-A |
| 14 | Seamless looping (`postFx.loop`) + `SFX.stop()` | both | v0.3.0-A |
| 15 | Preview board with filters and per-sound audit | `tools/preview.html` | v0.2.3-A |

## Left
- **Publish** (see Next task).
- **Music.** Three short loops (menu, gameplay, tension). These stay separate streamed files,
  never in the sprite, and want a music model rather than a sound-effects one.
- **Test pages.** A `tools/tests/` runner like the UI kit has: every registry name resolves,
  sprite offsets land inside the file, nothing clips, the primary bundle stays under 1 MB.
- **Real phone check.** iPhone + Android: first-tap unlock, the iOS silent switch, music
  surviving a phone call.
- **Owner review.** Nothing in the pack has been judged by ear across the board yet; the
  measurements only prove no sound is silent, clipping, distant or dull.
- **Second pack.** The format already supports more than one — an `arcade` or `realistic`
  pack can reuse the whole runtime.

## Links
- Companion UI kit: `../Mobile Game UI Library` · https://advme.github.io/mobile-game-ui-library/
- Preview locally: `python3 tools/serve.py 8766`
