# Sound prompts — Casual SFX Pack

_Generated from `packs/casual/registry.json` by `tools/make_prompts.py`. Do not edit by hand —
edit the registry and run the tool again._

## How to use this

1. Open your AI sound generator (ElevenLabs Sound Effects, Stable Audio, …).
2. Copy a prompt below, generate it, and pick the best take.
3. Save it as `packs/casual/sounds/<name>.wav` — the file name **must** match the
   sound name exactly (`ui.tap.wav`). For several takes of the same sound use
   `coin.collect.1.wav`, `coin.collect.2.wav`, … and the game will vary them automatically.
4. Run `python3 tools/build_pack.py casual` and listen on the preview page.

**House style (put this in the generator if it has a style field):**

> Modern mobile casual game audio: clean, bright, punchy, lightly processed. Not retro/8-bit, not cinematic/orchestral. Mono, dry (no long reverb tails), normalized to -1 dBFS peak.

**Progress: 0 of 14 sounds delivered.**

## game

- [ ] **`feedback.powerup`** — A booster, power-up or upgrade activates.
  - Target length: ~0.6s
  - Prompt: `Power up activation for a casual mobile game, fast rising bubbly arpeggio with a bright energetic swell, positive and punchy, 0.6 seconds`

## reward

- [ ] **`coin.collect`** — One coin, gem or pickup is collected. Plays many times in a row, so it is deliberately short.
  - Target length: ~0.18s · generate **3 takes** (`coin.collect.1.wav`, `coin.collect.2.wav`, …)
  - Prompt: `Bright short coin pickup chime for a casual mobile game, small metallic bell ping with a quick upward pitch, clean and sweet, no reverb tail, 0.15 seconds`

- [ ] **`coin.pile`** — A burst of coins flies to the counter, or the reward total counts up.
  - Target length: ~0.9s
  - Prompt: `Cascade of coins landing in a pile for a mobile game reward, many bright metallic tinkles overlapping in a rising shimmer, cheerful, clean, 0.9 seconds`

- [ ] **`reward.star`** — One star fills on a level-complete screen. Play it once per star with a rising pitch.
  - Target length: ~0.45s
  - Prompt: `Magical star earned chime for a mobile game level complete screen, bright glassy bell with a sparkle shimmer, rising, warm and rewarding, 0.4 seconds`

- [ ] **`reward.claim`** — The player claims a reward, buys an item, or opens a gift.
  - Target length: ~0.7s
  - Prompt: `Satisfying reward claimed sound for a casual mobile game, bright three note rising sparkle with a soft magical shimmer, generous and happy, 0.7 seconds`

- [ ] **`reward.chest`** — A chest, box or crate opens and reveals its contents.
  - Target length: ~1.2s
  - Prompt: `Treasure chest opening for a casual mobile game, wooden creak and metal latch click then a magical rising sparkle reveal with golden shimmer, 1.2 seconds`

- [ ] **`state.win`** — The level is completed. Plays once on the Success screen.
  - Target length: ~1.6s
  - Prompt: `Short happy level complete fanfare for a casual mobile game, bright playful ascending melody on marimba and bells with a light cheerful sparkle ending, no orchestra, 1.5 seconds`

- [ ] **`state.lose`** — The level is failed. Plays once on the Fail screen.
  - Target length: ~1.3s
  - Prompt: `Gentle level failed sound for a casual mobile game, soft descending three note woodwind sigh, disappointed but friendly and encouraging, not dark or scary, 1.2 seconds`

## ui

- [ ] **`ui.tap`** — The player taps any button. The single most-used sound in the game.
  - Target length: ~0.12s
  - Prompt: `Short soft UI button tap for a mobile puzzle game, single clean woody pop with a light bright click on top, no reverb, no tail, 0.1 seconds`

- [ ] **`ui.back`** — Back, close or cancel. The darker twin of ui.tap.
  - Target length: ~0.14s
  - Prompt: `Short soft UI back button sound for a mobile game, muted low woody pop, slightly descending pitch, no reverb, 0.12 seconds`

- [ ] **`ui.whoosh`** — A popup opens or a screen slides in. Also good for cards dealing and panels sliding.
  - Target length: ~0.35s
  - Prompt: `Quick soft air whoosh for a mobile game popup opening, filtered noise sweep rising then settling, smooth and clean, no reverb tail, 0.3 seconds`

- [ ] **`ui.toggle`** — A switch, checkbox or tab changes state.
  - Target length: ~0.1s
  - Prompt: `Tiny crisp UI switch toggle click for a mobile game settings menu, single short plastic tick with a small pitch bump, dry, 0.08 seconds`

- [ ] **`ui.error`** — The action is not allowed: not enough coins, locked level, wrong move.
  - Target length: ~0.3s
  - Prompt: `Gentle friendly error sound for a casual mobile game, two soft descending muted tones, discouraging but not harsh or alarming, dry, 0.3 seconds`

- [ ] **`ui.tick`** — Countdown timer in its warning seconds, or a counter ticking up.
  - Target length: ~0.08s
  - Prompt: `Short clean clock tick for a mobile game countdown timer, single dry wooden tick with slight pitch, tense but light, 0.06 seconds`
