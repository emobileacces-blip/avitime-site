"""Guides signés (E-E-A-T) : /guides/ — générés depuis ce script (même en-tête et pied de page que le site)."""
import json, os, html, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from site_footer import footer, SAME_AS
ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "public")
OUT = os.path.join(ROOT, "guides"); os.makedirs(OUT, exist_ok=True)
IG, TT = "https://www.instagram.com/avitime_fr/", "https://www.tiktok.com/@avitime_fr"
AUTHOR = {"@type": "Person", "name": "Cyril Quémy", "jobTitle": "Fondateur d’Avitime", "url": "https://avitime.fr/a-propos.html"}
PUBLISHER = {"@type": "Organization", "name": "Avitime", "url": "https://avitime.fr/", "logo": {"@type": "ImageObject", "url": "https://avitime.fr/assets/img/icon-512.png"}, "sameAs": SAME_AS}

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
<link rel="preload" href="/assets/fonts/geist-latin-400-normal.woff2" as="font" type="font/woff2" crossorigin>
<link rel="stylesheet" href="/assets/fonts/fonts.css?v=1">
<link rel="stylesheet" href="/assets/css/style.css?v=d602f768bd">
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
.gd-related{{border-top:1px solid var(--line);margin-top:48px;padding-top:28px}}
.gd-related h2{{margin-top:0}}
.gd-related .gd-cards{{grid-template-columns:repeat(3,minmax(0,1fr));margin-top:16px}}
@media (max-width:860px){{.gd-related .gd-cards{{grid-template-columns:minmax(0,1fr)}}}}
.gd-related .gd-card h2{{font-size:18px;margin:6px 0 0}}
.gd-cta{{display:flex;flex-wrap:wrap;gap:12px 24px;align-items:center;background:var(--band);color:var(--band-ink);border-radius:22px;padding:22px 26px;margin-top:36px}}
.gd-cta p{{margin:0;color:var(--band-ink)!important;font-size:16px!important;flex:1 1 280px}}
.gd-cta .btn{{background:var(--hl);color:#0A0A0A!important;text-decoration:none}}
.gd-cta p b{{color:var(--band-ink)!important}}
.gd-body .gd-card,.gd-body .gd-card h2{{color:var(--ink);text-decoration:none}}
.gd-tbl{{margin:18px 0 8px;border:1px solid var(--line);border-radius:18px;overflow-x:auto}}\n.gd-tbl table{{min-width:640px}}
.gd-tbl table{{font-size:15px}}
.gd-tbl th{{text-align:left;background:var(--bg-2);padding:12px 14px;font-size:13.5px;letter-spacing:.01em}}
.gd-tbl td{{padding:12px 14px;border-top:1px solid var(--line);vertical-align:top;color:var(--ink-2);line-height:1.45}}
.gd-tbl td:first-child{{color:var(--ink);font-weight:600}}
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
{footer("fr")}
<script type="application/ld+json">{{ld}}</script>
<script src="/assets/js/main.js?v=19d91e0a16" defer></script>
</body>
</html>
"""

BYLINE = """<div class="gd-by"><div class="av" aria-hidden="true" style="overflow:hidden"><img src="/assets/img/cyril-quemy-tete.webp" alt="" width="44" height="44" style="width:100%;height:100%;object-fit:cover;border-radius:50%"></div><p><b>Cyril Quémy</b>, fondateur d’Avitime<br>Publié le {pub} · lecture {read} min</p></div>"""

GUIDES = [
 {
  "slug": "avis-clients-ia",
  "related": ["combien-avis-clients", "avis-clients-prestashop", "premiers-avis-clients"],
  "seo_title": "Avis clients et IA : être recommandé par ChatGPT et Gemini",
  "seo_desc": "Vos clients demandent désormais à une IA quoi acheter. Pourquoi les avis clients décident si ChatGPT, Gemini ou Google recommandent vos produits.",
  "title": "Avis clients et IA : pourquoi vos avis décident si ChatGPT recommande vos produits",
  "desc": "Les acheteurs demandent de plus en plus à une IA quoi acheter. Ce que ces assistants regardent, pourquoi les avis clients comptent autant, et comment préparer vos fiches produits.",
  "kicker": "Guide · IA et visibilité",
  "lede": "« Quel est le meilleur coussin en lin pour un salon ? » Cette question, vos clients ne la tapent plus seulement dans Google : ils la posent à ChatGPT, à Gemini ou au mode IA de Google. Et pour répondre, ces assistants s’appuient sur ce que disent les clients. Une boutique sans avis a peu de chances d’être citée.",
  "read": 7,
  "body": """
<nav class="gd-toc" aria-label="Sommaire"><p>Au sommaire</p><ol>
<li><a href="#achat-ia">Les acheteurs passent par l’IA</a></li>
<li><a href="#comment">Comment une IA choisit un produit</a></li>
<li><a href="#pourquoi">Pourquoi les avis pèsent autant</a></li>
<li><a href="#quels-avis">Les avis qui comptent pour une IA</a></li>
<li><a href="#checklist">Préparer vos fiches produits</a></li>
</ol></nav>

<div class="gd-key"><p><b>L’essentiel :</b> une IA conversationnelle ne « voit » pas votre produit. Elle lit ce qui est écrit à son sujet. Des avis clients nombreux, détaillés et authentiques sur vos fiches produits lui donnent la matière pour vous recommander, et pour expliquer pourquoi.</p></div>

<h2 id="achat-ia">1. Les acheteurs passent désormais par l’IA</h2>
<p>Le changement est rapide. D’après le premier baromètre GEO de Valiuz, mené auprès de 13 grandes enseignes (Decathlon, Leroy Merlin, Boulanger, Kiabi…), <b>le trafic venu des IA génératives a été multiplié par 18</b> entre décembre 2024 et décembre 2025. Plus de 90 % de ce trafic vient de ChatGPT.</p>
<p>Deux chiffres de ce baromètre comptent particulièrement pour une petite boutique :</p>
<ul>
<li><b>72 % de ces visiteurs sont nouveaux</b> : l’IA envoie des clients qui ne connaissaient pas l’enseigne ;</li>
<li><b>90 % arrivent directement sur une fiche produit</b> : l’IA ne recommande pas un site, elle recommande un produit précis.</li>
</ul>
<p>Autrement dit, être cité par une IA, c’est être présenté à un acheteur qui a déjà décidé quoi chercher, au moment où il compare.</p>

<h2 id="comment">2. Comment une IA choisit un produit à recommander</h2>
<p>Chaque assistant a sa méthode, mais le principe est proche. L’IA découpe la question en sous-questions (prix, matière, usage, avis, disponibilité…), puis va chercher des réponses dans les pages qu’elle peut lire : fiches produits, comparatifs, forums, avis.</p>
<p>OpenAI le dit clairement pour ChatGPT : les produits proposés sont choisis selon la pertinence pour la demande, à partir de données structurées fournies par les marchands et par des tiers. Les <b>résumés d’avis sont rédigés par le modèle à partir de sites publics</b>, pour faire ressortir ce que les acheteurs aiment et n’aiment pas. Et ces résultats produits ne sont pas des publicités : on ne peut pas y acheter sa place.</p>
<p>Côté Google, le mode IA s’appuie sur le Shopping Graph, une immense base de fiches produits qui inclut les prix, la disponibilité et les avis.</p>

<h2 id="pourquoi">3. Pourquoi les avis pèsent autant</h2>
<p>Pour recommander un produit, une IA doit pouvoir dire <b>pour qui il est fait, ce qu’il vaut à l’usage et quels sont ses défauts</b>. Ces informations, la fiche produit les donne rarement. Les avis clients, si.</p>
<ul>
<li><b>Ils apportent des faits d’usage</b> : « tient bien au lavage », « taille petit », « idéal pour un petit balcon ». C’est exactement ce que l’acheteur demande à l’IA.</li>
<li><b>Ils permettent de comparer</b> : sans avis, deux produits se ressemblent ; avec des avis, l’IA peut expliquer pourquoi choisir l’un plutôt que l’autre.</li>
<li><b>Ils rassurent</b> : l’IA reprend souvent ce que « les clients soulignent ». Un produit sans avis ne lui donne rien à citer.</li>
</ul>
<p>Et l’effet ne se limite pas à l’IA. Une étude du Spiegel Research Center (Northwestern University) a montré qu’un produit avec <b>cinq avis</b> a une probabilité d’achat <b>270 % plus élevée</b> qu’un produit sans avis. Les premiers avis sont donc ceux qui comptent le plus.</p>

<h2 id="quels-avis">4. Les avis qui comptent pour une IA</h2>
<ul>
<li><b>Des avis détaillés</b> plutôt qu’un simple « super produit ». Un avis qui raconte le contexte, la durée d’utilisation, les points forts et les limites est bien plus utile.</li>
<li><b>Des avis visibles sur la fiche produit</b>, en texte lisible par un robot, pas seulement dans une fenêtre qui s’ouvre au clic.</li>
<li><b>Des avis récents et réguliers</b>, qui montrent que le produit se vend et que l’information est à jour.</li>
<li><b>Des avis authentiques</b>, positifs comme critiques. Une page remplie de cinq étoiles identiques paraît suspecte, aux acheteurs comme aux systèmes de détection. Et les faux avis sont lourdement sanctionnés : voir notre guide <a href="/guides/faux-avis-loi.html">Faux avis en ligne : ce que dit la loi</a>.</li>
</ul>
<p>Selon le Spiegel Research Center, la probabilité d’achat culmine d’ailleurs pour une note moyenne <b>entre 4,0 et 4,7</b> : une note parfaite inspire moins confiance qu’une note réaliste.</p>

<h2 id="checklist">5. Préparer vos fiches produits pour l’IA</h2>
<ol>
<li><b>Obtenez vos premiers avis</b>, même cinq par produit : demandez-les à vos clients après la livraison, ou faites tester vos produits de façon transparente (voir <a href="/guides/premiers-avis-clients.html">notre guide</a>).</li>
<li><b>Affichez les avis en texte</b> sur la fiche produit, avec le balisage de données structurées (Product, Review, AggregateRating) que lisent les moteurs.</li>
<li><b>Décrivez précisément vos produits</b> : matière, dimensions, usage, entretien. L’IA croise la description et les avis.</li>
<li><b>Répondez aux avis</b>, surtout aux critiques : vos réponses deviennent elles aussi une information publique.</li>
<li><b>Restez transparent</b> : un avis obtenu avec un produit offert doit le dire. C’est la loi, et c’est aussi ce qui rend l’avis crédible.</li>
</ol>
<p>C’est ce que fait Avitime : des testeurs sélectionnés par Avitime utilisent réellement vos produits, puis publient sur vos fiches des avis argumentés (avantages, limites, durée d’utilisation), avec la mention « Produit offert pour test — Testeur Avitime vérifié ». <a href="/#google-ia">Voir comment les avis nourrissent Google et les IA</a>.</p>

<h2 id="sources">Sources</h2>
<ul class="gd-src">
<li>OpenAI, <a href="https://help.openai.com/en/articles/11128490-improving-shopping-results-from-chatgpt-search" rel="noopener" target="_blank">« Improving shopping results from ChatGPT search »</a> (centre d’aide OpenAI)</li>
<li>E-Commerce Nation, <a href="https://www.ecommerce-nation.fr/?p=125702" rel="noopener" target="_blank">« Baromètre GEO : le trafic e-commerce issu des IA génératives multiplié par 18 en un an »</a> (baromètre Valiuz, février 2026)</li>
<li>Spiegel Research Center, Northwestern University, <a href="https://spiegel.medill.northwestern.edu/How-Online-Reviews-Influence-Sales" rel="noopener" target="_blank">« How Online Reviews Influence Sales »</a> (2017)</li>
<li>Channable, <a href="https://www.channable.com/blog/google-shopping-ai-mode" rel="noopener" target="_blank">« Google AI Mode for Shopping »</a> (fonctionnement du mode IA et du Shopping Graph)</li>
</ul>
<p class="gd-note">Article d’information générale, à jour au 15 octobre 2026. Le fonctionnement des assistants IA évolue vite : les principes restent, les détails changent.</p>
"""
 },
 {
  "slug": "faux-avis-loi",
  "related": ["premiers-avis-clients", "repondre-avis-negatifs", "arnaques-testeur-produits"],
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
  "related": ["combien-avis-clients", "avis-clients-ia", "comparatif-solutions-avis-clients"],
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
 {'slug': 'avis-clients-prestashop', 'seo_title': 'Avis clients PrestaShop : afficher de vrais avis vérifiés', 'seo_desc': 'Comment afficher des avis clients sur PrestaShop : le module natif Commentaires produits, ses limites, les étoiles dans Google et les avis vérifiés.', 'title': 'Avis clients sur PrestaShop : comment afficher de vrais avis vérifiés', 'desc': 'Le module natif « Commentaires produits », ce qu’il fait et ce qu’il ne fait pas, les étoiles dans Google, et comment obtenir des avis vérifiés sur une boutique PrestaShop.', 'kicker': 'Guide · PrestaShop', 'lede': 'PrestaShop sait afficher des avis clients, mais pas les obtenir à votre place. Voici ce que fait le module natif, ce qui lui manque, et comment remplir vos fiches produits d’avis réels et vérifiables.', 'read': 6, 'related': ['avis-clients-woocommerce', 'combien-avis-clients', 'avis-clients-ia'], 'body': '\n<nav class="gd-toc" aria-label="Sommaire"><p>Au sommaire</p><ol>\n<li><a href="#natif">Le module natif « Commentaires produits »</a></li>\n<li><a href="#limites">Ce qui lui manque</a></li>\n<li><a href="#google">Les étoiles dans Google</a></li>\n<li><a href="#obtenir">Obtenir vos premiers avis</a></li>\n<li><a href="#avitime">Avitime sur PrestaShop</a></li>\n</ol></nav>\n\n<div class="gd-key"><p><b>L’essentiel :</b> le module gratuit de PrestaShop suffit pour afficher et modérer des avis. Il ne sait ni les demander à vos clients, ni prouver qu’un avis vient d’un acheteur. C’est souvent là que les boutiques restent bloquées à zéro avis.</p></div>\n\n<h2 id="natif">1. Le module natif « Commentaires produits »</h2>\n<p>PrestaShop propose un module gratuit, <b>Commentaires produits</b> (productcomments). Selon la version de votre boutique, il est déjà installé ou se trouve dans le catalogue de modules. Il permet :</p>\n<ul>\n<li>une <b>note sur 5 étoiles</b>, avec des critères que vous définissez (qualité, rapport qualité-prix…) ;</li>\n<li>une <b>modération</b> : par défaut, un avis n’apparaît qu’après votre validation dans le back-office ;</li>\n<li>d’autoriser ou non les <b>visiteurs non connectés</b> à laisser un avis (désactivé par défaut) ;</li>\n<li>un vote « cet avis est-il utile ? ».</li>\n</ul>\n\n<h2 id="limites">2. Ce qui lui manque</h2>\n<ul>\n<li><b>Aucune demande d’avis automatique</b> après l’achat : il faut que le client pense à revenir sur la fiche produit. Résultat, peu d’avis.</li>\n<li><b>Pas de distinction entre acheteur et simple visiteur</b> : le module ne vérifie pas que l’auteur a acheté le produit, donc pas de badge « achat vérifié ».</li>\n<li><b>Pas de photos</b> dans les avis.</li>\n<li><b>Pas de balisage pour les étoiles dans Google</b> : cela dépend de votre thème ou d’un module SEO.</li>\n</ul>\n<p>Or la loi impose d’indiquer si vos avis sont contrôlés et comment (voir <a href="/guides/faux-avis-loi.html">Faux avis en ligne : ce que dit la loi</a>). Avec le module seul, vous ne pouvez pas affirmer que vos avis sont « vérifiés ».</p>\n\n<h2 id="google">3. Les étoiles dans les résultats Google</h2>\n<p>Pour que Google puisse afficher des étoiles sous vos produits, la fiche doit contenir des <b>données structurées</b> (Product, avec Review ou AggregateRating) qui décrivent les avis réellement visibles sur la page. Vérifiez si votre thème les génère, sinon ajoutez-les avec un module SEO. Google reste libre de les afficher ou non.</p>\n<p>Ces mêmes données aident les assistants IA à comprendre vos produits : voir <a href="/guides/avis-clients-ia.html">Avis clients et IA</a>.</p>\n\n<h2 id="obtenir">4. Obtenir vos premiers avis</h2>\n<ol>\n<li><b>Demandez un avis par e-mail</b> à chaque client, quelques jours après la livraison, avec un lien direct vers la fiche produit.</li>\n<li><b>Répondez aux avis</b>, y compris aux critiques (voir <a href="/guides/repondre-avis-negatifs.html">Répondre aux avis négatifs</a>).</li>\n<li><b>Faites tester vos produits</b> en toute transparence pour amorcer les premiers avis (voir <a href="/guides/premiers-avis-clients.html">Obtenir ses premiers avis clients</a>).</li>\n</ol>\n\n<h2 id="avitime">5. Avitime sur PrestaShop</h2>\n<p>Avitime a un <b>module PrestaShop</b> (versions 1.7.7 à 9). Des testeurs sélectionnés par Avitime commandent vos produits à 0 € : la commande arrive dans votre back-office avec l’état « Testeur Avitime », vous l’expédiez comme d’habitude, puis le testeur publie un avis argumenté avec la mention « Produit offert pour test — Testeur Avitime vérifié ». Chaque avis est relié à une vraie commande et à une livraison. <a href="/#commercants">Voir l’offre commerçants</a>.</p>\n\n<h2 id="sources">Sources</h2>\n<ul class="gd-src">\n<li>PrestaShop, module <a href="https://github.com/PrestaShop/productcomments" rel="noopener" target="_blank">productcomments</a> (dépôt officiel)</li>\n<li>MyPresta, <a href="https://mypresta.rocks/blog/product-reviews-prestashop-built-in-vs-third-party" rel="noopener" target="_blank">« Product reviews in PrestaShop: built-in vs third-party »</a></li>\n<li>Google Search Central, <a href="https://developers.google.com/search/docs/appearance/structured-data/review-snippet" rel="noopener" target="_blank">données structurées des extraits d’avis</a></li>\n</ul>\n<p class="gd-note">Article d’information générale, à jour au 15 octobre 2026. PrestaShop est une marque de son propriétaire ; Avitime est un service indépendant.</p>\n'},
 {'slug': 'avis-clients-woocommerce', 'seo_title': 'Avis clients WooCommerce : réglages et avis vérifiés', 'seo_desc': 'Activer et bien régler les avis clients sur WooCommerce : propriétaire vérifié, étoiles, modération, et comment obtenir vos premiers avis réels.', 'title': 'Avis clients sur WooCommerce : les bons réglages et les avis vérifiés', 'desc': 'Les réglages natifs des avis WooCommerce (propriétaire vérifié, étoiles obligatoires, modération) et comment obtenir des avis réels sur vos fiches produits.', 'kicker': 'Guide · WooCommerce', 'lede': 'WooCommerce gère les avis clients sans extension, avec une option précieuse : le badge « propriétaire vérifié ». Voici les bons réglages, et comment passer de zéro avis à vos premiers retours clients.', 'read': 5, 'related': ['avis-clients-shopify', 'premiers-avis-clients', 'faux-avis-loi'], 'body': '\n<nav class="gd-toc" aria-label="Sommaire"><p>Au sommaire</p><ol>\n<li><a href="#reglages">Les réglages natifs</a></li>\n<li><a href="#conseil">Nos recommandations</a></li>\n<li><a href="#moderation">Modérer sans trier</a></li>\n<li><a href="#obtenir">Obtenir vos premiers avis</a></li>\n<li><a href="#avitime">Avitime sur WooCommerce</a></li>\n</ol></nav>\n\n<div class="gd-key"><p><b>L’essentiel :</b> activez le badge « propriétaire vérifié » et la note obligatoire. Vos avis gagnent en crédibilité, et vous pouvez dire précisément comment ils sont contrôlés, comme la loi le demande.</p></div>\n\n<h2 id="reglages">1. Les réglages natifs</h2>\n<p>Dans <b>WooCommerce → Réglages → Produits</b>, rubrique Avis, cinq options :</p>\n<ul>\n<li><b>Activer les avis produits</b> ;</li>\n<li><b>Afficher le libellé « propriétaire vérifié »</b> sur les avis des clients qui ont acheté le produit ;</li>\n<li><b>Réserver les avis aux « propriétaires vérifiés »</b> ;</li>\n<li><b>Activer la note par étoiles</b> ;</li>\n<li><b>Rendre la note obligatoire</b>.</li>\n</ul>\n\n<h2 id="conseil">2. Nos recommandations</h2>\n<ul>\n<li><b>Activez le libellé « propriétaire vérifié »</b> : c’est une preuve simple et visible que l’avis vient d’un acheteur.</li>\n<li><b>Rendez la note obligatoire</b> : une note moyenne n’a de sens que si chaque avis en a une.</li>\n<li><b>Réserver les avis aux acheteurs</b> protège contre les avis fantaisistes, mais réduit le volume. Au lancement, quand vous avez peu de ventes, c’est un choix à peser.</li>\n<li><b>Indiquez sur votre site</b> comment vos avis sont contrôlés : c’est une obligation légale (voir <a href="/guides/faux-avis-loi.html">Faux avis en ligne : ce que dit la loi</a>).</li>\n</ul>\n\n<h2 id="moderation">3. Modérer sans trier</h2>\n<p>Les avis se gèrent dans <b>Produits → Avis</b> : approuver, répondre, marquer comme indésirable. Modérez pour écarter le spam, les insultes ou les données personnelles, <b>jamais pour masquer un avis critique authentique</b>. Une critique bien traitée rassure davantage qu’une page sans défaut (voir <a href="/guides/repondre-avis-negatifs.html">Répondre aux avis négatifs</a>).</p>\n\n<h2 id="obtenir">4. Obtenir vos premiers avis</h2>\n<p>WooCommerce n’envoie pas de demande d’avis après l’achat. Prévoyez un e-mail quelques jours après la livraison, avec un lien direct vers la fiche produit. Pour amorcer les premiers avis quand les ventes sont encore rares, voir <a href="/guides/premiers-avis-clients.html">Comment obtenir ses premiers avis clients</a> et <a href="/guides/combien-avis-clients.html">Combien d’avis faut-il pour vendre ?</a></p>\n\n<h2 id="avitime">5. Avitime sur WooCommerce</h2>\n<p>Avitime a une <b>extension WordPress pour WooCommerce</b> (WooCommerce 7 et plus, compatible HPOS et paiement en blocs). La commande du testeur arrive « En cours » à 0 € avec la mention « ★ Testeur Avitime », un encadré vous permet de saisir le suivi, et l’avis est publié avec la mention « Produit offert pour test — Testeur Avitime vérifié ». <a href="/#commercants">Voir l’offre commerçants</a>.</p>\n\n<h2 id="sources">Sources</h2>\n<ul class="gd-src">\n<li>WooCommerce, <a href="https://woocommerce.com/document/product-reviews/" rel="noopener" target="_blank">documentation « Product Reviews »</a></li>\n<li>Google Search Central, <a href="https://developers.google.com/search/docs/appearance/structured-data/review-snippet" rel="noopener" target="_blank">données structurées des extraits d’avis</a></li>\n</ul>\n<p class="gd-note">Article d’information générale, à jour au 15 octobre 2026. WooCommerce est une marque de son propriétaire ; Avitime est un service indépendant.</p>\n'},
 {'slug': 'avis-clients-shopify', 'seo_title': 'Avis clients Shopify : afficher des avis depuis 2024', 'seo_desc': 'Shopify a retiré son application d’avis en 2024. Comment afficher des avis clients sur Shopify aujourd’hui, et obtenir vos premiers avis réels.', 'title': 'Avis clients sur Shopify : comment faire depuis la fin de l’application officielle', 'desc': 'Shopify a retiré son application Product Reviews en 2024. Ce qu’il faut savoir pour afficher des avis sur votre boutique Shopify et obtenir vos premiers avis réels.', 'kicker': 'Guide · Shopify', 'lede': 'Pendant des années, Shopify proposait sa propre application d’avis gratuite. Elle a été retirée en 2024 : aujourd’hui, afficher des avis passe par une application tierce. Voici comment choisir, et comment obtenir des avis à afficher.', 'read': 5, 'related': ['avis-clients-prestashop', 'avis-clients-ia', 'comparatif-solutions-avis-clients'], 'body': '\n<nav class="gd-toc" aria-label="Sommaire"><p>Au sommaire</p><ol>\n<li><a href="#fin">La fin de l’application officielle</a></li>\n<li><a href="#choisir">Choisir une application d’avis</a></li>\n<li><a href="#google">Étoiles dans Google et IA</a></li>\n<li><a href="#obtenir">Obtenir vos premiers avis</a></li>\n<li><a href="#avitime">Avitime sur Shopify</a></li>\n</ol></nav>\n\n<div class="gd-key"><p><b>L’essentiel :</b> sur Shopify, l’application d’avis est un choix à faire dès le lancement. Vérifiez trois points : les avis sont-ils liés à une commande, sont-ils lisibles par Google, et pouvez-vous les exporter ?</p></div>\n\n<h2 id="fin">1. La fin de l’application officielle</h2>\n<p>Shopify a annoncé le retrait de son application gratuite <b>Product Reviews</b> à partir du <b>6 mai 2024</b>. Les marchands devaient exporter leurs avis et passer par une autre application. Depuis, les avis sur Shopify passent par des applications de l’App Store.</p>\n\n<h2 id="choisir">2. Choisir une application d’avis</h2>\n<ul>\n<li><b>Lien avec les commandes</b> : l’application doit pouvoir signaler les avis d’acheteurs vérifiés.</li>\n<li><b>Demande d’avis automatique</b> après la livraison, avec un délai réglable.</li>\n<li><b>Données structurées</b> sur la fiche produit, pour Google et les assistants IA.</li>\n<li><b>Export des avis</b> : vos avis vous appartiennent. Leçon du retrait de 2024, gardez toujours la possibilité de partir avec eux.</li>\n<li><b>Transparence</b> : affichage de la date, des avis critiques, et d’une mention quand un produit a été offert (voir <a href="/guides/faux-avis-loi.html">ce que dit la loi</a>).</li>\n</ul>\n\n<h2 id="google">3. Étoiles dans Google et visibilité dans les IA</h2>\n<p>Les étoiles sous un produit dans Google viennent des données structurées (Product, Review, AggregateRating) que votre application ou votre thème ajoute à la page. Ce sont aussi ces avis, en texte sur la fiche, que lisent ChatGPT, Gemini et le mode IA de Google : voir <a href="/guides/avis-clients-ia.html">Avis clients et IA</a>.</p>\n\n<h2 id="obtenir">4. Obtenir vos premiers avis</h2>\n<p>Une application affiche des avis, elle ne les crée pas. Au lancement, deux sources honnêtes : vos premiers clients, à qui vous demandez leur avis après la livraison, et des tests produits transparents. Voir <a href="/guides/premiers-avis-clients.html">Comment obtenir ses premiers avis clients</a>.</p>\n\n<h2 id="avitime">5. Avitime sur Shopify</h2>\n<p>L’application Avitime pour Shopify est <b>en cours de validation sur le Shopify App Store</b>. Le testeur valide sa commande à 0 € depuis son espace Avitime, la commande est créée dans votre boutique, et l’avis est publié sur la fiche produit avec la mention « Produit offert pour test — Testeur Avitime vérifié ». <a href="/#commercants">Être prévenu du lancement</a>.</p>\n\n<h2 id="sources">Sources</h2>\n<ul class="gd-src">\n<li>Communauté Shopify, <a href="https://community.shopify.com/t/whats-going-on-with-the-product-reviews-app-its-no-longer-available/249489" rel="noopener" target="_blank">discussion sur le retrait de Product Reviews</a></li>\n<li>Junip, <a href="https://junip.co/blog/what-to-do-about-shopify-product-reviews-app-being-deprecated-in-may-2024/" rel="noopener" target="_blank">« Shopify Product Reviews app deprecated in May 2024 »</a></li>\n<li>Google Search Central, <a href="https://developers.google.com/search/docs/appearance/structured-data/review-snippet" rel="noopener" target="_blank">données structurées des extraits d’avis</a></li>\n</ul>\n<p class="gd-note">Article d’information générale, à jour au 15 octobre 2026. Shopify est une marque de son propriétaire ; Avitime est un service indépendant.</p>\n'},
 {'slug': 'repondre-avis-negatifs', 'seo_title': 'Répondre à un avis négatif : méthode et exemples', 'seo_desc': 'Comment répondre à un avis client négatif sur votre boutique en ligne : la méthode en 4 étapes, des exemples de réponses et les erreurs à éviter.', 'title': 'Répondre à un avis négatif : la méthode et des exemples', 'desc': 'Un avis critique bien traité rassure davantage qu’une page parfaite. La méthode en quatre étapes, des exemples de réponses et les erreurs à éviter.', 'kicker': 'Guide · Relation client', 'lede': 'Un avis critique n’est pas une catastrophe. Pour les futurs clients, c’est surtout l’occasion de voir comment vous réagissez quand quelque chose ne va pas. Voici une méthode simple, et des exemples à adapter.', 'read': 5, 'related': ['combien-avis-clients', 'premiers-avis-clients', 'faux-avis-loi'], 'body': '\n<nav class="gd-toc" aria-label="Sommaire"><p>Au sommaire</p><ol>\n<li><a href="#pourquoi">Pourquoi répondre</a></li>\n<li><a href="#methode">La méthode en 4 étapes</a></li>\n<li><a href="#exemples">Exemples de réponses</a></li>\n<li><a href="#erreurs">Les erreurs à éviter</a></li>\n</ol></nav>\n\n<div class="gd-key"><p><b>L’essentiel :</b> vous ne répondez pas seulement au client mécontent, vous répondez à tous ceux qui liront l’avis ensuite. Restez factuel, proposez une solution, et ne supprimez jamais un avis authentique parce qu’il est critique.</p></div>\n\n<h2 id="pourquoi">1. Pourquoi répondre</h2>\n<ul>\n<li><b>Les futurs clients lisent vos réponses</b> : elles montrent qu’il y a quelqu’un derrière la boutique.</li>\n<li><b>Une note parfaite inspire moins confiance</b> : selon le Spiegel Research Center, la probabilité d’achat culmine pour une note entre 4,0 et 4,7, pas à 5 (voir <a href="/guides/combien-avis-clients.html">Combien d’avis faut-il pour vendre ?</a>).</li>\n<li><b>Votre réponse devient une information publique</b>, que lisent aussi les moteurs de recherche et les assistants IA (voir <a href="/guides/avis-clients-ia.html">Avis clients et IA</a>).</li>\n</ul>\n\n<h2 id="methode">2. La méthode en 4 étapes</h2>\n<ol>\n<li><b>Remercier</b> pour le retour, sans formule toute faite.</li>\n<li><b>Reconnaître le problème</b> précis, sans se justifier en bloc.</li>\n<li><b>Expliquer ou corriger</b> : ce qui s’est passé, et ce que vous avez changé.</li>\n<li><b>Proposer une solution</b> et un contact direct pour la suite.</li>\n</ol>\n<p>Répondez vite, en quelques jours, et relisez à froid avant de publier.</p>\n\n<h2 id="exemples">3. Exemples de réponses</h2>\n<h3>Produit qui ne correspond pas à la description</h3>\n<p><i>« Merci d’avoir pris le temps de nous écrire. Vous avez raison : la photo rend la couleur plus claire qu’elle ne l’est. Nous avons ajouté une photo à la lumière du jour sur la fiche. Écrivez-nous à contact@… : nous vous proposons un échange ou un remboursement. »</i></p>\n<h3>Livraison en retard</h3>\n<p><i>« Désolés pour ce retard, ce n’est pas le délai que nous annonçons. Le transporteur a eu un incident sur votre zone cette semaine-là. Nous avons ajouté un second transporteur pour éviter que cela se reproduise. Merci pour votre patience. »</i></p>\n<h3>Critique sur un défaut réel</h3>\n<p><i>« Merci pour cet avis précis. Le fermoir est effectivement le point faible de ce modèle : nous l’avons signalé au fabricant et la prochaine série en aura un renforcé. En attendant, nous vous envoyons un fermoir de remplacement. »</i></p>\n\n<h2 id="erreurs">4. Les erreurs à éviter</h2>\n<ul>\n<li><b>Supprimer ou masquer un avis authentique</b> : c’est trompeur pour les clients, et risqué au regard de la loi (voir <a href="/guides/faux-avis-loi.html">Faux avis en ligne : ce que dit la loi</a>).</li>\n<li><b>Contacter le client pour qu’il modifie sa note</b> en échange d’un geste commercial.</li>\n<li><b>Répondre sur le ton du reproche</b>, ou dévoiler des informations personnelles sur la commande.</li>\n<li><b>Copier-coller la même réponse</b> sous chaque avis.</li>\n</ul>\n<p>Chez Avitime, la boutique peut répondre à l’avis d’un testeur, mais elle ne peut ni le modifier, ni le supprimer, ni contacter le testeur à propos de sa note. Voir notre <a href="/a-propos.html#methode">méthode de vérification</a>.</p>\n\n<h2 id="sources">Sources</h2>\n<ul class="gd-src">\n<li>Spiegel Research Center, Northwestern University, <a href="https://spiegel.medill.northwestern.edu/How-Online-Reviews-Influence-Sales" rel="noopener" target="_blank">« How Online Reviews Influence Sales »</a></li>\n<li>DGCCRF, <a href="https://www.economie.gouv.fr/dgccrf/Publications/Vie-pratique/Fiches-pratiques/Faux-avis-consommateurs-sur-internet" rel="noopener" target="_blank">« Avis en ligne : attention aux faux commentaires ! »</a></li>\n</ul>\n<p class="gd-note">Article d’information générale, à jour au 15 octobre 2026. Les exemples de réponses sont fictifs, à adapter à votre situation.</p>\n'},
 {'slug': 'combien-avis-clients', 'seo_title': 'Combien d’avis clients faut-il pour vendre en ligne ?', 'seo_desc': 'Combien d’avis faut-il sur une fiche produit ? Ce que montrent les études : l’effet des 5 premiers avis, la note idéale entre 4,0 et 4,7 et les avis vérifiés.', 'title': 'Combien d’avis clients faut-il pour vendre ? Les chiffres qui comptent', 'desc': 'L’effet des cinq premiers avis, la note qui inspire le plus confiance, le poids des avis vérifiés : ce que disent les études, et ce qu’il faut viser.', 'kicker': 'Guide · E-commerce', 'lede': 'Faut-il cent avis pour rassurer un client ? Non. Les études montrent que ce sont les tout premiers avis qui changent le plus les ventes, et qu’une note parfaite n’est pas la meilleure. Voici les chiffres à retenir.', 'read': 4, 'related': ['premiers-avis-clients', 'avis-clients-ia', 'comparatif-solutions-avis-clients'], 'body': '\n<nav class="gd-toc" aria-label="Sommaire"><p>Au sommaire</p><ol>\n<li><a href="#cinq">Le cap des cinq avis</a></li>\n<li><a href="#note">La note qui inspire confiance</a></li>\n<li><a href="#verifies">Le poids des avis vérifiés</a></li>\n<li><a href="#viser">Ce qu’il faut viser</a></li>\n</ol></nav>\n\n<div class="gd-key"><p><b>L’essentiel :</b> passer de zéro à cinq avis sur un produit compte plus que passer de cinquante à cent. Visez d’abord quelques avis détaillés et vérifiés sur chacun de vos produits phares.</p></div>\n\n<h2 id="cinq">1. Le cap des cinq avis</h2>\n<p>Le Spiegel Research Center (Northwestern University) a analysé les ventes de sites e-commerce : un produit avec <b>cinq avis</b> a une probabilité d’achat <b>270 % plus élevée</b> qu’un produit sans avis. Au-delà, chaque avis supplémentaire apporte de moins en moins.</p>\n<p>L’effet est plus fort sur les produits chers : <b>+380 %</b> pour un produit cher, contre +190 % pour un produit bon marché. Plus l’achat engage, plus le client a besoin d’être rassuré.</p>\n\n<h2 id="note">2. La note qui inspire confiance</h2>\n<p>Selon la même étude, la probabilité d’achat culmine pour une note moyenne <b>entre 4,0 et 4,7</b>, puis baisse quand la note s’approche de 5. Une note parfaite paraît trop belle pour être vraie. Les avis critiques authentiques, et la façon dont vous y répondez, renforcent la confiance (voir <a href="/guides/repondre-avis-negatifs.html">Répondre aux avis négatifs</a>).</p>\n\n<h2 id="verifies">3. Le poids des avis vérifiés</h2>\n<p>Un badge « acheteur vérifié » augmente la probabilité d’achat de <b>15 %</b>, toujours d’après le Spiegel Research Center. Les clients font davantage confiance à un avis dont ils savent qu’il vient d’une vraie commande. Dire comment vos avis sont vérifiés est d’ailleurs une obligation (voir <a href="/guides/faux-avis-loi.html">ce que dit la loi</a>).</p>\n\n<h2 id="viser">4. Ce qu’il faut viser</h2>\n<ul>\n<li><b>Au moins cinq avis</b> sur chacun de vos produits phares.</li>\n<li><b>Des avis détaillés</b> (contexte, durée d’utilisation, points forts et limites) : ils convainquent les clients et nourrissent les assistants IA (voir <a href="/guides/avis-clients-ia.html">Avis clients et IA</a>).</li>\n<li><b>Des avis réguliers</b>, plutôt qu’un pic au lancement puis plus rien.</li>\n<li><b>Des avis vérifiés</b>, reliés à une commande.</li>\n</ul>\n<p>Pour y arriver sans tricher, voir <a href="/guides/premiers-avis-clients.html">Comment obtenir ses premiers avis clients</a>. Avitime a été pensé pour ça : quelques testeurs par produit, chacun relié à une vraie commande, pour franchir le cap des premiers avis. <a href="/#concept">Voir le concept</a>.</p>\n\n<h2 id="sources">Sources</h2>\n<ul class="gd-src">\n<li>Spiegel Research Center, Northwestern University, <a href="https://spiegel.medill.northwestern.edu/How-Online-Reviews-Influence-Sales" rel="noopener" target="_blank">« How Online Reviews Influence Sales »</a> (2017)</li>\n</ul>\n<p class="gd-note">Article d’information générale, à jour au 15 octobre 2026.</p>\n'},
 {'slug': 'arnaques-testeur-produits', 'seo_title': 'Testeur de produits gratuit : les arnaques à éviter', 'seo_desc': 'Devenir testeur de produits gratuitement sans se faire avoir : les signes d’une arnaque (frais à payer, carte bancaire, faux recrutement) et où signaler.', 'title': 'Testeur de produits gratuit : les arnaques à éviter', 'desc': 'Frais de port à payer, carte bancaire demandée, abonnement caché : les signes d’une fausse offre de test de produits, et comment reconnaître un programme sérieux.', 'kicker': 'Guide · Testeurs', 'lede': '« Recevez des produits gratuits à tester » : la promesse attire, et certains en profitent. Voici les signes qui doivent vous alerter, et ce qu’un programme de test sérieux ne vous demandera jamais.', 'read': 4, 'related': ['premiers-avis-clients', 'faux-avis-loi', 'avis-clients-ia'], 'body': '\n<nav class="gd-toc" aria-label="Sommaire"><p>Au sommaire</p><ol>\n<li><a href="#signes">Les signes d’une arnaque</a></li>\n<li><a href="#serieux">Ce que fait un programme sérieux</a></li>\n<li><a href="#avis">Le piège des avis rémunérés</a></li>\n<li><a href="#signaler">Où signaler</a></li>\n</ol></nav>\n\n<div class="gd-key"><p><b>La règle d’or :</b> un vrai programme de test ne vous demande jamais d’argent. Ni frais de port, ni « frais de dossier », ni numéro de carte bancaire.</p></div>\n\n<h2 id="signes">1. Les signes d’une arnaque</h2>\n<ul>\n<li><b>Des frais à payer</b>, même petits : « seulement les frais de port », « frais d’inscription ».</li>\n<li><b>Votre carte bancaire demandée</b> pour « vérifier votre identité » : c’est souvent la porte d’un abonnement caché.</li>\n<li><b>Une offre trop belle</b> : smartphone ou console « offerts » contre un simple avis.</li>\n<li><b>Une urgence artificielle</b> : « plus que 2 places, inscrivez-vous en 10 minutes ».</li>\n<li><b>Un contact par message privé</b> (WhatsApp, Telegram) pour un « emploi de testeur » payé à la tâche.</li>\n<li><b>Aucune société identifiable</b> : pas de mentions légales, pas d’adresse, pas de conditions d’utilisation.</li>\n</ul>\n\n<h2 id="serieux">2. Ce que fait un programme sérieux</h2>\n<ul>\n<li><b>Il est gratuit de bout en bout</b> : produit et livraison offerts.</li>\n<li><b>Il publie ses règles</b> : conditions d’utilisation, délais, ce qu’on attend de vous.</li>\n<li><b>Il affiche son identité</b> : société, mentions légales, contact.</li>\n<li><b>Il vous laisse libre de votre avis</b>, et le signale comme « produit offert ».</li>\n</ul>\n<p>C’est le cas d’Avitime : inscription gratuite, produit et livraison offerts, <a href="/cgu-testeurs.html">conditions publiques</a>, <a href="/mentions-legales.html">société identifiée</a>, et une règle écrite noir sur blanc : Avitime ne demande jamais de paiement à un testeur. Voir <a href="/devenir-testeur">comment devenir testeur</a>.</p>\n\n<h2 id="avis">3. Le piège des avis rémunérés</h2>\n<p>Certaines offres proposent de l’argent pour publier des avis cinq étoiles sur des produits que vous n’avez jamais utilisés. Ce n’est pas un test : c’est de la fabrication de faux avis, et <b>les particuliers qui les rédigent engagent aussi leur responsabilité</b>. Voir <a href="/guides/faux-avis-loi.html">Faux avis en ligne : ce que dit la loi</a>.</p>\n\n<h2 id="signaler">4. Où signaler</h2>\n<ul>\n<li><a href="https://signal.conso.gouv.fr" rel="noopener" target="_blank">SignalConso</a>, le service de la DGCCRF pour signaler une pratique commerciale douteuse ;</li>\n<li><a href="https://www.cybermalveillance.gouv.fr" rel="noopener" target="_blank">Cybermalveillance.gouv.fr</a>, pour l’assistance aux victimes d’arnaques en ligne ;</li>\n<li><a href="https://www.internet-signalement.gouv.fr" rel="noopener" target="_blank">Pharos</a>, pour signaler un contenu illicite en ligne.</li>\n</ul>\n<p>Si vous avez donné vos coordonnées bancaires, faites opposition auprès de votre banque sans attendre.</p>\n<p class="gd-note">Article d’information générale, à jour au 15 octobre 2026.</p>\n'},
 {'slug': 'comparatif-solutions-avis-clients', 'pub_iso': '2026-10-16', 'pub_fr': '16 octobre 2026', 'seo_title': 'Solutions d’avis clients : le comparatif honnête (2026)', 'seo_desc': 'Avis Vérifiés, Trustpilot, Google, clubs de testeurs, Amazon Vine, Reviewers.com, Avitime : quelle solution pour obtenir de vrais avis clients ?', 'title': 'Solutions d’avis clients : le comparatif honnête pour les boutiques en ligne', 'desc': 'Collecte d’avis, clubs de testeurs, programmes de marketplace, échantillonnage : ce que fait chaque type de solution, et laquelle règle le problème du « zéro avis ».', 'kicker': 'Guide · Comparatif', 'lede': 'Avis Vérifiés, Trustpilot, Google, Sampleo, Amazon Vine, Reviewers.com… Les solutions d’avis clients se ressemblent sur le papier, mais elles ne répondent pas au même problème. Voici comment elles fonctionnent, pour qui elles sont faites, et ce qu’elles ne font pas.', 'read': 8, 'related': ['combien-avis-clients', 'statistiques-avis-clients', 'faux-avis-loi'], 'body': '\n<nav class="gd-toc" aria-label="Sommaire"><p>Au sommaire</p><ol>\n<li><a href="#collecte">Les plateformes de collecte d’avis</a></li>\n<li><a href="#clubs">Les clubs de testeurs grand public</a></li>\n<li><a href="#marketplace">Les programmes des marketplaces</a></li>\n<li><a href="#echantillonnage">L’échantillonnage relié à la boutique</a></li>\n<li><a href="#tableau">Le tableau récapitulatif</a></li>\n<li><a href="#choisir">Comment choisir</a></li>\n</ol></nav>\n\n<div class="gd-key"><p><b>L’essentiel :</b> la plupart des solutions d’avis <b>collectent</b> les avis de vos acheteurs. C’est indispensable, mais ça ne règle pas le problème d’une boutique qui démarre : sans clients, pas d’avis. Pour obtenir les tout premiers avis, il faut faire <b>tester</b> vos produits, en toute transparence. Les deux approches se complètent.</p></div>\n\n<h2 id="collecte">1. Les plateformes de collecte d’avis</h2>\n<p>C’est la famille la plus connue : <b>Avis Vérifiés</b>, <b>Trustpilot</b>, <b>Trusted Shops</b>, <b>Société des Avis Garantis</b>, ou le programme gratuit <b>Google Avis clients</b>. Leur principe : après un achat, le client reçoit une invitation à donner son avis, qui est ensuite modéré et affiché sur votre site, sur la plateforme et parfois dans Google.</p>\n<ul>\n<li><b>Leur force :</b> des avis d’acheteurs réels, en volume, avec un processus de collecte automatisé.</li>\n<li><b>Les différences :</b> certaines sont ouvertes (sur Trustpilot, n’importe quel consommateur peut publier un avis sur une entreprise), d’autres ne recueillent que les avis de clients ayant passé commande.</li>\n<li><b>Leur limite :</b> elles ont besoin de commandes pour fonctionner. Google indique par exemple qu’il faut en général <b>au moins 100 avis</b> pour calculer une note de marchand fiable.</li>\n</ul>\n<p>Pour une boutique déjà installée, c’est un excellent outil. Pour une boutique qui lance ses premiers produits, la collecte tourne à vide.</p>\n\n<h2 id="clubs">2. Les clubs de testeurs grand public</h2>\n<p><b>Sampleo</b>, <b>TRND</b>, <b>Home Tester Club</b>, <b>The Insiders</b>, ou des clubs de marque comme <b>Kiabi Community</b> : des particuliers s’inscrivent pour tester des produits, souvent gratuitement, puis répondent à un questionnaire, rédigent un compte rendu ou parlent du produit autour d’eux et sur les réseaux sociaux.</p>\n<ul>\n<li><b>Leur force :</b> de grandes communautés et une vraie expérience de campagnes de bouche-à-oreille.</li>\n<li><b>Leur limite :</b> ces opérations s’adressent surtout aux <b>grandes marques</b>, et les retours restent souvent sur la plateforme ou les réseaux sociaux, <b>pas sur la fiche produit de votre boutique</b>.</li>\n</ul>\n\n<h2 id="marketplace">3. Les programmes des marketplaces</h2>\n<p>Le plus connu est <b>Amazon Vine</b> : Amazon sélectionne des membres de sa communauté, qui reçoivent gratuitement des produits et publient un avis signalé comme tel sur la fiche Amazon.</p>\n<ul>\n<li><b>Sa force :</b> un fonctionnement rodé, avec un affichage clair de la contrepartie.</li>\n<li><b>Sa limite :</b> il ne concerne que les produits vendus sur Amazon. Les avis ne vont pas sur votre propre boutique.</li>\n</ul>\n\n<h2 id="echantillonnage">4. L’échantillonnage relié à la boutique</h2>\n<p>C’est la famille la plus récente : des testeurs reçoivent le produit, l’utilisent, puis leur avis est publié <b>sur la fiche produit de la marque</b>.</p>\n<ul>\n<li><b>Try &amp; Review</b>, connecté notamment à Yotpo : un réseau international d’essais produits, dont les avis remontent sur les fiches des marchands. Il vise surtout les marques déjà équipées d’outils d’avis avancés.</li>\n<li><b>Reviewers.com</b>, lancé par Loox en juin 2026 : les testeurs commandent le produit sur le site de la marque et publient un avis vidéo. Le service est réservé aux <b>boutiques Shopify basées aux États-Unis</b>, à partir de 150 $ par mois.</li>\n<li><b>Avitime</b> : des testeurs <b>sélectionnés par Avitime, jamais par la boutique</b>, majeurs et résidant en France, commandent le produit à 0 € sur votre boutique, l’utilisent, puis publient un avis argumenté sur votre fiche produit avec la mention « Produit offert pour test — Testeur Avitime vérifié ». Toutes les notes sont publiées, de 1 à 5 étoiles. Avitime fonctionne avec <b>PrestaShop et WooCommerce</b>, et l’application Shopify est en cours de validation.</li>\n</ul>\n<p>Attention à ne pas confondre ces services avec les sites qui <b>rémunèrent</b> des particuliers pour publier des avis : payer pour une note, c’est fabriquer de faux avis. Voir <a href="/guides/faux-avis-loi.html">Faux avis en ligne : ce que dit la loi</a>.</p>\n\n<h2 id="tableau">5. Le tableau récapitulatif</h2>\n<div class="tbl-wrap gd-tbl"><table>\n<thead><tr><th>Type de solution</th><th>Exemples</th><th>Règle le « zéro avis » ?</th><th>Où l’avis est publié</th></tr></thead>\n<tbody>\n<tr><td>Collecte d’avis</td><td>Avis Vérifiés, Trustpilot, Trusted Shops, Google Avis clients</td><td>Non : il faut déjà des acheteurs</td><td>Votre site, la plateforme, Google</td></tr>\n<tr><td>Clubs de testeurs</td><td>Sampleo, TRND, Home Tester Club, The Insiders</td><td>Pour les grandes marques</td><td>Plateforme du club, réseaux sociaux</td></tr>\n<tr><td>Programme de marketplace</td><td>Amazon Vine</td><td>Oui, sur Amazon seulement</td><td>Fiche Amazon</td></tr>\n<tr><td>Échantillonnage relié à la boutique</td><td>Try &amp; Review, Reviewers.com (Shopify, États-Unis), Avitime (France)</td><td>Oui</td><td>Fiche produit de votre boutique</td></tr>\n</tbody></table></div>\n\n<h2 id="choisir">6. Comment choisir : 5 questions à se poser</h2>\n<ol>\n<li><b>Avez-vous déjà des commandes régulières ?</b> Oui : une solution de collecte vous fera gagner du temps. Non : commencez par faire tester vos produits phares.</li>\n<li><b>Où voulez-vous voir les avis ?</b> Sur votre fiche produit, c’est là qu’ils rassurent l’acheteur et qu’ils nourrissent Google et les assistants IA (voir <a href="/guides/avis-clients-ia.html">Avis clients et IA</a>).</li>\n<li><b>Sur quelle plateforme est votre boutique ?</b> PrestaShop, WooCommerce, Shopify : vérifiez l’intégration avant tout.</li>\n<li><b>Qui choisit les testeurs ?</b> Si c’est la boutique, la neutralité de l’avis est discutable. Un tiers indépendant est préférable.</li>\n<li><b>La contrepartie est-elle affichée ?</b> Un avis obtenu avec un produit offert doit le dire. C’est la loi, et c’est ce qui le rend crédible.</li>\n</ol>\n<p>Dans la plupart des cas, la bonne stratégie combine les deux approches : quelques avis de testeurs pour franchir le cap des premiers avis (cinq par produit changent déjà beaucoup, voir <a href="/guides/combien-avis-clients.html">Combien d’avis faut-il pour vendre ?</a>), puis une collecte régulière auprès de vos acheteurs.</p>\n\n<h3>Sources</h3>\n<ul class="gd-src">\n<li>Loox, <a href="https://webdisclosure.com/press-release/loox-launches-reviewerscom-the-first-product-sampling-platform-built-exclusively-for-shopify-brands-bXNVYVxkiH6" rel="noopener" target="_blank">« Loox launches Reviewers.com »</a> (communiqué, juin 2026)</li>\n<li>Yotpo, <a href="https://www.yotpo.com/integrations/try-review/" rel="noopener" target="_blank">intégration Try &amp; Review</a></li>\n<li>Google, <a href="https://support.google.com/merchants/answer/190657?hl=fr" rel="noopener" target="_blank">« Présentation des notes de magasin »</a> (Merchant Center)</li>\n<li>Journal du Net, <a href="https://www.journaldunet.com/retail/1211302-vine-program-comment-fonctionne-la-boite-a-avis-d-amazon/" rel="noopener" target="_blank">« Vine program : comment fonctionne la boîte à avis d’Amazon »</a></li>\n<li>Bons Plans Mania, <a href="https://bonsplansmania.fr/article/top-sites-tester-produits-gratuits-2026" rel="noopener" target="_blank">« Top des sites pour tester des produits gratuits en 2026 »</a></li>\n</ul>\n<p class="gd-note">Comparatif d’information générale, établi à partir des informations publiques des services cités, à jour au 16 octobre 2026. Les offres évoluent : vérifiez les conditions de chaque service avant de choisir. Avitime est l’éditeur de ce guide.</p>\n'},
 {'slug': 'statistiques-avis-clients', 'pub_iso': '2026-10-16', 'pub_fr': '16 octobre 2026', 'seo_title': 'Statistiques avis clients 2026 : les chiffres clés (sources)', 'seo_desc': 'Les chiffres clés sur les avis clients en 2026 : lecture avant achat, effet des 5 premiers avis, note idéale, IA, faux avis et sanctions. Toutes les sources.', 'title': 'Statistiques avis clients 2026 : les chiffres clés, avec leurs sources', 'desc': 'Lecture des avis avant achat, effet des premiers avis, note idéale, avis et IA, faux avis et sanctions : les chiffres fiables sur les avis clients, réunis et sourcés.', 'kicker': 'Guide · Chiffres', 'lede': 'Combien de consommateurs lisent les avis ? Combien d’avis faut-il pour vendre ? Quelle part des sites triche ? Voici les chiffres les plus fiables sur les avis clients, réunis sur une seule page, chacun avec sa source.', 'read': 6, 'related': ['combien-avis-clients', 'avis-clients-ia', 'faux-avis-loi'], 'body': '\n<nav class="gd-toc" aria-label="Sommaire"><p>Au sommaire</p><ol>\n<li><a href="#cles">Les chiffres clés en un coup d’œil</a></li>\n<li><a href="#achat">Les avis et la décision d’achat</a></li>\n<li><a href="#combien">Combien d’avis, et quelle note</a></li>\n<li><a href="#ia">Avis clients et intelligence artificielle</a></li>\n<li><a href="#faux">Faux avis : l’ampleur du problème</a></li>\n<li><a href="#sanctions">Les sanctions en France</a></li>\n<li><a href="#citer">Citer ces chiffres</a></li>\n</ol></nav>\n\n<div class="gd-key"><p><b>L’essentiel :</b> trois consommateurs sur quatre lisent les avis avant d’acheter, et les cinq premiers avis d’un produit changent le plus ses ventes. Mais plus de la moitié des grands sites contrôlés en Europe ne respectaient pas les règles sur les avis. Chaque chiffre ci-dessous renvoie à sa source.</p></div>\n\n<h2 id="cles">1. Les chiffres clés en un coup d’œil</h2>\n<div class="tbl-wrap gd-tbl"><table>\n<thead><tr><th>Chiffre</th><th>Ce qu’il mesure</th><th>Source</th></tr></thead>\n<tbody>\n<tr><td><b>75 %</b></td><td>des consommateurs lisent les avis avant d’acheter</td><td>Avis Vérifiés, baromètre 2024 (France, Espagne, Italie)</td></tr>\n<tr><td><b>+270 %</b></td><td>de probabilité d’achat pour un produit avec 5 avis, par rapport à un produit sans avis</td><td>Spiegel Research Center, 2017</td></tr>\n<tr><td><b>4,0 à 4,7</b></td><td>la note moyenne qui maximise la probabilité d’achat</td><td>Spiegel Research Center, 2017</td></tr>\n<tr><td><b>+15 %</b></td><td>de probabilité d’achat avec un badge « acheteur vérifié »</td><td>Spiegel Research Center, 2017</td></tr>\n<tr><td><b>× 18</b></td><td>le trafic e-commerce venu des IA génératives, entre décembre 2024 et décembre 2025</td><td>Baromètre GEO Valiuz, 2026</td></tr>\n<tr><td><b>55 %</b></td><td>des grands sites contrôlés en Europe enfreignaient probablement le droit sur les avis</td><td>Commission européenne, 2022</td></tr>\n<tr><td><b>750 000 €</b></td><td>d’amende maximale pour une pratique trompeuse commise en ligne (5 ans de prison)</td><td>Loi n° 2024-420 du 10 mai 2024</td></tr>\n</tbody></table></div>\n\n<h2 id="achat">2. Les avis et la décision d’achat</h2>\n<p>Le baromètre Avis Vérifiés by Skeepers, mené auprès de <b>72 000 consommateurs</b> de 18 à 78 ans en France, en Espagne et en Italie et publié en juillet 2024, donne une photographie précise des habitudes :</p>\n<ul>\n<li><b>75 %</b> lisent les avis avant un achat.</li>\n<li><b>40 %</b> lisent entre 1 et 5 avis, <b>34 %</b> entre 6 et 10, et <b>26 %</b> plus de 10.</li>\n<li>Plus de <b>72 %</b> font confiance à la note moyenne et <b>65 %</b> au nombre d’avis.</li>\n<li><b>63 %</b> regardent comment la marque répond aux avis négatifs (deux étoiles ou moins).</li>\n<li><b>71 %</b> déposent leur avis dans les sept jours qui suivent l’achat, et <b>62 %</b> l’écrivent sur mobile.</li>\n<li>Mais <b>21 %</b> jugent que les avis manquent de crédibilité ou d’authenticité.</li>\n</ul>\n<p>Ce dernier chiffre résume l’enjeu : les avis pèsent sur la décision, à condition d’être crédibles. Voir <a href="/guides/repondre-avis-negatifs.html">Répondre aux avis négatifs</a>.</p>\n\n<h2 id="combien">3. Combien d’avis, et quelle note</h2>\n<p>Le Spiegel Research Center (Northwestern University) a analysé les ventes de sites e-commerce. Ses résultats restent la référence la plus citée :</p>\n<ul>\n<li>Un produit avec <b>5 avis</b> a une probabilité d’achat <b>270 % plus élevée</b> qu’un produit sans avis.</li>\n<li>L’effet est plus fort sur les produits chers : <b>+380 %</b>, contre <b>+190 %</b> pour un produit bon marché.</li>\n<li>La probabilité d’achat culmine pour une note moyenne <b>entre 4,0 et 4,7</b>, puis baisse quand la note approche 5.</li>\n<li>Un badge <b>« acheteur vérifié »</b> augmente la probabilité d’achat de <b>15 %</b>.</li>\n</ul>\n<p>Côté Google, il faut en général <b>au moins 100 avis</b> pour qu’une note de marchand s’affiche. Détails et conseils : <a href="/guides/combien-avis-clients.html">Combien d’avis faut-il pour vendre ?</a></p>\n\n<h2 id="ia">4. Avis clients et intelligence artificielle</h2>\n<p>Le premier baromètre GEO de Valiuz, mené auprès de 13 grandes enseignes (Decathlon, Leroy Merlin, Boulanger, Kiabi…), mesure l’arrivée des assistants IA dans le commerce en ligne :</p>\n<ul>\n<li>le trafic venu des IA génératives a été <b>multiplié par 18</b> entre décembre 2024 et décembre 2025 ;</li>\n<li>plus de <b>90 %</b> de ce trafic vient de ChatGPT ;</li>\n<li><b>72 %</b> de ces visiteurs sont nouveaux pour l’enseigne ;</li>\n<li><b>9 sur 10</b> arrivent directement sur une fiche produit.</li>\n</ul>\n<p>Pour recommander un produit, ces assistants s’appuient largement sur les avis publiés en texte sur la fiche. Voir <a href="/guides/avis-clients-ia.html">Avis clients et IA</a>.</p>\n\n<h2 id="faux">5. Faux avis : l’ampleur du problème</h2>\n<p>En janvier 2022, la Commission européenne et les autorités de 26 États membres, de l’Islande et de la Norvège ont contrôlé <b>223 grands sites</b> qui publient des avis de consommateurs :</p>\n<ul>\n<li><b>55 %</b> enfreignaient probablement la directive sur les pratiques commerciales déloyales, avec des doutes pour <b>18 %</b> de plus ;</li>\n<li><b>144 sites (65 %)</b> ne prenaient pas assez de mesures pour s’assurer que les avis venaient de vrais utilisateurs ;</li>\n<li><b>104 sites (47 %)</b> n’expliquaient pas comment les avis étaient collectés et traités ;</li>\n<li><b>176 sites (79 %)</b> n’indiquaient pas comment les avis avec contrepartie étaient interdits ou signalés.</li>\n</ul>\n<p>D’où les obligations d’information qui s’imposent aujourd’hui aux boutiques : voir <a href="/guides/faux-avis-loi.html">Faux avis en ligne : ce que dit la loi</a>.</p>\n\n<h2 id="sanctions">6. Les sanctions en France</h2>\n<ul>\n<li>Pratique commerciale trompeuse (dont les faux avis) : <b>2 ans d’emprisonnement et 300 000 € d’amende</b>, montant pouvant être porté à <b>10 % du chiffre d’affaires annuel moyen</b> ou à 50 % des dépenses engagées pour la pratique.</li>\n<li>Depuis la loi n° 2024-420 du 10 mai 2024, quand la pratique est commise en ligne : jusqu’à <b>5 ans d’emprisonnement et 750 000 € d’amende</b> pour une personne physique, et <b>3,75 millions d’euros</b> pour une société.</li>\n</ul>\n\n<h2 id="citer">7. Citer ces chiffres</h2>\n<p>Journaliste, blogueur, enseignant ou étudiant : vous pouvez reprendre librement ces chiffres. Merci de citer la <b>source originale</b> indiquée pour chacun, et cette page comme point d’entrée : <b>« Statistiques avis clients 2026, Avitime »</b>, avec un lien vers https://avitime.fr/guides/statistiques-avis-clients.html. Une erreur ou une étude récente à ajouter ? <a href="/contact">Écrivez-nous</a>.</p>\n<p>Ces chiffres ont guidé la conception d’Avitime : de vrais testeurs, sélectionnés par Avitime, une vraie commande à 0 € et un avis publié avec la mention « Produit offert pour test ». <a href="/#concept">Voir le concept</a>.</p>\n\n<h2 id="sources">Sources</h2>\n<ul class="gd-src">\n<li>Avis Vérifiés by Skeepers, baromètre 2024, présenté par CB News : <a href="https://www.cbnews.fr/etudes/75-consommateurs-consultent-les-avis-ligne-avant-achat" rel="noopener" target="_blank">« 75 % des consommateurs consultent les avis en ligne avant l’achat »</a> (juillet 2024)</li>\n<li>Spiegel Research Center, Northwestern University, <a href="https://spiegel.medill.northwestern.edu/How-Online-Reviews-Influence-Sales" rel="noopener" target="_blank">« How Online Reviews Influence Sales »</a> (2017)</li>\n<li>E-Commerce Nation, <a href="https://www.ecommerce-nation.fr/?p=125702" rel="noopener" target="_blank">« Baromètre GEO : le trafic e-commerce issu des IA génératives multiplié par 18 en un an »</a> (baromètre Valiuz, février 2026)</li>\n<li>Commission européenne, <a href="https://france.representation.ec.europa.eu/informations/protection-des-consommateurs-contre-les-avis-trompeurs-55-des-sites-web-controles-enfreignent-les-2022-01-20_fr" rel="noopener" target="_blank">« Protection des consommateurs contre les avis trompeurs : 55 % des sites web contrôlés enfreignent les règles de l’UE »</a> (20 janvier 2022)</li>\n<li>DGCCRF, <a href="https://www.economie.gouv.fr/dgccrf/Publications/Vie-pratique/Fiches-pratiques/Faux-avis-consommateurs-sur-internet" rel="noopener" target="_blank">« Avis en ligne : attention aux faux commentaires ! »</a></li>\n<li>CMS Francis Lefebvre, <a href="https://cms.law/fr/fra/news-information/les-nouvelles-sanctions-pour-les-pratiques-commerciales-trompeuses-commises-en-ligne" rel="noopener" target="_blank">« Les nouvelles sanctions pour les pratiques commerciales trompeuses commises en ligne »</a> (loi n° 2024-420 du 10 mai 2024)</li>\n<li>Google, <a href="https://support.google.com/merchants/answer/190657?hl=fr" rel="noopener" target="_blank">« Présentation des notes de magasin »</a> (Merchant Center)</li>\n</ul>\n<p class="gd-note">Page de synthèse, à jour au 16 octobre 2026. Les chiffres proviennent des études citées : leur méthodologie complète est disponible auprès de chaque source. Avitime est l’éditeur de cette page.</p>\n'}
]

from guide_referencement import GUIDE as _G_REF
GUIDES.append(_G_REF)

# --- 21/10/2026 : 5 guides pour les testeurs (mots-clés Haloscan), cluster autour de /devenir-testeur
from guides_testeurs import GUIDES_TESTEURS, TESTEUR_SLUGS
GUIDES.extend(GUIDES_TESTEURS)
# --- 21/10/2026 : 5 guides boutiques (mots-clés Haloscan)
from guides_boutiques import GUIDES_BOUTIQUES, BOUTIQUE_SLUGS
GUIDES.extend(GUIDES_BOUTIQUES)

# --- 20/10/2026, audit SEO : maillage interne (guides plateformes, référencement et statistiques peu liés)
RELATED_20_10 = {
    "avis-clients-ia": ["combien-avis-clients", "statistiques-avis-clients", "referencement-boutique-en-ligne"],
    "faux-avis-loi": ["premiers-avis-clients", "statistiques-avis-clients", "arnaques-testeur-produits"],
    "premiers-avis-clients": ["combien-avis-clients", "avis-clients-prestashop", "avis-clients-woocommerce"],
    "avis-clients-prestashop": ["avis-clients-woocommerce", "avis-clients-shopify", "referencement-boutique-en-ligne"],
    "avis-clients-woocommerce": ["avis-clients-prestashop", "avis-clients-shopify", "referencement-boutique-en-ligne"],
    "avis-clients-shopify": ["avis-clients-prestashop", "comparatif-solutions-avis-clients", "referencement-boutique-en-ligne"],
    "repondre-avis-negatifs": ["combien-avis-clients", "statistiques-avis-clients", "referencement-boutique-en-ligne"],
    "combien-avis-clients": ["statistiques-avis-clients", "premiers-avis-clients", "comparatif-solutions-avis-clients"],
    "comparatif-solutions-avis-clients": ["combien-avis-clients", "avis-clients-prestashop", "statistiques-avis-clients"],
    "referencement-boutique-en-ligne": ["combien-avis-clients", "avis-clients-prestashop", "avis-clients-ia"],
    # 21/10 : guides boutiques reliés aux nouveaux guides (demande d'avis, fiche produit, conversion, échantillonnage)
    "premiers-avis-clients": ["demander-avis-client", "echantillonnage-produit", "combien-avis-clients"],
    "referencement-boutique-en-ligne": ["fiche-produit-e-commerce", "combien-avis-clients", "avis-clients-ia"],
    "combien-avis-clients": ["taux-conversion-e-commerce", "statistiques-avis-clients", "premiers-avis-clients"],
    "comparatif-solutions-avis-clients": ["echantillonnage-produit", "combien-avis-clients", "statistiques-avis-clients"],
    "repondre-avis-negatifs": ["demander-avis-client", "combien-avis-clients", "statistiques-avis-clients"],
    # 21/10 : le guide arnaques rejoint le cluster testeurs
    "arnaques-testeur-produits": ["sites-tester-produits-gratuitement", "testeur-de-produit", "tester-produits-a-domicile"],
}
for _g in GUIDES:
    if _g["slug"] in RELATED_20_10:
        _g["related"] = RELATED_20_10[_g["slug"]]

# --- 20/10/2026 : « Combien d'avis » devient le guide pilier du thème avis clients (chiffres sourcés + liens vers tous les guides)
_COMBIEN_LECTURE = '''<h2 id="lecture">4. Combien d’avis vos clients lisent-ils ?</h2>
<p>Le baromètre 2024 d’Avis Vérifiés by Skeepers, mené auprès de <b>72 000 consommateurs</b> en France, en Espagne et en Italie, montre que les avis comptent avant chaque achat :</p>
<ul>
<li><b>75 %</b> des consommateurs lisent les avis avant d’acheter ;</li>
<li><b>40 %</b> en lisent entre 1 et 5, <b>34 %</b> entre 6 et 10, et <b>26 %</b> plus de 10 ;</li>
<li><b>65 %</b> font confiance au <b>nombre d’avis</b>, et plus de <b>72 %</b> à la note moyenne ;</li>
<li><b>63 %</b> regardent comment la marque répond aux avis négatifs.</li>
</ul>
<p>Autrement dit, la plupart de vos clients liront au moins quelques avis : avec zéro avis, il n’y a rien à lire, et la fiche ne rassure pas.</p>

<h2 id="google">5. Et pour les étoiles dans Google ?</h2>
<p>Deux cas différents. La <b>note de votre boutique</b> (les étoiles du marchand dans Google Shopping) demande en général <b>au moins 100 avis</b>, selon Google Merchant Center. Les <b>étoiles d’une fiche produit</b> dans les résultats de recherche dépendent, elles, des avis affichés en texte sur la page et de leurs données structurées : Google n’impose pas de nombre minimum, mais ne garantit jamais leur affichage. Détails dans notre <a href="/guides/referencement-boutique-en-ligne.html#etoiles">guide du référencement</a>.</p>

'''
_COMBIEN_HUB = '''<h2 id="guides">7. Tous nos guides sur les avis clients</h2>
<ul>
<li><a href="/guides/premiers-avis-clients.html">Obtenir ses premiers avis clients sans tricher</a> : les méthodes honnêtes, étape par étape.</li>
<li><a href="/guides/statistiques-avis-clients.html">Statistiques avis clients 2026</a> : tous les chiffres clés, avec leurs sources.</li>
<li><a href="/guides/demander-avis-client.html">Demander un avis client</a> : le bon moment et des modèles d’e-mail.</li>
<li><a href="/guides/echantillonnage-produit.html">Échantillonnage produit</a> : faire tester ses produits, dans les règles.</li>
<li><a href="/guides/taux-conversion-e-commerce.html">Taux de conversion e-commerce</a> : le calcul et le rôle des avis.</li>
<li><a href="/guides/repondre-avis-negatifs.html">Répondre à un avis négatif</a> : la méthode en 4 étapes et des exemples.</li>
<li><a href="/guides/faux-avis-loi.html">Faux avis : ce que dit la loi</a> : les mentions obligatoires et les sanctions.</li>
<li><a href="/guides/avis-clients-ia.html">Avis clients et IA</a> : pourquoi ChatGPT et Gemini lisent vos avis.</li>
<li><a href="/guides/comparatif-solutions-avis-clients.html">Comparatif des solutions d’avis clients</a> : collecte, clubs de testeurs, échantillonnage.</li>
<li>Par plateforme : <a href="/guides/avis-clients-prestashop.html">PrestaShop</a>, <a href="/guides/avis-clients-woocommerce.html">WooCommerce</a> et <a href="/guides/avis-clients-shopify.html">Shopify</a>.</li>
</ul>

'''
for _g in GUIDES:
    if _g["slug"] == "combien-avis-clients":
        _b = _g["body"]
        _b = _b.replace('<li><a href="#viser">Ce qu’il faut viser</a></li>',
                        '<li><a href="#lecture">Combien d’avis vos clients lisent</a></li>\n<li><a href="#google">Les étoiles dans Google</a></li>\n'
                        '<li><a href="#viser">Ce qu’il faut viser</a></li>\n<li><a href="#guides">Tous nos guides sur les avis clients</a></li>', 1)
        _b = _b.replace('<h2 id="viser">4. Ce qu’il faut viser</h2>', _COMBIEN_LECTURE + '<h2 id="viser">6. Ce qu’il faut viser</h2>', 1)
        _b = _b.replace('<h2 id="sources">Sources</h2>', _COMBIEN_HUB + '<h2 id="sources">Sources</h2>', 1)
        _b = _b.replace('<ul class="gd-src">\n',
                        '<ul class="gd-src">\n<li>Avis Vérifiés by Skeepers, baromètre 2024, présenté par CB News : <a href="https://www.cbnews.fr/etudes/75-consommateurs-consultent-les-avis-ligne-avant-achat" rel="noopener" target="_blank">« 75 % des consommateurs consultent les avis en ligne avant l’achat »</a> (juillet 2024)</li>\n', 1)
        _b = _b.replace('(2017)</li>\n</ul>',
                        '(2017)</li>\n<li>Google, <a href="https://support.google.com/merchants/answer/190657?hl=fr" rel="noopener" target="_blank">« Présentation des notes de magasin »</a> (Merchant Center)</li>\n</ul>', 1)
        _b = _b.replace('Article d’information générale, à jour au 15 octobre 2026.', 'Article d’information générale, mis à jour le 20 octobre 2026. Avitime est l’éditeur de ce guide.', 1)
        assert _b.count('id="lecture"') == 1 and _b.count('id="guides"') == 1 and 'cbnews' in _b and 'merchants/answer' in _b and '20 octobre 2026' in _b
        _g["body"] = _b
        _g["read"] = 6
        _g["mod_iso"] = "2026-10-20"

# --- 20/10/2026, audit Search Console : le comparatif sort sur « plateforme d'avis clients », « solution avis client »,
# « alternative avis vérifiés » (positions 60 à 95) → titre aligné sur ces recherches + 2 sections + questions fréquentes
_COMP_ALT = '''<h2 id="alternative">7. Quelle alternative à Avis Vérifiés ou Trustpilot pour une petite boutique ?</h2>
<p>Les grandes plateformes de collecte sont pensées pour des boutiques qui ont déjà des commandes régulières. Quand vous démarrez, d’autres options, souvent gratuites, font très bien le travail :</p>
<ul>
<li><b>Les avis intégrés à votre boutique.</b> PrestaShop propose un module natif « Commentaires produits », WooCommerce gère les avis et le libellé « propriétaire vérifié » dans ses réglages. Voir nos guides <a href="/guides/avis-clients-prestashop.html">PrestaShop</a> et <a href="/guides/avis-clients-woocommerce.html">WooCommerce</a>. Sur Shopify, l’application d’avis officielle a été retirée en 2024 : il faut passer par une application tierce (voir <a href="/guides/avis-clients-shopify.html">notre guide Shopify</a>).</li>
<li><b>Google Avis clients</b>, le programme gratuit de Google Merchant Center, pour collecter des avis après achat.</li>
<li><b>Une simple demande par e-mail</b> quelques jours après la livraison, avec un lien direct vers la fiche produit (voir <a href="/guides/premiers-avis-clients.html">obtenir ses premiers avis</a>).</li>
<li><b>Des tests produits transparents</b> pour les tout premiers avis, quand les ventes sont encore rares : c’est ce que fait Avitime.</li>
</ul>
<p>La bonne alternative n’est donc pas forcément une plateforme de plus, mais la bonne combinaison : un affichage des avis intégré à votre boutique, une demande systématique après achat, et des testeurs pour amorcer.</p>

<h2 id="faq">8. Questions fréquentes</h2>
<h3>Qu’est-ce qu’une plateforme d’avis clients ?</h3>
<p>C’est un service qui recueille les avis de vos clients, les modère selon des règles publiées, puis les affiche sur votre site, sur sa propre page et parfois dans Google. Certaines collectent après chaque commande, d’autres sont ouvertes à tous les consommateurs.</p>
<h3>Une plateforme d’avis est-elle obligatoire ?</h3>
<p>Non. En revanche, dès que vous affichez des avis, la loi vous impose d’indiquer s’ils sont contrôlés et comment, de les dater, et de signaler ceux qui ont été obtenus avec une contrepartie. Voir <a href="/guides/faux-avis-loi.html">ce que dit la loi</a>.</p>
<h3>Peut-on offrir un produit en échange d’un avis ?</h3>
<p>Oui, à condition que l’avis reste libre, quelle que soit la note, et que la contrepartie soit clairement indiquée à côté de l’avis. Payer pour obtenir une bonne note, en revanche, revient à fabriquer de faux avis.</p>
<h3>Combien coûte une solution d’avis clients ?</h3>
<p>Cela va de gratuit (avis intégrés à la boutique, Google Avis clients) à plusieurs dizaines ou centaines d’euros par mois pour les plateformes complètes. Les tarifs évoluent souvent : comparez sur le site de chaque service.</p>

'''
for _g in GUIDES:
    if _g["slug"] == "comparatif-solutions-avis-clients":
        _b = _g["body"]
        _b = _b.replace('<li><a href="#choisir">Comment choisir</a></li>',
                        '<li><a href="#choisir">Comment choisir</a></li>\n<li><a href="#alternative">Quelle alternative pour une petite boutique</a></li>\n<li><a href="#faq">Questions fréquentes</a></li>', 1)
        _b = _b.replace('<h3>Sources</h3>', _COMP_ALT + '<h3>Sources</h3>', 1)
        _b = _b.replace('à jour au 16 octobre 2026.', 'mis à jour le 20 octobre 2026.', 1)
        assert _b.count('id="alternative"') == 1 and _b.count('id="faq"') == 1 and '20 octobre 2026' in _b
        _g["body"] = _b
        _g["seo_title"] = "Plateformes d’avis clients : le comparatif honnête (2026)"
        _g["seo_desc"] = ("Avis Vérifiés, Trustpilot, Google, clubs de testeurs, Avitime : quelle plateforme d’avis clients choisir, "
                          "et quelles alternatives pour une petite boutique ?")
        _g["read"] = 10
        _g["mod_iso"] = "2026-10-20"

BY_SLUG = {}

def cta_block(g):
    if g["slug"] == "arnaques-testeur-produits" or g["slug"] in TESTEUR_SLUGS:
        return ('<div class="gd-cta"><p><b>Testeur Avitime :</b> gratuit, produit et livraison offerts, jamais rien à payer.</p>'
                '<a class="btn" href="/devenir-testeur">Devenir testeur</a></div>')
    return ('<div class="gd-cta"><p><b>Vos produits méritent de vrais avis.</b> Avitime les fait tester par de vrais consommateurs, '
            'sur PrestaShop, WooCommerce et Shopify.</p><a class="btn" href="/#commercants">Découvrir l’offre commerçants</a></div>')

def related_block(g):
    rel = [BY_SLUG[x] for x in g.get("related", []) if x in BY_SLUG][:3]
    if not rel:
        return ""
    cards = "".join(f'<a class="gd-card" href="/guides/{r["slug"]}.html"><p class="eyebrow">{r["kicker"]}</p><h2>{r["title"]}</h2></a>' for r in rel)
    return f'<aside class="gd-related" aria-label="À lire aussi"><h2>À lire aussi</h2><div class="gd-cards">{cards}</div><p style="margin-top:18px"><a href="/guides/">Tous les guides</a></p></aside>'

def page_guide(g):
    path = f"/guides/{g['slug']}.html"
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "headline": g["title"], "description": g["desc"], "inLanguage": "fr-FR",
         "datePublished": g.get("pub_iso", "2026-10-15"), "dateModified": g.get("mod_iso", g.get("pub_iso", "2026-10-15")), "author": AUTHOR, "publisher": PUBLISHER,
         "mainEntityOfPage": f"https://avitime.fr{path}", "image": "https://avitime.fr/assets/img/og-image.jpg"},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Accueil", "item": "https://avitime.fr/"},
            {"@type": "ListItem", "position": 2, "name": "Guides", "item": "https://avitime.fr/guides/"},
            {"@type": "ListItem", "position": 3, "name": g["title"], "item": f"https://avitime.fr{path}"}]}]}
    out = HEAD.format(title=html.escape(g["seo_title"]), desc=html.escape(g["seo_desc"]), path=path, ogtype="article", guides_current=' aria-current="page"')
    out += (f'<article>\n<section class="gd-hero"><div class="gd-wrap">\n<p class="eyebrow"><a href="/guides/" style="color:inherit;text-decoration:none">Guides</a> · {g["kicker"].split("· ")[1]}</p>\n'
            f'<h1>{g["title"]}</h1>\n<p class="gd-lede">{g["lede"]}</p>\n'
            + BYLINE.format(pub=g.get("pub_fr", "15 octobre 2026"), read=g["read"]) + '\n</div></section>\n'
            f'<section class="gd-body"><div class="gd-wrap">{g["body"]}{cta_block(g)}{related_block(g)}</div></section>\n</article>\n')
    out += FOOT.replace("{ld}", json.dumps(ld, ensure_ascii=False))
    open(os.path.join(OUT, f"{g['slug']}.html"), "w", encoding="utf-8").write(out)

def page_index():
    path = "/guides/"
    ld = {"@context": "https://schema.org", "@type": "CollectionPage", "name": "Guides Avitime", "inLanguage": "fr-FR",
          "url": "https://avitime.fr/guides/", "hasPart": [{"@type": "Article", "headline": g["title"], "url": f"https://avitime.fr/guides/{g['slug']}.html", "author": AUTHOR} for g in GUIDES]}
    out = HEAD.format(title="Guides Avitime : avis clients et tests de produits", desc="Guides pour les boutiques en ligne (premiers avis clients, loi sur les faux avis) et pour les testeurs de produits : sites fiables, Amazon Vine, arnaques.", path=path, ogtype="website", guides_current=' aria-current="page"')
    card = lambda g: f'<a class="gd-card" href="/guides/{g["slug"]}.html"><p class="eyebrow">{g["kicker"]}</p><h2>{g["title"]}</h2><p>{g["desc"]}</p></a>'
    pour_testeurs = [g for g in GUIDES if g["slug"] in TESTEUR_SLUGS] + [g for g in GUIDES if g["slug"] == "arnaques-testeur-produits"]
    pour_boutiques = [g for g in GUIDES if g not in pour_testeurs]
    cards = ('<h2 style="font-size:24px;letter-spacing:-.03em;margin:44px 0 0">Pour les boutiques en ligne</h2>'
             f'<div class="gd-cards" style="margin-top:18px">{"".join(card(g) for g in pour_boutiques)}</div>'
             '<h2 style="font-size:24px;letter-spacing:-.03em;margin:44px 0 0">Pour les testeurs</h2>'
             f'<div class="gd-cards" style="margin-top:18px">{"".join(card(g) for g in pour_testeurs)}'
             '<a class="gd-card" href="/devenir-testeur"><p class="eyebrow">Guide · Testeurs</p><h2>Devenir testeur Avitime : le guide complet en 7 étapes</h2><p>Inscription gratuite, candidature, commande à 0 €, test et avis, avec les vraies captures de l’espace testeur.</p></a></div>')
    out += ('<section class="gd-hero"><div class="gd-wrap" style="max-width:960px">\n<p class="eyebrow">Guides</p>\n'
            '<h1>Nos guides : avis clients et tests de produits</h1>\n'
            '<p class="gd-lede">Des articles courts et sourcés : pour les boutiques, obtenir de vrais avis et rester dans les règles ; pour les testeurs, tester des produits sans se faire avoir. Écrits par Cyril Quémy, fondateur d’Avitime.</p>\n'
            f'{cards}\n</div></section>\n<div style="height:72px"></div>\n')
    out += FOOT.replace("{ld}", json.dumps(ld, ensure_ascii=False))
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(out)

if __name__ == "__main__":
    BY_SLUG.update({g['slug']: g for g in GUIDES})
    for g in GUIDES: page_guide(g)
    page_index()
    print(sorted(os.listdir(OUT)))
