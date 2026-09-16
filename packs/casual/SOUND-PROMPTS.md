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

**51 of the 105 sounds in this pack are made by code and need nothing from you.**
This checklist is only the 54 that need real audio.

**Progress: 5 of 54 generated.**

## game

- [x] **`weapon.pistol`** — A realistic handgun shot.
  - Target length: ~0.4s · generate **3 takes** (`weapon.pistol.1.wav`, `weapon.pistol.2.wav`, …)
  - Prompt: `Single handgun gunshot, sharp dry crack with a short punchy tail, close perspective, no music, no reverb room`

- [ ] **`weapon.shotgun`** — A shotgun blast.
  - Target length: ~0.7s · generate **2 takes** (`weapon.shotgun.1.wav`, `weapon.shotgun.2.wav`, …)
  - Prompt: `Single shotgun blast, deep powerful boom with a bright crack on top and a short pump action click after, dry close recording`

- [ ] **`weapon.rifle.auto`** — A short burst of automatic fire. Loop or retrigger for sustained fire.
  - Target length: ~1.2s
  - Prompt: `Short burst of automatic assault rifle fire, five rapid dry cracks with mechanical action, close perspective, no reverb`

- [ ] **`weapon.reload`** — Reloading a weapon.
  - Target length: ~0.9s
  - Prompt: `Gun reload, magazine ejected and a fresh clip slapped in then the slide racked, crisp metallic mechanical clicks, dry close recording`

- [ ] **`weapon.empty`** — Out of ammo — the trigger clicks on nothing.
  - Target length: ~0.25s
  - Prompt: `Empty gun dry fire click, small hollow metallic trigger click with no shot, dry and close`

- [ ] **`weapon.bow`** — Firing a bow or crossbow.
  - Target length: ~0.6s · generate **2 takes** (`weapon.bow.1.wav`, `weapon.bow.2.wav`, …)
  - Prompt: `Bow firing an arrow, taut string release with a woody thwack and the arrow whistling away quickly, dry outdoor recording`

- [ ] **`weapon.sword.swing`** — Swinging a blade through the air and hitting nothing.
  - Target length: ~0.4s · generate **3 takes** (`weapon.sword.swing.1.wav`, `weapon.sword.swing.2.wav`, …)
  - Prompt: `Sword slashing through air, fast sharp metallic whoosh with a thin blade ring, dry, no impact at the end`

- [ ] **`weapon.sword.clash`** — Two blades meeting, or a blade blocked by a shield.
  - Target length: ~0.7s · generate **2 takes** (`weapon.sword.clash.1.wav`, `weapon.sword.clash.2.wav`, …)
  - Prompt: `Two metal swords clashing together, bright ringing steel impact with a shimmering metallic tail, dry close recording`

- [ ] **`weapon.cannon`** — A cannon, mortar or heavy artillery firing.
  - Target length: ~1.4s
  - Prompt: `Large cannon firing, enormous deep explosive boom with a powerful low rumble tail, distant and heavy`

- [ ] **`impact.punch`** — A fist or body hit connects.
  - Target length: ~0.3s · generate **3 takes** (`impact.punch.1.wav`, `impact.punch.2.wav`, …)
  - Prompt: `Punch impact on a body, dull heavy thump with a short slap on top, cartoon action movie style, dry`

- [ ] **`impact.metal`** — Something hits metal: armour, a robot, a car, a pipe.
  - Target length: ~0.5s · generate **2 takes** (`impact.metal.1.wav`, `impact.metal.2.wav`, …)
  - Prompt: `Hard impact on thick metal, loud clang with a ringing metallic tail, dry close recording`

- [ ] **`impact.wood`** — Something hits wood: a crate, a door, a bat, a tree.
  - Target length: ~0.35s · generate **2 takes** (`impact.wood.1.wav`, `impact.wood.2.wav`, …)
  - Prompt: `Hard impact on solid wood, sharp woody knock with a short dry thud, no reverb`

- [ ] **`impact.crit`** — A critical hit or perfect timing. Layer it ON TOP of the normal hit sound.
  - Target length: ~0.5s
  - Prompt: `Critical hit sparkle layer for a game, bright metallic shing with a quick glittering shimmer, no impact thump, dry`

- [ ] **`step.grass`** — One footstep on grass. Play per step; the library varies pitch and picks a different take each time.
  - Target length: ~0.25s · generate **5 takes** (`step.grass.1.wav`, `step.grass.2.wav`, …)
  - Prompt: `Single footstep on grass, soft dry rustle of blades with a light earthy scuff, close perspective, no reverb`

- [ ] **`step.wood`** — One footstep on wood. Play per step; the library varies pitch and picks a different take each time.
  - Target length: ~0.25s · generate **5 takes** (`step.wood.1.wav`, `step.wood.2.wav`, …)
  - Prompt: `Single footstep on a hollow wooden floor, warm woody knock with a slight creak, close indoor recording, no reverb`

- [ ] **`step.stone`** — One footstep on stone. Play per step; the library varies pitch and picks a different take each time.
  - Target length: ~0.25s · generate **5 takes** (`step.stone.1.wav`, `step.stone.2.wav`, …)
  - Prompt: `Single footstep on stone or concrete, firm hard scuff of a shoe sole, close and dry, no reverb`

- [ ] **`step.gravel`** — One footstep on gravel. Play per step; the library varies pitch and picks a different take each time.
  - Target length: ~0.25s · generate **5 takes** (`step.gravel.1.wav`, `step.gravel.2.wav`, …)
  - Prompt: `Single footstep on gravel, crunchy scatter of small stones under a shoe, close and dry`

- [ ] **`step.metal`** — One footstep on metal. Play per step; the library varies pitch and picks a different take each time.
  - Target length: ~0.25s · generate **5 takes** (`step.metal.1.wav`, `step.metal.2.wav`, …)
  - Prompt: `Single footstep on a metal grate or steel walkway, hollow metallic clank with a faint ring, close and dry`

- [ ] **`step.snow`** — One footstep on snow. Play per step; the library varies pitch and picks a different take each time.
  - Target length: ~0.25s · generate **5 takes** (`step.snow.1.wav`, `step.snow.2.wav`, …)
  - Prompt: `Single footstep in fresh snow, tight squeaky crunch of compacting powder, close and dry`

- [ ] **`step.water`** — One footstep on water. Play per step; the library varies pitch and picks a different take each time.
  - Target length: ~0.25s · generate **5 takes** (`step.water.1.wav`, `step.water.2.wav`, …)
  - Prompt: `Single footstep in a shallow puddle, wet splash with a light splatter, close and dry`

- [ ] **`step.sand`** — One footstep on sand. Play per step; the library varies pitch and picks a different take each time.
  - Target length: ~0.25s · generate **5 takes** (`step.sand.1.wav`, `step.sand.2.wav`, …)
  - Prompt: `Single footstep in dry sand, soft granular shuffle with no hard impact, close and dry`

- [ ] **`move.swim`** — A swimming stroke or moving through water.
  - Target length: ~0.6s · generate **3 takes** (`move.swim.1.wav`, `move.swim.2.wav`, …)
  - Prompt: `One swimming stroke in water, arm pulling through with a churning splash and bubbles, close perspective`

- [ ] **`move.climb`** — Grabbing a ledge, climbing a rope or scrambling up.
  - Target length: ~0.5s · generate **3 takes** (`move.climb.1.wav`, `move.climb.2.wav`, …)
  - Prompt: `Climbing grab on a rocky ledge, hand slapping stone with a gritty scrape and a cloth rustle, close and dry`

- [ ] **`move.cloth`** — A cape, dodge or quick body movement that needs fabric.
  - Target length: ~0.35s · generate **3 takes** (`move.cloth.1.wav`, `move.cloth.2.wav`, …)
  - Prompt: `Quick cloth movement, fabric swishing sharply through air like a cape flick, close and dry`

- [ ] **`voice.grunt`** — The character jumps, lifts, swings or takes effort.
  - Target length: ~0.4s · generate **4 takes** (`voice.grunt.1.wav`, `voice.grunt.2.wav`, …)
  - Prompt: `Short cartoon character effort grunt, light energetic hup sound, non verbal, dry close recording`

- [ ] **`voice.hurt`** — The character takes damage.
  - Target length: ~0.5s · generate **3 takes** (`voice.hurt.1.wav`, `voice.hurt.2.wav`, …)
  - Prompt: `Short cartoon character hurt sound, light non verbal ouch with a comic tone, not distressing, dry close recording`

- [ ] **`match.blast`** — A booster fires: rocket, bomb, lightning, rainbow clear.
  - Target length: ~0.7s
  - Prompt: `Match three booster explosion, bright cartoon blast with sparkling debris and a satisfying low thump, playful not violent`

- [ ] **`match.shuffle`** — The board reshuffles, or cards are dealt.
  - Target length: ~1.0s
  - Prompt: `Shuffling and dealing playing cards quickly, crisp paper riffle and light slaps, dry close recording`

- [x] **`break.glass`** — Glass, ice or a crystal shatters.
  - Target length: ~1.0s · generate **2 takes** (`break.glass.1.wav`, `break.glass.2.wav`, …)
  - Prompt: `Pane of glass shattering, bright sharp crack followed by many small shards tinkling to the ground, dry close recording`

- [ ] **`break.wood`** — A crate, plank, barrel or door breaks apart.
  - Target length: ~0.8s · generate **2 takes** (`break.wood.1.wav`, `break.wood.2.wav`, …)
  - Prompt: `Wooden crate smashing apart, sharp splintering crack with planks clattering down, dry close recording`

- [ ] **`break.stone`** — Rock, brick or concrete breaks.
  - Target length: ~1.0s · generate **2 takes** (`break.stone.1.wav`, `break.stone.2.wav`, …)
  - Prompt: `Stone block breaking apart, heavy dry crack with gravel and rubble scattering, close recording`

- [ ] **`break.pot`** — A pot, vase or ceramic container smashes.
  - Target length: ~0.7s · generate **2 takes** (`break.pot.1.wav`, `break.pot.2.wav`, …)
  - Prompt: `Clay pot smashing on the floor, bright ceramic crack with shards scattering, dry close recording`

- [ ] **`explosion.big`** — A real, heavy explosion with debris and rumble.
  - Target length: ~2.2s
  - Prompt: `Large explosion, powerful deep boom with a bright initial crack, followed by falling debris and a long low rumble tail`

- [ ] **`magic.fire`** — A fireball, flamethrower or burning attack. Fire texture is impossible in code.
  - Target length: ~1.0s · generate **2 takes** (`magic.fire.1.wav`, `magic.fire.2.wav`, …)
  - Prompt: `Fireball spell being cast, whooshing flame burst with crackling fire and a deep roar, magical and powerful`

- [ ] **`magic.ice`** — Freezing, an ice attack, or something turning to crystal.
  - Target length: ~0.9s
  - Prompt: `Ice freezing spell, sharp crystalline crackle spreading with a cold shimmering tail, magical and icy`

- [ ] **`door.open`** — A door, gate or hatch opens.
  - Target length: ~1.0s
  - Prompt: `Heavy wooden door opening slowly, low creak of hinges with a final wooden thud, dry close recording`

- [ ] **`door.close`** — A door, gate or hatch closes.
  - Target length: ~0.7s
  - Prompt: `Heavy wooden door closing firmly, short creak then a solid thud and latch click, dry close recording`

- [ ] **`water.splash`** — Something falls into water, or a big splash on impact.
  - Target length: ~0.8s · generate **3 takes** (`water.splash.1.wav`, `water.splash.2.wav`, …)
  - Prompt: `Object splashing into water, single strong splash with droplets falling after, close outdoor recording`

- [ ] **`fire.crackle`** — A campfire, torch or burning object nearby. Loops.
  - Target length: ~3.0s
  - Prompt: `Campfire burning steadily, continuous soft crackling and popping of wood embers, seamless loop, no music`

- [ ] **`engine.start`** — A car, kart or machine starts up.
  - Target length: ~1.8s
  - Prompt: `Car engine starting, starter motor cranking then the engine catching and settling into an idle, close recording`

- [ ] **`engine.loop`** — An engine running while driving. Loops; change pitch with rate for speed.
  - Target length: ~3.0s
  - Prompt: `Car engine running at a steady medium speed, continuous smooth motor drone, seamless loop, no music`

- [ ] **`vehicle.brake`** — Hard braking, a handbrake turn or skidding to a stop.
  - Target length: ~1.2s
  - Prompt: `Car tyres screeching on asphalt during a hard brake, sharp rubber squeal fading out, close outdoor recording`

- [ ] **`vehicle.crash`** — A vehicle collision.
  - Target length: ~1.5s
  - Prompt: `Car crash impact, heavy metal crunch with glass breaking and debris settling, dry close recording`

## reward

- [ ] **`voice.cheer`** — The player wins something big. Layer under state.win for extra celebration.
  - Target length: ~1.5s
  - Prompt: `Small group of happy children cheering and clapping briefly, warm and joyful, short burst, dry close recording`

- [ ] **`voice.laugh`** — A playful taunt, a mascot reaction, a funny fail.
  - Target length: ~1.0s
  - Prompt: `Short playful cartoon giggle, light friendly laughter, non verbal, dry close recording`

- [ ] **`pickup.food`** — Eating: fruit, candy, a power snack. Organic and wet — code cannot fake this.
  - Target length: ~0.5s · generate **3 takes** (`pickup.food.1.wav`, `pickup.food.2.wav`, …)
  - Prompt: `Cartoon character eating, single juicy crunchy bite with a light wet chomp, playful, dry close recording`

- [ ] **`pickup.ammo`** — Ammo, tools or equipment picked up.
  - Target length: ~0.35s · generate **2 takes** (`pickup.ammo.1.wav`, `pickup.ammo.2.wav`, …)
  - Prompt: `Picking up ammunition, small metallic clink of shells and a quick gear rattle, dry close recording`

- [x] **`reward.chest`** — A chest, box or crate opens and reveals its contents.
  - Target length: ~1.5s
  - Prompt: `Treasure chest opening, wooden creak and a heavy metal latch clunk followed by a magical golden sparkle reveal, warm and rewarding`

- [ ] **`reward.jackpot`** — A rare drop, jackpot or huge prize. The biggest reward sound in the game.
  - Target length: ~2.0s
  - Prompt: `Big jackpot win for a casual game, cascading bright bells and coins with a triumphant sparkle rise, celebratory and generous`

- [x] **`state.win`** — The level is completed. Plays once on the Success screen.
  - Target length: ~1.8s
  - Prompt: `Short happy level complete fanfare for a casual mobile game, bright playful ascending melody on marimba and glockenspiel with a cheerful sparkle ending, no orchestra, no drums`

- [x] **`state.lose`** — The level is failed. Plays once on the Fail screen.
  - Target length: ~1.5s
  - Prompt: `Gentle level failed sound for a casual mobile game, soft descending three note woodwind and marimba sigh, disappointed but friendly and encouraging, not dark`

- [ ] **`state.gameover`** — The run is over for good — endless runner death, all lives lost.
  - Target length: ~2.2s
  - Prompt: `Game over sting for a casual mobile game, short descending melody with a soft final chord, gently final, warm not scary`

- [ ] **`state.levelup`** — The player levels up or ranks up.
  - Target length: ~1.8s
  - Prompt: `Level up fanfare for a casual mobile game, bright rising melody on bells with a warm triumphant swell and sparkle, uplifting and short`

- [ ] **`state.newrecord`** — A new high score or personal best.
  - Target length: ~2.0s
  - Prompt: `New high score celebration for a casual mobile game, excited rising bell melody with a shimmering sparkle burst and a happy final chime`
