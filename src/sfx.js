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

  var VERSION = '0.1.0';
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
  var music = { name: null, src: null, gain: null };
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

    nodes.master = ctx.createGain();
    nodes.master.connect(ctx.destination);
    nodes.duck = ctx.createGain();          // music passes through this
    nodes.duck.connect(nodes.master);

    CATEGORIES.forEach(function (c) {
      nodes[c] = ctx.createGain();
      nodes[c].connect(c === 'music' ? nodes.duck : nodes.master);
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
        packs[manifest.name || pack] = { manifest: manifest, buffer: null };
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

  /* --------------------------------------------------------- synth backup */

  // Tiny stand-in sounds so the library is usable before real audio exists.
  // These are deliberately simple: they say "a coin was collected", not
  // "this is the final sound of the game".
  var SHAPES = {
    blip:  { wave: 'square',   f0: 880,  f1: 1320, dur: 0.07, gain: 0.30 },
    tap:   { wave: 'triangle', f0: 620,  f1: 520,  dur: 0.05, gain: 0.35 },
    chime: { wave: 'sine',     f0: 1046, f1: 1568, dur: 0.30, gain: 0.30, partials: [1, 2, 3] },
    thud:  { wave: 'sine',     f0: 180,  f1: 60,   dur: 0.18, gain: 0.45 },
    buzz:  { wave: 'sawtooth', f0: 220,  f1: 110,  dur: 0.22, gain: 0.25 },
    noise: { noise: true,      f0: 2200, f1: 400,  dur: 0.25, gain: 0.30, q: 1.2 },
    sweep: { noise: true,      f0: 400,  f1: 4200, dur: 0.30, gain: 0.22, q: 2.0 }
  };

  function noiseBuffer(c, seconds) {
    var len = Math.max(1, Math.floor(c.sampleRate * seconds));
    var buf = c.createBuffer(1, len, c.sampleRate);
    var d = buf.getChannelData(0);
    for (var i = 0; i < len; i++) d[i] = Math.random() * 2 - 1;
    return buf;
  }

  function synth(def, dest, when, rate, volume) {
    var c = ctx;
    var spec = Object.assign({}, SHAPES[def.shape] || SHAPES.blip, def.synth || {});
    var notes = spec.notes || def.notes;          // arpeggio, e.g. win fanfare
    var step = spec.step || 0.09;

    if (notes && notes.length) {
      notes.forEach(function (f, i) {
        voiceOne(c, spec, dest, when + i * step, f * rate, volume * (spec.gain || 0.3));
      });
      return;
    }
    voiceOne(c, spec, dest, when, null, volume * (spec.gain || 0.3), rate);
  }

  function voiceOne(c, spec, dest, when, fixedFreq, gain, rate) {
    rate = rate || 1;
    var dur = (spec.dur || 0.12) / rate;
    var env = c.createGain();
    env.connect(dest);
    env.gain.setValueAtTime(0, when);
    env.gain.linearRampToValueAtTime(gain, when + Math.min(0.012, dur * 0.2));
    env.gain.exponentialRampToValueAtTime(0.0001, when + dur);

    if (spec.noise) {
      var src = c.createBufferSource();
      src.buffer = noiseBuffer(c, dur);
      var f = c.createBiquadFilter();
      f.type = 'bandpass';
      f.Q.value = spec.q || 1;
      f.frequency.setValueAtTime(spec.f0 * rate, when);
      f.frequency.exponentialRampToValueAtTime(Math.max(40, spec.f1 * rate), when + dur);
      src.connect(f); f.connect(env);
      src.start(when); src.stop(when + dur + 0.02);
      track(src);
      return;
    }

    var partials = spec.partials || [1];
    partials.forEach(function (mult, i) {
      var o = c.createOscillator();
      o.type = spec.wave || 'square';
      var f0 = (fixedFreq || spec.f0) * rate * mult;
      var f1 = (fixedFreq ? fixedFreq * (spec.f1 / spec.f0) : spec.f1) * rate * mult;
      o.frequency.setValueAtTime(f0, when);
      o.frequency.exponentialRampToValueAtTime(Math.max(30, f1), when + dur);
      var pg = c.createGain();
      pg.gain.value = 1 / (i + 1);
      o.connect(pg); pg.connect(env);
      o.start(when); o.stop(when + dur + 0.02);
      track(o);
    });
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
      g.gain.value = volume;
      src.connect(g); g.connect(dest);
      src.start(when, slice[0], slice[1]);
      track(src);
      return src;
    }

    synth(def, dest, when, rate, volume);
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

  function playMusic(name, opts) {
    opts = opts || {};
    var c = ensureContext();
    if (!c) return;
    if (music.name === name) return;
    var fade = opts.fade != null ? opts.fade : 0.6;
    stopMusic(fade);
    if (!name) return;

    var def = sounds[name] || {};
    var url = def.file ? BASE + def.file : opts.url;
    if (!url) { music.name = name; return; }      // nothing to stream yet

    var el = new Audio(url);
    el.loop = opts.loop !== false;
    el.crossOrigin = 'anonymous';
    var src = c.createMediaElementSource(el);
    var g = c.createGain();
    g.gain.setValueAtTime(0, c.currentTime);
    g.gain.linearRampToValueAtTime(1, c.currentTime + fade);
    src.connect(g); g.connect(nodes.music);
    el.play().catch(function () { /* blocked until a gesture; unlock() retries */ });
    music = { name: name, src: el, gain: g };
  }

  function stopMusic(fade) {
    if (!music.src) { music.name = null; return; }
    var el = music.src, g = music.gain;
    fade = fade != null ? fade : 0.4;
    if (g && ctx) {
      g.gain.cancelScheduledValues(ctx.currentTime);
      g.gain.setValueAtTime(g.gain.value, ctx.currentTime);
      g.gain.linearRampToValueAtTime(0, ctx.currentTime + fade);
    }
    setTimeout(function () { try { el.pause(); } catch (e) {} }, fade * 1000 + 50);
    music = { name: null, src: null, gain: null };
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
      if (global.document.hidden) { if (music.src) music.src.pause(); ctx.suspend(); }
      else { ctx.resume(); if (music.src) music.src.play().catch(function () {}); }
    });
  }

  /* ------------------------------------------------------------ public API */

  var SFX = {
    version: VERSION,
    load: load,
    play: play,
    music: playMusic,
    stopMusic: stopMusic,
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
        master: ctx ? nodes.master : null,
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
