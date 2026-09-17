# STATUS

**Last updated:** 2026-09-17 · by **A (Claude)** · version **v0.5.0-A**

## Next task
**Listen through the board and flag what is wrong.** Nothing in the pack has been judged by
ear across the board. Every check so far only proves no sound is silent, clipping, distant,
dull or seamed — not that it sounds right. Use the loop buttons on the 42 loops in
particular, since seams in noisy material cannot be measured, only heard.

After that: **publish**. Create `advme/pixelfork-sfx-library`, push, tag, turn on Pages, and
check the jsDelivr URLs in `AI-GUIDE.md`, `llms.txt` and `README.md` load.

## In progress
_Nothing._

## The pack — 373 sounds, all playable
| Group | Sounds |
|---|---|
| `ambience.*` | 7 |
| `animal.*` | 22 |
| `break.*` | 4 |
| `car.*` | 30 |
| `coin.*` | 2 |
| `cook.*` | 6 |
| `craft.*` | 2 |
| `creature.*` | 4 |
| `crowd.*` | 3 |
| `door.*` | 9 |
| `engine.*` | 2 |
| `explosion.*` | 2 |
| `farm.*` | 3 |
| `fire.*` | 6 |
| `game.*` | 8 |
| `gun.*` | 15 |
| `horror.*` | 12 |
| `impact.*` | 7 |
| `kitchen.*` | 8 |
| `machine.*` | 4 |
| `magic.*` | 19 |
| `match.*` | 5 |
| `melee.*` | 10 |
| `moto.*` | 3 |
| `move.*` | 10 |
| `nature.*` | 2 |
| `object.*` | 15 |
| `office.*` | 3 |
| `phone.*` | 2 |
| `pickup.*` | 7 |
| `race.*` | 4 |
| `reward.*` | 4 |
| `rpg.*` | 10 |
| `scifi.*` | 14 |
| `sport.*` | 16 |
| `state.*` | 6 |
| `step.*` | 15 |
| `tool.*` | 7 |
| `truck.*` | 3 |
| `ui.*` | 16 |
| `vehicle.*` | 10 |
| `voice.*` | 7 |
| `water.*` | 8 |
| `weapon.*` | 15 |
| `weather.*` | 6 |

**51 made by code** · **322 from generated audio** · **0 waiting** ·
42 seamless loops · 144 with multiple takes · 23 cut from real sequences.
Bundle: `casual.webm` 6484 KB · `casual.m4a` 10068 KB.

## Done
| Piece | Where | Version |
|-------|-------|---------|
| Runtime: play, pitch variation, voice cap, mixer, mute, iOS unlock | `src/sfx.js` | v0.1.0-A |
| Auto-wiring into the Super Casual UI Kit | `src/sfx.js` | v0.1.0-A |
| Layered synth engine (osc / noise / FM) | `src/sfx.js` | v0.2.0-A |
| Tone shaping on the synthesis path only | `src/sfx.js` | v0.2.5-A |
| `postFx` repair: tighten, highpass, presence, bright, loop | `tools/build_pack.py` | v0.2.5-A |
| ElevenLabs generator with level gate and auto-retry | `tools/generate_ai.py` | v0.2.2-A |
| Sequence mode: generate one real take, cut it into takes | `tools/split_takes.py` | v0.2.8-A |
| Seamless looping + `SFX.play({loop})` + `SFX.stop()` | both | v0.3.0-A |
| Preview board: filters, per-sound loop buttons, audit | `tools/preview.html` | v0.4.0-A |
| Catalog grown 14 -> 373 | `packs/casual/registry.json` | v0.5.0-A |

## Left
- **Owner review by ear** (see Next task).
- **Publish** to GitHub so games can load it.
- **Music.** Menu / gameplay / tension loops. These want a music model, not a
  sound-effects one, and stay separate streamed files rather than going in the sprite.
- **Test pages.** A `tools/tests/` runner: every registry name resolves, sprite offsets land
  inside the file, nothing clips, every loop is checked.
- **Real phone check.** iPhone + Android: first-tap unlock, the iOS silent switch.
- **Pack size.** 6484 KB is a real download for a mobile web game. The runtime already
  merges several packs into one namespace, so splitting into themed packs would need no
  game-code change.

## Links
- Companion UI kit: `../Mobile Game UI Library`
- Preview locally: `python3 tools/serve.py 8766`
