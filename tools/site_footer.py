"""Pied de page commun du site avitime.fr (FR et EN).

Utilisé par make_guides.py, make_en.py et make_contact.py ; `python3 tools/site_footer.py` l'applique
aux pages écrites à la main (toutes sauf /demo/). Ne pas modifier le <footer> d'une page à la main.
"""
import os
import re
import sys

IG = "https://www.instagram.com/avitime_fr/"
TT = "https://www.tiktok.com/@avitime_fr"

ICON_IG = ('<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><rect x="2.5" y="2.5" width="19" height="19" rx="5.5" '
           'fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="4.3" fill="none" stroke="currentColor" '
           'stroke-width="2"/><circle cx="17.6" cy="6.4" r="1.3" fill="currentColor"/></svg>')
ICON_TT = ('<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" d="M12.53.02c1.31-.02 2.61-.01 '
           '3.91-.02.08 1.53.63 3.09 1.75 4.17 1.12 1.11 2.7 1.62 4.24 1.79v4.03c-1.44-.05-2.89-.35-4.2-.97-.57-.26-1.1-.59-1.62-.93'
           '-.01 2.92.01 5.84-.02 8.75-.08 1.4-.54 2.79-1.35 3.94-1.31 1.92-3.58 3.17-5.91 3.21-1.43.08-2.86-.31-4.08-1.03-2.02-1.19'
           '-3.44-3.37-3.65-5.71-.02-.5-.03-1-.01-1.49.18-1.9 1.12-3.72 2.58-4.96 1.66-1.44 3.98-2.13 6.15-1.72.02 1.48-.04 2.96-.04 '
           '4.44-.99-.32-2.15-.23-3.02.37-.63.41-1.11 1.04-1.36 1.75-.21.51-.15 1.07-.14 1.61.24 1.64 1.82 3.02 3.5 2.87 1.12-.01 '
           '2.19-.66 2.77-1.61.19-.33.4-.67.41-1.06.1-1.79.06-3.57.07-5.36.01-4.03-.01-8.05.02-12.07z"/></svg>')
ICON_MAIL = ('<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><rect x="2.5" y="4.5" width="19" height="15" rx="3" fill="none" '
             'stroke="currentColor" stroke-width="2"/><path d="M3.5 6.5l8.5 6.5 8.5-6.5" fill="none" stroke="currentColor" stroke-width="2" '
             'stroke-linejoin="round"/></svg>')

T = {
    "fr": dict(
        home="/", logo_alt="Avitime, accueil",
        pitch="De vrais avis clients, écrits par de vrais testeurs. Chaque avis porte la mention « Produit offert pour test ».",
        compat="Compatible avec", col1="Avitime", col2="Informations légales", col3="Suivez-nous",
        links1=[("/a-propos.html", "À propos", ""), ("/a-propos.html#methode", "Méthode de vérification", ""),
                ("/guides/", "Guides", ""), ("/contact", "Contact", ""), ("/devenir-testeur", "Devenir testeur", ""),
                ("/espace-commercant", "Espace commerçant", "")],
        links2=[("/mentions-legales.html", "Mentions légales", ""), ("/cgv.html", "CGV commerçants", ""),
                ("/cgu-testeurs.html", "CGU testeurs", ""), ("/confidentialite.html", "Confidentialité", "")],
        social_label="Réseaux sociaux", ig_aria="Avitime sur Instagram (@avitime_fr)", tt_aria="Avitime sur TikTok (@avitime_fr)",
        legal="© 2026 Avitime · édité par SPARKMOTION AGENCY LTD",
        other=("/en/", "English version", 'hreflang="en" lang="en"'),
    ),
    "en": dict(
        home="/en/", logo_alt="Avitime, home",
        pitch="Real customer reviews, written by real testers. Every review is labelled “Free product for testing”.",
        compat="Works with", col1="Avitime", col2="Legal", col3="Follow us",
        links1=[("/a-propos.html", "About (FR)", 'hreflang="fr"'), ("/guides/", "Guides (FR)", 'hreflang="fr"'),
                ("/en/contact", "Contact", ""), ("/en/become-tester", "Become a tester", ""),
                ("/en/merchant", "Merchant account", "")],
        links2=[("/en/terms.html", "Merchant terms", ""), ("/en/tester-terms.html", "Tester terms", ""),
                ("/en/privacy.html", "Privacy", ""), ("/mentions-legales.html", "Mentions légales", 'hreflang="fr" lang="fr"')],
        social_label="Social media", ig_aria="Avitime on Instagram (@avitime_fr)", tt_aria="Avitime on TikTok (@avitime_fr)",
        legal="© 2026 Avitime · published by SPARKMOTION AGENCY LTD",
        other=("/", "Version française", 'hreflang="fr" lang="fr"'),
    ),
}


def _links(items):
    out = []
    for href, label, extra in items:
        attrs = f' {extra}' if extra else ""
        out.append(f'<li><a href="{href}"{attrs}>{label}</a></li>')
    return "".join(out)


def footer(lang="fr"):
    t = T[lang]
    o_href, o_label, o_extra = t["other"]
    return f"""<footer class="site-foot">
<div class="wrap">
<div class="foot-grid">
<div class="foot-brand">
<a class="foot-logo" href="{t['home']}"><img src="/assets/img/avitime-logo-96.png" alt="{t['logo_alt']}" width="168" height="40" loading="lazy"></a>
<p>{t['pitch']}</p>
<ul class="foot-compat" aria-label="{t['compat']}"><li>PrestaShop</li><li>WooCommerce</li><li>Shopify</li></ul>
</div>
<nav class="foot-col" aria-label="{t['col1']}"><p class="foot-h">{t['col1']}</p><ul>{_links(t['links1'])}</ul></nav>
<nav class="foot-col" aria-label="{t['col2']}"><p class="foot-h">{t['col2']}</p><ul>{_links(t['links2'])}</ul></nav>
<div class="foot-col"><p class="foot-h">{t['col3']}</p>
<ul class="foot-social" aria-label="{t['social_label']}">
<li><a class="soc" href="{IG}" rel="me noopener" target="_blank" aria-label="{t['ig_aria']}">{ICON_IG}<span>Instagram</span></a></li>
<li><a class="soc" href="{TT}" rel="me noopener" target="_blank" aria-label="{t['tt_aria']}">{ICON_TT}<span>TikTok</span></a></li>
</ul>
<a class="foot-mail" href="mailto:contact@avitime.fr">{ICON_MAIL}<span>contact@avitime.fr</span></a>
</div>
</div>
<div class="foot-bottom"><span>{t['legal']}</span><a href="{o_href}" {o_extra}>{o_label}</a></div>
</div>
</footer>"""


FOOTER_RE = re.compile(r"<footer\b[^>]*>.*?</footer>", re.S)


def replace_footer(html, lang):
    n = len(FOOTER_RE.findall(html))
    if n != 1:
        raise SystemExit(f"{n} <footer> trouvés (1 attendu)")
    return FOOTER_RE.sub(lambda m: footer(lang), html)


if __name__ == "__main__":
    root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "public")
    done = []
    for dp, _, files in os.walk(root):
        if os.sep + "demo" in dp:
            continue
        for f in files:
            if not f.endswith(".html"):
                continue
            p = os.path.join(dp, f)
            s = open(p, encoding="utf-8").read()
            if "<footer" not in s:
                continue
            lang = "en" if re.search(r'<html lang="en"', s) else "fr"
            open(p, "w", encoding="utf-8").write(replace_footer(s, lang))
            done.append(f"{lang} {os.path.relpath(p, root)}")
    print("\n".join(sorted(done)))
    print(len(done), "pages", file=sys.stderr)
