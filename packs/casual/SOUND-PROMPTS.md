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

**51 of the 373 sounds in this pack are made by code and need nothing from you.**
This checklist is only the 322 that need real audio.

**Progress: 169 of 322 generated.**

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

- [ ] **`car.idle`** — Engine idling while parked or waiting on the grid. Loops.
  - Target length: ~8.0s
  - Prompt: `Car engine idling steadily while parked, continuous low rumbling tickover, microphone close to the exhaust`

- [ ] **`car.accelerate`** — The car pulls away and gains speed.
  - Target length: ~3.0s
  - Prompt: `Car engine accelerating hard from standstill, rising roar climbing through the rev range, recorded close`

- [ ] **`car.decelerate`** — The driver lifts off and the car slows.
  - Target length: ~2.5s
  - Prompt: `Car engine decelerating as the driver lifts off the throttle, falling roar settling to a burble, recorded close`

- [ ] **`car.cruise`** — Steady driving at speed. Loops under gameplay.
  - Target length: ~8.0s
  - Prompt: `Car engine running at a steady cruising speed on a motorway, continuous even roar, microphone close to the engine`

- [ ] **`car.redline`** — Engine held at maximum revs. Loops.
  - Target length: ~6.0s
  - Prompt: `Car engine screaming at maximum revs held at the redline, continuous high pitched roar, recorded close`

- [ ] **`car.rev.blip`** — A quick throttle blip — showing off, gear match.
  - Target length: ~1.2s · generate **3 takes** (`car.rev.blip.1.wav`, `car.rev.blip.2.wav`, …)
  - Prompt: `Car engine given a quick hard throttle blip, hard rise and fall of the revs, recorded close`

- [ ] **`car.start`** — The ignition turns and the engine catches.
  - Target length: ~2.5s
  - Prompt: `Car ignition starting, starter motor cranking then the engine firing up into an idle, recorded close`

- [ ] **`car.start.fail`** — The engine cranks but will not start.
  - Target length: ~2.5s
  - Prompt: `Car engine failing to start, starter motor cranking repeatedly without the engine catching, recorded close`

- [ ] **`car.stall`** — The engine cuts out.
  - Target length: ~1.5s
  - Prompt: `Car engine stalling and dying, revs dropping away into silence with a mechanical shudder, recorded close`

- [ ] **`car.off`** — The driver switches the engine off.
  - Target length: ~1.8s
  - Prompt: `Car engine being switched off, revs falling away with a final mechanical settle, recorded close`

- [ ] **`car.drift`** — The car slides sideways through a corner.
  - Target length: ~3.0s
  - Prompt: `Car tyres sliding sideways across asphalt in a long drift, sustained rubber squeal with the engine roaring behind`

- [ ] **`car.skid`** — A short tyre chirp — hard turn, quick stop.
  - Target length: ~1.0s · generate **3 takes** (`car.skid.1.wav`, `car.skid.2.wav`, …)
  - Prompt: `Car tyres chirping briefly on asphalt during a hard turn, short rubber scrub, recorded close outdoors`

- [ ] **`car.handbrake`** — A handbrake turn.
  - Target length: ~2.0s
  - Prompt: `Car handbrake lever ratcheting up followed by tyres breaking traction and squealing across asphalt`

- [ ] **`car.tyre.squeal`** — Sustained tyre scrub through a long corner. Loops.
  - Target length: ~6.0s
  - Prompt: `Car tyres squealing continuously while cornering hard on asphalt, sustained rubber scrub, recorded close`

- [ ] **`car.gear.up`** — An upshift.
  - Target length: ~0.6s · generate **2 takes** (`car.gear.up.1.wav`, `car.gear.up.2.wav`, …)
  - Prompt: `Car gear lever being shifted up a gear, solid mechanical clunk of the gate, recorded close`

- [ ] **`car.gear.down`** — A downshift, often with a throttle blip.
  - Target length: ~0.9s · generate **2 takes** (`car.gear.down.1.wav`, `car.gear.down.2.wav`, …)
  - Prompt: `Car downshifting a gear with a quick throttle blip, mechanical gate clunk with a rev flare, recorded close`

- [ ] **`car.turbo.spool`** — The turbo spools up under load.
  - Target length: ~2.0s
  - Prompt: `Car turbocharger spooling up under load, rising mechanical whistle building over the engine, recorded close`

- [ ] **`car.turbo.blowoff`** — The blow-off valve releases on a gear change.
  - Target length: ~0.8s · generate **2 takes** (`car.turbo.blowoff.1.wav`, `car.turbo.blowoff.2.wav`, …)
  - Prompt: `Car turbo blow off valve releasing pressure, forceful hissing whoosh of escaping air, recorded close`

- [ ] **`car.nitro`** — Nitrous boost fires.
  - Target length: ~2.5s
  - Prompt: `Nitrous boost firing in a race car, forceful hissing surge with the engine roar leaping in pitch`

- [ ] **`car.backfire`** — The exhaust backfires — pops and bangs.
  - Target length: ~1.0s · generate **3 takes** (`car.backfire.1.wav`, `car.backfire.2.wav`, …)
  - Prompt: `Car exhaust backfiring, loud hard popping bangs from the tailpipe, recorded close`

- [ ] **`car.suspension`** — The car lands or crosses a bump.
  - Target length: ~0.9s · generate **2 takes** (`car.suspension.1.wav`, `car.suspension.2.wav`, …)
  - Prompt: `Car suspension compressing hard as the car lands over a bump, metallic thump with a spring rebound`

- [ ] **`car.scrape`** — The car scrapes along a wall or barrier.
  - Target length: ~1.8s
  - Prompt: `Car body scraping hard along a metal barrier, sustained grinding metal with sparks, recorded close`

- [ ] **`car.crash.light`** — A minor collision — bump, tap, fender bender.
  - Target length: ~1.2s
  - Prompt: `Light car collision, dull metallic bump with plastic trim rattling, recorded close`

- [ ] **`car.horn.long`** — A long angry horn blast.
  - Target length: ~2.0s
  - Prompt: `Car horn held down in a long angry blast, recorded close outdoors`

- [ ] **`car.door.open`** — A car door opens.
  - Target length: ~1.2s · generate **2 takes** (`car.door.open.1.wav`, `car.door.open.2.wav`, …)
  - Prompt: `Car door handle being pulled and the door swinging open, metallic latch and hinge, recorded close`

- [ ] **`car.door.close`** — A car door shuts.
  - Target length: ~1.0s · generate **2 takes** (`car.door.close.1.wav`, `car.door.close.2.wav`, …)
  - Prompt: `Car door being shut firmly, solid heavy thunk of the latch, recorded close`

- [ ] **`car.window`** — An electric window winds down.
  - Target length: ~1.5s
  - Prompt: `Electric car window winding down, small motor whirring with glass sliding in the seal, recorded close`

- [ ] **`car.seatbelt`** — A seatbelt is pulled and clicked in.
  - Target length: ~1.5s
  - Prompt: `Car seatbelt being pulled out and clicked into the buckle, webbing zip with a plastic click, recorded close`

- [ ] **`car.indicator`** — The indicator ticks. Loops.
  - Target length: ~3.0s
  - Prompt: `Car indicator relay ticking steadily, continuous even clicking, recorded close in the cabin`

- [ ] **`car.wiper`** — Windscreen wipers sweep. Loops.
  - Target length: ~4.0s
  - Prompt: `Car windscreen wipers sweeping back and forth across wet glass, continuous rubber squeak, recorded in the cabin`

- [ ] **`moto.idle`** — A motorbike idles. Loops.
  - Target length: ~6.0s
  - Prompt: `Motorcycle engine idling, continuous uneven thumping tickover, microphone close to the exhaust`

- [ ] **`moto.rev`** — A motorbike revs hard.
  - Target length: ~2.0s · generate **2 takes** (`moto.rev.1.wav`, `moto.rev.2.wav`, …)
  - Prompt: `Motorcycle engine revved hard, fast rising snarl from the exhaust, recorded close`

- [ ] **`moto.pass`** — A motorbike flies past.
  - Target length: ~2.5s
  - Prompt: `Motorcycle speeding past the microphone at high speed, rising then falling doppler roar, outdoor recording`

- [ ] **`truck.horn`** — An air horn blasts.
  - Target length: ~2.0s
  - Prompt: `Large truck air horn blasting twice, deep powerful honk, recorded outdoors`

- [ ] **`truck.airbrake`** — Air brakes release with a hiss.
  - Target length: ~1.5s
  - Prompt: `Truck air brakes releasing with a hard pressurised hiss, recorded close`

- [ ] **`truck.idle`** — A diesel truck idles. Loops.
  - Target length: ~8.0s
  - Prompt: `Large diesel truck engine idling, continuous deep clattering rumble, microphone close to the engine`

- [ ] **`race.light`** — A starting light changes on the grid.
  - Target length: ~0.8s · generate **2 takes** (`race.light.1.wav`, `race.light.2.wav`, …)
  - Prompt: `Motorsport starting light beeping once on the grid, single clear electronic tone, recorded close`

- [ ] **`race.lap`** — A lap is completed.
  - Target length: ~1.2s
  - Prompt: `Racing game lap completed sound, clear electronic double chime with a satisfying confirmation tone`

- [ ] **`race.finish`** — The chequered flag — race over.
  - Target length: ~2.5s
  - Prompt: `Race finish line moment, crowd cheering with an air horn blast as a car speeds past, outdoor recording`

- [ ] **`race.flag.wave`** — A flag snaps in the wind.
  - Target length: ~1.0s · generate **2 takes** (`race.flag.wave.1.wav`, `race.flag.wave.2.wav`, …)
  - Prompt: `Large flag snapping and flapping hard in strong wind, heavy cloth cracking, outdoor recording`

- [ ] **`gun.smg`** — A submachine gun burst.
  - Target length: ~1.5s
  - Prompt: `Submachine gun firing a rapid burst, fast dry cracking shots with mechanical action, recorded close`

- [ ] **`gun.sniper`** — A sniper rifle fires.
  - Target length: ~2.0s
  - Prompt: `Sniper rifle firing a single shot, huge cracking report with a long decaying tail, recorded outdoors`

- [ ] **`gun.revolver`** — A revolver fires.
  - Target length: ~1.0s · generate **2 takes** (`gun.revolver.1.wav`, `gun.revolver.2.wav`, …)
  - Prompt: `Revolver firing a single round, loud deep cracking report, recorded close and dry`

- [ ] **`gun.silenced`** — A suppressed shot.
  - Target length: ~0.7s · generate **2 takes** (`gun.silenced.1.wav`, `gun.silenced.2.wav`, …)
  - Prompt: `Suppressed pistol firing a single round, muffled thumping report with the slide cycling, recorded close`

- [ ] **`gun.minigun`** — A minigun spins up and fires. Loops.
  - Target length: ~4.0s
  - Prompt: `Minigun firing continuously at high rate, rapid overlapping shots with a spinning barrel whine`

- [ ] **`gun.shell.drop`** — A spent shell hits the ground.
  - Target length: ~1.0s · generate **3 takes** (`gun.shell.drop.1.wav`, `gun.shell.drop.2.wav`, …)
  - Prompt: `Spent brass shell casing bouncing on a concrete floor, ringing metallic tinkling, recorded close`

- [ ] **`gun.mag.out`** — A magazine is ejected.
  - Target length: ~0.7s · generate **2 takes** (`gun.mag.out.1.wav`, `gun.mag.out.2.wav`, …)
  - Prompt: `Gun magazine being released and dropping free, metallic click with a clatter, recorded close`

- [ ] **`gun.mag.in`** — A fresh magazine is seated.
  - Target length: ~0.7s · generate **2 takes** (`gun.mag.in.1.wav`, `gun.mag.in.2.wav`, …)
  - Prompt: `Fresh gun magazine being slapped firmly into the receiver, solid metallic clack, recorded close`

- [ ] **`gun.bolt`** — The bolt or slide is pulled.
  - Target length: ~0.6s · generate **2 takes** (`gun.bolt.1.wav`, `gun.bolt.2.wav`, …)
  - Prompt: `Rifle bolt being pulled back and released, heavy metallic rack, recorded close`

- [ ] **`gun.grenade.pin`** — A grenade pin is pulled.
  - Target length: ~0.7s
  - Prompt: `Grenade safety pin being pulled out with the lever springing off, small metallic clicks, recorded close`

- [ ] **`gun.grenade.throw`** — A grenade is thrown.
  - Target length: ~0.8s
  - Prompt: `Grenade being thrown through the air, cloth swish with a metallic tumble, recorded close`

- [ ] **`gun.rocket.launch`** — A rocket launcher fires.
  - Target length: ~2.0s
  - Prompt: `Rocket launcher firing, huge whooshing ignition with a roaring rocket motor departing, recorded close`

- [ ] **`gun.flamethrower`** — A flamethrower burns. Loops.
  - Target length: ~4.0s
  - Prompt: `Flamethrower burning continuously, roaring jet of flame with crackling fire, recorded close`

- [ ] **`gun.crossbow`** — A crossbow looses a bolt.
  - Target length: ~0.9s · generate **2 takes** (`gun.crossbow.1.wav`, `gun.crossbow.2.wav`, …)
  - Prompt: `Crossbow firing a bolt, taut string snapping forward with a wooden thunk, recorded close`

- [ ] **`gun.reload.shotgun`** — Shells are pumped into a shotgun.
  - Target length: ~2.0s
  - Prompt: `Shotgun being loaded with shells and pumped, mechanical metallic racking, recorded close`

- [ ] **`melee.stab`** — A blade goes in.
  - Target length: ~0.7s · generate **3 takes** (`melee.stab.1.wav`, `melee.stab.2.wav`, …)
  - Prompt: `Knife stabbing into a melon, wet penetrating impact, recorded close, cartoon action style`

- [ ] **`melee.block`** — A hit is blocked on a shield.
  - Target length: ~0.8s · generate **2 takes** (`melee.block.1.wav`, `melee.block.2.wav`, …)
  - Prompt: `Sword striking a wooden shield with a metal boss, loud blocking impact with a ringing clang, recorded close`

- [ ] **`melee.parry`** — A blade is deflected at the last moment.
  - Target length: ~0.7s · generate **2 takes** (`melee.parry.1.wav`, `melee.parry.2.wav`, …)
  - Prompt: `Two sword blades scraping and deflecting off each other, quick metallic ring, recorded close`

- [ ] **`melee.sheathe`** — A blade is put away.
  - Target length: ~0.9s · generate **2 takes** (`melee.sheathe.1.wav`, `melee.sheathe.2.wav`, …)
  - Prompt: `Steel sword being slid back into a leather scabbard, metallic scraping slide, recorded close`

- [ ] **`melee.axe.swing`** — A heavy axe swings.
  - Target length: ~0.7s · generate **2 takes** (`melee.axe.swing.1.wav`, `melee.axe.swing.2.wav`, …)
  - Prompt: `Heavy battle axe swinging through the air, deep slow air whoosh, recorded close`

- [ ] **`melee.hammer.swing`** — A war hammer swings.
  - Target length: ~0.8s · generate **2 takes** (`melee.hammer.swing.1.wav`, `melee.hammer.swing.2.wav`, …)
  - Prompt: `Heavy war hammer swinging through the air, deep booming air whoosh, recorded close`

- [ ] **`melee.spear`** — A spear thrusts.
  - Target length: ~0.6s · generate **2 takes** (`melee.spear.1.wav`, `melee.spear.2.wav`, …)
  - Prompt: `Wooden spear thrusting fast through the air, fast air whoosh with a shaft rattle, recorded close`

- [ ] **`melee.whip`** — A whip cracks.
  - Target length: ~0.8s · generate **2 takes** (`melee.whip.1.wav`, `melee.whip.2.wav`, …)
  - Prompt: `Leather whip cracking hard, hard explosive snap with a leather hiss, recorded close`

- [ ] **`melee.kick`** — A heavy kick lands.
  - Target length: ~0.5s · generate **3 takes** (`melee.kick.1.wav`, `melee.kick.2.wav`, …)
  - Prompt: `Heavy boot kicking into a body, dull thudding impact with cloth, cartoon action style, recorded close`

- [ ] **`melee.dodge`** — A dodge or evade — body moving fast.
  - Target length: ~0.5s · generate **3 takes** (`melee.dodge.1.wav`, `melee.dodge.2.wav`, …)
  - Prompt: `Fast body movement dodging, quick cloth and air whoosh, recorded close`

- [ ] **`magic.lightning.cast`** — A lightning spell is cast.
  - Target length: ~1.4s
  - Prompt: `Lightning spell being cast, crackling electrical charge building into a hard thunderous discharge`

- [ ] **`magic.lightning.hit`** — Lightning strikes a target.
  - Target length: ~1.2s · generate **2 takes** (`magic.lightning.hit.1.wav`, `magic.lightning.hit.2.wav`, …)
  - Prompt: `Lightning bolt striking a target, violent electrical crack with a sizzling aftermath`

- [ ] **`magic.fire.cast`** — A fire spell winds up.
  - Target length: ~1.3s
  - Prompt: `Fire spell being conjured, swelling roar of flames gathering with a whooshing ignition`

- [ ] **`magic.fire.hit`** — A fireball lands.
  - Target length: ~1.2s · generate **2 takes** (`magic.fire.hit.1.wav`, `magic.fire.hit.2.wav`, …)
  - Prompt: `Fireball impacting a target, explosive burst of flame with crackling burning aftermath`

- [ ] **`magic.ice.cast`** — An ice spell winds up.
  - Target length: ~1.3s
  - Prompt: `Ice spell being conjured, crystalline chiming with a rising cold wind`

- [ ] **`magic.ice.hit`** — Ice strikes and shatters on a target.
  - Target length: ~1.2s · generate **2 takes** (`magic.ice.hit.1.wav`, `magic.ice.hit.2.wav`, …)
  - Prompt: `Ice spell impacting a target, hard crystalline shatter with frozen shards scattering`

- [ ] **`magic.wind`** — A wind or gust spell.
  - Target length: ~1.5s
  - Prompt: `Wind spell being cast, powerful rushing gust of air sweeping past with a whistling swirl`

- [ ] **`magic.earth`** — An earth or stone spell.
  - Target length: ~1.6s
  - Prompt: `Earth spell erupting, heavy grinding stone rising with rubble and a deep ground rumble`

- [ ] **`magic.holy`** — A holy or blessing spell.
  - Target length: ~2.0s
  - Prompt: `Holy blessing spell, radiant choir-like shimmer with ringing bells and a warm rising glow`

- [ ] **`magic.dark`** — A dark or shadow spell.
  - Target length: ~1.8s
  - Prompt: `Dark shadow spell being cast, deep ominous swell with whispering void and a sinister rush`

- [ ] **`magic.shield.up`** — A magic barrier comes up.
  - Target length: ~1.2s
  - Prompt: `Magical shield forming, rising crystalline hum sealing into a steady protective tone`

- [ ] **`magic.shield.hit`** — Something strikes a magic barrier.
  - Target length: ~0.8s · generate **2 takes** (`magic.shield.hit.1.wav`, `magic.shield.hit.2.wav`, …)
  - Prompt: `Projectile striking a magical energy shield, ringing electric deflection with a ringing wobble`

- [ ] **`scifi.laser.charge`** — An energy weapon charges before firing.
  - Target length: ~1.8s
  - Prompt: `Science fiction energy weapon charging up, rising electronic whine building to a peak, synthetic recording`

- [ ] **`scifi.shield.hit`** — A ship or suit shield takes a hit.
  - Target length: ~0.9s · generate **2 takes** (`scifi.shield.hit.1.wav`, `scifi.shield.hit.2.wav`, …)
  - Prompt: `Science fiction energy shield absorbing an impact, electric wobbling deflection with a metallic ring`

- [ ] **`scifi.alarm`** — A ship or base alarm. Loops.
  - Target length: ~4.0s
  - Prompt: `Science fiction ship alarm klaxon sounding repeatedly, continuous urgent electronic alert`

- [ ] **`scifi.engine.hum`** — Spaceship engine hum. Loops.
  - Target length: ~6.0s
  - Prompt: `Science fiction spaceship engine humming steadily, continuous deep electronic drone, synthetic recording`

- [ ] **`scifi.warp`** — A jump to lightspeed.
  - Target length: ~2.5s
  - Prompt: `Spaceship jumping to lightspeed, deep rising whoosh building into an explosive departure`

- [ ] **`scifi.door`** — An automatic door slides open.
  - Target length: ~1.2s · generate **2 takes** (`scifi.door.1.wav`, `scifi.door.2.wav`, …)
  - Prompt: `Science fiction automatic door sliding open with a pneumatic hiss and mechanical servo, synthetic recording`

- [ ] **`scifi.computer.beep`** — A console acknowledges input.
  - Target length: ~0.5s · generate **3 takes** (`scifi.computer.beep.1.wav`, `scifi.computer.beep.2.wav`, …)
  - Prompt: `Science fiction computer console beeping a short confirmation tone, clean synthetic recording`

- [ ] **`scifi.robot.talk`** — A robot speaks in machine noise.
  - Target length: ~1.4s · generate **2 takes** (`scifi.robot.talk.1.wav`, `scifi.robot.talk.2.wav`, …)
  - Prompt: `Small robot chattering in electronic beeps and warbles, wordless machine speech, synthetic recording`

- [ ] **`step.carpet`** — One footstep on on thick carpet. Play per step; the library varies pitch and picks a different take each time.
  - Target length: ~0.25s · generate **5 takes** (`step.carpet.1.wav`, `step.carpet.2.wav`, …)
  - Prompt: `Single footstep on on thick carpet`

- [ ] **`step.mud`** — One footstep on through wet mud. Play per step; the library varies pitch and picks a different take each time.
  - Target length: ~0.25s · generate **5 takes** (`step.mud.1.wav`, `step.mud.2.wav`, …)
  - Prompt: `Single footstep on through wet mud`

- [ ] **`step.tile`** — One footstep on on hard ceramic tiles. Play per step; the library varies pitch and picks a different take each time.
  - Target length: ~0.25s · generate **5 takes** (`step.tile.1.wav`, `step.tile.2.wav`, …)
  - Prompt: `Single footstep on on hard ceramic tiles`

- [ ] **`step.ice`** — One footstep on on solid ice. Play per step; the library varies pitch and picks a different take each time.
  - Target length: ~0.25s · generate **5 takes** (`step.ice.1.wav`, `step.ice.2.wav`, …)
  - Prompt: `Single footstep on on solid ice`

- [ ] **`step.leaves`** — One footstep on through dry fallen leaves. Play per step; the library varies pitch and picks a different take each time.
  - Target length: ~0.25s · generate **5 takes** (`step.leaves.1.wav`, `step.leaves.2.wav`, …)
  - Prompt: `Single footstep on through dry fallen leaves`

- [ ] **`step.stairs`** — One footstep on up a wooden staircase. Play per step; the library varies pitch and picks a different take each time.
  - Target length: ~0.25s · generate **5 takes** (`step.stairs.1.wav`, `step.stairs.2.wav`, …)
  - Prompt: `Single footstep on up a wooden staircase`

- [ ] **`step.run.stone`** — One footstep while running on stone. Faster and harder than walking.
  - Target length: ~0.2s · generate **5 takes** (`step.run.stone.1.wav`, `step.run.stone.2.wav`, …)
  - Prompt: `Single running footstep on stone`

- [ ] **`water.drip`** — A single drip — cave, leak, tension.
  - Target length: ~0.8s · generate **3 takes** (`water.drip.1.wav`, `water.drip.2.wav`, …)
  - Prompt: `Single water drop falling into a shallow puddle, clear plink with a small echo, recorded close`

- [ ] **`water.tap`** — A running tap. Loops.
  - Target length: ~4.0s
  - Prompt: `Water running steadily from a kitchen tap into a sink, continuous splashing stream, recorded close`

- [ ] **`water.underwater`** — Submerged ambience. Loops.
  - Target length: ~6.0s
  - Prompt: `Underwater ambience with muffled low rumble and bubbles, continuous submerged sound, recorded with a hydrophone`

- [ ] **`water.bubble`** — Bubbles rise through water.
  - Target length: ~1.2s · generate **3 takes** (`water.bubble.1.wav`, `water.bubble.2.wav`, …)
  - Prompt: `Air bubbles rising through water, gurgling glugging burst, recorded close`

- [ ] **`water.dive`** — A body enters the water.
  - Target length: ~1.5s
  - Prompt: `Person diving into a swimming pool, big plunging splash with water churning after, recorded close`

- [ ] **`water.wave.crash`** — A big wave breaks.
  - Target length: ~2.5s
  - Prompt: `Large ocean wave crashing hard onto rocks, powerful churning break with foam hissing after, outdoor recording`

- [ ] **`water.fountain`** — A fountain runs. Loops.
  - Target length: ~4.0s
  - Prompt: `Ornamental stone fountain running, continuous falling water splashing into a pool, outdoor recording`

- [ ] **`fire.ignite`** — Something catches light.
  - Target length: ~1.5s
  - Prompt: `Fire igniting suddenly, hard whooshing burst of flame catching and settling into a burn, recorded close`

- [ ] **`fire.torch`** — A handheld torch burns. Loops.
  - Target length: ~4.0s
  - Prompt: `Handheld burning torch, continuous flapping flame with crackling, recorded close`

- [ ] **`fire.extinguish`** — A flame is put out.
  - Target length: ~1.5s
  - Prompt: `Fire being doused with water, violent hissing steam as the flames die out, recorded close`

- [ ] **`fire.match`** — A match is struck.
  - Target length: ~1.2s · generate **3 takes** (`fire.match.1.wav`, `fire.match.2.wav`, …)
  - Prompt: `Match being struck on a box and catching light, gritty scrape with a flaring ignition, recorded close`

- [ ] **`fire.lighter`** — A lighter flicks on.
  - Target length: ~0.8s · generate **2 takes** (`fire.lighter.1.wav`, `fire.lighter.2.wav`, …)
  - Prompt: `Cigarette lighter being flicked, metal wheel sparking with a small flame catching, recorded close`

- [ ] **`weather.rain.light`** — Light rain. Loops.
  - Target length: ~6.0s
  - Prompt: `Light drizzling rain falling on pavement, continuous gentle patter, clean field recording, no music`

- [ ] **`weather.rain.heavy`** — Heavy downpour. Loops.
  - Target length: ~6.0s
  - Prompt: `Heavy torrential rain pouring down hard, continuous roaring downpour, clean field recording, no music`

- [ ] **`weather.rain.window`** — Rain on glass. Loops.
  - Target length: ~6.0s
  - Prompt: `Rain drumming against a window pane from inside, continuous tapping on glass, clean recording, no music`

- [ ] **`weather.storm.wind`** — Storm wind howling. Loops.
  - Target length: ~8.0s
  - Prompt: `Powerful storm wind howling and gusting hard, continuous roaring blasts, clean field recording, no music`

- [ ] **`weather.thunder.distant`** — Thunder rolls far away.
  - Target length: ~3.5s
  - Prompt: `Distant thunder rolling across the sky, long low rumbling growl with no sharp crack`

- [ ] **`door.wood.open`** — A wooden door opens.
  - Target length: ~1.3s · generate **2 takes** (`door.wood.open.1.wav`, `door.wood.open.2.wav`, …)
  - Prompt: `Wooden door swinging open on dry hinges, loud creaking with a final knock, recorded close`

- [ ] **`door.metal.open`** — A heavy metal door opens.
  - Target length: ~1.6s
  - Prompt: `Heavy steel industrial door being pushed open, loud grinding metal with a booming echo, recorded close`

- [ ] **`door.slide`** — A sliding door runs on its track.
  - Target length: ~1.4s
  - Prompt: `Sliding glass door running along its track and stopping, rolling wheels with a final bump, recorded close`

- [ ] **`door.knock`** — Someone knocks.
  - Target length: ~1.2s · generate **2 takes** (`door.knock.1.wav`, `door.knock.2.wav`, …)
  - Prompt: `Firm knuckles knocking three times on a solid wooden door, loud and close, dry recording`

- [ ] **`door.bell`** — A doorbell rings.
  - Target length: ~2.0s
  - Prompt: `Classic two tone doorbell chiming, ringing ding dong with a ringing decay, recorded close`

- [ ] **`door.locked`** — A locked door rattles.
  - Target length: ~1.2s · generate **2 takes** (`door.locked.1.wav`, `door.locked.2.wav`, …)
  - Prompt: `Locked door handle being rattled hard without opening, metallic clattering, recorded close`

- [ ] **`door.slam`** — A door slams shut.
  - Target length: ~1.2s · generate **2 takes** (`door.slam.1.wav`, `door.slam.2.wav`, …)
  - Prompt: `Wooden door being slammed shut hard, explosive booming bang with the frame rattling, recorded close`

- [ ] **`horror.scream`** — A terrified scream.
  - Target length: ~2.0s
  - Prompt: `Terrified human scream of fear, loud shrieking wail, wordless, no speech, dry close recording`

- [ ] **`horror.growl.deep`** — Something very large growls in the dark.
  - Target length: ~2.5s
  - Prompt: `Enormous creature growling deep in the dark, low rumbling menacing throat, wordless, recorded close`

- [ ] **`horror.musicbox`** — A music box plays — classic dread.
  - Target length: ~4.0s
  - Prompt: `Old wind up music box playing a slow simple lullaby, delicate metallic chimes slightly out of tune, recorded close`

- [ ] **`horror.knock.slow`** — Slow deliberate knocking.
  - Target length: ~2.5s
  - Prompt: `Three slow heavy knocks on a distant wooden door, ominous and deliberate, hollow room`

- [ ] **`horror.laugh`** — An unsettling laugh.
  - Target length: ~2.0s
  - Prompt: `Sinister low laughter, slow menacing chuckle, wordless, no speech, dry close recording`

- [ ] **`horror.static`** — Radio or TV static. Loops.
  - Target length: ~4.0s
  - Prompt: `Radio static hissing with occasional crackling interference, continuous, recorded close`

- [ ] **`kitchen.kettle`** — A kettle comes to the boil.
  - Target length: ~3.0s
  - Prompt: `Metal kettle heating and whistling as it comes to the boil, rising steam whistle, recorded close`

- [ ] **`kitchen.microwave`** — A microwave finishes and beeps.
  - Target length: ~1.5s
  - Prompt: `Microwave oven beeping three times when finished, clear electronic tones, recorded close`

- [ ] **`kitchen.blender`** — A blender runs.
  - Target length: ~2.5s
  - Prompt: `Kitchen blender running at high speed grinding ice, loud motor whine with rattling, recorded close`

- [ ] **`kitchen.egg.crack`** — An egg is cracked.
  - Target length: ~0.8s · generate **2 takes** (`kitchen.egg.crack.1.wav`, `kitchen.egg.crack.2.wav`, …)
  - Prompt: `Egg being cracked on the edge of a bowl and opened, brittle shell crack with a wet slop, recorded close`

- [ ] **`kitchen.can.open`** — A drink can is opened.
  - Target length: ~1.0s · generate **2 takes** (`kitchen.can.open.1.wav`, `kitchen.can.open.2.wav`, …)
  - Prompt: `Aluminium drink can being opened, ringing metallic crack with a hissing fizz, recorded close`

- [ ] **`kitchen.bottle.open`** — A bottle is uncorked or opened.
  - Target length: ~1.0s · generate **2 takes** (`kitchen.bottle.open.1.wav`, `kitchen.bottle.open.2.wav`, …)
  - Prompt: `Cork being pulled from a glass bottle, deep hollow pop, recorded close`

- [ ] **`kitchen.cutlery`** — Cutlery clatters on a plate.
  - Target length: ~1.0s · generate **2 takes** (`kitchen.cutlery.1.wav`, `kitchen.cutlery.2.wav`, …)
  - Prompt: `Metal knife and fork clattering onto a ceramic plate, ringing clinking, recorded close`

- [ ] **`kitchen.sip`** — A drink is sipped.
  - Target length: ~1.0s · generate **2 takes** (`kitchen.sip.1.wav`, `kitchen.sip.2.wav`, …)
  - Prompt: `Person taking a sip of a drink and swallowing, wet gulp, recorded close`

- [ ] **`office.printer`** — A printer prints a page.
  - Target length: ~3.0s
  - Prompt: `Office printer feeding and printing a sheet of paper, mechanical whirring with paper rollers, recorded close`

- [ ] **`office.drawer`** — A drawer opens or closes.
  - Target length: ~1.2s · generate **2 takes** (`office.drawer.1.wav`, `office.drawer.2.wav`, …)
  - Prompt: `Wooden desk drawer being pulled open and pushed shut, sliding wood with a final knock, recorded close`

- [ ] **`office.stapler`** — A stapler clicks.
  - Target length: ~0.6s · generate **2 takes** (`office.stapler.1.wav`, `office.stapler.2.wav`, …)
  - Prompt: `Desk stapler being pressed down firmly, ringing metallic punch, recorded close`

- [ ] **`animal.dog.growl`** — A dog growls a warning.
  - Target length: ~1.5s · generate **2 takes** (`animal.dog.growl.1.wav`, `animal.dog.growl.2.wav`, …)
  - Prompt: `Dog growling low in warning, rumbling threatening throat, recorded close`

- [ ] **`animal.cat.purr`** — A cat purrs. Loops.
  - Target length: ~4.0s
  - Prompt: `Cat purring contentedly, continuous soft rumbling vibration, microphone close to the cat`

- [ ] **`animal.cat.hiss`** — A cat hisses.
  - Target length: ~1.0s · generate **2 takes** (`animal.cat.hiss.1.wav`, `animal.cat.hiss.2.wav`, …)
  - Prompt: `Angry cat hissing sharply, sudden air hiss with a spit, recorded close`

- [ ] **`animal.bird.flap`** — Wings beat as a bird takes off.
  - Target length: ~1.2s · generate **2 takes** (`animal.bird.flap.1.wav`, `animal.bird.flap.2.wav`, …)
  - Prompt: `Large bird taking off with heavy wing beats, flapping feathers pushing air, recorded close`

- [ ] **`animal.rooster`** — A rooster crows — morning, farm.
  - Target length: ~1.8s
  - Prompt: `Rooster crowing loudly at dawn, full cock a doodle doo, outdoor farm recording`

- [ ] **`animal.lion.roar`** — A lion roars.
  - Target length: ~2.5s
  - Prompt: `Lion roaring powerfully, deep full throated roar, recorded close`

- [ ] **`animal.bear.growl`** — A bear growls.
  - Target length: ~2.0s
  - Prompt: `Large bear growling threateningly, deep guttural rumble, recorded close`

- [ ] **`animal.owl`** — An owl hoots at night.
  - Target length: ~1.8s
  - Prompt: `Owl hooting twice in a quiet night forest, clear low hoots, outdoor recording`

- [ ] **`animal.seagull`** — Seagulls call — coast, harbour.
  - Target length: ~1.8s
  - Prompt: `Seagulls calling loudly by the sea, hard squawking cries, outdoor coastal recording`

- [ ] **`animal.horse.gallop`** — A horse gallops. Loops.
  - Target length: ~4.0s
  - Prompt: `Horse galloping fast on packed dirt, continuous rhythmic hoofbeats, outdoor recording`

- [ ] **`sport.golf`** — A golf club strikes the ball.
  - Target length: ~0.8s · generate **2 takes** (`sport.golf.1.wav`, `sport.golf.2.wav`, …)
  - Prompt: `Golf driver striking a ball off a tee, hard cracking impact, outdoor recording`

- [ ] **`sport.bowling`** — A bowling ball hits the pins.
  - Target length: ~2.5s
  - Prompt: `Bowling ball rolling down a lane and smashing into the pins, rumbling roll with a clattering strike`

- [ ] **`sport.pool.break`** — A pool break scatters the balls.
  - Target length: ~2.0s
  - Prompt: `Pool cue breaking a rack of billiard balls, hard crack with balls scattering across the table`

- [ ] **`sport.boxing.bell`** — The boxing bell rings a round.
  - Target length: ~2.0s
  - Prompt: `Boxing ring bell struck three times, loud ringing metallic clangs with ringing decay`

- [ ] **`sport.skate`** — A skateboard rolls and grinds.
  - Target length: ~2.0s
  - Prompt: `Skateboard rolling on concrete then grinding along a metal rail, rumbling wheels with harsh scraping`

- [ ] **`sport.ski`** — Skis carve through snow. Loops.
  - Target length: ~4.0s
  - Prompt: `Skis carving through packed snow at speed, continuous scraping hiss, outdoor recording`

- [ ] **`sport.crowd.goal`** — The crowd erupts at a goal.
  - Target length: ~3.0s
  - Prompt: `Stadium crowd erupting into a huge roar and cheering after a goal, outdoor stadium recording`

- [ ] **`sport.stadium`** — Stadium crowd ambience. Loops.
  - Target length: ~6.0s
  - Prompt: `Large stadium crowd murmuring and occasionally cheering, continuous background, outdoor recording`

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

## ui

- [x] **`voice.countdown.go`** — A voice shouts GO at the start of a race or round.
  - Target length: ~0.8s
  - Prompt: `Loud energetic male voice shouting the single word GO, sports announcer style, dry close recording`

- [ ] **`phone.ring`** — A phone rings.
  - Target length: ~3.0s
  - Prompt: `Mobile phone ringing with a classic electronic ringtone, repeating trill, recorded close`

- [ ] **`phone.vibrate`** — A phone buzzes on a surface.
  - Target length: ~2.0s · generate **2 takes** (`phone.vibrate.1.wav`, `phone.vibrate.2.wav`, …)
  - Prompt: `Mobile phone vibrating on a hard wooden table, buzzing rattle, recorded close`
