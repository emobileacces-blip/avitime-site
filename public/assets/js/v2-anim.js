/* Avitime v2 : animations de l'accueil, de /tarifs et de la page « Pourquoi faire tester ».
   Tout le texte est dans le HTML et reste visible sans JavaScript ou en mouvement réduit :
   ce script ne masque un élément que juste avant de l'animer. */
(function () {
  if (!window.gsap || !window.ScrollTrigger) return;
  if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
  gsap.registerPlugin(ScrollTrigger);
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* Déclenche une action dès qu'un élément atteint le bas de l'écran ou l'a dépassé, même après un saut
     direct (ancre, touche Fin) : aucun élément ne peut rester caché. */
  var attentes = [];
  var prevu = false;
  function verifier() {
    prevu = false;
    var limite = window.innerHeight * 0.92;
    var prets = [];
    attentes = attentes.filter(function (a) {
      if (a.el.getBoundingClientRect().top < limite) { prets.push(a); return false; }
      return true;
    });
    var blocsPrets = prets.filter(function (a) { return a.bloc; }).map(function (a) { return a.el; });
    if (blocsPrets.length) {
      gsap.to(blocsPrets, { opacity: 1, y: 0, duration: 0.5, stagger: Math.min(0.07, 0.5 / blocsPrets.length), ease: 'power2.out', clearProps: 'transform,opacity' });
    }
    prets.forEach(function (a) { if (a.fn) a.fn(); });
  }
  function planifier() { if (!prevu) { prevu = true; requestAnimationFrame(verifier); } }
  window.addEventListener('scroll', planifier, { passive: true });
  window.addEventListener('resize', planifier);
  function quandVisible(el, fn) { attentes.push({ el: el, fn: fn }); }

  /* Barre de progression de lecture */
  var bar = document.createElement('div');
  bar.className = 'v2-progress';
  bar.setAttribute('aria-hidden', 'true');
  document.body.appendChild(bar);
  gsap.to(bar, { scaleX: 1, ease: 'none', scrollTrigger: { start: 0, end: 'max', scrub: 0.2 } });

  /* Garanties : bandeau défilant, avec un bouton pause */
  var proof = document.querySelector('.v2-proof');
  if (proof) {
    var ul = proof.querySelector('ul');
    var wrap = document.createElement('div');
    wrap.className = 'v2-marq';
    var track = document.createElement('div');
    track.className = 'v2-marq-track';
    track.appendChild(ul);
    for (var c = 0; c < 3; c++) {
      var copie = ul.cloneNode(true);
      copie.setAttribute('aria-hidden', 'true');
      track.appendChild(copie);
    }
    wrap.appendChild(track);
    var pause = document.createElement('button');
    pause.type = 'button';
    pause.className = 'v2-marq-btn';
    pause.textContent = 'Pause';
    pause.setAttribute('aria-pressed', 'false');
    pause.addEventListener('click', function () {
      var arret = proof.classList.toggle('is-paused');
      pause.textContent = arret ? 'Lecture' : 'Pause';
      pause.setAttribute('aria-pressed', arret ? 'true' : 'false');
    });
    proof.textContent = '';
    proof.appendChild(wrap);
    proof.appendChild(pause);
    proof.classList.add('is-marq');
    track.style.setProperty('--d', Math.max(24, ul.offsetWidth / 45) + 's');
  }

  /* Apparition douce à l'arrivée dans l'écran. Opacité seule, pour laisser le clavier accéder aux éléments. */
  var blocs = $$(['main .v2-band .v2-h2', 'main .v2-band > .v2-w > .v2-lead', '.v2-compare > .v2-fiche', '.v2-gains > article',
    '.v2-merchant > li', '.v2-shots > figure', '.v2-steps > li', '.v2-shot > *', '.v2-law-grid > div', '.v2-price-table',
    '.v2-grid3 > article', '.v2-method > li', '.tt-step', '.v2-nevers > li', '.v2-figs > div', '.v2-person', '.v2-grid4 > article', '.v2-duo > *', '.v2-plat > li', '.v2-faq > details'].join(','));
  gsap.set(blocs, { opacity: 0, y: 16 });
  blocs.forEach(function (el) { attentes.push({ el: el, bloc: true }); });

  /* Étoiles : elles se remplissent une à une */
  $$('main .v2-stars').forEach(function (el) {
    var texte = el.textContent;
    el.textContent = '';
    var etoiles = texte.split('').map(function (ch) {
      var s = document.createElement('span');
      s.className = 'v2-star';
      s.textContent = ch;
      el.appendChild(s);
      return s;
    });
    gsap.set(etoiles, { scale: 0 });
    quandVisible(el, function () {
      gsap.to(etoiles, { scale: 1, duration: 0.35, stagger: 0.09, delay: 0.2, ease: 'back.out(2.4)', clearProps: 'transform' });
    });
  });

  /* Compteurs : le texte d'origine est remis tel quel à la fin */
  function compter(el) {
    var original = el.textContent;
    var m = original.match(/\d[\d\s  ]*/);
    if (!m) return;
    var cible = parseInt(m[0].replace(/\D/g, ''), 10);
    var o = { v: 0 };
    var boite = el.parentElement;
    if (boite) boite.style.minWidth = Math.ceil(boite.getBoundingClientRect().width) + 'px';
    el.textContent = original.replace(m[0], '0' + (/\s$/.test(m[0]) ? ' ' : ''));
    quandVisible(el, function () {
      gsap.to(o, {
        v: cible, duration: 1.3, ease: 'power2.out',
        onUpdate: function () {
          var n = Math.round(o.v).toString().replace(/\B(?=(\d{3})+$)/g, ' ');
          el.textContent = original.replace(m[0], n + (/\s$/.test(m[0]) ? ' ' : ''));
        },
        onComplete: function () { el.textContent = original; if (boite) boite.style.minWidth = ''; }
      });
    });
  }
  $$('.v2-law-nums b, .v2-count').forEach(compter);

  /* Espace commerçant : la barre de chaque étape se remplit en descendant */
  var etapes = $$('.v2-merchant > li');
  if (etapes.length) {
    var barres = etapes.map(function (li) {
      var b = document.createElement('span');
      b.className = 'v2-fill';
      b.setAttribute('aria-hidden', 'true');
      li.appendChild(b);
      return b;
    });
    gsap.timeline({ scrollTrigger: { trigger: '.v2-merchant', start: 'top 82%', end: 'bottom 55%', scrub: 0.4 } })
      .to(barres, { scaleX: 1, ease: 'none', stagger: 1, duration: 1 });
  }

  /* Trajet du colis : il avance avec le défilement, et chaque étape s'allume à son passage */
  var trajet = document.querySelector('.v2-track');
  var pas = $$('.v2-steps > li');
  if (trajet && pas.length) {
    var mm = gsap.matchMedia();
    mm.add('(min-width:521px)', function () {
      var colis = trajet.querySelector('.v2-parcel');
      gsap.set(colis, { left: 0 });
      gsap.fromTo(colis, { x: 0 }, {
        x: function () { return trajet.clientWidth - colis.offsetWidth; },
        ease: 'none',
        scrollTrigger: {
          trigger: trajet, start: 'top 85%', end: 'top 30%', scrub: 0.5, invalidateOnRefresh: true,
          onUpdate: function (self) {
            pas.forEach(function (li, i) { li.classList.toggle('on', self.progress >= i / (pas.length - 1) * 0.98); });
          }
        }
      });
    });
    mm.add('(max-width:520px)', function () {
      pas.forEach(function (li) {
        quandVisible(li, function () { li.classList.add('on'); });
      });
    });
  }

  /* Étiquette du premier écran : elle suit légèrement la souris */
  var etiquette = document.querySelector('.v2-hero .v2-label');
  if (etiquette && window.matchMedia('(hover:hover) and (pointer:fine) and (min-width:821px)').matches) {
    var hero = document.querySelector('.v2-hero');
    setTimeout(function () {
      var rx = gsap.quickTo(etiquette, 'x', { duration: 0.7, ease: 'power3' });
      var ry = gsap.quickTo(etiquette, 'y', { duration: 0.7, ease: 'power3' });
      var rr = gsap.quickTo(etiquette, 'rotation', { duration: 0.7, ease: 'power3' });
      hero.addEventListener('pointermove', function (e) {
        var b = hero.getBoundingClientRect();
        var dx = (e.clientX - b.left) / b.width - 0.5;
        var dy = (e.clientY - b.top) / b.height - 0.5;
        rx(dx * 16); ry(dy * 12); rr(1.5 + dx * 3);
      });
      hero.addEventListener('pointerleave', function () { rx(0); ry(0); rr(1.5); });
    }, 1300);
  }

  /* Recalcul une fois la page chargée (polices et images) */
  planifier();
  window.addEventListener('load', function () { ScrollTrigger.refresh(); planifier(); });
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(function () { ScrollTrigger.refresh(); });
})();
