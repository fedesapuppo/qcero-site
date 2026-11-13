# Qcero

Static site for qcero.com.ar, built with Jekyll.

- Products: `_productos/`, services: `_servicios/`, colors: `_colores/`.
- Company data (address, phone, branches, social): `_data/empresa.yml`.
- Images: `python3 scripts/imagenes.py <media-dir>` converts referenced originals to WebP in `assets/img/`.
- Local: `bundle install && bundle exec jekyll serve`.
- Pushing to `main` publishes through GitHub Actions.
