# String Theory Wiki

The static successor to the MediaWiki-based String Theory Wiki. Its pages are stored in Markdown files in
[`docs/`](docs/), built with MkDocs Material and published through
GitHub Pages.

Currently hosted at:

<https://stringwiki.github.io/>

## Local preview

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/mkdocs serve
```

Then open the local address shown by MkDocs (normally <http://127.0.0.1:8000/>).

## Updating pages

Edit the relevant Markdown file in `docs/` and open a pull request. The
workflow validates every pull request and publishes pushes to `main`.

## Migration source

`scripts/convert_mediawiki.py` converts a current-revision MediaWiki XML export
to Markdown. The raw export and personal notes are intentionally ignored by Git,
so they are not published. To repeat the conversion:

```bash
python3 scripts/convert_mediawiki.py \
  --source stringwiki-pages-YYYY-MM-DD.xml.gz \
  --output docs
```

Copy any uploaded assets to `docs/assets/` afterwards. The converter publishes
the main, project, and help namespaces; it excludes MediaWiki settings, user
profiles, talk pages, and file-description records.
