#!/usr/bin/env python3
"""Corrections du site vitrine issues de l'audit du 6 novembre 2026 : menu, pied de page,
promesses, titres, robots et sitemap. Relançable sans effet de bord.

N'agit que sur le site vitrine : ni l'application, ni l'extension Shopify, ni le logo,
ni le contenu des pages légales.
"""
import re
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
PUBLIC = RACINE / "public"
MENU = [("/commercants", "Commerçants"), ("/audit-seo", "Audit SEO"), ("/tarifs", "Tarifs"),
        ("/integrations", "Intégrations"), ("/devenir-testeur", "Testeurs"), ("/faq", "FAQ"),
        ("/guides/", "Guides"), ("/a-propos.html", "À propos")]
COURANT = {"commercants.html": "/commercants", "audit-seo.html": "/audit-seo", "tarifs.html": "/tarifs",
           "integrations.html": "/integrations", "devenir-testeur.html": "/devenir-testeur", "faq.html": "/faq",
           "a-propos.html": "/a-propos.html"}


def menu(nom, dans_guides):
    actif = "/guides/" if dans_guides else COURANT.get(nom)
    liens = "\n".join(f'<a href="{u}"{" aria-current=\"page\"" if u == actif else ""}>{t}</a>' for u, t in MENU)
    return f'<nav aria-label="Navigation principale" class="nav-links">\n{liens}\n</nav>'


PILOTE_FR = ("Le pilote commence par des accessoires non réglementés. ",
             "Votre boutique doit livrer en France, et le produit testé doit être celui que reçoivent vos clients. ")
REMPLACEMENTS = [
    # Aucun volume d'avis garanti
    ("sans abonnement, pour cinq avis vérifiés publiés sur votre fiche.",
     "sans abonnement, pour cinq testeurs qui s’engagent à donner leur avis sur votre fiche. Aucun volume d’avis n’est garanti."),
    PILOTE_FR,
    ("<b>Produits&nbsp;:</b> le pilote commence par des accessoires non réglementés. Les catégories",
     "<b>Produits&nbsp;:</b> les catégories"),
    ("Produits : le pilote commence par des accessoires non réglementés. Les catégories", "Produits : les catégories"),
    # Prix visibles
    ("Ensuite, les offres et conditions sont présentées dans votre espace commerçant, après connexion, avant tout engagement.",
     'Ensuite, <a href="/tarifs">les offres et leurs prix sont publics</a>, avec une formule mensuelle sans engagement.'),
    # /commercants
    ("<title>Faire tester ses produits par des consommateurs | Avitime</title>",
     "<title>Faire tester ses produits par des consommateurs | Avitime</title>"),
    ('content="Faire tester ses produits par des consommateurs | Avitime"',
     'content="Faire tester ses produits par des consommateurs | Avitime"'),
    ("<h1>Faites tester vos produits par de vrais consommateurs</h1>",
     "<h1>Faire tester ses produits par de vrais consommateurs</h1>"),
    ('<h1 class="gd-h1">Faites tester vos produits par de vrais consommateurs</h1>',
     '<h1 class="gd-h1">Faire tester ses produits par de vrais consommateurs</h1>'),
    # /pionniers
    ("<title>Avitime : vos 5 premiers tests produits offerts</title>",
     "<title>5 testeurs offerts, seuls produit et port à payer | Avitime</title>"),
    ('content="Avitime : vos 5 premiers tests produits offerts"',
     'content="5 testeurs offerts, seuls produit et port à payer | Avitime"'),
    ("<h1>Vos 5 premiers tests offerts</h1>", "<h1>5 testeurs offerts : vous ne payez que le produit et le port</h1>"),
    # /audit-seo et promesses sur l'accueil anglais
    ("The pilot starts with non-regulated accessories. ", "Your store must deliver to France, and the tested product must be the one your customers receive. "),
    ("The stars under the blue link: added automatically by the Avitime module",
     "Stars under the blue link are Google’s decision: the Avitime module only provides compatible markup"),
]
PAGES_TEXTE = [p for p in PUBLIC.rglob("*.html") if p.relative_to(PUBLIC).parts[0] != "demo"]
SOURCES = list((RACINE / "tools" / "pages").glob("*.main.html"))


def appliquer(html):
    for avant, apres in REMPLACEMENTS:
        html = html.replace(avant, apres)
    return html


# Tarifs dans le pied de page français
LIEN_TESTS = '<li><a href="/pionniers">Tests offerts</a></li>'
LIEN_TARIFS = '<li><a href="/tarifs">Tarifs</a></li>'
LIEN_POURQUOI = '<li><a href="/pourquoi-faire-tester-vos-produits">Pourquoi faire tester</a></li>'

modifies = 0
for f in PAGES_TEXTE + SOURCES:
    avant = f.read_text(encoding="utf-8", newline="")
    html = appliquer(avant)
    rel = f.relative_to(RACINE).parts
    if rel[0] == "public" and rel[1] != "en":
        html = re.sub(r'<nav aria-label="Navigation principale" class="nav-links">.*?</nav>',
                      lambda m: menu(f.name, "guides" in rel), html, count=1, flags=re.S)
        if LIEN_TARIFS not in html:
            html = html.replace(LIEN_TESTS, LIEN_TARIFS + LIEN_TESTS)
        if LIEN_POURQUOI not in html:
            html = html.replace(LIEN_TARIFS, LIEN_POURQUOI + LIEN_TARIFS)
    if html != avant:
        f.write_text(html, encoding="utf-8", newline="")
        modifies += 1
print(f"{modifies} pages modifiées")

# À propos : liens vers les pages qui n'en recevaient aucun
ap = PUBLIC / "a-propos.html"
html = ap.read_text(encoding="utf-8", newline="")
AJOUT = ('<p class="fine-note" style="margin-top:18px">À lire aussi : <a class="link" href="/avis-verifies.html">comment nous vérifions les avis sur Avitime</a> · '
         '<a class="link" href="/badge-avitime">ce que signifie le badge Avitime</a>.</p>\n')
ANCRE = '<a href="#faq-apropos">Politique d’avis</a>'
if "/avis-verifies.html" not in html and ANCRE in html:
    i = html.index(ANCRE)
    fin = html.index("</section>", i)
    html = html[:fin] + AJOUT + html[fin:]
    ap.write_text(html, encoding="utf-8", newline="")

# robots.txt : Google doit pouvoir lire le noindex de /demo/
rb = PUBLIC / "robots.txt"
html = rb.read_text(encoding="utf-8", newline="")
rb.write_text(re.sub(r"Disallow: /demo/\r?\n", "", html), encoding="utf-8", newline="")

# llms.txt
lm = PUBLIC / "llms.txt"
html = lm.read_text(encoding="utf-8", newline="")
html = html.replace("Avitime est une plateforme française de tests produits pour les boutiques en ligne.",
                    "Avitime est un service de tests produits pour les boutiques en ligne du marché français, édité par SPARKMOTION AGENCY LTD.")
if "avitime.fr/tarifs" not in html:
    html = html.replace("- [Intégrations](https://avitime.fr/integrations)",
                        "- [Tarifs](https://avitime.fr/tarifs): 5 premiers tests offerts, puis Starter à partir de 39,90 € HT/mois et Pro à partir de 59,90 € HT/mois ; mensuel sans engagement\n- [Intégrations](https://avitime.fr/integrations)")
if "pourquoi-faire-tester-vos-produits" not in html:
    html = html.replace("- [Tarifs](https://avitime.fr/tarifs)",
                        "- [Pourquoi faire tester vos produits](https://avitime.fr/pourquoi-faire-tester-vos-produits): premiers avis, Google et IA, publicité, loi sur les faux avis, règles de transparence\n- [Tarifs](https://avitime.fr/tarifs)", 1)
lm.write_text(html, encoding="utf-8", newline="")

# sitemap : la date commune du 1er novembre n'apporte aucune information
sm = PUBLIC / "sitemap.xml"
html = sm.read_text(encoding="utf-8", newline="")
html = html.replace("<lastmod>2026-11-01</lastmod>", "")
AUJ = "2026-11-06"
for adresse in ("https://avitime.fr/", "https://avitime.fr/commercants", "https://avitime.fr/pionniers"):
    html = re.sub(rf"<loc>{re.escape(adresse)}</loc>(<lastmod>[^<]*</lastmod>)?", f"<loc>{adresse}</loc><lastmod>{AUJ}</lastmod>", html, count=1)
if "https://avitime.fr/tarifs" not in html:
    html = html.replace("<url><loc>https://avitime.fr/audit-seo</loc>",
                        f"<url><loc>https://avitime.fr/tarifs</loc><lastmod>{AUJ}</lastmod></url>\n  <url><loc>https://avitime.fr/audit-seo</loc>", 1)
if "pourquoi-faire-tester-vos-produits" not in html:
    html = html.replace("<url><loc>https://avitime.fr/tarifs</loc>",
                        f"<url><loc>https://avitime.fr/pourquoi-faire-tester-vos-produits</loc><lastmod>{AUJ}</lastmod></url>\n  <url><loc>https://avitime.fr/tarifs</loc>", 1)
sm.write_text(html, encoding="utf-8", newline="")

# nginx : vraie page 404, anciennes adresses de prix vers /tarifs
ng = RACINE / "nginx.conf"
html = ng.read_text(encoding="utf-8", newline="")
html = html.replace("error_page 404 /index.html;", "error_page 404 /404.html;")
if "location = /prix" not in html:
    html = html.replace("    location = /en { return 301 /en/; }",
                        "    location = /prix    { return 301 /tarifs; }\n    location = /pricing { return 301 /tarifs; }\n    location = /en { return 301 /en/; }", 1)
ng.write_text(html, encoding="utf-8", newline="")
print("robots, llms, sitemap et nginx à jour")
