#!/usr/bin/env python3
"""/commercants : reprend deux blocs de l'ancien accueil (publicité ou avis, types de boutiques).
Relançable sans effet de bord."""
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent

PUB = '''<h3 id="pub-ou-avis">Publicité ou avis clients : où investir pour votre boutique en ligne ?</h3>
<p>Les publicités amènent des visiteurs tant que vous payez. Les avis, eux, restent sur vos fiches et travaillent pour vous sur le long terme.</p>
<p><b>La publicité seule, un robinet qu’il faut payer en continu :</b></p>
<ul>
<li><b>Chaque clic se paie</b>, et les enchères montent avec la concurrence.</li>
<li><b>Budget coupé, trafic coupé</b> : le jour où vous arrêtez, les visites s’arrêtent net.</li>
<li><b>Des clics qui n’achètent pas</b> : sans avis, une grande partie du trafic payé repart sans commander.</li>
<li><b>Des règles qui changent sans prévenir</b> : prix, ciblage, algorithmes, vous dépendez des plateformes publicitaires.</li>
</ul>
<p><b>Les avis, un acquis qui dure :</b></p>
<ul>
<li><b>Ils restent sur vos fiches</b> et continuent de rassurer chaque visiteur, mois après mois.</li>
<li><b>Ils rentabilisent vos pubs</b> : avec des avis, plus de visiteurs passent à l’achat, y compris ceux qui viennent de la pub.</li>
<li><b>Google et les IA peuvent les lire</b> : de vraies expériences de clients, c’est le « E » d’Expérience des critères E‑E‑A‑T de Google.</li>
<li><b>Un investissement qui dure</b> : ce que vous mettez en place aujourd’hui travaille encore dans un an.</li>
</ul>
<p>Les avis ne remplacent pas toute publicité et ne garantissent aucun classement : ils rendent chaque visite plus utile, aujourd’hui comme demain.</p>

'''

BOUTIQUES = '''<h3 id="pour-qui">Quelles boutiques en ligne peuvent faire tester leurs produits ?</h3>
<p>Grande ou petite, généraliste ou spécialisée : si vous vendez en ligne, Avitime s’adapte à votre modèle. Une seule règle : le produit testé est exactement celui que reçoivent vos clients.</p>
<ul>
<li><b>Boutiques multi-produits</b> : mode, déco, high-tech, sport, maison… Faites tester vos best-sellers ou vos nouveautés, campagne par campagne, produit par produit.</li>
<li><b>Marques mono-produit</b> : un seul produit phare ? Ses avis font toute la différence : plusieurs testeurs aux profils variés, et une fiche produit qui rassure enfin.</li>
<li><b>Créateurs, artisans, marques de niche</b> : fait main, petites séries, produits locaux. De vrais retours pour prouver la qualité de votre travail face aux grandes enseignes.</li>
<li><b>Boutiques qui démarrent</b> : vos premiers avis dès les premières semaines, sans attendre les premières ventes. Idéal pour lancer une boutique ou un nouveau produit.</li>
</ul>

'''

for f in (RACINE / "public" / "commercants.html", RACINE / "tools" / "pages" / "commercants.main.html"):
    html = f.read_text(encoding="utf-8", newline="")
    if 'id="pub-ou-avis"' not in html:
        html = html.replace('<h2 id="deroulement">', PUB + '<h2 id="deroulement">', 1)
    if 'id="pour-qui"' not in html:
        html = html.replace('<h2 id="tarifs">', BOUTIQUES + '<h2 id="tarifs">', 1)
    RENVOI = '<p>Le détail, avec Google, les IA et la loi : <a href="/pourquoi-faire-tester-vos-produits">pourquoi faire tester vos produits</a>.</p>\n\n'
    if "pourquoi-faire-tester-vos-produits\">pourquoi" not in html:
        html = html.replace('<h2 id="tarifs">', RENVOI + '<h2 id="tarifs">', 1)
    f.write_text(html, encoding="utf-8", newline="")
    print(f.name, html.count('id="pub-ou-avis"'), html.count('id="pour-qui"'))
