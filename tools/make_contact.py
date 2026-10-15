"""Page Contact : /contact (FR) et /en/contact (EN). Générée par ce script ; ne pas éditer les HTML à la main.

Le formulaire est envoyé à la plateforme (app.avitime.fr/api/contact), qui renvoie vers la page avec ?envoye=1 / ?sent=1.
Pour un test local : CONTACT_ACTION=http://localhost:3999/api/contact python3 tools/make_contact.py
"""
import json, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from make_guides import HEAD
from site_footer import footer, ICON_IG, ICON_TT, ICON_MAIL, IG, TT

ROOT = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "public")
ACTION = os.environ.get("CONTACT_ACTION", "https://app.avitime.fr/api/contact")

CSS = """<style>
.ct-hero{padding-block:clamp(56px,8vw,96px) 8px}
.ct-wrap{max-width:1080px;margin-inline:auto;padding-inline:22px}
.ct-hero h1{font-size:clamp(36px,5.4vw,60px);letter-spacing:-.045em;line-height:1.03;margin:14px 0 0;text-wrap:balance;max-width:16ch}
.ct-lede{font-size:clamp(18px,2vw,21px);color:var(--ink-2);line-height:1.5;margin:20px 0 0;max-width:56ch}
.ct-facts{display:flex;flex-wrap:wrap;gap:10px;margin:26px 0 0;padding:0;list-style:none}
.ct-facts li{display:inline-flex;align-items:center;gap:8px;background:var(--surface);border:1px solid var(--line);border-radius:999px;padding:7px 14px;font-size:14.5px;font-weight:500}
.ct-facts li::before{content:"";width:8px;height:8px;border-radius:50%;background:var(--hl);flex:none}
.ct-grid{display:grid;grid-template-columns:minmax(0,1.35fr) minmax(0,1fr);gap:28px;padding-block:40px 88px;align-items:start}
@media (max-width:900px){.ct-grid{grid-template-columns:minmax(0,1fr)}}
.ct-card{background:var(--surface);border:1px solid var(--line);border-radius:26px;padding:clamp(22px,3.4vw,36px)}
.ct-card h2{font-size:clamp(24px,2.6vw,30px);letter-spacing:-.035em;margin:0 0 6px;line-height:1.1}
.ct-sub{margin:0 0 22px;color:var(--ink-2);font-size:15.5px;line-height:1.5}
.ct-form{display:grid;gap:18px}
.ct-row{display:grid;grid-template-columns:1fr 1fr;gap:18px}
@media (max-width:600px){.ct-row{grid-template-columns:1fr}}
.ct-field{display:grid;gap:7px}
.ct-field label,.ct-legend{font-size:14.5px;font-weight:600}
.ct-field .opt{font-weight:400;color:var(--ink-2)}
.ct-field input,.ct-field textarea{font:inherit;font-size:16px;color:var(--ink);background:var(--bg);border:1.5px solid var(--line);border-radius:14px;padding:13px 15px;width:100%;transition:border-color .15s ease,box-shadow .15s ease}
.ct-field textarea{min-height:170px;resize:vertical;line-height:1.55}
.ct-field input:focus,.ct-field textarea:focus{outline:none;border-color:var(--hl);box-shadow:0 0 0 4px color-mix(in srgb,var(--hl) 22%,transparent)}
.ct-field .hint{font-size:13px;color:var(--ink-2)}
.ct-who{border:0;margin:0;padding:0;display:grid;gap:9px}
.ct-chips{display:flex;flex-wrap:wrap;gap:8px}
.ct-chips label{position:relative;cursor:pointer}
.ct-chips input{position:absolute;opacity:0;inset:0;margin:0;cursor:pointer}
.ct-chips span{display:inline-flex;align-items:center;gap:8px;border:1.5px solid var(--line);border-radius:999px;padding:10px 16px;font-size:15px;font-weight:600;background:var(--bg);transition:border-color .15s ease,background-color .15s ease}
.ct-chips input:checked+span{background:var(--hl);border-color:var(--hl);color:#0A0A0A}
.ct-chips input:focus-visible+span{outline:3px solid var(--hl);outline-offset:2px}
.ct-hp{position:absolute!important;left:-9999px!important;width:1px;height:1px;overflow:hidden}
.ct-send{display:flex;flex-wrap:wrap;align-items:center;gap:14px 20px;margin-top:4px}
.ct-send .btn{background:var(--hl);color:#0A0A0A;font-weight:600}
.ct-send p{margin:0;font-size:13.5px;color:var(--ink-2);flex:1 1 240px;line-height:1.45}
.ct-send a,.ct-aside a.inline{color:var(--hl-ink)}
.ct-alert{display:none;border-radius:14px;padding:13px 16px;font-size:15px;line-height:1.45;background:var(--bad-bg);color:var(--bad);margin:0 0 18px}
.ct-alert.on{display:block}
.ct-sent{display:none;text-align:left}
#formulaire,#envoye,#sent{scroll-margin-top:calc(var(--nav-h) + 24px)}
.ct-sent:target,.ct-sent.on{display:block}
.ct-sent .tick{width:56px;height:56px;border-radius:50%;background:var(--hl);display:grid;place-items:center;margin-bottom:16px}
.ct-sent .tick svg{width:28px;height:28px}
.ct-sent p{color:var(--ink-2);font-size:16px;line-height:1.55}
.ct-aside{display:grid;gap:18px}
.ct-box{background:var(--surface);border:1px solid var(--line);border-radius:22px;padding:22px}
.ct-box h2{font-size:19px;letter-spacing:-.02em;margin:0 0 4px}
.ct-box > p{margin:0 0 14px;color:var(--ink-2);font-size:15px;line-height:1.5}
.ct-links{list-style:none;margin:0;padding:0;display:grid;gap:2px}
.ct-links a{display:flex;justify-content:space-between;align-items:center;gap:12px;padding:10px 12px;margin-inline:-12px;border-radius:12px;color:var(--ink);text-decoration:none;font-weight:600;font-size:15.5px}
.ct-links a::after{content:"→";color:var(--hl-ink);font-weight:500}
.ct-links a:hover{background:var(--bg-2)}
.ct-mail{display:inline-flex;align-items:center;gap:10px;font-size:17px;font-weight:700;color:var(--ink);text-decoration:none}
.ct-mail svg{width:22px;height:22px;color:var(--hl-ink)}
.ct-soc{display:flex;flex-wrap:wrap;gap:10px;margin-top:14px;padding:0;list-style:none}
.ct-soc a{display:inline-flex;align-items:center;gap:9px;background:var(--accent);color:var(--accent-ink);border-radius:999px;padding:8px 16px 8px 9px;font-weight:600;font-size:15px;text-decoration:none}
.ct-soc svg{width:26px;height:26px;padding:4px;border-radius:50%;background:var(--hl);color:#0A0A0A}
.ct-org{font-size:14px!important;line-height:1.55!important}
</style>
</head>"""

TICK = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12.5l4.2 4.2L19 7" fill="none" stroke="#0A0A0A" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/></svg>'

TXT = {
    "fr": dict(
        path="/contact", title="Contact : écrire à l’équipe Avitime",
        desc="Une question sur Avitime, les tests produits ou votre mission de testeur ? Écrivez-nous via le formulaire ou à contact@avitime.fr : réponse sous 48 h ouvrées.",
        eyebrow="Contact", h1="Une question ? Écrivez-nous.",
        lede="Boutique en ligne, testeur ou simple curieux : envoyez-nous votre message, un membre de l’équipe Avitime vous répond personnellement.",
        facts=["Réponse sous 48 h ouvrées", "En français ou en anglais", "Une vraie personne vous répond"],
        form_h="Envoyer un message", form_sub="Tous les champs sont obligatoires, sauf mention contraire.",
        who="Vous êtes", who_opts=[("boutique", "Une boutique"), ("testeur", "Un testeur"), ("autre", "Autre")],
        nom="Prénom et nom", email="Adresse e-mail", shop="Site de votre boutique", opt="(facultatif)",
        shop_ph="https://www.ma-boutique.fr", sujet="Sujet", sujet_ph="Ex. : faire tester un produit",
        msg="Votre message", msg_hint="10 caractères au minimum.",
        send="Envoyer mon message",
        privacy='Vos informations servent uniquement à vous répondre. <a href="/confidentialite.html">Confidentialité</a>',
        errors={"invalide": "Il manque une information ou l’adresse e-mail n’est pas valide. Vérifiez le formulaire et réessayez.",
                "limite": "Vous avez envoyé plusieurs messages en peu de temps. Réessayez dans une heure, ou écrivez-nous directement à contact@avitime.fr.",
                "serveur": "Votre message n’a pas pu être envoyé à cause d’un problème technique. Réessayez, ou écrivez-nous à contact@avitime.fr."},
        sent_id="envoye", sent_q="envoye", sent_h="Merci, votre message est bien parti !",
        sent_p="Nous l’avons reçu et nous vous répondons sous 48 h ouvrées, à l’adresse e-mail que vous avez indiquée. Pensez à regarder vos courriers indésirables.",
        sent_again="Envoyer un autre message",
        quick_h="Une réponse tout de suite ?",
        quick_p="Les questions les plus fréquentes ont déjà leur réponse :",
        quick=[("/devenir-testeur#faq", "Testeurs : les 13 questions fréquentes"), ("/devenir-testeur", "Devenir testeur, étape par étape"),
               ("/#commercants", "Boutiques : comment fonctionne Avitime"), ("/guides/", "Nos guides sur les avis clients")],
        direct_h="Nous écrire directement", direct_p="Vous préférez votre messagerie ? Écrivez-nous à :",
        follow_h="Suivez-nous", follow_p="Les coulisses d’Avitime et les nouveaux produits à tester :",
        org_h="Qui vous répond ?",
        org_p='Avitime est édité par <b>SPARKMOTION AGENCY LTD</b>, société enregistrée en Angleterre et au pays de Galles (n° 16880032), et fondé par Cyril Quémy. <a class="inline" href="/a-propos.html">En savoir plus sur Avitime</a> · <a class="inline" href="/mentions-legales.html">Mentions légales</a>',
        ig_aria="Avitime sur Instagram (@avitime_fr)", tt_aria="Avitime sur TikTok (@avitime_fr)",
        ld_name="Contact Avitime",
    ),
    "en": dict(
        path="/en/contact", title="Contact: write to the Avitime team",
        desc="A question about Avitime, product testing or your tester mission? Write to us through the form or at contact@avitime.fr: we reply within 2 business days.",
        eyebrow="Contact", h1="A question? Write to us.",
        lede="Online store, tester or just curious: send us your message and a member of the Avitime team will reply personally.",
        facts=["Reply within 2 business days", "In English or French", "A real person replies"],
        form_h="Send a message", form_sub="All fields are required unless marked optional.",
        who="You are", who_opts=[("boutique", "A store"), ("testeur", "A tester"), ("autre", "Other")],
        nom="First and last name", email="Email address", shop="Your store’s website", opt="(optional)",
        shop_ph="https://www.my-store.com", sujet="Subject", sujet_ph="E.g. having a product tested",
        msg="Your message", msg_hint="At least 10 characters.",
        send="Send my message",
        privacy='Your details are only used to reply to you. <a href="/en/privacy.html">Privacy</a>',
        errors={"invalide": "Some information is missing or the email address is not valid. Please check the form and try again.",
                "limite": "You sent several messages in a short time. Please try again in an hour, or email us at contact@avitime.fr.",
                "serveur": "Your message could not be sent because of a technical problem. Please try again, or email us at contact@avitime.fr."},
        sent_id="sent", sent_q="sent", sent_h="Thank you, your message is on its way!",
        sent_p="We have received it and will reply within 2 business days to the email address you entered. Please check your spam folder too.",
        sent_again="Send another message",
        quick_h="Need an answer right now?",
        quick_p="The most common questions are already answered:",
        quick=[("/en/#faq", "Frequently asked questions"), ("/en/become-tester", "Become a tester"),
               ("/en/#commercants", "Stores: how Avitime works"), ("/guides/", "Our guides on customer reviews (FR)")],
        direct_h="Email us directly", direct_p="Prefer your own inbox? Write to:",
        follow_h="Follow us", follow_p="Behind the scenes at Avitime and new products to test:",
        org_h="Who replies?",
        org_p='Avitime is published by <b>SPARKMOTION AGENCY LTD</b>, a company registered in England and Wales (no. 16880032), and was founded by Cyril Quémy. <a class="inline" href="/a-propos.html" hreflang="fr">About Avitime (FR)</a> · <a class="inline" href="/mentions-legales.html" hreflang="fr">Legal notice (FR)</a>',
        ig_aria="Avitime on Instagram (@avitime_fr)", tt_aria="Avitime on TikTok (@avitime_fr)",
        ld_name="Contact Avitime",
    ),
}

JS = """<script>
(function(){
  var f=document.getElementById('ct-form'); if(!f) return;
  var t=f.querySelector('input[name=t]'); if(t) t.value=String(Date.now());
  var q=new URLSearchParams(location.search), sent=document.getElementById('%(sent_id)s');
  if(q.get('%(sent_q)s')==='1'&&sent){sent.classList.add('on');f.hidden=true;var a=document.getElementById('ct-alert');if(a)a.hidden=true;}
  var err=q.get('erreur'), msgs=%(errors)s, box=document.getElementById('ct-alert');
  if(err&&msgs[err]&&box){box.textContent=msgs[err];box.classList.add('on');}
  var shop=document.getElementById('ct-shop');
  function sync(){var v=(f.querySelector('input[name=profil]:checked')||{}).value; if(shop) shop.hidden=(v!=='boutique');}
  f.addEventListener('change',function(e){if(e.target.name==='profil')sync();}); sync();
  f.addEventListener('submit',function(){var b=f.querySelector('button[type=submit]'); if(b){b.disabled=true;b.textContent='%(sending)s';}});
})();
</script>"""


def head(lang, t):
    h = HEAD.format(title=t["title"], desc=t["desc"], path=t["path"], ogtype="website", guides_current="")
    h = h.replace("</style>\n</head>", "</style>\n" + CSS, 1)
    if lang == "en":
        h = h.replace('<html lang="fr">', '<html lang="en">').replace('content="fr_FR"', 'content="en_GB"')
        a = h.index('<header class="nav"'); b = h.index("</header>", a) + len("</header>")
        h = h[:a] + """<header class="nav" id="top-nav">
<div class="wrap">
<a class="brand" href="/en/"><img alt="Avitime, home" height="40" src="/assets/img/avitime-logo-96.png" width="168"/></a>
<nav aria-label="Main navigation" class="nav-links">
<a href="/en/#concept">How it works</a>
<a href="/en/#commercants">Merchants</a>
<a href="/en/become-tester">Testers</a>
<a href="/en/#faq">FAQ</a>
<a href="/a-propos.html" hreflang="fr">About (FR)</a>
</nav>
<div class="nav-actions">
<a class="lang" href="/contact" hreflang="fr" lang="fr" aria-label="Version française">FR</a>
<a class="ghost" href="/en/merchant">Merchant account</a>
<a class="btn-sm" href="/en/become-tester">Become a tester</a>
</div>
</div>
</header>""" + h[b:]
        h = h.replace('<main id="contenu">', '<main id="content">')
    alt = ('<link rel="alternate" hreflang="fr" href="https://avitime.fr/contact">\n'
           '<link rel="alternate" hreflang="en" href="https://avitime.fr/en/contact">\n'
           '<link rel="alternate" hreflang="x-default" href="https://avitime.fr/contact">\n')
    return h.replace('<meta property="og:type"', alt + '<meta property="og:type"', 1)


def page(lang):
    t = TXT[lang]
    chips = "".join(
        f'<label><input type="radio" name="profil" value="{v}"{" required" if i == 0 else ""}><span>{l}</span></label>'
        for i, (v, l) in enumerate(t["who_opts"]))
    quick = "".join(f'<li><a href="{h}">{l}</a></li>' for h, l in t["quick"])
    facts = "".join(f"<li>{x}</li>" for x in t["facts"])
    ld = {"@context": "https://schema.org", "@type": "ContactPage", "name": t["ld_name"], "url": "https://avitime.fr" + t["path"],
          "inLanguage": "fr-FR" if lang == "fr" else "en",
          "mainEntity": {"@type": "Organization", "name": "Avitime", "url": "https://avitime.fr/",
                         "legalName": "SPARKMOTION AGENCY LTD", "email": "contact@avitime.fr", "sameAs": [IG, TT],
                         "contactPoint": {"@type": "ContactPoint", "contactType": "customer support", "email": "contact@avitime.fr",
                                          "availableLanguage": ["French", "English"]}}}
    body = f"""<section class="ct-hero"><div class="ct-wrap">
<p class="eyebrow">{t['eyebrow']}</p>
<h1>{t['h1']}</h1>
<p class="ct-lede">{t['lede']}</p>
<ul class="ct-facts">{facts}</ul>
</div></section>
<div class="ct-wrap ct-grid">
<section class="ct-card" id="formulaire" aria-labelledby="ct-form-h">
<div class="ct-sent" id="{t['sent_id']}" role="status">
<div class="tick">{TICK}</div>
<h2>{t['sent_h']}</h2>
<p>{t['sent_p']}</p>
<p><a class="link" href="{t['path']}#formulaire">{t['sent_again']}</a></p>
</div>
<form class="ct-form" id="ct-form" method="post" action="{ACTION}" accept-charset="utf-8">
<div>
<h2 id="ct-form-h">{t['form_h']}</h2>
<p class="ct-sub">{t['form_sub']}</p>
<p class="ct-alert" id="ct-alert" role="alert"></p>
</div>
<input type="hidden" name="lang" value="{lang}">
<input type="hidden" name="t" value="">
<div class="ct-hp" aria-hidden="true"><label>Website <input type="text" name="website" tabindex="-1" autocomplete="off"></label></div>
<fieldset class="ct-who"><legend class="ct-legend">{t['who']}</legend><div class="ct-chips">{chips}</div></fieldset>
<div class="ct-row">
<div class="ct-field"><label for="ct-nom">{t['nom']}</label><input id="ct-nom" name="nom" type="text" autocomplete="name" required minlength="2" maxlength="120"></div>
<div class="ct-field"><label for="ct-email">{t['email']}</label><input id="ct-email" name="email" type="email" autocomplete="email" required maxlength="254"></div>
</div>
<div class="ct-field" id="ct-shop"><label for="ct-boutique">{t['shop']} <span class="opt">{t['opt']}</span></label><input id="ct-boutique" name="boutique" type="text" inputmode="url" autocomplete="url" maxlength="200" placeholder="{t['shop_ph']}"></div>
<div class="ct-field"><label for="ct-sujet">{t['sujet']}</label><input id="ct-sujet" name="sujet" type="text" required minlength="2" maxlength="150" placeholder="{t['sujet_ph']}"></div>
<div class="ct-field"><label for="ct-msg">{t['msg']}</label><textarea id="ct-msg" name="message" required minlength="10" maxlength="5000" aria-describedby="ct-msg-hint"></textarea><span class="hint" id="ct-msg-hint">{t['msg_hint']}</span></div>
<div class="ct-send"><button class="btn" type="submit">{t['send']}</button><p>{t['privacy']}</p></div>
</form>
</section>
<aside class="ct-aside">
<section class="ct-box"><h2>{t['quick_h']}</h2><p>{t['quick_p']}</p><ul class="ct-links">{quick}</ul></section>
<section class="ct-box"><h2>{t['direct_h']}</h2><p>{t['direct_p']}</p><a class="ct-mail" href="mailto:contact@avitime.fr">{ICON_MAIL}<span>contact@avitime.fr</span></a></section>
<section class="ct-box"><h2>{t['follow_h']}</h2><p>{t['follow_p']}</p>
<ul class="ct-soc"><li><a href="{IG}" rel="me noopener" target="_blank" aria-label="{t['ig_aria']}">{ICON_IG}<span>Instagram</span></a></li><li><a href="{TT}" rel="me noopener" target="_blank" aria-label="{t['tt_aria']}">{ICON_TT}<span>TikTok</span></a></li></ul></section>
<section class="ct-box"><h2>{t['org_h']}</h2><p class="ct-org">{t['org_p']}</p></section>
</aside>
</div>
</main>
"""
    js = JS % {"sent_id": t["sent_id"], "sent_q": t["sent_q"], "errors": json.dumps(t["errors"], ensure_ascii=False),
               "sending": "Envoi…" if lang == "fr" else "Sending…"}
    out = (head(lang, t) + body + footer(lang) + "\n"
           + f'<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>\n' + js
           + '\n<script src="/assets/js/main.js?v=19d91e0a16" defer></script>\n</body>\n</html>\n')
    dst = os.path.join(ROOT, "contact.html" if lang == "fr" else "en/contact.html")
    open(dst, "w", encoding="utf-8").write(out)
    return dst


if __name__ == "__main__":
    for l in ("fr", "en"):
        print(page(l))
    print("action :", ACTION)
