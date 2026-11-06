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
]

SOURCES = [f for f in list((RACINE / "tools").glob("*.py")) + list((RACINE / "tools" / "pages").glob("*.py")) + list((RACINE / "tools" / "pages").glob("guide-*.html"))
           if f.name != Path(__file__).name]
ajouts = 0
sans_source = []
for slug, avant, expr, apres, cible in LIENS:
    page = GUIDES / f"{slug}.html"
    html = page.read_text(encoding="utf-8", newline="")
    ancien = avant + expr + apres
    nouveau = f'{avant}<a href="{cible}">{expr}</a>{apres}'
    if nouveau in html:
        continue
    assert html.count(ancien) == 1, (slug, expr, html.count(ancien))
    pos = html.index(ancien)
    assert html[:pos].rfind("<a ") <= html[:pos].rfind("</a>"), ("déjà dans un lien", slug, expr)
    page.write_text(html.replace(ancien, nouveau), encoding="utf-8", newline="")
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
