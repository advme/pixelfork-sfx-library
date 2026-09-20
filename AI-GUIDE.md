# Pixelfork SFX Library — AI guide

Ready-made game sound effects for AI-generated web games. **You never create or describe audio — you call a name from the list below.**

403 sounds, 30 of them looping music tracks. 51 are **made by code** (they play instantly and weigh nothing) and the rest are **real audio files**. You do not need to care which: `SFX.play(name)` works the same either way.

## 1. Add it (2 lines)

```html
<script src="https://advme.github.io/pixelfork-sfx-library/dist/sfx.js"></script>
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

**`body.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `body.cough` | A cough. | ai |
| `body.footstep.bare` | A barefoot step on a hard floor. | ai |
| `body.heartbeat.fast` | A racing heartbeat. Loops. | ai |
| `body.knuckle` | Knuckles crack before a fight. | ai |
| `body.shiver` | Teeth chatter with cold. | ai |
| `body.sneeze` | A sneeze. | ai |
| `body.sniff` | A sniff. | ai |
| `body.stomach` | A hungry stomach rumbles. | ai |
| `body.swallow` | A nervous swallow. | ai |
| `body.yawn` | A yawn. | ai |

**`break.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `break.glass` | Glass, ice or a crystal shatters. | ai |
| `break.pot` | A pot, vase or ceramic container smashes. | ai |
| `break.stone` | Rock, brick or concrete breaks. | ai |
| `break.wood` | A crate, plank, barrel or door breaks apart. | ai |

**`build.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `build.brick` | A brick is laid in mortar. | ai |
| `build.bulldozer` | A bulldozer pushes earth. Loops. | ai |
| `build.cement` | A cement mixer turns. Loops. | ai |
| `build.complete` | A building finishes construction. | ai |
| `build.crane` | A crane lifts a load. Loops. | ai |
| `build.glass.fit` | A pane of glass is fitted. | ai |
| `build.jackhammer` | A jackhammer breaks concrete. Loops. | ai |
| `build.measure` | A tape measure snaps back. | ai |
| `build.nail.gun` | A nail gun fires. | ai |
| `build.saw.power` | A circular saw cuts timber. | ai |
| `build.scaffold` | Scaffolding poles clang together. | ai |
| `build.weld` | Welding sparks. | ai |

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

**`casino.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `casino.ambience` | Casino floor ambience. Loops. | ai |
| `casino.bell` | The win bell rings. | ai |
| `casino.card.deal` | One card is dealt. | ai |
| `casino.card.flip` | A card is turned face up. | ai |
| `casino.chips.stack` | Chips are stacked or counted. | ai |
| `casino.chips.toss` | Chips are pushed into the pot. | ai |
| `casino.dice.roll` | Dice are thrown. | ai |
| `casino.dice.shake` | Dice rattle in a cup. | ai |
| `casino.lever` | The slot lever is pulled. | ai |
| `casino.payout` | Coins pour out of a machine. | ai |
| `casino.reel.spin` | A slot reel starts spinning. Loops while it runs. | ai |
| `casino.reel.stop` | One slot reel lands. | ai |
| `casino.roulette.drop` | The roulette ball settles into a pocket. | ai |
| `casino.roulette.spin` | The roulette wheel spins. Loops. | ai |

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

**`emote.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `emote.cheer.one` | One person cheers. | ai |
| `emote.clap` | A single person claps. | ai |
| `emote.drumroll` | A drumroll before a reveal. | ai |
| `emote.huh` | A confused reaction. | ai |
| `emote.kiss` | A blown kiss. | ai |
| `emote.oops` | A small mistake reaction. | ai |
| `emote.sigh` | A weary sigh. | ai |
| `emote.snap` | A finger snap. | ai |
| `emote.taunt` | A mocking taunt. | ai |
| `emote.whistle` | An admiring whistle. | ai |

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

**`fish.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `fish.bob` | A float bobs and dips. | ai |
| `fish.cast` | A fishing rod casts. | ai |
| `fish.catch` | A fish is landed. | ai |
| `fish.flop` | A caught fish flaps about. | ai |
| `fish.line.snap` | The line breaks. | ai |
| `fish.net` | A landing net scoops. | ai |
| `fish.reel.fast` | A fish runs and the drag screams. | ai |
| `fish.reel.in` | Reeling in. Loops. | ai |
| `fish.tacklebox` | A tackle box opens. | ai |
| `fish.water.calm` | Calm lake water. Loops. | ai |

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

**`holiday.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `holiday.birthday` | A birthday moment. | ai |
| `holiday.church.bells` | Church bells peal. | ai |
| `holiday.confetti` | A confetti cannon fires. | ai |
| `holiday.cork.pop` | A champagne cork pops. | ai |
| `holiday.cracker` | A christmas cracker snaps. | ai |
| `holiday.halloween.creak` | A spooky creak. | ai |
| `holiday.newyear` | New year countdown moment. | ai |
| `holiday.organ` | A pipe organ stab. | ai |
| `holiday.party.horn` | A party blower. | ai |
| `holiday.sleighbells` | Sleigh bells jingle. | ai |
| `holiday.wrapping` | Wrapping paper is torn. | ai |

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

**`idle.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `idle.autocollect` | An automated collector picks something up. | ai |
| `idle.coin.rain` | Coins rain down after a big gain. | ai |
| `idle.generator` | A generator or factory runs. Loops. | ai |
| `idle.levelup` | A generator or hero levels up. | ai |
| `idle.milestone` | A milestone number is reached. | ai |
| `idle.multiplier` | A multiplier increases. | ai |
| `idle.offline` | Offline earnings are collected on return. | ai |
| `idle.prestige` | A prestige or rebirth reset. | ai |
| `idle.tap` | The main tap in a clicker. Fires constantly. | ai |
| `idle.upgrade.chain` | Several upgrades buy at once. | ai |

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

**`med.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `med.anvil` | A smith strikes the anvil. | ai |
| `med.arrow.hit` | An arrow strikes wood. | ai |
| `med.arrow.volley` | A volley of arrows flies. | ai |
| `med.catapult` | A catapult launches. | ai |
| `med.chest.lock` | A treasure chest is unlocked. | ai |
| `med.coin.purse` | A purse of coins is handled. | ai |
| `med.drawbridge` | A drawbridge lowers. | ai |
| `med.dungeon.door` | A heavy dungeon door opens. | ai |
| `med.gate` | A castle gate opens. | ai |
| `med.portcullis` | A portcullis drops. | ai |
| `med.scroll.open` | A scroll is unrolled. | ai |
| `med.siege.impact` | A boulder smashes a wall. | ai |
| `med.tavern` | Tavern ambience. Loops. | ai |
| `med.torch.mount` | A torch is taken from a wall. | ai |

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
| `music.casino.1` | Casino floors, card tables, lounge scenes. | ai |
| `music.casino.2` | Casino floors, card tables, lounge scenes. | ai |
| `music.casino.3` | Casino floors, card tables, lounge scenes. | ai |
| `music.casual.1` | Match-3, puzzle and casual games. Light and friendly, never distracting. | ai |
| `music.casual.2` | Match-3, puzzle and casual games. Light and friendly, never distracting. | ai |
| `music.casual.3` | Match-3, puzzle and casual games. Light and friendly, never distracting. | ai |
| `music.chase.1` | Pursuit, escape, timer running out. | ai |
| `music.chase.2` | Pursuit, escape, timer running out. | ai |
| `music.chase.3` | Pursuit, escape, timer running out. | ai |
| `music.chiptune.1` | Retro arcade and 8-bit styled games. | ai |
| `music.chiptune.2` | Retro arcade and 8-bit styled games. | ai |
| `music.chiptune.3` | Retro arcade and 8-bit styled games. | ai |
| `music.comedy.1` | Cartoon slapstick, silly failures, funny moments. | ai |
| `music.comedy.2` | Cartoon slapstick, silly failures, funny moments. | ai |
| `music.comedy.3` | Cartoon slapstick, silly failures, funny moments. | ai |
| `music.cozy.1` | Farming, idle, life sim and crafting. Warm and unhurried. | ai |
| `music.cozy.2` | Farming, idle, life sim and crafting. Warm and unhurried. | ai |
| `music.cozy.3` | Farming, idle, life sim and crafting. Warm and unhurried. | ai |
| `music.desert.1` | Middle-Eastern and Arabian settings, markets, dunes. | ai |
| `music.desert.2` | Middle-Eastern and Arabian settings, markets, dunes. | ai |
| `music.desert.3` | Middle-Eastern and Arabian settings, markets, dunes. | ai |
| `music.epic.1` | Trailers, cinematic reveals, big story moments. | ai |
| `music.epic.2` | Trailers, cinematic reveals, big story moments. | ai |
| `music.epic.3` | Trailers, cinematic reveals, big story moments. | ai |
| `music.horror.1` | Horror, survival and tension. Sparse and unsettling. | ai |
| `music.horror.2` | Horror, survival and tension. Sparse and unsettling. | ai |
| `music.horror.3` | Horror, survival and tension. Sparse and unsettling. | ai |
| `music.hypercasual.1` | Hyper-casual games: one-tap, endless runner, arcade. Simple and driving. | ai |
| `music.hypercasual.2` | Hyper-casual games: one-tap, endless runner, arcade. Simple and driving. | ai |
| `music.hypercasual.3` | Hyper-casual games: one-tap, endless runner, arcade. Simple and driving. | ai |
| `music.lofi.1` | Study, chill, idle and slow-burn games. | ai |
| `music.lofi.2` | Study, chill, idle and slow-burn games. | ai |
| `music.lofi.3` | Study, chill, idle and slow-burn games. | ai |
| `music.menu.1` | Main menu, lobby, shop and between-level screens. | ai |
| `music.menu.2` | Main menu, lobby, shop and between-level screens. | ai |
| `music.menu.3` | Main menu, lobby, shop and between-level screens. | ai |
| `music.oriental.1` | East-Asian settings, temples, gardens, martial arts. | ai |
| `music.oriental.2` | East-Asian settings, temples, gardens, martial arts. | ai |
| `music.oriental.3` | East-Asian settings, temples, gardens, martial arts. | ai |
| `music.puzzle.1` | Thinking music for puzzle games. Calmer than casual, no melody that pulls focus. | ai |
| `music.puzzle.2` | Thinking music for puzzle games. Calmer than casual, no melody that pulls focus. | ai |
| `music.puzzle.3` | Thinking music for puzzle games. Calmer than casual, no melody that pulls focus. | ai |
| `music.racing.1` | Racing and driving games. High energy electronic. | ai |
| `music.racing.2` | Racing and driving games. High energy electronic. | ai |
| `music.racing.3` | Racing and driving games. High energy electronic. | ai |
| `music.scifi.1` | Sci-fi, space and cyberpunk. | ai |
| `music.scifi.2` | Sci-fi, space and cyberpunk. | ai |
| `music.scifi.3` | Sci-fi, space and cyberpunk. | ai |
| `music.tavern.1` | Medieval inn, fantasy village, RPG rest stop. | ai |
| `music.tavern.2` | Medieval inn, fantasy village, RPG rest stop. | ai |
| `music.tavern.3` | Medieval inn, fantasy village, RPG rest stop. | ai |
| `music.tension.1` | Stealth, dread, the moment before something happens. | ai |
| `music.tension.2` | Stealth, dread, the moment before something happens. | ai |
| `music.tension.3` | Stealth, dread, the moment before something happens. | ai |
| `music.tropical.1` | Beach, island, summer and holiday settings. | ai |
| `music.tropical.2` | Beach, island, summer and holiday settings. | ai |
| `music.tropical.3` | Beach, island, summer and holiday settings. | ai |
| `music.underwater.1` | Submerged levels, dream sequences, floaty worlds. | ai |
| `music.underwater.2` | Submerged levels, dream sequences, floaty worlds. | ai |
| `music.underwater.3` | Submerged levels, dream sequences, floaty worlds. | ai |
| `music.western.1` | Deserts, duels, cowboy and frontier settings. | ai |
| `music.western.2` | Deserts, duels, cowboy and frontier settings. | ai |
| `music.western.3` | Deserts, duels, cowboy and frontier settings. | ai |
| `music.winter.1` | Snow levels, festive seasons, ice worlds. | ai |
| `music.winter.2` | Snow levels, festive seasons, ice worlds. | ai |
| `music.winter.3` | Snow levels, festive seasons, ice worlds. | ai |
| `music.zen.1` | Meditation, calm puzzle, wellness, relaxation modes. | ai |
| `music.zen.2` | Meditation, calm puzzle, wellness, relaxation modes. | ai |
| `music.zen.3` | Meditation, calm puzzle, wellness, relaxation modes. | ai |

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

**`plat.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `plat.checkpoint` | A checkpoint flag raises. | ai |
| `plat.coin.block` | Hitting a block that gives a reward. | ai |
| `plat.conveyor` | A conveyor belt carries the player. Loops. | ai |
| `plat.crumble` | A block crumbles under the player. | ai |
| `plat.key` | A key is collected. | ai |
| `plat.ladder` | Climbing a ladder rung. | ai |
| `plat.ledge` | The player grabs a ledge. | ai |
| `plat.life.lost` | The player loses a life. | ai |
| `plat.lock.open` | A lock opens and a door swings free. | ai |
| `plat.platform.move` | A moving platform travels. Loops. | ai |
| `plat.portal.enter` | The player enters a pipe or portal. | ai |
| `plat.powerup.grow` | The character grows or powers up. | ai |
| `plat.rope.swing` | Swinging on a rope. | ai |
| `plat.sawblade` | A spinning saw blade. Loops. | ai |
| `plat.spikes` | Spikes shoot up from the floor. | ai |
| `plat.spring` | A spring or bounce pad launches the player. | ai |
| `plat.trampoline` | A trampoline bounce. | ai |
| `plat.wallslide` | Sliding down a wall. | ai |

**`puzzle.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `puzzle.bomb.tick` | A bomb tile counts down. | ai |
| `puzzle.chess` | A chess piece is moved. | ai |
| `puzzle.correct` | A correct answer or valid move. | ai |
| `puzzle.domino` | Dominoes topple. | ai |
| `puzzle.hint` | A hint is revealed. | ai |
| `puzzle.jigsaw` | A jigsaw piece seats correctly. | ai |
| `puzzle.line.clear` | A full row or line clears. | ai |
| `puzzle.lock` | A piece locks into the grid permanently. | ai |
| `puzzle.reset` | The board is cleared and reset. | ai |
| `puzzle.rotate` | A block or piece rotates. | ai |
| `puzzle.snap` | A piece snaps into place. | ai |
| `puzzle.tile.place` | A tile is set down on the board. | ai |
| `puzzle.tile.slide` | A tile slides to a new position. | ai |
| `puzzle.timer` | Timer pressure ticking. Loops. | ai |
| `puzzle.undo` | A move is taken back. | ai |
| `puzzle.wrong` | A wrong answer or invalid move. | ai |

**`race.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `race.finish` | The chequered flag — race over. | ai |
| `race.flag.wave` | A flag snaps in the wind. | ai |
| `race.lap` | A lap is completed. | ai |
| `race.light` | A starting light changes on the grid. | ai |

**`rest.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `rest.chop.fast` | Rapid prep chopping. | ai |
| `rest.coffee` | An espresso machine runs. | ai |
| `rest.customer.angry` | A customer gives up and leaves. | ai |
| `rest.customer.happy` | A customer is satisfied. | ai |
| `rest.fryer` | A basket goes into the deep fryer. | ai |
| `rest.grill` | Food hits a hot grill. Loops. | ai |
| `rest.icecream` | Soft ice cream is dispensed. | ai |
| `rest.order.bell` | The order-up bell rings. | ai |
| `rest.plate` | A plate is set down on a counter. | ai |
| `rest.pour.drink` | A drink is poured into a glass. | ai |
| `rest.receipt` | A receipt prints. | ai |
| `rest.register` | The till opens and rings. | ai |

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

**`shop.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `shop.ad.reward` | A rewarded video finishes and pays out. | ai |
| `shop.coin.spend` | Currency is spent. | ai |
| `shop.gift` | A gift box opens. | ai |
| `shop.mail` | New mail arrives. | ai |
| `shop.piggy` | A piggy bank is smashed open. | ai |
| `shop.purchase.fail` | A purchase is declined or cancelled. | ai |
| `shop.purchase.ok` | A purchase completes successfully. | ai |
| `shop.restore` | Purchases are restored. | ai |
| `shop.streak` | A daily streak advances. | ai |
| `shop.subscribe` | A subscription starts. | ai |
| `shop.wheel.spin` | A prize wheel spins. Loops. | ai |
| `shop.wheel.stop` | The prize wheel lands on a segment. | ai |

**`space.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `space.airlock.cycle` | An airlock cycles. | ai |
| `space.beacon` | A distress beacon pulses. Loops. | ai |
| `space.cryo` | A cryo pod opens. | ai |
| `space.docking` | A docking clamp seals. | ai |
| `space.hull.stress` | The hull groans under stress. | ai |
| `space.oxygen.alarm` | Low oxygen warning. Loops. | ai |
| `space.radar` | A radar sweep pings. | ai |
| `space.rocket.launch` | A rocket lifts off. | ai |
| `space.stage.sep` | Stage separation. | ai |
| `space.thruster` | A manoeuvring thruster fires. | ai |
| `space.warp.charge` | A jump drive spins up. | ai |
| `space.zero.g` | Movement in zero gravity. | ai |

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

**`stealth.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `stealth.alert` | A guard notices something. | ai |
| `stealth.camera` | A security camera pans. | ai |
| `stealth.detected` | The player is spotted. | ai |
| `stealth.hide` | The player enters a hiding spot. | ai |
| `stealth.lockpick` | A lock is picked. | ai |
| `stealth.lost` | The guard loses track and calms down. | ai |
| `stealth.radio` | Radio chatter between guards. | ai |
| `stealth.sneak` | A slow careful footstep. | ai |
| `stealth.takedown` | A silent takedown. | ai |
| `stealth.vent` | A vent grate is removed. | ai |

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

**`sting.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `sting.boss.appear` | A boss enters. | ai |
| `sting.chapter` | A chapter or world title card. | ai |
| `sting.danger` | A sudden threat appears. | ai |
| `sting.defeat` | The player loses. | ai |
| `sting.gameover` | The run is over for good. | ai |
| `sting.level.start` | A level or round begins. | ai |
| `sting.levelup` | The player levels up. | ai |
| `sting.logo` | Studio logo or splash screen. | ai |
| `sting.newrecord` | A new high score. | ai |
| `sting.quest` | A quest or objective completes. | ai |
| `sting.rankup` | The player ranks up or promotes. | ai |
| `sting.reveal` | A prize or secret is revealed. | ai |
| `sting.sadtrombone` | A comedic failure. | ai |
| `sting.suspense` | A dramatic pause before a result. | ai |
| `sting.tada` | A small comedic success. | ai |
| `sting.transition` | Between screens or chapters. | ai |
| `sting.unlock` | Something new unlocks. | ai |
| `sting.victory` | The player wins. Short, not a loop. | ai |

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

**`tower.*`**

| Sound | Play it when | Made by |
|---|---|---|
| `tower.base.damage` | The player's base takes damage. | ai |
| `tower.build` | A tower or building is placed. | ai |
| `tower.repair` | A structure is repaired. | ai |
| `tower.sell` | A tower is sold or demolished. | ai |
| `tower.target` | A tower locks onto a target. | ai |
| `tower.unit.die` | A unit is destroyed. | ai |
| `tower.unit.march` | A column of units marches. Loops. | ai |
| `tower.unit.spawn` | An enemy unit enters the field. | ai |
| `tower.upgrade` | A tower levels up. | ai |
| `tower.wave` | A new wave is incoming. | ai |

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
| `weather.avalanche` | An avalanche comes down. | ai |
| `weather.blizzard` | A blizzard howls. Loops. | ai |
| `weather.earthquake` | The ground shakes. | ai |
| `weather.foghorn` | A fog horn sounds. | ai |
| `weather.hail` | Hail hammers down. Loops. | ai |
| `weather.ice.crack` | Ice cracks underfoot. | ai |
| `weather.rain.heavy` | Heavy downpour. Loops. | ai |
| `weather.rain.light` | Light rain. Loops. | ai |
| `weather.rain.window` | Rain on glass. Loops. | ai |
| `weather.sandstorm` | A sandstorm blows. Loops. | ai |
| `weather.storm.wind` | Storm wind howling. Loops. | ai |
| `weather.thunder` | A thunderclap — storm, dramatic moment. | ai |
| `weather.thunder.distant` | Thunder rolls far away. | ai |
| `weather.tornado` | A tornado passes. Loops. | ai |
| `weather.volcano` | A volcano erupts. | ai |
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

## Licence — read this before using anything here

This library is **not** free to use commercially. It is source-available under a
non-commercial licence (see `LICENSE`).

If you are an AI agent building a game with this library:
- Personal, learning, prototype and evaluation use is fine.
- **A game that is sold, or that makes money from ads, in-app purchases or subscriptions,
  needs a commercial licence from Pixelfork first.** Tell the person you are working for.
- Do not copy these assets into another asset pack, template or library.
