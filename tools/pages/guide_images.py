#!/usr/bin/env python3
"""
Images des guides (public/guides/*.html) : image d'en-tête sous le titre + images dans le texte.

- Images générées (API OpenAI, compte d'Avitime), style d'illustration unique aux couleurs du site, sans texte ni logo,
  jamais de faux avis ni de faux témoignages. Sources PNG : tools/images-src/<slug>-cover.png, <slug>-1.png, <slug>-2.png…
- Ce script convertit en WebP (1200 et 760 px de large) + JPEG 1200x800 pour les réseaux (og:image), dans
  public/assets/img/guides/, puis injecte les <figure> entre marqueurs <!--gd-img:…--> (idempotent).
- Remplace aussi l'image de partage (og:image, twitter) et l'image de l'Article (données structurées) par l'en-tête du guide.
- Réglages : tools/pages/guide_images.json ({slug: {cover: {alt}, inline: [{before: id du h2, alt, caption}]}}).
Lancer : python3 tools/pages/guide_images.py
"""
import json
import re
import subprocess
from html import escape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PUB = ROOT / "public"
SRC = ROOT / "tools" / "images-src"
OUT = PUB / "assets" / "img" / "guides"
CFG = json.loads((Path(__file__).with_name("guide_images.json")).read_text(encoding="utf-8"))

CSS = """<!--gd-img:css--><style id="gd-img-css">
.gd-cover{margin:30px 0 0}
.gd-cover img,.gd-fig img{display:block;width:100%;height:auto;border-radius:20px;background:var(--bg-2,#F3F2EE)}
.gd-fig{margin:34px 0 8px}
.gd-fig figcaption{font-size:14px;color:var(--ink-2);margin-top:10px;line-height:1.45}
.gd-card .gd-thumb{display:block;width:calc(100% + 48px);max-width:none;height:auto;aspect-ratio:3/2;object-fit:cover;margin:-24px -24px 18px;border-radius:21px 21px 0 0;background:var(--bg-2,#F3F2EE)}
</style><!--/gd-img:css-->"""


def convert(src: Path, stem: str):
    """PNG source → WebP/JPEG. Sans la source (PNG gardés hors dépôt), les fichiers déjà publiés sont réutilisés."""
    if not src.exists():
        return (OUT / f"{stem}.webp").exists()
    OUT.mkdir(parents=True, exist_ok=True)
    jobs = [(f"{stem}.webp", "scale=1200:-2", ["-c:v", "libwebp", "-quality", "80"]),
            (f"{stem}-760.webp", "scale=760:-2", ["-c:v", "libwebp", "-quality", "78"])]
    if stem.endswith("-cover"):
        jobs.append((f"{stem}.jpg", "scale=1200:800:force_original_aspect_ratio=increase,crop=1200:800", ["-q:v", "4"]))
    for name, vf, codec in jobs:
        dst = OUT / name
        if dst.exists() and dst.stat().st_mtime >= src.stat().st_mtime:
            continue
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(src), "-vf", vf, *codec, str(dst)], check=True)
    return True


def picture(stem: str, alt: str, eager: bool) -> str:
    base = f"/assets/img/guides/{stem}"
    load = 'fetchpriority="high"' if eager else 'loading="lazy" decoding="async"'
    return (f'<img src="{base}.webp" srcset="{base}-760.webp 760w, {base}.webp 1200w" sizes="(max-width: 800px) 100vw, 760px" '
            f'width="1200" height="800" alt="{escape(alt)}" {load}>')


def strip(s: str, tag: str) -> str:
    return re.sub(rf"<!--gd-img:{tag}-->.*?<!--/gd-img:{tag}-->", "", s, flags=re.S)


def apply(slug: str, conf: dict):
    page = PUB / "guides" / f"{slug}.html"
    s = page.read_text(encoding="utf-8")
    for tag in ("css", "cover", r"inline-\d+"):
        s = strip(s, tag)
    s = s.replace("</head>", CSS + "</head>", 1)
    cover = SRC / f"{slug}-cover.png"
    has_cover = bool(conf.get("cover")) and convert(cover, f"{slug}-cover")
    if has_cover:
        fig = f'<!--gd-img:cover--><figure class="gd-cover">{picture(f"{slug}-cover", conf["cover"]["alt"], True)}</figure><!--/gd-img:cover-->'
        hero = s.index('class="gd-hero"')
        end = s.index("</div></section>", hero)
        s = s[:end] + fig + s[end:]
        url = f"https://avitime.fr/assets/img/guides/{slug}-cover.jpg"
        s = re.sub(r'<meta property="og:image" content="[^"]*">', f'<meta property="og:image" content="{url}">', s, count=1)
        if 'property="og:image:width"' not in s:
            s = s.replace(f'<meta property="og:image" content="{url}">', f'<meta property="og:image" content="{url}">\n<meta property="og:image:width" content="1200">\n<meta property="og:image:height" content="800">', 1)
        s = re.sub(r'("@type": "Article".*?"image": )"[^"]*"', lambda m: m.group(1) + f'"{url}"', s, count=1, flags=re.S)
    for n, it in enumerate(conf.get("inline", []), 1):
        if not convert(SRC / f"{slug}-{n}.png", f"{slug}-{n}"):
            continue
        cap = f'<figcaption>{escape(it["caption"])}</figcaption>' if it.get("caption") else ""
        fig = f'<!--gd-img:inline-{n}--><figure class="gd-fig">{picture(f"{slug}-{n}", it["alt"], False)}{cap}</figure><!--/gd-img:inline-{n}-->'
        m = re.search(rf'<h2 id="{re.escape(it["before"])}"', s)
        if not m:
            raise SystemExit(f"{slug} : titre #{it['before']} introuvable")
        s = s[:m.start()] + fig + s[m.start():]
    page.write_text(s, encoding="utf-8")
    print(f"{slug} : en-tête {'oui' if has_cover else 'non'}, {len(conf.get('inline', []))} image(s) dans le texte")


# Cartes de la liste des guides qui mènent vers une page du site (pas un guide) : href → nom de l'image
EXTRA_CARDS = {"/devenir-testeur": "devenir-testeur"}


def thumbs(page: Path):
    """Vignette (en-tête du guide) en haut de chaque carte de guide : liste des guides et « À lire aussi »."""
    s = page.read_text(encoding="utf-8")
    s = re.sub(r'<img class="gd-thumb"[^>]*>', "", s)
    if "gd-img-css" not in s:
        s = s.replace("</head>", CSS + "</head>", 1)

    def add(m):
        slug = m.group(1) or EXTRA_CARDS.get(m.group(2), "")
        if not (OUT / f"{slug}-cover-760.webp").exists():
            return m.group(0)
        return (m.group(0) + f'<img class="gd-thumb" src="/assets/img/guides/{slug}-cover-760.webp" width="760" height="507" '
                f'alt="" loading="lazy" decoding="async">')
    extra = "|".join(re.escape(h) for h in EXTRA_CARDS)
    s = re.sub(rf'<a class="gd-card" href="(?:/guides/([\w-]+)\.html|({extra}))">', add, s)
    page.write_text(s, encoding="utf-8")


if __name__ == "__main__":
    for slug, conf in CFG.items():
        apply(slug, conf)
    for name in EXTRA_CARDS.values():
        convert(SRC / f"{name}-cover.png", f"{name}-cover")
    for page in sorted((PUB / "guides").glob("*.html")):
        thumbs(page)
