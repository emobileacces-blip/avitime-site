# Guides pour les boutiques en ligne (21/10/2026), mots-clés Haloscan :
#   demander-avis-client       → exemple demande avis google (170), demander des avis (79), collecter des avis (70), mail pour demander un avis client (50)
#   fiche-produit-e-commerce   → comment faire une fiche produit (170), fiche produit e-commerce (40), exemple fiche produit
#   taux-conversion-e-commerce → calcul taux de conversion (720), taux de conversion e-commerce (100, concurrence facile)
#   lancer-nouveau-produit     → lancement d'un nouveau produit exemple (127), lancement d'un nouveau produit (45), plan de lancement
#   echantillonnage-produit    → échantillonnage marketing (90), échantillonnage produit (70)
# Maillage : chaque guide renvoie vers 3 à 6 guides boutiques existants (premiers avis, loi, combien d'avis, référencement…).

PUB = {"pub_iso": "2026-10-21", "pub_fr": "21 octobre 2026"}
NOTE = '<p class="gd-note">Article d’information générale, à jour au 21 octobre 2026. Avitime est l’éditeur de ce guide.</p>\n'

def src(label, url, title, extra=""):
    return f'<li>{label}, <a href="{url}" rel="noopener" target="_blank">{title}</a>{extra}</li>\n'

S_SPIEGEL = src("Spiegel Research Center, Northwestern University", "https://spiegel.medill.northwestern.edu/How-Online-Reviews-Influence-Sales", "« How Online Reviews Influence Sales »")
S_BARO = src("Avis Vérifiés by Skeepers, baromètre 2024, présenté par CB News", "https://www.cbnews.fr/etudes/75-consommateurs-consultent-les-avis-ligne-avant-achat", "« 75 % des consommateurs consultent les avis en ligne avant l’achat »", " (juillet 2024)")
S_DGCCRF = src("DGCCRF", "https://www.economie.gouv.fr/dgccrf/les-fiches-pratiques-et-les-faq/avis-en-ligne-attention-aux-faux-commentaires", "« Avis en ligne : attention aux faux commentaires ! »")
S_CNIL = src("CNIL", "https://www.cnil.fr/fr/cnil-direct/question/prospection-commerciale-par-courrier-electronique-fax-ou-sms-le-consentement", "« Prospection commerciale par courrier électronique, fax ou SMS : le consentement »")
S_GCR = src("Google Merchant Center", "https://support.google.com/merchants/answer/7106244", "« Avis clients Google »", " (aide Google, en anglais)")
S_BAYMARD = src("Baymard Institute", "https://baymard.com/lists/cart-abandonment-rate", "« Cart Abandonment Rate Statistics »", " (mis à jour en septembre 2025)")
S_CSQ = src("Contentsquare", "https://contentsquare.com/fr-fr/blog/taux-de-conversion/", "« Taux de conversion : définition, calcul et optimisation »")
S_CSQ25 = src("Contentsquare", "https://contentsquare.com/fr-fr/blog/2025-digital-experience-benchmarks/", "« Digital Experience Benchmark 2025 »")
S_BPI_ECOM = src("Bpifrance Création", "https://bpifrance-creation.fr/encyclopedie/vendre-ligne/obligations-juridiques-reglementaires/e-commerce-consommateurs-regles-a", "« E-commerce et consommateurs : les règles à respecter »", " (mai 2026)")
S_GOOGLE_PRODUCT = src("Google Search Central", "https://developers.google.com/search/docs/appearance/structured-data/product-snippet?hl=fr", "données structurées des extraits de produit")
S_BYU = src("Brigham Young University", "https://news.byu.edu/news/study-free-samples-increase-sales-work-better-end-aisle-promotions", "« Free samples increase sales »", " (étude publiée dans le Journal of Retailing)")
S_BPI_ETUDE = src("Bpifrance Création", "https://bpifrance-creation.fr/moment-de-vie/etude-marche-cest-indispensable-se-lancer", "« L’étude de marché, c’est indispensable pour se lancer ? »")
S_JPIM = src("Journal of Product Innovation Management", "https://metatoc.com/papers/19715-perspective-new-product-failure-rates-influence-of-argumentum-ad-populum-and-self-interest", "« New Product Failure Rates: Influence of Argumentum ad Populum and Self-Interest »", " (résumé)")

GUIDES_BOUTIQUES = [
 dict(PUB, **{
  "slug": "demander-avis-client",
  "related": ["premiers-avis-clients", "repondre-avis-negatifs", "faux-avis-loi"],
  "seo_title": "Demander un avis client : modèles d’e-mail et de SMS",
  "seo_desc": "Comment demander un avis client sans être lourd : le bon moment, des exemples d’e-mails et de SMS à copier, les règles CNIL et ce que la loi interdit.",
  "title": "Demander un avis client : le bon moment et des modèles d’e-mail à copier",
  "desc": "Quand envoyer la demande, quoi écrire, combien de relances : la méthode et des modèles d’e-mail et de SMS prêts à adapter, dans les règles de la CNIL et du Code de la consommation.",
  "kicker": "Guide · Avis clients",
  "lede": "La plupart des clients satisfaits ne laissent pas d’avis… parce qu’on ne le leur demande pas. Une demande simple, au bon moment, avec un lien direct, suffit souvent. Voici la méthode, des modèles à copier, et les règles à respecter.",
  "read": 7,
  "body": """
<nav class="gd-toc" aria-label="Sommaire"><p>Au sommaire</p><ol>
<li><a href="#moment">Le bon moment</a></li>
<li><a href="#bonne-demande">Ce que doit contenir la demande</a></li>
<li><a href="#modeles-email">Modèles d’e-mail</a></li>
<li><a href="#sms">Modèles de SMS</a></li>
<li><a href="#google">Avis sur Google : le programme Avis clients Google</a></li>
<li><a href="#regles">Les règles à respecter</a></li>
<li><a href="#aucun-client">Et quand on n’a pas encore de clients ?</a></li>
</ol></nav>

<div class="gd-key"><p><b>L’essentiel :</b> demandez l’avis quelques jours après la livraison, quand le client a pu utiliser le produit. Un message court, personnel, avec un lien direct vers la fiche produit. Demandez à tous vos clients, pas seulement aux plus contents, et une seule relance suffit.</p></div>

<h2 id="moment">1. Le bon moment</h2>
<p>Selon le baromètre 2024 d’Avis Vérifiés by Skeepers (72 000 consommateurs en France, en Espagne et en Italie), <b>71 % des clients qui laissent un avis le font dans les sept jours</b> qui suivent leur achat. La fenêtre est courte : passé quelques semaines, l’envie retombe.</p>
<ul>
<li><b>Produit à utiliser tout de suite</b> (accessoire, vêtement, déco) : 2 à 4 jours après la livraison.</li>
<li><b>Produit qui demande un peu de temps</b> (soin, complément, appareil) : 7 à 14 jours après la livraison.</li>
<li><b>Jamais avant la livraison</b> : un client qui n’a pas reçu son colis n’a rien à dire… sauf qu’il l’attend.</li>
</ul>

<h2 id="bonne-demande">2. Ce que doit contenir la demande</h2>
<ol>
<li><b>Le prénom du client et le nom du produit</b> : on répond plus volontiers à un message qui parle de son achat.</li>
<li><b>Un lien direct vers le formulaire d’avis</b> sur la fiche produit, sans connexion obligatoire si possible.</li>
<li><b>Une indication de durée</b> : « 1 minute » est plus engageant qu’un long formulaire.</li>
<li><b>Une vraie liberté</b> : « positif ou critique, votre avis nous aide ». Jamais « laissez-nous 5 étoiles ».</li>
<li><b>Un moyen de vous joindre</b> en cas de problème, pour régler un souci avant qu’il ne devienne un avis négatif… sans jamais conditionner l’avis à cette prise de contact.</li>
</ol>

<h2 id="modeles-email">3. Modèles d’e-mail</h2>
<h3>Premier envoi</h3>
<p><i>Objet : Votre [nom du produit] vous plaît ?</i></p>
<p><i>« Bonjour [Prénom], votre [nom du produit] est arrivé il y a quelques jours. Nous serions ravis d’avoir votre avis, qu’il soit enthousiaste ou critique : il aide les prochains clients à choisir, et nous aide à nous améliorer. Ça prend une minute : [lien vers l’avis]. Un souci avec votre commande ? Répondez simplement à cet e-mail. Merci ! [Prénom du vendeur], [Nom de la boutique] »</i></p>
<h3>Relance (une seule, 5 à 7 jours plus tard)</h3>
<p><i>Objet : Une minute pour votre avis ?</i></p>
<p><i>« Bonjour [Prénom], petit rappel : si vous avez un moment, votre avis sur [nom du produit] aiderait beaucoup les autres clients. [lien]. Si vous préférez ne pas en laisser, aucun souci, nous ne vous relancerons plus. »</i></p>
<h3>Pour une petite boutique, version plus personnelle</h3>
<p><i>« Bonjour [Prénom], c’est [Prénom], je prépare moi-même les commandes de [boutique]. Vous faites partie de nos premiers clients pour [produit] : votre retour, même critique, m’aiderait énormément. [lien]. Merci du fond du cœur. »</i></p>

<h2 id="sms">4. Modèles de SMS</h2>
<p>Le SMS est plus intrusif : réservez-le aux clients qui ont accepté d’être contactés par SMS, et restez très court.</p>
<p><i>« [Boutique] : bonjour [Prénom], votre [produit] vous plaît ? Votre avis en 1 min : [lien court]. STOP au [numéro] »</i></p>

<h2 id="google">5. Avis sur Google : le programme Avis clients Google</h2>
<p>Google propose aux marchands inscrits sur Google Merchant Center un programme de collecte : un module s’affiche sur votre page de confirmation de commande, et si le client l’accepte, <b>Google lui envoie une enquête après la date de livraison estimée</b>. Ces avis alimentent la note de votre boutique dans Google, qui demande en général <b>au moins 100 avis</b> pour s’afficher (voir <a href="/guides/combien-avis-clients.html#google">Combien d’avis faut-il pour vendre ?</a>).</p>
<p>Pour les avis sur vos fiches produits, ce sont les avis affichés en texte sur votre site et leurs données structurées qui comptent : voir <a href="/guides/referencement-boutique-en-ligne.html#etoiles">les étoiles dans Google</a>.</p>

<h2 id="regles">6. Les règles à respecter</h2>
<ul>
<li><b>Ne triez pas vos clients.</b> La DGCCRF considère comme trompeur le fait d’écarter les avis négatifs ; demander l’avis à tous, et publier tous les avis, c’est la meilleure protection.</li>
<li><b>Ne payez pas une note.</b> Une réduction contre « 5 étoiles », c’est fabriquer de faux avis : jusqu’à 2 ans de prison et 300 000 € d’amende, voire davantage en ligne (voir <a href="/guides/faux-avis-loi.html">ce que dit la loi</a>).</li>
<li><b>Affichez les bonnes informations</b> à côté de vos avis : date, contrôle éventuel, et contrepartie s’il y en a une. Le détail est dans <a href="/guides/faux-avis-loi.html#obligations">ce qu’une boutique doit afficher</a>.</li>
<li><b>Respectez la CNIL pour vos e-mails.</b> Pour la prospection, la CNIL exige en principe un consentement, sauf pour vos clients sur des produits analogues, qui doivent alors pouvoir s’opposer simplement à chaque envoi. La CNIL ne traite pas spécifiquement des demandes d’avis : le plus prudent est d’appliquer les mêmes précautions, avec un lien pour ne plus recevoir ces messages, et de ne pas y glisser de publicité.</li>
</ul>

<h2 id="aucun-client">7. Et quand on n’a pas encore de clients ?</h2>
<p>La demande d’avis tourne à vide tant que les commandes sont rares. Pour amorcer, la solution honnête est de faire <b>tester vos produits</b> par de vrais consommateurs, avec la mention de la contrepartie : voir <a href="/guides/premiers-avis-clients.html">Obtenir ses premiers avis clients</a> et <a href="/guides/echantillonnage-produit.html">l’échantillonnage produit</a>. C’est ce que fait Avitime : des testeurs sélectionnés par Avitime commandent le produit à 0 € sur votre boutique et publient un avis argumenté, avec la mention « Produit offert pour test ».</p>

<h2 id="sources">Sources</h2>
<ul class="gd-src">
""" + S_BARO + S_GCR + S_DGCCRF + S_CNIL + "</ul>\n" +
  '<p class="gd-note">Article d’information générale, à jour au 21 octobre 2026. Les modèles de messages sont à adapter à votre boutique ; ils ne remplacent pas un conseil juridique. Avitime est l’éditeur de ce guide.</p>\n',
 }),

 dict(PUB, **{
  "slug": "fiche-produit-e-commerce",
  "related": ["referencement-boutique-en-ligne", "taux-conversion-e-commerce", "combien-avis-clients"],
  "seo_title": "Fiche produit e-commerce : méthode et exemple (2026)",
  "seo_desc": "Comment faire une fiche produit e-commerce qui vend : titre, description, photos, mentions obligatoires, avis clients et données structurées. Exemple commenté.",
  "title": "Fiche produit e-commerce : la méthode, les mentions obligatoires et un exemple",
  "desc": "Titre, description, photos, prix, livraison, avis : comment construire une fiche produit qui rassure et qui vend, avec les informations que la loi impose et un exemple commenté.",
  "kicker": "Guide · E-commerce",
  "lede": "Sur une boutique en ligne, la fiche produit fait le travail du vendeur en magasin : montrer, expliquer, rassurer, répondre aux questions. Voici comment la construire, bloc par bloc, avec ce que la loi impose et un exemple commenté.",
  "read": 8,
  "body": """
<nav class="gd-toc" aria-label="Sommaire"><p>Au sommaire</p><ol>
<li><a href="#blocs">Les blocs d’une bonne fiche produit</a></li>
<li><a href="#titre">Le titre</a></li>
<li><a href="#description">La description</a></li>
<li><a href="#photos">Les photos</a></li>
<li><a href="#obligatoire">Les mentions obligatoires</a></li>
<li><a href="#avis">Les avis clients</a></li>
<li><a href="#google">Ce que Google lit</a></li>
<li><a href="#exemple">Un exemple commenté</a></li>
</ol></nav>

<div class="gd-key"><p><b>L’essentiel :</b> une bonne fiche produit répond, avant qu’on les pose, aux questions d’un client qui ne peut ni toucher ni essayer : à quoi ça sert, pour qui, quelle taille, quelle matière, quand je le reçois, et qu’en pensent ceux qui l’ont acheté.</p></div>

<h2 id="blocs">1. Les blocs d’une bonne fiche produit</h2>
<ol>
<li>un <b>titre</b> clair ;</li>
<li>des <b>photos</b> qui montrent le produit sous tous les angles et en situation ;</li>
<li>le <b>prix</b>, la <b>disponibilité</b> et le <b>délai de livraison</b>, visibles sans chercher ;</li>
<li>une <b>description</b> utile : bénéfices, usage, caractéristiques ;</li>
<li>les <b>caractéristiques techniques</b> en liste (dimensions, matière, entretien, compatibilité) ;</li>
<li>les <b>avis clients</b> ;</li>
<li>les <b>informations rassurantes</b> : retours, garanties, paiement, contact.</li>
</ol>

<h2 id="titre">2. Le titre</h2>
<p>Le titre dit ce qu’est le produit, avec les mots que tapent vos clients : type de produit, caractéristique principale, éventuellement la marque, la taille ou la couleur. « Coussin en lin lavé 45 × 45 cm, terracotta » vaut mieux que « Coussin Sienna ». Un titre unique par produit : deux fiches presque identiques se font concurrence dans Google (voir <a href="/guides/referencement-boutique-en-ligne.html#pages">une page, une recherche</a>).</p>

<h2 id="description">3. La description</h2>
<ul>
<li><b>Commencez par le bénéfice</b> : à quoi sert le produit, quel problème il règle, pour qui il est fait.</li>
<li><b>Décrivez l’usage réel</b> : comment on s’en sert, dans quelle pièce, à quelle saison, avec quoi on l’associe.</li>
<li><b>Répondez aux objections</b> : taille, entretien, résistance, ce qui est inclus ou non.</li>
<li><b>Écrivez avec vos mots</b>, pas ceux du fournisseur : une description copiée chez un fournisseur se retrouve sur des dizaines de sites, et Google n’en met généralement qu’une en avant.</li>
<li><b>Restez exact</b> : une description trompeuse sur les caractéristiques est une pratique commerciale trompeuse, et elle vous vaudra des retours… et des avis négatifs.</li>
</ul>

<h2 id="photos">4. Les photos</h2>
<ul>
<li>une photo principale nette sur fond neutre ;</li>
<li>plusieurs angles et les détails (matière, finitions, étiquette) ;</li>
<li>au moins une photo <b>en situation</b> pour donner l’échelle ;</li>
<li>un texte alternatif descriptif pour chaque image (accessibilité et référencement).</li>
</ul>
<p>Les photos de vos clients ou testeurs, publiées avec leur avis, complètent idéalement les vôtres : elles montrent le produit dans une vraie maison.</p>

<h2 id="obligatoire">5. Les mentions obligatoires</h2>
<p>Pour une vente à distance à des particuliers, le Code de la consommation impose d’informer le client avant la commande. Selon Bpifrance Création, cela comprend notamment :</p>
<ul>
<li>les <b>caractéristiques essentielles</b> du produit ;</li>
<li>le <b>prix TTC</b> et les éventuels frais de livraison ;</li>
<li>le <b>délai de livraison</b> (à défaut d’indication, la livraison doit intervenir au plus tard 30 jours après la commande) ;</li>
<li>les <b>garanties légales</b> et le <b>droit de rétractation de 14 jours</b>, avec ses conditions ;</li>
<li>l’<b>identité et les coordonnées</b> du vendeur, et l’accès aux conditions générales de vente.</li>
</ul>
<p>Certaines informations vivent sur des pages dédiées (CGV, mentions légales), mais le prix, la disponibilité et le délai doivent être visibles sur la fiche. Et si vous affichez des avis, des mentions s’ajoutent : voir <a href="/guides/faux-avis-loi.html#obligations">ce qu’une boutique doit afficher</a>.</p>

<h2 id="avis">6. Les avis clients</h2>
<p>C’est souvent le bloc qui décide. Selon le Spiegel Research Center, un produit avec <b>cinq avis</b> a une probabilité d’achat <b>270 % plus élevée</b> qu’un produit sans avis, et la note qui inspire le plus confiance se situe <b>entre 4,0 et 4,7</b>. Les avis répondent aussi aux questions que votre description a oubliées. Pour les obtenir : <a href="/guides/premiers-avis-clients.html">Obtenir ses premiers avis clients</a> et <a href="/guides/demander-avis-client.html">Demander un avis client</a>.</p>

<h2 id="google">7. Ce que Google lit</h2>
<p>Google peut afficher dans ses résultats le prix, la disponibilité, la note et les avis d’un produit, grâce aux <b>données structurées Product</b> placées dans la page. Il faut au minimum le nom du produit et l’un de ces éléments : des avis, une note moyenne ou une offre (prix). Google réserve ce balisage aux pages qui présentent un seul produit, et ne garantit jamais l’affichage. PrestaShop, WooCommerce et Shopify ajoutent souvent ce balisage via le thème ou un module : vérifiez-le avec l’outil de test des résultats enrichis de Google.</p>

<h2 id="exemple">8. Un exemple commenté</h2>
<div class="tbl-wrap gd-tbl"><table>
<thead><tr><th>Bloc</th><th>Exemple (boutique fictive)</th><th>Pourquoi</th></tr></thead>
<tbody>
<tr><td>Titre</td><td>Coussin en lin lavé 45 × 45 cm, terracotta</td><td>Type, matière, taille, couleur : les mots que tape le client</td></tr>
<tr><td>Accroche</td><td>Un lin épais et doux, qui se froisse joliment et se lave en machine.</td><td>Le bénéfice en une phrase</td></tr>
<tr><td>Usage</td><td>Pour le canapé ou un fauteuil de lecture ; s’associe aux tons naturels.</td><td>Le client se projette</td></tr>
<tr><td>Caractéristiques</td><td>100 % lin, housse amovible, garnissage plumes, lavage 30 °C</td><td>Répond aux questions avant qu’elles ne soient posées</td></tr>
<tr><td>Livraison et retours</td><td>Expédié sous 48 h · livré en 3 à 5 jours · retours sous 14 jours</td><td>Rassure et respecte l’obligation d’information</td></tr>
<tr><td>Avis</td><td>Note, nombre d’avis, avis détaillés avec photos, critiques comprises</td><td>La preuve sociale qui décide</td></tr>
</tbody></table></div>
<p>Pour la partie référencement (mots-clés, une page par recherche, Search Console), voir <a href="/guides/referencement-boutique-en-ligne.html#fiche">la fiche produit en 5 points</a> dans notre guide du référencement.</p>

<h2 id="sources">Sources</h2>
<ul class="gd-src">
""" + S_BPI_ECOM + S_GOOGLE_PRODUCT + S_SPIEGEL + "</ul>\n" +
  '<p class="gd-note">Article d’information générale, à jour au 21 octobre 2026 ; il ne remplace pas un conseil juridique. L’exemple est fictif. Avitime est l’éditeur de ce guide.</p>\n',
 }),

 dict(PUB, **{
  "slug": "taux-conversion-e-commerce",
  "related": ["fiche-produit-e-commerce", "combien-avis-clients", "statistiques-avis-clients"],
  "seo_title": "Taux de conversion e-commerce : calcul, repères et leviers",
  "seo_desc": "Comment calculer le taux de conversion de votre boutique en ligne, quels repères utiliser, pourquoi les paniers sont abandonnés et les leviers pour l’améliorer.",
  "title": "Taux de conversion e-commerce : le calcul, les repères et les leviers pour l’améliorer",
  "desc": "La formule, les repères publiés, les raisons des paniers abandonnés et les leviers concrets pour transformer plus de visiteurs en clients, avis clients compris.",
  "kicker": "Guide · E-commerce",
  "lede": "Sur cent visiteurs, combien achètent ? C’est le taux de conversion, l’indicateur qui dit si votre boutique transforme ses visites en ventes. Voici comment le calculer, comment le lire sans se comparer à n’importe quoi, et sur quoi agir.",
  "read": 7,
  "body": """
<nav class="gd-toc" aria-label="Sommaire"><p>Au sommaire</p><ol>
<li><a href="#calcul">Le calcul</a></li>
<li><a href="#reperes">Quel est un bon taux de conversion ?</a></li>
<li><a href="#abandon">Pourquoi les paniers sont abandonnés</a></li>
<li><a href="#leviers">Les leviers pour l’améliorer</a></li>
<li><a href="#avis">Le rôle des avis clients</a></li>
<li><a href="#mesurer">Mesurer sans se tromper</a></li>
</ol></nav>

<div class="gd-key"><p><b>L’essentiel :</b> taux de conversion = commandes ÷ visites × 100. Comparez-vous d’abord à vous-même, mois après mois, plutôt qu’à une moyenne mondiale. Les leviers les plus simples : frais de livraison clairs dès la fiche produit, un paiement sans compte obligatoire, et des avis clients sur vos produits phares.</p></div>

<h2 id="calcul">1. Le calcul</h2>
<p><b>Taux de conversion = (nombre de commandes × 100) ÷ nombre de visites.</b></p>
<p>Exemple : 1 200 visites et 18 commandes dans le mois donnent 18 × 100 ÷ 1 200 = <b>1,5 %</b>.</p>
<p>Attention à ce que vous comptez : des visites (sessions) ou des visiteurs uniques, des commandes ou des clients. Gardez toujours la même définition pour pouvoir comparer d’un mois sur l’autre. Vous pouvez aussi calculer un taux par page : sur une fiche produit, le taux d’ajout au panier dit si la fiche convainc.</p>

<h2 id="reperes">2. Quel est un bon taux de conversion ?</h2>
<p>Il n’existe pas de chiffre universel. Contentsquare le dit lui-même : le « bon » taux dépend du secteur, de la source du trafic, de la saison, du produit et de l’appareil. Dans sa FAQ, l’éditeur cite <b>2 %</b> comme un bon taux en e-commerce, à prendre comme un ordre de grandeur.</p>
<p>Ce qui compte vraiment, c’est votre tendance. Et le contexte n’aide pas : le Digital Experience Benchmark 2025 de Contentsquare, établi sur plus de 90 milliards de sessions, note que la conversion a continué de baisser en 2024 et que <b>53 % des visiteurs quittent un site après une seule page</b>. Chaque visite compte.</p>

<h2 id="abandon">3. Pourquoi les paniers sont abandonnés</h2>
<p>Le Baymard Institute, qui compile 50 études, mesure un taux d’abandon de panier moyen de <b>70,22 %</b>. En mettant de côté les visiteurs qui ne faisaient que regarder, les raisons les plus citées sont :</p>
<div class="tbl-wrap gd-tbl"><table>
<thead><tr><th>Raison de l’abandon</th><th>Part des acheteurs</th></tr></thead>
<tbody>
<tr><td>Frais supplémentaires trop élevés (livraison, taxes)</td><td>40 %</td></tr>
<tr><td>Livraison trop lente</td><td>20 %</td></tr>
<tr><td>Pas confiance pour donner sa carte bancaire</td><td>19 %</td></tr>
<tr><td>Création de compte obligatoire</td><td>18 %</td></tr>
<tr><td>Paiement trop long ou compliqué</td><td>17 %</td></tr>
<tr><td>Erreurs ou plantages du site</td><td>17 %</td></tr>
<tr><td>Politique de retour insatisfaisante</td><td>13 %</td></tr>
</tbody></table></div>
<p>Source : Baymard Institute, enquête auprès d’acheteurs américains. Les ordres de grandeur sont parlants pour toute boutique en ligne.</p>

<h2 id="leviers">4. Les leviers pour l’améliorer</h2>
<ol>
<li><b>Annoncez les frais de livraison dès la fiche produit</b>, et le délai. La mauvaise surprise au panier est la première cause d’abandon.</li>
<li><b>Permettez la commande sans création de compte.</b></li>
<li><b>Rassurez</b> : moyens de paiement connus, politique de retour claire, coordonnées visibles.</li>
<li><b>Soignez vos fiches produits</b> : photos, description utile, caractéristiques (voir <a href="/guides/fiche-produit-e-commerce.html">Fiche produit e-commerce : la méthode</a>).</li>
<li><b>Accélérez votre site, surtout sur mobile</b> (voir <a href="/guides/referencement-boutique-en-ligne.html#mobile">mobile et vitesse</a>).</li>
<li><b>Ajoutez des avis clients</b> sur vos produits phares.</li>
</ol>

<h2 id="avis">5. Le rôle des avis clients</h2>
<p>Les avis agissent directement sur la décision. Selon le Spiegel Research Center, un produit avec <b>cinq avis</b> a une probabilité d’achat <b>270 % plus élevée</b> qu’un produit sans avis ; l’effet monte à <b>+380 %</b> pour un produit cher, et un badge « acheteur vérifié » ajoute <b>15 %</b>. Au-delà des cinq premiers avis, chaque avis supplémentaire apporte moins : la priorité est donc de sortir vos produits phares du « zéro avis ». Voir <a href="/guides/combien-avis-clients.html">Combien d’avis faut-il pour vendre ?</a></p>

<h2 id="mesurer">6. Mesurer sans se tromper</h2>
<ul>
<li>Mesurez par <b>source de trafic</b> : un visiteur venu de Google Shopping n’a pas la même intention qu’un visiteur venu d’Instagram.</li>
<li>Comparez à <b>période égale</b> : décembre ne se compare pas à août.</li>
<li>Changez <b>une chose à la fois</b>, et attendez assez de visites pour conclure.</li>
<li>Suivez aussi le <b>panier moyen</b> : convertir plus en vendant moins cher n’est pas toujours gagnant.</li>
</ul>

<h2 id="sources">Sources</h2>
<ul class="gd-src">
""" + S_CSQ + S_CSQ25 + S_BAYMARD + S_SPIEGEL + "</ul>\n" + NOTE,
 }),

 dict(PUB, **{
  "slug": "lancer-nouveau-produit",
  "related": ["premiers-avis-clients", "echantillonnage-produit", "fiche-produit-e-commerce"],
  "seo_title": "Lancer un nouveau produit en ligne : plan et exemple",
  "seo_desc": "Le plan de lancement d’un nouveau produit pour une boutique en ligne : tester la demande, préparer la fiche, obtenir les premiers avis et suivre les ventes.",
  "title": "Lancer un nouveau produit en ligne : le plan en 6 étapes, avec un exemple",
  "desc": "Tester la demande, préparer la fiche, obtenir les premiers avis avant le lancement, annoncer, puis mesurer : un plan simple pour une petite boutique, et un exemple de calendrier.",
  "kicker": "Guide · E-commerce",
  "lede": "Un nouveau produit en ligne démarre avec un handicap : personne ne le connaît, et sa fiche n’a aucun avis. Voici un plan en six étapes pour une petite boutique, avec un exemple de calendrier, pour que le lancement ne se joue pas à pile ou face.",
  "read": 7,
  "body": """
<nav class="gd-toc" aria-label="Sommaire"><p>Au sommaire</p><ol>
<li><a href="#echec">Le mythe des 95 % d’échecs</a></li>
<li><a href="#plan">Le plan en 6 étapes</a></li>
<li><a href="#calendrier">Un exemple de calendrier</a></li>
<li><a href="#message">Le message de lancement</a></li>
<li><a href="#erreurs">Les erreurs à éviter</a></li>
</ol></nav>

<div class="gd-key"><p><b>L’essentiel :</b> validez la demande avant de commander du stock, préparez une fiche produit complète, et ne lancez pas un produit avec zéro avis : faites-le tester avant, en toute transparence. Puis mesurez pendant quatre semaines avant de juger.</p></div>

<h2 id="echec">1. Le mythe des 95 % d’échecs</h2>
<p>On lit souvent que « 95 % des nouveaux produits échouent », chiffre attribué à Clayton Christensen. Nous n’avons trouvé aucune étude d’origine pour ce chiffre. Une analyse publiée dans le <i>Journal of Product Innovation Management</i> qualifie même de « mythe tenace » l’idée d’un taux d’échec de 80 % ou plus : les études menées depuis 1977 trouvent plutôt <b>40 % ou moins</b>.</p>
<p>Un lancement reste risqué, mais il se prépare. Bpifrance Création le rappelle : une étude de marché ne garantit pas le succès, elle sert à <b>réduire les risques</b>.</p>

<h2 id="plan">2. Le plan en 6 étapes</h2>
<h3>Étape 1 : tester la demande</h3>
<p>Avant de commander du stock, vérifiez que le produit répond à une recherche ou à un besoin : mots-clés tapés dans Google (voir <a href="/guides/referencement-boutique-en-ligne.html#mots-cles">choisir ses mots-clés</a>), questions de vos clients, produits similaires qui se vendent. Bpifrance cite trois méthodes simples : interroger des acheteurs potentiels, analyser des projets similaires, et tester « en grandeur nature » sur une petite quantité. Faites une estimation basse et une estimation haute.</p>
<h3>Étape 2 : préparer la fiche produit</h3>
<p>Titre clair, photos en situation, description utile, prix, délai et frais de livraison visibles. La méthode complète : <a href="/guides/fiche-produit-e-commerce.html">Fiche produit e-commerce</a>.</p>
<h3>Étape 3 : obtenir les premiers avis avant le lancement</h3>
<p>Un produit avec cinq avis a une probabilité d’achat 270 % plus élevée qu’un produit sans avis (Spiegel Research Center). Faites tester le produit par quelques consommateurs avant l’annonce : c’est l’<a href="/guides/echantillonnage-produit.html">échantillonnage produit</a>. Leurs avis, signalés comme « produit offert pour test », seront en ligne le jour J.</p>
<h3>Étape 4 : préparer l’annonce</h3>
<p>Prévenez ceux qui vous connaissent déjà : clients, abonnés à la newsletter (s’ils ont accepté de la recevoir), réseaux sociaux. Préparez deux ou trois visuels et un message court.</p>
<h3>Étape 5 : lancer</h3>
<p>Mettez le produit en avant sur la page d’accueil, envoyez l’annonce, publiez. Vérifiez vous-même le parcours d’achat complet, sur mobile.</p>
<h3>Étape 6 : mesurer et ajuster</h3>
<p>Pendant quatre semaines : visites de la fiche, taux d’ajout au panier, ventes, questions reçues, avis. Ajustez la fiche en fonction de ce que disent les premiers clients (voir <a href="/guides/taux-conversion-e-commerce.html">taux de conversion</a>).</p>

<h2 id="calendrier">3. Un exemple de calendrier</h2>
<div class="tbl-wrap gd-tbl"><table>
<thead><tr><th>Quand</th><th>Quoi</th></tr></thead>
<tbody>
<tr><td>J − 45</td><td>Tester la demande, commander une petite série</td></tr>
<tr><td>J − 30</td><td>Photos, fiche produit, lancement d’un test auprès de quelques consommateurs</td></tr>
<tr><td>J − 10</td><td>Premiers avis publiés sur la fiche, préparation de l’annonce</td></tr>
<tr><td>Jour J</td><td>Mise en avant sur le site, newsletter, réseaux sociaux</td></tr>
<tr><td>J + 7</td><td>Demande d’avis aux premiers acheteurs (voir <a href="/guides/demander-avis-client.html">nos modèles</a>)</td></tr>
<tr><td>J + 30</td><td>Bilan : conversion, avis, retours ; décision de réassort</td></tr>
</tbody></table></div>

<h2 id="message">4. Le message de lancement</h2>
<p>Un exemple à adapter : <i>« Nouveau chez [boutique] : [produit], [bénéfice en une phrase]. Nous l’avons fait tester avant de le lancer : voici ce qu’en disent nos premiers testeurs. [lien] »</i>. Montrer de vrais avis dès l’annonce rassure bien plus qu’un slogan.</p>

<h2 id="erreurs">5. Les erreurs à éviter</h2>
<ul>
<li><b>Commander tout le stock avant d’avoir testé la demande.</b></li>
<li><b>Lancer une fiche vide</b> : sans avis ni photos en situation, le visiteur ne prend pas le risque.</li>
<li><b>Fabriquer des avis</b> pour le lancement : c’est une pratique commerciale trompeuse, lourdement sanctionnée (voir <a href="/guides/faux-avis-loi.html">ce que dit la loi</a>).</li>
<li><b>Juger au bout de trois jours</b> : un lancement se mesure sur plusieurs semaines.</li>
</ul>

<h2 id="sources">Sources</h2>
<ul class="gd-src">
""" + S_JPIM + S_BPI_ETUDE + S_SPIEGEL + "</ul>\n" +
  '<p class="gd-note">Article d’information générale, à jour au 21 octobre 2026. Le calendrier est un exemple, à adapter à votre produit. Avitime est l’éditeur de ce guide.</p>\n',
 }),

 dict(PUB, **{
  "slug": "echantillonnage-produit",
  "related": ["premiers-avis-clients", "comparatif-solutions-avis-clients", "faux-avis-loi"],
  "seo_title": "Échantillonnage produit : faire tester ses produits",
  "seo_desc": "L’échantillonnage produit (sampling) pour une boutique en ligne : à quoi ça sert, ce que montrent les études, comment l’organiser et les règles sur les avis.",
  "title": "Échantillonnage produit : faire tester ses produits pour vendre plus",
  "desc": "Le sampling, ou échantillonnage produit : ce que c’est, ce que disent les études, comment l’adapter à une boutique en ligne, et les règles à respecter quand le test donne lieu à un avis.",
  "kicker": "Guide · Marketing",
  "lede": "Faire goûter, faire essayer : l’échantillonnage est l’une des plus vieilles techniques du commerce. En ligne, le principe reste le même, avec un bonus : le client qui a testé peut laisser un avis que liront tous les suivants. Voici comment s’y prendre, et dans quelles règles.",
  "read": 6,
  "body": """
<nav class="gd-toc" aria-label="Sommaire"><p>Au sommaire</p><ol>
<li><a href="#definition">Échantillonnage produit : la définition</a></li>
<li><a href="#etudes">Ce que montrent les études</a></li>
<li><a href="#en-ligne">L’échantillonnage pour une boutique en ligne</a></li>
<li><a href="#organiser">Organiser un test produit</a></li>
<li><a href="#regles">Les règles sur les avis</a></li>
<li><a href="#cout">Le coût</a></li>
</ol></nav>

<div class="gd-key"><p><b>L’essentiel :</b> l’échantillonnage consiste à faire essayer gratuitement un produit pour déclencher l’achat. En ligne, sa forme la plus utile est le test produit : de vrais consommateurs reçoivent le produit, l’utilisent, puis publient un avis signalé comme « produit offert ». Les testeurs doivent rester libres de leur note.</p></div>

<h2 id="definition">1. Échantillonnage produit : la définition</h2>
<p>En marketing, l’échantillonnage (ou <i>sampling</i>) consiste à distribuer gratuitement un produit, en format réduit ou en taille réelle, pour le faire découvrir. L’objectif : lever le frein de l’inconnu. On hésite à payer pour un produit qu’on n’a jamais essayé ; une fois testé, la décision devient facile.</p>
<p>Attention, le mot « échantillonnage » désigne aussi, en statistique, la façon de choisir un échantillon représentatif pour une enquête. Ici, on parle bien de faire essayer un produit.</p>

<h2 id="etudes">2. Ce que montrent les études</h2>
<p>Une étude de chercheurs américains publiée dans le <i>Journal of Retailing</i>, menée sur des données de caisse en magasin, montre que l’échantillonnage a <b>un effet immédiat et un effet durable</b> sur les ventes, bien plus fort que celui d’un présentoir en bout de rayon : l’effet du présentoir disparaît au bout de deux semaines, celui des échantillons dure plusieurs semaines. Les auteurs notent aussi une limite de rentabilité : l’opération cesse d’être rentable quand son coût dépasse environ 15 fois le prix unitaire du produit.</p>
<p>L’étude porte sur des produits alimentaires vendus en magasin : ses chiffres ne se transposent pas tels quels à la vente en ligne, mais le mécanisme est le même.</p>

<h2 id="en-ligne">3. L’échantillonnage pour une boutique en ligne</h2>
<p>En ligne, distribuer des échantillons au hasard coûte cher et se mesure mal. Le test produit est plus efficace, pour trois raisons :</p>
<ul>
<li><b>Il cible</b> : le produit va à des consommateurs qui correspondent à vos clients.</li>
<li><b>Il laisse une trace</b> : l’avis du testeur reste sur la fiche produit et convainc les visiteurs suivants. Cinq avis suffisent à changer la probabilité d’achat (voir <a href="/guides/combien-avis-clients.html">Combien d’avis faut-il pour vendre ?</a>).</li>
<li><b>Il apprend</b> : les retours des testeurs vous disent ce qu’il faut corriger dans le produit ou la fiche.</li>
</ul>
<p>Les clubs de testeurs grand public (Sampleo, trnd…) travaillent surtout pour de grandes marques, et les retours restent sur leur plateforme ou les réseaux sociaux. Pour une boutique, l’intérêt est que l’avis soit publié <b>sur sa propre fiche produit</b>. Le comparatif des solutions est dans <a href="/guides/comparatif-solutions-avis-clients.html">notre comparatif honnête</a>.</p>

<h2 id="organiser">4. Organiser un test produit</h2>
<ol>
<li><b>Choisissez vos produits phares</b>, ou un produit qui se lance (voir <a href="/guides/lancer-nouveau-produit.html">lancer un nouveau produit</a>).</li>
<li><b>Fixez le nombre de testeurs</b> : cinq à dix par produit suffisent pour franchir le cap des premiers avis.</li>
<li><b>Faites sélectionner les testeurs par un tiers</b>, pas par vous : la neutralité de l’avis est meilleure, et plus crédible.</li>
<li><b>Envoyez le produit par une vraie commande</b> : l’avis est relié à une commande, comme celui d’un acheteur.</li>
<li><b>Laissez le temps de tester</b>, puis demandez un avis détaillé : contexte, durée, points forts et points faibles, photos.</li>
<li><b>Publiez tous les avis</b>, quelle que soit la note, et répondez-y (voir <a href="/guides/repondre-avis-negatifs.html">répondre aux avis négatifs</a>).</li>
</ol>

<h2 id="regles">5. Les règles sur les avis</h2>
<p>Offrir un produit en échange d’un avis est autorisé, à deux conditions :</p>
<ul>
<li><b>L’avis reste libre</b> : aucune note imposée, aucune pression, aucun tri des avis négatifs. La DGCCRF range parmi les pratiques trompeuses le fait de publier ou faire publier de faux avis, et met en garde les particuliers démarchés pour des avis positifs contre un produit gratuit.</li>
<li><b>La contrepartie est signalée</b> : le Code de la consommation impose d’informer le lecteur lorsqu’un avis a donné lieu à une contrepartie. Les mentions à afficher sont détaillées dans <a href="/guides/faux-avis-loi.html#obligations">ce qu’une boutique doit afficher</a>.</li>
</ul>
<p>Chez Avitime, chaque avis porte la mention « Produit offert pour test — Testeur Avitime vérifié », toutes les notes de 1 à 5 sont publiées, et la boutique ne peut ni modifier ni supprimer un avis.</p>

<h2 id="cout">6. Le coût</h2>
<p>Le coût d’un test produit, c’est d’abord le produit offert et sa livraison, puis la plateforme si vous en utilisez une. Comparez-le à ce que coûte une fiche sans avis : des visiteurs qui repartent. Avec la limite de rentabilité relevée par l’étude du <i>Journal of Retailing</i> en tête, réservez l’échantillonnage aux produits où un avis change vraiment la décision : produits phares, nouveautés, produits chers.</p>
<p>Avitime organise ces tests pour les boutiques PrestaShop et WooCommerce (Shopify en cours de validation) : <a href="/#commercants">découvrir l’offre commerçants</a>.</p>

<h2 id="sources">Sources</h2>
<ul class="gd-src">
""" + S_BYU + S_DGCCRF + S_SPIEGEL +
  src("INC (Institut national de la consommation)", "https://www.inc-conso.fr/content/avis-en-ligne-ce-qui-change-au-1er-janvier-2018", "« Avis en ligne : ce qui change au 1er janvier 2018 »") +
  "</ul>\n" + NOTE,
 }),
]

BOUTIQUE_SLUGS = [g["slug"] for g in GUIDES_BOUTIQUES]
