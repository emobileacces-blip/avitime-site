"""Construit /commercants et /integrations à partir du gabarit faq.html (en-tête, pied, styles).
Usage : python3 tools/pages/build.py   (depuis avitime-site/)"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PUB = ROOT / "public"
HERE = Path(__file__).resolve().parent
tpl = (PUB / "faq.html").read_text()
guide = (PUB / "guides/premiers-avis-clients.html").read_text()
a = guide.index('<div class="lead-card" id="guide">')
b = guide.index("</script>", a) + len("</script>")
LEAD = guide[a:b]

CSS = """<style>
.pg-ctas{display:flex;flex-wrap:wrap;gap:12px 20px;align-items:center;margin:28px 0 0}
.pg-ctas .btn{text-decoration:none}
.pg-sec{font-weight:600;color:var(--hl-ink);text-decoration:underline;text-underline-offset:3px}
.pg-pill{margin:18px 0 0}
.pg-pill a{display:inline-block;background:var(--surface);border:1px solid var(--line);border-radius:999px;padding:8px 16px;font-size:14.5px;font-weight:600;color:var(--ink);text-decoration:none}
.pg-pill a:hover{border-color:var(--hl)}
.gd-body .pg-steps{gap:12px}
.pg-fig{margin:22px 0 0}
.pg-fig img{width:100%;height:auto;display:block;border-radius:18px;border:1px solid var(--line);box-shadow:0 18px 50px rgba(0,0,0,.12)}
.pg-fig-sm{max-width:520px}
.pg-fig figcaption{font-size:14px;color:var(--ink-2);margin-top:8px}
.pg-video{margin:0 auto 36px;max-width:360px}
.pg-video video{width:100%;aspect-ratio:9/16;display:block;border-radius:22px;background:#0A0A0A;box-shadow:0 30px 70px -40px rgba(0,0,0,.6)}
.pg-video figcaption{font-size:14px;color:var(--ink-2);text-align:center;margin-top:10px}
.pg-video-wide{max-width:none;margin:22px 0 28px}
.pg-video-wide video{aspect-ratio:16/9;border-radius:18px}
</style>
"""

PAGES = {
    "commercants": {
        "title": "Faire tester vos produits par de vrais consommateurs | Avitime",
        "desc": "Boutiques en ligne : faites tester vos produits par des consommateurs sélectionnés, à 0 € sur votre boutique, et obtenez des avis vérifiés, légalement.",
        "crumb": "Pour les boutiques",
        "video": {"@type": "VideoObject", "name": "Vous cramez votre budget pub ? Les avis clients, le chaînon manquant",
                  "description": "Cyril, fondateur d’Avitime, explique pourquoi une boutique sans avis clients gaspille son budget publicitaire et comment obtenir ses premiers avis vérifiés en faisant tester ses produits.",
                  "thumbnailUrl": "https://avitime.fr/assets/video/commercants-budget-poster.jpg",
                  "contentUrl": "https://avitime.fr/assets/video/commercants-budget.mp4",
                  "uploadDate": "2026-10-26T12:00:00+01:00", "duration": "PT1M53S", "inLanguage": "fr-FR"},
        "video2": {"@type": "VideoObject", "name": "De l’audit SEO gratuit à vos premiers avis clients : la démo pas à pas",
                  "description": "Démonstration filmée de l’espace commerçant Avitime : lancer l’audit SEO gratuit, lire le score, les 3 piliers (SEO, GEO, E-E-A-T) et les 5 priorités, puis créer une campagne de test produit (choix du produit, centres d’intérêt, nombre de testeurs). Avitime sélectionne les testeurs.",
                  "thumbnailUrl": "https://avitime.fr/assets/video/tuto-audit-premier-test-poster.jpg",
                  "contentUrl": "https://avitime.fr/assets/video/tuto-audit-premier-test.mp4",
                  "uploadDate": "2026-10-30T12:30:00+01:00", "duration": "PT2M10S", "inLanguage": "fr-FR"},
    },
    "audit-seo": {
        "title": "Audit SEO gratuit de votre boutique en ligne | Avitime",
        "desc": "Audit SEO gratuit pour Shopify, PrestaShop et WooCommerce : score sur 100, fiches produits, maillage interne, avis clients et plan d’action clair.",
        "crumb": "Audit SEO",
        "faq": True,
    },
    "integrations": {
        "title": "Module avis clients PrestaShop, WooCommerce et Shopify | Avitime",
        "desc": "Le module Avitime pour PrestaShop, l’extension WooCommerce et l’application Shopify : commandes testeurs à 0 €, suivi et avis vérifiés sur vos fiches.",
        "crumb": "Intégrations",
    },
}

head_end = tpl.index("</head>")
body_start = tpl.index("<main id=\"contenu\">")
main_end = tpl.index("</main>")

for slug, p in PAGES.items():
    url = f"https://avitime.fr/{slug}"
    head = tpl[:head_end]
    head = re.sub(r'<script type="application/ld\+json">.*?</script>\n?', "", head, flags=re.S)
    head = re.sub(r"<title>.*?</title>", f"<title>{p['title']}</title>", head)
    head = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{p["desc"]}">', head)
    head = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{p["title"]}">', head)
    head = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{p["desc"]}">', head)
    head = head.replace('href="https://avitime.fr/faq"', f'href="{url}"').replace('content="https://avitime.fr/faq"', f'content="{url}"')
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebPage", "@id": url + "#page", "url": url, "name": p["title"], "description": p["desc"], "inLanguage": "fr-FR",
         "publisher": {"@type": "Organization", "name": "Avitime", "url": "https://avitime.fr/"}},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Accueil", "item": "https://avitime.fr/"},
            {"@type": "ListItem", "position": 2, "name": p["crumb"], "item": url}]}]}
    for vk in ("video", "video2"):
        if p.get(vk):
            ld["@graph"].append(p[vk])
    if p.get("faq"):
        # FAQPage tirée des <details> de la page (questions / réponses visibles, sans HTML).
        src = (HERE / f"{slug}.main.html").read_text()
        qa = re.findall(r"<details><summary>(.*?)</summary><p>(.*?)</p></details>", src, flags=re.S)
        txt = lambda h: re.sub(r"\s+", " ", re.sub(r"<[^>]+>", "", h).replace("&nbsp;", "\u00a0").replace("&amp;", "&")).strip()
        ld["@graph"].append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": txt(q), "acceptedAnswer": {"@type": "Answer", "text": txt(a)}} for q, a in qa]})
    head += CSS + '<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + "</script>\n"
    main = (HERE / f"{slug}.main.html").read_text().replace("[[LEAD]]", LEAD)
    foot = tpl[main_end:]
    foot = re.sub(r'<script type="application/ld\+json">.*?</script>\n?', "", foot, flags=re.S)
    html = head + tpl[head_end:body_start] + '<main id="contenu">\n' + main + "\n" + foot
    (PUB / f"{slug}.html").write_text(html)
    print("ok", slug, len(html))
