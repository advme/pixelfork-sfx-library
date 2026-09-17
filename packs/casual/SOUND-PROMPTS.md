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

**51 of the 220 sounds in this pack are made by code and need nothing from you.**
This checklist is only the 169 that need real audio.

**Progress: 54 of 169 generated.**

## game

- [x] **`weapon.pistol`** — A realistic handgun shot.
  - Target length: ~0.4s · generate **3 takes** (`weapon.pistol.1.wav`, `weapon.pistol.2.wav`, …)
  - Prompt: `Loud gunshot from a 9mm pistol fired once, sharp explosive bang with a hard crack and a short punchy decay, recorded close and dry`

- [x] **`weapon.shotgun`** — A shotgun blast.
  - Target length: ~0.7s · generate **2 takes** (`weapon.shotgun.1.wav`, `weapon.shotgun.2.wav`, …)
  - Prompt: `Single shotgun blast, deep powerful boom with a bright crack on top and a short pump action click after, dry close recording`

- [x] **`weapon.rifle.auto`** — A short burst of automatic fire. Loop or retrigger for sustained fire.
  - Target length: ~1.2s
  - Prompt: `Short burst of automatic assault rifle fire, five rapid dry cracks with mechanical action, close perspective, no reverb`

- [x] **`weapon.reload`** — Reloading a weapon.
  - Target length: ~0.9s
  - Prompt: `Gun reload, magazine ejected and a fresh clip slapped in then the slide racked, crisp metallic mechanical clicks, dry close recording`

- [x] **`weapon.empty`** — Out of ammo — the trigger clicks on nothing.
  - Target length: ~0.25s
  - Prompt: `Empty gun dry fire click, small hollow metallic trigger click with no shot, dry and close`

- [x] **`weapon.bow`** — Firing a bow or crossbow.
  - Target length: ~0.6s · generate **2 takes** (`weapon.bow.1.wav`, `weapon.bow.2.wav`, …)
  - Prompt: `Bow firing an arrow, taut string release with a woody thwack and the arrow whistling away quickly, dry outdoor recording`

- [x] **`weapon.sword.swing`** — Swinging a blade through the air and hitting nothing.
  - Target length: ~0.4s · generate **3 takes** (`weapon.sword.swing.1.wav`, `weapon.sword.swing.2.wav`, …)
  - Prompt: `Loud sword slashing fast through the air, strong metallic whoosh with a blade ring, recorded close and dry, no impact at the end`

- [x] **`weapon.sword.clash`** — Two blades meeting, or a blade blocked by a shield.
  - Target length: ~0.7s · generate **2 takes** (`weapon.sword.clash.1.wav`, `weapon.sword.clash.2.wav`, …)
  - Prompt: `Loud clash of two steel swords striking together, strong ringing metal impact with a shimmering tail, recorded close and dry`

- [x] **`weapon.cannon`** — A cannon, mortar or heavy artillery firing.
  - Target length: ~1.4s
  - Prompt: `Loud cannon firing, huge explosive blast with a hard cracking report at the front and a deep rumbling tail, recorded close outdoors`

- [x] **`impact.punch`** — A fist or body hit connects.
  - Target length: ~0.3s · generate **3 takes** (`impact.punch.1.wav`, `impact.punch.2.wav`, …)
  - Prompt: `Punch impact on a body, dull heavy thump with a short slap on top, cartoon action movie style, dry`

- [x] **`impact.metal`** — Something hits metal: armour, a robot, a car, a pipe.
  - Target length: ~0.5s · generate **2 takes** (`impact.metal.1.wav`, `impact.metal.2.wav`, …)
  - Prompt: `Hard impact on thick metal, loud clang with a ringing metallic tail, dry close recording`

- [x] **`impact.wood`** — Something hits wood: a crate, a door, a bat, a tree.
  - Target length: ~0.35s · generate **2 takes** (`impact.wood.1.wav`, `impact.wood.2.wav`, …)
  - Prompt: `Loud hard impact on solid wood, strong woody knock with a short dry thud, recorded close, no reverb`

- [x] **`impact.crit`** — A critical hit or perfect timing. Layer it ON TOP of the normal hit sound.
  - Target length: ~0.5s
  - Prompt: `Loud metallic shing with a quick glittering shimmer, close and dry, no impact thump, no reverb`

- [x] **`step.grass`** — One footstep on grass. Play per step; the library varies pitch and picks a different take each time.
  - Target length: ~0.25s · generate **5 takes** (`step.grass.1.wav`, `step.grass.2.wav`, …)
  - Prompt: `Single loud close-up footstep on grass, crisp dry rustle of blades with an earthy scuff, recorded right next to the shoe, no reverb`

- [x] **`step.wood`** — One footstep on wood. Play per step; the library varies pitch and picks a different take each time.
  - Target length: ~0.25s · generate **5 takes** (`step.wood.1.wav`, `step.wood.2.wav`, …)
  - Prompt: `Single footstep on a hard hollow wooden floorboard, sharp bright woody knock with a crisp attack and a short hollow resonance, close dry recording, no reverb`

- [x] **`step.stone`** — One footstep on stone. Play per step; the library varies pitch and picks a different take each time.
  - Target length: ~0.25s · generate **5 takes** (`step.stone.1.wav`, `step.stone.2.wav`, …)
  - Prompt: `Single footstep on stone or concrete, firm hard scuff of a shoe sole, close and dry, no reverb`

- [x] **`step.gravel`** — One footstep on gravel. Play per step; the library varies pitch and picks a different take each time.
  - Target length: ~0.25s · generate **5 takes** (`step.gravel.1.wav`, `step.gravel.2.wav`, …)
  - Prompt: `Single footstep on gravel, crunchy scatter of small stones under a shoe, close and dry`

- [x] **`step.metal`** — One footstep on metal. Play per step; the library varies pitch and picks a different take each time.
  - Target length: ~0.25s · generate **5 takes** (`step.metal.1.wav`, `step.metal.2.wav`, …)
  - Prompt: `Single footstep on a metal grate or steel walkway, hollow metallic clank with a faint ring, close and dry`

- [x] **`step.snow`** — One footstep on snow. Play per step; the library varies pitch and picks a different take each time.
  - Target length: ~0.25s · generate **5 takes** (`step.snow.1.wav`, `step.snow.2.wav`, …)
  - Prompt: `Single footstep in fresh snow, tight squeaky crunch of compacting powder, close and dry`

- [x] **`step.water`** — One footstep on water. Play per step; the library varies pitch and picks a different take each time.
  - Target length: ~0.25s · generate **5 takes** (`step.water.1.wav`, `step.water.2.wav`, …)
  - Prompt: `Single footstep in a shallow puddle, wet splash with a light splatter, close and dry`

- [x] **`step.sand`** — One footstep on sand. Play per step; the library varies pitch and picks a different take each time.
  - Target length: ~0.25s · generate **5 takes** (`step.sand.1.wav`, `step.sand.2.wav`, …)
  - Prompt: `Single footstep in dry sand, soft granular shuffle with no hard impact, close and dry`

- [x] **`move.swim`** — A swimming stroke or moving through water.
  - Target length: ~0.6s · generate **3 takes** (`move.swim.1.wav`, `move.swim.2.wav`, …)
  - Prompt: `One swimming stroke in water, arm pulling through with a churning splash and bubbles, close perspective`

- [x] **`move.climb`** — Grabbing a ledge, climbing a rope or scrambling up.
  - Target length: ~0.5s · generate **3 takes** (`move.climb.1.wav`, `move.climb.2.wav`, …)
  - Prompt: `Climbing grab on a rocky ledge, hand slapping stone with a gritty scrape and a cloth rustle, close and dry`

- [x] **`move.cloth`** — A cape, dodge or quick body movement that needs fabric.
  - Target length: ~0.35s · generate **3 takes** (`move.cloth.1.wav`, `move.cloth.2.wav`, …)
  - Prompt: `Quick cloth movement, fabric swishing sharply through air like a cape flick, close and dry`

- [x] **`voice.grunt`** — The character jumps, lifts, swings or takes effort.
  - Target length: ~0.4s · generate **4 takes** (`voice.grunt.1.wav`, `voice.grunt.2.wav`, …)
  - Prompt: `Short cartoon character effort grunt, light energetic hup sound, wordless, no speech, no words, dry close recording`

- [x] **`voice.hurt`** — The character takes damage.
  - Target length: ~0.5s · generate **3 takes** (`voice.hurt.1.wav`, `voice.hurt.2.wav`, …)
  - Prompt: `Short cartoon character hurt sound, light wordless, no speech, no words ouch with a comic tone, not distressing, dry close recording`

- [x] **`match.blast`** — A booster fires: rocket, bomb, lightning, rainbow clear.
  - Target length: ~0.7s
  - Prompt: `Loud cartoon booster explosion for a match three game, punchy blast with glittering sparkle debris and a satisfying low thump, playful not violent, recorded close`

- [x] **`match.shuffle`** — The board reshuffles, or cards are dealt.
  - Target length: ~1.0s
  - Prompt: `Shuffling and dealing a deck of playing cards quickly, loud paper riffle and light card slaps, recorded close and dry`

- [x] **`break.glass`** — Glass, ice or a crystal shatters.
  - Target length: ~1.0s · generate **2 takes** (`break.glass.1.wav`, `break.glass.2.wav`, …)
  - Prompt: `Pane of glass shattering, bright sharp crack followed by many small shards tinkling to the ground, dry close recording`

- [x] **`break.wood`** — A crate, plank, barrel or door breaks apart.
  - Target length: ~0.8s · generate **2 takes** (`break.wood.1.wav`, `break.wood.2.wav`, …)
  - Prompt: `Wooden crate smashing apart, loud splintering crack with planks clattering down, recorded close and dry`

- [x] **`break.stone`** — Rock, brick or concrete breaks.
  - Target length: ~1.0s · generate **2 takes** (`break.stone.1.wav`, `break.stone.2.wav`, …)
  - Prompt: `Stone block breaking apart, heavy dry crack with gravel and rubble scattering, close recording`

- [x] **`break.pot`** — A pot, vase or ceramic container smashes.
  - Target length: ~0.7s · generate **2 takes** (`break.pot.1.wav`, `break.pot.2.wav`, …)
  - Prompt: `Clay pot smashing on a tile floor, loud ceramic crack with shards scattering, recorded close and dry`

- [x] **`explosion.big`** — A real, heavy explosion with debris and rumble.
  - Target length: ~2.2s
  - Prompt: `Large explosion recorded close, powerful deep boom with a hard cracking report at the front, followed by falling debris and a long low rumble`

- [x] **`magic.fire`** — A fireball, flamethrower or burning attack. Fire texture is impossible in code.
  - Target length: ~1.0s · generate **2 takes** (`magic.fire.1.wav`, `magic.fire.2.wav`, …)
  - Prompt: `Fireball spell being cast, whooshing flame burst with crackling fire and a deep roar, magical and powerful`

- [x] **`magic.ice`** — Freezing, an ice attack, or something turning to crystal.
  - Target length: ~0.9s
  - Prompt: `Ice freezing spell, loud crystalline crackling spreading fast with a glassy shimmering tail, recorded close, magical and icy`

- [x] **`door.open`** — A door, gate or hatch opens.
  - Target length: ~1.0s
  - Prompt: `Heavy wooden door opening slowly, low creak of hinges with a final wooden thud, dry close recording`

- [x] **`door.close`** — A door, gate or hatch closes.
  - Target length: ~0.7s
  - Prompt: `Heavy wooden door closing firmly, short creak then a solid thud and latch click, dry close recording`

- [x] **`water.splash`** — Something falls into water, or a big splash on impact.
  - Target length: ~0.8s · generate **3 takes** (`water.splash.1.wav`, `water.splash.2.wav`, …)
  - Prompt: `Object splashing into water, single strong splash with droplets falling after, close outdoor recording`

- [x] **`fire.crackle`** — A campfire, torch or burning object nearby. Loops.
  - Target length: ~3.0s
  - Prompt: `Campfire burning steadily, continuous soft crackling and popping of wood embers, seamless loop, no music`

- [x] **`engine.start`** — A car, kart or machine starts up.
  - Target length: ~1.8s
  - Prompt: `Car engine starting, starter motor cranking then the engine catching and settling into an idle, close recording`

- [x] **`engine.loop`** — An engine running while driving. Loops; change pitch with rate for speed.
  - Target length: ~3.0s
  - Prompt: `Car engine running at a steady medium speed, continuous smooth motor drone, seamless loop, no music`

- [x] **`vehicle.brake`** — Hard braking, a handbrake turn or skidding to a stop.
  - Target length: ~1.2s
  - Prompt: `Car tyres screeching loudly on asphalt during a hard brake, rubber squeal fading out, recorded close outdoors`

- [x] **`vehicle.crash`** — A vehicle collision.
  - Target length: ~1.5s
  - Prompt: `Car crash impact, heavy metal crunch with glass breaking and debris settling, dry close recording`

- [ ] **`animal.dog.bark`** — A dog barks — pet, guard, companion or enemy.
  - Target length: ~0.8s · generate **3 takes** (`animal.dog.bark.1.wav`, `animal.dog.bark.2.wav`, …)
  - Prompt: `Loud single dog bark recorded close, energetic medium sized dog, dry outdoor recording`

- [ ] **`animal.cat.meow`** — A cat meows — pet or character.
  - Target length: ~0.9s · generate **2 takes** (`animal.cat.meow.1.wav`, `animal.cat.meow.2.wav`, …)
  - Prompt: `Loud close up cat meow, friendly house cat, clean dry recording`

- [ ] **`animal.bird.chirp`** — A small bird chirps — collectible, ambience accent, cute character.
  - Target length: ~0.6s · generate **3 takes** (`animal.bird.chirp.1.wav`, `animal.bird.chirp.2.wav`, …)
  - Prompt: `Loud close up small songbird chirping twice, clear dry recording, no background`

- [ ] **`animal.horse.neigh`** — A horse whinnies — mount, race, farm.
  - Target length: ~1.2s
  - Prompt: `Loud horse neighing close up, strong whinny, dry outdoor recording`

- [ ] **`animal.cow.moo`** — A cow lows — farm game, idle animal.
  - Target length: ~1.4s
  - Prompt: `Loud cow mooing close up in a barn, deep full moo, dry recording`

- [ ] **`animal.sheep.bleat`** — A sheep bleats — farm game, idle animal.
  - Target length: ~1.0s
  - Prompt: `Loud sheep bleating close up, clear bleat, dry outdoor recording`

- [ ] **`animal.chicken.cluck`** — A chicken clucks — farm game, egg collection.
  - Target length: ~0.8s · generate **2 takes** (`animal.chicken.cluck.1.wav`, `animal.chicken.cluck.2.wav`, …)
  - Prompt: `Loud chicken clucking close up, quick series of clucks, dry farmyard recording`

- [ ] **`animal.pig.oink`** — A pig oinks — farm game, idle animal.
  - Target length: ~0.8s
  - Prompt: `Loud pig oinking and snuffling close up, dry farmyard recording`

- [ ] **`animal.frog.croak`** — A frog croaks — pond, swamp, collectible creature.
  - Target length: ~0.7s · generate **2 takes** (`animal.frog.croak.1.wav`, `animal.frog.croak.2.wav`, …)
  - Prompt: `Loud frog croaking close up by a pond, deep ribbit, dry recording`

- [ ] **`animal.wolf.howl`** — A wolf howls — night, danger, boss approach.
  - Target length: ~2.2s
  - Prompt: `Wolf howling at night recorded close, long rising howl, clean dry recording`

- [ ] **`animal.snake.hiss`** — A snake hisses — enemy warning, trap.
  - Target length: ~1.0s
  - Prompt: `Loud snake hissing close up, sustained sharp air hiss, dry recording`

- [ ] **`animal.bee.buzz`** — An insect buzzes past — bee, fly, wasp enemy.
  - Target length: ~1.2s · generate **2 takes** (`animal.bee.buzz.1.wav`, `animal.bee.buzz.2.wav`, …)
  - Prompt: `Loud bee buzzing flying close past the microphone, dry outdoor recording`

- [ ] **`creature.roar`** — A big monster or boss roars.
  - Target length: ~1.8s
  - Prompt: `Loud deep monster roar recorded close, huge angry beast with a growling throat, cinematic creature vocal`

- [ ] **`creature.growl`** — A creature growls a warning before attacking.
  - Target length: ~1.2s · generate **2 takes** (`creature.growl.1.wav`, `creature.growl.2.wav`, …)
  - Prompt: `Loud low monster growl recorded close, menacing rumbling throat, creature vocal`

- [ ] **`creature.squeak`** — A small cute creature squeaks — slime, pet, critter.
  - Target length: ~0.5s · generate **3 takes** (`creature.squeak.1.wav`, `creature.squeak.2.wav`, …)
  - Prompt: `Loud cute cartoon creature squeak, small high voice chirp, playful, dry recording`

- [ ] **`creature.die`** — An enemy is defeated and vanishes.
  - Target length: ~0.9s · generate **2 takes** (`creature.die.1.wav`, `creature.die.2.wav`, …)
  - Prompt: `Loud cartoon creature defeat sound, comic descending squeal with a soft pop at the end, playful not gory`

- [ ] **`ambience.wind`** — Open outdoor wind. Loops behind gameplay.
  - Target length: ~4.0s
  - Prompt: `Steady outdoor wind blowing through an open field, continuous even gusting, clean recording, no music`

- [ ] **`ambience.rain`** — Rainfall. Loops behind gameplay.
  - Target length: ~4.0s
  - Prompt: `Steady rain falling on the ground recorded close, continuous even downpour, no thunder, no music`

- [ ] **`ambience.forest`** — Daytime forest with birds. Loops.
  - Target length: ~4.0s
  - Prompt: `Peaceful forest in daytime with birds singing and leaves rustling, continuous, clean field recording, no music`

- [ ] **`ambience.waves`** — Sea shore. Loops.
  - Target length: ~4.0s
  - Prompt: `Ocean waves washing onto a sandy beach, continuous rolling surf, clean field recording, no music`

- [ ] **`ambience.cave`** — Underground cave with drips. Loops.
  - Target length: ~4.0s
  - Prompt: `Deep underground cave ambience with occasional water drips and a low hollow rumble, continuous, no music`

- [ ] **`ambience.night`** — Night outdoors with crickets. Loops.
  - Target length: ~4.0s
  - Prompt: `Quiet night outdoors with crickets chirping steadily, continuous field recording, no music`

- [ ] **`ambience.crowd`** — Busy crowd murmur — market, stadium, town. Loops.
  - Target length: ~4.0s
  - Prompt: `Busy crowd of people talking in a large open market, continuous indistinct chatter, no music`

- [ ] **`weather.thunder`** — A thunderclap — storm, dramatic moment.
  - Target length: ~2.5s
  - Prompt: `Loud thunderclap recorded close, sharp cracking strike followed by a long deep rolling rumble`

- [ ] **`nature.leaves`** — Rustling foliage — walking through bushes, searching undergrowth.
  - Target length: ~0.9s · generate **3 takes** (`nature.leaves.1.wav`, `nature.leaves.2.wav`, …)
  - Prompt: `Loud rustling of leaves and branches as someone pushes through a bush, dry outdoor recording`

- [ ] **`nature.water.flow`** — A running stream. Loops.
  - Target length: ~4.0s
  - Prompt: `Small stream of water flowing quickly over rocks, continuous, clean close field recording, no music`

- [ ] **`crowd.boo`** — The crowd boos — failure, bad move.
  - Target length: ~1.8s
  - Prompt: `Loud crowd booing in disappointment, group of people, dry recording`

- [ ] **`crowd.gasp`** — The crowd gasps — a surprise, a near miss.
  - Target length: ~1.2s
  - Prompt: `Loud crowd of people gasping in surprise together, short sharp intake of breath, dry recording`

- [ ] **`voice.aww`** — A disappointed reaction to a loss.
  - Target length: ~1.0s
  - Prompt: `Loud disappointed aww sound from a small group of people, gentle and playful, dry close recording`

- [ ] **`horror.heartbeat`** — A heartbeat under tension — low health, chase, hiding. Loops.
  - Target length: ~3.0s
  - Prompt: `Loud human heartbeat thumping steadily, deep chest thuds at a fast nervous pace, continuous, dry recording`

- [ ] **`horror.whisper`** — An unsettling whisper — ghost, haunting, secret.
  - Target length: ~2.0s
  - Prompt: `Creepy breathy whisper voice close to the microphone, wordless, no speech, unsettling, dry recording`

- [ ] **`horror.creak`** — A door or floorboard creaks slowly — suspense.
  - Target length: ~2.0s · generate **2 takes** (`horror.creak.1.wav`, `horror.creak.2.wav`, …)
  - Prompt: `Long slow creaking of an old wooden door hinge, loud and close, dry recording`

- [ ] **`horror.jumpscare`** — A sudden scare hit.
  - Target length: ~1.5s
  - Prompt: `Sudden loud horror jump scare hit, violent screeching string stab with a deep boom underneath`

- [ ] **`horror.breathing`** — Nervous breathing — low health, hiding, stamina.
  - Target length: ~2.5s
  - Prompt: `Loud nervous human breathing close to the microphone, fast shallow frightened breaths, wordless, dry recording`

- [ ] **`horror.bell`** — A distant church bell tolls — dread, time passing.
  - Target length: ~3.0s
  - Prompt: `Single large church bell tolling once, loud deep metallic bell with a long ringing decay`

- [ ] **`sport.ball.kick`** — A ball is kicked or struck hard.
  - Target length: ~0.5s · generate **3 takes** (`sport.ball.kick.1.wav`, `sport.ball.kick.2.wav`, …)
  - Prompt: `Loud football being kicked hard, solid leather impact with a short thump, dry outdoor recording`

- [ ] **`sport.ball.bounce`** — A ball bounces on a hard surface.
  - Target length: ~0.4s · generate **4 takes** (`sport.ball.bounce.1.wav`, `sport.ball.bounce.2.wav`, …)
  - Prompt: `Loud basketball bouncing once on a hard wooden court, sharp rubber impact, dry indoor recording`

- [ ] **`sport.net.swish`** — A ball passes cleanly through a net — basket scored.
  - Target length: ~0.6s · generate **2 takes** (`sport.net.swish.1.wav`, `sport.net.swish.2.wav`, …)
  - Prompt: `Loud basketball swishing through a nylon net, clean rope rustle, dry indoor recording`

- [ ] **`sport.whistle`** — A referee whistle — round start, foul, time up.
  - Target length: ~0.9s · generate **2 takes** (`sport.whistle.1.wav`, `sport.whistle.2.wav`, …)
  - Prompt: `Loud referee whistle blown once sharply, metal pea whistle, dry recording`

- [ ] **`sport.bat.hit`** — A bat or club strikes a ball.
  - Target length: ~0.5s · generate **2 takes** (`sport.bat.hit.1.wav`, `sport.bat.hit.2.wav`, …)
  - Prompt: `Loud wooden baseball bat hitting a ball, solid cracking impact, dry outdoor recording`

- [ ] **`sport.racket.hit`** — A racket strikes a ball — tennis, padel, squash.
  - Target length: ~0.4s · generate **3 takes** (`sport.racket.hit.1.wav`, `sport.racket.hit.2.wav`, …)
  - Prompt: `Loud tennis racket striking a ball, taut string thwack, dry outdoor recording`

- [ ] **`sport.buzzer`** — An end-of-round buzzer.
  - Target length: ~1.2s
  - Prompt: `Loud stadium end of game buzzer, harsh electric horn blast, dry recording`

- [ ] **`sport.start.gun`** — A starting pistol fires — race begins.
  - Target length: ~0.8s
  - Prompt: `Loud starting pistol firing once at a race, sharp cracking report, dry outdoor recording`

- [ ] **`tool.hammer`** — Hammering a nail — building, crafting, repair.
  - Target length: ~0.5s · generate **4 takes** (`tool.hammer.1.wav`, `tool.hammer.2.wav`, …)
  - Prompt: `Loud steel hammer striking a nail into wood, single hard metallic knock, dry close recording`

- [ ] **`tool.saw`** — Sawing wood — building, crafting.
  - Target length: ~1.6s
  - Prompt: `Loud hand saw cutting through a wooden plank, rough rasping strokes, dry close recording`

- [ ] **`tool.chop.wood`** — An axe splits a log.
  - Target length: ~0.8s · generate **3 takes** (`tool.chop.wood.1.wav`, `tool.chop.wood.2.wav`, …)
  - Prompt: `Loud axe splitting a log of firewood, heavy cracking impact with splintering wood, dry outdoor recording`

- [ ] **`tool.pickaxe`** — Mining stone with a pickaxe.
  - Target length: ~0.7s · generate **4 takes** (`tool.pickaxe.1.wav`, `tool.pickaxe.2.wav`, …)
  - Prompt: `Loud steel pickaxe striking rock, hard chipping impact with small stones falling, dry recording`

- [ ] **`tool.dig`** — Digging with a shovel — farming, treasure, burying.
  - Target length: ~0.9s · generate **3 takes** (`tool.dig.1.wav`, `tool.dig.2.wav`, …)
  - Prompt: `Loud metal shovel digging into loose soil and lifting it, gritty scoop and dirt fall, dry outdoor recording`

- [ ] **`tool.drill`** — A power drill runs — repair, construction.
  - Target length: ~1.5s
  - Prompt: `Loud electric power drill running and driving a screw into wood, whirring motor, dry close recording`

- [ ] **`tool.wrench`** — A spanner or ratchet turns — repair, machinery.
  - Target length: ~0.8s · generate **2 takes** (`tool.wrench.1.wav`, `tool.wrench.2.wav`, …)
  - Prompt: `Loud metal ratchet wrench turning a bolt, clicking mechanism, dry close recording`

- [ ] **`craft.forge`** — Hammering hot metal on an anvil — smithing, upgrading.
  - Target length: ~0.9s · generate **3 takes** (`craft.forge.1.wav`, `craft.forge.2.wav`, …)
  - Prompt: `Loud blacksmith hammer striking hot metal on a steel anvil, bright ringing clang, dry workshop recording`

- [ ] **`craft.sew`** — Stitching fabric — tailoring, crafting.
  - Target length: ~0.9s · generate **2 takes** (`craft.sew.1.wav`, `craft.sew.2.wav`, …)
  - Prompt: `Loud needle and thread pulling through heavy fabric, fibrous stitching sound, dry close recording`

- [ ] **`farm.plant`** — Seeds are planted in soil.
  - Target length: ~0.7s · generate **2 takes** (`farm.plant.1.wav`, `farm.plant.2.wav`, …)
  - Prompt: `Loud scattering of seeds into loose soil and patting the earth down, dry close recording`

- [ ] **`farm.harvest`** — A crop is pulled or cut — harvesting.
  - Target length: ~0.8s · generate **3 takes** (`farm.harvest.1.wav`, `farm.harvest.2.wav`, …)
  - Prompt: `Loud pulling of a leafy vegetable out of soil, tearing roots with soil falling, dry close recording`

- [ ] **`farm.water`** — Watering plants from a can.
  - Target length: ~1.4s
  - Prompt: `Loud water pouring from a watering can onto soil and leaves, steady splashing stream, dry recording`

- [ ] **`cook.sizzle`** — Food frying in a pan. Loops.
  - Target length: ~3.0s
  - Prompt: `Loud food frying in a hot oiled pan, continuous sizzling and popping, dry kitchen recording`

- [ ] **`cook.chop`** — Chopping food on a board.
  - Target length: ~0.5s · generate **4 takes** (`cook.chop.1.wav`, `cook.chop.2.wav`, …)
  - Prompt: `Loud sharp kitchen knife chopping a vegetable on a wooden board, single clean cut, dry recording`

- [ ] **`cook.pour`** — Liquid poured into a container.
  - Target length: ~1.3s
  - Prompt: `Loud liquid pouring from a bottle into a glass, steady glugging stream, dry close recording`

- [ ] **`cook.boil`** — Water boiling in a pot. Loops.
  - Target length: ~3.0s
  - Prompt: `Loud water boiling vigorously in a metal pot, continuous rolling bubbles, dry kitchen recording`

- [ ] **`cook.oven.ding`** — An oven or microwave finishes.
  - Target length: ~1.2s
  - Prompt: `Loud kitchen oven timer dinging once, clear metallic bell chime with a ringing decay, dry recording`

- [ ] **`cook.fridge.open`** — A fridge or cabinet opens.
  - Target length: ~1.0s
  - Prompt: `Loud refrigerator door opening, rubber seal peeling apart with a soft suction, dry kitchen recording`

- [ ] **`object.zip`** — A zip fastens — bag, jacket, inventory.
  - Target length: ~0.6s · generate **2 takes** (`object.zip.1.wav`, `object.zip.2.wav`, …)
  - Prompt: `Loud metal zipper being pulled quickly closed on a jacket, dry close recording`

- [ ] **`object.paper.crumple`** — Paper is crushed — discard, delete, note.
  - Target length: ~0.9s · generate **2 takes** (`object.paper.crumple.1.wav`, `object.paper.crumple.2.wav`, …)
  - Prompt: `Loud sheet of paper being crumpled into a ball in two hands, crisp crackling, dry close recording`

- [ ] **`object.page.turn`** — A page turns — book, journal, tutorial.
  - Target length: ~0.6s · generate **3 takes** (`object.page.turn.1.wav`, `object.page.turn.2.wav`, …)
  - Prompt: `Loud single page of a book being turned, paper sweep and settle, dry close recording`

- [ ] **`object.book.close`** — A book shuts — menu closed, chapter done.
  - Target length: ~0.8s
  - Prompt: `Loud heavy hardback book being snapped shut, papery thump, dry close recording`

- [ ] **`object.keyboard`** — Typing on a keyboard — hacking, terminal, chat.
  - Target length: ~0.4s · generate **5 takes** (`object.keyboard.1.wav`, `object.keyboard.2.wav`, …)
  - Prompt: `Typing quickly on a mechanical computer keyboard, loud clicking keys, dry close recording`

- [ ] **`object.camera`** — A camera shutter — photo, capture, screenshot.
  - Target length: ~0.5s
  - Prompt: `Loud camera shutter clicking once on a film SLR, mechanical snap and wind, dry close recording`

- [ ] **`object.clock.tick`** — A clock ticking — timer pressure. Loops.
  - Target length: ~3.0s
  - Prompt: `Loud mechanical clock ticking steadily, continuous even ticks, dry close recording`

- [ ] **`object.lock`** — A padlock or bolt clicks shut or open.
  - Target length: ~0.6s · generate **2 takes** (`object.lock.1.wav`, `object.lock.2.wav`, …)
  - Prompt: `Loud metal padlock clicking shut, mechanical latch snap, dry close recording`

- [ ] **`object.chain`** — Chains rattle — gate, prison, anchor.
  - Target length: ~1.0s · generate **2 takes** (`object.chain.1.wav`, `object.chain.2.wav`, …)
  - Prompt: `Loud heavy metal chain being dragged and rattling, dry close recording`

- [ ] **`object.rope`** — Rope creaks under tension — pulling, climbing, bridge.
  - Target length: ~1.0s
  - Prompt: `Loud thick rope creaking under heavy tension, fibrous strain, dry close recording`

- [ ] **`object.glass.clink`** — Glasses clink — toast, potion, bottle.
  - Target length: ~0.6s · generate **2 takes** (`object.glass.clink.1.wav`, `object.glass.clink.2.wav`, …)
  - Prompt: `Loud two glass bottles clinking together once, clear ringing glass, dry close recording`

- [ ] **`object.coin.drop`** — A coin falls onto a hard surface.
  - Target length: ~0.8s · generate **3 takes** (`object.coin.drop.1.wav`, `object.coin.drop.2.wav`, …)
  - Prompt: `Loud metal coin dropping onto a hard stone floor and spinning to rest, dry close recording`

- [ ] **`object.switch`** — A physical switch or lever is thrown.
  - Target length: ~0.4s · generate **2 takes** (`object.switch.1.wav`, `object.switch.2.wav`, …)
  - Prompt: `Loud heavy industrial lever switch being thrown, solid mechanical clunk, dry close recording`

- [ ] **`object.balloon.pop`** — A balloon bursts — party, target, bubble.
  - Target length: ~0.5s · generate **2 takes** (`object.balloon.pop.1.wav`, `object.balloon.pop.2.wav`, …)
  - Prompt: `Loud balloon popping close to the microphone, sharp rubber burst, dry recording`

- [ ] **`object.firework`** — A firework launches and bursts — celebration.
  - Target length: ~2.5s
  - Prompt: `Loud firework whistling upward then bursting with a bright crackling explosion, outdoor recording`

- [ ] **`vehicle.horn`** — A car horn sounds.
  - Target length: ~0.9s · generate **2 takes** (`vehicle.horn.1.wav`, `vehicle.horn.2.wav`, …)
  - Prompt: `Loud car horn honking once, dry outdoor recording`

- [ ] **`vehicle.rev`** — An engine revs hard — boost, start line, showing off.
  - Target length: ~1.6s
  - Prompt: `Loud car engine revving hard, throttle blipped with a rising roar, recorded close`

- [ ] **`vehicle.gear`** — A gear change — racing, machinery.
  - Target length: ~0.5s · generate **2 takes** (`vehicle.gear.1.wav`, `vehicle.gear.2.wav`, …)
  - Prompt: `Loud mechanical gear lever shifting into place, solid metallic clunk, dry close recording`

- [ ] **`vehicle.helicopter`** — Helicopter rotors overhead. Loops.
  - Target length: ~3.5s
  - Prompt: `Loud helicopter rotor blades beating overhead, continuous steady chopping, recorded close`

- [ ] **`vehicle.plane`** — A plane passes overhead.
  - Target length: ~3.0s
  - Prompt: `Loud jet aircraft flying past overhead, rising then falling roar, outdoor recording`

- [ ] **`vehicle.train`** — A train passes or pulls away.
  - Target length: ~3.5s
  - Prompt: `Loud train rolling along rails past the microphone, rhythmic wheel clatter, outdoor recording`

- [ ] **`vehicle.boat`** — A small boat motor runs. Loops.
  - Target length: ~3.5s
  - Prompt: `Loud small outboard boat motor running steadily on water, continuous engine drone, recorded close`

- [ ] **`vehicle.bike`** — A bicycle bell rings.
  - Target length: ~0.9s
  - Prompt: `Loud bicycle bell ringing twice, bright metallic ping, dry outdoor recording`

- [ ] **`machine.robot.servo`** — A robot joint moves — mech, turret, droid.
  - Target length: ~0.7s · generate **3 takes** (`machine.robot.servo.1.wav`, `machine.robot.servo.2.wav`, …)
  - Prompt: `Loud robotic servo motor moving a mechanical joint, whirring electric motor with a soft clunk, dry recording`

- [ ] **`machine.steam`** — Steam vents — machinery, valve, pressure release.
  - Target length: ~1.4s · generate **2 takes** (`machine.steam.1.wav`, `machine.steam.2.wav`, …)
  - Prompt: `Loud burst of pressurised steam venting from a metal valve, sharp hissing release, dry recording`

- [ ] **`machine.conveyor`** — A conveyor or factory line runs. Loops.
  - Target length: ~3.0s
  - Prompt: `Loud factory conveyor belt running with rollers turning, continuous mechanical rumble, dry recording`

- [ ] **`machine.elevator`** — A lift arrives and the doors open.
  - Target length: ~2.0s
  - Prompt: `Loud elevator arriving with a bell ding then metal doors sliding open, dry indoor recording`

- [ ] **`scifi.scanner`** — A scanner sweeps — detection, radar, search.
  - Target length: ~1.4s
  - Prompt: `Science fiction scanner sweeping, loud electronic warbling sweep with a digital ping, clean synthetic recording`

- [ ] **`scifi.airlock`** — A pressurised door opens — spaceship, vault, lab.
  - Target length: ~2.0s
  - Prompt: `Loud heavy science fiction airlock door unsealing with a pressure hiss and deep mechanical thud`

- [ ] **`scifi.powerdown`** — A machine or system powers down.
  - Target length: ~1.8s
  - Prompt: `Loud science fiction machine powering down, falling electronic whine dropping in pitch to silence`

- [ ] **`scifi.powerup`** — A machine or system powers up.
  - Target length: ~1.8s
  - Prompt: `Loud science fiction machine powering up, rising electronic hum building to a steady tone`

- [ ] **`scifi.glitch`** — A digital error or corruption — hacking, damage, static.
  - Target length: ~0.8s · generate **3 takes** (`scifi.glitch.1.wav`, `scifi.glitch.2.wav`, …)
  - Prompt: `Loud digital glitch burst, stuttering electronic static and corrupted data noise, synthetic recording`

- [ ] **`scifi.hologram`** — A hologram appears or flickers.
  - Target length: ~1.2s
  - Prompt: `Science fiction hologram switching on, loud electronic shimmer with a flickering projector hum`

- [ ] **`rpg.potion`** — A potion is drunk — healing, buff.
  - Target length: ~1.2s · generate **2 takes** (`rpg.potion.1.wav`, `rpg.potion.2.wav`, …)
  - Prompt: `Loud liquid being gulped from a glass bottle then a cork stopper popping, dry close recording`

- [ ] **`rpg.scroll`** — A scroll or map unrolls.
  - Target length: ~1.0s
  - Prompt: `Loud old parchment scroll being unrolled, dry crackling paper, close recording`

- [ ] **`rpg.armor.equip`** — Armour or heavy gear is put on.
  - Target length: ~0.9s · generate **2 takes** (`rpg.armor.equip.1.wav`, `rpg.armor.equip.2.wav`, …)
  - Prompt: `Loud metal armour plates being fitted together, heavy clanking steel, dry close recording`

- [ ] **`rpg.sword.draw`** — A blade is drawn from a sheath.
  - Target length: ~0.8s · generate **2 takes** (`rpg.sword.draw.1.wav`, `rpg.sword.draw.2.wav`, …)
  - Prompt: `Loud steel sword being drawn quickly from a leather sheath, metallic ringing scrape, dry recording`

- [ ] **`rpg.spell.cast`** — A generic spell is cast.
  - Target length: ~1.3s
  - Prompt: `Loud magic spell being cast, swirling energy rush with a bright magical shimmer and a deep whoosh`

- [ ] **`rpg.curse`** — A dark spell or debuff lands.
  - Target length: ~1.5s
  - Prompt: `Loud dark magic curse landing, low ominous swell with a twisted metallic shriek, sinister`

- [ ] **`rpg.enchant`** — An item is enchanted or blessed.
  - Target length: ~1.8s
  - Prompt: `Loud magical enchantment being placed on an object, rising crystalline shimmer with a warm glowing hum`

- [ ] **`rpg.quest.accept`** — A quest is accepted or a journal updates.
  - Target length: ~1.2s
  - Prompt: `Loud fantasy game quest accepted sound, warm rising harp flourish with a soft parchment rustle`

- [ ] **`rpg.gold`** — A pile of gold coins is gathered.
  - Target length: ~1.2s · generate **2 takes** (`rpg.gold.1.wav`, `rpg.gold.2.wav`, …)
  - Prompt: `Loud handful of gold coins being scooped up and jingling together, dry close recording`

- [ ] **`rpg.trap`** — A trap springs — spikes, snare, alarm.
  - Target length: ~0.9s · generate **2 takes** (`rpg.trap.1.wav`, `rpg.trap.2.wav`, …)
  - Prompt: `Loud metal spike trap springing shut, fast mechanical snap with ringing steel, dry recording`

- [ ] **`game.spawn`** — An enemy or object appears in the world.
  - Target length: ~0.9s
  - Prompt: `Loud magical spawn sound, quick rising whoosh with a bright energetic pop as something appears`

- [ ] **`game.wave.start`** — A new wave or round begins — tower defence, survival.
  - Target length: ~1.8s
  - Prompt: `Loud battle horn signalling the start of an enemy wave, deep brass call with a war drum hit`

- [ ] **`game.tower.place`** — A tower, building or block is placed.
  - Target length: ~0.7s · generate **2 takes** (`game.tower.place.1.wav`, `game.tower.place.2.wav`, …)
  - Prompt: `Loud wooden and stone structure being set down firmly into place, solid thud with a settling clatter`

- [ ] **`game.shield.break`** — A shield or barrier shatters.
  - Target length: ~1.0s
  - Prompt: `Loud energy shield shattering, bright crystalline crack with an electric fizzing collapse`

- [ ] **`game.bullet.whizby`** — A projectile flies close past the player.
  - Target length: ~0.6s · generate **3 takes** (`game.bullet.whizby.1.wav`, `game.bullet.whizby.2.wav`, …)
  - Prompt: `Loud bullet whizzing fast past the microphone, sharp air zip with a doppler pitch drop, dry recording`

- [ ] **`game.ricochet`** — A bullet or projectile bounces off metal or stone.
  - Target length: ~0.8s · generate **3 takes** (`game.ricochet.1.wav`, `game.ricochet.2.wav`, …)
  - Prompt: `Loud bullet ricocheting off metal, sharp metallic ping with a whining departure, dry recording`

- [ ] **`game.portal`** — A portal opens or is entered.
  - Target length: ~2.0s
  - Prompt: `Loud magical portal opening, deep swirling vortex with rising energy and an otherworldly hum`

## reward

- [x] **`voice.cheer`** — The player wins something big. Layer under state.win for extra celebration.
  - Target length: ~1.5s
  - Prompt: `Small group of happy children cheering and clapping briefly, warm and joyful, short burst, dry close recording`

- [x] **`voice.laugh`** — A playful taunt, a mascot reaction, a funny fail.
  - Target length: ~1.0s
  - Prompt: `Short playful cartoon giggle, light friendly laughter, wordless, no speech, no words, dry close recording`

- [x] **`pickup.food`** — Eating: fruit, candy, a power snack. Organic and wet — code cannot fake this.
  - Target length: ~0.5s · generate **3 takes** (`pickup.food.1.wav`, `pickup.food.2.wav`, …)
  - Prompt: `Cartoon character eating, single juicy crunchy bite with a light wet chomp, playful, dry close recording`

- [x] **`pickup.ammo`** — Ammo, tools or equipment picked up.
  - Target length: ~0.35s · generate **2 takes** (`pickup.ammo.1.wav`, `pickup.ammo.2.wav`, …)
  - Prompt: `Picking up ammunition, small metallic clink of shells and a quick gear rattle, dry close recording`

- [x] **`reward.chest`** — A chest, box or crate opens and reveals its contents.
  - Target length: ~1.5s
  - Prompt: `Treasure chest opening, wooden creak and a heavy metal latch clunk followed by a magical golden sparkle reveal, warm and rewarding`

- [x] **`reward.jackpot`** — A rare drop, jackpot or huge prize. The biggest reward sound in the game.
  - Target length: ~2.0s
  - Prompt: `Loud jackpot win celebration, cascading bells and coins tumbling with a triumphant rising sparkle, recorded close, celebratory and generous`

- [x] **`state.win`** — The level is completed. Plays once on the Success screen.
  - Target length: ~1.8s
  - Prompt: `Short happy level complete fanfare for a casual mobile game, bright playful ascending melody on marimba and glockenspiel with a cheerful sparkle ending, no orchestra, no drums`

- [x] **`state.lose`** — The level is failed. Plays once on the Fail screen.
  - Target length: ~1.5s
  - Prompt: `Gentle level failed sound for a casual mobile game, soft descending three note woodwind and marimba sigh, disappointed but friendly and encouraging, not dark`

- [x] **`state.gameover`** — The run is over for good — endless runner death, all lives lost.
  - Target length: ~2.2s
  - Prompt: `Game over sting for a casual mobile game, short descending melody with a soft final chord, gently final, warm not scary`

- [x] **`state.levelup`** — The player levels up or ranks up.
  - Target length: ~1.8s
  - Prompt: `Loud level up fanfare, rising melody on glockenspiel and tubular bells with a warm triumphant swell, uplifting and short, recorded close`

- [x] **`state.newrecord`** — A new high score or personal best.
  - Target length: ~2.0s
  - Prompt: `New high score celebration for a casual mobile game, excited rising bell melody with a shimmering sparkle burst and a happy final chime`

- [ ] **`crowd.applause`** — The crowd applauds — win screen, big achievement.
  - Target length: ~2.5s
  - Prompt: `Loud enthusiastic crowd applause and clapping in a hall, recorded close, no cheering voices`

- [ ] **`voice.yay`** — A happy child voice reacts to a reward.
  - Target length: ~1.0s · generate **2 takes** (`voice.yay.1.wav`, `voice.yay.2.wav`, …)
  - Prompt: `Loud happy young child voice cheering yay, joyful, dry close recording`

- [ ] **`game.checkpoint`** — A checkpoint is reached — progress saved.
  - Target length: ~1.4s
  - Prompt: `Loud game checkpoint reached sound, warm rising three note chime with a soft magical sparkle`

## ui

- [ ] **`voice.countdown.go`** — A voice shouts GO at the start of a race or round.
  - Target length: ~0.8s
  - Prompt: `Loud energetic male voice shouting the single word GO, sports announcer style, dry close recording`
