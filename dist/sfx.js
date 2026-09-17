/*!
 * Pixelfork SFX Library — runtime
 * One line to load a pack, one line to play a sound.
 *
 *   <script src=".../dist/sfx.js"></script>
 *   <script>SFX.load('casual'); SFX.attach();</script>
 *   SFX.play('coin.collect');
 *
 * Handles everything mobile web audio gets wrong: iOS unlock, autoplay policy,
 * voice pooling, pitch variation, per-category volume, mute memory, music
 * ducking and tab-hidden pausing.
 *
 * Until a real audio pack is built, every sound falls back to a built-in
 * synthesized stand-in, so a game is never silent and never errors.
 */
(function (global) {
  'use strict';

  var VERSION = '0.6.0';
  var STORE_KEY = 'pixelfork.sfx';
  var CATEGORIES = ['ui', 'game', 'reward', 'music'];
  var MAX_VOICES = 24;          // hard cap on simultaneous one-shots
  var DEFAULT_MIN_GAP = 25;     // ms between two plays of the same name

  /* ---------------------------------------------------------------- state */

  var ctx = null;               // AudioContext (created on demand)
  var nodes = {};               // master + per-category GainNodes
  var packs = {};               // name -> { manifest, buffer }
  var sounds = {};              // "ui.tap" -> definition (merged from packs)
  var voices = [];              // live one-shot sources
  var lastPlay = {};            // name -> timestamp, for throttling
  var lastVariant = {};         // name -> last variation index used
  var music = { name: null, src: null, gain: null, token: 0 };
  var unlocked = false;
  var attached = false;
  var readyResolve;
  var readyPromise = new Promise(function (r) { readyResolve = r; });

  var settings = {
    master: 1, ui: 1, game: 1, reward: 1, music: 0.6, muted: false
  };

  /* ------------------------------------------------------------- settings */

  function loadSettings() {
    try {
      var raw = global.localStorage && global.localStorage.getItem(STORE_KEY);
      if (raw) {
        var saved = JSON.parse(raw);
        for (var k in saved) if (k in settings) settings[k] = saved[k];
      }
    } catch (e) { /* private mode / blocked storage: keep defaults */ }
  }

  function saveSettings() {
    try {
      global.localStorage && global.localStorage.setItem(STORE_KEY, JSON.stringify(settings));
    } catch (e) { /* ignore */ }
  }

  function applyGains() {
    if (!ctx) return;
    var m = settings.muted ? 0 : settings.master;
    nodes.master.gain.setTargetAtTime(m, ctx.currentTime, 0.01);
    CATEGORIES.forEach(function (c) {
      nodes[c].gain.setTargetAtTime(settings[c], ctx.currentTime, 0.01);
    });
  }

  /* ---------------------------------------------------------------- audio */

  function ensureContext() {
    if (ctx) return ctx;
    var AC = global.AudioContext || global.webkitAudioContext;
    if (!AC) return null;
    ctx = new AC();

    // ---- master bus --------------------------------------------------------
    // Only a soft limiter here, to round off transient edges. Tone shaping is
    // NOT global: see the per-category tone chain below.
    nodes.master = ctx.createGain();

    var limiter = ctx.createDynamicsCompressor();
    limiter.threshold.value = -10;
    limiter.knee.value = 8;
    limiter.ratio.value = 10;
    limiter.attack.value = 0.004;
    limiter.release.value = 0.12;

    nodes.master.connect(limiter);
    limiter.connect(ctx.destination);
    nodes.out = limiter;                    // what the speaker actually gets

    nodes.duck = ctx.createGain();          // music passes through this
    nodes.duck.connect(nodes.master);

    CATEGORIES.forEach(function (c) {
      nodes[c] = ctx.createGain();
      nodes[c].connect(c === 'music' ? nodes.duck : nodes.master);

      // Raw synthesis is too bright for a phone speaker, so synthesized sounds
      // get a high-shelf cut and a lowpass. Recorded audio is already mastered
      // and must NOT pass through this — doing so costs it about a quarter of
      // its high end and makes it sound dull and far away.
      var shelf = ctx.createBiquadFilter();
      shelf.type = 'highshelf';
      shelf.frequency.value = 4200;
      shelf.gain.value = -5.5;

      var air = ctx.createBiquadFilter();
      air.type = 'lowpass';
      air.frequency.value = 12000;
      air.Q.value = 0.7;

      shelf.connect(air);
      air.connect(nodes[c]);
      nodes['tone:' + c] = shelf;           // synthesized sounds enter here
    });

    applyGains();
    return ctx;
  }

  // iOS/Android start the context suspended. Resume it on the first real gesture.
  function unlock() {
    var c = ensureContext();
    if (!c) return;
    if (c.state === 'suspended') c.resume();
    if (unlocked) return;
    unlocked = true;
    // A one-sample silent buffer satisfies older iOS, which only trusts a
    // buffer that actually started inside the gesture.
    try {
      var s = c.createBufferSource();
      s.buffer = c.createBuffer(1, 1, 22050);
      s.connect(c.destination);
      s.start(0);
    } catch (e) { /* ignore */ }
    emit('unlock');
  }

  function installUnlockHooks() {
    var evs = ['pointerdown', 'touchend', 'mousedown', 'keydown'];
    function go() {
      unlock();
      evs.forEach(function (e) { global.removeEventListener(e, go, true); });
    }
    evs.forEach(function (e) { global.addEventListener(e, go, true); });
  }

  /* ------------------------------------------------------------ pack load */

  function pickFormat(sprite) {
    var probe = global.document && global.document.createElement('audio');
    if (probe && sprite.webm && probe.canPlayType('audio/webm; codecs=opus')) return sprite.webm;
    if (probe && sprite.m4a && probe.canPlayType('audio/mp4; codecs="mp4a.40.2"')) return sprite.m4a;
    return sprite.m4a || sprite.mp3 || sprite.webm;
  }

  function baseUrl() {
    // Resolve pack files relative to this script, so the CDN tag stays in one place.
    var s = global.document && global.document.currentScript;
    if (!s) {
      var all = global.document ? global.document.getElementsByTagName('script') : [];
      for (var i = all.length - 1; i >= 0; i--) {
        if (/sfx(\.min)?\.js(\?|$)/.test(all[i].src || '')) { s = all[i]; break; }
      }
    }
    return s && s.src ? s.src.replace(/\/[^\/]*$/, '/') : '';
  }

  var BASE = '';

  function load(pack, opts) {
    opts = opts || {};
    var url = opts.url || (BASE + pack + '.json');

    return fetch(url)
      .then(function (r) {
        if (!r.ok) throw new Error('SFX: pack manifest ' + url + ' → ' + r.status);
        return r.json();
      })
      .then(function (manifest) {
        registerSounds(manifest);
        packs[manifest.name || pack] = {
          manifest: manifest,
          buffer: null,
          trim: manifest.spriteTrim != null ? manifest.spriteTrim : 0.55
        };
        if (!manifest.sprite) return null;          // names only, synth fallback
        var file = BASE + pickFormat(manifest.sprite);
        return fetch(file)
          .then(function (r) { return r.arrayBuffer(); })
          .then(function (data) {
            var c = ensureContext();
            if (!c) return null;
            return c.decodeAudioData(data);
          })
          .then(function (buf) { packs[manifest.name || pack].buffer = buf; return buf; });
      })
      .then(function () { readyResolve(SFX); return SFX; })
      .catch(function (err) {
        // A missing pack must never break a game — fall back to synth.
        if (global.console) console.warn('[SFX] pack "' + pack + '" not loaded, using built-in fallback sounds.', err.message);
        readyResolve(SFX);
        return SFX;
      });
  }

  function registerSounds(manifest) {
    var list = manifest.sounds || {};
    for (var name in list) {
      var def = list[name];
      def._pack = manifest.name;
      sounds[name] = def;
    }
  }

  /* -------------------------------------------------------- synth engine */

  // Some sounds in this library are MEANT to be code, permanently: lasers, UI
  // blips, coin chimes, whooshes, energy hums, jumps, pitch ladders. They are
  // synthetic by nature, so code beats a recording — infinite variation,
  // perfect pitch control, zero download. Sounds with real-world texture
  // (footsteps, guns, glass, voices, instruments) are generated as audio
  // instead. Which is which is declared in registry.json → "source".
  //
  // A recipe is a stack of layers. Each layer is one of:
  //   osc   { wave, f0, f1, dur, gain, at, curve, partials, vib }
  //   noise { f0, f1, dur, gain, at, curve, filter: lowpass|bandpass|highpass, q }
  //   fm    { f0, f1, ratio, index, index1, dur, gain, at }   ← bells, coins, metal
  // "at" delays a layer, so you can put a click transient in front of a body.

  var NOISE = null;

  function noiseBuf(c) {
    if (NOISE) return NOISE;
    var len = Math.floor(c.sampleRate * 2);
    NOISE = c.createBuffer(1, len, c.sampleRate);
    var d = NOISE.getChannelData(0);
    for (var i = 0; i < len; i++) d[i] = Math.random() * 2 - 1;
    return NOISE;
  }

  function envelope(c, when, dur, peak, attack, hold) {
    attack = attack == null ? 0.009 : attack;
    hold = hold || 0;
    peak = Math.max(0.0001, peak);
    if (attack + hold > dur * 0.9) { attack = dur * 0.1; hold = 0; }
    var g = c.createGain();
    g.gain.setValueAtTime(0.0001, when);
    g.gain.exponentialRampToValueAtTime(peak, when + attack);
    if (hold) g.gain.setValueAtTime(peak, when + attack + hold);
    g.gain.exponentialRampToValueAtTime(0.0001, when + dur);
    return g;
  }

  function ramp(param, v0, v1, when, dur, curve) {
    param.setValueAtTime(v0, when);
    if (v1 == null || v1 === v0) return;
    if (curve === 'lin') param.linearRampToValueAtTime(v1, when + dur);
    else param.exponentialRampToValueAtTime(Math.max(1, v1), when + dur);
  }

  function layerOsc(c, L, dest, when, rate, vol, note) {
    var dur = (L.dur || 0.15) / rate;
    var base = L.f0 || 440;
    var f0 = (note || base) * rate;
    var f1 = L.f1 != null ? (note ? note * (L.f1 / base) : L.f1) * rate : null;
    var env = envelope(c, when, dur, vol * (L.gain == null ? 1 : L.gain), L.attack, L.hold);
    env.connect(dest);

    (L.partials || [1]).forEach(function (mult, i) {
      var o = c.createOscillator();
      o.type = L.wave || 'sine';
      ramp(o.frequency, f0 * mult, f1 != null ? f1 * mult : null, when, dur, L.curve);
      var pg = c.createGain();
      pg.gain.value = (L.partialGains && L.partialGains[i] != null) ? L.partialGains[i] : 1 / (i + 1);
      o.connect(pg); pg.connect(env);
      if (L.vib) {
        var lfo = c.createOscillator(), lg = c.createGain();
        lfo.frequency.value = L.vib.rate || 6;
        lg.gain.value = L.vib.depth || 10;
        lfo.connect(lg); lg.connect(o.frequency);
        lfo.start(when); lfo.stop(when + dur + 0.02);
      }
      o.start(when); o.stop(when + dur + 0.02);
      track(o);
    });
  }

  function layerNoise(c, L, dest, when, rate, vol) {
    var dur = (L.dur || 0.2) / rate;
    var src = c.createBufferSource();
    src.buffer = noiseBuf(c);
    src.loop = true;
    var f = c.createBiquadFilter();
    f.type = L.filter || 'bandpass';
    f.Q.value = L.q || 1;
    ramp(f.frequency, (L.f0 || 1000) * rate, L.f1 != null ? L.f1 * rate : null, when, dur, L.curve);
    var env = envelope(c, when, dur, vol * (L.gain == null ? 1 : L.gain), L.attack, L.hold);
    src.connect(f); f.connect(env); env.connect(dest);
    src.start(when, Math.random() * 1.5);   // random offset = a different grain every time
    src.stop(when + dur + 0.02);
    track(src);
  }

  // Frequency modulation: the cheapest way to get a convincing bell, coin,
  // metal clank or laser out of two oscillators.
  function layerFM(c, L, dest, when, rate, vol, note) {
    var dur = (L.dur || 0.3) / rate;
    var carrier = (note || L.f0 || 660) * rate;
    var o = c.createOscillator();
    o.type = L.wave || 'sine';
    ramp(o.frequency, carrier, L.f1 != null ? L.f1 * rate : null, when, dur, L.curve);

    var m = c.createOscillator();
    m.type = 'sine';
    m.frequency.value = carrier * (L.ratio || 2);
    var mg = c.createGain();
    var i0 = L.index == null ? 200 : L.index;
    mg.gain.setValueAtTime(Math.max(0.01, i0), when);
    mg.gain.exponentialRampToValueAtTime(Math.max(0.01, L.index1 == null ? 0.01 : L.index1), when + dur);
    m.connect(mg); mg.connect(o.frequency);

    var env = envelope(c, when, dur, vol * (L.gain == null ? 1 : L.gain), L.attack, L.hold);
    o.connect(env); env.connect(dest);
    o.start(when); o.stop(when + dur + 0.02);
    m.start(when); m.stop(when + dur + 0.02);
    track(o); track(m);
  }

  var LAYER = { osc: layerOsc, noise: layerNoise, fm: layerFM };

  // Presets, so a simple sound can say shape:"tap" instead of a layer stack.
  var SHAPES = {
    blip:  { layers: [{ type: 'osc', wave: 'square', f0: 880, f1: 1320, dur: 0.07, gain: 0.3 }] },
    tap:   { layers: [
              { type: 'osc', wave: 'triangle', f0: 620, f1: 520, dur: 0.05, gain: 0.35 },
              { type: 'noise', filter: 'highpass', f0: 3200, f1: 2200, dur: 0.02, gain: 0.12 }] },
    chime: { layers: [{ type: 'fm', f0: 1046, ratio: 3.5, index: 600, dur: 0.3, gain: 0.3 }] },
    thud:  { layers: [{ type: 'osc', wave: 'sine', f0: 180, f1: 55, dur: 0.18, gain: 0.5 }] },
    buzz:  { layers: [{ type: 'osc', wave: 'sawtooth', f0: 220, f1: 110, dur: 0.22, gain: 0.25 }] },
    noise: { layers: [{ type: 'noise', filter: 'bandpass', f0: 2200, f1: 400, dur: 0.25, gain: 0.3, q: 1.2 }] },
    sweep: { layers: [{ type: 'noise', filter: 'bandpass', f0: 400, f1: 4200, dur: 0.3, gain: 0.22, q: 2 }] }
  };

  // An "ai" sound with no audio file yet has no recipe of its own. Give it a
  // plausible stand-in for its category rather than a generic blip.
  var DEFAULT_SHAPE = { ui: 'tap', game: 'thud', reward: 'chime', music: 'sweep' };

  function synth(def, dest, when, rate, volume) {
    var c = ctx;
    var recipe = def.synth || SHAPES[def.shape] || SHAPES[DEFAULT_SHAPE[def.category] || 'blip'];
    var layers = recipe.layers || [recipe];
    var notes = recipe.notes || def.notes;
    var step = recipe.step || 0.09;
    var gain = volume * (recipe.gain == null ? 1 : recipe.gain);

    function stack(at, note) {
      layers.forEach(function (L) {
        var fn = LAYER[L.type || 'osc'];
        if (fn) fn(c, L, dest, at + (L.at || 0) / rate, rate, gain, note);
      });
    }

    if (notes && notes.length) {
      notes.forEach(function (n, i) { stack(when + i * step / rate, n); });
    } else {
      stack(when, null);
    }
  }

  function track(src) {
    voices.push(src);
    src.onended = function () {
      var i = voices.indexOf(src);
      if (i >= 0) voices.splice(i, 1);
    };
    if (voices.length > MAX_VOICES) {
      var old = voices.shift();
      try { old.stop(); } catch (e) { /* already stopped */ }
    }
  }

  /* ----------------------------------------------------------------- play */

  function play(name, opts) {
    opts = opts || {};
    var c = ensureContext();
    if (!c) return null;
    if (c.state === 'suspended') c.resume();

    var def = sounds[name];
    if (!def) {
      if (global.console && !play._warned[name]) {
        play._warned[name] = true;
        console.warn('[SFX] unknown sound "' + name + '". See SFX.list().');
      }
      def = { shape: 'blip', category: 'ui' };
    }

    // Throttle machine-gunning of the same sound (sounds like distortion).
    var now = performance.now();
    var gap = def.minGap != null ? def.minGap : DEFAULT_MIN_GAP;
    if (lastPlay[name] && now - lastPlay[name] < gap) return null;
    lastPlay[name] = now;

    var cat = def.category || 'ui';
    var dest = nodes[cat] || nodes.ui;
    var when = c.currentTime + (opts.delay || 0);

    // Small random pitch shift so repeats never sound identical.
    var vary = def.vary != null ? def.vary : 0.04;
    var rate = (def.rate || 1) * (opts.rate || 1) * (1 + (Math.random() - 0.5) * 2 * vary);
    var volume = (def.gain != null ? def.gain : 1) * (opts.volume != null ? opts.volume : 1);

    var pack = packs[def._pack];
    var buffer = pack && pack.buffer;

    if (buffer && def.start != null) {
      var slice = pickSlice(name, def);
      var src = c.createBufferSource();
      src.buffer = buffer;
      src.playbackRate.value = rate;
      var g = c.createGain();
      g.gain.value = volume * (pack.trim == null ? 0.55 : pack.trim);
      src.connect(g); g.connect(dest);
      if (opts.loop) {
        // Loop inside the sprite: the slice repeats, nothing after it is heard.
        src.loop = true;
        src.loopStart = slice[0];
        src.loopEnd = slice[0] + slice[1];
        src.start(when, slice[0]);
      } else {
        src.start(when, slice[0], slice[1]);
      }
      track(src);
      return src;
    }

    // Synthesized sounds go through the tone chain; recordings go in clean.
    synth(def, nodes['tone:' + cat] || dest, when, rate, volume);
    return null;
  }
  play._warned = {};

  // Pick one of a sound's recorded variations, never the same one twice.
  function pickSlice(name, def) {
    if (!def.variations || !def.variations.length) return [def.start, def.dur];
    var n = def.variations.length, i = Math.floor(Math.random() * n);
    if (n > 1 && i === lastVariant[name]) i = (i + 1) % n;
    lastVariant[name] = i;
    return def.variations[i];
  }

  /* ---------------------------------------------------------------- music */

  var musicCache = {};          // name -> decoded AudioBuffer

  function musicUrl(def, opts) {
    if (opts && opts.url) return opts.url;
    if (def.files) return BASE + pickFormat(def.files);
    if (def.file) return BASE + def.file;
    return null;
  }

  // Music loops with an AudioBufferSourceNode, not <audio loop>. An audio
  // element inserts a small gap every time it wraps, which would undo the
  // crossfade the track was built with. A buffer source loops sample-exactly.
  function playMusic(name, opts) {
    opts = opts || {};
    var c = ensureContext();
    if (!c) return;
    if (music.name === name && music.src) return;

    var fade = opts.fade != null ? opts.fade : 0.8;
    stopMusic(fade);
    if (!name) return;

    var def = sounds[name] || {};
    var url = musicUrl(def, opts);
    if (!url) { music.name = name; return; }   // no track file yet: stay silent

    music.name = name;
    var token = ++music.token;

    function start(buffer) {
      if (token !== music.token) return;       // a newer call won the race
      var src = c.createBufferSource();
      src.buffer = buffer;
      src.loop = opts.loop !== false;
      var g = c.createGain();
      g.gain.setValueAtTime(0.0001, c.currentTime);
      g.gain.linearRampToValueAtTime(1, c.currentTime + fade);
      src.connect(g); g.connect(nodes.music);
      src.start(0);
      music.src = src;
      music.gain = g;
      emit('music', { name: name });
    }

    if (musicCache[name]) { start(musicCache[name]); return; }

    fetch(url)
      .then(function (r) {
        if (!r.ok) throw new Error(url + ' -> ' + r.status);
        return r.arrayBuffer();
      })
      .then(function (data) { return c.decodeAudioData(data); })
      .then(function (buf) { musicCache[name] = buf; start(buf); })
      .catch(function (err) {
        if (global.console) console.warn('[SFX] music "' + name + '" could not load.', err.message);
      });
  }

  function stopMusic(fade) {
    music.token++;
    if (!music.src) { music.name = null; return; }
    var src = music.src, g = music.gain;
    fade = fade != null ? fade : 0.5;
    if (g && ctx) {
      var t = ctx.currentTime;
      g.gain.cancelScheduledValues(t);
      g.gain.setValueAtTime(Math.max(0.0001, g.gain.value), t);
      g.gain.exponentialRampToValueAtTime(0.0001, t + fade);
    }
    try { src.stop(ctx.currentTime + fade + 0.05); } catch (e) { /* already stopped */ }
    music = { name: null, src: null, gain: null, token: music.token };
  }

  // Dip the music so a big moment (win, reward) cuts through.
  function duck(amount, ms) {
    if (!ctx) return;
    amount = amount != null ? amount : 0.3;
    ms = ms != null ? ms : 900;
    var t = ctx.currentTime;
    nodes.duck.gain.cancelScheduledValues(t);
    nodes.duck.gain.setValueAtTime(nodes.duck.gain.value, t);
    nodes.duck.gain.linearRampToValueAtTime(amount, t + 0.08);
    nodes.duck.gain.linearRampToValueAtTime(1, t + 0.08 + ms / 1000);
  }

  /* --------------------------------------------- auto-wiring the UI kit */

  // Default sound for each Super Casual component/event, so a game that uses
  // the UI kit gets a fully sounding interface with one call: SFX.attach().
  var KIT_MAP = [
    ['.sc-button',      'ui.tap'],
    ['.sc-icon-button', 'ui.tap'],
    ['.sc-tabbar button', 'ui.tap'],
    ['.sc-tabs button', 'ui.tap'],
    ['.sc-shopcard',    'ui.tap'],
    ['.sc-row',         'ui.tap'],
    ['.sc-checkbox',    'ui.toggle'],
    ['.sc-toggle',      'ui.toggle']
  ];

  function soundFor(el) {
    var node = el.closest ? el.closest('[data-sfx]') : null;
    if (node) return node.getAttribute('data-sfx');           // explicit wins
    for (var i = 0; i < KIT_MAP.length; i++) {
      if (el.closest && el.closest(KIT_MAP[i][0])) return KIT_MAP[i][1];
    }
    return null;
  }

  function attach(root) {
    if (attached) return SFX;
    attached = true;
    root = root || global.document;

    root.addEventListener('pointerdown', function (e) {
      var t = e.target;
      if (!t || !t.closest) return;
      var name = soundFor(t);
      if (name && name !== 'none') play(name);
    }, true);

    // Kit events. Capture phase catches these even though they do not bubble.
    var EVENT_MAP = {
      open:  'ui.whoosh',   // popup opened
      close: 'ui.back',     // popup closed
      buy:   'reward.claim'
      // 'star' is handled separately below so each star rises in pitch.
    };
    Object.keys(EVENT_MAP).forEach(function (type) {
      root.addEventListener(type, function (e) {
        var el = e.target;
        if (el && el.getAttribute && el.getAttribute('data-sfx') === 'none') return;
        play(EVENT_MAP[type]);
      }, true);
    });

    // Rising pitch ladder as stars fill — the classic casual "juice" moment.
    // The kit sends detail.index (0-based). Older or custom emitters may send
    // nothing at all, so fall back to counting events per element.
    var starCount = new WeakMap();
    root.addEventListener('star', function (e) {
      var el = e.target;
      if (el && el.getAttribute && el.getAttribute('data-sfx') === 'none') return;

      var i = e.detail && typeof e.detail.index === 'number' ? e.detail.index : null;
      if (i === null) {
        var seen = starCount.get(el) || { n: 0, t: 0 };
        if (performance.now() - seen.t > 1500) seen.n = 0;   // a new run of stars
        i = seen.n++;
        seen.t = performance.now();
        starCount.set(el, seen);
      }
      // Each star is one semitone-ish higher than the last.
      play('reward.star', { rate: Math.pow(1.122, Math.min(i, 5)) });
    }, true);

    // SC.toast has no DOM hook, so wrap it.
    if (global.SC && typeof global.SC.toast === 'function' && !global.SC.toast._sfx) {
      var original = global.SC.toast;
      var wrapped = function (text, o) {
        var kind = (o && o.kind) || 'info';
        play(kind === 'error' ? 'ui.error' : 'ui.tap');
        return original.apply(this, arguments);
      };
      wrapped._sfx = true;
      global.SC.toast = wrapped;
    }
    return SFX;
  }

  /* --------------------------------------------------------------- events */

  var listeners = {};
  function on(type, fn) { (listeners[type] = listeners[type] || []).push(fn); return SFX; }
  function emit(type, data) { (listeners[type] || []).forEach(function (f) { f(data); }); }

  /* ------------------------------------------------------- tab visibility */

  if (global.document) {
    global.document.addEventListener('visibilitychange', function () {
      if (!ctx) return;
      if (global.document.hidden) { ctx.suspend(); }
      else { ctx.resume(); }
    });
  }

  /* ------------------------------------------------------------ public API */

  var SFX = {
    version: VERSION,
    load: load,
    play: play,
    music: playMusic,
    stopMusic: stopMusic,
    // Stop one looping/long sound started by play(). Returns true if it stopped.
    stop: function (handle, fade) {
      if (!handle || !ctx) return false;
      try {
        if (fade) {
          var g = ctx.createGain();
          handle.stop(ctx.currentTime + fade);
        } else {
          handle.stop();
        }
        return true;
      } catch (e) { return false; }
    },
    duck: duck,
    attach: attach,
    unlock: unlock,
    on: on,
    ready: readyPromise,

    volume: function (category, value) {
      if (value === undefined) return settings[category];
      settings[category] = Math.max(0, Math.min(1, value));
      applyGains(); saveSettings();
      return SFX;
    },
    mute: function (on) {
      settings.muted = on === undefined ? !settings.muted : !!on;
      applyGains(); saveSettings();
      return settings.muted;
    },
    get muted() { return settings.muted; },
    settings: function () { return Object.assign({}, settings); },

    list: function (category) {
      return Object.keys(sounds).filter(function (n) {
        return !category || (sounds[n].category || 'ui') === category;
      }).sort();
    },
    info: function (name) { return sounds[name] || null; },
    has: function (name) { return !!sounds[name]; },

    // Register sounds without a pack file (tests, local packs).
    define: function (manifest) { registerSounds(manifest); packs[manifest.name] = { manifest: manifest, buffer: null }; return SFX; },

    // Internals, for the test pages only. Not part of the game-facing API.
    debug: function () {
      return {
        context: ctx,
        master: ctx ? nodes.out : null,
        duckGain: ctx ? nodes.duck.gain.value : null,
        preTone: ctx ? nodes.master : null,
        state: ctx ? ctx.state : 'none',
        voices: voices.length,
        unlocked: unlocked,
        packs: Object.keys(packs).map(function (p) {
          return { name: p, hasBuffer: !!packs[p].buffer };
        })
      };
    }
  };

  loadSettings();
  installUnlockHooks();
  BASE = baseUrl();

  global.SFX = SFX;
  if (typeof module !== 'undefined' && module.exports) module.exports = SFX;
})(typeof window !== 'undefined' ? window : this);
