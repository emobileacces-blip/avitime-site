#!/usr/bin/env python3
"""
Boutons de partage + « Suivre Avitime sur LinkedIn » sur tous les guides (public/guides/*.html, sauf l'index).

- Sous l'auteur (haut) : WhatsApp, LinkedIn, Facebook, X, Copier le lien ; sur téléphone, un bouton « Partager »
  ouvre le menu du téléphone (navigator.share).
- En bas, avant « À lire aussi » : « Cet article vous a aidé ? Partagez-le » + « Suivre Avitime sur LinkedIn ».
- Simples liens, aucun script d'un autre site (pas de cookie, pas de pisteur, page aussi rapide).
- Idempotent : les blocs entre marqueurs <!--gd-share:…--> sont remplacés à chaque passage.
  Appelé à la fin de build_guide.py ; se lance aussi seul : python3 tools/pages/guide_share.py
"""
import html
import re
from pathlib import Path
from urllib.parse import quote

PUB = Path(__file__).resolve().parents[2] / "public"
LINKEDIN_PAGE = "https://www.linkedin.com/company/avitime/"

CSS = """<!--gd-share:css--><style id="gd-share-css">
.gd-share{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin:18px 0 0}
.gd-share-l{font-size:14px;color:var(--muted,#5E5E58);margin-right:2px}
.gd-share a,.gd-share button{display:inline-flex;align-items:center;gap:6px;min-height:36px;padding:0 13px;border-radius:999px;border:1px solid var(--line,#E5E5E0);background:#fff;color:inherit;font:inherit;font-size:14px;font-weight:600;text-decoration:none;cursor:pointer}
.gd-share a:hover,.gd-share button:hover{border-color:currentColor}
.gd-share svg{width:16px;height:16px;flex:none}
.gd-share .gd-native{display:none}
.gd-share-box{margin:34px 0 0;padding:20px 22px;border-radius:16px;background:var(--bg-2,#F3F2EE)}
.gd-share-box h2{font-size:19px;margin:0}
.gd-share-box p{margin:6px 0 0}
.gd-share-box .gd-share{margin-top:12px}
.gd-follow{margin-top:14px;font-size:15px}
@media (max-width:640px){.gd-share .gd-net{display:none}.gd-share .gd-native{display:inline-flex}}
</style><!--/gd-share:css-->"""

ICON = {
    "whatsapp": '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2Zm0 18.2a8.2 8.2 0 0 1-4.2-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2Zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.2-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.3.8 3.2.6a2.7 2.7 0 0 0 1.8-1.2 2.2 2.2 0 0 0 .1-1.2c-.1-.1-.2-.2-.5-.3Z"/></svg>',
    "linkedin": '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5ZM3 9.75h4V21H3V9.75Zm6.5 0h3.8v1.6h.06a4.2 4.2 0 0 1 3.76-2.06c4 0 4.78 2.64 4.78 6.07V21h-4v-5c0-1.2 0-2.74-1.67-2.74s-1.93 1.3-1.93 2.65V21h-4V9.75Z"/></svg>',
    "facebook": '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M14 8.5V6.8c0-.8.5-1 .9-1H17V2.1L14 2c-3.3 0-4 2.4-4 4v2.5H8V12h2v10h4V12h2.7l.4-3.5H14Z"/></svg>',
    "x": '<svg viewBox="0 0 24 24" aria-hidden="true" fill="currentColor"><path d="M17.8 3H21l-7 8 8.2 10h-6.4l-5-6.1L5 21H1.8l7.5-8.6L1.5 3H8l4.5 5.6L17.8 3Zm-1.1 16.2h1.8L7.4 4.7H5.5l11.2 14.5Z"/></svg>',
    "link": '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M10 13a5 5 0 0 0 7.5.5l3-3a5 5 0 0 0-7-7l-1.7 1.7"/><path d="M14 11a5 5 0 0 0-7.5-.5l-3 3a5 5 0 0 0 7 7l1.7-1.7"/></svg>',
    "share": '<svg viewBox="0 0 24 24" aria-hidden="true" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v12"/><path d="m7 8 5-5 5 5"/><path d="M5 13v6a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-6"/></svg>',
}

# Copier le lien + menu de partage du téléphone (un seul script par page, en bas).
JS = """<script>(function(){document.querySelectorAll('.gd-share').forEach(function(b){var u=b.dataset.url,t=b.dataset.title;
var c=b.querySelector('.gd-copy');if(c)c.addEventListener('click',function(){var d=function(){c.lastChild.textContent=' Lien copié';setTimeout(function(){c.lastChild.textContent=' Copier le lien'},2000)};
if(navigator.clipboard)navigator.clipboard.writeText(u).then(d,function(){prompt('Copiez ce lien :',u)});else prompt('Copiez ce lien :',u)});
var n=b.querySelector('.gd-native');if(n){if(!navigator.share){n.remove();b.querySelectorAll('.gd-net').forEach(function(e){e.style.display='inline-flex'})}
else n.addEventListener('click',function(){navigator.share({title:t,url:u}).catch(function(){})})}})})();</script>"""


def bar(url: str, title: str, where: str) -> str:
    u, t = quote(url, safe=""), quote(title, safe="")
    wa = quote(f"{title} {url}", safe="")
    a = lambda net, href, label: (f'<a class="gd-net" href="{href}" target="_blank" rel="noopener nofollow" '
                                  f'aria-label="Partager sur {label}" data-net="{net}">{ICON[net]}<span>{label}</span></a>')
    return (f'<div class="gd-share" data-url="{html.escape(url)}" data-title="{html.escape(title)}" data-where="{where}">'
            + ('<span class="gd-share-l">Partager :</span>' if where == "top" else "")
            + f'<button type="button" class="gd-native">{ICON["share"]}<span> Partager</span></button>'
            + a("whatsapp", f"https://wa.me/?text={wa}", "WhatsApp")
            + a("linkedin", f"https://www.linkedin.com/sharing/share-offsite/?url={u}", "LinkedIn")
            + a("facebook", f"https://www.facebook.com/sharer/sharer.php?u={u}", "Facebook")
            + a("x", f"https://x.com/intent/tweet?text={t}&amp;url={u}", "X")
            + f'<button type="button" class="gd-copy gd-net">{ICON["link"]}<span> Copier le lien</span></button>'
            + "</div>")


def strip(s: str) -> str:
    return re.sub(r"<!--gd-share:(\w+)-->.*?<!--/gd-share:\1-->", "", s, flags=re.S)


def apply_one(p: Path) -> bool:
    s0 = p.read_text()
    s = strip(s0)
    m = re.search(r'<link rel="canonical" href="([^"]+)"', s)
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", s, re.S)
    if not m or not h1:
        return False
    url = m.group(1)
    title = html.unescape(re.sub(r"<[^>]+>", "", h1.group(1))).replace("\xa0", " ").strip()
    # Haut : sous le bloc auteur (fin de l'en-tête du guide).
    by = re.search(r'(<div class="gd-by">.*?</p></div>)', s, re.S)
    if not by:
        return False
    s = s[:by.end()] + f"<!--gd-share:top-->{bar(url, title, 'top')}<!--/gd-share:top-->" + s[by.end():]
    # Bas : avant « À lire aussi » (ou, à défaut, à la fin du corps du guide).
    box = ('<!--gd-share:bottom--><div class="gd-share-box"><h2>Cet article vous a aidé&nbsp;?</h2>'
           '<p>Partagez-le avec un commerçant ou un proche que le sujet intéresse.</p>'
           + bar(url, title, "bottom")
           + f'<p class="gd-follow">Pour lire les prochains guides&nbsp;: <a class="link" href="{LINKEDIN_PAGE}" target="_blank" rel="noopener">'
           + f'{ICON["linkedin"].replace("<svg ", "<svg style=\"width:15px;height:15px;vertical-align:-2px\" ")} Suivre Avitime sur LinkedIn</a></p>'
           + JS + "</div><!--/gd-share:bottom-->")
    i = s.find('<aside class="gd-related"')
    if i < 0:
        i = s.find("</div></section>", s.find('<section class="gd-body"'))
    if i < 0:
        return False
    s = s[:i] + box + s[i:]
    s = s.replace("</head>", CSS + "</head>", 1)
    if s != s0:
        p.write_text(s)
    return True


def apply_all():
    done, skipped = 0, []
    for p in sorted((PUB / "guides").glob("*.html")):
        if p.name == "index.html":
            continue
        if apply_one(p):
            done += 1
        else:
            skipped.append(p.name)
    print(f"[guide_share] {done} guides" + (f", ignorés : {', '.join(skipped)}" if skipped else ""))


if __name__ == "__main__":
    apply_all()
