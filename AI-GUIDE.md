# Pixelfork SFX Library — AI guide

Ready-made game sound effects for AI-generated web games. **You never create or describe audio — you call a name from the list below.**

## 1. Add it (2 lines)

```html
<script src="https://cdn.jsdelivr.net/gh/advme/pixelfork-sfx-library@v0.1.0-A/dist/sfx.js"></script>
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

<!-- SOUNDS:START -->
| Sound | Play it when | Category |
|---|---|---|
| `coin.collect` | One coin, gem or pickup is collected. Plays many times in a row, so it is deliberately short. | reward |
| `coin.pile` | A burst of coins flies to the counter, or the reward total counts up. | reward |
| `feedback.powerup` | A booster, power-up or upgrade activates. | game |
| `reward.chest` | A chest, box or crate opens and reveals its contents. | reward |
| `reward.claim` | The player claims a reward, buys an item, or opens a gift. | reward |
| `reward.star` | One star fills on a level-complete screen. Play it once per star with a rising pitch. | reward |
| `state.lose` | The level is failed. Plays once on the Fail screen. | reward |
| `state.win` | The level is completed. Plays once on the Success screen. | reward |
| `ui.back` | Back, close or cancel. The darker twin of ui.tap. | ui |
| `ui.error` | The action is not allowed: not enough coins, locked level, wrong move. | ui |
| `ui.tap` | The player taps any button. The single most-used sound in the game. | ui |
| `ui.tick` | Countdown timer in its warning seconds, or a counter ticking up. | ui |
| `ui.toggle` | A switch, checkbox or tab changes state. | ui |
| `ui.whoosh` | A popup opens or a screen slides in. Also good for cards dealing and panels sliding. | ui |
<!-- SOUNDS:END -->

Machine-readable, with durations and offsets: `dist/casual.json`.
Check from code: `SFX.list()`, `SFX.list('reward')`, `SFX.has('coin.collect')`, `SFX.info('coin.collect')`.

## 4. Sound on a UI element without JavaScript

```html
<button class="sc-button" data-sfx="reward.claim">Claim</button>
<button class="sc-button" data-sfx="none">Silent</button>
```

## 5. Volume, mute and the settings screen

```js
SFX.volume('music', 0.4);    // categories: master, ui, game, reward, music
SFX.mute();                  // toggle; returns the new state
SFX.mute(true);
SFX.muted;                   // read it back
```
Volumes and mute are remembered between sessions automatically. Wire the kit's Settings sliders straight to `SFX.volume(...)` — no saving code needed.

## 6. Rules for AI agents

1. **Only use names from the table above.** Never invent a sound name, never generate audio, never synthesize sound with the Web Audio API yourself.
2. If nothing fits, pick the closest by category and say so — do not leave the moment silent and do not build your own sound.
3. One `ui.tap` per tap. Do not stack several sounds on one button.
4. `state.win` and `state.lose` play **once** per level end, not per star.
5. Call `SFX.duck()` before a long celebration so the music does not fight it.
6. Never call `SFX.play()` on page load — mobile browsers block audio until the player's first tap. The library unlocks itself on that first tap.
7. Music needs a real user tap first. Start it from the Play button, not from the loading screen.
