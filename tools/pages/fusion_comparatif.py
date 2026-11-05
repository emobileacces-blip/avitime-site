#!/usr/bin/env python3
"""Fusion du 05/11/2026 (plan SEO commerçants, phase 1) :
plateformes-avis-clients-pme-comparatif.html est fondu dans comparatif-solutions-avis-clients.html
(page la plus ancienne, déjà classée), qui devient LA page « plateforme d'avis clients : comparatif et prix ».
L'ancienne URL est redirigée en 301 par nginx. Script à lancer une seule fois depuis avitime-site/."""
import json
import re
import urllib.parse
from pathlib import Path

PUB = Path("public")
G = PUB / "guides"
OLD_SLUG = "plateformes-avis-clients-pme-comparatif"
NEW_SLUG = "comparatif-solutions-avis-clients"
page = (G / f"{NEW_SLUG}.html").read_text()
pme = Path("tools/pages/guide-pme.body.html").read_text()

# ---------- morceaux de l'ancien comparatif ----------
body_start = page.index('<nav class="gd-toc"')
body_end = page.index('<div class="gd-cta">', body_start)  # le CTA final et la suite restent
old_body = page[body_start:body_end]


def between(s, a, b):
    i = s.index(a)
    j = s.index(b, i)
    return s[i:j]


familles = between(old_body, '<h2 id="collecte">', '<h2 id="choisir">')
# les 5 sections deviennent des sous-parties
familles = re.sub(r'<h2 id="(collecte|clubs|marketplace|echantillonnage|tableau)">\d\. ', r'<h3 id="\1">', familles)
familles = re.sub(r'(<h3 id="(?:collecte|clubs|marketplace|echantillonnage|tableau)">[^<]*)</h2>', r'\1</h3>', familles)
choisir = between(old_body, '<h2 id="choisir">', '<h2 id="alternative">')
choisir = re.sub(r'<h2 id="choisir">[^<]*</h2>', '<h3 id="questions">Les 5 questions à se poser</h3>', choisir)
alternative = between(old_body, '<h2 id="alternative">', '<h2 id="faq">')
alternative = alternative.replace('<h2 id="alternative">7. ', '<h2 id="alternative">8. ')
faq_old = between(old_body, '<h2 id="faq">', '<h3>Sources</h3>')
sources_old = between(old_body, '<ul class="gd-src">', '</ul>') + '</ul>'

# ---------- morceaux du comparatif PME ----------
p_intro = between(pme, '<p>Trustpilot, Avis Vérifiés, Bazaarvoice', '<h2 id="trustpilot">')
p_trust = between(pme, '<h2 id="trustpilot">', '<h2 id="criteres">')
p_crit = between(pme, '<h2 id="criteres">', '<h2 id="tableau">')
p_tab = between(pme, '<h2 id="tableau">', '<h2 id="solutions">')
p_sol = between(pme, '<h2 id="solutions">', '<h2 id="budget">')
p_budget = between(pme, '<h2 id="budget">', '<h2 id="profil">')
p_profil = between(pme, '<h2 id="profil">', '<h2 id="faq">')
p_faq = between(pme, '<h2 id="faq">', '<h2 id="sources">')
p_sources = between(pme, '<ul class="gd-src">', '</ul>') + '</ul>'

p_trust = p_trust.replace('<h2 id="trustpilot">Pourquoi Trustpilot n’est pas toujours le bon choix pour une PME</h2>',
                          '<h2 id="trustpilot">5. Trustpilot est-il adapté à une PME&nbsp;?</h2>')
p_trust = p_trust.replace(' Voir aussi notre comparatif <a href="/guides/alternative-avis-verifies-trustpilot.html">alternative à Avis Vérifiés et Trustpilot</a>.',
                          ' Voir aussi <a href="/guides/alternative-avis-verifies-trustpilot.html">alternative à Avis Vérifiés et Trustpilot</a>.')
p_crit = p_crit.replace('<h2 id="criteres">Les critères de choix pour une PME</h2>', '<h3 id="criteres">Les critères qui comptent pour une PME</h3>')
p_tab = p_tab.replace('<h2 id="tableau">Le tableau comparatif 2026</h2>', '<h2 id="prix">1. Le tableau comparatif des prix 2026</h2>')
p_sol = p_sol.replace('<h2 id="solutions">Les solutions, une par une</h2>', '<h2 id="solutions">3. Les plateformes, une par une</h2>')
p_budget = p_budget.replace('<h2 id="budget">Ce que coûte chaque solution sur un an</h2>', '<h2 id="budget">4. Ce que coûte chaque solution sur un an</h2>')
p_profil = p_profil.replace('<h2 id="profil">Quelle solution selon votre profil&nbsp;?</h2>', '<h3 id="profil">Quelle solution selon votre profil</h3>')
p_profil = re.sub(r'<h3>(Vous [^<]*)</h3>', r'<h4>\1</h4>', p_profil)

# ---------- FAQ fusionnée (sans doublon) ----------
faq_old = faq_old.replace('<h2 id="faq">8. Questions fréquentes</h2>', '')
# la question qui renvoyait vers le guide PME pointe maintenant vers le tableau de cette page
faq_old = faq_old.replace(
    'Les prix de chaque plateforme sont comparés dans notre guide <a href="/guides/plateformes-avis-clients-pme-comparatif.html">plateformes d’avis clients pour PME</a>.',
    'Les prix de chaque plateforme sont dans <a href="#prix">le tableau comparatif</a>.')
faq_old = re.sub(r'<h3>Combien coûte une solution d’avis clients \?</h3>\s*<p>.*?</p>\s*', '', faq_old, flags=re.S)
p_faq = p_faq.replace('<h2 id="faq">Questions fréquentes</h2>', '')
keep = ["Quelle est la meilleure plateforme d’avis clients pour une PME",
        "Combien coûte une plateforme d’avis clients",
        "Comment obtenir des avis sur un produit qui n’a jamais été vendu",
        "Peut-on combiner plusieurs solutions d’avis",
        "Les plateformes d’avis sont-elles soumises à la directive Omnibus"]
add = ""
for q in keep:
    m = re.search(r'<h3>' + re.escape(q) + r'[^<]*</h3>\s*<p>.*?</p>\s*', p_faq, flags=re.S)
    assert m, q
    add += m.group(0)
faq = '<h2 id="faq">9. Questions fréquentes</h2>\n' + add + faq_old.strip() + "\n\n"

# sources : union sans doublon
src_items = []
for ul in (p_sources, sources_old):
    for li in re.findall(r'<li>.*?</li>', ul, flags=re.S):
        if li not in src_items:
            src_items.append(li)
sources = '<h2 id="sources">Sources</h2>\n<ul class="gd-src">\n' + "\n".join(src_items) + "\n</ul>\n"
note = ('<p class="gd-note">Comparatif d’information générale, établi à partir des informations publiques des services cités, '
        'mis à jour le 5 novembre 2026. Les prix en dollars sont ceux affichés par les éditeurs ou les comparateurs, hors taxes. '
        'Les offres évoluent souvent&nbsp;: vérifiez les conditions de chaque service avant de choisir. Avitime est l’éditeur de ce guide '
        'et l’une des solutions comparées. Les marques citées appartiennent à leurs propriétaires respectifs.</p>\n')

toc = ('<nav class="gd-toc" aria-label="Sommaire"><p>Au sommaire</p><ol>\n'
       '<li><a href="#prix">Le tableau comparatif des prix 2026</a></li>\n'
       '<li><a href="#familles">Quatre familles de solutions</a></li>\n'
       '<li><a href="#solutions">Les plateformes, une par une</a></li>\n'
       '<li><a href="#budget">Ce que coûte chaque solution sur un an</a></li>\n'
       '<li><a href="#trustpilot">Trustpilot est-il adapté à une PME&nbsp;?</a></li>\n'
       '<li><a href="#choisir">Comment choisir</a></li>\n'
       '<li><a href="#gratuit">Les solutions gratuites</a></li>\n'
       '<li><a href="#alternative">Quelle alternative pour une petite boutique&nbsp;?</a></li>\n'
       '<li><a href="#faq">Questions fréquentes</a></li>\n'
       '</ol></nav>\n\n')
key = ('<div class="gd-key"><p><b>L’essentiel :</b> une plateforme d’avis clients <b>collecte</b> les avis de vos acheteurs '
       'après chaque commande. Les offres d’entrée publiques vont d’environ 29&nbsp;€ par mois (Société des Avis Garantis) '
       'à 59&nbsp;€ (Avis Vérifiés) et 99&nbsp;$ (Trustpilot Starter, facturé à l’année). Toutes supposent déjà des ventes. '
       'Pour les produits qui n’ont encore aucun avis, il faut les faire <b>tester</b>, en toute transparence. '
       'Les deux approches se complètent.</p></div>\n\n')
gratuit = ('<h2 id="gratuit">7. Les solutions gratuites</h2>\n'
           '<p>Une plateforme payante n’est pas indispensable pour commencer. Quatre options ne coûtent rien&nbsp;:</p>\n<ul>\n'
           '<li><b>Les avis intégrés à votre boutique</b>&nbsp;: module « Commentaires produits » de PrestaShop, avis et libellé « propriétaire vérifié » de WooCommerce. '
           'Sur Shopify, il faut une application tierce, dont certaines ont une offre gratuite (voir <a href="/guides/avis-clients-shopify-gratuit.html">avis Shopify sans application payante</a>).</li>\n'
           '<li><b>Google Avis clients</b>, le programme gratuit de Google Merchant Center, pour collecter des avis après achat.</li>\n'
           '<li><b>Votre fiche Google Business Profile</b>, pour les avis sur votre entreprise.</li>\n'
           '<li><b>Les offres gratuites limitées</b> de Trustpilot et de Custplace.</li>\n</ul>\n'
           '<p>Aucune de ces solutions ne crée d’avis quand vous n’avez pas encore de clients. Chez Avitime, les 5 premiers tests sont offerts '
           'à chaque nouvelle boutique, sans abonnement&nbsp;: <a href="/commercants">voir l’offre commerçants</a>.</p>\n\n')

new_body = (toc + key + p_intro.strip() + "\n\n" + p_tab
            + '<h2 id="familles">2. Quatre familles de solutions, quatre usages</h2>\n'
            + '<p>Avant de comparer les prix, il faut savoir ce que chaque solution fait. Elles ne répondent pas au même problème&nbsp;:</p>\n'
            + familles + p_sol + p_budget + p_trust
            + '<h2 id="choisir">6. Comment choisir&nbsp;?</h2>\n' + p_crit + choisir + p_profil
            + gratuit + alternative + faq + sources + note)
# vocabulaire (règle de Cyril du 05/11) : jamais « avis négatifs »
new_body = new_body.replace("tous les avis sont publiés, y compris les négatifs, sans que", "tous les avis sont publiés, quelle que soit leur note, sans que")
new_body = new_body.replace("contreparties signalées, avis négatifs publiés.", "contreparties signalées, tous les avis publiés.")
page = page[:body_start] + new_body + page[body_end:]

# ---------- en-tête, titres, partage ----------
OLD_H1 = "Solutions d’avis clients : le comparatif honnête pour les boutiques en ligne"
NEW_H1 = "Plateforme d’avis clients : le comparatif 2026, prix compris"
SEO_T = "Plateforme d’avis clients : comparatif et prix 2026 (PME)"
SEO_D = "Avis Vérifiés, Trustpilot, Avis Garantis, Google, testeurs : prix publics, avantages et limites. Quelle plateforme d’avis clients choisir pour une PME ?"
LEDE = ("Avis Vérifiés, Trustpilot, Société des Avis Garantis, Google, clubs de testeurs, Avitime… Les plateformes d’avis clients se ressemblent sur le papier, "
        "mais elles n’ont ni le même prix ni le même usage. Voici leurs tarifs publics, ce que fait chacune, pour qui elle est faite, et ce qu’elle ne fait pas.")
page = re.sub(r"<title>.*?</title>", f"<title>{SEO_T}</title>", page, count=1)
page = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{SEO_D}">', page, count=1)
page = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{SEO_T}">', page, count=1)
page = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{SEO_D}">', page, count=1)
page = re.sub(r'<meta name="twitter:title" content="[^"]*">', f'<meta name="twitter:title" content="{SEO_T}">', page)
page = re.sub(r'<meta name="twitter:description" content="[^"]*">', f'<meta name="twitter:description" content="{SEO_D}">', page)
page = page.replace(f"<h1>{OLD_H1}</h1>", f"<h1>{NEW_H1}</h1>")
page = re.sub(r'<p class="gd-lede">.*?</p>', f'<p class="gd-lede">{LEDE}</p>', page, count=1, flags=re.S)
page = page.replace(f'data-title="{OLD_H1}"', f'data-title="{NEW_H1}"')
page = page.replace(urllib.parse.quote(OLD_H1), urllib.parse.quote(NEW_H1))
page = page.replace("mis à jour le 1er novembre 2026 · lecture 10 min", "mis à jour le 5 novembre 2026 · lecture 15 min")

# ---------- JSON-LD : Article + FAQPage reconstruits ----------
faq_pairs = re.findall(r'<h3>(.*?)</h3>\s*<p>(.*?)</p>', faq, flags=re.S)


def txt(s):
    s = re.sub(r"<[^>]+>", "", s).replace("&nbsp;", " ").replace("&amp;", "&")
    return re.sub(r"\s+", " ", s).strip()


def fix_ld(m):
    raw = m.group(1)
    data = json.loads(raw)
    nodes = data["@graph"] if isinstance(data, dict) and "@graph" in data else [data]
    for n in nodes:
        t = n.get("@type")
        if t in ("Article", "BlogPosting"):
            n["headline"] = NEW_H1
            n["description"] = SEO_D
            n["dateModified"] = "2026-11-05"
        if t == "FAQPage":
            n["mainEntity"] = [{"@type": "Question", "name": txt(q), "acceptedAnswer": {"@type": "Answer", "text": txt(a)}} for q, a in faq_pairs]
        if t == "BreadcrumbList":
            for it in n.get("itemListElement", []):
                if it.get("item", "").endswith(f"{NEW_SLUG}.html"):
                    it["name"] = NEW_H1
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"


page = re.sub(r'<script type="application/ld\+json">(.*?)</script>', fix_ld, page, flags=re.S)
(G / f"{NEW_SLUG}.html").write_text(page)
print("comparatif fusionné :", len(re.sub(r"<[^>]+>", " ", new_body).split()), "mots ;", len(faq_pairs), "questions")
