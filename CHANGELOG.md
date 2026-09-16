# CHANGELOG

## v0.3.0-A — the pack is complete: all 54 audio sounds generated
- Agent: A (Claude) · Date: 2026-09-17
- Done: Generated the final 28 sounds (46 files) — voices, musical stingers, breaking
  glass/wood/stone/pottery, doors, explosions, magic, vehicles, swimming and climbing.
  **All 105 sounds now play for real: 51 from code, 54 from generated audio, none on a
  stand-in.**
  Rewrote nine prompts *before* spending generations, because they contained the words that
  had already cost us three rounds of rework — "bright", "sharp", "distant". The whole batch
  came back with **zero rejected takes**, where earlier batches needed repeated retries.
  Implemented **seamless looping** (`postFx.loop`), which had been an open item since v0.1.0.
  A generator never returns a loop: its first and last samples are unrelated, so playing it
  round clicks every cycle. The tail is now wrapped over the head by a crossfade, and the
  edge fades are skipped for looping sounds because they would re-open the seam. Added
  `opts.loop` to `SFX.play()` (looping a slice inside the sprite via loopStart/loopEnd) and
  `SFX.stop(handle)` to end it.
  Dropped the encode bitrates (Opus 96k→64k, AAC 128k→96k) to respect the pack's own size
  rule: `casual.webm` is now **892 KB**, under the 1 MB limit, with the AAC fallback at
  1311 KB. Verified the lower bitrate costs nothing — brightness is identical to the decimal.
- Tested: All 105 sounds audited in the browser: none silent. Loops verified by measuring
  the sample-to-sample jump where the end wraps to the beginning against a normal moment
  mid-clip — `fire.crackle` 0.018 vs 0.276, `engine.loop` 0.146 vs 0.116, both seamless.
  `engine.loop` needed a 1.2s crossfade where fire needed 0.6s: tonal material has to phase-
  match, noisy material does not. Loop playback confirmed end to end — `fire.crackle` still
  sounding at 5.5s (more than twice its 2.5s length) and silent immediately after
  `SFX.stop()`.
- Notes for next agent: `AGENTS.md` §5 now records the four rules this cost real work to
  learn — describe the source instead of asking for tone, generate repetitive sounds as one
  sequence and cut them, how to make and verify a loop, and the size limit applying to the
  Opus bundle rather than the AAC fallback.
  **Nothing has been judged by ear across the board.** Every measurement here proves only
  that no sound is silent, clipping, distant or dull. `state.gameover` is the weakest on
  paper (7% of energy above 2 kHz after repair) and is worth a listen.


## v0.2.9-A — all eight footstep surfaces cut from real walks
- Agent: A (Claude) · Date: 2026-09-17
- Done: Converted the remaining seven `step.*` surfaces to sequence mode, so all eight are
  now cut from a real 3-second walk instead of being generated one step at a time:
  grass, gravel, metal, sand, snow, stone, water, wood. Seven generations replaced
  thirty-five, and every take now carries the natural variation of a different footfall.
  **Found and fixed a real bug in the splitter.** It picked the strongest N onsets as take
  starts but ended each take at the next *selected* onset — so a quieter step sitting
  between two loud ones was swallowed into the take before it, and that take then held two
  footsteps. It now detects every hit at a low threshold and ends each cut at the next hit
  of **any** strength. `step.stone` went from two steps in two of its takes to one each.
  Re-cutting used the cached walks in `packs/casual/sounds/_seq/`, so fixing the bug cost
  no generations at all — which is the reason those are kept.
  `step.wood` came back 69% below 500 Hz with no knock in it, and EQ could not invent what
  was not there (2% → 5% above 2 kHz at +12 dB of shelf). Regenerating it as "hard leather
  shoes on a hollow wooden stage floor with knocking heel clicks" fixed it properly:
  **15% above 2 kHz**, and still loud at −2.9 dBFS. Describing the *source* gets brightness
  where asking for "bright" only gets quiet audio.
- Tested: Every take on all eight surfaces holds exactly one footstep. Verified by onset
  gaps rather than onset counts: a footstep in these walks lands every ~600 ms and no take
  exceeds 380 ms, so the extra onsets on grass, gravel, sand and snow (largest inner gap
  208 ms) are crunch texture inside one step — which is what those surfaces should sound
  like. Counting onsets alone falsely flagged them; counting the gaps settled it.
- Notes for next agent: sequence mode suits anything naturally repetitive. Obvious next
  candidates are `match.pop`, `impact.punch` and coin pickups. `step.wood` yields 4 takes
  rather than 5 because its walk only has four clear steps; that is fine, the runtime just
  cycles four.


## v0.2.8-A — generate a real walk, then cut it into takes
- Agent: A (Claude) · Date: 2026-09-17
- Done: The owner pointed out that generating footsteps one at a time was the wrong
  approach, and they were right. A generator asked for "a single footstep" still has to
  fill the API's half-second floor, so it pads or returns several steps crammed together —
  which is why v0.2.6 needed a `tighten` postFx to hack the extra steps off.
  Added **sequence mode**: a sound can declare a `sequence` block in the registry, and
  `generate_ai.py` then generates ONE natural recording (a 3-second walk) and cuts it into
  individual takes with `tools/split_takes.py`. The splitter finds each hit by rising
  energy with a refractory gap, lowering its threshold until it finds the number of takes
  asked for, then writes each one out normalized with fades on both edges.
  This is strictly better: the model is good at a natural walk, and every step in a real
  walk already differs, so the takes get their variation for free instead of from five
  separate rolls of the dice.
  Applied to `step.metal` as the trial.
- Tested: `step.metal` is now 5 takes cut from one 3-second walk. Every take contains
  **exactly one onset**, where the old approach left two steps inside several takes.
  The takes vary naturally: 153–419 ms long, 23–45% of energy above 4 kHz.
  The `tighten` hack is no longer needed for this sound and was removed from it.
- Notes for next agent: if the owner approves, convert the other seven `step.*` surfaces
  the same way, and consider it for anything else that is naturally repetitive —
  `coin.collect`-style pickups, `match.pop`, `impact.punch`. The source recordings live in
  `packs/casual/sounds/_seq/` and are gitignored; only the cut takes are committed.


## v0.2.7-A — 10 more generated sounds (25 of 54 done)
- Agent: A (Claude) · Date: 2026-09-17
- Done: Generated `weapon.sword.swing`, `weapon.sword.clash`, `weapon.cannon`,
  `impact.metal`, `impact.wood`, `impact.crit`, `step.gravel`, `step.metal`, `step.snow`
  and `step.water` — 31 files including takes. 25 of the 54 audio sounds are now done.
  Applied the v0.2.6 lesson **before** spending generations: four of these prompts asked
  for "sharp", "bright" or "thin", which is what had been returning audio 20–40 dB too
  quiet. Reworded them to ask for a loud close recording and moved the brightness into
  `postFx`. It worked — both sword sounds came back at 0.0 dBFS and needed no retries,
  where the old wording would almost certainly have failed.
  `weapon.cannon` had the same problem in reverse: its prompt literally said "distant and
  heavy", and asking for distance is asking for the dull, reverberant sound the owner
  complained about in v0.2.5. Reworded to "recorded close outdoors", which fixed the level
  (−15.3 → −0.3 dBFS).
- Tested: Level, room decay, brightness and onset count on every new sound. The sword
  sounds and `impact.crit` are bright and clean (68%, 68%, 89% of energy above 4 kHz),
  impacts and footsteps all sit in range, and no source file was rejected.
- Notes for next agent: `weapon.cannon` is still only 2% above 4 kHz even after rewording
  and +8 dB of shelf. A cannon genuinely is a low-frequency event and the generator is
  consistent about it, so this is probably correct — but it is the one in this batch most
  worth a second opinion by ear.
  Several footstep takes show two onsets inside 220 ms. That was investigated and left
  alone: heel-then-toe is what a real footstep does, and cutting shorter starts removing
  the step itself. Do not "fix" it without listening first.


## v0.2.6-A — 10 more generated sounds (15 of 54 done)
- Agent: A (Claude) · Date: 2026-09-16
- Done: Generated `step.grass`, `step.wood`, `step.stone`, `impact.punch`, `water.splash`,
  `weapon.shotgun`, `weapon.rifle.auto`, `weapon.reload`, `weapon.empty` and `weapon.bow`
  — 28 files including variation takes.
  **Found a bug I had introduced in v0.2.4.** Asking the API for the target length plus
  0.4s of headroom backfired on short sounds: the model fills whatever duration it is
  given, so a request for "a single footstep" long enough to clear the API's 0.5s floor
  came back as a **sequence** — `step.wood` contained five steps in one clip, which would
  have made every footstep in a game sound like a stampede. Headroom is now 0.15s and
  scaled to the sound's own length, and the eight `step.*` surfaces plus `impact.punch`
  got a `tighten` postFx that cuts to the first hit regardless of what comes back.
  Added a per-sound `minLevelDb`, because the blanket −20 dBFS floor is wrong for sounds
  that are genuinely soft: grass, snow, sand and cloth now allow −26. What makes boosting
  dangerous is a *noisy* source, not a quiet one.
- Tested: Onset counting (with a 70 ms refractory gap, since a naive threshold count reads
  14 "steps" in a 220 ms grass rustle) confirms one hit per take across the footstep sets.
  `weapon.shotgun` correctly shows three, because its prompt asks for a pump-action click
  after the blast. Checked brightness on every new sound; all are healthy except
  `step.wood`.
- Notes for next agent: **ElevenLabs reliably returns unusably quiet audio when a prompt
  asks for "bright", "sharp", "thin" or "piercing".** It happened on the pistol and again
  on `step.wood` (−26 to −44 dBFS). Ask for a loud, close recording and add the brightness
  with `postFx.bright` instead — prompt for level, fix tone in the build.
  `step.wood` is still only 8% energy above 4 kHz even after +12 dB of shelf; wood is a
  naturally low-mid sound, but the owner should judge whether it reads as muffled.
  Regenerating an already-good take is a bad trade: re-rolling `step.grass.1` turned a
  −15.5 dBFS take into a −21 dBFS one.


## v0.2.5-A — fixed the "far away / fake microphone" sound
- Agent: A (Claude) · Date: 2026-09-16
- Done: The owner reported the generated sounds felt distant, like a fake microphone.
  Measuring found **two separate causes**, one mine and one from the generator.
  **(1) Mine.** The master tone stage added in v0.2.1 (−5.5 dB shelf above 4.2 kHz plus a
  12 kHz lowpass) existed to tame *synthesized* sounds, which are raw oscillators and
  genuinely too bright. But it sat on the master bus, so it also processed the recorded
  audio — which is already mastered — and stripped roughly a quarter of its high end
  (`reward.chest` 48% → 36% of energy above 4 kHz, `break.glass` 86% → 79%). That dullness
  is exactly what reads as a cheap microphone. Tone shaping is now **per-category and on the
  synthesis path only**: synthesized sounds enter through the shelf, recordings go in clean.
  The soft limiter stays on the master for everything.
  **(2) The generator.** ElevenLabs baked room reverb into the pistol despite the prompt
  asking for a dry close recording: it decayed over **626 ms**, where a genuinely dry source
  like `break.glass` decays in 83 ms. That long tail is the "far away".
  Added a `postFx` repair step to `build_pack.py` so a sound can be fixed without
  regenerating it — `tighten` (hard-stop a room tail), `highpass` (cut distant rumble),
  `presence` (lift 2.5 kHz, where "close" lives) and `bright` (high-shelf lift).
- Tested: `weapon.pistol` now decays in **85 ms**, matching `break.glass` at 83 ms and
  `reward.chest` at 78 ms, and its energy above 4 kHz went from 6% to 17%. The two long
  decays left in the pack are `state.win` (989 ms) and `state.lose` (368 ms), which are
  music and are supposed to ring.
  Re-checked the mix after removing the shelf from the recorded path: generated sounds
  average 0.645 peak against 0.535 for code, and are now brighter than the synthesized half
  (33% vs 14% above 4 kHz), which is what real recordings should be.
- Notes for next agent: `postFx` is per-sound and stripped from `dist/`, so it costs games
  nothing. Reach for it before regenerating — a bad room tail is cheaper to cut than to
  re-roll, and re-rolling often changes the character you already approved.


## v0.2.4-A — fixed the "laser pistol" and the blip at the end of sounds
- Agent: A (Claude) · Date: 2026-09-16
- Done: The owner reported that the generated pistol sounded like a laser gun and that
  sounds had a pitched artifact at the very end. Both were real, and both were caused by
  `build_pack.py`, not by ElevenLabs.
  **(1)** The generated pistol came back at **−36.6 dBFS** — a whisper. `build_pack.py`
  peak-normalizes every file to −1 dBFS, so it applied a **+35.6 dB boost**, raising the
  file's noise floor and codec artifacts by the same amount and turning them into a loud
  tonal whine. Added a low-level check: any source under −20 dBFS is now reported as
  unusable instead of being silently amplified. `generate_ai.py` measures each take as it
  arrives and automatically retries a quiet one, so bad takes never reach the pack.
  **(2)** The trailing-silence trim used an **absolute** −50 dB threshold. When a file
  decays below that and then has a low-level blip at the very end, the trim stops at the
  blip and keeps both it and the near-silent gap before it — heard as a little pitched
  burst after the sound has finished. The threshold is now **relative to each file's own
  peak** (−45 dB under it), and every slice gets a 4 ms fade in and up to a 30 ms fade out
  so no sprite slice can click at its boundary.
  Also asked the API for a little more duration than the target length, since the trim
  removes the excess and a very short request gave the model no room.
- Tested: Measured every generated slice out of the built sprite. All five tails now
  read clean; `state.lose`, which previously jumped from −73 dB back up to −45 dB at its
  very end, now decays to −66.8 dB and stays there.
  Regenerated the pistol: three takes at −1 to −4 dBFS instead of −36.6, and `build_pack`
  reports no source problems.
- Notes for next agent: the pistol still measures **bass-heavy** — 23–32% of its onset
  energy is above 2 kHz, where a genuinely broadband source like `break.glass` reads 92%.
  That is ElevenLabs' character for this prompt, not a pipeline bug. An attempt to brighten
  it by asking for "thin and piercing with very little bass" produced takes at −20 to −40
  dBFS, which the new level gate caught and rejected. If it still sounds wrong to the
  owner, the fix is a per-sound EQ step in `build_pack.py` (highpass + high-shelf lift)
  rather than more prompt roulette.


## v0.2.2-A — first 5 generated sounds, and a generator tool
- Agent: A (Claude) · Date: 2026-09-16
- Done: Added `tools/generate_ai.py`, which generates the `ai` sounds straight from the
  registry using the ElevenLabs Sound Effects API — prompts, durations and take counts all
  come from `registry.json`, so what is generated is exactly what the library documents.
  It skips files that already exist, so re-running costs nothing, and reads the API key
  from `$ELEVENLABS_API_KEY`, `~/.config/elevenlabs/key` or a gitignored `.elevenlabs.key`,
  never printing or committing it.
  Generated the first 5 as a style test, chosen to span the hard cases: `state.win` and
  `state.lose` (music), `reward.chest` (layered mechanical + magical), `break.glass`
  (material texture) and `weapon.pistol` (sharp transient).
- Tested: Confirmed all 5 play from the sprite rather than a stand-in, and that each one's
  audible length matches its declared slice to within 5% — which is what proves the sprite
  offsets are right and no sound bleeds into its neighbour.
  Found a real mix problem while checking levels: `build_pack.py` normalizes every
  generated file to −1 dBFS, which is correct for a file but left the generated sounds
  roughly twice as loud as the synthesized half (peaks 0.68–0.84 against a code median of
  0.37). Rather than hand-tune five gains, added a single `spriteTrim` (default 0.55)
  applied to all sprite playback, so the remaining 49 sounds will balance automatically as
  they arrive. After: generated average 0.565 against code average 0.496.
- Notes for next agent: the owner judges these by ear — a sound that measures fine can
  still be wrong. To redo one, edit its `prompt` in `registry.json` and run
  `python3 tools/generate_ai.py <name> --force`. Per-pack balance can be overridden with
  `spriteTrim` in the manifest if a future pack is mastered differently.


## v0.2.1-A — fixed the harshness and the speaker glitch
- Agent: A (Claude) · Date: 2026-09-16
- Done: The owner reported the code sounds were harsh, pitched too high, and made a
  tiny glitch on the speaker. All three were real and all three were mine.
  **(1)** There was no tone control anywhere — every sound hit the speaker with its full
  top end. Added a master tone stage: a −5.5 dB high-shelf above 4.2 kHz, a 12 kHz
  lowpass, and a soft limiter that rounds off transient edges.
  **(2)** Fundamentals sat about an octave too high and stacked partials pushed the real
  energy to 4–6 kHz. Dropped the pitch on the coin, gem, star, sparkle, notify, tick,
  toggle, crit, ice and laser recipes, and rebuilt `ui.tap`, `ui.back` and `ui.slider`
  around a warm sine body instead of noise.
  **(3)** Square and sawtooth waves with 4 ms attacks made the hard edge that clicks.
  Swapped them for triangle everywhere the sound does not need to bite (lasers,
  electricity and summoning keep theirs) and raised the default attack to 9 ms.
  Also found a structural mistake: several recipes filtered noise with a **highpass**,
  which has no upper limit and hands the speaker everything above the cutoff. Converted
  those to bandpass. `weapon.zap` deliberately keeps its bright crackle — it is electricity.
- Tested: Measured spectral centroid and the share of energy above 5 kHz for all 105
  sounds, before and after, plus peak level. The numbers matched the complaint exactly:
  `ui.slider` had **90% of its energy above 5 kHz** (centroid 13.2 kHz — essentially hiss)
  and `ui.tap`, the most-played sound in any game, was at 51%.
  After: median centroid **2668 Hz → 1246 Hz**, median high-frequency share **0.035**,
  `ui.tap` 0.51 → 0.035, `ui.slider` 0.90 → 0.087, `pickup.gem` 0.49 → 0.095,
  `reward.star` 0.49 → 0.066. Nothing silent, nothing clipping, and levels are more
  even than before (quietest peak rose 0.104 → 0.181 thanks to the limiter).
- Notes for next agent: when adding a `code` sound, check the share of energy above 5 kHz,
  not just that it makes noise. Above ~0.25 it will sound harsh on a phone. Never filter a
  noise layer with `highpass` — use `bandpass`, which has a top as well as a bottom.


## v0.2.0-A — 105 sounds, and a real synth engine
- Agent: A (Claude) · Date: 2026-09-16
- Done: Grew the pack from 14 sounds to **105**, covering shooting, footsteps, jumping,
  impacts, breaking, explosions, magic, pickups, puzzle moves, results, doors, water,
  fire, vehicles and voices.
  The important change is conceptual: every sound now declares **how it is made**.
  `code` sounds are synthesized by the runtime *permanently* — not as placeholders —
  because things like lasers, UI blips, coin chimes and whooshes are synthetic by nature,
  and code repitches them forever without sounding like a loop. `ai` sounds are generated
  audio files, because footsteps, guns, glass, fire, engines, voices and musical fanfares
  carry material texture no oscillator fakes. That split is **51 code / 51 ai / 3 hybrid**,
  so only 54 of the 105 need any work from the owner.
  To make the code half real rather than a stand-in, replaced the toy synth with a proper
  layered engine: oscillator, filtered-noise and FM layers, stacked with per-layer delay,
  plus arpeggios, partials and vibrato. FM is what makes convincing coins, bells and metal.
- Tested: Played all 105 in a real browser and measured each one on the master bus with a
  sample-continuous meter (ScriptProcessor, not analyser snapshots — snapshots miss short
  transients and gave numbers that moved between runs). Result: nothing silent, nothing
  clipping, quietest 0.104, median 0.30, loudest 0.65.
  Found and fixed a systematic flaw on the way: narrow-bandpass noise layers measured 4–6×
  quieter than intended, so every whoosh, swipe, dash and miss was inaudible under music —
  `ui.whoosh`, which fires on every popup, was the worst at 0.046. Widened the filters
  (which also stops them whistling) and calibrated the gains from the measurements.
  Also caught a contaminated measurement: an early run had the page's own audit playing
  all 105 sounds *underneath* the meter, so those numbers were meaningless and were redone.
- Notes for next agent: **`AGENTS.md` §5 rule 1 changed meaning.** It used to say "never
  synthesize the final sound in code". That is now wrong — for half the pack, code *is*
  the final sound. The rule is replaced by the `source` contract, with the test: could this
  sound exist without a physical object making it?
  No generated audio exists yet, so the 54 `ai` sounds play a rough category stand-in
  (`ui`→tap, `game`→thud, `reward`→chime) and will sound generic until real files land.
  `fire.crackle` and `engine.loop` are marked loopable but nothing checks they loop
  seamlessly — generated files almost never do, and `build_pack.py` has no crossfade step.
  The GitHub repo `advme/pixelfork-sfx-library` still does not exist, so the CDN URLs are dead.


## v0.1.0-A — the library works end to end
- Agent: A (Claude) · Date: 2026-09-16
- Done: First working version. A game adds 2 lines and calls `SFX.play('coin.collect')`.
  Built the runtime (`src/sfx.js`), the pack registry with 14 core sounds, the build
  pipeline that turns raw audio into one small sprite, the listening board, and a demo
  that runs the library together with the Super Casual UI Kit.
  Two things worth knowing: **(1)** the library plays built-in synthesized stand-ins for any
  sound that has no real audio yet, so the whole system is testable and a game is never
  silent before a single file is generated; **(2)** `SFX.attach()` gives every UI-kit button,
  popup, toggle, shop card and star rating its sound with no per-button code.
- Tested: In a real browser. Confirmed audio actually reaches the output by attaching an
  analyser to the master bus and measuring signal (peak 0.70) rather than trusting the API.
  Confirmed `SFX.attach()` sounds a `.sc-button` tap with zero sound code on the button.
  Confirmed the build pipeline with real audio: two throwaway tones produced a correct
  sprite with variation offsets, while the other 12 sounds kept using stand-ins in the same pack.
  Fixed two bugs found this way: the star pitch ladder read `detail.value` but the UI kit
  sends `detail.index`, and `star` was handled twice so the throttle silently ate the second
  call. Verified the fix: three stars now play at 887 → 988 → 1129 Hz, once each.
- Notes for next agent: no real audio exists yet — every sound is a stand-in. That is the
  next task. The GitHub repo `advme/pixelfork-sfx-library` does not exist yet, so the CDN
  URLs in `AI-GUIDE.md`, `llms.txt` and `README.md` are not live.
