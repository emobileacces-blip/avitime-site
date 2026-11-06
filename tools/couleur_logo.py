#!/usr/bin/env python3
"""Couleur du site vitrine : le dégradé jaune-orangé relevé sur le logo.
Remplace les anciens oranges (feuilles de style, styles dans les pages, générateurs) et change le numéro
de version de style.css, sinon les navigateurs gardent l'ancienne feuille en cache 7 jours.
Relançable sans effet de bord. Ne touche ni au logo, ni aux images, ni aux vidéos, ni aux textes."""
import re
from pathlib import Path

RACINE = Path(__file__).resolve().parent.parent
PUBLIC = RACINE / "public"
DEGRADE = "linear-gradient(180deg,#F8AA15 0%,#F98C07 55%,#F47302 100%)"
VERSION = "logo1"

# Ancienne couleur -> couleur accordée au logo. Les textes foncés restent lisibles sur fond clair.
COULEURS = {"#FF6A13": "#F98C07", "#FF7A2A": "#F98C07", "#B34100": "#964A00", "#FF8A3D": "#FFA63D",
            "#FFEBDD": "#FFF0D2", "#3A1E0C": "#3A2808", "#FF9B5E": "#FFB54D", "#FFB27A": "#FFC98A",
            "#F98F5C": "#FFC04D", "#F4763A": "#F98C07", "#9C3F10": "#964A00"}
MOTIF = re.compile("|".join(COULEURS), re.I)


def recolorer(texte):
    texte = MOTIF.sub(lambda m: COULEURS[m.group(0).upper()], texte)
    texte = texte.replace("background:#F98C07;color:#0A0A0A", "background:var(--hl-grad,#F98C07);color:#0A0A0A")
    return re.sub(r"style\.css\?v=[A-Za-z0-9]+", f"style.css?v={VERSION}", texte)


fichiers = [f for f in PUBLIC.rglob("*") if f.suffix in {".html", ".css", ".js"} and "vendor" not in f.parts]
fichiers += [f for f in (RACINE / "tools").rglob("*") if f.suffix in {".py", ".html"} and f.name != Path(__file__).name
             and "guide" not in f.parts and f.name != "build_guide.py"]
modifies = 0
for f in fichiers:
    avant = f.read_text(encoding="utf-8", newline="")
    apres = recolorer(avant)
    if apres != avant:
        f.write_text(apres, encoding="utf-8", newline="")
        modifies += 1
print(modifies, "fichiers recolorés")

# Feuille principale : le dégradé pour les boutons, les surfaces et le pied de page
f = PUBLIC / "assets" / "css" / "style.css"
css = f.read_text(encoding="utf-8", newline="")
if "--hl-grad:" not in css:
    css = css.replace("--hl:#F98C07;", f"--hl:#F98C07; --hl-grad:{DEGRADE};", 1)
css = css.replace("background:var(--hl);color:#0A0A0A", "background:var(--hl-grad);color:#0A0A0A")
css = css.replace("background:var(--foot-bg);", "background:var(--hl-grad);")
f.write_text(css, encoding="utf-8", newline="")

f = PUBLIC / "assets" / "css" / "anim.css"
css = f.read_text(encoding="utf-8", newline="")
css = css.replace("background:var(--hl);color:#0A0A0A", "background:var(--hl-grad);color:#0A0A0A")
f.write_text(css, encoding="utf-8", newline="")

# Refonte : mêmes surfaces en dégradé, chiffres de la loi comme les lettres du logo
f = PUBLIC / "assets" / "css" / "v2.css"
css = f.read_text(encoding="utf-8", newline="")
for selecteur in (".v2-btn.alt", ".v2-hero", ".v2-page-head"):
    css = css.replace(f"{selecteur}{{background:var(--orange);", f"{selecteur}{{background:var(--hl-grad);")
css = css.replace(".v2 .nav .btn-sm{background:var(--orange);", ".v2 .nav .btn-sm{background:var(--hl-grad);")
css = css.replace(".v2 .site-foot{--foot-bg:var(--orange)}\n", "")
css = css.replace("Anton\",Impact,sans-serif;color:var(--orange)}",
                  "Anton\",Impact,sans-serif;color:var(--orange);background:var(--hl-grad);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}")
f.write_text(css, encoding="utf-8", newline="")
print("dégradé appliqué")
