#!/usr/bin/env python3
"""Parcours commerçant : à relancer après chaque génération des pages.

- Boutons de création de compte : /devenir-commercant (inscription), plus la page de connexion.
- « Je suis commerçant » : page /commercants.
- Bouton orange de l'en-tête : audit SEO gratuit, sauf sur les pages destinées aux testeurs.
- Le lien discret « Espace commerçant » reste sur la connexion, pour les comptes existants.
Le script peut être relancé sans effet de bord.
"""
import re
from pathlib import Path

PUBLIC = Path(__file__).resolve().parent.parent / "public"

CREER = [
    "Créer mon espace commerçant", "Connecter ma boutique", "Rendre mes produits visibles",
    "Obtenir mes premiers vrais avis", "Obtenir mes premiers avis", "Obtenir de vrais avis",
    "Lancer mes premiers tests", "Faire tester mon produit numérique",
]
PAGES_TESTEURS = {
    "cgu-testeurs.html", "devenir-testeur.html", "arnaques-testeur-produits.html",
    "video-testeur-produit.html", "testeur-de-produit.html", "sites-tester-produits-gratuitement.html",
    "testeur-amazon-vine.html", "tester-produits-a-domicile.html", "testeur-produits-par-categorie.html",
    "tester-formations-logiciels-gratuitement.html",
}
EN_TESTEURS = {"tester-terms.html"}
CTA_TESTEUR = '<a class="btn-sm" href="/devenir-testeur">Devenir testeur</a>'
CTA_AUDIT = '<a class="btn-sm" href="/audit-seo">Audit gratuit</a>'
CTA_AUDIT_ICI = '<a class="btn-sm" href="#audit">Audit gratuit</a>'
EN_CTA_TESTEUR = '<a class="btn-sm" href="/en/become-tester">Become a tester</a>'
EN_CTA_MARCHAND = '<a class="btn-sm" href="/en/become-merchant">Merchant sign-up</a>'


def fr(html, nom):
    for texte in CREER:
        html = html.replace(f'href="/espace-commercant">{texte}<', f'href="/devenir-commercant">{texte}<')
    html = html.replace('<a class="btn" href="/espace-commercant">Accéder à l’espace commerçant</a>',
                        '<a class="btn" href="/devenir-commercant">Créer mon espace commerçant</a>')
    html = html.replace('<a class="btn" href="/espace-commercant">Espace commerçant</a>',
                        '<a class="btn" href="/devenir-commercant">Créer mon espace commerçant</a>')
    html = html.replace('href="/espace-commercant">Je suis commerçant<', 'href="/commercants">Je suis commerçant<')
    if nom in PAGES_TESTEURS:
        cta = CTA_TESTEUR
    elif nom == "audit-seo.html":
        cta = CTA_AUDIT_ICI
    else:
        cta = CTA_AUDIT
    return re.sub('|'.join(map(re.escape, (CTA_TESTEUR, CTA_AUDIT, CTA_AUDIT_ICI))), cta, html)


def en(html, nom):
    html = html.replace('<a class="btn" href="/en/merchant">Go to the merchant account</a>',
                        '<a class="btn" href="/en/become-merchant">Create my merchant account</a>')
    html = html.replace('<a class="btn" href="/en/merchant">Merchant account</a>',
                        '<a class="btn" href="/en/become-merchant">Create my merchant account</a>')
    html = html.replace('<a class="btn" href="/en/merchant">', '<a class="btn" href="/en/become-merchant">')
    html = html.replace('class="ms-m" href="/en/merchant"', 'class="ms-m" href="/en/become-merchant"')
    cta = EN_CTA_TESTEUR if nom in EN_TESTEURS else EN_CTA_MARCHAND
    return re.sub('|'.join(map(re.escape, (EN_CTA_TESTEUR, EN_CTA_MARCHAND))), cta, html)


modifies = 0
for f in PUBLIC.rglob("*.html"):
    rel = f.relative_to(PUBLIC).parts
    if rel[0] == "demo":
        continue
    avant = f.read_text(encoding="utf-8", newline="")
    apres = en(avant, f.name) if rel[0] == "en" else fr(avant, f.name)
    if apres != avant:
        f.write_text(apres, encoding="utf-8", newline="")
        modifies += 1
print(f"{modifies} fichiers modifiés")
