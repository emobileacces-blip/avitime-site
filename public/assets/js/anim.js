/* Avitime — animations de l'accueil (GSAP + ScrollTrigger). Sans JavaScript, ou en mouvement réduit, tout reste visible et immobile. */
(function () {
  if (!window.gsap || !window.ScrollTrigger) return;
  gsap.registerPlugin(ScrollTrigger);
  var reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  if (reduce) return;
  var ease = 'power3.out';

  /* 1. Titre principal : les mots montent un à un */
  function splitWords(el) {
    if (!el || el.dataset.split) return [];
    el.dataset.split = '1';
    var words = [];
    var nodes = Array.prototype.slice.call(el.childNodes);
    el.textContent = '';
    nodes.forEach(function (node) {
      var text = node.textContent;
      var cls = node.nodeType === 1 ? node.className : '';
      text.split(/(\s+)/).forEach(function (part) {
        if (!part) return;
        if (/^\s+$/.test(part)) { el.appendChild(document.createTextNode(' ')); return; }
        var line = document.createElement('span');
        line.className = 'split-line';
        var w = document.createElement('span');
        w.className = 'split-word' + (cls ? ' ' + cls.replace(/\bw\b/, '').trim() : '');
        w.textContent = part;
        line.appendChild(w);
        el.appendChild(line);
        words.push(w);
      });
    });
    return words;
  }

  var h1 = document.querySelector('.hero h1');
  var heroWords = splitWords(h1);
  var intro = gsap.timeline({ defaults: { ease: ease } });
  intro.from(heroWords, { yPercent: 110, duration: .9, stagger: .045 })
       .from('.hero .eyebrow, .hero .lede, .hero .ctas, .hero .pioneer-pill', { y: 18, opacity: 0, duration: .6, stagger: .08 }, '-=.5');

  /* 2. La fiche produit reçoit ses avis */
  var card = document.querySelector('.hl-page');
  if (card) {
    var stars = card.querySelector('.hl-stars');
    var note = card.querySelector('.hl-note');
    var count = card.querySelector('.hl-count');
    var bars = card.querySelectorAll('.ba-hist u');
    var nums = card.querySelectorAll('.ba-hist .hl-num');
    var review = card.querySelector('.ba-rev');
    var stamp = card.querySelector('.hl-stamp');
    var counter = { n: 0, c: 0 };
    intro.from(card, { y: 60, rotateX: 14, opacity: 0, duration: 1.1 }, .25)
         .to(counter, { n: 4.2, c: 5, duration: 1.6, ease: 'power2.out', onUpdate: function () {
            note.textContent = counter.n.toFixed(1).replace('.', ',');
            count.textContent = Math.round(counter.c);
            stars.style.setProperty('--fill', (counter.n / 5 * 100) + '%');
         } }, .9)
         .fromTo(bars, { '--w': '0%' }, { '--w': function (i, el) { return el.dataset.w; }, duration: 1, stagger: .08, ease: 'power2.out' }, 1)
         .from(nums, { opacity: 0, duration: .3, stagger: .08 }, 1.2)
         .from(review, { y: 24, opacity: 0, duration: .7 }, 2.1)
         .from(stamp, { scale: 1.6, rotate: -8, opacity: 0, duration: .45, ease: 'back.out(2.2)' }, 2.6);

    /* Légère inclinaison qui suit la souris (ordinateur seulement) */
    var vis = document.querySelector('.hero-live');
    if (vis && window.matchMedia('(pointer: fine)').matches) {
      var rx = gsap.quickTo(card, 'rotateX', { duration: .6, ease: 'power3' });
      var ry = gsap.quickTo(card, 'rotateY', { duration: .6, ease: 'power3' });
      vis.addEventListener('pointermove', function (e) {
        var r = vis.getBoundingClientRect();
        ry(((e.clientX - r.left) / r.width - .5) * 10);
        rx(-((e.clientY - r.top) / r.height - .5) * 8);
      });
      vis.addEventListener('pointerleave', function () { rx(0); ry(0); });
    }
  }

  /* 3. Titres de section : les mots montent quand on arrive dessus */
  document.querySelectorAll('.sec-title, .film h2').forEach(function (t) {
    var w = splitWords(t);
    gsap.from(w, { yPercent: 110, duration: .8, stagger: .03, ease: ease,
      scrollTrigger: { trigger: t, start: 'top 88%', once: true } });
  });

  /* 4. Cartes : elles arrivent en vague, une seule fois */
  ScrollTrigger.batch('.truth-card, .pq-card, .integ-card, .gain-card, .duo-grid > *, .ai-card, .eeat, .law-col, .faq details, .tile, .lead-card', {
    start: 'top 90%', once: true,
    onEnter: function (els) { gsap.from(els, { y: 28, opacity: 0, duration: .6, stagger: .07, ease: ease }); }
  });

  /* 5. Chronologie J0 → J+30 : la ligne orange se trace au défilement */
  var tl = document.querySelector('#nouvelle-boutique .timeline');
  if (tl) {
    var rail = document.createElement('span');
    rail.className = 'tl-rail';
    rail.setAttribute('aria-hidden', 'true');
    rail.innerHTML = '<i></i>';
    tl.style.paddingLeft = tl.style.paddingLeft || '22px';
    tl.prepend(rail);
    var items = tl.querySelectorAll('li');
    gsap.to(rail.firstChild, { scaleY: 1, ease: 'none',
      scrollTrigger: { trigger: tl, start: 'top 75%', end: 'bottom 55%', scrub: .6,
        onUpdate: function (st) { items.forEach(function (li, i) { li.classList.toggle('on', st.progress >= i / items.length); }); } } });
  }

  /* 6. Avant / après : la fiche de droite se remplit pendant qu'on fait défiler */
  var after = document.querySelector('#avant-apres .ba-col:not(.ba-off) .ba-page');
  if (after) {
    var ub = after.querySelectorAll('.ba-hist u');
    ub.forEach(function (u) { u.dataset.w = getComputedStyle(u).getPropertyValue('--w').trim() || '0%'; });
    var st = { trigger: '#avant-apres .ba-grid', start: 'top 80%', end: 'center 45%', scrub: .7 };
    gsap.fromTo(ub, { '--w': '0%' }, { '--w': function (i, el) { return el.dataset.w; }, stagger: .1, ease: 'none', scrollTrigger: st });
    gsap.from(after.querySelectorAll('.ba-rev'), { opacity: 0, y: 30, stagger: .2, ease: 'none', scrollTrigger: st });
    gsap.from('#avant-apres .ba-arrow', { rotate: -180, scale: .4, ease: 'none', scrollTrigger: st });
    gsap.fromTo('#avant-apres .ba-off .ba-page', { filter: 'saturate(1)' }, { filter: 'saturate(.2)', ease: 'none', scrollTrigger: st });
  }

  /* 7. La loi : les chiffres défilent jusqu'à leur valeur */
  document.querySelectorAll('.law-stat b').forEach(function (b) {
    var txt = b.textContent;
    var m = txt.match(/[\d\s  ]+/);
    if (!m) return;
    var target = parseInt(m[0].replace(/\D/g, ''), 10);
    var o = { v: 0 };
    gsap.to(o, { v: target, duration: 1.4, ease: 'power2.out',
      scrollTrigger: { trigger: b, start: 'top 85%', once: true },
      onUpdate: function () { b.textContent = txt.replace(m[0].trim(), Math.round(o.v).toLocaleString('fr-FR').replace(/ /g, ' ')); } });
  });

  /* 8. Espace commerçant : les écrans se redressent */
  var shots = document.querySelectorAll('#apercu-espace .app-shots > *');
  if (shots.length) {
    gsap.fromTo(shots, { rotateX: 22, y: 60, scale: .94 }, { rotateX: 0, y: 0, scale: 1, ease: 'none', stagger: .05,
      scrollTrigger: { trigger: '#apercu-espace .app-shots', start: 'top 95%', end: 'top 35%', scrub: .8 } });
  }

  /* 9. FAQ : la réponse se déplie en douceur */
  document.querySelectorAll('.faq details').forEach(function (d) {
    var sum = d.querySelector('summary');
    var body = d.querySelector('summary ~ *');
    if (!sum || !body) return;
    sum.addEventListener('click', function (e) {
      e.preventDefault();
      if (d.open) {
        gsap.to(body, { height: 0, opacity: 0, duration: .3, ease: 'power2.in', onComplete: function () { d.open = false; gsap.set(body, { clearProps: 'height,opacity' }); } });
      } else {
        d.open = true;
        gsap.fromTo(body, { height: 0, opacity: 0, overflow: 'hidden' }, { height: 'auto', opacity: 1, duration: .45, ease: ease, onComplete: function () { gsap.set(body, { clearProps: 'height,overflow' }); } });
      }
    });
  });

  /* 10. Appel final : les boutons arrivent après le titre */
  gsap.from('.final .ctas > *, .final .btn', { y: 24, opacity: 0, duration: .6, stagger: .1, ease: ease,
    scrollTrigger: { trigger: '.final', start: 'top 75%', once: true } });

  /* 11. Bouton principal : il suit légèrement le curseur */
  if (window.matchMedia('(pointer: fine)').matches) {
    document.querySelectorAll('.hero .btn, .final .btn').forEach(function (btn) {
      var x = gsap.quickTo(btn, 'x', { duration: .4, ease: 'power3' });
      var y = gsap.quickTo(btn, 'y', { duration: .4, ease: 'power3' });
      btn.addEventListener('pointermove', function (e) {
        var r = btn.getBoundingClientRect();
        x((e.clientX - r.left - r.width / 2) * .25);
        y((e.clientY - r.top - r.height / 2) * .35);
      });
      btn.addEventListener('pointerleave', function () { x(0); y(0); });
    });
  }
})();
