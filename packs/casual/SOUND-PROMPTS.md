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

**51 of the 659 sounds in this pack are made by code and need nothing from you.**
This checklist is only the 608 that need real audio.

**Progress: 512 of 608 generated.**

## game

- [x] **`weapon.pistol`** — A realistic handgun shot.
  - Target length: ~0.4s · generate **3 takes** (`weapon.pistol.1.wav`, `weapon.pistol.2.wav`, …)
  - Prompt: `Loud gunshot from a 9mm pistol fired once, hard explosive bang with a hard crack and a short punchy decay, recorded close and dry`

- [x] **`weapon.shotgun`** — A shotgun blast.
  - Target length: ~0.7s · generate **2 takes** (`weapon.shotgun.1.wav`, `weapon.shotgun.2.wav`, …)
  - Prompt: `Single shotgun blast, deep powerful boom with a ringing crack on top and a short pump action click after, dry close recording`

- [x] **`weapon.rifle.auto`** — A short burst of automatic fire. Loop or retrigger for sustained fire.
  - Target length: ~1.2s
  - Prompt: `Short burst of automatic assault rifle fire, five rapid dry cracks with mechanical action, close perspective, no reverb`

- [x] **`weapon.reload`** — Reloading a weapon.
  - Target length: ~0.9s
  - Prompt: `Gun reload, magazine ejected and a fresh clip slapped in then the slide racked, clean metallic mechanical clicks, dry close recording`

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
  - Prompt: `Single loud close-up footstep on grass, clean dry rustle of blades with an earthy scuff, recorded right next to the shoe, no reverb`

- [x] **`step.wood`** — One footstep on wood. Play per step; the library varies pitch and picks a different take each time.
  - Target length: ~0.25s · generate **5 takes** (`step.wood.1.wav`, `step.wood.2.wav`, …)
  - Prompt: `Single footstep on a hard hollow wooden floorboard, hard ringing woody knock with a clean attack and a short hollow resonance, close dry recording, no reverb`

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
  - Prompt: `Pane of glass shattering, ringing hard crack followed by many small shards tinkling to the ground, dry close recording`

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

- [x] **`animal.dog.bark`** — A dog barks — pet, guard, companion or enemy.
  - Target length: ~0.8s · generate **3 takes** (`animal.dog.bark.1.wav`, `animal.dog.bark.2.wav`, …)
  - Prompt: `Loud single dog bark recorded close, energetic medium sized dog, dry outdoor recording`

- [x] **`animal.cat.meow`** — A cat meows — pet or character.
  - Target length: ~0.9s · generate **2 takes** (`animal.cat.meow.1.wav`, `animal.cat.meow.2.wav`, …)
  - Prompt: `Loud close up cat meow, friendly house cat, clean dry recording`

- [x] **`animal.bird.chirp`** — A small bird chirps — collectible, ambience accent, cute character.
  - Target length: ~0.6s · generate **3 takes** (`animal.bird.chirp.1.wav`, `animal.bird.chirp.2.wav`, …)
  - Prompt: `Loud close up small songbird chirping twice, clear dry recording, no background`

- [x] **`animal.horse.neigh`** — A horse whinnies — mount, race, farm.
  - Target length: ~1.2s
  - Prompt: `Loud horse neighing close up, strong whinny, dry outdoor recording`

- [x] **`animal.cow.moo`** — A cow lows — farm game, idle animal.
  - Target length: ~1.4s
  - Prompt: `Loud cow mooing close up in a barn, deep full moo, dry recording`

- [x] **`animal.sheep.bleat`** — A sheep bleats — farm game, idle animal.
  - Target length: ~1.0s
  - Prompt: `Loud sheep bleating close up, clear bleat, dry outdoor recording`

- [x] **`animal.chicken.cluck`** — A chicken clucks — farm game, egg collection.
  - Target length: ~0.8s · generate **2 takes** (`animal.chicken.cluck.1.wav`, `animal.chicken.cluck.2.wav`, …)
  - Prompt: `Loud chicken clucking close up, quick series of clucks, dry farmyard recording`

- [x] **`animal.pig.oink`** — A pig oinks — farm game, idle animal.
  - Target length: ~0.8s
  - Prompt: `Loud pig oinking and snuffling close up, dry farmyard recording`

- [x] **`animal.frog.croak`** — A frog croaks — pond, swamp, collectible creature.
  - Target length: ~0.7s · generate **2 takes** (`animal.frog.croak.1.wav`, `animal.frog.croak.2.wav`, …)
  - Prompt: `Loud frog croaking close up by a pond, deep ribbit, dry recording`

- [x] **`animal.wolf.howl`** — A wolf howls — night, danger, boss approach.
  - Target length: ~2.2s
  - Prompt: `Wolf howling at night recorded close, long rising howl, clean dry recording`

- [x] **`animal.snake.hiss`** — A snake hisses — enemy warning, trap.
  - Target length: ~1.0s
  - Prompt: `Loud snake hissing close up, sustained fast air hiss, dry recording`

- [x] **`animal.bee.buzz`** — An insect buzzes past — bee, fly, wasp enemy.
  - Target length: ~1.2s · generate **2 takes** (`animal.bee.buzz.1.wav`, `animal.bee.buzz.2.wav`, …)
  - Prompt: `Loud bee buzzing flying close past the microphone, dry outdoor recording`

- [x] **`creature.roar`** — A big monster or boss roars.
  - Target length: ~1.8s
  - Prompt: `Loud deep monster roar recorded close, huge angry beast with a growling throat, cinematic creature vocal`

- [x] **`creature.growl`** — A creature growls a warning before attacking.
  - Target length: ~1.2s · generate **2 takes** (`creature.growl.1.wav`, `creature.growl.2.wav`, …)
  - Prompt: `Loud low monster growl recorded close, menacing rumbling throat, creature vocal`

- [x] **`creature.squeak`** — A small cute creature squeaks — slime, pet, critter.
  - Target length: ~0.5s · generate **3 takes** (`creature.squeak.1.wav`, `creature.squeak.2.wav`, …)
  - Prompt: `Loud cute cartoon creature squeak, small high voice chirp, playful, dry recording`

- [x] **`creature.die`** — An enemy is defeated and vanishes.
  - Target length: ~0.9s · generate **2 takes** (`creature.die.1.wav`, `creature.die.2.wav`, …)
  - Prompt: `Loud cartoon creature defeat sound, comic descending squeal with a soft pop at the end, playful not gory`

- [x] **`ambience.wind`** — Open outdoor wind. Loops behind gameplay.
  - Target length: ~10.0s
  - Prompt: `Steady outdoor wind blowing through an open field, continuous even gusting, clean recording, no music`

- [x] **`ambience.rain`** — Rainfall. Loops behind gameplay.
  - Target length: ~4.0s
  - Prompt: `Steady rain falling on the ground recorded close, continuous even downpour, no thunder, no music`

- [x] **`ambience.forest`** — Daytime forest with birds. Loops.
  - Target length: ~4.0s
  - Prompt: `Peaceful forest in daytime with birds singing and leaves rustling, continuous, clean field recording, no music`

- [x] **`ambience.waves`** — Sea shore. Loops.
  - Target length: ~4.0s
  - Prompt: `Ocean waves washing onto a sandy beach, continuous rolling surf, clean field recording, no music`

- [x] **`ambience.cave`** — Underground cave with drips. Loops.
  - Target length: ~10.0s
  - Prompt: `Deep underground cave ambience with occasional water drips and a low hollow rumble, continuous, no music`

- [x] **`ambience.night`** — Night outdoors with crickets. Loops.
  - Target length: ~4.0s
  - Prompt: `Quiet night outdoors with crickets chirping steadily, continuous field recording, no music`

- [x] **`ambience.crowd`** — Busy crowd murmur — market, stadium, town. Loops.
  - Target length: ~4.0s
  - Prompt: `Busy crowd of people talking in a large open market, continuous indistinct chatter, no music`

- [x] **`weather.thunder`** — A thunderclap — storm, dramatic moment.
  - Target length: ~2.5s
  - Prompt: `Loud thunderclap recorded close, hard cracking strike followed by a long deep rolling rumble`

- [x] **`nature.leaves`** — Rustling foliage — walking through bushes, searching undergrowth.
  - Target length: ~0.9s · generate **3 takes** (`nature.leaves.1.wav`, `nature.leaves.2.wav`, …)
  - Prompt: `Loud rustling of leaves and branches as someone pushes through a bush, dry outdoor recording`

- [x] **`nature.water.flow`** — A running stream. Loops.
  - Target length: ~4.0s
  - Prompt: `Small stream of water flowing quickly over rocks, continuous, clean close field recording, no music`

- [x] **`crowd.boo`** — The crowd boos — failure, bad move.
  - Target length: ~1.8s
  - Prompt: `Loud crowd booing in disappointment, group of people, dry recording`

- [x] **`crowd.gasp`** — The crowd gasps — a surprise, a near miss.
  - Target length: ~1.2s
  - Prompt: `Loud crowd of people gasping in surprise together, short hard intake of breath, dry recording`

- [x] **`voice.aww`** — A disappointed reaction to a loss.
  - Target length: ~1.0s
  - Prompt: `Loud disappointed aww sound from a small group of people, gentle and playful, dry close recording`

- [x] **`horror.heartbeat`** — A heartbeat under tension — low health, chase, hiding. Loops.
  - Target length: ~3.0s
  - Prompt: `Loud human heartbeat thumping steadily, deep chest thuds at a fast nervous pace, continuous, dry recording`

- [x] **`horror.whisper`** — An unsettling whisper — ghost, haunting, secret.
  - Target length: ~2.0s
  - Prompt: `Creepy breathy whisper voice close to the microphone, wordless, no speech, unsettling, dry recording`

- [x] **`horror.creak`** — A door or floorboard creaks slowly — suspense.
  - Target length: ~2.0s · generate **2 takes** (`horror.creak.1.wav`, `horror.creak.2.wav`, …)
  - Prompt: `Long slow creaking of an old wooden door hinge, loud and close, dry recording`

- [x] **`horror.jumpscare`** — A sudden scare hit.
  - Target length: ~1.5s
  - Prompt: `Sudden loud horror jump scare hit, violent screeching string stab with a deep boom underneath`

- [x] **`horror.breathing`** — Nervous breathing — low health, hiding, stamina.
  - Target length: ~2.5s
  - Prompt: `Loud nervous human breathing close to the microphone, fast shallow frightened breaths, wordless, dry recording`

- [x] **`horror.bell`** — A distant church bell tolls — dread, time passing.
  - Target length: ~3.0s
  - Prompt: `Single large church bell tolling once, loud deep metallic bell with a long ringing decay`

- [x] **`sport.ball.kick`** — A ball is kicked or struck hard.
  - Target length: ~0.5s · generate **3 takes** (`sport.ball.kick.1.wav`, `sport.ball.kick.2.wav`, …)
  - Prompt: `Loud football being kicked hard, solid leather impact with a short thump, dry outdoor recording`

- [x] **`sport.ball.bounce`** — A ball bounces on a hard surface.
  - Target length: ~0.4s · generate **4 takes** (`sport.ball.bounce.1.wav`, `sport.ball.bounce.2.wav`, …)
  - Prompt: `Loud basketball bouncing once on a hard wooden court, hard rubber impact, dry indoor recording`

- [x] **`sport.net.swish`** — A ball passes cleanly through a net — basket scored.
  - Target length: ~0.6s · generate **2 takes** (`sport.net.swish.1.wav`, `sport.net.swish.2.wav`, …)
  - Prompt: `Loud basketball swishing through a nylon net, clean rope rustle, dry indoor recording`

- [x] **`sport.whistle`** — A referee whistle — round start, foul, time up.
  - Target length: ~0.9s · generate **2 takes** (`sport.whistle.1.wav`, `sport.whistle.2.wav`, …)
  - Prompt: `Loud referee whistle blown once sharply, metal pea whistle, dry recording`

- [x] **`sport.bat.hit`** — A bat or club strikes a ball.
  - Target length: ~0.5s · generate **2 takes** (`sport.bat.hit.1.wav`, `sport.bat.hit.2.wav`, …)
  - Prompt: `Loud wooden baseball bat hitting a ball, solid cracking impact, dry outdoor recording`

- [x] **`sport.racket.hit`** — A racket strikes a ball — tennis, padel, squash.
  - Target length: ~0.4s · generate **4 takes** (`sport.racket.hit.1.wav`, `sport.racket.hit.2.wav`, …)
  - Prompt: `Loud tennis racket striking a ball, taut string thwack, dry outdoor recording`

- [x] **`sport.buzzer`** — An end-of-round buzzer.
  - Target length: ~1.2s
  - Prompt: `Loud stadium end of game buzzer, harsh electric horn blast, dry recording`

- [x] **`sport.start.gun`** — A starting pistol fires — race begins.
  - Target length: ~0.8s
  - Prompt: `Loud starting pistol firing once at a race, hard cracking report, dry outdoor recording`

- [x] **`tool.hammer`** — Hammering a nail — building, crafting, repair.
  - Target length: ~0.5s · generate **4 takes** (`tool.hammer.1.wav`, `tool.hammer.2.wav`, …)
  - Prompt: `Loud steel hammer striking a nail into wood, single hard metallic knock, dry close recording`

- [x] **`tool.saw`** — Sawing wood — building, crafting.
  - Target length: ~1.6s
  - Prompt: `Loud hand saw cutting through a wooden plank, rough rasping strokes, dry close recording`

- [x] **`tool.chop.wood`** — An axe splits a log.
  - Target length: ~0.8s · generate **3 takes** (`tool.chop.wood.1.wav`, `tool.chop.wood.2.wav`, …)
  - Prompt: `Loud axe splitting a log of firewood, heavy cracking impact with splintering wood, dry outdoor recording`

- [x] **`tool.pickaxe`** — Mining stone with a pickaxe.
  - Target length: ~0.7s · generate **4 takes** (`tool.pickaxe.1.wav`, `tool.pickaxe.2.wav`, …)
  - Prompt: `Loud steel pickaxe striking rock, hard chipping impact with small stones falling, dry recording`

- [x] **`tool.dig`** — Digging with a shovel — farming, treasure, burying.
  - Target length: ~0.9s · generate **3 takes** (`tool.dig.1.wav`, `tool.dig.2.wav`, …)
  - Prompt: `Loud metal shovel digging into loose soil and lifting it, gritty scoop and dirt fall, dry outdoor recording`

- [x] **`tool.drill`** — A power drill runs — repair, construction.
  - Target length: ~1.5s
  - Prompt: `Loud electric power drill running and driving a screw into wood, whirring motor, dry close recording`

- [x] **`tool.wrench`** — A spanner or ratchet turns — repair, machinery.
  - Target length: ~0.8s · generate **2 takes** (`tool.wrench.1.wav`, `tool.wrench.2.wav`, …)
  - Prompt: `Loud metal ratchet wrench turning a bolt, clicking mechanism, dry close recording`

- [x] **`craft.forge`** — Hammering hot metal on an anvil — smithing, upgrading.
  - Target length: ~0.9s · generate **3 takes** (`craft.forge.1.wav`, `craft.forge.2.wav`, …)
  - Prompt: `Loud blacksmith hammer striking hot metal on a steel anvil, ringing ringing clang, dry workshop recording`

- [x] **`craft.sew`** — Stitching fabric — tailoring, crafting.
  - Target length: ~0.9s · generate **2 takes** (`craft.sew.1.wav`, `craft.sew.2.wav`, …)
  - Prompt: `Loud needle and thread pulling through heavy fabric, fibrous stitching sound, dry close recording`

- [x] **`farm.plant`** — Seeds are planted in soil.
  - Target length: ~0.7s · generate **2 takes** (`farm.plant.1.wav`, `farm.plant.2.wav`, …)
  - Prompt: `Loud scattering of seeds into loose soil and patting the earth down, dry close recording`

- [x] **`farm.harvest`** — A crop is pulled or cut — harvesting.
  - Target length: ~0.8s · generate **3 takes** (`farm.harvest.1.wav`, `farm.harvest.2.wav`, …)
  - Prompt: `Loud pulling of a leafy vegetable out of soil, tearing roots with soil falling, dry close recording`

- [x] **`farm.water`** — Watering plants from a can.
  - Target length: ~1.4s
  - Prompt: `Loud water pouring from a watering can onto soil and leaves, steady splashing stream, dry recording`

- [x] **`cook.sizzle`** — Food frying in a pan. Loops.
  - Target length: ~3.0s
  - Prompt: `Loud food frying in a hot oiled pan, continuous sizzling and popping, dry kitchen recording`

- [x] **`cook.chop`** — Chopping food on a board.
  - Target length: ~0.5s · generate **4 takes** (`cook.chop.1.wav`, `cook.chop.2.wav`, …)
  - Prompt: `Loud hard kitchen knife chopping a vegetable on a wooden board, single clean cut, dry recording`

- [x] **`cook.pour`** — Liquid poured into a container.
  - Target length: ~1.3s
  - Prompt: `Loud liquid pouring from a bottle into a glass, steady glugging stream, dry close recording`

- [x] **`cook.boil`** — Water boiling in a pot. Loops.
  - Target length: ~3.0s
  - Prompt: `Loud water boiling vigorously in a metal pot, continuous rolling bubbles, dry kitchen recording`

- [x] **`cook.oven.ding`** — An oven or microwave finishes.
  - Target length: ~1.2s
  - Prompt: `Kitchen timer bell struck hard by its hammer, loud ringing metallic ding with a long ringing decay, microphone right next to the bell`

- [x] **`cook.fridge.open`** — A fridge or cabinet opens.
  - Target length: ~1.0s
  - Prompt: `Loud refrigerator door opening, rubber seal peeling apart with a soft suction, dry kitchen recording`

- [x] **`object.zip`** — A zip fastens — bag, jacket, inventory.
  - Target length: ~0.6s · generate **2 takes** (`object.zip.1.wav`, `object.zip.2.wav`, …)
  - Prompt: `Loud metal zipper being pulled quickly closed on a jacket, dry close recording`

- [x] **`object.paper.crumple`** — Paper is crushed — discard, delete, note.
  - Target length: ~0.9s · generate **2 takes** (`object.paper.crumple.1.wav`, `object.paper.crumple.2.wav`, …)
  - Prompt: `Loud sheet of paper being crumpled into a ball in two hands, clean crackling, dry close recording`

- [x] **`object.page.turn`** — A page turns — book, journal, tutorial.
  - Target length: ~0.6s · generate **3 takes** (`object.page.turn.1.wav`, `object.page.turn.2.wav`, …)
  - Prompt: `Loud single page of a book being turned, paper sweep and settle, dry close recording`

- [x] **`object.book.close`** — A book shuts — menu closed, chapter done.
  - Target length: ~0.8s
  - Prompt: `Loud heavy hardback book being snapped shut, papery thump, dry close recording`

- [x] **`object.keyboard`** — Typing on a keyboard — hacking, terminal, chat.
  - Target length: ~0.4s · generate **5 takes** (`object.keyboard.1.wav`, `object.keyboard.2.wav`, …)
  - Prompt: `Typing quickly on a mechanical computer keyboard, loud clicking keys, dry close recording`

- [x] **`object.camera`** — A camera shutter — photo, capture, screenshot.
  - Target length: ~0.5s
  - Prompt: `Loud camera shutter clicking once on a film SLR, mechanical snap and wind, dry close recording`

- [x] **`object.clock.tick`** — A clock ticking — timer pressure. Loops.
  - Target length: ~3.0s
  - Prompt: `Loud mechanical clock ticking steadily, continuous even ticks, dry close recording`

- [x] **`object.lock`** — A padlock or bolt clicks shut or open.
  - Target length: ~0.6s · generate **2 takes** (`object.lock.1.wav`, `object.lock.2.wav`, …)
  - Prompt: `Loud metal padlock clicking shut, mechanical latch snap, dry close recording`

- [x] **`object.chain`** — Chains rattle — gate, prison, anchor.
  - Target length: ~1.0s · generate **2 takes** (`object.chain.1.wav`, `object.chain.2.wav`, …)
  - Prompt: `Loud heavy metal chain being dragged and rattling, dry close recording`

- [x] **`object.rope`** — Rope creaks under tension — pulling, climbing, bridge.
  - Target length: ~1.0s
  - Prompt: `Loud thick rope creaking under heavy tension, fibrous strain, dry close recording`

- [x] **`object.glass.clink`** — Glasses clink — toast, potion, bottle.
  - Target length: ~0.6s · generate **2 takes** (`object.glass.clink.1.wav`, `object.glass.clink.2.wav`, …)
  - Prompt: `Loud two glass bottles clinking together once, clear ringing glass, dry close recording`

- [x] **`object.coin.drop`** — A coin falls onto a hard surface.
  - Target length: ~0.8s · generate **3 takes** (`object.coin.drop.1.wav`, `object.coin.drop.2.wav`, …)
  - Prompt: `Loud metal coin dropping onto a hard stone floor and spinning to rest, dry close recording`

- [x] **`object.switch`** — A physical switch or lever is thrown.
  - Target length: ~0.4s · generate **2 takes** (`object.switch.1.wav`, `object.switch.2.wav`, …)
  - Prompt: `Loud heavy industrial lever switch being thrown, solid mechanical clunk, dry close recording`

- [x] **`object.balloon.pop`** — A balloon bursts — party, target, bubble.
  - Target length: ~0.5s · generate **3 takes** (`object.balloon.pop.1.wav`, `object.balloon.pop.2.wav`, …)
  - Prompt: `Loud balloon popping close to the microphone, hard rubber burst, dry recording`

- [x] **`object.firework`** — A firework launches and bursts — celebration.
  - Target length: ~2.5s
  - Prompt: `Loud firework whistling upward then bursting with a ringing crackling explosion, outdoor recording`

- [x] **`vehicle.horn`** — A car horn sounds.
  - Target length: ~0.9s · generate **2 takes** (`vehicle.horn.1.wav`, `vehicle.horn.2.wav`, …)
  - Prompt: `Loud car horn honking once, dry outdoor recording`

- [x] **`vehicle.rev`** — An engine revs hard — boost, start line, showing off.
  - Target length: ~1.6s
  - Prompt: `Loud car engine revving hard, throttle blipped with a rising roar, recorded close`

- [x] **`vehicle.gear`** — A gear change — racing, machinery.
  - Target length: ~0.5s · generate **2 takes** (`vehicle.gear.1.wav`, `vehicle.gear.2.wav`, …)
  - Prompt: `Loud mechanical gear lever shifting into place, solid metallic clunk, dry close recording`

- [x] **`vehicle.helicopter`** — Helicopter rotors overhead. Loops.
  - Target length: ~10.0s
  - Prompt: `Loud helicopter rotor blades beating overhead, continuous steady chopping, recorded close`

- [x] **`vehicle.plane`** — A plane passes overhead.
  - Target length: ~3.0s
  - Prompt: `Loud jet aircraft flying past overhead, rising then falling roar, outdoor recording`

- [x] **`vehicle.train`** — A train passes or pulls away.
  - Target length: ~3.5s
  - Prompt: `Loud train rolling along rails past the microphone, rhythmic wheel clatter, outdoor recording`

- [x] **`vehicle.boat`** — A small boat motor runs. Loops.
  - Target length: ~10.0s
  - Prompt: `Loud small outboard boat motor running steadily on water, continuous engine drone, recorded close`

- [x] **`vehicle.bike`** — A bicycle bell rings.
  - Target length: ~0.9s
  - Prompt: `Loud bicycle bell ringing twice, ringing metallic ping, dry outdoor recording`

- [x] **`machine.robot.servo`** — A robot joint moves — mech, turret, droid.
  - Target length: ~0.7s · generate **3 takes** (`machine.robot.servo.1.wav`, `machine.robot.servo.2.wav`, …)
  - Prompt: `Loud robotic servo motor moving a mechanical joint, whirring electric motor with a soft clunk, dry recording`

- [x] **`machine.steam`** — Steam vents — machinery, valve, pressure release.
  - Target length: ~1.4s · generate **2 takes** (`machine.steam.1.wav`, `machine.steam.2.wav`, …)
  - Prompt: `Loud burst of pressurised steam venting from a metal valve, forceful hissing release, dry recording`

- [x] **`machine.conveyor`** — A conveyor or factory line runs. Loops.
  - Target length: ~3.0s
  - Prompt: `Loud factory conveyor belt running with rollers turning, continuous mechanical rumble, dry recording`

- [x] **`machine.elevator`** — A lift arrives and the doors open.
  - Target length: ~2.0s
  - Prompt: `Loud elevator arriving with a bell ding then metal doors sliding open, dry indoor recording`

- [x] **`scifi.scanner`** — A scanner sweeps — detection, radar, search.
  - Target length: ~1.4s
  - Prompt: `Science fiction scanner sweeping, loud electronic warbling sweep with a digital ping, clean synthetic recording`

- [x] **`scifi.airlock`** — A pressurised door opens — spaceship, vault, lab.
  - Target length: ~2.0s
  - Prompt: `Loud heavy science fiction airlock door unsealing with a pressure hiss and deep mechanical thud`

- [x] **`scifi.powerdown`** — A machine or system powers down.
  - Target length: ~1.8s
  - Prompt: `Loud science fiction machine powering down, falling electronic whine dropping in pitch to silence`

- [x] **`scifi.powerup`** — A machine or system powers up.
  - Target length: ~1.8s
  - Prompt: `Loud science fiction machine powering up, rising electronic hum building to a steady tone`

- [x] **`scifi.glitch`** — A digital error or corruption — hacking, damage, static.
  - Target length: ~0.8s · generate **3 takes** (`scifi.glitch.1.wav`, `scifi.glitch.2.wav`, …)
  - Prompt: `Loud digital glitch burst, stuttering electronic static and corrupted data noise, synthetic recording`

- [x] **`scifi.hologram`** — A hologram appears or flickers.
  - Target length: ~1.2s
  - Prompt: `Science fiction hologram switching on, loud electronic shimmer with a flickering projector hum`

- [x] **`rpg.potion`** — A potion is drunk — healing, buff.
  - Target length: ~1.2s · generate **2 takes** (`rpg.potion.1.wav`, `rpg.potion.2.wav`, …)
  - Prompt: `Loud liquid being gulped from a glass bottle then a cork stopper popping, dry close recording`

- [x] **`rpg.scroll`** — A scroll or map unrolls.
  - Target length: ~1.0s
  - Prompt: `Loud old parchment scroll being unrolled, dry crackling paper, close recording`

- [x] **`rpg.armor.equip`** — Armour or heavy gear is put on.
  - Target length: ~0.9s · generate **2 takes** (`rpg.armor.equip.1.wav`, `rpg.armor.equip.2.wav`, …)
  - Prompt: `Loud metal armour plates being fitted together, heavy clanking steel, dry close recording`

- [x] **`rpg.sword.draw`** — A blade is drawn from a sheath.
  - Target length: ~0.8s · generate **2 takes** (`rpg.sword.draw.1.wav`, `rpg.sword.draw.2.wav`, …)
  - Prompt: `Loud steel sword being drawn quickly from a leather sheath, metallic ringing scrape, dry recording`

- [x] **`rpg.spell.cast`** — A generic spell is cast.
  - Target length: ~1.3s
  - Prompt: `Loud magic spell being cast, swirling energy rush with a ringing magical shimmer and a deep whoosh`

- [x] **`rpg.curse`** — A dark spell or debuff lands.
  - Target length: ~1.5s
  - Prompt: `Loud dark magic curse landing, low ominous swell with a twisted metallic shriek, sinister`

- [x] **`rpg.enchant`** — An item is enchanted or blessed.
  - Target length: ~1.8s
  - Prompt: `Loud magical enchantment being placed on an object, rising crystalline shimmer with a warm glowing hum`

- [x] **`rpg.quest.accept`** — A quest is accepted or a journal updates.
  - Target length: ~1.2s
  - Prompt: `Loud fantasy game quest accepted sound, warm rising harp flourish with a soft parchment rustle`

- [x] **`rpg.gold`** — A pile of gold coins is gathered.
  - Target length: ~1.2s · generate **2 takes** (`rpg.gold.1.wav`, `rpg.gold.2.wav`, …)
  - Prompt: `Loud handful of gold coins being scooped up and jingling together, dry close recording`

- [x] **`rpg.trap`** — A trap springs — spikes, snare, alarm.
  - Target length: ~0.9s · generate **2 takes** (`rpg.trap.1.wav`, `rpg.trap.2.wav`, …)
  - Prompt: `Loud metal spike trap springing shut, fast mechanical snap with ringing steel, dry recording`

- [x] **`game.spawn`** — An enemy or object appears in the world.
  - Target length: ~0.9s
  - Prompt: `Loud magical spawn sound, quick rising whoosh with a ringing energetic pop as something appears`

- [x] **`game.wave.start`** — A new wave or round begins — tower defence, survival.
  - Target length: ~1.8s
  - Prompt: `Loud battle horn signalling the start of an enemy wave, deep brass call with a war drum hit`

- [x] **`game.tower.place`** — A tower, building or block is placed.
  - Target length: ~0.7s · generate **2 takes** (`game.tower.place.1.wav`, `game.tower.place.2.wav`, …)
  - Prompt: `Loud wooden and stone structure being set down firmly into place, solid thud with a settling clatter`

- [x] **`game.shield.break`** — A shield or barrier shatters.
  - Target length: ~1.0s
  - Prompt: `Loud energy shield shattering, ringing crystalline crack with an electric fizzing collapse`

- [x] **`game.bullet.whizby`** — A projectile flies close past the player.
  - Target length: ~0.6s · generate **3 takes** (`game.bullet.whizby.1.wav`, `game.bullet.whizby.2.wav`, …)
  - Prompt: `Loud bullet whizzing fast past the microphone, fast air zip with a doppler pitch drop, dry recording`

- [x] **`game.ricochet`** — A bullet or projectile bounces off metal or stone.
  - Target length: ~0.8s · generate **3 takes** (`game.ricochet.1.wav`, `game.ricochet.2.wav`, …)
  - Prompt: `Loud bullet ricocheting off metal, ringing metallic ping with a whining departure, dry recording`

- [x] **`game.portal`** — A portal opens or is entered.
  - Target length: ~2.0s
  - Prompt: `Loud magical portal opening, deep swirling vortex with rising energy and an otherworldly hum`

- [x] **`car.idle`** — Engine idling while parked or waiting on the grid. Loops.
  - Target length: ~8.0s
  - Prompt: `Car engine idling steadily while parked, continuous low rumbling tickover, microphone close to the exhaust`

- [x] **`car.accelerate`** — The car pulls away and gains speed.
  - Target length: ~3.0s
  - Prompt: `Car engine accelerating hard from standstill, rising roar climbing through the rev range, recorded close`

- [x] **`car.decelerate`** — The driver lifts off and the car slows.
  - Target length: ~2.5s
  - Prompt: `Car engine decelerating as the driver lifts off the throttle, falling roar settling to a burble, recorded close`

- [x] **`car.cruise`** — Steady driving at speed. Loops under gameplay.
  - Target length: ~8.0s
  - Prompt: `Car engine running at a steady cruising speed on a motorway, continuous even roar, microphone close to the engine`

- [x] **`car.redline`** — Engine held at maximum revs. Loops.
  - Target length: ~10.0s
  - Prompt: `Car engine screaming at maximum revs held at the redline, continuous high pitched roar, recorded close`

- [x] **`car.rev.blip`** — A quick throttle blip — showing off, gear match.
  - Target length: ~1.2s · generate **3 takes** (`car.rev.blip.1.wav`, `car.rev.blip.2.wav`, …)
  - Prompt: `Car engine given a quick hard throttle blip, hard rise and fall of the revs, recorded close`

- [x] **`car.start`** — The ignition turns and the engine catches.
  - Target length: ~2.5s
  - Prompt: `Car ignition starting, starter motor cranking then the engine firing up into an idle, recorded close`

- [x] **`car.start.fail`** — The engine cranks but will not start.
  - Target length: ~2.5s
  - Prompt: `Car engine failing to start, starter motor cranking repeatedly without the engine catching, recorded close`

- [x] **`car.stall`** — The engine cuts out.
  - Target length: ~1.5s
  - Prompt: `Car engine stalling and dying, revs dropping away into silence with a mechanical shudder, recorded close`

- [x] **`car.off`** — The driver switches the engine off.
  - Target length: ~1.8s
  - Prompt: `Car engine being switched off, revs falling away with a final mechanical settle, recorded close`

- [x] **`car.drift`** — The car slides sideways through a corner.
  - Target length: ~3.0s
  - Prompt: `Car tyres sliding sideways across asphalt in a long drift, sustained rubber squeal with the engine roaring behind`

- [x] **`car.skid`** — A short tyre chirp — hard turn, quick stop.
  - Target length: ~1.0s · generate **3 takes** (`car.skid.1.wav`, `car.skid.2.wav`, …)
  - Prompt: `Car tyres chirping briefly on asphalt during a hard turn, short rubber scrub, recorded close outdoors`

- [x] **`car.handbrake`** — A handbrake turn.
  - Target length: ~2.0s
  - Prompt: `Car handbrake lever ratcheting up followed by tyres breaking traction and squealing across asphalt`

- [x] **`car.tyre.squeal`** — Sustained tyre scrub through a long corner. Loops.
  - Target length: ~6.0s
  - Prompt: `Car tyres squealing continuously while cornering hard on asphalt, sustained rubber scrub, recorded close`

- [x] **`car.gear.up`** — An upshift.
  - Target length: ~0.6s · generate **2 takes** (`car.gear.up.1.wav`, `car.gear.up.2.wav`, …)
  - Prompt: `Car gear lever being shifted up a gear, solid mechanical clunk of the gate, recorded close`

- [x] **`car.gear.down`** — A downshift, often with a throttle blip.
  - Target length: ~0.9s · generate **2 takes** (`car.gear.down.1.wav`, `car.gear.down.2.wav`, …)
  - Prompt: `Car downshifting a gear with a quick throttle blip, mechanical gate clunk with a rev flare, recorded close`

- [x] **`car.turbo.spool`** — The turbo spools up under load.
  - Target length: ~2.0s
  - Prompt: `Car turbocharger spooling up under load, rising mechanical whistle building over the engine, recorded close`

- [x] **`car.turbo.blowoff`** — The blow-off valve releases on a gear change.
  - Target length: ~0.8s · generate **2 takes** (`car.turbo.blowoff.1.wav`, `car.turbo.blowoff.2.wav`, …)
  - Prompt: `Car turbo blow off valve releasing pressure, forceful hissing whoosh of escaping air, recorded close`

- [x] **`car.nitro`** — Nitrous boost fires.
  - Target length: ~2.5s
  - Prompt: `Nitrous boost firing in a race car, forceful hissing surge with the engine roar leaping in pitch`

- [x] **`car.backfire`** — The exhaust backfires — pops and bangs.
  - Target length: ~1.0s · generate **3 takes** (`car.backfire.1.wav`, `car.backfire.2.wav`, …)
  - Prompt: `Car exhaust backfiring, loud hard popping bangs from the tailpipe, recorded close`

- [x] **`car.suspension`** — The car lands or crosses a bump.
  - Target length: ~0.9s · generate **2 takes** (`car.suspension.1.wav`, `car.suspension.2.wav`, …)
  - Prompt: `Car suspension compressing hard as the car lands over a bump, metallic thump with a spring rebound`

- [x] **`car.scrape`** — The car scrapes along a wall or barrier.
  - Target length: ~1.8s
  - Prompt: `Car body scraping hard along a metal barrier, sustained grinding metal with sparks, recorded close`

- [x] **`car.crash.light`** — A minor collision — bump, tap, fender bender.
  - Target length: ~1.2s
  - Prompt: `Light car collision, dull metallic bump with plastic trim rattling, recorded close`

- [x] **`car.horn.long`** — A long angry horn blast.
  - Target length: ~2.0s
  - Prompt: `Car horn held down in a long angry blast, recorded close outdoors`

- [x] **`car.door.open`** — A car door opens.
  - Target length: ~1.2s · generate **2 takes** (`car.door.open.1.wav`, `car.door.open.2.wav`, …)
  - Prompt: `Car door handle being pulled and the door swinging open, metallic latch and hinge, recorded close`

- [x] **`car.door.close`** — A car door shuts.
  - Target length: ~1.0s · generate **2 takes** (`car.door.close.1.wav`, `car.door.close.2.wav`, …)
  - Prompt: `Car door being shut firmly, solid heavy thunk of the latch, recorded close`

- [x] **`car.window`** — An electric window winds down.
  - Target length: ~1.5s
  - Prompt: `Electric car window winding down, small motor whirring with glass sliding in the seal, recorded close`

- [x] **`car.seatbelt`** — A seatbelt is pulled and clicked in.
  - Target length: ~1.5s
  - Prompt: `Car seatbelt being pulled out and clicked into the buckle, webbing zip with a plastic click, recorded close`

- [x] **`car.indicator`** — The indicator ticks. Loops.
  - Target length: ~10.0s
  - Prompt: `Car indicator relay ticking steadily, continuous even clicking, recorded close in the cabin`

- [x] **`car.wiper`** — Windscreen wipers sweep. Loops.
  - Target length: ~4.0s
  - Prompt: `Car windscreen wipers sweeping back and forth across wet glass, continuous rubber squeak, recorded in the cabin`

- [x] **`moto.idle`** — A motorbike idles. Loops.
  - Target length: ~6.0s
  - Prompt: `Motorcycle engine idling, continuous uneven thumping tickover, microphone close to the exhaust`

- [x] **`moto.rev`** — A motorbike revs hard.
  - Target length: ~2.0s · generate **2 takes** (`moto.rev.1.wav`, `moto.rev.2.wav`, …)
  - Prompt: `Motorcycle engine revved hard, fast rising snarl from the exhaust, recorded close`

- [x] **`moto.pass`** — A motorbike flies past.
  - Target length: ~2.5s
  - Prompt: `Motorcycle speeding past the microphone at high speed, rising then falling doppler roar, outdoor recording`

- [x] **`truck.horn`** — An air horn blasts.
  - Target length: ~2.0s
  - Prompt: `Large truck air horn blasting twice, deep powerful honk, recorded outdoors`

- [x] **`truck.airbrake`** — Air brakes release with a hiss.
  - Target length: ~1.5s
  - Prompt: `Truck air brakes releasing with a hard pressurised hiss, recorded close`

- [x] **`truck.idle`** — A diesel truck idles. Loops.
  - Target length: ~8.0s
  - Prompt: `Large diesel truck engine idling, continuous deep clattering rumble, microphone close to the engine`

- [x] **`race.light`** — A starting light changes on the grid.
  - Target length: ~0.8s · generate **2 takes** (`race.light.1.wav`, `race.light.2.wav`, …)
  - Prompt: `Motorsport starting light beeping once on the grid, single clear electronic tone, recorded close`

- [x] **`race.lap`** — A lap is completed.
  - Target length: ~1.2s
  - Prompt: `Racing game lap completed sound, clear electronic double chime with a satisfying confirmation tone`

- [x] **`race.finish`** — The chequered flag — race over.
  - Target length: ~2.5s
  - Prompt: `Race finish line moment, crowd cheering with an air horn blast as a car speeds past, outdoor recording`

- [x] **`race.flag.wave`** — A flag snaps in the wind.
  - Target length: ~1.0s · generate **2 takes** (`race.flag.wave.1.wav`, `race.flag.wave.2.wav`, …)
  - Prompt: `Large flag snapping and flapping hard in strong wind, heavy cloth cracking, outdoor recording`

- [x] **`gun.smg`** — A submachine gun burst.
  - Target length: ~1.5s
  - Prompt: `Submachine gun firing a rapid burst, fast dry cracking shots with mechanical action, recorded close`

- [x] **`gun.sniper`** — A sniper rifle fires.
  - Target length: ~2.0s
  - Prompt: `Sniper rifle firing a single shot, huge cracking report with a long decaying tail, recorded outdoors`

- [x] **`gun.revolver`** — A revolver fires.
  - Target length: ~1.0s · generate **3 takes** (`gun.revolver.1.wav`, `gun.revolver.2.wav`, …)
  - Prompt: `Revolver firing a single round, loud deep cracking report, recorded close and dry`

- [x] **`gun.silenced`** — A suppressed shot.
  - Target length: ~0.7s · generate **2 takes** (`gun.silenced.1.wav`, `gun.silenced.2.wav`, …)
  - Prompt: `Suppressed pistol firing a single round, muffled thumping report with the slide cycling, recorded close`

- [x] **`gun.minigun`** — A minigun spins up and fires. Loops.
  - Target length: ~4.0s
  - Prompt: `Minigun firing continuously at high rate, rapid overlapping shots with a spinning barrel whine`

- [x] **`gun.shell.drop`** — A spent shell hits the ground.
  - Target length: ~1.0s · generate **3 takes** (`gun.shell.drop.1.wav`, `gun.shell.drop.2.wav`, …)
  - Prompt: `Spent brass shell casing bouncing on a concrete floor, ringing metallic tinkling, recorded close`

- [x] **`gun.mag.out`** — A magazine is ejected.
  - Target length: ~0.7s · generate **2 takes** (`gun.mag.out.1.wav`, `gun.mag.out.2.wav`, …)
  - Prompt: `Gun magazine being released and dropping free, metallic click with a clatter, recorded close`

- [x] **`gun.mag.in`** — A fresh magazine is seated.
  - Target length: ~0.7s · generate **2 takes** (`gun.mag.in.1.wav`, `gun.mag.in.2.wav`, …)
  - Prompt: `Fresh gun magazine being slapped firmly into the receiver, solid metallic clack, recorded close`

- [x] **`gun.bolt`** — The bolt or slide is pulled.
  - Target length: ~0.6s · generate **2 takes** (`gun.bolt.1.wav`, `gun.bolt.2.wav`, …)
  - Prompt: `Rifle bolt being pulled back and released, heavy metallic rack, recorded close`

- [x] **`gun.grenade.pin`** — A grenade pin is pulled.
  - Target length: ~0.7s
  - Prompt: `Grenade safety pin being pulled out with the lever springing off, small metallic clicks, recorded close`

- [x] **`gun.grenade.throw`** — A grenade is thrown.
  - Target length: ~0.8s
  - Prompt: `Grenade being thrown through the air, cloth swish with a metallic tumble, recorded close`

- [x] **`gun.rocket.launch`** — A rocket launcher fires.
  - Target length: ~2.0s
  - Prompt: `Rocket launcher firing, huge whooshing ignition with a roaring rocket motor departing, recorded close`

- [x] **`gun.flamethrower`** — A flamethrower burns. Loops.
  - Target length: ~4.0s
  - Prompt: `Flamethrower burning continuously, roaring jet of flame with crackling fire, recorded close`

- [x] **`gun.crossbow`** — A crossbow looses a bolt.
  - Target length: ~0.9s · generate **2 takes** (`gun.crossbow.1.wav`, `gun.crossbow.2.wav`, …)
  - Prompt: `Crossbow firing a bolt, taut string snapping forward with a wooden thunk, recorded close`

- [x] **`gun.reload.shotgun`** — Shells are pumped into a shotgun.
  - Target length: ~2.0s
  - Prompt: `Shotgun being loaded with shells and pumped, mechanical metallic racking, recorded close`

- [x] **`melee.stab`** — A blade goes in.
  - Target length: ~0.7s · generate **3 takes** (`melee.stab.1.wav`, `melee.stab.2.wav`, …)
  - Prompt: `Knife stabbing into a melon, wet penetrating impact, recorded close, cartoon action style`

- [x] **`melee.block`** — A hit is blocked on a shield.
  - Target length: ~0.8s · generate **2 takes** (`melee.block.1.wav`, `melee.block.2.wav`, …)
  - Prompt: `Sword striking a wooden shield with a metal boss, loud blocking impact with a ringing clang, recorded close`

- [x] **`melee.parry`** — A blade is deflected at the last moment.
  - Target length: ~0.7s · generate **2 takes** (`melee.parry.1.wav`, `melee.parry.2.wav`, …)
  - Prompt: `Two sword blades scraping and deflecting off each other, quick metallic ring, recorded close`

- [x] **`melee.sheathe`** — A blade is put away.
  - Target length: ~0.9s · generate **2 takes** (`melee.sheathe.1.wav`, `melee.sheathe.2.wav`, …)
  - Prompt: `Steel sword being slid back into a leather scabbard, metallic scraping slide, recorded close`

- [x] **`melee.axe.swing`** — A heavy axe swings.
  - Target length: ~0.7s · generate **2 takes** (`melee.axe.swing.1.wav`, `melee.axe.swing.2.wav`, …)
  - Prompt: `Heavy battle axe swinging through the air, deep slow air whoosh, recorded close`

- [x] **`melee.hammer.swing`** — A war hammer swings.
  - Target length: ~0.8s · generate **2 takes** (`melee.hammer.swing.1.wav`, `melee.hammer.swing.2.wav`, …)
  - Prompt: `Heavy war hammer swinging through the air, deep booming air whoosh, recorded close`

- [x] **`melee.spear`** — A spear thrusts.
  - Target length: ~0.6s · generate **2 takes** (`melee.spear.1.wav`, `melee.spear.2.wav`, …)
  - Prompt: `Wooden spear thrusting fast through the air, fast air whoosh with a shaft rattle, recorded close`

- [x] **`melee.whip`** — A whip cracks.
  - Target length: ~0.8s · generate **2 takes** (`melee.whip.1.wav`, `melee.whip.2.wav`, …)
  - Prompt: `Leather whip cracking hard, hard explosive snap with a leather hiss, recorded close`

- [x] **`melee.kick`** — A heavy kick lands.
  - Target length: ~0.5s · generate **3 takes** (`melee.kick.1.wav`, `melee.kick.2.wav`, …)
  - Prompt: `Heavy boot kicking into a body, dull thudding impact with cloth, cartoon action style, recorded close`

- [x] **`melee.dodge`** — A dodge or evade — body moving fast.
  - Target length: ~0.5s · generate **3 takes** (`melee.dodge.1.wav`, `melee.dodge.2.wav`, …)
  - Prompt: `Fast body movement dodging, quick cloth and air whoosh, recorded close`

- [x] **`magic.lightning.cast`** — A lightning spell is cast.
  - Target length: ~1.4s
  - Prompt: `Lightning spell being cast, crackling electrical charge building into a hard thunderous discharge`

- [x] **`magic.lightning.hit`** — Lightning strikes a target.
  - Target length: ~1.2s · generate **2 takes** (`magic.lightning.hit.1.wav`, `magic.lightning.hit.2.wav`, …)
  - Prompt: `Lightning bolt striking a target, violent electrical crack with a sizzling aftermath`

- [x] **`magic.fire.cast`** — A fire spell winds up.
  - Target length: ~1.3s
  - Prompt: `Fire spell being conjured, swelling roar of flames gathering with a whooshing ignition`

- [x] **`magic.fire.hit`** — A fireball lands.
  - Target length: ~1.2s · generate **2 takes** (`magic.fire.hit.1.wav`, `magic.fire.hit.2.wav`, …)
  - Prompt: `Fireball impacting a target, explosive burst of flame with crackling burning aftermath`

- [x] **`magic.ice.cast`** — An ice spell winds up.
  - Target length: ~1.3s
  - Prompt: `Ice spell being conjured, crystalline chiming with a rising cold wind`

- [x] **`magic.ice.hit`** — Ice strikes and shatters on a target.
  - Target length: ~1.2s · generate **2 takes** (`magic.ice.hit.1.wav`, `magic.ice.hit.2.wav`, …)
  - Prompt: `Ice spell impacting a target, hard crystalline shatter with frozen shards scattering`

- [x] **`magic.wind`** — A wind or gust spell.
  - Target length: ~1.5s
  - Prompt: `Wind spell being cast, powerful rushing gust of air sweeping past with a whistling swirl`

- [x] **`magic.earth`** — An earth or stone spell.
  - Target length: ~1.6s
  - Prompt: `Earth spell erupting, heavy grinding stone rising with rubble and a deep ground rumble`

- [x] **`magic.holy`** — A holy or blessing spell.
  - Target length: ~2.0s
  - Prompt: `Holy blessing spell, radiant choir-like shimmer with ringing bells and a warm rising glow`

- [x] **`magic.dark`** — A dark or shadow spell.
  - Target length: ~1.8s
  - Prompt: `Dark shadow spell being cast, deep ominous swell with whispering void and a sinister rush`

- [x] **`magic.shield.up`** — A magic barrier comes up.
  - Target length: ~1.2s
  - Prompt: `Magical shield forming, rising crystalline hum sealing into a steady protective tone`

- [x] **`magic.shield.hit`** — Something strikes a magic barrier.
  - Target length: ~0.8s · generate **2 takes** (`magic.shield.hit.1.wav`, `magic.shield.hit.2.wav`, …)
  - Prompt: `Projectile striking a magical energy shield, ringing electric deflection with a ringing wobble`

- [x] **`scifi.laser.charge`** — An energy weapon charges before firing.
  - Target length: ~1.8s
  - Prompt: `Science fiction energy weapon charging up, rising electronic whine building to a peak, synthetic recording`

- [x] **`scifi.shield.hit`** — A ship or suit shield takes a hit.
  - Target length: ~0.9s · generate **2 takes** (`scifi.shield.hit.1.wav`, `scifi.shield.hit.2.wav`, …)
  - Prompt: `Science fiction energy shield absorbing an impact, electric wobbling deflection with a metallic ring`

- [x] **`scifi.alarm`** — A ship or base alarm. Loops.
  - Target length: ~10.0s
  - Prompt: `Science fiction ship alarm klaxon sounding repeatedly, continuous urgent electronic alert`

- [x] **`scifi.engine.hum`** — Spaceship engine hum. Loops.
  - Target length: ~6.0s
  - Prompt: `Science fiction spaceship engine humming steadily, continuous deep electronic drone, synthetic recording`

- [x] **`scifi.warp`** — A jump to lightspeed.
  - Target length: ~2.5s
  - Prompt: `Spaceship jumping to lightspeed, deep rising whoosh building into an explosive departure`

- [x] **`scifi.door`** — An automatic door slides open.
  - Target length: ~1.2s · generate **2 takes** (`scifi.door.1.wav`, `scifi.door.2.wav`, …)
  - Prompt: `Science fiction automatic door sliding open with a pneumatic hiss and mechanical servo, synthetic recording`

- [x] **`scifi.computer.beep`** — A console acknowledges input.
  - Target length: ~0.5s · generate **3 takes** (`scifi.computer.beep.1.wav`, `scifi.computer.beep.2.wav`, …)
  - Prompt: `Science fiction computer console beeping a short confirmation tone, clean synthetic recording`

- [x] **`scifi.robot.talk`** — A robot speaks in machine noise.
  - Target length: ~1.4s · generate **2 takes** (`scifi.robot.talk.1.wav`, `scifi.robot.talk.2.wav`, …)
  - Prompt: `Small robot chattering in electronic beeps and warbles, wordless machine speech, synthetic recording`

- [x] **`step.carpet`** — One footstep on on thick carpet. Play per step; the library varies pitch and picks a different take each time.
  - Target length: ~0.25s · generate **5 takes** (`step.carpet.1.wav`, `step.carpet.2.wav`, …)
  - Prompt: `Single footstep on on thick carpet`

- [x] **`step.mud`** — One footstep on through wet mud. Play per step; the library varies pitch and picks a different take each time.
  - Target length: ~0.25s · generate **5 takes** (`step.mud.1.wav`, `step.mud.2.wav`, …)
  - Prompt: `Single footstep on through wet mud`

- [x] **`step.tile`** — One footstep on on hard ceramic tiles. Play per step; the library varies pitch and picks a different take each time.
  - Target length: ~0.25s · generate **5 takes** (`step.tile.1.wav`, `step.tile.2.wav`, …)
  - Prompt: `Single footstep on on hard ceramic tiles`

- [x] **`step.ice`** — One footstep on on solid ice. Play per step; the library varies pitch and picks a different take each time.
  - Target length: ~0.25s · generate **5 takes** (`step.ice.1.wav`, `step.ice.2.wav`, …)
  - Prompt: `Single footstep on on solid ice`

- [x] **`step.leaves`** — One footstep on through dry fallen leaves. Play per step; the library varies pitch and picks a different take each time.
  - Target length: ~0.25s · generate **5 takes** (`step.leaves.1.wav`, `step.leaves.2.wav`, …)
  - Prompt: `Single footstep on through dry fallen leaves`

- [x] **`step.stairs`** — One footstep on up a wooden staircase. Play per step; the library varies pitch and picks a different take each time.
  - Target length: ~0.25s · generate **5 takes** (`step.stairs.1.wav`, `step.stairs.2.wav`, …)
  - Prompt: `Single footstep on up a wooden staircase`

- [x] **`step.run.stone`** — One footstep while running on stone. Faster and harder than walking.
  - Target length: ~0.2s · generate **5 takes** (`step.run.stone.1.wav`, `step.run.stone.2.wav`, …)
  - Prompt: `Single running footstep on stone`

- [x] **`water.drip`** — A single drip — cave, leak, tension.
  - Target length: ~0.8s · generate **3 takes** (`water.drip.1.wav`, `water.drip.2.wav`, …)
  - Prompt: `Single water drop falling into a shallow puddle, clear plink with a small echo, recorded close`

- [x] **`water.tap`** — A running tap. Loops.
  - Target length: ~4.0s
  - Prompt: `Water running steadily from a kitchen tap into a sink, continuous splashing stream, recorded close`

- [x] **`water.underwater`** — Submerged ambience. Loops.
  - Target length: ~6.0s
  - Prompt: `Underwater ambience with muffled low rumble and bubbles, continuous submerged sound, recorded with a hydrophone`

- [x] **`water.bubble`** — Bubbles rise through water.
  - Target length: ~1.2s · generate **3 takes** (`water.bubble.1.wav`, `water.bubble.2.wav`, …)
  - Prompt: `Air bubbles rising through water, gurgling glugging burst, recorded close`

- [x] **`water.dive`** — A body enters the water.
  - Target length: ~1.5s
  - Prompt: `Person diving into a swimming pool, big plunging splash with water churning after, recorded close`

- [x] **`water.wave.crash`** — A big wave breaks.
  - Target length: ~2.5s
  - Prompt: `Large ocean wave crashing hard onto rocks, powerful churning break with foam hissing after, outdoor recording`

- [x] **`water.fountain`** — A fountain runs. Loops.
  - Target length: ~4.0s
  - Prompt: `Ornamental stone fountain running, continuous falling water splashing into a pool, outdoor recording`

- [x] **`fire.ignite`** — Something catches light.
  - Target length: ~1.5s
  - Prompt: `Fire igniting suddenly, hard whooshing burst of flame catching and settling into a burn, recorded close`

- [x] **`fire.torch`** — A handheld torch burns. Loops.
  - Target length: ~4.0s
  - Prompt: `Handheld burning torch, continuous flapping flame with crackling, recorded close`

- [x] **`fire.extinguish`** — A flame is put out.
  - Target length: ~1.5s
  - Prompt: `Fire being doused with water, violent hissing steam as the flames die out, recorded close`

- [x] **`fire.match`** — A match is struck.
  - Target length: ~1.2s · generate **3 takes** (`fire.match.1.wav`, `fire.match.2.wav`, …)
  - Prompt: `Match being struck on a box and catching light, gritty scrape with a flaring ignition, recorded close`

- [x] **`fire.lighter`** — A lighter flicks on.
  - Target length: ~0.8s · generate **2 takes** (`fire.lighter.1.wav`, `fire.lighter.2.wav`, …)
  - Prompt: `Cigarette lighter being flicked, metal wheel sparking with a small flame catching, recorded close`

- [x] **`weather.rain.light`** — Light rain. Loops.
  - Target length: ~6.0s
  - Prompt: `Light drizzling rain falling on pavement, continuous gentle patter, clean field recording, no music`

- [x] **`weather.rain.heavy`** — Heavy downpour. Loops.
  - Target length: ~6.0s
  - Prompt: `Heavy torrential rain pouring down hard, continuous roaring downpour, clean field recording, no music`

- [x] **`weather.rain.window`** — Rain on glass. Loops.
  - Target length: ~6.0s
  - Prompt: `Rain drumming against a window pane from inside, continuous tapping on glass, clean recording, no music`

- [x] **`weather.storm.wind`** — Storm wind howling. Loops.
  - Target length: ~8.0s
  - Prompt: `Powerful storm wind howling and gusting hard, continuous roaring blasts, clean field recording, no music`

- [x] **`weather.thunder.distant`** — Thunder rolls far away.
  - Target length: ~3.5s
  - Prompt: `Distant thunder rolling across the sky, long low rumbling growl with no hard crack`

- [x] **`door.wood.open`** — A wooden door opens.
  - Target length: ~1.3s · generate **2 takes** (`door.wood.open.1.wav`, `door.wood.open.2.wav`, …)
  - Prompt: `Wooden door swinging open on dry hinges, loud creaking with a final knock, recorded close`

- [x] **`door.metal.open`** — A heavy metal door opens.
  - Target length: ~1.6s
  - Prompt: `Heavy steel industrial door being pushed open, loud grinding metal with a booming echo, recorded close`

- [x] **`door.slide`** — A sliding door runs on its track.
  - Target length: ~1.4s
  - Prompt: `Sliding glass door running along its track and stopping, rolling wheels with a final bump, recorded close`

- [x] **`door.knock`** — Someone knocks.
  - Target length: ~1.2s · generate **2 takes** (`door.knock.1.wav`, `door.knock.2.wav`, …)
  - Prompt: `Firm knuckles knocking three times on a solid wooden door, loud and close, dry recording`

- [x] **`door.bell`** — A doorbell rings.
  - Target length: ~2.0s
  - Prompt: `Classic two tone doorbell chiming, ringing ding dong with a ringing decay, recorded close`

- [x] **`door.locked`** — A locked door rattles.
  - Target length: ~1.2s · generate **2 takes** (`door.locked.1.wav`, `door.locked.2.wav`, …)
  - Prompt: `Locked door handle being rattled hard without opening, metallic clattering, recorded close`

- [x] **`door.slam`** — A door slams shut.
  - Target length: ~1.2s · generate **2 takes** (`door.slam.1.wav`, `door.slam.2.wav`, …)
  - Prompt: `Wooden door being slammed shut hard, explosive booming bang with the frame rattling, recorded close`

- [x] **`horror.scream`** — A terrified scream.
  - Target length: ~2.0s
  - Prompt: `Terrified human scream of fear, loud shrieking wail, wordless, no speech, dry close recording`

- [x] **`horror.growl.deep`** — Something very large growls in the dark.
  - Target length: ~2.5s
  - Prompt: `Enormous creature growling deep in the dark, low rumbling menacing throat, wordless, recorded close`

- [x] **`horror.musicbox`** — A music box plays — classic dread.
  - Target length: ~4.0s
  - Prompt: `Old wind up music box playing a slow simple lullaby, delicate metallic chimes slightly out of tune, recorded close`

- [x] **`horror.knock.slow`** — Slow deliberate knocking.
  - Target length: ~2.5s
  - Prompt: `Three slow heavy knocks on a distant wooden door, ominous and deliberate, hollow room`

- [x] **`horror.laugh`** — An unsettling laugh.
  - Target length: ~2.0s
  - Prompt: `Sinister low laughter, slow menacing chuckle, wordless, no speech, dry close recording`

- [x] **`horror.static`** — Radio or TV static. Loops.
  - Target length: ~4.0s
  - Prompt: `Radio static hissing with occasional crackling interference, continuous, recorded close`

- [x] **`kitchen.kettle`** — A kettle comes to the boil.
  - Target length: ~3.0s
  - Prompt: `Metal kettle heating and whistling as it comes to the boil, rising steam whistle, recorded close`

- [x] **`kitchen.microwave`** — A microwave finishes and beeps.
  - Target length: ~1.5s
  - Prompt: `Microwave oven beeping three times when finished, clear electronic tones, recorded close`

- [x] **`kitchen.blender`** — A blender runs.
  - Target length: ~2.5s
  - Prompt: `Kitchen blender running at high speed grinding ice, loud motor whine with rattling, recorded close`

- [x] **`kitchen.egg.crack`** — An egg is cracked.
  - Target length: ~0.8s · generate **2 takes** (`kitchen.egg.crack.1.wav`, `kitchen.egg.crack.2.wav`, …)
  - Prompt: `Egg being cracked on the edge of a bowl and opened, brittle shell crack with a wet slop, recorded close`

- [x] **`kitchen.can.open`** — A drink can is opened.
  - Target length: ~1.0s · generate **2 takes** (`kitchen.can.open.1.wav`, `kitchen.can.open.2.wav`, …)
  - Prompt: `Aluminium drink can being opened, ringing metallic crack with a hissing fizz, recorded close`

- [x] **`kitchen.bottle.open`** — A bottle is uncorked or opened.
  - Target length: ~1.0s · generate **2 takes** (`kitchen.bottle.open.1.wav`, `kitchen.bottle.open.2.wav`, …)
  - Prompt: `Cork being pulled from a glass bottle, deep hollow pop, recorded close`

- [x] **`kitchen.cutlery`** — Cutlery clatters on a plate.
  - Target length: ~1.0s · generate **2 takes** (`kitchen.cutlery.1.wav`, `kitchen.cutlery.2.wav`, …)
  - Prompt: `Metal knife and fork clattering onto a ceramic plate, ringing clinking, recorded close`

- [x] **`kitchen.sip`** — A drink is sipped.
  - Target length: ~1.0s · generate **2 takes** (`kitchen.sip.1.wav`, `kitchen.sip.2.wav`, …)
  - Prompt: `Person taking a sip of a drink and swallowing, wet gulp, recorded close`

- [x] **`office.printer`** — A printer prints a page.
  - Target length: ~3.0s
  - Prompt: `Office printer feeding and printing a sheet of paper, mechanical whirring with paper rollers, recorded close`

- [x] **`office.drawer`** — A drawer opens or closes.
  - Target length: ~1.2s · generate **2 takes** (`office.drawer.1.wav`, `office.drawer.2.wav`, …)
  - Prompt: `Wooden desk drawer being pulled open and pushed shut, sliding wood with a final knock, recorded close`

- [x] **`office.stapler`** — A stapler clicks.
  - Target length: ~0.6s · generate **2 takes** (`office.stapler.1.wav`, `office.stapler.2.wav`, …)
  - Prompt: `Desk stapler being pressed down firmly, ringing metallic punch, recorded close`

- [x] **`animal.dog.growl`** — A dog growls a warning.
  - Target length: ~1.5s · generate **2 takes** (`animal.dog.growl.1.wav`, `animal.dog.growl.2.wav`, …)
  - Prompt: `Dog growling low in warning, rumbling threatening throat, recorded close`

- [x] **`animal.cat.purr`** — A cat purrs. Loops.
  - Target length: ~4.0s
  - Prompt: `Cat purring contentedly, continuous soft rumbling vibration, microphone close to the cat`

- [x] **`animal.cat.hiss`** — A cat hisses.
  - Target length: ~1.0s · generate **2 takes** (`animal.cat.hiss.1.wav`, `animal.cat.hiss.2.wav`, …)
  - Prompt: `Angry cat hissing sharply, sudden air hiss with a spit, recorded close`

- [x] **`animal.bird.flap`** — Wings beat as a bird takes off.
  - Target length: ~1.2s · generate **2 takes** (`animal.bird.flap.1.wav`, `animal.bird.flap.2.wav`, …)
  - Prompt: `Large bird taking off with heavy wing beats, flapping feathers pushing air, recorded close`

- [x] **`animal.rooster`** — A rooster crows — morning, farm.
  - Target length: ~1.8s
  - Prompt: `Rooster crowing loudly at dawn, full cock a doodle doo, outdoor farm recording`

- [x] **`animal.lion.roar`** — A lion roars.
  - Target length: ~2.5s
  - Prompt: `Lion roaring powerfully, deep full throated roar, recorded close`

- [x] **`animal.bear.growl`** — A bear growls.
  - Target length: ~2.0s
  - Prompt: `Large bear growling threateningly, deep guttural rumble, recorded close`

- [x] **`animal.owl`** — An owl hoots at night.
  - Target length: ~1.8s
  - Prompt: `Owl hooting twice in a quiet night forest, clear low hoots, outdoor recording`

- [x] **`animal.seagull`** — Seagulls call — coast, harbour.
  - Target length: ~1.8s
  - Prompt: `Seagulls calling loudly by the sea, hard squawking cries, outdoor coastal recording`

- [x] **`animal.horse.gallop`** — A horse gallops. Loops.
  - Target length: ~4.0s
  - Prompt: `Horse galloping fast on packed dirt, continuous rhythmic hoofbeats, outdoor recording`

- [x] **`sport.golf`** — A golf club strikes the ball.
  - Target length: ~0.8s · generate **2 takes** (`sport.golf.1.wav`, `sport.golf.2.wav`, …)
  - Prompt: `Golf driver striking a ball off a tee, hard cracking impact, outdoor recording`

- [x] **`sport.bowling`** — A bowling ball hits the pins.
  - Target length: ~2.5s
  - Prompt: `Bowling ball rolling down a lane and smashing into the pins, rumbling roll with a clattering strike`

- [x] **`sport.pool.break`** — A pool break scatters the balls.
  - Target length: ~2.0s
  - Prompt: `Pool cue breaking a rack of billiard balls, hard crack with balls scattering across the table`

- [x] **`sport.boxing.bell`** — The boxing bell rings a round.
  - Target length: ~2.0s
  - Prompt: `Boxing ring bell struck three times, loud ringing metallic clangs with ringing decay`

- [x] **`sport.skate`** — A skateboard rolls and grinds.
  - Target length: ~2.0s
  - Prompt: `Skateboard rolling on concrete then grinding along a metal rail, rumbling wheels with harsh scraping`

- [x] **`sport.ski`** — Skis carve through snow. Loops.
  - Target length: ~4.0s
  - Prompt: `Skis carving through packed snow at speed, continuous scraping hiss, outdoor recording`

- [x] **`sport.crowd.goal`** — The crowd erupts at a goal.
  - Target length: ~3.0s
  - Prompt: `Stadium crowd erupting into a huge roar and cheering after a goal, outdoor stadium recording`

- [x] **`sport.stadium`** — Stadium crowd ambience. Loops.
  - Target length: ~6.0s
  - Prompt: `Large stadium crowd murmuring and occasionally cheering, continuous background, outdoor recording`

- [x] **`casino.reel.spin`** — A slot reel starts spinning. Loops while it runs.
  - Target length: ~10.0s
  - Prompt: `Casino slot machine reels spinning continuously, mechanical whirring clatter, recorded close`

- [x] **`casino.reel.stop`** — One slot reel lands.
  - Target length: ~0.6s · generate **3 takes** (`casino.reel.stop.1.wav`, `casino.reel.stop.2.wav`, …)
  - Prompt: `Casino slot machine reel stopping with a solid mechanical clunk, recorded close`

- [x] **`casino.lever`** — The slot lever is pulled.
  - Target length: ~0.9s
  - Prompt: `Casino slot machine lever being pulled down and released, heavy spring loaded mechanism, recorded close`

- [x] **`casino.roulette.spin`** — The roulette wheel spins. Loops.
  - Target length: ~3.0s
  - Prompt: `Roulette wheel spinning steadily with the ball rattling around the rim, continuous, recorded close`

- [x] **`casino.roulette.drop`** — The roulette ball settles into a pocket.
  - Target length: ~1.2s · generate **2 takes** (`casino.roulette.drop.1.wav`, `casino.roulette.drop.2.wav`, …)
  - Prompt: `Roulette ball dropping and bouncing into a numbered pocket, wooden clattering settle, recorded close`

- [x] **`casino.chips.stack`** — Chips are stacked or counted.
  - Target length: ~1.0s · generate **3 takes** (`casino.chips.stack.1.wav`, `casino.chips.stack.2.wav`, …)
  - Prompt: `Stack of clay casino chips being riffled and stacked in one hand, clicking clatter, recorded close`

- [x] **`casino.chips.toss`** — Chips are pushed into the pot.
  - Target length: ~0.9s · generate **3 takes** (`casino.chips.toss.1.wav`, `casino.chips.toss.2.wav`, …)
  - Prompt: `Handful of clay casino chips being tossed onto a felt table, scattering clatter, recorded close`

- [x] **`casino.card.deal`** — One card is dealt.
  - Target length: ~0.5s · generate **4 takes** (`casino.card.deal.1.wav`, `casino.card.deal.2.wav`, …)
  - Prompt: `Single playing card being dealt across a felt table, paper slide with a soft landing, recorded close`

- [x] **`casino.card.flip`** — A card is turned face up.
  - Target length: ~0.4s · generate **3 takes** (`casino.card.flip.1.wav`, `casino.card.flip.2.wav`, …)
  - Prompt: `Single playing card being flipped face up on a table, quick paper snap, recorded close`

- [x] **`casino.dice.roll`** — Dice are thrown.
  - Target length: ~1.4s · generate **3 takes** (`casino.dice.roll.1.wav`, `casino.dice.roll.2.wav`, …)
  - Prompt: `Two dice being thrown and tumbling across a felt table before settling, recorded close`

- [x] **`casino.dice.shake`** — Dice rattle in a cup.
  - Target length: ~1.2s · generate **2 takes** (`casino.dice.shake.1.wav`, `casino.dice.shake.2.wav`, …)
  - Prompt: `Dice being shaken hard inside a leather cup, rattling clatter, recorded close`

- [x] **`casino.payout`** — Coins pour out of a machine.
  - Target length: ~2.5s
  - Prompt: `Casino machine paying out a flood of metal coins into a tray, cascading clattering, recorded close`

- [x] **`casino.bell`** — The win bell rings.
  - Target length: ~2.0s
  - Prompt: `Casino jackpot bell ringing rapidly and repeatedly, metallic clanging, recorded close`

- [x] **`casino.ambience`** — Casino floor ambience. Loops.
  - Target length: ~6.0s
  - Prompt: `Busy casino floor with distant machines chiming and people talking, continuous background, no music`

- [x] **`puzzle.tile.place`** — A tile is set down on the board.
  - Target length: ~0.4s · generate **3 takes** (`puzzle.tile.place.1.wav`, `puzzle.tile.place.2.wav`, …)
  - Prompt: `Wooden game tile being placed firmly onto a wooden board, solid knock, recorded close`

- [x] **`puzzle.tile.slide`** — A tile slides to a new position.
  - Target length: ~0.5s · generate **3 takes** (`puzzle.tile.slide.1.wav`, `puzzle.tile.slide.2.wav`, …)
  - Prompt: `Wooden tile sliding across a smooth wooden board, short scraping glide, recorded close`

- [x] **`puzzle.snap`** — A piece snaps into place.
  - Target length: ~0.4s · generate **3 takes** (`puzzle.snap.1.wav`, `puzzle.snap.2.wav`, …)
  - Prompt: `Two interlocking plastic puzzle pieces snapping together, clean click, recorded close`

- [x] **`puzzle.jigsaw`** — A jigsaw piece seats correctly.
  - Target length: ~0.5s · generate **3 takes** (`puzzle.jigsaw.1.wav`, `puzzle.jigsaw.2.wav`, …)
  - Prompt: `Cardboard jigsaw piece being pressed into place among others, soft fibrous click, recorded close`

- [x] **`puzzle.domino`** — Dominoes topple.
  - Target length: ~2.0s
  - Prompt: `Line of dominoes toppling over one after another, rapid clattering cascade, recorded close`

- [x] **`puzzle.chess`** — A chess piece is moved.
  - Target length: ~0.5s · generate **3 takes** (`puzzle.chess.1.wav`, `puzzle.chess.2.wav`, …)
  - Prompt: `Weighted wooden chess piece being set down on a board, solid felted knock, recorded close`

- [x] **`puzzle.rotate`** — A block or piece rotates.
  - Target length: ~0.3s · generate **3 takes** (`puzzle.rotate.1.wav`, `puzzle.rotate.2.wav`, …)
  - Prompt: `Small mechanical ratchet turning one notch, single clean click, recorded close`

- [x] **`puzzle.lock`** — A piece locks into the grid permanently.
  - Target length: ~0.5s · generate **2 takes** (`puzzle.lock.1.wav`, `puzzle.lock.2.wav`, …)
  - Prompt: `Metal bolt sliding home into a latch, firm mechanical seat, recorded close`

- [x] **`puzzle.line.clear`** — A full row or line clears.
  - Target length: ~0.9s · generate **2 takes** (`puzzle.line.clear.1.wav`, `puzzle.line.clear.2.wav`, …)
  - Prompt: `Row of glass blocks shattering and sweeping away, ringing crystalline collapse, recorded close`

- [x] **`puzzle.hint`** — A hint is revealed.
  - Target length: ~0.8s
  - Prompt: `Gentle magical chime revealing a clue, soft glassy shimmer rising, recorded close`

- [x] **`puzzle.undo`** — A move is taken back.
  - Target length: ~0.5s
  - Prompt: `Short reversed tape rewind whoosh, quick backwards sweep, clean recording`

- [x] **`puzzle.reset`** — The board is cleared and reset.
  - Target length: ~1.2s
  - Prompt: `Handful of wooden game tiles being swept off a board into a box, rattling scatter, recorded close`

- [x] **`puzzle.correct`** — A correct answer or valid move.
  - Target length: ~0.8s
  - Prompt: `Warm rising two note chime confirming a correct answer, clean bell tone, recorded close`

- [x] **`puzzle.wrong`** — A wrong answer or invalid move.
  - Target length: ~0.8s
  - Prompt: `Gentle descending two note buzz for a wrong answer, soft and not harsh, clean recording`

- [x] **`puzzle.timer`** — Timer pressure ticking. Loops.
  - Target length: ~3.0s
  - Prompt: `Fast mechanical timer ticking under pressure, continuous urgent ticks, recorded close`

- [x] **`puzzle.bomb.tick`** — A bomb tile counts down.
  - Target length: ~0.5s · generate **2 takes** (`puzzle.bomb.tick.1.wav`, `puzzle.bomb.tick.2.wav`, …)
  - Prompt: `Burning fuse hissing and sparking on a bomb, short crackling burn, recorded close`

- [x] **`plat.spring`** — A spring or bounce pad launches the player.
  - Target length: ~0.8s · generate **3 takes** (`plat.spring.1.wav`, `plat.spring.2.wav`, …)
  - Prompt: `Metal coil spring being compressed and released with a boing, cartoon style, recorded close`

- [x] **`plat.trampoline`** — A trampoline bounce.
  - Target length: ~0.9s · generate **2 takes** (`plat.trampoline.1.wav`, `plat.trampoline.2.wav`, …)
  - Prompt: `Trampoline fabric stretching and snapping back as someone bounces, deep elastic thump, recorded close`

- [x] **`plat.platform.move`** — A moving platform travels. Loops.
  - Target length: ~3.0s
  - Prompt: `Heavy mechanical platform grinding along a track, continuous low rumbling motor, recorded close`

- [x] **`plat.crumble`** — A block crumbles under the player.
  - Target length: ~1.0s · generate **2 takes** (`plat.crumble.1.wav`, `plat.crumble.2.wav`, …)
  - Prompt: `Stone block cracking and crumbling apart into rubble, recorded close`

- [x] **`plat.conveyor`** — A conveyor belt carries the player. Loops.
  - Target length: ~3.0s
  - Prompt: `Rubber conveyor belt running over rollers, continuous mechanical whirring, recorded close`

- [x] **`plat.spikes`** — Spikes shoot up from the floor.
  - Target length: ~0.7s · generate **2 takes** (`plat.spikes.1.wav`, `plat.spikes.2.wav`, …)
  - Prompt: `Metal spikes shooting up fast through a stone floor, scraping steel with a hard clank, recorded close`

- [x] **`plat.sawblade`** — A spinning saw blade. Loops.
  - Target length: ~10.0s
  - Prompt: `Large circular saw blade spinning fast in the air, continuous metallic whirring whine, recorded close`

- [x] **`plat.checkpoint`** — A checkpoint flag raises.
  - Target length: ~1.4s
  - Prompt: `Cloth flag being hoisted quickly up a metal pole, fabric snap with a mechanical ratchet, recorded close`

- [x] **`plat.key`** — A key is collected.
  - Target length: ~0.8s · generate **2 takes** (`plat.key.1.wav`, `plat.key.2.wav`, …)
  - Prompt: `Small metal key being picked up with a loud ringing jingle, recorded close`

- [x] **`plat.lock.open`** — A lock opens and a door swings free.
  - Target length: ~1.4s
  - Prompt: `Heavy iron padlock unlocking and falling open, mechanical clunk with chain rattle, recorded close`

- [x] **`plat.ledge`** — The player grabs a ledge.
  - Target length: ~0.6s · generate **3 takes** (`plat.ledge.1.wav`, `plat.ledge.2.wav`, …)
  - Prompt: `Hands slapping and gripping a stone ledge, gritty scrape with cloth, recorded close`

- [x] **`plat.wallslide`** — Sliding down a wall.
  - Target length: ~1.4s
  - Prompt: `Cloth and boots sliding down a rough concrete wall, sustained scraping friction, recorded close`

- [x] **`plat.ladder`** — Climbing a ladder rung.
  - Target length: ~0.5s · generate **4 takes** (`plat.ladder.1.wav`, `plat.ladder.2.wav`, …)
  - Prompt: `Boot stepping onto a metal ladder rung, hollow metallic clank, recorded close`

- [x] **`plat.rope.swing`** — Swinging on a rope.
  - Target length: ~1.5s
  - Prompt: `Thick rope creaking under load as it swings through the air, fibrous strain with wind, recorded close`

- [x] **`plat.portal.enter`** — The player enters a pipe or portal.
  - Target length: ~1.0s
  - Prompt: `Body being sucked quickly down a hollow pipe, descending whooshing slide, cartoon style, recorded close`

- [x] **`plat.coin.block`** — Hitting a block that gives a reward.
  - Target length: ~0.7s · generate **2 takes** (`plat.coin.block.1.wav`, `plat.coin.block.2.wav`, …)
  - Prompt: `Fist punching up into a hollow wooden crate, solid knock with a small rattle inside, recorded close`

- [x] **`plat.life.lost`** — The player loses a life.
  - Target length: ~1.4s
  - Prompt: `Cartoon character falling with a descending comic slide whistle ending in a soft thud, playful`

- [x] **`plat.powerup.grow`** — The character grows or powers up.
  - Target length: ~1.2s
  - Prompt: `Cartoon magical growth sound, rising bubbling swell with a ringing pop at the peak, playful`

- [x] **`tower.build`** — A tower or building is placed.
  - Target length: ~1.0s · generate **2 takes** (`tower.build.1.wav`, `tower.build.2.wav`, …)
  - Prompt: `Stone and timber structure being dropped into place and settling, heavy thud with debris, recorded close`

- [x] **`tower.sell`** — A tower is sold or demolished.
  - Target length: ~1.2s
  - Prompt: `Small wooden structure collapsing into a pile with coins jingling, recorded close`

- [x] **`tower.upgrade`** — A tower levels up.
  - Target length: ~1.2s
  - Prompt: `Magical upgrade surge, rising metallic ring with a ringing energetic swell, recorded close`

- [x] **`tower.unit.spawn`** — An enemy unit enters the field.
  - Target length: ~0.8s · generate **2 takes** (`tower.unit.spawn.1.wav`, `tower.unit.spawn.2.wav`, …)
  - Prompt: `Creature stepping out of a portal with a wet organic squelch and a low growl, recorded close`

- [x] **`tower.unit.march`** — A column of units marches. Loops.
  - Target length: ~3.0s
  - Prompt: `Column of armoured soldiers marching in step on dirt, continuous rhythmic boots and armour, recorded close`

- [x] **`tower.unit.die`** — A unit is destroyed.
  - Target length: ~0.9s · generate **3 takes** (`tower.unit.die.1.wav`, `tower.unit.die.2.wav`, …)
  - Prompt: `Creature being defeated with a short guttural cry and a wet collapse, cartoon style not gory`

- [x] **`tower.wave`** — A new wave is incoming.
  - Target length: ~2.2s
  - Prompt: `Deep war horn sounding a long warning call across a battlefield, ominous and loud`

- [x] **`tower.base.damage`** — The player's base takes damage.
  - Target length: ~1.4s · generate **2 takes** (`tower.base.damage.1.wav`, `tower.base.damage.2.wav`, …)
  - Prompt: `Heavy stone wall being struck and cracking with an alarm bell behind it, recorded close`

- [x] **`tower.repair`** — A structure is repaired.
  - Target length: ~1.4s
  - Prompt: `Quick hammering and sawing repairing a wooden structure, busy workshop burst, recorded close`

- [x] **`tower.target`** — A tower locks onto a target.
  - Target length: ~0.5s · generate **2 takes** (`tower.target.1.wav`, `tower.target.2.wav`, …)
  - Prompt: `Mechanical turret swivelling and locking into position, servo whir with a clunk, recorded close`

- [x] **`idle.tap`** — The main tap in a clicker. Fires constantly.
  - Target length: ~0.25s · generate **5 takes** (`idle.tap.1.wav`, `idle.tap.2.wav`, …)
  - Prompt: `Finger tapping firmly on a taut drum skin, short punchy thump, recorded close`

- [x] **`idle.prestige`** — A prestige or rebirth reset.
  - Target length: ~2.8s
  - Prompt: `Grand magical ascension, deep swelling rush rising into a radiant shimmering bloom, triumphant`

- [x] **`idle.offline`** — Offline earnings are collected on return.
  - Target length: ~2.0s
  - Prompt: `Large pile of coins cascading into a chest with a warm confirming chime, recorded close`

- [x] **`idle.autocollect`** — An automated collector picks something up.
  - Target length: ~0.6s · generate **3 takes** (`idle.autocollect.1.wav`, `idle.autocollect.2.wav`, …)
  - Prompt: `Small mechanical claw grabbing an object with a servo whir and a click, recorded close`

- [x] **`idle.multiplier`** — A multiplier increases.
  - Target length: ~0.9s · generate **2 takes** (`idle.multiplier.1.wav`, `idle.multiplier.2.wav`, …)
  - Prompt: `Rising electronic power surge with a clear confirming ping at the top, clean recording`

- [x] **`idle.milestone`** — A milestone number is reached.
  - Target length: ~1.8s
  - Prompt: `Celebratory burst of bells and a small cheer with sparkling shimmer, warm and rewarding`

- [x] **`idle.upgrade.chain`** — Several upgrades buy at once.
  - Target length: ~1.6s
  - Prompt: `Rapid series of mechanical switches and confirming pings in quick succession, recorded close`

- [x] **`idle.generator`** — A generator or factory runs. Loops.
  - Target length: ~10.0s
  - Prompt: `Small mechanical generator chugging steadily, continuous rhythmic machinery, recorded close`

- [x] **`idle.coin.rain`** — Coins rain down after a big gain.
  - Target length: ~2.2s
  - Prompt: `Hundreds of metal coins raining down onto a hard surface, dense cascading clatter, recorded close`

- [x] **`idle.levelup`** — A generator or hero levels up.
  - Target length: ~1.2s
  - Prompt: `Warm rising four note bell flourish with a soft magical sparkle, rewarding and short`

- [x] **`shop.wheel.spin`** — A prize wheel spins. Loops.
  - Target length: ~10.0s
  - Prompt: `Large prize wheel spinning with a flapper ticking rapidly over the pegs, continuous, recorded close`

- [x] **`rest.order.bell`** — The order-up bell rings.
  - Target length: ~1.2s · generate **2 takes** (`rest.order.bell.1.wav`, `rest.order.bell.2.wav`, …)
  - Prompt: `Counter service bell being struck once, ringing metallic ding with a ringing decay, recorded close`

- [x] **`rest.register`** — The till opens and rings.
  - Target length: ~1.6s
  - Prompt: `Old mechanical cash register ringing and the drawer sliding open with a clunk, recorded close`

- [x] **`rest.receipt`** — A receipt prints.
  - Target length: ~1.4s
  - Prompt: `Thermal receipt printer buzzing out a paper slip and tearing it off, recorded close`

- [x] **`rest.coffee`** — An espresso machine runs.
  - Target length: ~2.5s
  - Prompt: `Espresso machine grinding then extracting coffee with a steam hiss, recorded close`

- [x] **`rest.grill`** — Food hits a hot grill. Loops.
  - Target length: ~3.0s
  - Prompt: `Meat sizzling continuously on a hot griddle, steady fat crackling, recorded close`

- [x] **`rest.fryer`** — A basket goes into the deep fryer.
  - Target length: ~2.0s
  - Prompt: `Basket of food being lowered into hot oil with a violent bubbling roar, recorded close`

- [x] **`rest.plate`** — A plate is set down on a counter.
  - Target length: ~0.7s · generate **3 takes** (`rest.plate.1.wav`, `rest.plate.2.wav`, …)
  - Prompt: `Ceramic plate being set down firmly on a hard counter, solid clink, recorded close`

- [x] **`rest.icecream`** — Soft ice cream is dispensed.
  - Target length: ~1.8s
  - Prompt: `Soft serve ice cream machine dispensing with a motor whir and a wet squelch, recorded close`

- [x] **`rest.customer.happy`** — A customer is satisfied.
  - Target length: ~1.4s · generate **2 takes** (`rest.customer.happy.1.wav`, `rest.customer.happy.2.wav`, …)
  - Prompt: `Cheerful short hum of approval from a person with a small coin tip landing, wordless, recorded close`

- [x] **`rest.customer.angry`** — A customer gives up and leaves.
  - Target length: ~1.4s · generate **2 takes** (`rest.customer.angry.1.wav`, `rest.customer.angry.2.wav`, …)
  - Prompt: `Annoyed huff from a person and a chair scraping as they stand and walk off, wordless, recorded close`

- [x] **`rest.chop.fast`** — Rapid prep chopping.
  - Target length: ~1.6s
  - Prompt: `Chef chopping vegetables rapidly on a wooden board, fast rhythmic knife work, recorded close`

- [x] **`rest.pour.drink`** — A drink is poured into a glass.
  - Target length: ~1.6s
  - Prompt: `Fizzy drink being poured into a glass over ice, glugging with crackling bubbles, recorded close`

- [x] **`build.crane`** — A crane lifts a load. Loops.
  - Target length: ~3.0s
  - Prompt: `Construction crane winch motor running with cables under load, continuous mechanical grind`

- [x] **`build.bulldozer`** — A bulldozer pushes earth. Loops.
  - Target length: ~3.0s
  - Prompt: `Bulldozer engine working hard with steel tracks grinding over rubble, continuous`

- [x] **`build.jackhammer`** — A jackhammer breaks concrete. Loops.
  - Target length: ~10.0s
  - Prompt: `Pneumatic jackhammer hammering into concrete, continuous rapid pounding, recorded close`

- [x] **`build.cement`** — A cement mixer turns. Loops.
  - Target length: ~10.0s
  - Prompt: `Cement mixer drum turning with gravel tumbling inside, continuous rumbling, recorded close`

- [x] **`build.weld`** — Welding sparks.
  - Target length: ~1.8s · generate **2 takes** (`build.weld.1.wav`, `build.weld.2.wav`, …)
  - Prompt: `Arc welder striking and running a bead on steel, electrical crackling buzz, recorded close`

- [x] **`build.brick`** — A brick is laid in mortar.
  - Target length: ~0.7s · generate **3 takes** (`build.brick.1.wav`, `build.brick.2.wav`, …)
  - Prompt: `Clay brick being set into wet mortar and tapped level with a trowel, recorded close`

- [x] **`build.glass.fit`** — A pane of glass is fitted.
  - Target length: ~1.2s
  - Prompt: `Large glass pane being lifted and seated into a frame with a squeak and a settle, recorded close`

- [x] **`build.scaffold`** — Scaffolding poles clang together.
  - Target length: ~1.2s · generate **2 takes** (`build.scaffold.1.wav`, `build.scaffold.2.wav`, …)
  - Prompt: `Steel scaffolding poles being slotted together and clamped, ringing metallic clangs, recorded close`

- [x] **`build.measure`** — A tape measure snaps back.
  - Target length: ~0.9s · generate **2 takes** (`build.measure.1.wav`, `build.measure.2.wav`, …)
  - Prompt: `Steel tape measure being pulled out and snapping back into its case, recorded close`

- [x] **`build.complete`** — A building finishes construction.
  - Target length: ~2.0s
  - Prompt: `Construction completing, final hammer strikes with a satisfying settling thud and a warm confirming chime`

- [x] **`build.saw.power`** — A circular saw cuts timber.
  - Target length: ~1.8s
  - Prompt: `Electric circular saw ripping through a timber plank, rising motor whine with wood, recorded close`

- [x] **`build.nail.gun`** — A nail gun fires.
  - Target length: ~0.5s · generate **3 takes** (`build.nail.gun.1.wav`, `build.nail.gun.2.wav`, …)
  - Prompt: `Pneumatic nail gun firing a nail into timber, hard air-driven crack, recorded close`

- [x] **`med.gate`** — A castle gate opens.
  - Target length: ~3.0s
  - Prompt: `Enormous wooden castle gate grinding open on iron hinges, deep groaning creak, recorded close`

- [x] **`med.drawbridge`** — A drawbridge lowers.
  - Target length: ~3.0s
  - Prompt: `Heavy drawbridge chains clanking as the bridge lowers and crashes down, recorded close`

- [x] **`med.portcullis`** — A portcullis drops.
  - Target length: ~2.0s
  - Prompt: `Iron portcullis dropping fast down its runners and slamming into stone, recorded close`

- [x] **`med.catapult`** — A catapult launches.
  - Target length: ~1.8s
  - Prompt: `Wooden catapult arm releasing under tension with a groaning snap and rope whip, recorded close`

- [x] **`med.siege.impact`** — A boulder smashes a wall.
  - Target length: ~2.2s
  - Prompt: `Huge boulder smashing into a stone castle wall, massive crunching impact with falling rubble`

- [x] **`med.arrow.volley`** — A volley of arrows flies.
  - Target length: ~1.8s
  - Prompt: `Volley of many arrows being loosed together and whistling through the air, recorded outdoors`

- [x] **`med.arrow.hit`** — An arrow strikes wood.
  - Target length: ~0.6s · generate **3 takes** (`med.arrow.hit.1.wav`, `med.arrow.hit.2.wav`, …)
  - Prompt: `Arrow striking a wooden target with a solid thunk and a quivering shaft, recorded close`

- [x] **`med.torch.mount`** — A torch is taken from a wall.
  - Target length: ~1.0s · generate **2 takes** (`med.torch.mount.1.wav`, `med.torch.mount.2.wav`, …)
  - Prompt: `Burning torch being pulled from an iron wall bracket, metal scrape with flame flare, recorded close`

- [x] **`med.dungeon.door`** — A heavy dungeon door opens.
  - Target length: ~2.5s
  - Prompt: `Rusted iron dungeon door dragging open across stone, grinding metal with a deep echo`

- [x] **`med.chest.lock`** — A treasure chest is unlocked.
  - Target length: ~1.4s · generate **2 takes** (`med.chest.lock.1.wav`, `med.chest.lock.2.wav`, …)
  - Prompt: `Iron key turning in an old chest lock and the hasp springing open, recorded close`

- [x] **`med.coin.purse`** — A purse of coins is handled.
  - Target length: ~1.0s · generate **2 takes** (`med.coin.purse.1.wav`, `med.coin.purse.2.wav`, …)
  - Prompt: `Leather pouch of gold coins being shaken and set down, muffled metallic jingle, recorded close`

- [x] **`med.tavern`** — Tavern ambience. Loops.
  - Target length: ~6.0s
  - Prompt: `Busy medieval tavern with people talking and tankards clinking, continuous background, no music`

- [x] **`med.anvil`** — A smith strikes the anvil.
  - Target length: ~0.8s · generate **4 takes** (`med.anvil.1.wav`, `med.anvil.2.wav`, …)
  - Prompt: `Blacksmith hammer striking steel on an anvil, ringing metallic clang, recorded close`

- [x] **`med.scroll.open`** — A scroll is unrolled.
  - Target length: ~1.2s · generate **2 takes** (`med.scroll.open.1.wav`, `med.scroll.open.2.wav`, …)
  - Prompt: `Old parchment scroll being unrolled across a table, dry crackling paper, recorded close`

- [x] **`fish.cast`** — A fishing rod casts.
  - Target length: ~1.4s · generate **2 takes** (`fish.cast.1.wav`, `fish.cast.2.wav`, …)
  - Prompt: `Fishing rod casting with the line whistling out and the reel spinning free, recorded outdoors`

- [x] **`fish.reel.in`** — Reeling in. Loops.
  - Target length: ~10.0s
  - Prompt: `Fishing reel being wound in steadily, continuous mechanical ratcheting, recorded close`

- [x] **`fish.reel.fast`** — A fish runs and the drag screams.
  - Target length: ~2.0s
  - Prompt: `Fishing reel drag screaming as a fish runs with the line, fast ratcheting whir, recorded close`

- [x] **`fish.line.snap`** — The line breaks.
  - Target length: ~0.8s
  - Prompt: `Taut fishing line snapping under tension with a hard whipping recoil, recorded close`

- [x] **`fish.bob`** — A float bobs and dips.
  - Target length: ~0.9s · generate **3 takes** (`fish.bob.1.wav`, `fish.bob.2.wav`, …)
  - Prompt: `Fishing float dipping and bobbing in still water, small wet plops, recorded close`

- [x] **`fish.catch`** — A fish is landed.
  - Target length: ~1.6s · generate **2 takes** (`fish.catch.1.wav`, `fish.catch.2.wav`, …)
  - Prompt: `Fish breaking the surface and being lifted out of the water, big splash with flapping, recorded close`

- [x] **`fish.flop`** — A caught fish flaps about.
  - Target length: ~1.4s · generate **2 takes** (`fish.flop.1.wav`, `fish.flop.2.wav`, …)
  - Prompt: `Fish flapping wetly on a wooden boat deck, rapid slapping, recorded close`

- [x] **`fish.net`** — A landing net scoops.
  - Target length: ~1.0s · generate **2 takes** (`fish.net.1.wav`, `fish.net.2.wav`, …)
  - Prompt: `Landing net being swept through water and lifted out dripping, recorded close`

- [x] **`fish.tacklebox`** — A tackle box opens.
  - Target length: ~1.2s
  - Prompt: `Plastic tackle box being unclipped and opened with lures rattling inside, recorded close`

- [x] **`fish.water.calm`** — Calm lake water. Loops.
  - Target length: ~6.0s
  - Prompt: `Calm lake water lapping gently against a wooden boat, continuous, clean field recording, no music`

- [x] **`stealth.alert`** — A guard notices something.
  - Target length: ~1.2s
  - Prompt: `Tense alert sting, two rising dissonant string notes with a metallic edge, short and urgent`

- [x] **`stealth.detected`** — The player is spotted.
  - Target length: ~2.0s
  - Prompt: `Alarm being triggered on detection, harsh rising klaxon blast with a tense orchestral stab`

- [x] **`stealth.lost`** — The guard loses track and calms down.
  - Target length: ~1.8s
  - Prompt: `Tension releasing, falling string line settling into a calm sustained note, relieved`

- [x] **`stealth.radio`** — Radio chatter between guards.
  - Target length: ~2.0s · generate **2 takes** (`stealth.radio.1.wav`, `stealth.radio.2.wav`, …)
  - Prompt: `Two way radio crackling with muffled unintelligible chatter and static bursts, wordless, recorded close`

- [x] **`stealth.sneak`** — A slow careful footstep.
  - Target length: ~0.4s · generate **4 takes** (`stealth.sneak.1.wav`, `stealth.sneak.2.wav`, …)
  - Prompt: `Single very quiet careful footstep on a wooden floor, soft controlled weight shift, recorded close`

- [x] **`stealth.lockpick`** — A lock is picked.
  - Target length: ~2.0s
  - Prompt: `Lock being picked with metal tools, small scraping and tumbler clicks ending in a turn, recorded close`

- [x] **`stealth.vent`** — A vent grate is removed.
  - Target length: ~1.6s
  - Prompt: `Metal vent grate being unscrewed and lifted away, hollow metallic rattle, recorded close`

- [x] **`stealth.camera`** — A security camera pans.
  - Target length: ~1.4s · generate **2 takes** (`stealth.camera.1.wav`, `stealth.camera.2.wav`, …)
  - Prompt: `Security camera servo panning across a room and stopping, electric whir with a click, recorded close`

- [x] **`stealth.takedown`** — A silent takedown.
  - Target length: ~1.0s · generate **2 takes** (`stealth.takedown.1.wav`, `stealth.takedown.2.wav`, …)
  - Prompt: `Quick grappling struggle with cloth and a muffled body slump to the floor, recorded close`

- [x] **`stealth.hide`** — The player enters a hiding spot.
  - Target length: ~1.0s · generate **2 takes** (`stealth.hide.1.wav`, `stealth.hide.2.wav`, …)
  - Prompt: `Metal locker door being pulled shut from inside with a soft hollow clank, recorded close`

- [x] **`emote.taunt`** — A mocking taunt.
  - Target length: ~1.2s · generate **2 takes** (`emote.taunt.1.wav`, `emote.taunt.2.wav`, …)
  - Prompt: `Person making a short wordless mocking raspberry and hum, playful, recorded close`

- [x] **`emote.sigh`** — A weary sigh.
  - Target length: ~1.2s · generate **2 takes** (`emote.sigh.1.wav`, `emote.sigh.2.wav`, …)
  - Prompt: `Person letting out a long weary sigh, wordless, recorded close`

- [x] **`emote.oops`** — A small mistake reaction.
  - Target length: ~0.9s · generate **2 takes** (`emote.oops.1.wav`, `emote.oops.2.wav`, …)
  - Prompt: `Person making a short wordless oops sound of mild embarrassment, playful, recorded close`

- [x] **`body.sneeze`** — A sneeze.
  - Target length: ~1.0s · generate **2 takes** (`body.sneeze.1.wav`, `body.sneeze.2.wav`, …)
  - Prompt: `Person sneezing once loudly, wordless, recorded close`

- [x] **`body.cough`** — A cough.
  - Target length: ~1.0s · generate **2 takes** (`body.cough.1.wav`, `body.cough.2.wav`, …)
  - Prompt: `Person coughing twice, wordless, recorded close`

- [x] **`body.yawn`** — A yawn.
  - Target length: ~1.6s · generate **2 takes** (`body.yawn.1.wav`, `body.yawn.2.wav`, …)
  - Prompt: `Person yawning widely, wordless, recorded close`

- [x] **`body.sniff`** — A sniff.
  - Target length: ~0.7s · generate **2 takes** (`body.sniff.1.wav`, `body.sniff.2.wav`, …)
  - Prompt: `Person sniffing sharply through the nose twice, wordless, recorded close`

- [x] **`body.swallow`** — A nervous swallow.
  - Target length: ~0.7s · generate **2 takes** (`body.swallow.1.wav`, `body.swallow.2.wav`, …)
  - Prompt: `Person swallowing nervously, single wet gulp, recorded close`

- [x] **`body.stomach`** — A hungry stomach rumbles.
  - Target length: ~1.6s · generate **2 takes** (`body.stomach.1.wav`, `body.stomach.2.wav`, …)
  - Prompt: `Empty stomach rumbling and gurgling loudly, recorded very close`

- [x] **`body.shiver`** — Teeth chatter with cold.
  - Target length: ~1.4s · generate **2 takes** (`body.shiver.1.wav`, `body.shiver.2.wav`, …)
  - Prompt: `Person shivering with teeth chattering rapidly from cold, wordless, recorded close`

- [x] **`body.heartbeat.fast`** — A racing heartbeat. Loops.
  - Target length: ~3.0s
  - Prompt: `Human heart pounding very fast in panic, continuous rapid chest thuds, recorded very close`

- [x] **`body.knuckle`** — Knuckles crack before a fight.
  - Target length: ~0.8s · generate **2 takes** (`body.knuckle.1.wav`, `body.knuckle.2.wav`, …)
  - Prompt: `Person cracking their knuckles, series of small hard pops, recorded close`

- [x] **`body.footstep.bare`** — A barefoot step on a hard floor.
  - Target length: ~0.3s · generate **4 takes** (`body.footstep.bare.1.wav`, `body.footstep.bare.2.wav`, …)
  - Prompt: `Single bare foot slapping down on a hard tiled floor, wet skin contact, recorded close`

- [x] **`weather.hail`** — Hail hammers down. Loops.
  - Target length: ~6.0s
  - Prompt: `Hailstones hammering down hard on a roof, continuous rattling impacts, clean field recording, no music`

- [x] **`weather.blizzard`** — A blizzard howls. Loops.
  - Target length: ~8.0s
  - Prompt: `Blizzard howling with driving snow and hard wind gusts, continuous, clean field recording, no music`

- [x] **`weather.sandstorm`** — A sandstorm blows. Loops.
  - Target length: ~8.0s
  - Prompt: `Desert sandstorm with grit driving hard through the air, continuous hissing wind, clean field recording`

- [x] **`weather.foghorn`** — A fog horn sounds.
  - Target length: ~3.0s
  - Prompt: `Ship fog horn sounding one long deep blast across water, outdoor recording`

- [x] **`weather.earthquake`** — The ground shakes.
  - Target length: ~3.5s
  - Prompt: `Earthquake rumbling deeply with the ground shaking and objects rattling, powerful low roar`

- [x] **`weather.avalanche`** — An avalanche comes down.
  - Target length: ~3.5s
  - Prompt: `Avalanche of snow thundering down a mountainside, building roaring rush, outdoor recording`

- [x] **`weather.volcano`** — A volcano erupts.
  - Target length: ~4.0s
  - Prompt: `Volcano erupting with a huge explosive blast and a deep sustained magma roar`

- [x] **`weather.tornado`** — A tornado passes. Loops.
  - Target length: ~8.0s
  - Prompt: `Tornado roaring with violent swirling wind and debris, continuous, powerful`

- [x] **`weather.ice.crack`** — Ice cracks underfoot.
  - Target length: ~1.4s · generate **2 takes** (`weather.ice.crack.1.wav`, `weather.ice.crack.2.wav`, …)
  - Prompt: `Frozen lake ice cracking and splitting underfoot, brittle splintering, recorded close`

- [x] **`space.rocket.launch`** — A rocket lifts off.
  - Target length: ~4.0s
  - Prompt: `Rocket engines igniting and building to full thrust at liftoff, enormous roaring rumble`

- [x] **`space.stage.sep`** — Stage separation.
  - Target length: ~1.6s
  - Prompt: `Explosive bolts firing and a rocket stage separating, hard metallic bang with a rush`

- [x] **`space.docking`** — A docking clamp seals.
  - Target length: ~2.0s
  - Prompt: `Spacecraft docking clamps engaging and sealing with heavy metallic clunks and a pressure hiss`

- [x] **`space.airlock.cycle`** — An airlock cycles.
  - Target length: ~3.0s
  - Prompt: `Airlock cycling with air being pumped out and pressure equalising, long hissing drain`

- [x] **`space.oxygen.alarm`** — Low oxygen warning. Loops.
  - Target length: ~3.0s
  - Prompt: `Life support warning alarm beeping urgently and repeatedly, continuous electronic alert`

- [x] **`space.zero.g`** — Movement in zero gravity.
  - Target length: ~1.8s
  - Prompt: `Spacesuit fabric and hardware moving slowly with muffled breathing inside the helmet, microphone right against the suit, close and intimate`

- [x] **`space.cryo`** — A cryo pod opens.
  - Target length: ~2.5s
  - Prompt: `Cryogenic pod unsealing with a freezing pressure hiss and mechanical lid lift`

- [x] **`space.radar`** — A radar sweep pings.
  - Target length: ~1.6s · generate **2 takes** (`space.radar.1.wav`, `space.radar.2.wav`, …)
  - Prompt: `Submarine style radar sweeping with a single clear sonar ping and a long decay, clean recording`

- [x] **`space.hull.stress`** — The hull groans under stress.
  - Target length: ~3.0s
  - Prompt: `Large metal hull groaning and creaking under structural stress, deep ominous metallic bending`

- [x] **`space.thruster`** — A manoeuvring thruster fires.
  - Target length: ~1.0s · generate **3 takes** (`space.thruster.1.wav`, `space.thruster.2.wav`, …)
  - Prompt: `Short burst of compressed gas from a manoeuvring thruster, hard hissing puff`

- [x] **`space.beacon`** — A distress beacon pulses. Loops.
  - Target length: ~3.0s
  - Prompt: `Distress beacon pulsing a single repeating electronic tone, continuous, clean synthetic recording`

- [x] **`space.warp.charge`** — A jump drive spins up.
  - Target length: ~3.0s
  - Prompt: `Faster than light drive spooling up, rising electronic whine building with deep power, synthetic`

- [x] **`holiday.sleighbells`** — Sleigh bells jingle.
  - Target length: ~2.0s
  - Prompt: `Sleigh bells jingling rhythmically as a sled moves, ringing metallic shake, recorded close`

- [x] **`holiday.church.bells`** — Church bells peal.
  - Target length: ~4.0s
  - Prompt: `Church bells pealing together in celebration, layered ringing bronze, outdoor recording`

- [x] **`holiday.halloween.creak`** — A spooky creak.
  - Target length: ~2.5s
  - Prompt: `Old coffin lid creaking slowly open in a stone crypt, long groaning wood with a hollow echo`

- [x] **`holiday.organ`** — A pipe organ stab.
  - Target length: ~3.0s
  - Prompt: `Dramatic gothic pipe organ playing a dark sustained chord, grand and ominous`

- [x] **`holiday.wrapping`** — Wrapping paper is torn.
  - Target length: ~1.2s · generate **2 takes** (`holiday.wrapping.1.wav`, `holiday.wrapping.2.wav`, …)
  - Prompt: `Gift wrapping paper being torn open quickly, crackling paper tearing, recorded close`

## music

- [ ] **`music.casual.1`** — Match-3, puzzle and casual games. Light and friendly, never distracting.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.casual.2`** — Match-3, puzzle and casual games. Light and friendly, never distracting.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.casual.3`** — Match-3, puzzle and casual games. Light and friendly, never distracting.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.hypercasual.1`** — Hyper-casual games: one-tap, endless runner, arcade. Simple and driving.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.hypercasual.2`** — Hyper-casual games: one-tap, endless runner, arcade. Simple and driving.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.hypercasual.3`** — Hyper-casual games: one-tap, endless runner, arcade. Simple and driving.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.action.1`** — Shooters, brawlers and combat. Tense and driving without being oppressive.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.action.2`** — Shooters, brawlers and combat. Tense and driving without being oppressive.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.action.3`** — Shooters, brawlers and combat. Tense and driving without being oppressive.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.racing.1`** — Racing and driving games. High energy electronic.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.racing.2`** — Racing and driving games. High energy electronic.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.racing.3`** — Racing and driving games. High energy electronic.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.adventure.1`** — Adventure, exploration and RPG overworld.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.adventure.2`** — Adventure, exploration and RPG overworld.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.adventure.3`** — Adventure, exploration and RPG overworld.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.boss.1`** — Boss fights and final showdowns. The most intense music in the game.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.boss.2`** — Boss fights and final showdowns. The most intense music in the game.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.boss.3`** — Boss fights and final showdowns. The most intense music in the game.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.horror.1`** — Horror, survival and tension. Sparse and unsettling.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.horror.2`** — Horror, survival and tension. Sparse and unsettling.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.horror.3`** — Horror, survival and tension. Sparse and unsettling.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.cozy.1`** — Farming, idle, life sim and crafting. Warm and unhurried.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.cozy.2`** — Farming, idle, life sim and crafting. Warm and unhurried.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.cozy.3`** — Farming, idle, life sim and crafting. Warm and unhurried.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.scifi.1`** — Sci-fi, space and cyberpunk.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.scifi.2`** — Sci-fi, space and cyberpunk.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.scifi.3`** — Sci-fi, space and cyberpunk.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.menu.1`** — Main menu, lobby, shop and between-level screens.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.menu.2`** — Main menu, lobby, shop and between-level screens.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.menu.3`** — Main menu, lobby, shop and between-level screens.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.puzzle.1`** — Thinking music for puzzle games. Calmer than casual, no melody that pulls focus.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.puzzle.2`** — Thinking music for puzzle games. Calmer than casual, no melody that pulls focus.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.puzzle.3`** — Thinking music for puzzle games. Calmer than casual, no melody that pulls focus.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.tavern.1`** — Medieval inn, fantasy village, RPG rest stop.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.tavern.2`** — Medieval inn, fantasy village, RPG rest stop.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.tavern.3`** — Medieval inn, fantasy village, RPG rest stop.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.western.1`** — Deserts, duels, cowboy and frontier settings.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.western.2`** — Deserts, duels, cowboy and frontier settings.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.western.3`** — Deserts, duels, cowboy and frontier settings.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.tropical.1`** — Beach, island, summer and holiday settings.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.tropical.2`** — Beach, island, summer and holiday settings.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.tropical.3`** — Beach, island, summer and holiday settings.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.desert.1`** — Middle-Eastern and Arabian settings, markets, dunes.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.desert.2`** — Middle-Eastern and Arabian settings, markets, dunes.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.desert.3`** — Middle-Eastern and Arabian settings, markets, dunes.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.oriental.1`** — East-Asian settings, temples, gardens, martial arts.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.oriental.2`** — East-Asian settings, temples, gardens, martial arts.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.oriental.3`** — East-Asian settings, temples, gardens, martial arts.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.chiptune.1`** — Retro arcade and 8-bit styled games.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.chiptune.2`** — Retro arcade and 8-bit styled games.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.chiptune.3`** — Retro arcade and 8-bit styled games.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.lofi.1`** — Study, chill, idle and slow-burn games.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.lofi.2`** — Study, chill, idle and slow-burn games.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.lofi.3`** — Study, chill, idle and slow-burn games.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.epic.1`** — Trailers, cinematic reveals, big story moments.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.epic.2`** — Trailers, cinematic reveals, big story moments.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.epic.3`** — Trailers, cinematic reveals, big story moments.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.comedy.1`** — Cartoon slapstick, silly failures, funny moments.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.comedy.2`** — Cartoon slapstick, silly failures, funny moments.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.comedy.3`** — Cartoon slapstick, silly failures, funny moments.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.casino.1`** — Casino floors, card tables, lounge scenes.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.casino.2`** — Casino floors, card tables, lounge scenes.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.casino.3`** — Casino floors, card tables, lounge scenes.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.underwater.1`** — Submerged levels, dream sequences, floaty worlds.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.underwater.2`** — Submerged levels, dream sequences, floaty worlds.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.underwater.3`** — Submerged levels, dream sequences, floaty worlds.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.winter.1`** — Snow levels, festive seasons, ice worlds.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.winter.2`** — Snow levels, festive seasons, ice worlds.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.winter.3`** — Snow levels, festive seasons, ice worlds.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.zen.1`** — Meditation, calm puzzle, wellness, relaxation modes.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.zen.2`** — Meditation, calm puzzle, wellness, relaxation modes.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.zen.3`** — Meditation, calm puzzle, wellness, relaxation modes.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.chase.1`** — Pursuit, escape, timer running out.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.chase.2`** — Pursuit, escape, timer running out.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.chase.3`** — Pursuit, escape, timer running out.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.tension.1`** — Stealth, dread, the moment before something happens.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.tension.2`** — Stealth, dread, the moment before something happens.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`music.tension.3`** — Stealth, dread, the moment before something happens.
  - Target length: ~32s
  - Prompt: `—`

- [ ] **`sting.level.start`** — A level or round begins.
  - Target length: ~4s
  - Prompt: `—`

- [ ] **`sting.victory`** — The player wins. Short, not a loop.
  - Target length: ~5s
  - Prompt: `—`

- [ ] **`sting.defeat`** — The player loses.
  - Target length: ~5s
  - Prompt: `—`

- [ ] **`sting.gameover`** — The run is over for good.
  - Target length: ~6s
  - Prompt: `—`

- [ ] **`sting.levelup`** — The player levels up.
  - Target length: ~4s
  - Prompt: `—`

- [ ] **`sting.unlock`** — Something new unlocks.
  - Target length: ~5s
  - Prompt: `—`

- [ ] **`sting.newrecord`** — A new high score.
  - Target length: ~5s
  - Prompt: `—`

- [ ] **`sting.quest`** — A quest or objective completes.
  - Target length: ~5s
  - Prompt: `—`

- [ ] **`sting.rankup`** — The player ranks up or promotes.
  - Target length: ~5s
  - Prompt: `—`

- [ ] **`sting.boss.appear`** — A boss enters.
  - Target length: ~5s
  - Prompt: `—`

- [ ] **`sting.danger`** — A sudden threat appears.
  - Target length: ~3s
  - Prompt: `—`

- [ ] **`sting.reveal`** — A prize or secret is revealed.
  - Target length: ~4s
  - Prompt: `—`

- [ ] **`sting.transition`** — Between screens or chapters.
  - Target length: ~3s
  - Prompt: `—`

- [ ] **`sting.logo`** — Studio logo or splash screen.
  - Target length: ~4s
  - Prompt: `—`

- [ ] **`sting.chapter`** — A chapter or world title card.
  - Target length: ~5s
  - Prompt: `—`

- [ ] **`sting.sadtrombone`** — A comedic failure.
  - Target length: ~4s
  - Prompt: `—`

- [ ] **`sting.tada`** — A small comedic success.
  - Target length: ~3s
  - Prompt: `—`

- [ ] **`sting.suspense`** — A dramatic pause before a result.
  - Target length: ~5s
  - Prompt: `—`

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
  - Prompt: `Short happy level complete fanfare for a casual mobile game, ringing playful ascending melody on marimba and glockenspiel with a cheerful sparkle ending, no orchestra, no drums`

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

- [x] **`crowd.applause`** — The crowd applauds — win screen, big achievement.
  - Target length: ~2.5s
  - Prompt: `Loud enthusiastic crowd applause and clapping in a hall, recorded close, no cheering voices`

- [x] **`voice.yay`** — A happy child voice reacts to a reward.
  - Target length: ~1.0s · generate **2 takes** (`voice.yay.1.wav`, `voice.yay.2.wav`, …)
  - Prompt: `Loud happy young child voice cheering yay, joyful, dry close recording`

- [x] **`game.checkpoint`** — A checkpoint is reached — progress saved.
  - Target length: ~1.4s
  - Prompt: `Loud game checkpoint reached sound, warm rising three note chime with a soft magical sparkle`

- [x] **`shop.ad.reward`** — A rewarded video finishes and pays out.
  - Target length: ~2.0s
  - Prompt: `Generous reward payout, clear cascading chimes with coins landing and a warm confirming swell`

- [x] **`shop.purchase.ok`** — A purchase completes successfully.
  - Target length: ~1.6s
  - Prompt: `Cash register drawer opening with a clear confirming bell and a receipt printing, recorded close`

- [x] **`shop.subscribe`** — A subscription starts.
  - Target length: ~2.2s
  - Prompt: `Luxurious premium unlock, warm golden shimmer rising into a rich confirming chord`

- [x] **`shop.streak`** — A daily streak advances.
  - Target length: ~1.6s
  - Prompt: `Series of rising stamp impacts with a ringing bell at the end, satisfying and rhythmic, recorded close`

- [x] **`shop.piggy`** — A piggy bank is smashed open.
  - Target length: ~2.0s
  - Prompt: `Ceramic piggy bank smashing on a hard floor and coins scattering everywhere, recorded close`

- [x] **`shop.wheel.stop`** — The prize wheel lands on a segment.
  - Target length: ~1.6s
  - Prompt: `Prize wheel slowing to a stop with the flapper ticking down and settling, recorded close`

- [x] **`shop.gift`** — A gift box opens.
  - Target length: ~1.8s
  - Prompt: `Wrapped gift box being torn open with paper tearing and a ribbon pull, then a clear reveal chime`

- [x] **`emote.clap`** — A single person claps.
  - Target length: ~1.4s · generate **2 takes** (`emote.clap.1.wav`, `emote.clap.2.wav`, …)
  - Prompt: `One person clapping their hands together several times, loud and close, dry recording`

- [x] **`emote.cheer.one`** — One person cheers.
  - Target length: ~1.4s · generate **2 takes** (`emote.cheer.one.1.wav`, `emote.cheer.one.2.wav`, …)
  - Prompt: `One person cheering happily with a short wordless whoop, recorded close`

- [x] **`holiday.confetti`** — A confetti cannon fires.
  - Target length: ~1.6s
  - Prompt: `Confetti cannon firing with a compressed air pop and paper fluttering down, recorded close`

- [x] **`holiday.birthday`** — A birthday moment.
  - Target length: ~2.5s
  - Prompt: `Small group cheering happily with party blowers and clapping at a birthday, wordless, recorded close`

- [x] **`holiday.cork.pop`** — A champagne cork pops.
  - Target length: ~1.4s · generate **2 takes** (`holiday.cork.pop.1.wav`, `holiday.cork.pop.2.wav`, …)
  - Prompt: `Champagne cork popping from a bottle with a deep hollow burst and fizzing, recorded close`

- [x] **`holiday.newyear`** — New year countdown moment.
  - Target length: ~3.0s
  - Prompt: `Crowd cheering and fireworks bursting at midnight celebration, outdoor recording`

## ui

- [x] **`voice.countdown.go`** — A voice shouts GO at the start of a race or round.
  - Target length: ~0.8s
  - Prompt: `Loud energetic male voice shouting the single word GO, sports announcer style, dry close recording`

- [x] **`phone.ring`** — A phone rings.
  - Target length: ~3.0s
  - Prompt: `Mobile phone ringing with a classic electronic ringtone, repeating trill, recorded close`

- [x] **`phone.vibrate`** — A phone buzzes on a surface.
  - Target length: ~2.0s · generate **2 takes** (`phone.vibrate.1.wav`, `phone.vibrate.2.wav`, …)
  - Prompt: `Mobile phone vibrating on a hard wooden table, buzzing rattle, recorded close`

- [x] **`shop.purchase.fail`** — A purchase is declined or cancelled.
  - Target length: ~1.2s
  - Prompt: `Card terminal rejecting a payment with two low descending error tones, recorded close`

- [x] **`shop.restore`** — Purchases are restored.
  - Target length: ~1.4s
  - Prompt: `Soft electronic sync completing with a rising confirming chime, clean recording`

- [x] **`shop.mail`** — New mail arrives.
  - Target length: ~1.2s · generate **2 takes** (`shop.mail.1.wav`, `shop.mail.2.wav`, …)
  - Prompt: `Paper envelope sliding through a letterbox and landing on a wooden floor, recorded close`

- [x] **`shop.coin.spend`** — Currency is spent.
  - Target length: ~0.9s · generate **2 takes** (`shop.coin.spend.1.wav`, `shop.coin.spend.2.wav`, …)
  - Prompt: `Handful of metal coins being handed over and clinking into a bowl, recorded close`

- [x] **`emote.snap`** — A finger snap.
  - Target length: ~0.4s · generate **4 takes** (`emote.snap.1.wav`, `emote.snap.2.wav`, …)
  - Prompt: `Single loud finger snap, recorded very close, dry`

- [x] **`emote.whistle`** — An admiring whistle.
  - Target length: ~1.2s · generate **2 takes** (`emote.whistle.1.wav`, `emote.whistle.2.wav`, …)
  - Prompt: `Person whistling two rising notes in admiration, wordless, recorded close`

- [x] **`emote.kiss`** — A blown kiss.
  - Target length: ~0.6s · generate **2 takes** (`emote.kiss.1.wav`, `emote.kiss.2.wav`, …)
  - Prompt: `Person blowing a kiss, single soft lip smack, recorded close`

- [x] **`emote.huh`** — A confused reaction.
  - Target length: ~0.9s · generate **2 takes** (`emote.huh.1.wav`, `emote.huh.2.wav`, …)
  - Prompt: `Person making a short questioning hum of confusion, wordless, recorded close`

- [x] **`emote.drumroll`** — A drumroll before a reveal.
  - Target length: ~2.2s
  - Prompt: `Snare drum roll building to a cymbal crash, recorded close`

- [x] **`holiday.party.horn`** — A party blower.
  - Target length: ~0.8s · generate **3 takes** (`holiday.party.horn.1.wav`, `holiday.party.horn.2.wav`, …)
  - Prompt: `Party paper blower being blown with a squeaky unrolling toot, recorded close`

- [x] **`holiday.cracker`** — A christmas cracker snaps.
  - Target length: ~0.6s · generate **2 takes** (`holiday.cracker.1.wav`, `holiday.cracker.2.wav`, …)
  - Prompt: `Christmas cracker being pulled apart with a small gunpowder snap, recorded close`
