# avitime-site

Site vitrine public d'Avitime, en ligne sur **https://avitime.fr**.

- `public/` : les pages HTML, styles, vidéos et images (générées depuis le prototype, dépôt privé `avitime`).
- `docker-compose.yaml` + `nginx.conf` : déploiement sur le VPS Hostinger (Docker + Traefik, HTTPS automatique).

Ce dépôt est public car le serveur ne peut récupérer que du code public ; il ne contient que ce qui est déjà visible sur le site.

Parcours commerçant : après chaque génération des pages, relancer tools/parcours_commercant.py.

## Refonte du site vitrine

Scripts à relancer dans cet ordre si besoin : `tools/corrections_vitrine.py`, `tools/commercants_blocs.py`, `tools/couleur_logo.py`, puis `tools/make_vitrine_v2.py`. Ce dernier génère l'accueil, `/tarifs`, `/pourquoi-faire-tester-vos-produits` et la page 404.

La page Intégrations est désormais générée par `tools/make_vitrine_v2.py` depuis `tools/pages/integrations.v2.html`. Ne relancez pas `tools/pages/build.py` pour cette page : il remettrait l'ancien gabarit.

La page Commerçants est elle aussi générée par `tools/make_vitrine_v2.py`, depuis `tools/pages/commercants.v2.html`. `tools/pages/build.py` ne doit plus être lancé pour cette page.
