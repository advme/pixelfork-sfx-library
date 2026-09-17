# AGENTS.md — start here (for every AI agent)

This project is worked on by **several AI agents taking turns** (Claude, Codex/GPT, …).
You have **no memory of earlier sessions**. Everything you need is in this repo.

## 1. Before you do anything
1. Read **`STATUS.md`**: what is done, what is in progress, and the **next task**.
2. Read the last 3 entries of **`CHANGELOG.md`**: what the previous agent just did.
3. Skim **`packs/casual/registry.json`** — it is the source of truth for every sound.

## 2. The project
A **sound effects library** for the **Pixelfork AI Engine**, which generates hyper-casual and casual 2D/3D mobile web games.

The point of this library is that **an AI building a game should never spend time or tokens creating audio**. It writes `SFX.play('coin.collect')` and the sound is already there, already mixed, already the right length. The library is the companion to the **Super Casual UI Kit** (`../Mobile Game UI Library`) and wires itself into it automatically.

The owner is **non-technical**: explain results in short, plain language. **Work in small steps, one task at a time.** **End every reply with exactly one "Next task: …" line.**

## 3. Where things are
```
src/sfx.js                       ← THE RUNTIME (work here). Loading, playback, mixing,
                                   iOS unlock, pitch variation, music, ducking, UI-kit auto-wiring.
packs/casual/
  registry.json                  SOURCE OF TRUTH: every sound, what it is for, the synth
                                   stand-in, and the prompt used to generate the real audio.
  sounds/                        the real audio files, named after the sound
                                   (ui.tap.wav, or coin.collect.1.wav / .2.wav for variations)
  SOUND-PROMPTS.md               GENERATED checklist for the owner. Never edit by hand.
dist/                            BUNDLE games load (generated, never edit)
  sfx.js  casual.json  casual.webm  casual.m4a
tools/build_pack.py              rebuild dist/ after ANY change to src/ or packs/
tools/make_prompts.py            regenerate packs/<pack>/SOUND-PROMPTS.md from the registry
tools/make_guide.py              regenerate the sound table inside AI-GUIDE.md
tools/preview.html               listen to every sound and approve it (the owner uses this)
tools/serve.py                   local no-cache preview server
demo/game.html                   the library + the Super Casual UI Kit in a working game screen
AI-GUIDE.md                      what an AI building a game reads. Keep it honest.
```

## 4. How to add a sound (follow exactly)
1. Add an entry to `packs/casual/registry.json` with `source`, `category`, `whenToUse`, `tags`, `duration`, `gain`, `vary`, then **either** a `synth` recipe (source `code`) **or** a `prompt` (source `ai`), or both for `hybrid`. Copy the shape of an existing entry.
2. `python3 tools/make_prompts.py casual` — adds it to the owner's checklist.
3. `python3 tools/make_guide.py casual` — adds it to the AI guide table.
4. `python3 tools/build_pack.py casual` — rebuilds `dist/`.
5. Listen: `python3 tools/serve.py 8766`, open `http://localhost:8766/tools/preview.html`. Press **Check every sound makes noise** — nothing may be silent. A new `code` sound must land near the pack's loudness median (~0.30 peak on the master bus) and must not clip. Narrow-bandpass noise layers are the usual offender: they measure far quieter than they look on paper, so widen the Q and raise the gain until the meter agrees.
6. If it is a UI-kit moment, wire it in `attach()` in `src/sfx.js` and check it in `demo/game.html`.
7. Update **`STATUS.md`** and **`CHANGELOG.md`** (see §7).

## 5. Design rules (the owner approved these; never break them)
- **Every sound declares how it is made, in `registry.json → source`:**
  - `code` — synthesized by the runtime, permanently. No file, no download, infinite variation. Correct for sounds that are **synthetic by nature**: UI blips, lasers, coin chimes, whooshes, energy hums, jumps, pitch ladders. A recording would be *worse* here, because it cannot be repitched endlessly without sounding like a loop.
  - `ai` — a generated audio file. Correct for sounds carrying **real-world material texture**: footsteps, guns, glass, wood, water, fire, engines, voices, musical fanfares. No oscillator fakes these.
  - `hybrid` — a coded layer plus a generated layer.
  The test when adding a sound: *could this exist without a physical object making it?* If yes, it is `code`. If it needs a material, a throat or an instrument, it is `ai`.
- **Describe the source in a prompt; never ask for the tone.** Asking a generator for "bright",
  "sharp", "thin" or "piercing" reliably returns audio 20–40 dB too quiet — it happened on the
  pistol, `step.wood` and others. Naming what makes the sound ("hard leather shoes on a hollow
  wooden floor", "clay pot on tile") gets the same brightness at a usable level. Ask for a **loud,
  close** recording and add any lift with `postFx.bright` / `postFx.presence`. "Distant" is the same
  trap in reverse: it returns the dull, reverberant sound that reads as a cheap microphone.
- **Sounds that repeat should be generated as one real sequence and cut up.** A generator asked for
  "a single footstep" still has to fill the API's 0.5s floor and returns several crammed together.
  Give the sound a `sequence` block instead: `generate_ai.py` makes one 3-second recording and
  `tools/split_takes.py` cuts it into takes. Every take is then a genuinely different footfall, and
  it costs one generation instead of five. The source recordings are kept in
  `packs/<pack>/sounds/_seq/` **and committed**, so takes can be re-cut later without
  paying to regenerate them — that is the whole point of keeping them.
- **Never give a `code` sound a prompt, and never leave an `ai` sound without one.** The merge script validates this; `build_pack.py` will not call a `code` sound "missing".
- **Style:** modern mobile casual — clean, bright, punchy, dry. Not retro/8-bit, not cinematic/orchestral. The house style lives in `registry.json → style`; the prompts must stay consistent with it.
- **Short.** UI sounds under 0.2s, pickups under 0.25s, only win/lose/chest go past 1s. A long sound in a game that fires it 40 times a minute is a bug.
- **Mono, dry, peak-normalized to −1 dBFS.** `build_pack.py` does the normalizing; do not pre-bake reverb tails.
- **Anything the player hears many times needs 3 variations** (`coin.collect.1.wav`, `.2.wav`, `.3.wav`) so it does not turn into a machine gun.
- **Names are a contract.** `category.thing` in lower case. Once a name ships, renaming it breaks every game that uses it — add an alias instead.
- **Never play audio before the player's first tap.** Browsers block it. The runtime unlocks itself; do not work around this.
- **Never let a missing sound throw.** Unknown names warn once and fall back to a stand-in.
- **No size limit.** Collect as many sounds as the library usefully needs. If a pack ever gets
  big enough to hurt load time, split it into a second pack — never drop sounds for size.
- **A sound that must loop needs `postFx.loop`.** A generator never returns a seamless loop — its first and last samples are unrelated, so playing it round clicks every cycle. `loop` wraps the tail over the head by the given number of seconds. Tonal material (an engine) needs a much longer overlap than noisy material (fire): 1.2s against 0.6s here. Verify by comparing the sample-to-sample jump at the wrap against a normal moment mid-clip; they should be about equal.

## 6. Git workflow
- Work on `main` in small commits. Don't rewrite history.
- `dist/` **is committed** — that is what jsDelivr serves.
- After publishing, update the pinned tag in `AI-GUIDE.md`, `llms.txt` and `README.md`.

## 7. Handoff protocol (REQUIRED after every task)
When you finish a task (or are about to run out of budget), **before stopping**:
1. **`STATUS.md`** — move the task to Done (with its version), put anything unfinished under **In progress** with exact notes, set **Next task** to the single next step, update the **Last updated** line.
2. **`CHANGELOG.md`** — add an entry at the top, format in §8.
3. **Commit and publish** using the version name from §8.

If you stop mid-task, still commit with `WIP` in the message and describe the exact state under **In progress**.

## 8. Version names — agent letter is REQUIRED
Every published update gets **`vMAJOR.MINOR.PATCH-<LETTER>`**

| Letter | Agent |
|--------|-------|
| **A**  | Claude (Anthropic) |
| **B**  | Codex / GPT (OpenAI) |

- **MINOR +1** for new sounds or a new runtime feature. **PATCH +1** for fixes.
- The number keeps counting across agents.
- Keep `registry.json → version` and `src/sfx.js → VERSION` equal to the number (without the letter).

```bash
git add -A
git commit -m "v0.2.0-A: real audio for the 14 core sounds"
git tag v0.2.0-A
git push origin main --tags
```

**CHANGELOG entry format:**
```markdown
## v0.2.0-A — real audio for the core sounds
- Agent: A (Claude) · Date: 2026-09-16
- Done: what was built/fixed, in plain language
- Tested: what was checked and how
- Notes for next agent: anything surprising, open issues
```
