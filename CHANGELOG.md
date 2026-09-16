# CHANGELOG

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
