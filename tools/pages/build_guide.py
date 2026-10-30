"""Construit un guide à partir d'un guide déjà en ligne (gabarit : en-tête, pied de page, signature à jour).
Les guides en ligne ont été retouchés après make_guides.py : ne PAS relancer make_guides.py, utiliser ce script
pour les nouveaux guides.
Usage : python3 tools/pages/build_guide.py   (depuis avitime-site/)"""
import json
import sys
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PUB = ROOT / "public"
HERE = Path(__file__).resolve().parent
SHELL = (PUB / "guides/geo-seo.html").read_text()
INDEX = (PUB / "guides/index.html").read_text()

AUTHOR = {"@type": "Person", "@id": "https://avitime.fr/a-propos.html#fondateur", "name": "Cyril Quémy", "jobTitle": "Fondateur d’Avitime", "url": "https://avitime.fr/a-propos.html#fondateur"}
PUBLISHER = {"@type": "Organization", "name": "Avitime", "url": "https://avitime.fr/", "logo": {"@type": "ImageObject", "url": "https://avitime.fr/assets/img/icon-512.png"}}

GUIDES = [{
    "slug": "audit-seo-boutique-en-ligne",
    "body": "guide-audit-seo.body.html",
    "seo_title": "Audit SEO d’une boutique en ligne : les 9 points à vérifier",
    "seo_desc": "Avis clients, fiches produits, technique, E-E-A-T, maillage interne, backlinks : les 9 points d’un audit SEO de boutique en ligne, avec les sources de Google.",
    "title": "Audit SEO d’une boutique en ligne : les 9 points à vérifier (2026)",
    "desc": "Les 9 points d’un audit SEO de boutique en ligne, du plus négligé (avis clients, maillage interne) au plus technique, avec ce que dit Google.",
    "topic": "Référencement",
    "lede": "Votre boutique est en ligne, mais Google et les assistants IA la voient-ils vraiment&nbsp;? Voici les 9 points qu’un audit SEO doit passer en revue, expliqués simplement et sources à l’appui, avec ce qu’il faut corriger en premier.",
    "pub_iso": "2026-10-28", "pub_fr": "28 octobre 2026", "read": 10,
    "related": ["seo-site-ne-decolle-pas", "referencement-boutique-en-ligne", "eeat-e-commerce"],
}, {
    "slug": "video-testeur-produit",
    "body": "guide-video-testeur.body.html",
    "seo_title": "Vidéo de test produit : comment la faire et la publier",
    "seo_desc": "Testeurs : tourner une vidéo de test produit en 60 secondes, la mention « Collaboration commerciale » obligatoire, les points gagnés et ce que la boutique peut en faire.",
    "title": "Vidéo de test produit : comment la faire et la publier (2026)",
    "desc": "Tourner une courte vidéo de test produit, la publier sur TikTok, Instagram ou YouTube avec la mention obligatoire, et ce que la boutique peut en faire.",
    "topic": "Testeurs",
    "lede": "Vous testez un produit et vous voulez le montrer en vidéo&nbsp;? Voici comment tourner une vidéo utile en 60 secondes, la mention que la loi impose quand le produit est offert, et ce que cette vidéo vous rapporte, à vous comme à la boutique.",
    "pub_iso": "2026-10-28", "pub_fr": "28 octobre 2026", "read": 7,
    "related": ["testeur-de-produit", "tester-produits-a-domicile", "faux-avis-loi"],
}, {
    "slug": "alternative-avis-verifies-trustpilot",
    "body": "guide-alternative-av-tp.body.html",
    "seo_title": "Alternative à Avis Vérifiés et Trustpilot : comparatif 2026",
    "seo_desc": "Avis Vérifiés, Trustpilot, avis Google, Bazaarvoice ou testeurs : prix publics, méthode de collecte, conformité et la bonne alternative pour une petite boutique.",
    "title": "Alternative à Avis Vérifiés et Trustpilot : le comparatif pour les e-commerçants (2026)",
    "desc": "Prix, méthode de collecte et limites d’Avis Vérifiés, Trustpilot, des avis Google et de Bazaarvoice, et l’alternative pour obtenir ses premiers avis sans ventes.",
    "topic": "Comparatif",
    "lede": "Avis Vérifiés et Trustpilot sont les deux noms qui reviennent quand on veut des avis clients. Mais sont-ils adaptés à une boutique qui démarre&nbsp;? Prix publics, méthode de collecte, conformité&nbsp;: voici le comparatif des principales solutions, et l’alternative quand vos fiches affichent encore zéro avis.",
    "pub_iso": "2026-10-30", "pub_fr": "30 octobre 2026", "read": 9,
    "related": ["comparatif-solutions-avis-clients", "premiers-avis-clients", "faux-avis-loi"],
}, {
    "slug": "directive-omnibus-avis-clients",
    "body": "guide-omnibus.body.html",
    "seo_title": "Directive Omnibus et avis clients : obligations 2026",
    "seo_desc": "Faux avis, avis supprimés, contrepartie, informations à afficher : ce que la directive Omnibus interdit et impose aux e-commerçants, textes de loi à l’appui.",
    "title": "Directive Omnibus et avis clients : ce que chaque e-commerçant doit savoir (2026)",
    "desc": "Ce que la directive Omnibus interdit (faux avis, avis déformés) et impose aux e-commerçants pour leurs avis clients, avec les textes de référence.",
    "topic": "Juridique",
    "lede": "Depuis le 28&nbsp;mai 2022, la directive Omnibus encadre strictement les avis clients en ligne. Qu’est-ce qui est interdit, qu’est-ce qui est obligatoire, et comment collecter des avis efficaces et conformes&nbsp;? Le point, textes de loi à l’appui.",
    "pub_iso": "2026-10-30", "pub_fr": "30 octobre 2026", "read": 10,
    "related": ["faux-avis-loi", "alternative-avis-verifies-trustpilot", "premiers-avis-clients"],
}, {
    "slug": "obtenir-avis-clients-boutique-en-ligne",
    "body": "guide-obtenir-avis.body.html",
    "seo_title": "Obtenir des avis clients rapidement : méthodes et outils",
    "seo_desc": "E-mail après livraison, SMS, encart colis, relance, communauté, testeurs : 6 méthodes pour obtenir des avis clients rapidement, et ce que la loi interdit.",
    "title": "Obtenir des avis clients rapidement : toutes les méthodes pour votre boutique en ligne (2026)",
    "desc": "Six méthodes pour obtenir des avis clients rapidement sur une boutique en ligne, quelle méthode selon votre situation, et les pratiques interdites.",
    "topic": "E-commerce",
    "lede": "Comment obtenir des avis clients rapidement quand on démarre, qu’on lance un nouveau produit ou que ses fiches affichent encore zéro étoile&nbsp;? Voici les six méthodes disponibles en 2026, leurs vraies limites et les erreurs à éviter pour rester dans les règles.",
    "pub_iso": "2026-10-30", "pub_fr": "30 octobre 2026", "read": 11,
    "related": ["premiers-avis-clients", "demander-avis-client", "combien-avis-clients"],
}, {
    "slug": "preuve-sociale-ecommerce-conversions",
    "body": "guide-preuve-sociale.body.html",
    "seo_title": "Preuve sociale e-commerce : boostez vos conversions",
    "seo_desc": "Avis, photos clients, labels, étoiles dans Google : comment la preuve sociale agit à chaque étape du parcours d’achat, et comment la construire quand on démarre.",
    "title": "Preuve sociale en e-commerce : comment elle alimente votre parcours d’achat et augmente vos conversions (2026)",
    "desc": "Les formats de preuve sociale, leur rôle à chaque étape du parcours d’achat, les règles de la directive Omnibus et comment construire sa preuve sociale quand on démarre.",
    "topic": "Marketing",
    "lede": "Avis, photos de clients, étoiles dans Google, labels&nbsp;: la preuve sociale pèse sur chaque étape du parcours d’achat. Voici ce qu’elle est, les formats qui fonctionnent, ce que la loi impose, et comment la construire quand votre boutique démarre.",
    "pub_iso": "2026-10-30", "pub_fr": "30 octobre 2026", "read": 12,
    "related": ["avis-clients-ia", "obtenir-avis-clients-boutique-en-ligne", "statistiques-avis-clients"],
}, {
    "slug": "plateformes-avis-clients-pme-comparatif",
    "body": "guide-pme.body.html",
    "seo_title": "Plateformes d’avis clients pour PME : prix et comparatif 2026",
    "seo_desc": "Découvrez les plateformes d’avis clients adaptées aux PME en 2026 : comparatif honnête des tarifs, des fonctionnalités et des alternatives à Trustpilot.",
    "title": "Plateformes d’avis clients pour PME : le comparatif des prix et des solutions (2026)",
    "desc": "Prix publics, engagement, collecte active ou passive : Société des Avis Garantis, Avis Vérifiés, Trustpilot, Custplace, Guest Suite, Partoo, avis Google et Avitime comparés pour une PME.",
    "topic": "Comparatif",
    "lede": "Trustpilot, Avis Vérifiés, Société des Avis Garantis…&nbsp;: quelle plateforme d’avis clients choisir quand on est une PME ou une boutique indépendante&nbsp;? Prix publics, engagement, ce que chaque solution fait vraiment, et laquelle convient à votre situation.",
    "pub_iso": "2026-10-30", "pub_fr": "30 octobre 2026", "read": 12,
    "related": ["alternative-avis-verifies-trustpilot", "comparatif-solutions-avis-clients", "obtenir-avis-clients-boutique-en-ligne"],
}, {
    "slug": "etoiles-google-shopping-avis-produits",
    "body": "guide-etoiles-google.body.html",
    "seo_title": "Étoiles Google Shopping : comment les obtenir en 2026",
    "seo_desc": "Notes des produits, note du magasin, étoiles Schema.org : les conditions de Google (50 avis, GTIN, flux mensuel, 3,5/5) et comment afficher des étoiles sur vos produits.",
    "title": "Étoiles Google Shopping : comment les obtenir et les afficher sur vos produits (2026)",
    "desc": "Les conditions de Google pour afficher les notes des produits, la note du magasin et les étoiles des résultats naturels, et comment les obtenir en 6 étapes.",
    "topic": "Référencement",
    "lede": "Pourquoi certaines fiches affichent-elles des étoiles dans Google, et pas les vôtres&nbsp;? Notes des produits, note du magasin, balisage Schema.org&nbsp;: les conditions exactes de Google, les raisons les plus fréquentes d’absence, et comment obtenir vos étoiles en 6 étapes.",
    "pub_iso": "2026-10-30", "pub_fr": "30 octobre 2026", "read": 11,
    "related": ["obtenir-avis-clients-boutique-en-ligne", "referencement-boutique-en-ligne", "preuve-sociale-ecommerce-conversions"],
}, {
    "slug": "avis-clients-shopify-gratuit",
    "body": "guide-shopify-gratuit.body.html",
    "seo_title": "Avis clients Shopify sans application payante (2026)",
    "seo_desc": "Afficher des avis clients sur Shopify sans payer : les forfaits gratuits de Judge.me, Loox et Junip comparés, leurs limites (Google Shopping, volume) et comment obtenir vos premiers avis.",
    "title": "Avis clients sur Shopify sans application payante : ce qui est possible en 2026",
    "desc": "Shopify n’a plus d’outil d’avis gratuit depuis 2024. Les forfaits gratuits de Judge.me, Loox et Junip, ce qu’ils font, ce qu’ils ne font pas, et quand passer à autre chose.",
    "topic": "Shopify",
    "lede": "Peut-on afficher des avis clients sur Shopify sans payer d’application chaque mois&nbsp;? Oui, avec des limites. Ce que proposent vraiment les forfaits gratuits en 2026, ce qu’ils ne font pas, et comment obtenir vos premiers avis quand la boutique démarre.",
    "pub_iso": "2026-10-30", "pub_fr": "30 octobre 2026", "read": 11,
    "related": ["avis-clients-shopify", "obtenir-avis-clients-boutique-en-ligne", "etoiles-google-shopping-avis-produits"],
}, {
    "slug": "widget-avis-clients",
    "body": "guide-widget-avis.body.html",
    "seo_title": "Widget avis clients : choisir et installer le bon en 2026",
    "seo_desc": "Quel widget d’avis clients choisir pour votre boutique en ligne ? Ce qu’il doit afficher, les critères de choix, le comparatif et l’installation sur PrestaShop, WooCommerce et Shopify.",
    "title": "Widget d’avis clients : comment choisir et installer le bon sur votre boutique en ligne (2026)",
    "desc": "Ce qu’un widget d’avis doit afficher selon la loi, les critères de choix, le comparatif des solutions et l’installation sur PrestaShop, WooCommerce et Shopify.",
    "topic": "Avis clients",
    "lede": "Note moyenne, dates, mention des contreparties, avis négatifs, étoiles dans Google&nbsp;: ce qu’un widget d’avis clients doit afficher, comment le choisir, où le placer, et comment l’installer sur PrestaShop, WooCommerce et Shopify.",
    "pub_iso": "2026-10-30", "pub_fr": "30 octobre 2026", "read": 13,
    "related": ["avis-clients-shopify-gratuit", "directive-omnibus-avis-clients", "etoiles-google-shopping-avis-produits"],
}, {
    "slug": "avis-produit-numerique-formation-saas",
    "body": "guide-produit-numerique.body.html",
    "seo_title": "Avis sur une formation, un SaaS ou un outil IA : la méthode",
    "seo_desc": "Formation en ligne (trading, marketing…), logiciel, SaaS, outil d’IA, e-book : comment obtenir ses premiers avis vérifiés en faisant tester son produit numérique, légalement.",
    "title": "Avis sur une formation, un SaaS ou un outil d’IA : comment obtenir les premiers (2026)",
    "desc": "Faire tester son produit numérique par de vrais utilisateurs : accès offert, durée d’utilisation avant l’avis, obligations légales et cas des formations en trading.",
    "topic": "Produits numériques",
    "lede": "Une formation en ligne, un logiciel ou un outil d’IA ne se touche pas avant l’achat&nbsp;: les avis sont la première preuve que cherchent vos visiteurs. Comment obtenir les premiers sans les acheter, quel accès offrir, combien de temps avant l’avis, et ce que la loi impose.",
    "pub_iso": "2026-10-30", "pub_fr": "30 octobre 2026", "read": 9,
    "related": ["tester-formations-logiciels-gratuitement", "obtenir-avis-clients-boutique-en-ligne", "directive-omnibus-avis-clients"],
}, {
    "slug": "tester-formations-logiciels-gratuitement",
    "body": "guide-testeur-numerique.body.html",
    "seo_title": "Tester des formations et des logiciels gratuitement (2026)",
    "seo_desc": "Formations (trading, marketing, langues…), logiciels, SaaS, outils d’IA, e-books : comment les tester gratuitement, donner un avis utile et éviter les arnaques.",
    "title": "Tester des formations, des logiciels et des outils d’IA gratuitement (2026)",
    "desc": "Ce qu’on peut tester (formations, SaaS, IA, e-books), comment se passe un test de produit numérique, comment donner un avis utile et les pièges à éviter.",
    "topic": "Testeurs",
    "lede": "On ne teste pas seulement des produits reçus par la poste&nbsp;: formations en ligne, logiciels, outils d’IA et e-books se testent aussi gratuitement. Comment ça marche, ce qu’on attend de vous, et les fausses offres à éviter, en particulier dans le trading.",
    "pub_iso": "2026-10-30", "pub_fr": "30 octobre 2026", "read": 7,
    "related": ["avis-produit-numerique-formation-saas", "testeur-de-produit", "arnaques-testeur-produits"],
}]


def card(slug):
    m = re.search(r'<a class="gd-card" href="/guides/' + re.escape(slug) + r'\.html"><p class="eyebrow">(.*?)</p><h2>(.*?)</h2>', INDEX)
    assert m, slug
    return f'<a class="gd-card" href="/guides/{slug}.html"><p class="eyebrow">{m.group(1)}</p><h2>{m.group(2)}</h2></a>'


ONLY = set(sys.argv[1:])
for g in GUIDES:
    if ONLY and g["slug"] not in ONLY:
        continue
    path = f"/guides/{g['slug']}.html"
    url = "https://avitime.fr" + path
    h = SHELL
    h = re.sub(r"<title>.*?</title>", f"<title>{g['seo_title']}</title>", h, count=1)
    h = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{g["seo_desc"]}">', h, count=1)
    h = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{g["seo_title"]}">', h, count=1)
    h = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{g["seo_desc"]}">', h, count=1)
    h = h.replace("https://avitime.fr/guides/geo-seo.html", url)
    by = re.search(r'<div class="gd-by">.*?</div></div>|<div class="gd-by">.*?</p></div>', SHELL, flags=re.S).group(0)
    by = re.sub(r"Publié le [^<]*", f"Publié le {g['pub_fr']} · lecture {g['read']} min", by)
    related = ('<aside class="gd-related" aria-label="À lire aussi"><h2>À lire aussi</h2><div class="gd-cards">'
               + "".join(card(s) for s in g["related"]) + '</div><p style="margin-top:18px"><a href="/guides/">Tous les guides</a></p></aside>')
    article = ('<article>\n<section class="gd-hero"><div class="gd-wrap">\n'
               f'<p class="eyebrow"><a href="/guides/" style="color:inherit;text-decoration:none">Guides</a> · {g["topic"]}</p>\n'
               f'<h1>{g["title"]}</h1>\n<p class="gd-lede">{g["lede"]}</p>\n{by}\n</div></section>\n'
               f'<section class="gd-body"><div class="gd-wrap">{(HERE / g["body"]).read_text()}{related}</div></section>\n</article>')
    h = re.sub(r"<article>.*?</article>", lambda _m: article, h, count=1, flags=re.S)
    body = (HERE / g["body"]).read_text()
    qa = re.findall(r"<h3>(.*?)</h3>\s*<p>(.*?)</p>", body.split('id="faq"', 1)[1].split('id="sources"', 1)[0], flags=re.S)
    txt = lambda s: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", s).replace("&nbsp;", " ")).strip()
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "headline": g["title"], "description": g["desc"], "inLanguage": "fr-FR",
         "datePublished": g["pub_iso"], "dateModified": g["pub_iso"], "author": AUTHOR, "publisher": PUBLISHER,
         "mainEntityOfPage": url, "image": "https://avitime.fr/assets/img/og-image.jpg"},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Accueil", "item": "https://avitime.fr/"},
            {"@type": "ListItem", "position": 2, "name": "Guides", "item": "https://avitime.fr/guides/"},
            {"@type": "ListItem", "position": 3, "name": g["title"], "item": url}]},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": txt(q), "acceptedAnswer": {"@type": "Answer", "text": txt(a)}} for q, a in qa]}]}
    h = re.sub(r'<script type="application/ld\+json">.*?</script>', lambda _m: '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + "</script>", h, count=1, flags=re.S)
    (PUB / "guides" / f"{g['slug']}.html").write_text(h)
    print("ok", path, len(h), "faq", len(qa))
