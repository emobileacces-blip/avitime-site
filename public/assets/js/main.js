/* Avitime — static site scripts: intro video, scroll film, scroll reveals. */
(() => {
  const $ = id => document.getElementById(id);
  const views = { home: { hidden: !document.getElementById('concept') } };
  /* ---------- Video ---------- */
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const reel = (() => {
    const v = $('reel'), b = $('reelBtn');
    if (!v) return { pause() {}, sync() {} };
    let userPaused = reduce;
    const ui = () => { const p = v.paused; $('icPause').hidden = p; $('icPlay').hidden = !p; b.setAttribute('aria-label', p ? 'Lire la vidéo' : 'Mettre la vidéo en pause'); };
    v.addEventListener('play', ui); v.addEventListener('pause', ui);
    const sb = $('soundBtn');
    sb.addEventListener('click', () => { v.muted = !v.muted; sb.setAttribute('aria-pressed', String(!v.muted)); sb.setAttribute('aria-label', v.muted ? 'Activer le son' : 'Couper le son'); $('icMuted').hidden = !v.muted; $('icSound').hidden = v.muted; if (!v.muted) { if (v.currentTime > 1) v.currentTime = 0; userPaused = false; v.play().catch(() => {}); } });
    b.addEventListener('click', () => { if (v.paused) { userPaused = false; v.play().catch(() => {}); } else { userPaused = true; v.pause(); } });
    const io = 'IntersectionObserver' in window ? new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting && !userPaused) v.play().catch(() => {}); else v.pause(); }), { threshold: .25 }) : null;
    if (io) io.observe(v);
    ui();
    return { pause() { v.pause(); }, sync() { if (!userPaused && !io) v.play().catch(() => {}); } };
  })();

  /* ---------- Film ---------- */
  const film = !document.getElementById('concept') ? { measure() {}, request() {} } : (() => {
    const NS = 'http://www.w3.org/2000/svg';
    const clamp = (x, a = 0, b = 1) => Math.min(b, Math.max(a, x));
    const ramp = (p, a, b) => clamp((p - a) / (b - a));
    const ease = t => t < .5 ? 4 * t * t * t : 1 - Math.pow(-2 * t + 2, 3) / 2;
    const E = (p, a, b) => ease(ramp(p, a, b));
    const lerp = (a, b, t) => a + (b - a) * t;
    const mk = (tag, attrs, parent) => { const el = document.createElementNS(NS, tag); for (const k in attrs) el.setAttribute(k, attrs[k]); if (parent) parent.appendChild(el); return el; };
    const op = (el, v) => { el.style.opacity = v.toFixed(3); };
    const tf = (el, x, y, s = 1) => el.setAttribute('transform', `translate(${x.toFixed(2)} ${y.toFixed(2)}) scale(${s.toFixed(3)})`);
    const filmEl = $('concept'), sticky = $('filmSticky'), stageWrap = $('filmStage'), svg = $('stage');

    const SEL = 15, ELIG = [1, 4, 8, 9, 13, 15, 18, 22, 24, 27];
    const testers = [];
    for (let i = 0; i < 30; i++) {
      const c = i % 6, r = Math.floor(i / 6), x = 590 + c * 58, y = 170 + r * 60;
      const t = { i, x, y, elig: ELIG.includes(i), el: null };
      if (i !== SEL) { const g = mk('g', { transform: `translate(${x} ${y})` }, $('testers')); mk('circle', { r: 20, class: 't-bg' }, g); mk('circle', { cy: -5, r: 6.5, class: 't-fg' }, g); mk('path', { d: 'M-11 13 a11 10 0 0 1 22 0 z', class: 't-fg' }, g); t.el = g; }
      testers.push(t);
    }
    const SELPOS = testers[SEL], elig = testers.filter(t => t.elig);
    const chips = [];
    [['Âge', 58], ['Pays', 62], ['Catégorie', 88], ['Anti-doublon', 104]].reduce((x, [label, w]) => {
      const g = mk('g', { opacity: 0 }, $('chips'));
      mk('rect', { x, y: 112, width: w, height: 26, rx: 13, class: 's-2' }, g);
      const u = mk('use', { href: '#check', x: x + 9, y: 118, width: 14, height: 14 }, g); u.style.color = 'var(--hl)';
      mk('text', { x: x + 27, y: 129, 'font-size': 11.5, class: 's-ink' }, g).textContent = label;
      chips.push(g); return x + w + 8;
    }, 575);
    const status = [];
    [['Commandé', 360], ['Expédié', 500], ['Livré', 640]].forEach(([label, cx]) => {
      const g = mk('g', {}, $('status'));
      mk('rect', { x: cx - 56, y: 504, width: 112, height: 32, rx: 16, class: 's-2' }, g);
      const on = mk('rect', { x: cx - 56, y: 504, width: 112, height: 32, rx: 16, class: 's-hl', opacity: 0 }, g);
      const t = mk('text', { x: cx, y: 525, 'text-anchor': 'middle', 'font-size': 13, 'font-weight': 500, class: 's-ink' }, g); t.textContent = label;
      status.push({ on, t });
    });
    const facts = [];
    ['Avis négatif ? Publié aussi.', 'Le produit reste au testeur.', 'L’IA reformule, sans inventer.'].forEach((label, i) => {
      const y = 190 + i * 66, g = mk('g', { opacity: 0 }, $('facts'));
      mk('rect', { x: 672, y, width: 262, height: 44, rx: 22, class: 's-2' }, g);
      mk('circle', { cx: 694, cy: y + 22, r: 10, class: 's-hl' }, g);
      const u = mk('use', { href: '#check', x: 688, y: y + 16, width: 12, height: 12 }, g); u.style.color = 'var(--stage)';
      mk('text', { x: 714, y: y + 27, 'font-size': 13.5, 'font-weight': 500, class: 's-ink' }, g).textContent = label;
      facts.push(g);
    });
    const route = $('route'), L = route.getTotalLength();
    route.style.strokeDasharray = `${L} ${L}`;
    const topStars = [...document.querySelectorAll('.topStar')], phStars = [...document.querySelectorAll('.phStar')];
    const caps = [...filmEl.querySelectorAll('.cap')], segs = [...filmEl.querySelectorAll('.seg')];
    const S = [0, .165, .335, .5, .665, .83, 1];
    const CAM_W = [[0,480,320,560,460],[.15,480,320,560,460],[.22,470,290,900,430],[.48,480,315,900,440],[.53,480,345,900,440],[.65,480,345,900,440],[.69,480,318,900,500],[.80,480,318,900,500],[.88,480,320,560,460],[1,480,320,560,460]];
    const CAM_N = [[0,480,320,520,440],[.15,480,320,520,440],[.22,735,282,380,420],[.32,735,282,380,420],[.37,560,315,560,340],[.49,560,315,560,340],[.53,520,350,440,420],[.65,520,350,440,420],[.69,515,318,250,480],[.80,515,318,250,480],[.88,480,320,520,440],[1,480,320,520,440]];
    const cam = (p, K) => { for (let i = 0; i < K.length - 1; i++) { const a = K[i], b = K[i + 1]; if (p <= b[0]) { const t = ease(ramp(p, a[0], b[0])); return a.slice(1).map((v, j) => lerp(v, b[j + 1], t)); } } return K[K.length - 1].slice(1); };
    let box = { w: 1, h: 1 };
    const measure = () => { box = { w: stageWrap.clientWidth || 1, h: stageWrap.clientHeight || 1 }; };
    const fmt = v => v.toFixed(2).replace('.', ',') + ' €';

    function render(p) {
      const narrow = box.w / box.h < 1.05;
      const tt = E(p, .53, .62), pt = route.getPointAtLength(L * tt);
      let [cx, cy, rw, rh] = cam(p, narrow ? CAM_N : CAM_W);
      if (narrow) { const f = E(p, .51, .54) * (1 - E(p, .64, .68)); cx = lerp(cx, clamp(pt.x, 300, 740), f); }
      const A = box.w / box.h; let w, h;
      if (rw / rh > A) { w = rw; h = rw / A; } else { h = rh; w = rh * A; }
      svg.setAttribute('viewBox', `${(cx - w / 2).toFixed(1)} ${(cy - h / 2).toFixed(1)} ${w.toFixed(1)} ${h.toFixed(1)}`);
      svg.setAttribute('preserveAspectRatio', 'xMidYMid slice');
      const glow = $('glow'); glow.setAttribute('cx', cx.toFixed(1)); glow.setAttribute('cy', cy.toFixed(1)); glow.setAttribute('r', (Math.max(w, h) * .55).toFixed(1));
      const k = E(p, .14, .22) * (1 - E(p, .80, .88));
      tf($('shop'), lerp(230, 40, k), lerp(110, 230, k), lerp(1, .42, k));
      op($('shop'), 1 - .6 * E(p, .64, .68) * (1 - E(p, .79, .83)));
      op($('shopLbl'), clamp(k * 1.4 - .4) * (1 - E(p, .63, .67)));
      const f = E(p, .86, .91);
      op($('revEmpty'), 1 - f); op($('revFull'), f); op($('noRev'), 1 - f); op($('oneRev'), f);
      topStars.forEach((s, i) => op(s, E(p, .88 + i * .012, .895 + i * .012)));
      op($('sel'), E(p, .16, .2) * (1 - E(p, .33, .37)));
      const sx = lerp(560, 920, ramp(p, .21, .27));
      $('scan').setAttribute('x1', sx); $('scan').setAttribute('x2', sx);
      op($('scan'), ramp(p, .205, .215) * (1 - ramp(p, .265, .275)));
      testers.forEach(t => { if (t.el) op(t.el, t.elig ? 1 : 1 - .82 * clamp((sx - t.x + 20) / 40)); });
      chips.forEach((c, i) => op(c, E(p, .21 + i * .014, .224 + i * .014)));
      const lt = ramp(p, .27, .315), ring = $('ring');
      if (lt <= 0) op(ring, 0); else { const tg = lt >= 1 ? SELPOS : elig[(Math.floor(lt * 16) * 7) % elig.length]; ring.setAttribute('cx', tg.x); ring.setAttribute('cy', tg.y); op(ring, lt >= 1 ? 0 : 1); }
      op($('drawLbl'), E(p, .27, .29));
      const m = E(p, .34, .39);
      tf($('me'), lerp(SELPOS.x, 800, m), lerp(SELPOS.y, 322, m), lerp(1, 1.5, m));
      op($('me'), E(p, .16, .2) * (1 - E(p, .66, .69)));
      op($('meRing'), E(p, .312, .322) * (1 - E(p, .5, .53)));
      const ci = E(p, .35, .39), co = E(p, .49, .52);
      op($('cart'), ci * (1 - co)); tf($('cart'), 320, 170 + 24 * (1 - ci)); op($('links'), ci * (1 - co));
      op($('discount'), E(p, .385, .4)); op($('shipPaid'), 1 - E(p, .4, .415)); op($('shipFree'), E(p, .4, .415));
      const tot = 29.8 * (1 - E(p, .385, .45)), totEl = $('total');
      totEl.textContent = fmt(tot); totEl.setAttribute('class', tot < .005 ? 'p-hl' : 'p-ink');
      op($('verified'), E(p, .45, .47));
      const dv = E(p, .5, .53) * (1 - E(p, .65, .68));
      op($('house'), dv); op($('routeG'), dv); op($('status'), dv);
      route.style.strokeDashoffset = (L * (1 - tt)).toFixed(1);
      tf($('parcel'), pt.x, pt.y, 1); op($('parcel'), E(p, .52, .535) * (1 - E(p, .615, .635)));
      [.535, .575, .62].forEach((th, i) => { const a = ramp(p, th, th + .01); op(status[i].on, a); status[i].t.setAttribute('class', a > .5 ? 's-dark' : 's-ink'); });
      op($('testLbl'), E(p, .62, .635) * (1 - E(p, .65, .68)));
      const pi = E(p, .66, .69), po = E(p, .8, .86);
      op($('phone'), pi * (1 - po));
      tf($('phone'), lerp(400, 440, po), lerp(80 + 30 * (1 - pi), 200, po), lerp(1, .6, po));
      phStars.forEach((s, i) => op(s, E(p, .69 + i * .01, .7 + i * .01)));
      op($('dur'), E(p, .71, .72));
      $('adv1').setAttribute('width', (170 * E(p, .72, .74)).toFixed(1));
      $('adv2').setAttribute('width', (120 * E(p, .735, .755)).toFixed(1));
      $('lim1').setAttribute('width', (140 * E(p, .75, .77)).toFixed(1));
      op($('pics'), E(p, .765, .775));
      const pb = E(p, .785, .795); op($('pubOn'), pb); $('pubTxt').setAttribute('class', pb > .5 ? 'p-ink' : 'p-on-btn');
      facts.forEach((g, i) => op(g, narrow ? 0 : E(p, .7 + i * .03, .72 + i * .03) * (1 - E(p, .8, .83))));
      caps.forEach((c, i) => {
        const a = i === 0 ? 1 : ramp(p, S[i] - .012, S[i] + .006);
        const b = i === caps.length - 1 ? 1 : 1 - ramp(p, S[i + 1] - .012, S[i + 1] + .006);
        const v = a * b;
        c.style.opacity = v.toFixed(3);
        c.style.transform = `translateY(${((1 - a) * 14 - (1 - b) * 14).toFixed(1)}px)`;
        c.setAttribute('aria-hidden', v < .5 ? 'true' : 'false');
      });
      segs.forEach((s, i) => { s.querySelector('b').style.width = (ramp(p, S[i], S[i + 1]) * 100).toFixed(1) + '%'; });
    }
    const progress = () => { const r = filmEl.getBoundingClientRect(); const total = filmEl.offsetHeight - sticky.offsetHeight; return total > 0 ? clamp(-r.top / total) : 0; };
    let ticking = false;
    const request = () => { if (views.home.hidden) return; if (!ticking) { ticking = true; requestAnimationFrame(() => { ticking = false; render(progress()); }); } };
    window.addEventListener('scroll', request, { passive: true });
    window.addEventListener('resize', () => { measure(); request(); });
    if ('ResizeObserver' in window) new ResizeObserver(() => { measure(); request(); }).observe(stageWrap);
    segs.forEach((s, i) => s.addEventListener('click', () => {
      const total = filmEl.offsetHeight - sticky.offsetHeight;
      const target = i === 0 ? 0 : (i === 5 ? .95 : (S[i] + S[i + 1]) / 2 + .03);
      window.scrollTo({ top: filmEl.getBoundingClientRect().top + window.scrollY + total * target, behavior: reduce ? 'auto' : 'smooth' });
    }));
    measure(); render(0);
    if (document.fonts && document.fonts.ready) document.fonts.ready.then(() => { measure(); request(); });
    return { measure, request };
  })();

  /* ---------- Scroll reveal ---------- */
  (() => {
    if (!('IntersectionObserver' in window)) return;
    const sel = '.sec .eyebrow, .sec-title, .sec-lede, .tile, .truth-card, .grade, .pact, .ticket, .checks li, .faq details, .form-card, .reel-frame, .reel-cap, .law-stat, .law-col, .law-pitch, .facts-box, .story > *, .method li, .nevers li, .org > *, .doc-links';
    const io = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.remove('pre'); io.unobserve(e.target); } }), { rootMargin: '0px 0px -8% 0px' });
    const arm = () => {
      document.querySelectorAll(sel).forEach(el => {
        if (el.dataset.reveal !== undefined) return;
        const view = el.closest('.view'); if (view && view.hidden) return;
        el.setAttribute('data-reveal', '');
        const sibs = [...el.parentElement.children].filter(c => c.matches(sel));
        el.style.setProperty('--i', Math.min(sibs.indexOf(el), 6));
        const r = el.getBoundingClientRect();
        if (r.top > window.innerHeight * 0.92) { el.classList.add('pre'); io.observe(el); }
      });
    };
    arm();
  })();

})();
