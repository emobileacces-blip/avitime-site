#!/usr/bin/env python3
"""Maillage interne : ajoute des liens sur des expressions déjà présentes dans les guides, sans changer le texte.
Relançable sans effet de bord. Modifie la page publiée et, quand l'expression y figure, ses fichiers sources."""
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
GUIDES = RACINE / "public" / "guides"
DOM = "/guides/tester-produits-a-domicile.html"
CAT = "/guides/testeur-produits-par-categorie.html"
TDP = "/guides/testeur-de-produit.html"
SIT = "/guides/sites-tester-produits-gratuitement.html"
TAR = "/tarifs"
PIO = "/pionniers"
POU = "/pourquoi-faire-tester-vos-produits"
COM = "/guides/comparatif-solutions-avis-clients.html"
ALT = "/guides/alternative-avis-verifies-trustpilot.html"
SYS = "/guides/avis-formation-systeme-io.html"
SUR = "/guides/avis-site-sur-mesure-api.html"
NUM = "/guides/avis-produit-numerique-formation-saas.html"
ETO = "/guides/etoiles-google-shopping-avis-produits.html"
LOI = "/guides/faux-avis-loi.html"
VID = "/guides/video-testeur-produit.html"
OMN = "/guides/directive-omnibus-avis-clients.html"
WID = "/guides/widget-avis-clients.html"
PRE = "/guides/premiers-avis-clients.html"

# guide, texte avant le lien, expression liée, texte après le lien, cible
LIENS = [
    ("testeur-de-produit", "Vous recevez ", "le produit chez vous", ", vous l’utilisez", DOM),
    ("testeur-produits-par-categorie", "<b>", "À domicile", "</b> : les clubs comme Sampleo", DOM),
    ("sites-tester-produits-gratuitement", "On y trouve des <b>", "tests à domicile", "</b> (produits gratuits", DOM),
    ("testeur-de-produit", "Surtout grandes marques (", "alimentaire, beauté, maison", ")</td>", CAT),
    ("testeur-amazon-vine", "<td>Grandes marques (", "alimentaire, beauté, maison", ")</td>", CAT),
    ("arnaques-testeur-produits", "<p>En général, non : ", "vous gardez le produit en échange d’un avis honnête", ".", TDP),
    ("arnaques-testeur-produits", "ou le produit n’arrive jamais. ", "Un programme sérieux", " paie la livraison", SIT),
    ("tester-formations-logiciels-gratuitement", "Sur un ", "programme sérieux", ", vous ne payez jamais rien", SIT),
    ("alternative-avis-verifies-trustpilot", "Ensuite, ", "la formule mensuelle", " est sans engagement et résiliable", TAR),
    ("avis-clients-shopify-gratuit", "<li><b>", "Une formule mensuelle sans engagement", "</b>, et vos", TAR),
    ("obtenir-avis-clients-boutique-en-ligne", "; ", "une formule mensuelle sans engagement", ". Les ", TAR),
    ("comparatif-solutions-avis-clients", "sans abonnement, puis ", "la formule mensuelle", " est sans engagement", TAR),
    ("widget-avis-clients", "5 premiers tests offerts, puis ", "formule mensuelle", "</td><td>Oui</td><td>Pas encore", TAR),
    ("avis-formation-systeme-io", "Ensuite, ", "les formules", " sont présentées dans votre espace commerçant avant tout engagement.</p>", TAR),
    ("avis-clients-woocommerce", "lui-même fonctionne ", "sur abonnement", ", après <a href", TAR),
    ("alternative-avis-verifies-trustpilot", "<b>Sans engagement.</b> Les ", "5 premiers tests sont offerts", " à chaque nouvelle boutique", PIO),
    ("avis-clients-shopify-gratuit", "</b>, et vos ", "5 premiers tests sont offerts", ".</li>", PIO),
    ("obtenir-avis-clients-boutique-en-ligne", ". Les ", "5 premiers tests sont offerts", " à chaque nouvelle boutique", PIO),
    ("comparatif-solutions-avis-clients", "validation). Les ", "5 premiers tests sont offerts", " à chaque nouvelle boutique", PIO),
    ("avis-formation-systeme-io", "<p>En ce moment, vos ", "5 premiers tests sont offerts", ", sans abonnement. Ensuite", PIO),
    ("premiers-avis-clients", "pour vos tout premiers avis, ", "faire tester le produit", " est souvent plus rapide. Le comparatif : <a", POU),
    ("boutique-en-ligne-sans-ventes", "<b>", "faisant tester vos produits", "</b> par de vrais consommateurs", POU),
    ("demander-avis-client", "la solution honnête est de faire <b>", "tester vos produits", "</b> par de vrais consommateurs", POU),
    # Comparatif : recherches « plateforme d'avis clients »
    ("avis-clients-prestashop", "un module de ", "plateforme d’avis", ", en général payant", COM),
    ("etoiles-google-shopping-avis-produits", "par une ", "plateforme d’avis partenaire", ".</p>", COM),
    ("site-cree-avec-ia", "Google comme les ", "plateformes d’avis", " les détectent", COM),
    ("avis-clients-ia", "médias, ", "plateformes d’avis", ". Une boutique", COM),
    # Pages peu reliées
    ("eeat-e-commerce", "dans Google. ", "Une plateforme comme Trustpilot", " renforce", ALT),
    ("obtenir-avis-clients-boutique-en-ligne", "), ", "une plateforme comme Avis Vérifiés ou Trustpilot", ", ou votre outil", ALT),
    ("avis-produit-numerique-formation-saas", "WooCommerce, sur ", "Systeme.io", " (inscription automatique", SYS),
    ("echantillonnage-produit", "validation), ", "Systeme.io", " et les ", SYS),
    ("avis-produit-numerique-formation-saas", "ou sur un ", "site sur mesure", " ou une autre", SUR),
    ("echantillonnage-produit", " et les ", "sites sur mesure", " : <a", SUR),
    ("avis-formation-systeme-io", "<p>", "Une formation en ligne", " ne se voit pas", NUM),
    ("avis-site-sur-mesure-api", "testeurs. Pour ", "un produit numérique", ", indiquez", NUM),
    # Guides qui renvoyaient vers trop peu de pages
    ("avis-site-sur-mesure-api", "d’afficher ou non ", "les étoiles", ".</p></div>", ETO),
    ("avis-formation-systeme-io", "positif ou négatif, avec ", "la mention qu’elle leur a été offerte", ". C’est exactement", LOI),
    ("avis-formation-systeme-io", "<b>", "vidéo d’utilisation", "</b> sur ses réseaux", VID),
    ("faux-avis-loi", "<b>D’où viennent ces règles : ", "la directive Omnibus", ".</b>", OMN),
    ("alternative-avis-verifies-trustpilot", "transposition de ", "la directive Omnibus", " (2019/2161)", OMN),
    ("alternative-avis-verifies-trustpilot", "faire publier ", "de faux avis", " est une pratique", LOI),
    ("alternative-avis-verifies-trustpilot", "grâce à ", "des widgets", " et des intégrations", WID),
    ("alternative-avis-verifies-trustpilot", "d’obtenir ", "les tout premiers avis", ", de façon transparente", PRE),
]

# Liens existants dont le texte devient plus descriptif : guide, ancien texte de lien (balises comprises), nouveau
TEXTES = [
    ("echantillonnage-produit", 'avis-clients.html">notre comparatif honnête</a>', 'avis-clients.html">notre comparatif des plateformes d’avis clients</a>'),
    ("directive-omnibus-avis-clients", 'avis-clients.html">comparatif pour PME</a>', 'avis-clients.html">comparatif des plateformes d’avis clients</a>'),
    ("echantillonnage-produit", '<a href="/commercants">découvrir l’offre commerçants</a>', '<a href="/commercants">faire tester vos produits</a>'),
    ("avis-formation-systeme-io", '<a href="/guides/avis-site-sur-mesure-api.html">le guide</a>', '<a href="/guides/avis-site-sur-mesure-api.html">le guide des sites sur mesure</a>'),
]

# Boutons qui disaient tous « Découvrir l'offre commerçants »
BOUTON = "Découvrir l’offre commerçants"
AVIS = "Obtenir mes premiers avis"
TEST = "Faire tester mes produits"
VRAIS = "Obtenir de vrais avis clients"
LIBELLES = {
    "premiers-avis-clients": AVIS, "obtenir-avis-clients-boutique-en-ligne": AVIS, "demander-avis-client": AVIS, "combien-avis-clients": AVIS,
    "lancer-nouveau-produit": AVIS, "boutique-en-ligne-sans-ventes": AVIS, "preuve-sociale-ecommerce-conversions": AVIS, "taux-conversion-e-commerce": AVIS,
    "statistiques-avis-clients": AVIS, "fiche-produit-e-commerce": AVIS,
    "alternative-avis-verifies-trustpilot": TEST, "comparatif-solutions-avis-clients": TEST, "widget-avis-clients": TEST, "avis-clients-shopify": TEST,
    "avis-clients-shopify-gratuit": TEST, "avis-clients-woocommerce": "Faire tester mes produits sur WooCommerce", "avis-clients-prestashop": "Faire tester mes produits sur PrestaShop",
    "directive-omnibus-avis-clients": TEST, "faux-avis-loi": TEST, "repondre-avis-negatifs": TEST, "echantillonnage-produit": TEST,
    "avis-clients-ia": VRAIS, "eeat-e-commerce": VRAIS, "geo-seo": VRAIS, "referencement-boutique-en-ligne": VRAIS, "seo-site-ne-decolle-pas": VRAIS,
    "site-cree-avec-ia": VRAIS, "etoiles-google-shopping-avis-produits": VRAIS,
}

SOURCES = [f for f in list((RACINE / "tools").glob("*.py")) + list((RACINE / "tools" / "pages").glob("*.py")) + list((RACINE / "tools" / "pages").glob("guide-*.html"))
           if f.name not in (Path(__file__).name, "make_vitrine_v2.py")]
ajouts = 0
sans_source = []
for slug, avant, expr, apres, cible in LIENS:
    page = GUIDES / f"{slug}.html"
    html = page.read_text(encoding="utf-8", newline="")
    d, f = html.index("<main"), html.index("</main>")
    corps = html[d:f]
    ancien = avant + expr + apres
    nouveau = f'{avant}<a href="{cible}">{expr}</a>{apres}'
    if nouveau in corps:
        continue
    assert corps.count(ancien) == 1, (slug, expr, corps.count(ancien))
    pos = corps.index(ancien)
    assert corps[:pos].rfind("<a ") <= corps[:pos].rfind("</a>"), ("déjà dans un lien", slug, expr)
    page.write_text(html[:d] + corps.replace(ancien, nouveau) + html[f:], encoding="utf-8", newline="")
    ajouts += 1
    trouve = False
    for src in SOURCES:
        s = src.read_text(encoding="utf-8", newline="")
        if s.count(ancien) == 1:
            src.write_text(s.replace(ancien, nouveau), encoding="utf-8", newline="")
            trouve = True
    if not trouve:
        sans_source.append((slug, expr))
print(ajouts, "liens ajoutés | sans source :", sans_source)

textes = 0
for slug, ancien, nouveau in TEXTES:
    page = GUIDES / f"{slug}.html"
    html = page.read_text(encoding="utf-8", newline="")
    if nouveau in html:
        continue
    assert html.count(ancien) == 1, (slug, ancien, html.count(ancien))
    page.write_text(html.replace(ancien, nouveau), encoding="utf-8", newline="")
    textes += 1
    for src in SOURCES:
        t = src.read_text(encoding="utf-8", newline="")
        if t.count(ancien) == 1:
            src.write_text(t.replace(ancien, nouveau), encoding="utf-8", newline="")
boutons = 0
for slug, libelle in LIBELLES.items():
    page = GUIDES / f"{slug}.html"
    html = page.read_text(encoding="utf-8", newline="")
    n = html.count(f">{BOUTON}</a>")
    if n:
        page.write_text(html.replace(f">{BOUTON}</a>", f">{libelle}</a>"), encoding="utf-8", newline="")
        boutons += n
print(textes, "textes de liens précisés |", boutons, "boutons renommés")
