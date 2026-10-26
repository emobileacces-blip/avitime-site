"""Page « Vos 5 premiers tests offerts » : /pionniers (FR, URL conservée : des e-mails déjà envoyés pointent dessus).
Générée par ce script ; ne pas éditer le HTML à la main.

Règles : aucun prix public (seuls les « 5 tests offerts » sont affichés), contrepartie affichée, et jamais d'avis demandé
en échange des tests offerts sur Trustpilot, Google, l'App Store Shopify ou WordPress.org.
Décision du 26/10/2026 (remplace le programme pionniers du 17/10 : 10 tests aux 10 premières boutiques) : « En ce moment :
vos 5 premiers tests offerts », pour toutes les nouvelles boutiques, sans limite de places, sans abonnement ni code, y compris
Shopify. Offre « en ce moment », sans date de fin promise. Les produits envoyés aux testeurs restent à la charge de la boutique.
On dit « tests offerts », jamais « avis offerts » : aucun volume d'avis n'est garanti, toutes les notes sont publiées.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_guides import HEAD, FOOT, AUTHOR, PUBLISHER

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "public")
PATH = "/pionniers"
TITLE = "Avitime : vos 5 premiers tests produits offerts"  # ≤ 60 caractères (audit SEO du 20/10)
DESC = ("En ce moment, toute nouvelle boutique PrestaShop, WooCommerce ou Shopify fait tester ses produits par 5 testeurs Avitime, "
        "sans abonnement ni code promo.")  # ≤ 160 caractères
APPLY = "https://app.avitime.fr/inscription?type=commercant"
QUESTION = "/contact?profil=boutique&sujet=Tests%20offerts#formulaire"

CSS = """<style>
.pi-steps{counter-reset:pi;list-style:none;padding:0!important;display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:14px!important;margin:18px 0 8px}
@media (max-width:700px){.pi-steps{grid-template-columns:minmax(0,1fr)}}
.pi-steps li{counter-increment:pi;background:var(--surface);border:1px solid var(--line);border-radius:18px;padding:18px 20px 18px 64px;position:relative;font-size:16px!important}
.pi-steps li::before{content:counter(pi);position:absolute;left:18px;top:18px;width:32px;height:32px;border-radius:50%;background:var(--hl);color:#0A0A0A;display:grid;place-items:center;font-weight:700;font-size:15px}
.pi-steps b{display:block;color:var(--ink);margin-bottom:2px}
.pi-cols{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:18px;margin:18px 0 8px}
@media (max-width:700px){.pi-cols{grid-template-columns:minmax(0,1fr)}}
.pi-col{background:var(--surface);border:1px solid var(--line);border-radius:20px;padding:20px 22px}
.pi-col h3{margin:0 0 8px!important}
.pi-col ul{margin:0}
.pi-col li{font-size:16px!important}
.pi-never{border-left:4px solid var(--bad,#B42318)}
.pi-empty{background:var(--bg-2);border:1px dashed var(--line);border-radius:18px;padding:18px 22px;margin:18px 0}
.pi-empty p{margin:0;font-size:16px!important}
</style>
</head>"""

BODY = f"""<article>
<section class="gd-hero"><div class="gd-wrap">
<p class="eyebrow">En ce moment</p>
<h1>Vos 5 premiers tests offerts</h1>
<p class="gd-lede">En ce moment, toute nouvelle boutique fait tester ses produits par 5 testeurs Avitime, sans abonnement. Pas d’appel, pas de code promo, pas de limite de places : les tests offerts s’appliquent automatiquement à votre première campagne.</p>
<div class="gd-by"><div class="av" aria-hidden="true">CQ</div><p><b>Cyril Quémy</b>, fondateur d’Avitime<br>Une question ? Je réponds moi-même à chaque message.</p></div>
</div></section>
<section class="gd-body"><div class="gd-wrap">

<h2>L’échange, en clair</h2>
<div class="pi-cols">
<div class="pi-col"><h3>Ce que vous recevez</h3><ul>
<li><b>5 tests offerts</b>, sans abonnement : jusqu’à 5 testeurs, sur une seule campagne ou répartis sur plusieurs.</li>
<li><b>Des testeurs sélectionnés par Avitime</b>, qui reçoivent votre produit, l’utilisent puis donnent leur avis.</li>
<li><b>Les avis des testeurs</b>, publiés sur vos fiches avec la mention « Produit offert pour test », quelle que soit la note.</li>
</ul></div>
<div class="pi-col"><h3>Ce qui reste à votre charge</h3><ul>
<li><b>Les produits envoyés aux testeurs</b> : c’est vous qui les offrez et les expédiez, comme pour toute campagne Avitime.</li>
<li><b>Si vous le voulez bien</b>, un court questionnaire à la fin de la campagne et votre accord pour une étude de cas sur avitime.fr, avec vos vrais chiffres. Vous la relisez et la validez avant publication, ou vous refusez : vos tests offerts n’en dépendent pas.</li>
</ul></div>
</div>
<div class="gd-key pi-never"><p><b>Ce que nous ne vous demanderons jamais :</b> un avis sur Avitime, positif ou non, sur Trustpilot, Google, l’App Store Shopify ou WordPress.org. Les tests offerts n’en dépendent pas. Plus tard, nous vous proposerons de donner votre avis, comme à tous nos clients, avec le même message neutre : libre à vous de le faire ou non, et de dire ce que vous pensez.</p></div>

<h2>Qui peut en profiter</h2>
<p>L’offre est ouverte à toutes les nouvelles boutiques, sans limite de places. Il suffit d’être :</p>
<ul>
<li>Une boutique <b>PrestaShop, WooCommerce ou Shopify</b> (l’application Shopify est en cours de validation : vous pouvez déjà créer votre compte).</li>
<li>Qui <b>livre en France</b>, puisque les testeurs Avitime y résident.</li>
<li>Avec un <b>produit physique ou numérique</b> que vous êtes prêt à offrir à quelques testeurs.</li>
<li>Portée par une <b>entreprise immatriculée</b> (SIRET, ou numéro de TVA pour la Belgique et l’UE).</li>
</ul>

<h2>Comment ça se passe</h2>
<ol class="pi-steps">
<li><b>Vous créez votre compte</b>Deux minutes, avec votre SIRET ou votre numéro de TVA, puis vous reliez votre boutique.</li>
<li><b>Vous lancez votre campagne</b>Sans choisir de formule ni saisir de code : vos 5 tests offerts s’appliquent automatiquement.</li>
<li><b>Avitime sélectionne les testeurs</b>Vous leur envoyez le produit ; ils le testent puis donnent leur avis.</li>
<li><b>Vous recevez les avis</b>Ils sont publiés sur vos fiches produit, quelle que soit la note. Vos 5 tests utilisés, vous choisissez une formule si vous voulez continuer.</li>
</ol>

<h2>Les conditions</h2>
<ul>
<li><b>5 tests offerts par boutique</b>, soit 5 testeurs au total, sans abonnement, sans engagement et sans code promo.</li>
<li><b>Les produits envoyés aux testeurs restent à votre charge</b>, ainsi que leur expédition.</li>
<li><b>Des tests offerts, pas des avis offerts</b> : chaque testeur s’engage à donner son avis, mais aucun volume d’avis n’est garanti. Les avis sont publiés quelle que soit la note, de 1 à 5 étoiles.</li>
<li><b>Une offre valable en ce moment</b>, sans date de fin annoncée : elle peut évoluer, et cette page sera mise à jour si c’est le cas.</li>
</ul>

<h2>Les études de cas</h2>
<div class="pi-empty"><p>Avitime démarre : les premières études de cas seront publiées ici. Elles montreront de vrais chiffres (nombre d’avis, délai, notes obtenues), y compris quand tout ne s’est pas passé comme prévu.</p></div>

<div class="gd-cta"><p><b>Envie de vous lancer ?</b> Vos 5 premiers tests sont offerts, sans abonnement.</p><a class="btn" href="{APPLY}">Créer mon compte commerçant</a></div>
<p style="margin-top:14px">Une question avant de vous lancer ? <a href="{QUESTION}">Écrivez-moi</a>.</p>
<p class="gd-note" style="margin-top:22px">Avitime est édité par SPARKMOTION AGENCY LTD. Les testeurs sont sélectionnés par Avitime, jamais par la boutique, et toutes les notes sont publiées, de 1 à 5 étoiles. <a href="/a-propos.html#methode">Notre méthode</a> · <a href="/cgv.html">CGV commerçants</a></p>
</div></section>
</article>
"""


def main():
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebPage", "name": TITLE, "description": DESC, "url": "https://avitime.fr" + PATH, "inLanguage": "fr-FR",
         "author": AUTHOR, "publisher": PUBLISHER},
        {"@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Accueil", "item": "https://avitime.fr/"},
            {"@type": "ListItem", "position": 2, "name": "Tests offerts", "item": "https://avitime.fr" + PATH}]}]}
    h = HEAD.format(title=TITLE, desc=DESC, path=PATH, ogtype="website", guides_current="")
    h = h.replace("</style>\n</head>", "</style>\n" + CSS, 1)
    out = h + BODY + FOOT.replace("{ld}", json.dumps(ld, ensure_ascii=False))
    dst = os.path.join(ROOT, "pionniers.html")
    open(dst, "w", encoding="utf-8").write(out)
    print(dst)


if __name__ == "__main__":
    main()
