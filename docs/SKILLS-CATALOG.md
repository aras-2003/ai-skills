# Skills catalog

The visual catalog is served from `docs/index.html`. Its data is generated from `CATALOG.md`, which in turn is generated from skill metadata in `SKILL.md` files.

## Refresh the catalog

After skill metadata changes, regenerate both files from the repository root:

```sh
python scripts/catalog/generate_catalog.py
python scripts/catalog/generate_site_catalog.py
```

Commit the resulting `CATALOG.md` and `docs/catalog.json` together.

## Publish with GitHub Pages

In repository **Settings → Pages**, choose **Deploy from a branch**, select `main` and `/docs`, then save. The site URL is `https://aras-2003.github.io/ai-skills/`.
