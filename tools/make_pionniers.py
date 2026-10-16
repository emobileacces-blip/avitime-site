"""Page « Programme pionniers » : /pionniers (FR). Générée par ce script ; ne pas éditer le HTML à la main.

Règles : aucun prix public (le tarif pionnier est donné en privé), contrepartie affichée, et jamais d'avis demandé
en échange du tarif sur Trustpilot, Google, l'App Store Shopify ou WordPress.org.
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_guides import HEAD, FOOT, AUTHOR, PUBLISHER

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "public")
PATH = "/pionniers"
TITLE = "Programme pionniers Avitime : 10 boutiques pour lancer les premiers tests"
DESC = ("Avitime démarre et cherche 10 boutiques PrestaShop, WooCommerce ou Shopify pour ses premières campagnes de test : "
        "tarif pionnier, accompagnement par le fondateur, étude de cas validée par vous.")
APPLY = "/contact?profil=boutique&sujet=Programme%20pionniers#formulaire"

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
<p class="eyebrow">Programme pionniers</p>
<h1>10 boutiques pour lancer les premiers tests Avitime</h1>
<p class="gd-lede">Avitime démarre. Nous cherchons dix boutiques en ligne pour mener les premières campagnes de test avec nous : un tarif pionnier, un accompagnement personnel, et de vrais avis sur vos fiches produit.</p>
<div class="gd-by"><div class="av" aria-hidden="true">CQ</div><p><b>Cyril Quémy</b>, fondateur d’Avitime<br>Je réponds moi-même à chaque candidature.</p></div>
</div></section>
<section class="gd-body"><div class="gd-wrap">

<h2>L’échange, en clair</h2>
<div class="pi-cols">
<div class="pi-col"><h3>Ce que vous recevez</h3><ul>
<li><b>Votre première campagne à tarif pionnier.</b> Les conditions vous sont envoyées après notre échange.</li>
<li><b>Un accompagnement par le fondateur :</b> installation du module ou de l’extension, choix du produit, suivi des testeurs.</li>
<li><b>Vos premiers avis vérifiés</b>, publiés sur vos fiches avec la mention « Produit offert pour test ».</li>
</ul></div>
<div class="pi-col"><h3>Ce que nous vous demandons</h3><ul>
<li><b>Un retour honnête</b> à la fin de la campagne : ce qui a marché, ce qui vous a gêné (un appel de 15 minutes ou un court questionnaire).</li>
<li><b>Votre accord pour une étude de cas</b> sur avitime.fr, avec vos vrais chiffres. Vous la relisez et la validez avant publication, ou vous refusez.</li>
</ul></div>
</div>
<div class="gd-key pi-never"><p><b>Ce que nous ne vous demanderons jamais :</b> un avis sur Avitime, positif ou non, sur Trustpilot, Google, l’App Store Shopify ou WordPress.org. Le tarif pionnier n’en dépend pas. Plus tard, nous vous proposerons de donner votre avis, comme à tous nos clients, avec le même message neutre : libre à vous de le faire ou non, et de dire ce que vous pensez.</p></div>
<p>Pourquoi tant de précautions ? Parce qu’un avis obtenu contre une remise n’est plus un avis libre, et que les plateformes d’avis l’interdisent. C’est la règle que nous appliquons à nos testeurs : la contrepartie est toujours affichée, et elle ne dépend jamais de la note. Nous l’appliquons aussi à nous-mêmes.</p>

<h2>Qui peut candidater</h2>
<ul>
<li>Une boutique <b>PrestaShop ou WooCommerce</b> (l’application Shopify est en cours de validation : vous pouvez candidater dès maintenant).</li>
<li>Qui <b>livre en France</b>, puisque les testeurs Avitime y résident.</li>
<li>Avec un <b>produit physique ou numérique</b> que vous êtes prêt à offrir à quelques testeurs.</li>
<li>Portée par une <b>entreprise immatriculée</b> (SIRET, ou numéro de TVA pour la Belgique et l’UE).</li>
</ul>

<h2>Comment ça se passe</h2>
<ol class="pi-steps">
<li><b>Vous candidatez</b>Deux minutes par le formulaire de contact : votre boutique et le produit que vous aimeriez faire tester.</li>
<li><b>On échange 15 minutes</b>Je vous explique le fonctionnement et le tarif pionnier. Vous décidez ensuite, sans engagement.</li>
<li><b>On lance votre campagne</b>Installation du module, choix du produit, sélection des testeurs par Avitime.</li>
<li><b>Vous recevez vos avis</b>Les testeurs publient leurs avis sur vos fiches. Puis on prépare ensemble votre étude de cas.</li>
</ol>

<h2>Les études de cas</h2>
<div class="pi-empty"><p>Avitime démarre : les premières études de cas des boutiques pionnières seront publiées ici. Elles montreront de vrais chiffres (nombre d’avis, délai, notes obtenues), y compris quand tout ne s’est pas passé comme prévu.</p></div>

<div class="gd-cta"><p><b>Envie d’en faire partie ?</b> Dix places, attribuées dans l’ordre des candidatures retenues.</p><a class="btn" href="{APPLY}">Candidater au programme</a></div>
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
            {"@type": "ListItem", "position": 2, "name": "Programme pionniers", "item": "https://avitime.fr" + PATH}]}]}
    h = HEAD.format(title=TITLE, desc=DESC, path=PATH, ogtype="website", guides_current="")
    h = h.replace("</style>\n</head>", "</style>\n" + CSS, 1)
    out = h + BODY + FOOT.replace("{ld}", json.dumps(ld, ensure_ascii=False))
    dst = os.path.join(ROOT, "pionniers.html")
    open(dst, "w", encoding="utf-8").write(out)
    print(dst)


if __name__ == "__main__":
    main()
