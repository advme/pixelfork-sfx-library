# Pixelfork SFX Library — AI guide

Ready-made game sound effects for AI-generated web games. **You never create or describe audio — you call a name from the list below.**

105 sounds. About half are **made by code** (they play instantly and weigh nothing) and half are **real audio files**. You do not need to care which: `SFX.play(name)` works the same either way.

## 1. Add it (2 lines)

```html
<script src="https://cdn.jsdelivr.net/gh/advme/pixelfork-sfx-library@v0.5.0-A/dist/sfx.js"></script>
<script>SFX.load('casual'); SFX.attach();</script>
```

`SFX.attach()` is optional but strongly recommended: if the game uses the **Super Casual UI Kit**, it gives every button, popup, toggle, shop card and star rating its sound automatically. You then only add sounds for things the UI kit does not know about (the gameplay itself).

## 2. Play a sound

```js
SFX.play('coin.collect');                   // one sound
SFX.play('reward.star', { rate: 1.25 });    // higher pitch
SFX.play('ui.tap', { volume: 0.5 });        // quieter
SFX.music('music.gameplay');                // looping background music
SFX.duck(0.25, 1500);                       // dip the music under a big moment
```

The library repeats safely: pitch varies slightly on every play, identical sounds fired in the same millisecond are collapsed, and no more than 24 sounds play at once.

## 3. Every sound in the `casual` pack

The **Made by** column is informational only — `code` sounds are final, not placeholders.

<!-- SOUNDS:START -->

**`ambience.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `ambience.cave` | Underground cave with drips. Loops. | ai |
| `ambience.crowd` | Busy crowd murmur — market, stadium, town. Loops. | ai |
| `ambience.forest` | Daytime forest with birds. Loops. | ai |
| `ambience.night` | Night outdoors with crickets. Loops. | ai |
| `ambience.rain` | Rainfall. Loops behind gameplay. | ai |
| `ambience.waves` | Sea shore. Loops. | ai |
| `ambience.wind` | Open outdoor wind. Loops behind gameplay. | ai |

**`animal.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `animal.bear.growl` | A bear growls. | ai |
| `animal.bee.buzz` | An insect buzzes past — bee, fly, wasp enemy. | ai |
| `animal.bird.chirp` | A small bird chirps — collectible, ambience accent, cute character. | ai |
| `animal.bird.flap` | Wings beat as a bird takes off. | ai |
| `animal.cat.hiss` | A cat hisses. | ai |
| `animal.cat.meow` | A cat meows — pet or character. | ai |
| `animal.cat.purr` | A cat purrs. Loops. | ai |
| `animal.chicken.cluck` | A chicken clucks — farm game, egg collection. | ai |
| `animal.cow.moo` | A cow lows — farm game, idle animal. | ai |
| `animal.dog.bark` | A dog barks — pet, guard, companion or enemy. | ai |
| `animal.dog.growl` | A dog growls a warning. | ai |
| `animal.frog.croak` | A frog croaks — pond, swamp, collectible creature. | ai |
| `animal.horse.gallop` | A horse gallops. Loops. | ai |
| `animal.horse.neigh` | A horse whinnies — mount, race, farm. | ai |
| `animal.lion.roar` | A lion roars. | ai |
| `animal.owl` | An owl hoots at night. | ai |
| `animal.pig.oink` | A pig oinks — farm game, idle animal. | ai |
| `animal.rooster` | A rooster crows — morning, farm. | ai |
| `animal.seagull` | Seagulls call — coast, harbour. | ai |
| `animal.sheep.bleat` | A sheep bleats — farm game, idle animal. | ai |
| `animal.snake.hiss` | A snake hisses — enemy warning, trap. | ai |
| `animal.wolf.howl` | A wolf howls — night, danger, boss approach. | ai |

**`break.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `break.glass` | Glass, ice or a crystal shatters. | ai |
| `break.pot` | A pot, vase or ceramic container smashes. | ai |
| `break.stone` | Rock, brick or concrete breaks. | ai |
| `break.wood` | A crate, plank, barrel or door breaks apart. | ai |

**`car.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `car.accelerate` | The car pulls away and gains speed. | ai |
| `car.backfire` | The exhaust backfires — pops and bangs. | ai |
| `car.crash.light` | A minor collision — bump, tap, fender bender. | ai |
| `car.cruise` | Steady driving at speed. Loops under gameplay. | ai |
| `car.decelerate` | The driver lifts off and the car slows. | ai |
| `car.door.close` | A car door shuts. | ai |
| `car.door.open` | A car door opens. | ai |
| `car.drift` | The car slides sideways through a corner. | ai |
| `car.gear.down` | A downshift, often with a throttle blip. | ai |
| `car.gear.up` | An upshift. | ai |
| `car.handbrake` | A handbrake turn. | ai |
| `car.horn.long` | A long angry horn blast. | ai |
| `car.idle` | Engine idling while parked or waiting on the grid. Loops. | ai |
| `car.indicator` | The indicator ticks. Loops. | ai |
| `car.nitro` | Nitrous boost fires. | ai |
| `car.off` | The driver switches the engine off. | ai |
| `car.redline` | Engine held at maximum revs. Loops. | ai |
| `car.rev.blip` | A quick throttle blip — showing off, gear match. | ai |
| `car.scrape` | The car scrapes along a wall or barrier. | ai |
| `car.seatbelt` | A seatbelt is pulled and clicked in. | ai |
| `car.skid` | A short tyre chirp — hard turn, quick stop. | ai |
| `car.stall` | The engine cuts out. | ai |
| `car.start` | The ignition turns and the engine catches. | ai |
| `car.start.fail` | The engine cranks but will not start. | ai |
| `car.suspension` | The car lands or crosses a bump. | ai |
| `car.turbo.blowoff` | The blow-off valve releases on a gear change. | ai |
| `car.turbo.spool` | The turbo spools up under load. | ai |
| `car.tyre.squeal` | Sustained tyre scrub through a long corner. Loops. | ai |
| `car.window` | An electric window winds down. | ai |
| `car.wiper` | Windscreen wipers sweep. Loops. | ai |

**`coin.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `coin.count` | Each tick while a score or coin total counts up on a result screen. | code |
| `coin.shower` | A burst of coins flies to the counter, or a reward total counts up. | code |

**`cook.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `cook.boil` | Water boiling in a pot. Loops. | ai |
| `cook.chop` | Chopping food on a board. | ai |
| `cook.fridge.open` | A fridge or cabinet opens. | ai |
| `cook.oven.ding` | An oven or microwave finishes. | ai |
| `cook.pour` | Liquid poured into a container. | ai |
| `cook.sizzle` | Food frying in a pan. Loops. | ai |

**`craft.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `craft.forge` | Hammering hot metal on an anvil — smithing, upgrading. | ai |
| `craft.sew` | Stitching fabric — tailoring, crafting. | ai |

**`creature.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `creature.die` | An enemy is defeated and vanishes. | ai |
| `creature.growl` | A creature growls a warning before attacking. | ai |
| `creature.roar` | A big monster or boss roars. | ai |
| `creature.squeak` | A small cute creature squeaks — slime, pet, critter. | ai |

**`crowd.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `crowd.applause` | The crowd applauds — win screen, big achievement. | ai |
| `crowd.boo` | The crowd boos — failure, bad move. | ai |
| `crowd.gasp` | The crowd gasps — a surprise, a near miss. | ai |

**`door.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `door.bell` | A doorbell rings. | ai |
| `door.close` | A door, gate or hatch closes. | ai |
| `door.knock` | Someone knocks. | ai |
| `door.locked` | A locked door rattles. | ai |
| `door.metal.open` | A heavy metal door opens. | ai |
| `door.open` | A door, gate or hatch opens. | ai |
| `door.slam` | A door slams shut. | ai |
| `door.slide` | A sliding door runs on its track. | ai |
| `door.wood.open` | A wooden door opens. | ai |

**`engine.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `engine.loop` | An engine running while driving. Loops; change pitch with rate for speed. | ai |
| `engine.start` | A car, kart or machine starts up. | ai |

**`explosion.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `explosion.big` | A real, heavy explosion with debris and rumble. | ai |
| `explosion.small` | A small stylized blast: a bomb, a popped enemy, a firework. | code |

**`farm.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `farm.harvest` | A crop is pulled or cut — harvesting. | ai |
| `farm.plant` | Seeds are planted in soil. | ai |
| `farm.water` | Watering plants from a can. | ai |

**`fire.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `fire.crackle` | A campfire, torch or burning object nearby. Loops. | ai |
| `fire.extinguish` | A flame is put out. | ai |
| `fire.ignite` | Something catches light. | ai |
| `fire.lighter` | A lighter flicks on. | ai |
| `fire.match` | A match is struck. | ai |
| `fire.torch` | A handheld torch burns. Loops. | ai |

**`game.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `game.bullet.whizby` | A projectile flies close past the player. | ai |
| `game.checkpoint` | A checkpoint is reached — progress saved. | ai |
| `game.portal` | A portal opens or is entered. | ai |
| `game.ricochet` | A bullet or projectile bounces off metal or stone. | ai |
| `game.shield.break` | A shield or barrier shatters. | ai |
| `game.spawn` | An enemy or object appears in the world. | ai |
| `game.tower.place` | A tower, building or block is placed. | ai |
| `game.wave.start` | A new wave or round begins — tower defence, survival. | ai |

**`gun.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `gun.bolt` | The bolt or slide is pulled. | ai |
| `gun.crossbow` | A crossbow looses a bolt. | ai |
| `gun.flamethrower` | A flamethrower burns. Loops. | ai |
| `gun.grenade.pin` | A grenade pin is pulled. | ai |
| `gun.grenade.throw` | A grenade is thrown. | ai |
| `gun.mag.in` | A fresh magazine is seated. | ai |
| `gun.mag.out` | A magazine is ejected. | ai |
| `gun.minigun` | A minigun spins up and fires. Loops. | ai |
| `gun.reload.shotgun` | Shells are pumped into a shotgun. | ai |
| `gun.revolver` | A revolver fires. | ai |
| `gun.rocket.launch` | A rocket launcher fires. | ai |
| `gun.shell.drop` | A spent shell hits the ground. | ai |
| `gun.silenced` | A suppressed shot. | ai |
| `gun.smg` | A submachine gun burst. | ai |
| `gun.sniper` | A sniper rifle fires. | ai |

**`horror.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `horror.bell` | A distant church bell tolls — dread, time passing. | ai |
| `horror.breathing` | Nervous breathing — low health, hiding, stamina. | ai |
| `horror.creak` | A door or floorboard creaks slowly — suspense. | ai |
| `horror.growl.deep` | Something very large growls in the dark. | ai |
| `horror.heartbeat` | A heartbeat under tension — low health, chase, hiding. Loops. | ai |
| `horror.jumpscare` | A sudden scare hit. | ai |
| `horror.knock.slow` | Slow deliberate knocking. | ai |
| `horror.laugh` | An unsettling laugh. | ai |
| `horror.musicbox` | A music box plays — classic dread. | ai |
| `horror.scream` | A terrified scream. | ai |
| `horror.static` | Radio or TV static. Loops. | ai |
| `horror.whisper` | An unsettling whisper — ghost, haunting, secret. | ai |

**`impact.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `impact.bounce` | A ball, bubble or character bounces off something. | code |
| `impact.crit` | A critical hit or perfect timing. Layer it ON TOP of the normal hit sound. | hybrid |
| `impact.metal` | Something hits metal: armour, a robot, a car, a pipe. | ai |
| `impact.miss` | An attack misses, or something flies past the player. | code |
| `impact.punch` | A fist or body hit connects. | ai |
| `impact.thud` | A soft generic landing or bump. The cheapest impact — good for stylized games. | code |
| `impact.wood` | Something hits wood: a crate, a door, a bat, a tree. | ai |

**`kitchen.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `kitchen.blender` | A blender runs. | ai |
| `kitchen.bottle.open` | A bottle is uncorked or opened. | ai |
| `kitchen.can.open` | A drink can is opened. | ai |
| `kitchen.cutlery` | Cutlery clatters on a plate. | ai |
| `kitchen.egg.crack` | An egg is cracked. | ai |
| `kitchen.kettle` | A kettle comes to the boil. | ai |
| `kitchen.microwave` | A microwave finishes and beeps. | ai |
| `kitchen.sip` | A drink is sipped. | ai |

**`machine.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `machine.conveyor` | A conveyor or factory line runs. Loops. | ai |
| `machine.elevator` | A lift arrives and the doors open. | ai |
| `machine.robot.servo` | A robot joint moves — mech, turret, droid. | ai |
| `machine.steam` | Steam vents — machinery, valve, pressure release. | ai |

**`magic.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `magic.buff` | A booster, power-up or upgrade activates. | code |
| `magic.dark` | A dark or shadow spell. | ai |
| `magic.earth` | An earth or stone spell. | ai |
| `magic.fire` | A fireball, flamethrower or burning attack. Fire texture is impossible in code. | ai |
| `magic.fire.cast` | A fire spell winds up. | ai |
| `magic.fire.hit` | A fireball lands. | ai |
| `magic.heal` | Healing, restoring energy or refilling lives. | code |
| `magic.holy` | A holy or blessing spell. | ai |
| `magic.ice` | Freezing, an ice attack, or something turning to crystal. | hybrid |
| `magic.ice.cast` | An ice spell winds up. | ai |
| `magic.ice.hit` | Ice strikes and shatters on a target. | ai |
| `magic.lightning.cast` | A lightning spell is cast. | ai |
| `magic.lightning.hit` | Lightning strikes a target. | ai |
| `magic.shield` | A shield, barrier or invincibility turns on. | code |
| `magic.shield.hit` | Something strikes a magic barrier. | ai |
| `magic.shield.up` | A magic barrier comes up. | ai |
| `magic.sparkle` | A small magical shimmer: a glow, a wand touch, an item twinkling. | code |
| `magic.summon` | Summoning, a portal opening, a boss appearing. | code |
| `magic.wind` | A wind or gust spell. | ai |

**`match.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `match.blast` | A booster fires: rocket, bomb, lightning, rainbow clear. | hybrid |
| `match.combo` | A combo step. Play it once per combo level with a rising pitch — SFX.play('match.combo', { rate: 1 + n * 0.12 }). | code |
| `match.pop` | A tile, bubble or block is cleared. The core match-3 sound. | code |
| `match.shuffle` | The board reshuffles, or cards are dealt. | ai |
| `match.swap` | Two tiles swap places. | code |

**`melee.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `melee.axe.swing` | A heavy axe swings. | ai |
| `melee.block` | A hit is blocked on a shield. | ai |
| `melee.dodge` | A dodge or evade — body moving fast. | ai |
| `melee.hammer.swing` | A war hammer swings. | ai |
| `melee.kick` | A heavy kick lands. | ai |
| `melee.parry` | A blade is deflected at the last moment. | ai |
| `melee.sheathe` | A blade is put away. | ai |
| `melee.spear` | A spear thrusts. | ai |
| `melee.stab` | A blade goes in. | ai |
| `melee.whip` | A whip cracks. | ai |

**`moto.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `moto.idle` | A motorbike idles. Loops. | ai |
| `moto.pass` | A motorbike flies past. | ai |
| `moto.rev` | A motorbike revs hard. | ai |

**`move.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `move.climb` | Grabbing a ledge, climbing a rope or scrambling up. | ai |
| `move.cloth` | A cape, dodge or quick body movement that needs fabric. | ai |
| `move.dash` | A dash, dodge roll, boost or sudden burst of speed. | code |
| `move.fly` | A jetpack, hover or flight boost. Short burst, retrigger while held. | code |
| `move.jump` | The character jumps. | code |
| `move.jump.double` | A second or mid-air jump. Higher and airier than move.jump. | code |
| `move.land` | The character lands after a jump or fall. | code |
| `move.slide` | Sliding, skidding or braking along a surface. | code |
| `move.swim` | A swimming stroke or moving through water. | ai |
| `move.teleport` | Teleporting, warping, spawning in or vanishing. | code |

**`music.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `music.action.1` | Shooters, brawlers and combat. Tense and driving without being oppressive. | ai |
| `music.action.2` | Shooters, brawlers and combat. Tense and driving without being oppressive. | ai |
| `music.action.3` | Shooters, brawlers and combat. Tense and driving without being oppressive. | ai |
| `music.adventure.1` | Adventure, exploration and RPG overworld. | ai |
| `music.adventure.2` | Adventure, exploration and RPG overworld. | ai |
| `music.adventure.3` | Adventure, exploration and RPG overworld. | ai |
| `music.boss.1` | Boss fights and final showdowns. The most intense music in the game. | ai |
| `music.boss.2` | Boss fights and final showdowns. The most intense music in the game. | ai |
| `music.boss.3` | Boss fights and final showdowns. The most intense music in the game. | ai |
| `music.casual.1` | Match-3, puzzle and casual games. Light and friendly, never distracting. | ai |
| `music.casual.2` | Match-3, puzzle and casual games. Light and friendly, never distracting. | ai |
| `music.casual.3` | Match-3, puzzle and casual games. Light and friendly, never distracting. | ai |
| `music.cozy.1` | Farming, idle, life sim and crafting. Warm and unhurried. | ai |
| `music.cozy.2` | Farming, idle, life sim and crafting. Warm and unhurried. | ai |
| `music.cozy.3` | Farming, idle, life sim and crafting. Warm and unhurried. | ai |
| `music.horror.1` | Horror, survival and tension. Sparse and unsettling. | ai |
| `music.horror.2` | Horror, survival and tension. Sparse and unsettling. | ai |
| `music.horror.3` | Horror, survival and tension. Sparse and unsettling. | ai |
| `music.hypercasual.1` | Hyper-casual games: one-tap, endless runner, arcade. Simple and driving. | ai |
| `music.hypercasual.2` | Hyper-casual games: one-tap, endless runner, arcade. Simple and driving. | ai |
| `music.hypercasual.3` | Hyper-casual games: one-tap, endless runner, arcade. Simple and driving. | ai |
| `music.menu.1` | Main menu, lobby, shop and between-level screens. | ai |
| `music.menu.2` | Main menu, lobby, shop and between-level screens. | ai |
| `music.menu.3` | Main menu, lobby, shop and between-level screens. | ai |
| `music.racing.1` | Racing and driving games. High energy electronic. | ai |
| `music.racing.2` | Racing and driving games. High energy electronic. | ai |
| `music.racing.3` | Racing and driving games. High energy electronic. | ai |
| `music.scifi.1` | Sci-fi, space and cyberpunk. | ai |
| `music.scifi.2` | Sci-fi, space and cyberpunk. | ai |
| `music.scifi.3` | Sci-fi, space and cyberpunk. | ai |

**`nature.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `nature.leaves` | Rustling foliage — walking through bushes, searching undergrowth. | ai |
| `nature.water.flow` | A running stream. Loops. | ai |

**`object.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `object.balloon.pop` | A balloon bursts — party, target, bubble. | ai |
| `object.book.close` | A book shuts — menu closed, chapter done. | ai |
| `object.camera` | A camera shutter — photo, capture, screenshot. | ai |
| `object.chain` | Chains rattle — gate, prison, anchor. | ai |
| `object.clock.tick` | A clock ticking — timer pressure. Loops. | ai |
| `object.coin.drop` | A coin falls onto a hard surface. | ai |
| `object.firework` | A firework launches and bursts — celebration. | ai |
| `object.glass.clink` | Glasses clink — toast, potion, bottle. | ai |
| `object.keyboard` | Typing on a keyboard — hacking, terminal, chat. | ai |
| `object.lock` | A padlock or bolt clicks shut or open. | ai |
| `object.page.turn` | A page turns — book, journal, tutorial. | ai |
| `object.paper.crumple` | Paper is crushed — discard, delete, note. | ai |
| `object.rope` | Rope creaks under tension — pulling, climbing, bridge. | ai |
| `object.switch` | A physical switch or lever is thrown. | ai |
| `object.zip` | A zip fastens — bag, jacket, inventory. | ai |

**`office.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `office.drawer` | A drawer opens or closes. | ai |
| `office.printer` | A printer prints a page. | ai |
| `office.stapler` | A stapler clicks. | ai |

**`phone.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `phone.ring` | A phone rings. | ai |
| `phone.vibrate` | A phone buzzes on a surface. | ai |

**`pickup.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `pickup.ammo` | Ammo, tools or equipment picked up. | ai |
| `pickup.coin` | One coin collected. Fires constantly, so it is short and varies every time. | code |
| `pickup.food` | Eating: fruit, candy, a power snack. Organic and wet — code cannot fake this. | ai |
| `pickup.gem` | A gem, crystal or premium currency is collected. Glassier than a coin. | code |
| `pickup.heart` | A life, heart or health pickup. | code |
| `pickup.key` | A key, card or quest item is picked up. | code |
| `pickup.star` | A star or collectible token is picked up during gameplay. | code |

**`race.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `race.finish` | The chequered flag — race over. | ai |
| `race.flag.wave` | A flag snaps in the wind. | ai |
| `race.lap` | A lap is completed. | ai |
| `race.light` | A starting light changes on the grid. | ai |

**`reward.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `reward.chest` | A chest, box or crate opens and reveals its contents. | ai |
| `reward.claim` | The player claims a reward, buys an item or opens a gift. | code |
| `reward.jackpot` | A rare drop, jackpot or huge prize. The biggest reward sound in the game. | ai |
| `reward.star` | One star fills on a level-complete screen. The library raises the pitch per star automatically. | code |

**`rpg.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `rpg.armor.equip` | Armour or heavy gear is put on. | ai |
| `rpg.curse` | A dark spell or debuff lands. | ai |
| `rpg.enchant` | An item is enchanted or blessed. | ai |
| `rpg.gold` | A pile of gold coins is gathered. | ai |
| `rpg.potion` | A potion is drunk — healing, buff. | ai |
| `rpg.quest.accept` | A quest is accepted or a journal updates. | ai |
| `rpg.scroll` | A scroll or map unrolls. | ai |
| `rpg.spell.cast` | A generic spell is cast. | ai |
| `rpg.sword.draw` | A blade is drawn from a sheath. | ai |
| `rpg.trap` | A trap springs — spikes, snare, alarm. | ai |

**`scifi.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `scifi.airlock` | A pressurised door opens — spaceship, vault, lab. | ai |
| `scifi.alarm` | A ship or base alarm. Loops. | ai |
| `scifi.computer.beep` | A console acknowledges input. | ai |
| `scifi.door` | An automatic door slides open. | ai |
| `scifi.engine.hum` | Spaceship engine hum. Loops. | ai |
| `scifi.glitch` | A digital error or corruption — hacking, damage, static. | ai |
| `scifi.hologram` | A hologram appears or flickers. | ai |
| `scifi.laser.charge` | An energy weapon charges before firing. | ai |
| `scifi.powerdown` | A machine or system powers down. | ai |
| `scifi.powerup` | A machine or system powers up. | ai |
| `scifi.robot.talk` | A robot speaks in machine noise. | ai |
| `scifi.scanner` | A scanner sweeps — detection, radar, search. | ai |
| `scifi.shield.hit` | A ship or suit shield takes a hit. | ai |
| `scifi.warp` | A jump to lightspeed. | ai |

**`sport.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `sport.ball.bounce` | A ball bounces on a hard surface. | ai |
| `sport.ball.kick` | A ball is kicked or struck hard. | ai |
| `sport.bat.hit` | A bat or club strikes a ball. | ai |
| `sport.bowling` | A bowling ball hits the pins. | ai |
| `sport.boxing.bell` | The boxing bell rings a round. | ai |
| `sport.buzzer` | An end-of-round buzzer. | ai |
| `sport.crowd.goal` | The crowd erupts at a goal. | ai |
| `sport.golf` | A golf club strikes the ball. | ai |
| `sport.net.swish` | A ball passes cleanly through a net — basket scored. | ai |
| `sport.pool.break` | A pool break scatters the balls. | ai |
| `sport.racket.hit` | A racket strikes a ball — tennis, padel, squash. | ai |
| `sport.skate` | A skateboard rolls and grinds. | ai |
| `sport.ski` | Skis carve through snow. Loops. | ai |
| `sport.stadium` | Stadium crowd ambience. Loops. | ai |
| `sport.start.gun` | A starting pistol fires — race begins. | ai |
| `sport.whistle` | A referee whistle — round start, foul, time up. | ai |

**`state.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `state.gameover` | The run is over for good — endless runner death, all lives lost. | ai |
| `state.levelup` | The player levels up or ranks up. | ai |
| `state.lose` | The level is failed. Plays once on the Fail screen. | ai |
| `state.newrecord` | A new high score or personal best. | ai |
| `state.win` | The level is completed. Plays once on the Success screen. | ai |
| `state.win.small` | A small win inside gameplay: a wave cleared, a goal met, a quest step done. | code |

**`step.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `step.carpet` | One footstep on on thick carpet. Play per step; the library varies pitch and picks a different take each time. | ai |
| `step.grass` | One footstep on grass. Play per step; the library varies pitch and picks a different take each time. | ai |
| `step.gravel` | One footstep on gravel. Play per step; the library varies pitch and picks a different take each time. | ai |
| `step.ice` | One footstep on on solid ice. Play per step; the library varies pitch and picks a different take each time. | ai |
| `step.leaves` | One footstep on through dry fallen leaves. Play per step; the library varies pitch and picks a different take each time. | ai |
| `step.metal` | One footstep on metal. Play per step; the library varies pitch and picks a different take each time. | ai |
| `step.mud` | One footstep on through wet mud. Play per step; the library varies pitch and picks a different take each time. | ai |
| `step.run.stone` | One footstep while running on stone. Faster and harder than walking. | ai |
| `step.sand` | One footstep on sand. Play per step; the library varies pitch and picks a different take each time. | ai |
| `step.snow` | One footstep on snow. Play per step; the library varies pitch and picks a different take each time. | ai |
| `step.stairs` | One footstep on up a wooden staircase. Play per step; the library varies pitch and picks a different take each time. | ai |
| `step.stone` | One footstep on stone. Play per step; the library varies pitch and picks a different take each time. | ai |
| `step.tile` | One footstep on on hard ceramic tiles. Play per step; the library varies pitch and picks a different take each time. | ai |
| `step.water` | One footstep on water. Play per step; the library varies pitch and picks a different take each time. | ai |
| `step.wood` | One footstep on wood. Play per step; the library varies pitch and picks a different take each time. | ai |

**`tool.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `tool.chop.wood` | An axe splits a log. | ai |
| `tool.dig` | Digging with a shovel — farming, treasure, burying. | ai |
| `tool.drill` | A power drill runs — repair, construction. | ai |
| `tool.hammer` | Hammering a nail — building, crafting, repair. | ai |
| `tool.pickaxe` | Mining stone with a pickaxe. | ai |
| `tool.saw` | Sawing wood — building, crafting. | ai |
| `tool.wrench` | A spanner or ratchet turns — repair, machinery. | ai |

**`truck.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `truck.airbrake` | Air brakes release with a hiss. | ai |
| `truck.horn` | An air horn blasts. | ai |
| `truck.idle` | A diesel truck idles. Loops. | ai |

**`ui.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `ui.back` | Back, close or cancel. The darker twin of ui.tap. | code |
| `ui.confirm` | A choice is accepted: settings saved, difficulty picked, name entered. | code |
| `ui.countdown` | 3… 2… 1… before a level starts. Play once per number, then state.go. | code |
| `ui.error` | The action is not allowed: not enough coins, locked level, wrong move. | code |
| `ui.go` | The GO! at the end of a countdown, when gameplay starts. | code |
| `ui.locked` | The player taps something still locked. | code |
| `ui.notify` | Something new appeared: a message, a gift, a quest, a friend request. | code |
| `ui.slider` | A slider handle passes a step. Fires rapidly, so it is very short and quiet. | code |
| `ui.swipe` | The player swipes a card, page or carousel. | code |
| `ui.tap` | The player taps any button. The most-used sound in the game. | code |
| `ui.tap.soft` | Secondary taps: list rows, tab switches, small toggles. Quieter than ui.tap. | code |
| `ui.tick` | Countdown timer in its warning seconds, or a number counting up. | code |
| `ui.toggle` | A switch, checkbox or tab changes state. | code |
| `ui.type` | Letter-by-letter dialogue or name entry. | code |
| `ui.unlock` | A level, skin, chapter or feature unlocks. | code |
| `ui.whoosh` | A popup opens or a screen slides in. | code |

**`vehicle.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `vehicle.bike` | A bicycle bell rings. | ai |
| `vehicle.boat` | A small boat motor runs. Loops. | ai |
| `vehicle.brake` | Hard braking, a handbrake turn or skidding to a stop. | ai |
| `vehicle.crash` | A vehicle collision. | ai |
| `vehicle.gear` | A gear change — racing, machinery. | ai |
| `vehicle.helicopter` | Helicopter rotors overhead. Loops. | ai |
| `vehicle.horn` | A car horn sounds. | ai |
| `vehicle.plane` | A plane passes overhead. | ai |
| `vehicle.rev` | An engine revs hard — boost, start line, showing off. | ai |
| `vehicle.train` | A train passes or pulls away. | ai |

**`voice.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `voice.aww` | A disappointed reaction to a loss. | ai |
| `voice.cheer` | The player wins something big. Layer under state.win for extra celebration. | ai |
| `voice.countdown.go` | A voice shouts GO at the start of a race or round. | ai |
| `voice.grunt` | The character jumps, lifts, swings or takes effort. | ai |
| `voice.hurt` | The character takes damage. | ai |
| `voice.laugh` | A playful taunt, a mascot reaction, a funny fail. | ai |
| `voice.yay` | A happy child voice reacts to a reward. | ai |

**`water.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `water.bubble` | Bubbles rise through water. | ai |
| `water.dive` | A body enters the water. | ai |
| `water.drip` | A single drip — cave, leak, tension. | ai |
| `water.fountain` | A fountain runs. Loops. | ai |
| `water.splash` | Something falls into water, or a big splash on impact. | ai |
| `water.tap` | A running tap. Loops. | ai |
| `water.underwater` | Submerged ambience. Loops. | ai |
| `water.wave.crash` | A big wave breaks. | ai |

**`weapon.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `weapon.bow` | Firing a bow or crossbow. | ai |
| `weapon.cannon` | A cannon, mortar or heavy artillery firing. | ai |
| `weapon.charge` | Holding down a charged shot or an ability winding up. | code |
| `weapon.empty` | Out of ammo — the trigger clicks on nothing. | ai |
| `weapon.laser` | Standard sci-fi blaster shot. The default for any space or robot shooter. | code |
| `weapon.laser.big` | Heavy or charged energy shot, boss cannon, ultimate ability. | code |
| `weapon.pistol` | A realistic handgun shot. | ai |
| `weapon.plasma` | Softer, rounder energy shot — bubble guns, goo shooters, magic bolts. | code |
| `weapon.reload` | Reloading a weapon. | ai |
| `weapon.rifle.auto` | A short burst of automatic fire. Loop or retrigger for sustained fire. | ai |
| `weapon.shotgun` | A shotgun blast. | ai |
| `weapon.sword.clash` | Two blades meeting, or a blade blocked by a shield. | ai |
| `weapon.sword.swing` | Swinging a blade through the air and hitting nothing. | ai |
| `weapon.throw` | Throwing anything: a ball, a knife, a bomb, a grappling hook. | code |
| `weapon.zap` | Electric attack, taser, lightning, short circuit. | code |

**`weather.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `weather.rain.heavy` | Heavy downpour. Loops. | ai |
| `weather.rain.light` | Light rain. Loops. | ai |
| `weather.rain.window` | Rain on glass. Loops. | ai |
| `weather.storm.wind` | Storm wind howling. Loops. | ai |
| `weather.thunder` | A thunderclap — storm, dramatic moment. | ai |
| `weather.thunder.distant` | Thunder rolls far away. | ai |
<!-- SOUNDS:END -->

Machine-readable, with durations and offsets: `dist/casual.json`.
Check from code: `SFX.list()`, `SFX.list('reward')`, `SFX.has('coin.collect')`, `SFX.info('coin.collect')`.

## 4. Sound on a UI element without JavaScript

```html
<button class="sc-button" data-sfx="reward.claim">Claim</button>
<button class="sc-button" data-sfx="none">Silent</button>
```

## 4b. Music

30 looping tracks, three per genre: `casual`, `hypercasual`, `action`, `racing`, `adventure`,
`boss`, `horror`, `cozy`, `scifi`, `menu`.

```js
SFX.music('music.casual.2');        // starts, loops forever, crossfades from whatever was playing
SFX.music('music.boss.1');          // switching tracks crossfades automatically
SFX.duck(0.25, 1500);               // dip the music under a win or a big moment
SFX.stopMusic();                    // fade out
```

Music is **not** part of the sound sprite: each track is its own stereo file and only the one
you play is downloaded. Tracks loop gaplessly, so a bed can run for as long as the player
stays on a screen.

Start music from a real tap (the Play button, not the loading screen) — browsers block audio
until the player has interacted.

## 5. Volume, mute and the settings screen

```js
SFX.volume('music', 0.4);    // categories: master, ui, game, reward, music
SFX.mute();                  // toggle; returns the new state
SFX.mute(true);
SFX.muted;                   // read it back
```
Volumes and mute are remembered between sessions automatically. Wire the kit's Settings sliders straight to `SFX.volume(...)` — no saving code needed.

## 6. Rules for AI agents

1. **Only use names from the table above.** Never invent a sound name, never generate audio, never build your own Web Audio oscillators. If you need a variant, change `rate` and `volume` on an existing sound.
2. If nothing fits, pick the closest by category and say so — do not leave the moment silent and do not build your own sound.
3. One `ui.tap` per tap. Do not stack several sounds on one button.
4. `state.win` and `state.lose` play **once** per level end, not per star.
5. Call `SFX.duck()` before a long celebration so the music does not fight it.
6. Never call `SFX.play()` on page load — mobile browsers block audio until the player's first tap. The library unlocks itself on that first tap.
7. Music needs a real user tap first. Start it from the Play button, not from the loading screen.
