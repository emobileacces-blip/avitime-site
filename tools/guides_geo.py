# Guides GEO / E-E-A-T (21/10/2026), mots-clés Haloscan :
#   geo-seo     → geo seo (2 900), seo vs geo (320), seo et geo (260), référencement chatgpt (210)
#   eeat-e-commerce → eeat (1 100), eeat seo (200), eeat google (200)
# Sources officielles relevées le 21/10/2026 (Google Search Central, OpenAI, Perplexity, Anthropic, Microsoft, arXiv).

PUB = {"pub_iso": "2026-10-21", "pub_fr": "21 octobre 2026"}

def src(label, url, title, extra=""):
    return f'<li>{label}, <a href="{url}" rel="noopener" target="_blank">{title}</a>{extra}</li>\n'

S_G_AIGUIDE = src("Google Search Central", "https://developers.google.com/search/docs/fundamentals/ai-optimization-guide", "« Google’s Guide to Optimizing for Generative AI Features on Google Search »", " (juillet 2026)")
S_G_AIFEAT = src("Google Search Central", "https://developers.google.com/search/docs/appearance/ai-features", "« AI features and your website »")
S_G_EXT = src("Google Search Central", "https://developers.google.com/crawling/docs/crawlers-fetchers/google-common-crawlers?hl=en", "robots de Google, dont Google-Extended")
S_G_HELPFUL = src("Google Search Central", "https://developers.google.com/search/docs/fundamentals/creating-helpful-content", "« Créer du contenu utile, fiable et axé sur les personnes »")
S_G_REVIEWS = src("Google Search Central", "https://developers.google.com/search/docs/specialty/ecommerce/write-high-quality-reviews", "« Rédiger des avis de produits de qualité »")
S_G_REVSYS = src("Google Search Central", "https://developers.google.com/search/docs/appearance/reviews-system", "« Le système d’avis de la recherche Google »")
S_OAI_BOTS = src("OpenAI", "https://developers.openai.com/api/docs/bots", "robots d’OpenAI (OAI-SearchBot, GPTBot, ChatGPT-User)")
S_OAI_SEARCH = src("OpenAI", "https://help.openai.com/en/articles/9237897-chatgpt-search", "« ChatGPT search »", " (centre d’aide)")
S_OAI_SHOP = src("OpenAI", "https://help.openai.com/en/articles/11128490", "« Shopping with ChatGPT Search »", " (centre d’aide)")
S_PPLX = src("Perplexity", "https://docs.perplexity.ai/docs/resources/perplexity-crawlers.md", "robots de Perplexity")
S_ANTH = src("Anthropic", "https://support.claude.com/en/articles/8896518-does-anthropic-crawl-data-from-the-web-and-how-can-site-owners-block-the-crawler", "robots d’Anthropic (ClaudeBot, Claude-SearchBot, Claude-User)")
S_MS = src("Microsoft Learn", "https://learn.microsoft.com/en-us/microsoft-365/copilot/manage-public-web-access", "Copilot et la recherche Bing")
S_BING_AI = src("Bing Webmaster Blog", "https://blogs.bing.com/webmaster/February-2026/Introducing-AI-Performance-in-Bing-Webmaster-Tools-Public-Preview", "« AI Performance in Bing Webmaster Tools »", " (février 2026)")
S_GEO = src("Aggarwal et al.", "https://arxiv.org/abs/2311.09735", "« GEO: Generative Engine Optimization »", " (KDD 2024)")
S_MUELLER = src("Search Engine Roundtable", "https://seroundtable.com/google-ai-llms-txt-39607.html", "John Mueller (Google) sur llms.txt", " (juin 2025)")

GUIDES_GEO = [
 dict(PUB, **{
  "slug": "geo-seo",
  "related": ["avis-clients-ia", "eeat-e-commerce", "referencement-boutique-en-ligne"],
  "seo_title": "GEO et SEO : la différence, et le rôle des avis clients",
  "seo_desc": "GEO ou SEO ? Ce que disent Google, OpenAI et la recherche sur l’optimisation pour ChatGPT et les IA, et pourquoi les avis clients pèsent autant.",
  "title": "GEO et SEO : la différence, et pourquoi les avis clients comptent pour ChatGPT",
  "desc": "Le GEO (Generative Engine Optimization) vise à être cité par les IA comme ChatGPT, Gemini ou Perplexity. Ce qui change vraiment par rapport au SEO, ce qui est un mythe, et le rôle des avis clients.",
  "kicker": "Guide · IA et visibilité",
  "lede": "Après le SEO, le GEO : il faudrait désormais optimiser son site pour ChatGPT, Gemini ou Perplexity. Que recouvre vraiment ce sigle ? Qu’en disent Google, OpenAI et les chercheurs qui l’ont inventé ? Et que doit faire une petite boutique en ligne, concrètement ? Voici les réponses, sources à l’appui.",
  "read": 9,
  "body": """
<nav class="gd-toc" aria-label="Sommaire"><p>Au sommaire</p><ol>
<li><a href="#definitions">SEO et GEO : les définitions</a></li>
<li><a href="#google">Ce que dit Google</a></li>
<li><a href="#robots">Laisser entrer les robots des IA</a></li>
<li><a href="#etude">Ce que montre la recherche sur le GEO</a></li>
<li><a href="#avis">Le rôle des avis clients</a></li>
<li><a href="#mythes">Les mythes du GEO</a></li>
<li><a href="#checklist">La checklist d’une boutique</a></li>
<li><a href="#faq">Questions fréquentes</a></li>
</ol></nav>

<div class="gd-key"><p><b>L’essentiel :</b> le GEO n’est pas une discipline à part. Google l’écrit noir sur blanc : optimiser pour la recherche par IA générative, « c’est toujours du SEO ». Ce qui fait la différence pour être cité par une IA : un contenu unique, des faits, des sources, et des retours d’expérience de première main. Pour une boutique, ce sont d’abord les avis clients détaillés.</p></div>

<h2 id="definitions">1. SEO et GEO : les définitions</h2>
<ul>
<li><b>SEO</b> (<i>Search Engine Optimization</i>) : tout ce qui aide une page à être trouvée et bien classée dans un moteur de recherche comme Google ou Bing.</li>
<li><b>GEO</b> (<i>Generative Engine Optimization</i>) : tout ce qui aide une page à être <b>reprise et citée</b> dans la réponse d’un moteur génératif : ChatGPT, Gemini, les aperçus IA de Google, Perplexity, Copilot ou Claude. Le terme vient d’un article de chercheurs de Princeton et de l’IIT Delhi, publié en 2023 et présenté à la conférence KDD en 2024.</li>
</ul>
<p>La différence tient en une phrase : le SEO vise une <b>place dans une liste de liens</b>, le GEO vise une <b>place dans une réponse rédigée</b>. Mais pour être cité, il faut d’abord être trouvé : les deux se recouvrent très largement.</p>

<h2 id="google">2. Ce que dit Google</h2>
<p>Google a publié en juillet 2026 un guide officiel sur l’optimisation pour ses fonctionnalités d’IA générative. Ses messages principaux :</p>
<ul>
<li>optimiser pour la recherche par IA générative, c’est optimiser pour l’expérience de recherche, « et donc toujours du SEO » ;</li>
<li><b>aucune exigence supplémentaire</b> pour apparaître dans les aperçus IA ou le mode IA : la page doit simplement être indexée et pouvoir s’afficher en extrait ;</li>
<li>pas besoin de fichiers spéciaux, de découper son contenu en petits morceaux, ni d’écrire « pour l’IA » ;</li>
<li>chercher à multiplier des mentions artificielles sur le web « n’est pas aussi utile qu’il y paraît » ;</li>
<li>ce qui aide : un contenu unique, avec un point de vue d’expert ou d’utilisateur qui va au-delà des généralités. Google cite justement l’exemple d’un <b>avis de première main</b> ;</li>
<li>pour l’e-commerce, Merchant Center et la fiche d’établissement Google peuvent aider vos produits à être visibles dans les réponses IA comme dans les résultats classiques.</li>
</ul>
<p>Google précise aussi qu’aucun outil tiers n’a accès à ses systèmes internes de classement ou d’IA : méfiez-vous des promesses de « positionnement garanti dans ChatGPT ».</p>

<h2 id="robots">3. Laisser entrer les robots des IA</h2>
<p>Un assistant ne peut citer que ce qu’il peut lire. Chaque éditeur a ses robots, avec des rôles différents :</p>
<div class="tbl-wrap gd-tbl"><table>
<thead><tr><th>Robot</th><th>Éditeur</th><th>À quoi il sert</th></tr></thead>
<tbody>
<tr><td>OAI-SearchBot</td><td>OpenAI</td><td>Recherche de ChatGPT. Un site qui le bloque n’apparaît pas dans les réponses de ChatGPT search.</td></tr>
<tr><td>GPTBot</td><td>OpenAI</td><td>Entraînement des modèles. Le bloquer n’empêche pas d’apparaître dans la recherche.</td></tr>
<tr><td>PerplexityBot</td><td>Perplexity</td><td>Faire apparaître et lier des sites dans les résultats de Perplexity.</td></tr>
<tr><td>Claude-SearchBot</td><td>Anthropic</td><td>Améliorer les résultats de recherche de Claude. Le bloquer peut réduire la visibilité.</td></tr>
<tr><td>Google-Extended</td><td>Google</td><td>Usage par Gemini (entraînement, ancrage). Sans effet sur l’inclusion ni le classement dans Google Search.</td></tr>
<tr><td>Bingbot</td><td>Microsoft</td><td>Index de Bing, que Copilot interroge pour répondre.</td></tr>
</tbody></table></div>
<p>Vérifiez que votre fichier <code>robots.txt</code> ne bloque pas les robots de recherche, et inscrivez votre site sur <b>Bing Webmaster Tools</b> en plus de la Google Search Console : Bing propose même un rapport « AI Performance » qui compte les citations de vos pages dans Copilot.</p>

<h2 id="etude">4. Ce que montre la recherche sur le GEO</h2>
<p>Les chercheurs à l’origine du terme ont testé plusieurs façons de réécrire un contenu, sur un large banc d’essai de questions (GEO-bench). Résultat : le GEO peut améliorer la visibilité d’une source dans les réponses générées <b>jusqu’à 40 %</b>, mais les meilleures méthodes varient selon le sujet. Dans leurs tests :</p>
<ul>
<li><b>ajouter des citations</b> de sources reconnues, <b>ajouter des statistiques</b> et <b>citer ses sources</b> faisaient partie des méthodes les plus efficaces ;</li>
<li>améliorer la fluidité du texte aidait aussi ;</li>
<li>le <b>bourrage de mots-clés</b>, vieille recette du SEO, faisait <b>baisser</b> la visibilité.</li>
</ul>
<p>Autrement dit : des faits vérifiables, des chiffres sourcés, des citations d’experts ou d’utilisateurs. Exactement ce qui rend un contenu utile pour un humain.</p>

<h2 id="avis">5. Le rôle des avis clients</h2>
<p>Pour recommander un produit, une IA a besoin de savoir ce qu’il vaut à l’usage, et pour qui. C’est précisément ce que contiennent les avis clients :</p>
<ul>
<li>OpenAI indique que, dans les résultats shopping de ChatGPT, les <b>résumés d’avis sont générés à partir d’avis publiés sur des sites publics</b> ;</li>
<li>Google recommande les contenus qui apportent une expérience <b>de première main</b> ; un avis détaillé de client ou de testeur en est la forme la plus directe ;</li>
<li>un avis apporte des faits que la description ne donne pas : « taille petit », « tient au lavage », « idéal pour un petit balcon ».</li>
</ul>
<p>Encore faut-il que ces avis soient <b>sur votre fiche produit, en texte lisible</b>, nombreux, détaillés et authentiques. Le détail est dans notre guide <a href="/guides/avis-clients-ia.html">Avis clients et IA : être recommandé par ChatGPT et Gemini</a>, et la notion de confiance dans <a href="/guides/eeat-e-commerce.html">E-E-A-T : ce que Google attend d’une boutique en ligne</a>.</p>

<h2 id="mythes">6. Les mythes du GEO</h2>
<ul>
<li><b>« Il faut un fichier llms.txt. »</b> Google indique ne pas utiliser ce type de fichier, et John Mueller, de Google, a déclaré en 2025 qu’aucun système d’IA ne l’utilise actuellement. Il ne fait pas de mal, mais ce n’est pas un levier.</li>
<li><b>« Il faut un balisage spécial pour l’IA. »</b> Google : aucune donnée structurée particulière n’est requise pour ses fonctionnalités d’IA. Les données structurées restent utiles pour les résultats enrichis, comme les étoiles.</li>
<li><b>« On peut acheter sa place dans ChatGPT. »</b> Les résultats produits de ChatGPT ne sont pas des publicités, selon OpenAI, et aucun outil tiers n’a accès aux systèmes de Google.</li>
<li><b>« Le SEO est mort. »</b> Pour être cité, il faut être trouvé : l’indexation, la qualité et la popularité d’une page restent la base.</li>
</ul>

<h2 id="checklist">7. La checklist d’une boutique</h2>
<ol>
<li>Votre site est indexé dans <b>Google</b> (Search Console) et dans <b>Bing</b> (Bing Webmaster Tools).</li>
<li>Votre <code>robots.txt</code> laisse passer les robots de recherche (OAI-SearchBot, PerplexityBot, Claude-SearchBot, Bingbot, Googlebot).</li>
<li>Vos produits sont dans <b>Google Merchant Center</b>.</li>
<li>Chaque fiche produit a une description unique et précise (voir <a href="/guides/fiche-produit-e-commerce.html">la méthode</a>).</li>
<li>Vos produits phares ont <b>au moins cinq avis détaillés</b>, affichés en texte, avec leur balisage (voir <a href="/guides/combien-avis-clients.html">combien d’avis</a>).</li>
<li>Vos pages de conseils citent leurs <b>sources</b> et donnent des <b>chiffres vérifiables</b>.</li>
<li>Votre identité est claire et cohérente : mentions légales, page « À propos », auteur des contenus, réseaux sociaux.</li>
<li>Vous testez régulièrement : posez à ChatGPT ou Perplexity les questions de vos clients, et regardez qui est cité.</li>
</ol>
<p>Avitime s’occupe du point 5 : des testeurs sélectionnés par Avitime publient des avis argumentés sur vos fiches produits, avec la mention « Produit offert pour test », et le module ajoute automatiquement le balisage des avis. Aucun classement n’est garanti, ni dans Google ni dans les IA : personne ne peut le promettre.</p>

<h2 id="faq">8. Questions fréquentes</h2>
<h3>Quelle est la différence entre SEO et GEO ?</h3>
<p>Le SEO vise à être bien classé dans les résultats d’un moteur de recherche ; le GEO vise à être cité dans la réponse rédigée par une IA. En pratique, Google considère que l’optimisation pour l’IA générative reste du SEO.</p>
<h3>Comment être cité par ChatGPT ?</h3>
<p>Laisser passer le robot OAI-SearchBot, être bien indexé, publier un contenu unique et sourcé, et, pour un produit, avoir des avis publics détaillés. OpenAI ne vend pas de place dans ses résultats.</p>
<h3>Le GEO remplace-t-il le SEO ?</h3>
<p>Non. Les réponses des IA s’appuient sur des pages qu’elles trouvent et jugent fiables : les bases du SEO restent indispensables.</p>
<h3>Combien de temps pour voir un effet ?</h3>
<p>Comme en SEO : plusieurs semaines à plusieurs mois. Google indique qu’un nouveau passage de ses robots peut prendre de plusieurs jours à plusieurs mois.</p>

<h2 id="sources">Sources</h2>
<ul class="gd-src">
""" + S_G_AIGUIDE + S_G_AIFEAT + S_G_EXT + S_OAI_BOTS + S_OAI_SEARCH + S_OAI_SHOP + S_PPLX + S_ANTH + S_MS + S_BING_AI + S_GEO + S_MUELLER + "</ul>\n" +
  '<p class="gd-note">Article d’information générale, à jour au 21 octobre 2026. Le fonctionnement des assistants IA évolue vite : les principes restent, les détails changent. Avitime est l’éditeur de ce guide et ne garantit aucun classement.</p>\n',
 }),

 dict(PUB, **{
  "slug": "eeat-e-commerce",
  "related": ["geo-seo", "avis-clients-ia", "faux-avis-loi"],
  "seo_title": "E-E-A-T : ce que Google attend d’une boutique en ligne",
  "seo_desc": "E-E-A-T (Expérience, Expertise, Autorité, Fiabilité) : ce que dit vraiment Google, pourquoi la confiance prime, et le rôle des avis clients.",
  "title": "E-E-A-T : ce que Google attend vraiment d’une boutique en ligne",
  "desc": "Expérience, Expertise, Autorité, Fiabilité : ce que recouvre l’E-E-A-T, ce que Google en dit officiellement, et comment une petite boutique peut le démontrer, avis clients en tête.",
  "kicker": "Guide · Référencement",
  "lede": "E-E-A-T : quatre lettres que l’on croise partout dès qu’on parle de référencement. Beaucoup en parlent comme d’un score secret de Google. La réalité est plus simple, et plus utile pour une petite boutique : c’est une façon de juger si un site mérite la confiance. Voici ce que dit Google, et comment le démontrer.",
  "read": 8,
  "body": """
<nav class="gd-toc" aria-label="Sommaire"><p>Au sommaire</p><ol>
<li><a href="#definition">E-E-A-T : la définition</a></li>
<li><a href="#google">Ce que dit officiellement Google</a></li>
<li><a href="#qui-comment-pourquoi">Qui, comment, pourquoi</a></li>
<li><a href="#boutique">L’E-E-A-T d’une boutique, lettre par lettre</a></li>
<li><a href="#avis">Les avis clients, preuve d’expérience</a></li>
<li><a href="#checklist">La checklist</a></li>
<li><a href="#faq">Questions fréquentes</a></li>
</ol></nav>

<div class="gd-key"><p><b>L’essentiel :</b> l’E-E-A-T n’est pas un facteur de classement en soi, mais il résume ce que les systèmes de Google cherchent à récompenser. Et de ses quatre piliers, Google le dit lui-même : <b>la confiance est le plus important</b>. Pour une boutique, la confiance se démontre par une identité claire, des informations exactes et des avis authentiques.</p></div>

<h2 id="definition">1. E-E-A-T : la définition</h2>
<ul>
<li><b>Experience (Expérience)</b> : l’auteur a-t-il vraiment utilisé le produit, vécu la situation ?</li>
<li><b>Expertise</b> : maîtrise-t-il son sujet ?</li>
<li><b>Authoritativeness (Autorité)</b> : le site ou l’auteur est-il reconnu comme une référence ?</li>
<li><b>Trustworthiness (Fiabilité)</b> : peut-on lui faire confiance ? Le contenu est-il exact, honnête, sûr ?</li>
</ul>
<p>Le premier « E », pour Expérience, a été ajouté par Google en décembre 2022. C’est le plus intéressant pour une boutique : il valorise le vécu, c’est-à-dire ce que racontent vos clients.</p>

<h2 id="google">2. Ce que dit officiellement Google</h2>
<p>Dans sa page « Créer du contenu utile, fiable et axé sur les personnes », Google précise :</p>
<ul>
<li>l’E-E-A-T <b>n’est pas en soi un facteur de classement</b> ; c’est un concept utilisé par des évaluateurs humains, dont les notes ne sont pas utilisées directement dans les algorithmes ;</li>
<li>parmi les quatre aspects, <b>la confiance est le plus important</b> ;</li>
<li>pour les sujets qui touchent à la santé, à l’argent ou à la sécurité, Google accorde encore plus de poids à un E-E-A-T solide.</li>
</ul>
<p>En clair : on ne « coche » pas l’E-E-A-T. On construit un site qui mérite la confiance, et les systèmes de Google, comme les assistants IA, finissent par le refléter (voir <a href="/guides/geo-seo.html">GEO et SEO</a>).</p>

<h2 id="qui-comment-pourquoi">3. Qui, comment, pourquoi</h2>
<p>Google propose trois questions pour évaluer son propre contenu :</p>
<ul>
<li><b>Qui</b> l’a créé ? Rendez l’auteur visible, avec une signature et une page de présentation. Les fausses informations sur l’auteur sont à proscrire.</li>
<li><b>Comment</b> a-t-il été créé ? Expliquez votre méthode, par exemple comment vous testez vos produits ou comment vous vérifiez vos avis.</li>
<li><b>Pourquoi</b> a-t-il été créé ? Selon Google, c’est peut-être la question la plus importante : pour aider des gens, et non pour attirer du trafic à tout prix.</li>
</ul>

<h2 id="boutique">4. L’E-E-A-T d’une boutique, lettre par lettre</h2>
<div class="tbl-wrap gd-tbl"><table>
<thead><tr><th>Pilier</th><th>Ce qui le démontre sur une boutique</th></tr></thead>
<tbody>
<tr><td>Expérience</td><td>Avis clients détaillés avec photos, tests de vos produits, photos réelles en situation, conseils d’usage tirés de votre pratique</td></tr>
<tr><td>Expertise</td><td>Descriptions précises (matières, dimensions, entretien), guides et comparatifs sourcés, réponses argumentées aux questions</td></tr>
<tr><td>Autorité</td><td>Mentions dans la presse, liens d’autres sites sérieux de votre secteur, présence dans des annuaires reconnus, réseaux sociaux actifs</td></tr>
<tr><td>Fiabilité</td><td>Mentions légales complètes, contact joignable, prix et frais clairs, politique de retour, paiement sécurisé, avis authentiques et transparents</td></tr>
</tbody></table></div>
<p>Pour la fiabilité, les obligations légales comptent aussi : informations avant la commande (voir <a href="/guides/fiche-produit-e-commerce.html#obligatoire">les mentions obligatoires</a>) et règles sur les avis (voir <a href="/guides/faux-avis-loi.html">Faux avis : ce que dit la loi</a>). Un site qui publie de faux avis perd exactement ce que l’E-E-A-T mesure : la confiance.</p>

<h2 id="avis">5. Les avis clients, preuve d’expérience</h2>
<p>Les avis clients sont la forme la plus directe d’« expérience » sur une boutique. Google donne d’ailleurs, pour les contenus d’avis, des conseils qui s’appliquent aussi aux avis de vos clients et testeurs : montrer l’usage réel avec des <b>photos ou des vidéos</b>, donner des <b>mesures concrètes</b>, citer les <b>avantages et les inconvénients</b> tirés de l’expérience, préciser <b>pour qui</b> le produit est fait.</p>
<p>Une nuance importante : le « système d’avis » de Google évalue les <b>articles et pages d’avis éditoriaux</b> (tests, comparatifs), pas les avis clients laissés sur les fiches produits. Les avis clients agissent autrement : ils enrichissent la fiche de faits d’usage, rassurent l’acheteur, et nourrissent les résumés que font les assistants IA à partir des avis publics (voir <a href="/guides/avis-clients-ia.html">Avis clients et IA</a>).</p>
<p>C’est pourquoi un avis Avitime suit une structure précise : contexte et durée d’utilisation, points forts, points faibles, « pour qui ? », et photos. Il est publié sur votre fiche avec la mention « Produit offert pour test — Testeur Avitime vérifié », quelle que soit la note.</p>

<h2 id="checklist">6. La checklist</h2>
<ol>
<li>Une page « À propos » qui dit qui est derrière la boutique, avec un vrai nom et un visage si possible.</li>
<li>Des mentions légales complètes et un contact joignable.</li>
<li>Des contenus signés, avec une méthode expliquée et des sources citées.</li>
<li>Des fiches produits exactes et complètes.</li>
<li>Des avis authentiques sur vos produits phares, critiques comprises, avec la contrepartie signalée quand il y en a une.</li>
<li>Des réponses aux avis, surtout négatifs (voir <a href="/guides/repondre-avis-negatifs.html">la méthode</a>).</li>
<li>Une présence cohérente ailleurs : réseaux sociaux, annuaires sérieux, partenaires.</li>
</ol>

<h2 id="faq">7. Questions fréquentes</h2>
<h3>L’E-E-A-T est-il un facteur de classement Google ?</h3>
<p>Pas directement. Google indique que l’E-E-A-T n’est pas en soi un facteur de classement, mais un ensemble de qualités que ses systèmes cherchent à récompenser à travers de nombreux signaux.</p>
<h3>Que veut dire E-E-A-T ?</h3>
<p>Experience, Expertise, Authoritativeness, Trustworthiness : expérience, expertise, autorité et fiabilité.</p>
<h3>Quel est le pilier le plus important ?</h3>
<p>La confiance (Trust). Google l’écrit : c’est le plus important des quatre.</p>
<h3>Les avis clients améliorent-ils l’E-E-A-T ?</h3>
<p>Ils en sont une preuve concrète, surtout pour l’expérience et la confiance, à condition d’être authentiques, détaillés et transparents. Des avis faux ou triés produisent l’effet inverse.</p>

<h2 id="sources">Sources</h2>
<ul class="gd-src">
""" + S_G_HELPFUL + S_G_REVIEWS + S_G_REVSYS + S_G_AIGUIDE + S_OAI_SHOP + "</ul>\n" +
  '<p class="gd-note">Article d’information générale, à jour au 21 octobre 2026. Avitime est l’éditeur de ce guide et ne garantit aucun classement.</p>\n',
 }),
]

GEO_SLUGS = [g["slug"] for g in GUIDES_GEO]
