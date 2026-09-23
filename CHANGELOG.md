# CHANGELOG

## v0.9.0-A — split into 15 themed bundles; music starts instantly
- Agent: A (Claude) · Date: 2026-09-24
- Why: Pixelfork V2 games were silent for 1-2 minutes on Safari. Measured by the V2 session:
  WebKit takes **78 s** to decode `casual.m4a` (Chromium 0.8 s), and WebKit decodes one file at
  a time, so `SFX.music()` sat in the queue behind the sprite. Decoded, that sprite was **258 MB**.
- Done:
  - **15 themed bundles** (`core`, `vehicles`, `world`, `casual`, `action`, `fantasy`, `scifi`,
    `animals`, `life`, `platformer`, `sports`, `casino`, `fishing`, `horror`, `holiday`), each
    under 2.2 MB. `SFX.load('casual')` now fetches the index plus `core` (1.3 MB) instead of
    16.8 MB. A theme is fetched the first time one of its sounds plays; `{themes:[...]}` and
    `SFX.preload()` load them up front.
  - **Music streams immediately** through an audio element (17 ms to first sound, measured),
    then hands over to the decoded buffer at the loop point so the seam stays sample-accurate.
    Verified over 28 s of captured output: no dropout, accents repeating exactly 16.0 s apart.
  - Board shows each sound's theme, searching a theme name filters to it, and the audit
    preloads everything first.
- Not done: not yet measured on real Safari/iOS — the WebKit numbers above are the V2 session's.

## v0.8.0-A — seamless music loops, Loop End, exact lengths, board fixes
- Agent: A (Claude) · Date: 2026-09-22
- Done:
  - **Music loops are cut, not blended.** The old tail-over-head crossfade played two parts of
    a track at once; across 78 loops it scored 0.99 (no better than a random jump). New
    `tools/loop_music.py` finds where each track repeats itself and cuts there. Median now
    0.13; 76 of 78 clean. 18 tracks that never repeated were regenerated at 48 s.
  - **Stuck buzz after a wrap fixed.** Chrome's whole-buffer loop replays one 128-sample block
    forever on some lengths (5 of 78 tracks). The loop end is now always one sample early.
  - **Music is stereo again** — looping had collapsed it to mono. **AAC padding** (~19 ms per
    .m4a) no longer gaps the loop on Safari/iPhone.
  - **`SFX.play()` plays stingers.** File-backed sounds fell through to a synth blip 28 dB
    too quiet. Stingers skip the music duck.
  - **New API:** `SFX.music(name, {loop:false})` plays once and emits `musicend`;
    `SFX.music(name, {offset:-5})` starts 5 s before the end.
  - **`duration` in the published manifest is the real length** (longest take), not the
    length requested from the generator.
  - **Board:** Play plays once, Loop loops, new Loop End (music only); exact lengths on every
    card; the preview server no longer deadlocks (threaded, Range support).
- Not done: `music.boss.3` (0.37) and `music.tension.1` (0.38) are just over the clean line —
  judge by ear. Nothing in the pack has had a full listening pass.

## v0.7.0-A — 659 sounds: 16 new SFX groups, 16 new music genres, first stingers
- Agent: A (Claude) · Date: 2026-09-20
- Done: Added **256 sounds**, taking the library from 403 to **659**.
  190 SFX across sixteen new groups — casino, puzzle, platformer, tower defence, idle,
  shop and monetisation, restaurant, construction, medieval, fishing, stealth, emotes, body
  foley, extreme weather, space and holiday.
  48 music beds across sixteen new genres, and the first **18 stingers** — level start,
  victory, defeat, game over, level up, unlock, new record, quest, rank up, boss appear,
  danger, reveal, transition, logo, chapter, sad trombone, ta-da and suspense. The library
  had no one-shot music at all before; those are marked `stream` but deliberately NOT
  loopable.
  Added **`tools/fix_loop.py`**, which sweeps crossfade lengths against the source file
  without calling the API or rebuilding the pack. It fixed **125 loops in one run** — work
  that had been costing minutes per sound.
- Tested: All 659 render and play, 145 loops, 96 music tracks.
  **The loop metric was wrong twice and I corrected it both times.** Measuring the
  single-sample jump at the wrap works for sustained tonal material but is meaningless for
  noise (which has large jumps by nature) and for impulsive rhythm (a jackhammer's jump
  between any two samples is large). Measuring **beat spacing across the wrap** instead
  cleared `idle.generator` and `build.jackhammer` as false positives, and caught a real one
  the seam test had understated: `shop.wheel.spin` skipped **+507%** of a beat every cycle,
  now +2%. `casino.reel.spin` went from +38% to +22%.
  Seven rhythmic machinery loops were regenerated at 10s because a 3s source cannot hold a
  crossfade long enough to land on the period.
- Notes for next agent: `generate_ai.py` crashed on every music entry when music joined the
  registry — they carry a `music` block instead of a `prompt`. It now skips them and refuses
  by name. Two SFX batches did nothing before I noticed, because I had piped the background
  command through `tail`, which threw away the error. **Do not pipe a background
  command's output through `tail`** — capture the whole log.
  The short-percussive-one-shot failure recurred five more times this pass
  (`sport.racket.hit`, `object.balloon.pop`, `plat.spring`, `emote.snap`,
  `body.footstep.bare`). Sequence mode fixed every one. Reach for it first.
  `space.zero.g` is deliberately quiet at −25 dBFS with `minLevelDb: -30`; it is a muffled
  suit in vacuum and forcing it loud would contradict the brief.


## v0.6.1-A — served from GitHub Pages (jsDelivr refuses repos over 50 MB)
- Agent: A (Claude) · Date: 2026-09-19
- Found right after publishing v0.6.0-A: jsDelivr answered 404 for most files. Its data API gives the reason: `403 Package size exceeded the configured limit of 50 MB`; this repo is 77 MB. (A few files loaded before jsDelivr had measured the repo, which made it look random.) My pre-publish size check was wrong: I assumed a higher limit.
- Done: links in `AI-GUIDE.md`, `README.md` and `llms.txt` moved from the jsDelivr tag URL to `https://advme.github.io/pixelfork-sfx-library/`; `.nojekyll` added so Pages serves `AI-GUIDE.md` as Markdown and does not run Jekyll over 700 files; GitHub Pages turned on for `main` / root (it was step 3 of the owner's own publish plan in STATUS). No code or audio changed; the runtime already finds its pack next to its own script URL.
- Trade-off recorded in STATUS: Pages URLs are not versioned, every game gets the latest files on push.
- Tested: see the v0.6.1-A release check in STATUS / the session log: Pages URLs for the runtime, manifest, both sprite formats, a music track and the guide; CORS header; pack loaded in a browser from another origin.

## v0.6.0-A — first public release
- Agent: A (Claude) · Date: 2026-09-19
- Done: published at the owner's request: `advme/pixelfork-sfx-library` (public), tag `v0.6.0-A`, jsDelivr. No code or audio changed. Docs brought in line with the pack before tagging: the four CDN links pinned `v0.5.0-A` (a tag that never existed) → `v0.6.0-A`; AI guide said "105 sounds, about half made by code" and the README said 373 → 403 sounds (51 code, 349 audio, 3 hybrid; 30 are music), from the registry; `llms.txt` pointed at two `advme.github.io` pages (this repo has no Pages, and the UI Kit moved to the `pixelfork-v1` account so its old Pages address is 404) → both now go through the CDN. `make_guide.py` re-run: the sound table already matched the registry.
- Tested: pre-publish scan of all tracked files AND the full git history for keys, tokens, personal paths and emails: clean (`.elevenlabs.key` is ignored and was never committed). Size: 77 MB tracked, largest file 9.8 MB, inside jsDelivr's limits. After publishing: CDN URLs for `sfx.js`, `casual.json`, the sprite and a music track load; pack loads in a browser from the CDN.
- Notes for next agent: the listening pass in STATUS is still open. The sibling UI Kit now lives under `pixelfork-v1`; this Mac is logged in as `advme`, which cannot create repos there.

## v0.6.0-A — 30 looping music tracks across 10 genres
- Agent: A (Claude) · Date: 2026-09-17
- Done: Added **30 music beds, three per genre** — casual, hyper-casual, action, racing,
  adventure, boss, horror, cozy, sci-fi and menu — bringing the library to **403 sounds**.
  Music needed a separate pipeline end to end, because it is not a sound effect:
  * a different API (`/v1/music`, not `/v1/sound-generation`), wrapped in the new
    `tools/generate_music.py`;
  * **stereo**, since a music bed folded to mono sounds flat;
  * **streamed as its own file** rather than packed into the sprite, so a game downloads
    only the track it is playing instead of all 12 MB of music;
  * looped with the same `postFx.loop` crossfade the ambiences use.
  **Rewrote music playback in the runtime.** It used an `<audio loop>` element, which
  inserts a small gap every time it wraps — that would have thrown away the crossfade each
  track was built with. Music now decodes to a buffer and loops with an
  AudioBufferSourceNode, which repeats sample-exactly, and crossfades between tracks.
- Tested: 29 of the 30 tracks were seamless on the first build; `music.racing.2` needed a
  2s crossfade instead of 4s and is now 0.79x RMS. Playback verified in the browser:
  the music streams and plays (peak 0.49), switching tracks crossfades with **zero silent
  blocks**, and a track ran **31 seconds past its own 28.1-second loop point with no gap**,
  which is the proof that the gapless loop works. Ducking confirmed by reading the duck
  gain directly: 1.0 → 0.297 → 1.0.
- Notes for next agent: I twice reached a wrong conclusion from a sloppy measurement here.
  Ducking looked broken when measured through the audio, because music level varies on its
  own; reading the gain node settled it. And sweeping a crossfade by rebuilding the whole
  pack took minutes per attempt until I tested the single file directly instead — do that.
  Music sources in `packs/casual/music/` and the sequence sources in `sounds/_seq/` are now
  **committed**. They had been gitignored, which contradicted the reason for keeping them:
  without them in the repo, nobody else can re-cut or re-loop a sound without paying to
  regenerate it.


## v0.5.0-A — depth pass: 373 sounds
- Agent: A (Claude) · Date: 2026-09-17
- Done: Added 153 sounds, taking the library from 220 to **373**. The point of this pass was
  depth rather than breadth — one sound per concept is not enough to build a game with.
  Cars got the whole engine state machine: idle, start, start-fail, stall, off, accelerate,
  decelerate, cruise, redline, rev blip, drift, skid, handbrake, sustained tyre squeal,
  up/downshift, turbo spool, blow-off, nitro, backfire, suspension, wall scrape, plus doors,
  window, seatbelt, indicator and wipers — with motorbikes, trucks and race events alongside.
  Also deepened firearms, melee, elemental magic as **cast + impact pairs**, sci-fi combat,
  six more footstep surfaces plus a running variant, water, fire, weather, doors, horror,
  kitchen, office, animals and sports.
- Tested: All 373 render and play; none silent. 42 loops, 143 sounds with multiple takes,
  22 cut from real sequences.
  Loop seams were checked only on **tonal/periodic** material, because that is the only kind
  where a seam is audible — noise has large sample-to-sample jumps by nature and nothing to
  phase-match. Three rhythmic loops failed and were fixed by regenerating a 10s source with a
  longer crossfade: `car.indicator` 9.66x → 0.17x RMS, `car.redline` 1.58x → 1.02x,
  `scifi.alarm` 2.38x → 0.69x (the alarm needed a 3s overlap; 1.5s and 4s were both worse,
  because the crossfade has to land on the klaxon's period).
- Notes for next agent: **the validator caught 28 of my own prompts** using "sharp", "bright",
  "thin" and "piercing" — the wording that returns audio 20-40 dB too quiet. I had written
  them myself, two versions after recording the rule. The check is what made that free
  instead of 28 wasted generations; keep running it before every batch.
  Single-shot firearms remain the most common failure: `gun.revolver` came back at −30 dBFS
  three times and was only fixed by sequence mode (−0.2 dBFS), the same way the pistol,
  racket and balloon were. Reach for sequence mode early on anything percussive.


## v0.4.0-A — 220 sounds, and a loop button on every one
- Agent: A (Claude) · Date: 2026-09-17
- Done: Expanded the library from 105 to **220 sounds** — 115 new ones generated with
  ElevenLabs: animals, nature and ambience beds, crowd and human reactions, horror, sports,
  tools and crafting, farming, cooking, everyday object foley, vehicles, machines, sci-fi,
  RPG abilities and more gameplay. 169 of the 220 now come from real audio.
  **Removed the 1 MB pack limit** from `AGENTS.md`. It was my own judgment call rather than
  a requirement, and it was standing in the way of simply collecting sounds.
  Added a **loop button to every sound on the preview board**, as asked. It does the right
  thing per sound: a sound built with a crossfade loops seamlessly inside the sprite, while
  a one-shot is replayed on a timer — and when it has several takes, the loop steps through
  them in turn and shows which one is playing. One sound loops at a time, Escape stops it.
  Three sounds that had failed the level gate (`sport.racket.hit`, `object.balloon.pop`,
  `cook.oven.ding`) were fixed rather than shipped quiet: the two percussive ones moved to
  sequence mode, which took them from −36.8 and −31.6 dBFS to **0.0 dBFS**.
- Tested: All 220 audited in the browser — none silent. Loop buttons verified both ways:
  `step.metal` repeated 12 times in 3 seconds while cycling its 5 takes, and `ambience.rain`
  played continuously for 8 seconds from a 3.12-second slice with zero silent blocks.
  Both stop cleanly.
- Notes for next agent: **my loop-seam tests were unreliable and I nearly acted on them.**
  Measuring the jump where the end wraps to the beginning flagged wind, cave and boil as
  broken while passing rain — yet rain's absolute jump (2.49× RMS) was *larger* than all
  three. Noise has big sample-to-sample jumps by nature and no phase to break, so a seam in
  it is inaudible; only periodic material (rotor, engine) genuinely suffers. The lesson:
  judge a loop seam by whether the material is tonal, and let the owner's ears settle the
  noisy ones. `vehicle.helicopter` was the one real case and was fixed by generating a 10s
  source with a 2s crossfade (1.60× → 0.86× RMS), the same fix that worked for the boat.
  The pack is now 3.1 MB (Opus) / 4.9 MB (AAC). That is a real download for a mobile web
  game; if it becomes a problem, split it into themed packs — the runtime already merges
  several packs into one namespace, so no game code would change.


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
