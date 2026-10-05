# Skills catalog

The visual catalog is served from docs/index.html. By default it groups skills into work domains, shows maturity counts, and links to the functional flows in docs/processes.json. The complete searchable skill list remains available as a secondary view.

The site data in docs/catalog.json is generated from CATALOG.md and release/package.yaml. CATALOG.md is generated from skill metadata in SKILL.md. The page shows the source production/Lab package versions and the revision recorded when the catalog data was generated; these let users compare the published catalog with their installed package.

## Refresh the catalog

After skill metadata or package-version changes, regenerate the source catalog and site data from the repository root:

\`\`\`sh
python scripts/catalog/generate_catalog.py
python scripts/catalog/generate_site_catalog.py
\`\`\`

Commit the resulting CATALOG.md and docs/catalog.json together.

## Publish with GitHub Pages

In repository Settings → Pages, choose Deploy from a branch, select main and /docs, then save. The site URL is https://aras-2003.github.io/ai-skills/.
