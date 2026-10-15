"""Guides signés (E-E-A-T) : /guides/ — générés depuis ce script (même en-tête et pied de page que le site)."""
import json, os, html
ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "public")
OUT = os.path.join(ROOT, "guides"); os.makedirs(OUT, exist_ok=True)
IG, TT = "https://www.instagram.com/avitime_fr/", "https://www.tiktok.com/@avitime_fr"
AUTHOR = {"@type": "Person", "name": "Cyril Quémy", "jobTitle": "Fondateur d’Avitime", "url": "https://avitime.fr/a-propos.html"}
PUBLISHER = {"@type": "Organization", "name": "Avitime", "url": "https://avitime.fr/", "logo": {"@type": "ImageObject", "url": "https://avitime.fr/assets/img/icon-512.png"}, "sameAs": [IG, TT]}

HEAD = """<!doctype html>
<html lang="fr">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="https://avitime.fr{path}">
<meta property="og:type" content="{ogtype}">
<meta property="og:locale" content="fr_FR">
<meta property="og:site_name" content="Avitime">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="https://avitime.fr{path}">
<meta property="og:image" content="https://avitime.fr/assets/img/og-image.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="/favicon.ico" sizes="any">
<link rel="icon" type="image/png" sizes="32x32" href="/assets/img/icon-32.png">
<link rel="apple-touch-icon" href="/assets/img/icon-180.png">
<meta name="theme-color" content="#0A0A0A">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700&family=Geist+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="/assets/css/style.css?v=cd85ec8812">
<style>
.gd-hero{{padding-block:clamp(56px,8vw,96px) 24px;text-align:left}}
.gd-wrap{{max-width:760px;margin-inline:auto;padding-inline:22px}}
.gd-hero h1{{font-size:clamp(34px,5vw,56px);letter-spacing:-.045em;line-height:1.05;margin:14px 0 0;text-wrap:balance}}
.gd-lede{{font-size:clamp(18px,2vw,21px);color:var(--ink-2);line-height:1.5;margin:20px 0 0}}
.gd-by{{display:flex;gap:14px;align-items:center;margin-top:28px;padding-top:20px;border-top:1px solid var(--line)}}
.gd-by .av{{width:44px;height:44px;border-radius:50%;background:var(--bg-2);display:grid;place-items:center;font-weight:700;color:var(--hl-ink);box-shadow:0 0 0 2px var(--hl);flex:none}}
.gd-by p{{margin:0;font-size:14px;color:var(--ink-2);line-height:1.4}}
.gd-by b{{color:var(--ink)}}
.gd-body{{padding-block:8px 72px}}
.gd-body h2{{font-size:clamp(24px,3vw,32px);letter-spacing:-.035em;line-height:1.12;margin:48px 0 14px}}
.gd-body h3{{font-size:20px;letter-spacing:-.02em;margin:28px 0 8px}}
.gd-body p,.gd-body li{{font-size:17.5px;line-height:1.65;color:var(--ink-2)}}
.gd-body p b,.gd-body li b{{color:var(--ink)}}
.gd-body ul,.gd-body ol{{padding-left:22px;display:grid;gap:6px}}
.gd-key{{background:var(--surface);border:1px solid var(--line);border-left:4px solid var(--hl);border-radius:16px;padding:18px 22px;margin:26px 0}}
.gd-key p{{margin:0}}
.gd-toc{{background:var(--surface);border:1px solid var(--line);border-radius:18px;padding:18px 22px;margin:8px 0 8px}}
.gd-toc p{{margin:0 0 8px;font-family:var(--font-mono);font-size:12px;text-transform:uppercase;letter-spacing:.08em;color:var(--hl-ink)}}
.gd-toc ol{{margin:0;font-size:15.5px}}
.gd-toc a,.gd-body a{{color:var(--hl-ink)}}
.gd-src{{font-size:14px!important}}
.gd-src li{{font-size:14px!important;line-height:1.5!important}}
.gd-note{{font-size:13.5px!important;font-family:var(--font-mono);color:var(--ink-2)}}
.gd-cards{{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px;margin-top:36px}}
@media (max-width:700px){{.gd-cards{{grid-template-columns:minmax(0,1fr)}}}}
.gd-card{{display:block;background:var(--surface);border:1px solid var(--line);border-radius:22px;padding:24px;text-decoration:none;color:inherit;transition:border-color .2s ease}}
.gd-card:hover{{border-color:var(--hl)}}
.gd-card h2{{font-size:22px;letter-spacing:-.03em;margin:8px 0 8px;line-height:1.15}}
.gd-card p{{margin:0;color:var(--ink-2);font-size:15.5px;line-height:1.5}}
</style>
</head>
<body>
<header class="nav" id="top-nav">
<div class="wrap">
<a class="brand" href="/"><img alt="Avitime, accueil" height="40" src="/assets/img/avitime-logo-96.png" width="168"/></a>
<nav aria-label="Navigation principale" class="nav-links">
<a href="/#concept">Le concept</a>
<a href="/#commercants">Commerçants</a>
<a href="/devenir-testeur">Testeurs</a>
<a href="/guides/"{guides_current}>Guides</a>
<a href="/a-propos.html">À propos</a>
</nav>
<div class="nav-actions">
<a class="ghost" href="/espace-commercant">Espace commerçant</a>
<a class="btn-sm" href="/devenir-testeur">Devenir testeur</a>
</div>
</div>
</header>
<main id="contenu">
"""

FOOT = f"""</main>
<footer>
<div class="wrap">
<span>Avitime · En France, sur PrestaShop, WooCommerce et Shopify.</span>
<nav aria-label="Pages légales"><a href="/a-propos.html">À propos</a><a href="/guides/">Guides</a><a href="/a-propos.html#methode">Méthode de vérification</a><a href="/mentions-legales.html">Mentions légales</a><a href="/cgv.html">CGV commerçants</a><a href="/cgu-testeurs.html">CGU testeurs</a><a href="/confidentialite.html">Confidentialité</a></nav>
<nav aria-label="Réseaux sociaux"><a href="{IG}" rel="me noopener" target="_blank">Instagram</a><a href="{TT}" rel="me noopener" target="_blank">TikTok</a></nav>
</div>
</footer>
<script type="application/ld+json">{{ld}}</script>
<script src="/assets/js/main.js?v=19d91e0a16" defer></script>
</body>
</html>
"""

BYLINE = """<div class="gd-by"><div class="av" aria-hidden="true">CQ</div><p><b>Cyril Quémy</b>, fondateur d’Avitime<br>Publié le {pub} · lecture {read} min</p></div>"""

GUIDES = [
 {
  "slug": "faux-avis-loi",
  "seo_title": "Faux avis en ligne : ce que dit la loi en France (2026)",
  "seo_desc": "Faux avis, avis achetés, avis « vérifiés » sans vérification : ce que dit le Code de la consommation, les sanctions et les mentions obligatoires.",
  "title": "Faux avis en ligne : ce que dit la loi en France (2026)",
  "desc": "Faux avis, avis achetés, avis « vérifiés » sans vérification : ce que prévoit le Code de la consommation, les sanctions encourues et les informations obligatoires pour une boutique qui publie des avis.",
  "kicker": "Guide · Réglementation",
  "lede": "Publier de faux avis, en acheter ou présenter des avis comme vérifiés sans les vérifier : en France, ce sont des pratiques commerciales trompeuses. Voici ce que dit la loi, ce que vous risquez, et ce qu’une boutique doit afficher quand elle publie des avis.",
  "read": 6,
  "body": """
<nav class="gd-toc" aria-label="Sommaire"><p>Au sommaire</p><ol>
<li><a href="#interdit">Ce qui est interdit</a></li>
<li><a href="#sanctions">Les sanctions</a></li>
<li><a href="#obligations">Ce qu’une boutique doit afficher</a></li>
<li><a href="#controles">Les contrôles de la DGCCRF</a></li>
<li><a href="#bonnes-pratiques">Obtenir des avis sans risque</a></li>
</ol></nav>

<div class="gd-key"><p><b>L’essentiel :</b> un avis doit refléter une expérience réelle. Si vous affirmez que vos avis viennent de vrais clients, vous devez pouvoir le prouver. Et si un avis a été obtenu avec une contrepartie (un produit offert, par exemple), cela doit être indiqué.</p></div>

<h2 id="interdit">1. Ce qui est interdit</h2>
<p>Le Code de la consommation range plusieurs pratiques liées aux avis parmi les <b>pratiques commerciales trompeuses</b> (articles L121-2 à L121-4). D’après la DGCCRF, sont notamment visés :</p>
<ul>
<li><b>se faire passer pour un consommateur</b>, par exemple en rédigeant soi-même des avis sur ses produits ;</li>
<li><b>diffuser ou faire diffuser de faux avis</b>, positifs pour soi ou négatifs pour un concurrent, y compris par des proches, des particuliers rémunérés ou des sociétés spécialisées ;</li>
<li><b>affirmer que des avis viennent de clients</b> ayant réellement acheté ou utilisé le produit, sans avoir pris de mesures raisonnables pour le vérifier ;</li>
<li><b>modifier des avis</b> pour promouvoir un produit, ou ne publier que les avis positifs et écarter les négatifs.</li>
</ul>
<p>La responsabilité ne pèse pas seulement sur la boutique : le prestataire qui fournit les faux avis et les particuliers qui les rédigent peuvent aussi être poursuivis.</p>

<h2 id="sanctions">2. Les sanctions</h2>
<p>La pratique commerciale trompeuse est un délit. Selon la DGCCRF, elle est punie de <b>deux ans d’emprisonnement et de 300 000 € d’amende</b>. L’amende peut être portée à <b>10 % du chiffre d’affaires annuel moyen</b>, ou à 50 % des dépenses engagées pour la pratique.</p>
<p>Depuis la loi n° 2024-420 du 10 mai 2024, les peines sont alourdies quand la pratique est commise <b>en ligne</b> : jusqu’à <b>cinq ans d’emprisonnement et 750 000 € d’amende</b> pour une personne physique (3,75 millions d’euros pour une société).</p>
<p>À cela s’ajoute un risque moins visible mais bien réel : des plateformes comme Google peuvent supprimer des avis ou suspendre un compte, et une réputation entamée par un faux avis découvert est longue à reconstruire.</p>

<h2 id="obligations">3. Ce qu’une boutique doit afficher quand elle publie des avis</h2>
<p>L’article L111-7-2 du Code de la consommation et les articles D111-16 à D111-19 imposent une information <b>loyale, claire et transparente</b> sur la façon dont les avis sont collectés et publiés. En pratique, une boutique qui affiche des avis doit indiquer :</p>
<ul>
<li><b>si les avis sont contrôlés ou non</b>, et si oui, comment ;</li>
<li><b>la date de publication</b> de chaque avis, et la date de l’expérience quand elle est connue ;</li>
<li><b>les critères de classement</b> des avis (par exemple, du plus récent au plus ancien) ;</li>
<li><b>l’existence d’une contrepartie</b> quand un avis a été obtenu en échange d’un avantage, comme un produit offert ;</li>
<li>le <b>délai de publication et de conservation</b> des avis, et les raisons possibles d’un refus.</li>
</ul>
<p>La norme volontaire <b>NF ISO 20488</b>, citée par la DGCCRF, va dans le même sens : pas d’avis achetés, publication des avis positifs comme négatifs, affichage des plus récents en premier.</p>

<h2 id="controles">4. Les contrôles de la DGCCRF</h2>
<p>La DGCCRF enquête régulièrement sur les avis en ligne et sanctionne aussi bien les faux avis que les informations incomplètes sur le traitement des avis. Elle utilise des outils d’analyse pour repérer les avis suspects sur les grandes plateformes. Pour un commerçant, la meilleure protection reste simple : <b>des avis réels, une procédure écrite, et une transparence affichée</b>.</p>

<h2 id="bonnes-pratiques">5. Obtenir des avis sans prendre de risque</h2>
<ul>
<li><b>Demandez un avis à tous vos clients</b> après la livraison, pas seulement à ceux qui sont satisfaits.</li>
<li><b>Publiez tous les avis</b> authentiques, y compris les critiques, et répondez-y.</li>
<li><b>Si vous offrez un produit</b> en échange d’un test, dites-le clairement à côté de l’avis, et ne conditionnez jamais le cadeau à une bonne note.</li>
<li><b>Gardez une trace</b> : commande, livraison, date de l’avis. C’est ce qui permet de prouver qu’un avis est authentique.</li>
</ul>
<p>C’est exactement le cadre que nous avons construit chez Avitime : la boutique ne choisit pas ses testeurs, chaque produit testé passe par une vraie commande à 0 €, et chaque avis est publié avec la mention « Produit offert pour test — Testeur Avitime vérifié ». Voir notre <a href="/a-propos.html#methode">méthode de vérification</a>.</p>

<h2 id="sources">Sources</h2>
<ul class="gd-src">
<li>DGCCRF, <a href="https://www.economie.gouv.fr/dgccrf/Publications/Vie-pratique/Fiches-pratiques/Faux-avis-consommateurs-sur-internet" rel="noopener" target="_blank">« Avis en ligne : attention aux faux commentaires ! »</a></li>
<li>Code de la consommation : articles L111-7-2, L121-2 à L121-4, L132-2 et D111-16 à D111-19 (<a href="https://www.legifrance.gouv.fr/codes/section_lc/LEGITEXT000006069565/LEGISCTA000032221101/" rel="noopener" target="_blank">Légifrance</a>)</li>
<li>CMS Francis Lefebvre, <a href="https://cms.law/fr/fra/news-information/les-nouvelles-sanctions-pour-les-pratiques-commerciales-trompeuses-commises-en-ligne" rel="noopener" target="_blank">« Les nouvelles sanctions pour les pratiques commerciales trompeuses commises en ligne »</a> (loi n° 2024-420 du 10 mai 2024)</li>
<li>Norme NF ISO 20488, avis en ligne de consommateurs</li>
</ul>
<p class="gd-note">Article d’information générale, à jour au 15 octobre 2026. Il ne remplace pas le conseil d’un avocat pour votre situation.</p>
"""
 },
 {
  "slug": "premiers-avis-clients",
  "seo_title": "Premiers avis clients : comment les obtenir sans tricher",
  "seo_desc": "Boutique en ligne sans avis ? Les méthodes honnêtes pour obtenir vos premiers avis clients : demande après livraison, tests produits transparents.",
  "title": "Comment obtenir ses premiers avis clients quand on lance sa boutique",
  "desc": "Boutique en ligne sans avis ? Les méthodes honnêtes pour obtenir vos premiers avis clients : demande après livraison, tests produits transparents, réponses aux avis, et les erreurs qui coûtent cher.",
  "kicker": "Guide · E-commerce",
  "lede": "Sans avis, les visiteurs hésitent. Sans clients, pas d’avis. Ce cercle, je l’ai vu chez presque tous les commerçants pour qui j’ai créé un site. Voici les méthodes honnêtes pour en sortir, sans faux avis.",
  "read": 5,
  "body": """
<nav class="gd-toc" aria-label="Sommaire"><p>Au sommaire</p><ol>
<li><a href="#pourquoi">Pourquoi les premiers avis comptent autant</a></li>
<li><a href="#demander">Demander, au bon moment</a></li>
<li><a href="#tester">Faire tester vos produits, en toute transparence</a></li>
<li><a href="#repondre">Répondre à tous les avis</a></li>
<li><a href="#erreurs">Les erreurs à éviter</a></li>
</ol></nav>

<div class="gd-key"><p><b>L’essentiel :</b> les premiers avis viennent de deux sources honnêtes. Vos vrais clients, à qui vous demandez simplement leur avis au bon moment. Et des testeurs à qui vous offrez le produit, à condition de l’afficher clairement et de ne jamais exiger une bonne note.</p></div>

<h2 id="pourquoi">1. Pourquoi les premiers avis comptent autant</h2>
<p>Un produit sans avis paraît risqué : le visiteur ne sait pas si d’autres l’ont acheté, ni s’ils ont été satisfaits. Les avis rassurent, répondent aux questions concrètes (taille, qualité, durabilité) et enrichissent vos fiches produits de mots que vos clients utilisent vraiment.</p>
<p>Ils comptent aussi pour la visibilité : les moteurs de recherche et les assistants d’intelligence artificielle s’appuient de plus en plus sur ce que disent les clients pour recommander un produit. Une fiche sans avis leur donne peu de matière.</p>

<h2 id="demander">2. Demander, au bon moment</h2>
<p>C’est la méthode la plus simple, et la plus sous-utilisée. Beaucoup de clients satisfaits ne laissent pas d’avis parce que personne ne le leur demande.</p>
<ul>
<li><b>Choisissez le bon moment :</b> après la livraison et un temps d’utilisation raisonnable, pas le jour de la commande.</li>
<li><b>Faites court :</b> un e-mail personnel, une question, un lien direct vers le formulaire d’avis.</li>
<li><b>Demandez à tout le monde,</b> pas seulement aux clients qui vous semblent contents. Trier à l’avance fausse vos avis.</li>
<li><b>Relancez une seule fois,</b> poliment.</li>
</ul>

<h2 id="tester">3. Faire tester vos produits, en toute transparence</h2>
<p>Quand une boutique démarre, elle a peu de clients : il faut parfois provoquer les premiers avis. Offrir un produit à des testeurs est légal, à trois conditions :</p>
<ol>
<li><b>L’avis reste libre :</b> le produit est offert quelle que soit la note, et le testeur peut dire ce qu’il pense, y compris ce qui ne va pas.</li>
<li><b>La contrepartie est affichée :</b> l’avis porte une mention claire, du type « Produit offert pour test ».</li>
<li><b>Le testeur utilise vraiment le produit</b> avant de donner son avis.</li>
</ol>
<p>C’est le principe d’Avitime : des testeurs sélectionnés par Avitime (jamais par la boutique) commandent le produit à 0 € sur votre site, l’utilisent, puis publient un avis argumenté sur votre fiche produit, avec la mention « Produit offert pour test — Testeur Avitime vérifié ». <a href="/#concept">Voir comment ça marche</a>.</p>

<h2 id="repondre">4. Répondre à tous les avis</h2>
<p>Répondre montre aux futurs clients qu’il y a quelqu’un derrière la boutique. Remerciez pour les avis positifs, et répondez aux critiques avec des faits : ce que vous avez corrigé, ce que vous proposez. Un avis critique bien traité inspire souvent plus confiance qu’une page remplie de cinq étoiles.</p>

<h2 id="erreurs">5. Les erreurs à éviter</h2>
<ul>
<li><b>Écrire ou acheter des avis :</b> c’est une pratique commerciale trompeuse, lourdement sanctionnée. Voir notre guide <a href="/guides/faux-avis-loi.html">Faux avis en ligne : ce que dit la loi</a>.</li>
<li><b>Récompenser uniquement les bonnes notes,</b> ou proposer un geste commercial en échange d’un avis positif.</li>
<li><b>Masquer les avis négatifs</b> authentiques.</li>
<li><b>Afficher « avis vérifiés »</b> sans vérification réelle derrière.</li>
</ul>

<h2 id="sources">Sources</h2>
<ul class="gd-src">
<li>DGCCRF, <a href="https://www.economie.gouv.fr/dgccrf/Publications/Vie-pratique/Fiches-pratiques/Faux-avis-consommateurs-sur-internet" rel="noopener" target="_blank">« Avis en ligne : attention aux faux commentaires ! »</a></li>
<li>Code de la consommation : articles L111-7-2 et D111-16 à D111-19 (information sur le traitement des avis)</li>
</ul>
<p class="gd-note">Article d’information générale, à jour au 15 octobre 2026.</p>
"""
 },
]

def page_guide(g):
    path = f"/guides/{g['slug']}.html"
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "headline": g["title"], "description": g["desc"], "inLanguage": "fr-FR",
         "datePublished": "2026-10-15", "dateModified": "2026-10-15", "author": AUTHOR, "publisher": PUBLISHER,
         "mainEntityOfPage": f"https://avitime.fr{path}", "image": "https://avitime.fr/assets/img/og-image.jpg"},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Accueil", "item": "https://avitime.fr/"},
            {"@type": "ListItem", "position": 2, "name": "Guides", "item": "https://avitime.fr/guides/"},
            {"@type": "ListItem", "position": 3, "name": g["title"], "item": f"https://avitime.fr{path}"}]}]}
    out = HEAD.format(title=html.escape(g["seo_title"]), desc=html.escape(g["seo_desc"]), path=path, ogtype="article", guides_current=' aria-current="page"')
    out += (f'<article>\n<section class="gd-hero"><div class="gd-wrap">\n<p class="eyebrow"><a href="/guides/" style="color:inherit;text-decoration:none">Guides</a> · {g["kicker"].split("· ")[1]}</p>\n'
            f'<h1>{g["title"]}</h1>\n<p class="gd-lede">{g["lede"]}</p>\n'
            + BYLINE.format(pub="15 octobre 2026", read=g["read"]) + '\n</div></section>\n'
            f'<section class="gd-body"><div class="gd-wrap">{g["body"]}</div></section>\n</article>\n')
    out += FOOT.replace("{ld}", json.dumps(ld, ensure_ascii=False))
    open(os.path.join(OUT, f"{g['slug']}.html"), "w", encoding="utf-8").write(out)

def page_index():
    path = "/guides/"
    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Guides Avitime", "inLanguage": "fr-FR",
          "url": "https://avitime.fr/guides/", "hasPart": [{"@type": "Article", "headline": g["title"], "url": f"https://avitime.fr/guides/{g['slug']}.html", "author": AUTHOR} for g in GUIDES]}
    out = HEAD.format(title="Guides Avitime : avis clients et réglementation", desc="Guides pour les boutiques en ligne : obtenir ses premiers avis clients, comprendre la loi sur les faux avis et publier des avis transparents.", path=path, ogtype="website", guides_current=' aria-current="page"')
    cards = "".join(f'<a class="gd-card" href="/guides/{g["slug"]}.html"><p class="eyebrow">{g["kicker"]}</p><h2>{g["title"]}</h2><p>{g["desc"]}</p></a>' for g in GUIDES)
    out += ('<section class="gd-hero"><div class="gd-wrap" style="max-width:960px">\n<p class="eyebrow">Guides</p>\n'
            '<h1>Avis clients : nos guides pour les boutiques en ligne</h1>\n'
            '<p class="gd-lede">Des articles courts et sourcés pour obtenir de vrais avis, rester dans les règles et rassurer vos clients. Écrits par Cyril Quémy, fondateur d’Avitime.</p>\n'
            f'<div class="gd-cards">{cards}</div>\n</div></section>\n<div style="height:72px"></div>\n')
    out += FOOT.replace("{ld}", json.dumps(ld, ensure_ascii=False))
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(out)

if __name__ == "__main__":
    for g in GUIDES: page_guide(g)
    page_index()
    print(sorted(os.listdir(OUT)))
