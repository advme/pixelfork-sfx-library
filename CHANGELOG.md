# CHANGELOG

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
