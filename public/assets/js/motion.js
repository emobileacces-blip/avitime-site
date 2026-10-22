/* Avitime — couche d'animation (aperçu v2). Additive : ne change aucun texte du HTML (SEO intact). */
(() => {
  const reduce = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const fine = window.matchMedia('(hover: hover) and (pointer: fine)').matches;
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];

  /* Plateformes en pastilles (le texte reste le même) */
  const plat = $$('.hero .eyebrow').find(p => /Compatible/.test(p.textContent));
  if (plat) {
    const names = plat.textContent.replace(/Compatible/i, '').split('·').map(s => s.trim()).filter(Boolean);
    const box = document.createElement('div');
    box.className = 'm-plats rise d4';
    box.setAttribute('aria-label', plat.textContent.trim());
    const lead = document.createElement('em'); lead.textContent = 'Compatible'; lead.setAttribute('aria-hidden', 'true'); box.appendChild(lead);
    names.forEach(n => { const s = document.createElement('span'); s.textContent = n; s.setAttribute('aria-hidden', 'true'); box.appendChild(s); });
    plat.replaceWith(box);
  }

  if (reduce) return;

  /* Barre de progression + ombre du menu */
  const bar = document.createElement('div'); bar.className = 'm-progress'; bar.setAttribute('aria-hidden', 'true'); document.body.appendChild(bar);
  const nav = $('#top-nav');
  let ticking = false;
  const onScroll = () => {
    if (ticking) return; ticking = true;
    requestAnimationFrame(() => {
      const h = document.documentElement.scrollHeight - innerHeight;
      bar.style.transform = `scaleX(${h > 0 ? Math.min(1, scrollY / h) : 0})`;
      if (nav) nav.classList.toggle('m-scrolled', scrollY > 8);
      ticking = false;
    });
  };
  addEventListener('scroll', onScroll, { passive: true }); onScroll();

  /* Hero : 2e halo + pastilles flottantes (décoratives, aria-hidden) */
  const hero = $('.hero');
  if (hero) {
    const g = document.createElement('div'); g.className = 'm-glow2'; g.setAttribute('aria-hidden', 'true'); hero.appendChild(g);
    const ico = {
      cart: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="9" cy="20" r="1.5"/><circle cx="18" cy="20" r="1.5"/><path d="M3 4h2l2.4 11.2a1 1 0 0 0 1 .8h9.2a1 1 0 0 0 1-.8L20 8H6"/></svg>',
      check: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6 9 17l-5-5"/></svg>',
      user: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg>',
      search: '<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>'
    };
    const chips = document.createElement('div'); chips.className = 'm-chips'; chips.setAttribute('aria-hidden', 'true');
    chips.innerHTML =
      `<div class="m-chip c1"><span class="m-ic">${ico.cart}</span><span>Commande à 0 €<small>Code à usage unique</small></span></div>` +
      `<div class="m-chip c2"><span class="m-ic">${ico.user}</span><span>Testeur sélectionné<small>par Avitime, pas par la boutique</small></span></div>` +
      `<div class="m-chip c3"><span class="m-ic ok">${ico.check}</span><span><span class="m-st">★★★★★</span> Avis publié<small>« Produit offert pour test »</small></span></div>` +
      `<div class="m-chip c4"><span class="m-ic">${ico.search}</span><span>Visible sur Google<small>et lisible par les IA</small></span></div>`;
    hero.appendChild(chips);
  }

  /* Cartes : halo qui suit la souris */
  const cards = $$('.tile, .truth-card, .gain-card, .ai-card, .eeat, .zero-card');
  cards.forEach(c => c.classList.add('m-spot'));
  if (fine) {
    cards.forEach(c => c.addEventListener('pointermove', e => {
      const r = c.getBoundingClientRect();
      c.style.setProperty('--mx', `${e.clientX - r.left}px`);
      c.style.setProperty('--my', `${e.clientY - r.top}px`);
    }));
    /* Boutons : léger effet aimant */
    $$('.btn').forEach(b => {
      b.addEventListener('pointermove', e => {
        const r = b.getBoundingClientRect();
        const x = (e.clientX - r.left - r.width / 2) / r.width, y = (e.clientY - r.top - r.height / 2) / r.height;
        b.style.transform = `translate(${x * 6}px, ${y * 5}px)`;
      });
      b.addEventListener('pointerleave', () => { b.style.transform = ''; });
    });
  }

  /* Bordure lumineuse : cartes claires « avec Avitime » à côté d'une carte sombre */
  $$('.duo-grid').forEach(g => $$(':scope > .tile:not(.dark)', g).forEach(t => t.classList.add('m-beam')));

  /* Apparitions en cascade dans les grilles (s'appuie sur [data-reveal] + --i de main.js) */
  const stagger = () => $$('.truth-grid, .duo-grid, .steps, .law-stats, .eeat-grid').forEach(g => {
    [...g.children].forEach((ch, i) => ch.style.setProperty('--i', i));
  });
  $$('.eeat').forEach(e => e.parentElement && e.parentElement.classList.add('eeat-grid'));
  $$('.law-stat').forEach(e => e.parentElement && e.parentElement.classList.add('law-stats'));
  stagger();

  /* ===== v3 ===== */

  /* Bandeau défilant sous le haut de page (décoratif, s'arrête au survol) */
  if (hero) {
    const items = ['Commande à 0 €', 'Testeurs sélectionnés par Avitime', 'Avis avec photos', '« Produit offert pour test »', 'Étoiles dans Google', 'Lisible par ChatGPT, Gemini et Claude', 'Avis négatifs publiés aussi', 'PrestaShop · WooCommerce · Shopify'];
    const row = items.map(t => `<span>${t}</span><i>★</i>`).join('');
    const mq = document.createElement('div'); mq.className = 'm-marquee'; mq.setAttribute('aria-hidden', 'true');
    mq.innerHTML = `<div class="m-track">${row}${row}</div>`;
    hero.after(mq);
  }

  /* Haut de page : relief qui suit la souris (pastilles et halos) */
  if (hero && fine) {
    const layers = [...$$('.m-chip', hero).map((el, i) => [el, [14, -10, 18, -12][i] || 10]), [$('.m-glow2', hero), -24]].filter(l => l[0]);
    let tx = 0, ty = 0, cx = 0, cy = 0, raf = 0;
    const loop = () => {
      cx += (tx - cx) * .08; cy += (ty - cy) * .08;
      layers.forEach(([el, d]) => { el.style.translate = `${cx * d}px ${cy * d}px`; });
      raf = Math.abs(tx - cx) + Math.abs(ty - cy) > .001 ? requestAnimationFrame(loop) : 0;
    };
    hero.addEventListener('pointermove', e => {
      const r = hero.getBoundingClientRect();
      tx = (e.clientX - r.left) / r.width - .5; ty = (e.clientY - r.top) / r.height - .5;
      if (!raf) raf = requestAnimationFrame(loop);
    });
    hero.addEventListener('pointerleave', () => { tx = 0; ty = 0; if (!raf) raf = requestAnimationFrame(loop); });
  }

  /* Petites cartes : légère inclinaison 3D au survol */
  if (fine) $$('.truth-card, .gain-card, .eeat, .ai-card').forEach(c => {
    c.classList.add('m-tilt');
    c.addEventListener('pointermove', e => {
      const r = c.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
      c.style.transform = `perspective(900px) rotateX(${(-y * 5).toFixed(2)}deg) rotateY(${(x * 6).toFixed(2)}deg) translateY(-4px)`;
    });
    c.addEventListener('pointerleave', () => { c.style.transform = ''; });
  });

  /* Icônes des listes : apparition en cascade */
  $$('.ico-list').forEach(l => [...l.children].forEach((li, i) => li.style.setProperty('--i', i)));

  /* Bande finale : aurore orange */
  $$('.sec.final').forEach(s => { const a = document.createElement('div'); a.className = 'm-aurora'; a.setAttribute('aria-hidden', 'true'); s.prepend(a); });

  if (!('IntersectionObserver' in window)) return;

  /* Titres de section : les mots montent un par un (texte inchangé) */
  const titles = $$('.sec-title').filter(h => [...h.childNodes].every(n => n.nodeType === 3));
  titles.forEach(h => {
    const words = h.textContent.trim().split(/\s+/);
    h.textContent = '';
    words.forEach((w, i) => {
      const s = document.createElement('span'); s.className = 'm-w'; s.textContent = w; s.style.setProperty('--wi', i);
      h.appendChild(s); if (i < words.length - 1) h.appendChild(document.createTextNode(' '));
    });
    h.classList.add('m-words');
  });
  const tio = new IntersectionObserver(es => es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('m-in'); tio.unobserve(e.target); } }), { rootMargin: '0px 0px -12% 0px' });
  titles.forEach(h => tio.observe(h));

  /* Frise J0 → J+30 : une ligne se trace au fil du défilement */
  const stepLists = $$('.steps');
  stepLists.forEach(ol => ol.classList.add('m-steps'));
  const drawSteps = () => stepLists.forEach(ol => {
    const r = ol.getBoundingClientRect(), mid = innerHeight * .62;
    const p = Math.max(0, Math.min(1, (mid - r.top) / r.height));
    ol.style.setProperty('--sp', p.toFixed(3));
    [...ol.querySelectorAll('li')].forEach(li => { const lr = li.getBoundingClientRect(); li.classList.toggle('m-on', lr.top + 20 < mid); });
  });
  if (stepLists.length) { addEventListener('scroll', () => requestAnimationFrame(drawSteps), { passive: true }); drawSteps(); }

  /* Étoiles qui s'allument une à une */
  const starRows = [...new Set($$('.star-on').map(s => s.parentElement))];
  starRows.forEach(row => { row.classList.add('m-stars-wait'); $$('.star-on', row).forEach((s, i) => s.style.setProperty('--si', i)); });
  const sio = new IntersectionObserver(es => es.forEach(e => {
    if (!e.isIntersecting) return;
    e.target.classList.remove('m-stars-wait'); e.target.classList.add('m-stars-go'); sio.unobserve(e.target);
  }), { threshold: .6 });
  starRows.forEach(r => sio.observe(r));

  /* Chiffres qui défilent (le texte final reste exactement celui du HTML) */
  const nums = $$('.law-stat b');
  const cio = new IntersectionObserver(es => es.forEach(e => {
    if (!e.isIntersecting) return; cio.unobserve(e.target);
    const el = e.target, final = el.textContent, m = final.match(/^([\d\s  ]+)(.*)$/);
    if (!m) return;
    const target = parseInt(m[1].replace(/\D/g, ''), 10), rest = m[2], t0 = performance.now(), dur = 1400;
    const fmt = n => n.toLocaleString('fr-FR').replace(/ /g, ' ');
    const step = t => {
      const p = Math.min(1, (t - t0) / dur), v = Math.round(target * (1 - Math.pow(1 - p, 3)));
      el.textContent = p < 1 ? fmt(v) + rest : final;
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  }), { threshold: .7 });
  nums.forEach(n => cio.observe(n));
})();
