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
