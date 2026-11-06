#!/usr/bin/env python3
"""Génère l'accueil, /tarifs et la page 404 de la direction « le colis ouvert ».
À lancer après tools/corrections_vitrine.py : le pied de page vient de public/commercants.html."""
import html as H
import json
import re
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
PUBLIC = RACINE / "public"
ref = (PUBLIC / "commercants.html").read_text(encoding="utf-8")
FOOTER = re.search(r'<footer class="site-foot">.*?</footer>', ref, re.S).group(0)
NAV_ACTIONS = '<div class="nav-actions">\n{lang}<a class="ghost" href="/espace-commercant">Espace commerçant</a>\n<a class="btn-sm" href="{cta}">Audit gratuit</a>\n</div>'
MENU = [("/commercants", "Commerçants"), ("/audit-seo", "Audit SEO"), ("/tarifs", "Tarifs"),
        ("/integrations", "Intégrations"), ("/devenir-testeur", "Testeurs"), ("/faq", "FAQ"),
        ("/guides/", "Guides"), ("/a-propos.html", "À propos")]


def typo(page):
    """Espaces insécables de la ponctuation française, dans le texte visible de <main> uniquement."""
    def texte(m):
        s = m.group(1)
        for avant, apres in ((" :", "\u00a0:"), (" ?", "\u00a0?"), (" !", "\u00a0!"), (" ;", "\u00a0;"), ("« ", "«\u00a0"), (" »", "\u00a0»")):
            s = s.replace(avant, apres)
        return ">" + s + "<"
    debut, fin = page.index("<main"), page.index("</main>")
    return page[:debut] + re.sub(r">([^<>]+)<", texte, page[debut:fin]) + page[fin:]


def header(courant=None, cta="/audit-seo", lang=""):
    liens = "\n".join(f'<a href="{u}"{" aria-current=\"page\"" if u == courant else ""}>{t}</a>' for u, t in MENU)
    return f'''<header class="nav" id="top-nav">
<div class="wrap">
<a class="brand" href="/"><img alt="Avitime, accueil" height="40" src="/assets/img/avitime-logo-96.png" width="168"/></a>
<nav aria-label="Navigation principale" class="nav-links">
{liens}
</nav>
{NAV_ACTIONS.format(lang=lang, cta=cta)}
</div>
</header>'''


def tete(titre, desc, adresse, ld, robots="", alternates=""):
    t, d = H.escape(titre, quote=True), H.escape(desc, quote=True)
    rob = f'<meta name="robots" content="{robots}">\n' if robots else ""
    canon = f'<link rel="canonical" href="{adresse}">\n' if adresse else ""
    og = f'<meta property="og:url" content="{adresse}">\n' if adresse else ""
    return f'''<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="msvalidate.01" content="2FBC50E0EB86A03E0B909D68B78DD90B">
<title>{t}</title>
<meta name="description" content="{d}">
{rob}{canon}{alternates}<meta property="og:type" content="website">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="Avitime">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
{og}<meta property="og:image" content="https://avitime.fr/assets/img/og-image.jpg">
<meta property="og:image:type" content="image/jpeg">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="Logo Avitime : des produits testés, des avis qui font vendre">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:image" content="https://avitime.fr/assets/img/og-image.jpg">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/img/icon-32.png">
<link rel="apple-touch-icon" href="/assets/img/icon-180.png">
<meta name="theme-color" content="#0A0A0A">
<link rel="preload" href="/assets/fonts/v2/anton-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="/assets/fonts/v2/archivo-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/css/style.css?v=logo1">
<link rel="stylesheet" href="/assets/css/v2.css?v=16">
{ld}</head>
<body class="v2">
'''


def jsonld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False) + "</script>\n"


FAQ = [
    ("Et si un testeur met une mauvaise note ?",
     "L’avis est publié. La boutique ne peut ni le modifier ni le supprimer : c’est ce qui rend les autres avis crédibles. Vous pouvez répondre publiquement, puis corriger la fiche ou le produit. Un avis qui parle seulement de la livraison est refusé, et le testeur signale le problème à part."),
    ("Combien ça coûte vraiment ?",
     "Vos 5 premiers tests sont offerts, sans abonnement ni carte bancaire. Les produits et leur expédition restent à votre charge : avec un produit à 12 € et 6 € de port, 5 testeurs coûtent 90 €. Ensuite, l’abonnement commence à 39,90 € HT par mois en annuel, ou 49,90 € HT par mois sans engagement."),
    ("Combien d’avis une boutique va-t-elle obtenir ?",
     "Avitime ne garantit aucun volume d’avis. Chaque produit offert est réellement commandé et livré à un testeur sélectionné, qui s’engage à publier un avis dans le délai prévu. Le tableau de bord montre exactement combien de missions aboutissent."),
    ("Une boutique peut-elle choisir ses testeurs ?",
     "Non. Elle définit les critères de la campagne (pays, catégorie, exclusions), mais la sélection finale revient à Avitime. C’est ce qui garantit l’indépendance des avis."),
    ("Qui expédie les produits ?",
     "La boutique, avec ses transporteurs habituels. Avitime ne stocke ni n’expédie de produits. Sur un site sans module, l’adresse du testeur sélectionné s’affiche dans votre espace, et vous indiquez le suivi."),
    ("Quels produits peuvent être testés ?",
     "Votre boutique doit livrer en France, et le produit testé doit être celui que reçoivent vos clients. Les catégories sensibles (santé, compléments, nicotine, alcool, produits pour mineurs…) suivent une politique d’éligibilité stricte. Les produits numériques sont acceptés."),
    ("Qui édite Avitime ?",
     "Avitime est un service récent, édité par SPARKMOTION AGENCY LTD, société anglaise (Companies House n° 16880032) dirigée par son fondateur, Cyril Quémy. Sa méthode et ses conditions sont publiques."),
]
ld_faq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
    {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": r}} for q, r in FAQ]}
ld_org = {"@context": "https://schema.org", "@graph": [
    {"@type": "WebSite", "name": "Avitime", "url": "https://avitime.fr/", "inLanguage": "fr-FR"},
    {"@type": "Organization", "name": "Avitime", "url": "https://avitime.fr/", "logo": "https://avitime.fr/assets/img/icon-512.png",
     "description": "Avitime fait tester des produits de boutiques en ligne par des consommateurs sélectionnés, puis publie leurs avis de façon transparente et traçable.",
     "sameAs": ["https://www.instagram.com/avitime_fr/", "https://www.tiktok.com/@avitime_fr", "https://www.facebook.com/profile.php?id=61595261199682",
                "https://www.linkedin.com/company/avitime/", "https://www.youtube.com/@avitime_fr", "https://fr.trustpilot.com/review/avitime.fr",
                "https://www.g2.com/products/avitime/reviews", "https://www.capterra.com/p/10270314/Avitime/", "https://www.getapp.com/all-software/a/avitime/",
                "https://www.softwareadvice.com/product/777663-Avitime/", "https://www.lafabriquedunet.fr/logiciel/avitime"],
     "founder": {"@type": "Person", "name": "Cyril Quémy"}}]}
faq_html = "\n".join(f"<details><summary>{H.escape(q, quote=False)}</summary><p>{H.escape(r, quote=False)}</p></details>" for q, r in FAQ)

SCRIPT_ANIM = '''<script src="/assets/js/vendor/gsap.min.js?v=3.12.5" defer></script>
<script src="/assets/js/vendor/ScrollTrigger.min.js?v=3.12.5" defer></script>
<script src="/assets/js/v2-anim.js?v=2" defer></script>
'''
SCRIPT_FORM = '''<script>(function(){var f=document.getElementById("audit");if(!f)return;var q=new URLSearchParams(location.search);f.t.value=String(Date.now());f.src.value=(q.get("src")||q.get("utm_source")||"accueil").replace(/[^a-z0-9_-]/gi,"").slice(0,60);f.addEventListener("submit",function(){var b=f.querySelector("button");setTimeout(function(){b.disabled=true;b.textContent="Lancement de l’analyse…"},0)})})();</script>
<script>(function(){var e=document.getElementById("nb-testeurs");if(!e||!window.fetch)return;fetch("https://app.avitime.fr/api/public/testeurs").then(function(r){return r.json()}).then(function(d){if(!d||typeof d.testeurs!=="number"||d.testeurs<100)return;e.querySelector("b").textContent=d.testeurs+"+";e.hidden=false}).catch(function(){})})();</script>
'''
FORM = '''<form class="v2-form" id="audit" method="post" action="https://app.avitime.fr/api/audit-gratuit" accept-charset="utf-8">
<div class="v2-form-row">
<label><span>Adresse de votre boutique</span><input type="text" name="url" inputmode="url" autocomplete="url" required maxlength="300" placeholder="www.ma-boutique.fr"></label>
<label><span>Votre e-mail</span><input type="email" name="email" autocomplete="email" required maxlength="254" placeholder="vous@ma-boutique.fr"></label>
<button class="v2-btn" type="submit">Auditer ma boutique</button>
</div>
<input type="hidden" name="from" value="https://avitime.fr/audit-seo"><input type="hidden" name="t" value=""><input type="hidden" name="src" value="accueil">
<div class="v2-hp" aria-hidden="true"><label>Website <input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
<p class="v2-form-note">Audit SEO gratuit, sans compte ni carte bancaire, résultat en 1 à 3 minutes. Votre e-mail sert seulement à vous envoyer le lien de votre rapport (et un rappel) ; désinscription en un clic. <a href="/confidentialite.html">Confidentialité</a></p>
</form>'''

H1_MOTS = "Obtenir des avis clients en faisant tester ses produits"
H1 = " ".join(f'<span class="v2-word" style="--i:{i}">{m}</span>' for i, m in enumerate(H1_MOTS.split()))

ACCUEIL = f'''<main id="contenu">
<div class="v2-strip"><div class="v2-w v2-strip-in"><p><b>Vous voulez tester des produits ?</b> <span class="v2-strip-opt">Inscription gratuite, le produit reste à vous.</span></p><a class="v2-btn" href="/devenir-testeur">Devenir testeur</a></div></div>
<section class="v2-hero" id="accueil"><div class="v2-w v2-hero-grid">
<div>
<h1 class="v2-h1">{H1}</h1>
<p class="v2-lead">Avitime est un service de tests produits pour les boutiques en ligne qui livrent en France, compatible avec PrestaShop et WooCommerce, et Shopify en cours de validation.</p>
<p class="v2-lead-2">Des consommateurs sélectionnés par Avitime commandent à 0 € sur votre boutique, testent chez eux, puis publient leur avis sur votre fiche, note basse comprise, avec la mention « Produit offert pour test ». Vos 5 premiers tests sont offerts&nbsp;: il vous reste à payer le produit et le port.</p>
{FORM}
<div class="v2-links"><a href="/devenir-commercant">Lancer mes 5 tests offerts</a><a href="/tarifs">Voir les tarifs</a><a href="https://cal.com/avitime/15min" target="_blank" rel="noopener">Réserver un appel de 15 min</a></div>
<p id="nb-testeurs" class="v2-mono v2-compat" hidden><b></b> testeurs inscrits</p>
</div>
<figure>
<div class="v2-label"><div class="v2-label-in">
<p class="v2-mono">MISSION M-2041 · COLIS LIVRÉ J+7<br>Gourde isotherme 500 ml<br>Julie M., testeuse · 3 semaines d’usage</p>
<hr>
<p class="v2-hand">« Le café reste chaud toute la matinée. Rien ne fuit dans le sac. »</p>
<p class="v2-pros">+ garde bien la chaleur · − un peu lourde pleine</p>
<span class="v2-stamp">Produit offert pour test</span>
</div></div>
<figcaption class="v2-cap">Exemple illustratif</figcaption>
</figure>
</div></section>

<section class="v2-proof" aria-label="Les garanties Avitime"><div class="v2-w"><ul>
<li>Une vraie commande à 0 € sur votre boutique</li>
<li>Des testeurs sélectionnés par Avitime</li>
<li>Tous les avis sont publiés, même les mitigés</li>
<li>La mention « Produit offert pour test » sur chaque avis</li>
</ul></div></section>

<section class="v2-band" id="probleme"><div class="v2-w v2-split">
<div>
<h2 class="v2-h2">Fiche produit avec ou sans avis clients : ce que voit le visiteur</h2>
<p class="v2-lead" style="margin-top:18px">Il faut des ventes pour avoir des avis, et des avis pour faire des ventes. Acheter des avis est interdit. Faire tester le produit pour de vrai, en le disant clairement, permet de sortir de ce cercle.</p>
<p style="margin-top:14px"><a href="/pourquoi-faire-tester-vos-produits">Pourquoi faire tester vos produits : Google, IA, publicité, loi</a></p>
</div>
<figure>
<h3 class="v2-h3" style="margin-bottom:12px">La même fiche, avant et après 5 tests</h3>
<div class="v2-compare">
<div class="v2-fiche"><span class="v2-mono">AVANT</span><h3>Gourde isotherme 500 ml</h3><p>24,90 €</p><p class="v2-sm" style="margin-top:8px">Aucun avis pour le moment.</p></div>
<div class="v2-fiche"><span class="v2-mono">APRÈS UNE CAMPAGNE</span><h3>Gourde isotherme 500 ml</h3><p>24,90 €</p><p class="v2-sm"><span class="v2-stars" aria-hidden="true">★★★★☆</span> 4,2 · <span class="v2-count">5</span> avis de testeurs</p>
<div class="v2-review"><b>Julie M.</b> · 5/5 · 3 semaines d’usage<br>« Le café reste chaud toute la matinée. »<span class="v2-mention">Produit offert pour test — Testeur Avitime vérifié</span></div>
<div class="v2-review"><b>Karim B.</b> · 2/5 · 2 semaines d’usage<br>« Bonne gourde, mais le bouchon est dur à dévisser avec des gants. »<span class="v2-mention">Produit offert pour test — Testeur Avitime vérifié</span></div>
</div>
</div>
<figcaption class="v2-fine" style="margin-top:10px">Exemple illustratif : boutique, produit et avis fictifs. Aucun volume d’avis n’est garanti.</figcaption>
</figure>
</div></section>

<section class="v2-band v2-route-band" id="concept"><div class="v2-w">
<div class="v2-route-head"><h2 class="v2-h2">Comment se déroule un test produit, en six étapes</h2><p class="v2-mono">Délais indicatifs : en général J+14 à J+30</p></div>
<p class="v2-lead" style="margin-top:14px">Vous créez une campagne, Avitime sélectionne les testeurs, ils commandent à 0 € sur votre boutique, testent le produit, puis publient leur avis sur votre fiche. Comptez en général 14 à 30 jours, selon vos expéditions et le temps de test.</p>
<div class="v2-track" aria-hidden="true"><span class="v2-parcel"></span></div>
<ol class="v2-steps">
<li><span class="v2-mono">J0</span><h3>Vous lancez une campagne</h3><p>Un produit, un nombre de testeurs, des critères. Le budget s’affiche avant publication.</p></li>
<li><span class="v2-mono">Ensuite</span><h3>Avitime choisit</h3><p>Âge, pays, catégorie, anti-doublons, puis tirage au sort. Jamais la boutique.</p></li>
<li><span class="v2-mono">J+3</span><h3>Commande à 0 €</h3><p>Un lien à usage unique, lié au compte, au produit et à la mission.</p></li>
<li><span class="v2-mono">J+7</span><h3>Vous expédiez, il reçoit</h3><p>Avec vos transporteurs habituels. Le délai de test démarre à la livraison.</p></li>
<li><span class="v2-mono">Après livraison</span><h3>Le testeur utilise</h3><p>Il garde le produit, quelle que soit sa note. Avitime le relance pour vous.</p></li>
<li><span class="v2-mono">J+14 à J+30</span><h3>L’avis arrive</h3><p>Sur votre fiche, avec note, limites, durée d’usage et mention du produit offert.</p></li>
</ol>
<div class="v2-shot">
<figure><video controls preload="none" playsinline poster="/assets/video/avitime-intro-poster.jpg" aria-label="Vidéo de présentation d’Avitime en six étapes"><source src="/assets/video/avitime-intro.mp4" type="video/mp4"></video></figure>
<div><h3 class="v2-h3">Avitime en 40 secondes</h3><p style="margin-top:8px">Le parcours complet en vidéo, de la campagne à l’avis publié sur votre fiche.</p><p>Le module publie les avis dans un format que Google et les assistants IA savent lire. Ce sont eux qui décident de les afficher : aucune étoile ni citation n’est promise.</p></div>
</div>
</div></section>

<section class="v2-band" id="prix"><div class="v2-w">
<h2 class="v2-h2">Combien coûte Avitime ? 5 tests offerts, puis un abonnement sans engagement</h2>
<p class="v2-lead" style="margin-top:14px">Vos 5 premiers tests sont offerts, sans abonnement ni carte bancaire : vous payez seulement le produit et le port. Ensuite, l’abonnement commence à 39,90 € HT par mois en annuel, ou 49,90 € HT par mois sans engagement.</p>
<div class="v2-scroll"><table class="v2-price-table">
<thead><tr><th>Offre</th><th>Unités de test / mois</th><th>Mensuel, sans engagement</th><th>Annuel, payé d’avance</th></tr></thead>
<tbody>
<tr><td>Premiers tests</td><td>5 au total</td><td>Offerts, sans carte bancaire</td><td>—</td></tr>
<tr><td>Starter</td><td>25</td><td>49,90 € HT/mois</td><td>39,90 € HT/mois (478,80 € HT/an)</td></tr>
<tr><td>Pro</td><td>60</td><td>74,90 € HT/mois</td><td>59,90 € HT/mois (718,80 € HT/an)</td></tr>
</tbody></table></div>
<p class="v2-next">Dans tous les cas, les produits et leur expédition restent à votre charge. <a href="/tarifs">Tous les détails et le calcul de votre campagne</a></p>
</div></section>

<section class="v2-band v2-route-band" id="integrations"><div class="v2-w">
<h2 class="v2-h2">Module d’avis clients pour PrestaShop, WooCommerce et Shopify</h2>
<p class="v2-lead" style="margin-top:14px">Avitime s’installe avec un module sur PrestaShop et une extension sur WooCommerce. L’application Shopify est en cours de validation par Shopify. Sans module, Avitime fonctionne aussi avec Systeme.io et les sites sur mesure.</p>
<ul class="v2-plat"><li>PrestaShop <small>module</small></li><li>WooCommerce <small>extension</small></li><li>Shopify <small>en cours de validation par Shopify</small></li><li>Systeme.io <small>sans module</small></li><li>Site sur mesure <small>sans module</small></li></ul>
<ul class="v2-list">
<li>Catalogue synchronisé automatiquement, variantes et stocks compris</li>
<li>Commandes testeurs à 0 € créées dans votre back-office</li>
<li>Suivi d’expédition transmis à Avitime et au testeur</li>
<li>Avis et étoiles affichés sur vos fiches produits</li>
</ul>
<p class="v2-next"><a href="/integrations">Voir le détail des intégrations</a></p>
<p class="v2-fine" style="margin-top:12px">Ces marques appartiennent à leurs propriétaires respectifs. Avitime est un service indépendant, qui n’est ni édité ni approuvé par eux.</p>
</div></section>

<section class="v2-band" id="commercants"><div class="v2-w">
<h2 class="v2-h2">Comment lancer un test produit depuis l’espace commerçant</h2>
<p class="v2-lead" style="margin-top:16px">Vous connectez votre boutique, créez une campagne, puis suivez chaque mission dans votre tableau de bord. Vous gardez vos produits, vos transporteurs et vos fiches produits.</p>
<ol class="v2-merchant">
<li><span class="v2-mono">01</span><h3 class="v2-h3">Connectez votre boutique</h3><p>Installez le module PrestaShop ou l’extension WooCommerce. Sur Shopify, l’application est en cours de validation par Shopify. Produits, variantes, stocks et images se synchronisent.</p></li>
<li><span class="v2-mono">02</span><h3 class="v2-h3">Créez une campagne</h3><p>Unités offertes, pays, délai de test, exclusions et dates. Le budget est affiché avant publication.</p></li>
<li><span class="v2-mono">03</span><h3 class="v2-h3">Suivez chaque mission</h3><p>Candidatures, commandes à 0 €, expéditions, avis et incidents, dans votre tableau de bord.</p></li>
<li><span class="v2-mono">04</span><h3 class="v2-h3">Lisez des chiffres honnêtes</h3><p>Unités livrées, missions terminées, avis publiés, note moyenne, coûts estimés.</p></li>
</ol>
<div class="v2-shots" id="apercu-espace">
<figure><img src="/assets/img/app/tableau-de-bord.webp" alt="Tableau de bord commerçant Avitime" width="1045" height="495" loading="lazy"><figcaption class="v2-fine" style="margin-top:7px">Le tableau de bord : campagnes, commandes testeurs, avis et visibilité Google et IA.</figcaption></figure>
<figure><img src="/assets/img/app/nouvelle-campagne.webp" alt="Création d’une campagne de test dans l’espace commerçant Avitime" width="610" height="495" loading="lazy"><figcaption class="v2-fine" style="margin-top:7px">Créer une campagne : un produit de votre catalogue, un nombre de testeurs, des centres d’intérêt.</figcaption></figure>
</div>
<p class="v2-fine" style="margin-top:10px">Captures réelles d’un compte de démonstration (nom et numéro d’entreprise modifiés).</p>
<div class="v2-links" style="margin-top:22px"><a class="v2-btn" href="/devenir-commercant">Créer mon espace commerçant</a><a href="https://cal.com/avitime/15min" target="_blank" rel="noopener">Voir l’outil avec nous : appel de 15 min</a></div>
</div></section>

<section class="v2-band v2-route-band" id="obtenez"><div class="v2-w">
<h2 class="v2-h2">Où s’affichent les avis clients : fiches produits, Google et IA</h2>
<p class="v2-lead" style="margin-top:14px">Les avis s’affichent sur vos fiches produits. Ils sont aussi publiés dans un format que Google et les assistants IA savent lire, mais ce sont eux qui décident de les reprendre.</p>
<div class="v2-gains">
<article>
<div class="v2-fiche v2-gain-vis" aria-hidden="true"><b>Coussin renard</b><p class="v2-sm"><span class="v2-stars">★★★★★</span> 4,6/5 · 32 avis</p><div class="v2-review">« Tissu très doux, couleurs fidèles. »<span class="v2-mention">Produit offert pour test</span></div></div>
<h3 class="v2-h3">De vrais avis sur vos fiches</h3><p>Avec photos, points forts et points faibles, affichés automatiquement par le module.</p>
</article>
<article>
<div class="v2-fiche v2-gain-vis" aria-hidden="true"><p class="v2-sm">https://ma-boutique.fr › coussin-renard</p><b>Coussin renard – Déco douce pour le salon</b><p class="v2-sm"><span class="v2-stars">★★★★★</span> Note : 4,6 · 32 avis · 18,90 €</p></div>
<h3 class="v2-h3">Des fiches éligibles aux étoiles dans Google</h3><p>Le module fournit les données. C’est Google qui décide de les afficher sous le lien bleu.</p>
</article>
<article>
<div class="v2-fiche v2-gain-vis" aria-hidden="true"><p class="v2-sm"><i>Quel coussin renard choisir ?</i></p><p class="v2-sm" style="margin-top:6px">D’après les avis de testeurs vérifiés, le Coussin renard de Ma Boutique est apprécié pour son tissu doux…</p></div>
<h3 class="v2-h3">Des avis lisibles par les IA</h3><p>Des avis structurés que les assistants IA peuvent reprendre dans leurs réponses, sans garantie de citation.</p>
</article>
</div>
<p class="v2-fine" style="margin-top:14px">Exemples illustratifs : boutique, produit, note et réponse fictifs. <a href="/pourquoi-faire-tester-vos-produits#avis-google-ia">Avis, Google et IA : le détail</a></p>
</div></section>

<section class="v2-band v2-dark" id="pub-ou-avis"><div class="v2-w">
<h2 class="v2-h2">Publicité ou <span class="v2-grad">avis clients</span> : où investir pour votre boutique en ligne ?</h2>
<p class="v2-lead" style="margin-top:14px">Les publicités amènent des visiteurs tant que vous payez. Les avis restent sur vos fiches et continuent de rassurer sur le long terme.</p>
<div class="v2-duo">
<article class="v2-box v2-box-outline">
<h3 class="v2-h3">La publicité seule : un robinet qu’il faut payer en continu</h3>
<ul class="v2-list">
<li><b>Chaque clic se paie</b>, et les enchères montent avec la concurrence.</li>
<li><b>Budget coupé, trafic coupé</b> : le jour où vous arrêtez, les visites s’arrêtent net.</li>
<li><b>Des clics qui n’achètent pas</b> : sans avis, une grande partie du trafic payé repart sans commander.</li>
<li><b>Des règles qui changent sans prévenir</b> : prix, ciblage, algorithmes, vous dépendez des plateformes.</li>
</ul>
</article>
<article class="v2-box v2-box-white">
<h3 class="v2-h3">Les avis vérifiés : un acquis qui dure</h3>
<ul class="v2-list">
<li><b>Ils restent sur vos fiches</b> et continuent de rassurer chaque visiteur, mois après mois.</li>
<li><b>Ils rentabilisent vos pubs</b> : avec des avis, plus de visiteurs passent à l’achat, y compris ceux qui viennent de la pub.</li>
<li><b>Google et les IA peuvent les lire</b> : de vraies expériences de clients, c’est le « E » d’Expérience des critères E‑E‑A‑T de Google.</li>
<li><b>Un investissement qui dure</b> : ce que vous mettez en place aujourd’hui travaille encore dans un an.</li>
</ul>
<div class="v2-links" style="margin-top:16px"><a class="v2-btn alt" href="/devenir-commercant">Obtenir de vrais avis</a></div>
</article>
</div>
<p class="v2-fine" style="margin-top:14px">Les avis ne remplacent pas toute publicité et ne garantissent aucun classement : ils rendent chaque visite plus utile. <a href="/pourquoi-faire-tester-vos-produits#pub-ou-avis">Le comparatif en détail</a></p>
</div></section>

<section class="v2-band v2-law" id="loi"><div class="v2-w">
<h2 class="v2-h2">Acheter des avis ou publier de faux avis : que dit la loi ?</h2>
<p class="v2-lead" style="margin-top:14px">En France, publier ou faire publier de faux avis est une pratique commerciale trompeuse, punie au maximum de 2 ans d’emprisonnement et de 300 000 € d’amende. Faire tester un produit reste possible, à condition de le dire clairement.</p>
<div class="v2-law-nums"><div><b>300 000 €</b><span>d’amende au maximum</span></div><div><b>2 ans</b><span>d’emprisonnement au maximum</span></div><div><b>10 %</b><span>du chiffre d’affaires annuel moyen, plafond possible de l’amende</span></div></div>
<div class="v2-law-grid">
<div><h3 class="v2-h3">Ce qui est interdit</h3><ul><li>Publier de faux avis, ou les faire publier.</li><li>Se faire passer pour un consommateur.</li><li>Présenter des avis comme vérifiés sans les vérifier.</li><li>Cacher qu’un avis a été obtenu contre un avantage.</li></ul></div>
<div><h3 class="v2-h3">Ce que fait Avitime</h3><ul><li>Une vraie commande et une livraison tracées pour chaque avis.</li><li>Des testeurs sélectionnés par Avitime, jamais par la boutique.</li><li>Toutes les notes de 1 à 5 publiées, si l’avis est authentique.</li><li>La mention « Produit offert pour test » sur chaque avis.</li></ul></div>
</div>
<p class="v2-fine" style="margin-top:24px"><a href="/a-propos.html#methode">Notre méthode de vérification</a>. Source : DGCCRF, Code de la consommation, art. L.121-2 à L.121-4. Ces informations ne constituent pas un conseil juridique.</p>
</div></section>

<section class="v2-band v2-route-band" id="pour-qui"><div class="v2-w">
<h2 class="v2-h2">Quelles boutiques en ligne peuvent faire tester leurs produits ?</h2>
<p class="v2-lead" style="margin-top:14px">Toute boutique en ligne qui livre en France, à condition que le produit testé soit exactement celui que reçoivent ses clients.</p>
<div class="v2-grid3">
<article><h3 class="v2-h3">Boutiques multi-produits</h3><p>Faites tester vos best-sellers ou vos nouveautés, campagne par campagne.</p></article>
<article><h3 class="v2-h3">Marques mono-produit</h3><p>Plusieurs testeurs aux profils variés, et une fiche produit qui rassure enfin.</p></article>
<article><h3 class="v2-h3">Dropshipping</h3><p>Le testeur commande comme un client, votre fournisseur expédie. Le délai d’avis démarre à la livraison.</p></article>
<article><h3 class="v2-h3">Créateurs et artisans</h3><p>Fait main, petites séries, produits locaux : de vrais retours pour prouver la qualité de votre travail.</p></article>
<article><h3 class="v2-h3">Boutiques qui démarrent</h3><p>Vos premiers avis dès les premières semaines, sans attendre les premières ventes.</p></article>
<article><h3 class="v2-h3">Produits numériques</h3><p>Formations, logiciels, e-books : le testeur reçoit ses accès, et son avis s’ouvre après une vraie période d’utilisation. <a href="/produits-numeriques">Le détail</a></p></article>
</div>
<p class="v2-fine" style="margin-top:16px">Catégories sensibles (santé, compléments, nicotine, alcool, produits pour mineurs…) : politique d’éligibilité stricte.</p>
</div></section>

<section class="v2-band" id="fondateur"><div class="v2-w v2-split">
<div><h2 class="v2-h2">Qui est derrière Avitime ?</h2></div>
<div>
<p class="v2-lead">Mon métier, c’est de créer des sites web pour des commerçants : plus d’une trentaine depuis 2020. Au lancement, le même problème revenait à chaque fois : zéro avis. J’ai créé Avitime pour casser ce cercle honnêtement.</p>
<p class="v2-sign">Cyril Quémy, fondateur</p>
<p style="margin-top:14px">Avitime est édité par SPARKMOTION AGENCY LTD, société anglaise (Companies House n° 16880032) dirigée par son fondateur.</p>
<p style="margin-top:14px">Nous démarrons : les premiers avis de commerçants arriveront avec les premières campagnes, sans faux témoignages en attendant. En attendant, vous pouvez lire <a href="/guides/etude-seo-petites-boutiques-2026.html">notre étude sur 73 petites boutiques</a> ou <a href="https://cal.com/avitime/15min" target="_blank" rel="noopener">réserver un appel de 15 minutes</a>.</p>
</div>
</div></section>
<!--# include virtual="/_avis-avitime" -->

<section class="v2-band v2-route-band" id="faq"><div class="v2-w">
<h2 class="v2-h2">Questions fréquentes sur les avis clients et les tests produits</h2>
<div class="v2-faq">
{faq_html}
</div>
<p class="v2-next"><a href="/faq">Toutes les questions</a></p>
</div></section>

<section class="v2-tester"><div class="v2-w v2-tester-in"><p><b>Vous voulez tester des produits ?</b> Inscription gratuite, le produit reste à vous.</p><a class="v2-btn v2-btn-tester" href="/devenir-testeur">Devenir testeur</a></div></section>

<section class="v2-band v2-final"><div class="v2-w">
<h2 class="v2-h2">Audit SEO gratuit de votre boutique en ligne</h2>
<p class="v2-lead" style="margin-top:14px">Votre score et vos 5 priorités en 1 à 3 minutes. Vous décidez ensuite de lancer vos tests ou non.</p>
<div class="v2-links"><a class="v2-btn alt" href="#audit">Auditer ma boutique</a><a href="/devenir-commercant">Créer mon espace commerçant</a></div>
</div></section>
</main>
'''
STICKY = '''<div class="m-sticky" id="m-sticky" aria-label="Accès rapide" hidden><a class="ms-m" href="#audit">Audit gratuit</a><a class="ms-t" href="/devenir-testeur">Devenir testeur</a></div>
<style>.m-sticky{display:none}@media (max-width:720px){.m-sticky{position:fixed;left:12px;right:12px;bottom:calc(12px + env(safe-area-inset-bottom));z-index:60;display:flex;gap:8px;padding:8px;background:#14110D;font-family:"Archivo",sans-serif;font-weight:800;font-size:15px;transition:opacity .2s,visibility .2s;opacity:0;visibility:hidden}.m-sticky.on{opacity:1;visibility:visible}.m-sticky a{flex:1;text-align:center;padding:11px 8px;text-decoration:none}.m-sticky .ms-m{background:var(--hl-grad,#F98C07);color:#14110D}.m-sticky .ms-t{background:#FFFDF8;color:#14110D}}</style>
<script>(function(){var b=document.getElementById("m-sticky"),h=document.getElementById("accueil"),f=document.querySelector("footer");if(!b||!h||!("IntersectionObserver" in window))return;b.hidden=false;var past=false,foot=false;function u(){b.classList.toggle("on",past&&!foot)}new IntersectionObserver(function(e){past=!e[0].isIntersecting;u()}).observe(h);if(f)new IntersectionObserver(function(e){foot=e[0].isIntersecting;u()}).observe(f)})();</script>
'''

alt = '<link rel="alternate" hreflang="fr" href="https://avitime.fr/">\n<link rel="alternate" hreflang="en" href="https://avitime.fr/en/">\n<link rel="alternate" hreflang="x-default" href="https://avitime.fr/">\n'
lang = '<a class="lang" href="/en/" hreflang="en" lang="en">EN</a>\n'
index = (tete("Avitime : tests produits et vrais avis clients pour e-commerce",
              "Aucun avis sur vos fiches ? Faites tester vos produits par de vrais testeurs, avec la mention du produit offert. 5 premiers tests offerts, sans abonnement.",
              "https://avitime.fr/", jsonld(ld_org) + jsonld(ld_faq), alternates=alt)
         + header(cta="#audit", lang=lang) + "\n" + ACCUEIL + FOOTER + "\n" + STICKY + SCRIPT_FORM + SCRIPT_ANIM + "</body>\n</html>\n")
(PUBLIC / "index.html").write_text(typo(index), encoding="utf-8", newline="")

# --- Tarifs ---
ld_tarifs = {"@context": "https://schema.org", "@graph": [
    {"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Accueil", "item": "https://avitime.fr/"},
        {"@type": "ListItem", "position": 2, "name": "Tarifs", "item": "https://avitime.fr/tarifs"}]},
    {"@type": "Service", "name": "Tests produits Avitime pour boutiques en ligne", "serviceType": "Tests produits et avis de testeurs",
     "url": "https://avitime.fr/tarifs", "areaServed": "FR", "provider": {"@type": "Organization", "name": "Avitime", "url": "https://avitime.fr/"},
     "offers": [
        {"@type": "Offer", "name": "Starter mensuel", "price": "49.90", "priceCurrency": "EUR", "url": "https://avitime.fr/tarifs"},
        {"@type": "Offer", "name": "Pro mensuel", "price": "74.90", "priceCurrency": "EUR", "url": "https://avitime.fr/tarifs"}]}]}
TARIFS = '''<main id="contenu">
<section class="v2-page-head"><div class="v2-w">
<h1 class="v2-h1">Tarifs Avitime</h1>
<p class="v2-lead">Vos 5 premiers tests sont offerts, sans abonnement ni carte bancaire. Ensuite, vous choisissez une formule si vous voulez continuer. Les produits et leur expédition restent toujours à votre charge.</p>
<div class="v2-links" style="margin-top:20px"><a class="v2-btn" href="/devenir-commercant">Lancer mes 5 tests offerts</a><a href="/audit-seo">Commencer par l’audit gratuit</a></div>
</div></section>

<section class="v2-band"><div class="v2-w">
<h2 class="v2-h2">Les formules</h2>
<div class="v2-scroll"><table class="v2-price-table">
<thead><tr><th>Offre</th><th>Unités de test / mois</th><th>Mensuel, sans engagement</th><th>Annuel, payé d’avance</th></tr></thead>
<tbody>
<tr><td>Premiers tests</td><td>5 au total, par boutique</td><td>Offerts, sans carte bancaire</td><td>—</td></tr>
<tr><td>Starter</td><td>25</td><td>49,90 € HT/mois</td><td>478,80 € HT/an, soit 39,90 € HT/mois</td></tr>
<tr><td>Pro</td><td>60</td><td>74,90 € HT/mois</td><td>718,80 € HT/an, soit 59,90 € HT/mois</td></tr>
</tbody></table></div>
<ul class="v2-list">
<li><b>Une unité de test</b> est un exemplaire de produit attribué à un testeur et effectivement commandé à 0 €. Ce n’est pas un avis garanti.</li>
<li><b>Les unités non utilisées</b> au cours d’un mois ne sont pas reportées sur le mois suivant.</li>
<li><b>La formule mensuelle</b> est résiliable à tout moment, avec effet à la fin du mois en cours.</li>
<li><b>La formule annuelle</b> est payée d’avance et reconduite sauf résiliation au plus tard 30 jours avant son échéance. Le montant payé reste acquis en cas de résiliation en cours d’année, sauf manquement grave d’Avitime.</li>
<li><b>Une boutique par abonnement.</b> Sur Shopify, dès la validation de l’application, le paiement passera par la facturation Shopify.</li>
</ul>
<p class="v2-fine" style="margin-top:16px">Prix hors taxes. Ces informations résument les <a href="/cgv.html">conditions générales de vente</a>, qui font foi.</p>
</div></section>

<section class="v2-band v2-route-band"><div class="v2-w">
<h2 class="v2-h2">Le coût de votre campagne</h2>
<p class="v2-lead" style="margin-top:14px">Vos 5 premiers tests sont offerts. Le produit et le port restent à payer pour chaque testeur.</p>
<form class="v2-calc" id="calcul" onsubmit="return false" aria-label="Estimer le coût de la campagne">
<label><span>Testeurs</span><input id="c-n" type="number" min="1" max="60" step="1" value="5" inputmode="numeric"></label>
<label><span>Coût du produit (€)</span><input id="c-p" type="number" min="0" step="0.5" value="12" inputmode="decimal"></label>
<label><span>Expédition par colis (€)</span><input id="c-e" type="number" min="0" step="0.5" value="6" inputmode="decimal"></label>
<label class="v2-calc-out"><span>Estimation produits + port</span><output id="c-t" for="c-n c-p c-e">90,00 €</output></label>
</form>
<p class="v2-fine" style="margin-top:12px">Estimation à titre indicatif, hors abonnement éventuel. Le budget exact de la campagne est affiché avant sa publication. Aucun volume d’avis n’est garanti.</p>
</div></section>

<section class="v2-band"><div class="v2-w">
<h2 class="v2-h2">Ce que vous ne payez jamais</h2>
<ul class="v2-list">
<li>Une note : demander une bonne note ou proposer une contrepartie est interdit.</li>
<li>Les testeurs : ils ne sont pas rémunérés. Ils reçoivent le produit et le gardent, quelle que soit leur note.</li>
<li>Un engagement pour vos 5 premiers tests, ni un code promo : l’offre s’applique automatiquement à votre première campagne.</li>
</ul>
<p class="v2-next">Une question ? <a href="https://cal.com/avitime/15min" target="_blank" rel="noopener">Réservez un appel de 15 minutes</a> ou <a href="/contact">écrivez-nous</a>.</p>
</div></section>
</main>
'''
SCRIPT_CALC = '''<script>(function(){var g=function(i){return document.getElementById(i)},v=function(i){var x=parseFloat(g(i).value);return isNaN(x)||x<0?0:x},m=function(){var t=v("c-n")*(v("c-p")+v("c-e"));g("c-t").textContent=t.toLocaleString("fr-FR",{minimumFractionDigits:2,maximumFractionDigits:2})+" €"};["c-n","c-p","c-e"].forEach(function(i){g(i).addEventListener("input",m)});m()})();</script>
'''
tarifs = (tete("Tarifs Avitime : 5 tests offerts, puis dès 39,90 € HT/mois",
               "Les prix d’Avitime : 5 premiers tests offerts, Starter et Pro en mensuel sans engagement ou en annuel. Produits et expédition restent à la charge de la boutique.",
               "https://avitime.fr/tarifs", jsonld(ld_tarifs))
          + header(courant="/tarifs") + "\n" + TARIFS + FOOTER + "\n" + SCRIPT_CALC + SCRIPT_ANIM + "</body>\n</html>\n")
(PUBLIC / "tarifs.html").write_text(typo(tarifs), encoding="utf-8", newline="")

# --- Pourquoi faire tester : l'ancien contenu détaillé de l'accueil ---
PQ_URL = "https://avitime.fr/pourquoi-faire-tester-vos-produits"
ld_pq = {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
    {"@type": "ListItem", "position": 1, "name": "Accueil", "item": "https://avitime.fr/"},
    {"@type": "ListItem", "position": 2, "name": "Pourquoi faire tester vos produits", "item": PQ_URL}]}
pq = (tete("Pourquoi faire tester vos produits : avis, Google et IA | Avitime",
           "Premiers avis, étoiles Google, assistants IA, publicité, loi sur les faux avis : ce que change un vrai test produit pour une boutique en ligne.",
           PQ_URL, jsonld(ld_pq))
      + header() + "\n" + (RACINE / "tools" / "pages" / "pourquoi.main.html").read_text(encoding="utf-8") + FOOTER + "\n" + SCRIPT_ANIM + "</body>\n</html>\n")
(PUBLIC / "pourquoi-faire-tester-vos-produits.html").write_text(typo(pq), encoding="utf-8", newline="")

# --- 404 ---
P404 = '''<main id="contenu"><section class="v2-404"><div class="v2-w">
<h1 class="v2-h1">Page introuvable</h1>
<p class="v2-lead">Cette adresse n’existe pas ou a changé. Vous pouvez repartir d’ici :</p>
<div class="v2-links"><a class="v2-btn" href="/">Retour à l’accueil</a><a href="/audit-seo">Audit SEO gratuit</a><a href="/tarifs">Tarifs</a><a href="/guides/">Guides</a><a href="/contact">Contact</a></div>
</div></section></main>
'''
p404 = (tete("Page introuvable | Avitime", "Cette page n’existe pas ou a changé d’adresse.", "", "", robots="noindex")
        + header() + "\n" + P404 + FOOTER + "\n</body>\n</html>\n")
(PUBLIC / "404.html").write_text(p404, encoding="utf-8", newline="")
print("accueil, tarifs, page pourquoi et 404 générés")
