# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

The content and build for **info.arxiv.org** — arXiv's about/help/policy/labs pages.
Pages are Markdown in `source/`, rendered by **mkdocs-material** into a fully static
HTML site (`site/`, gitignored) that is served from GCP buckets with no Python or web
server at runtime. See `DECISIONS.md` for why this replaced the old Flask-based
`arxiv-marxdown`.

Most work here is editing Markdown content, not code. Reserve architectural changes for
`mkdocs.yml`, `overrides/`, `hooks/`, and `make_arxiv_theme/`.

## Commands

```bash
# Local preview with hot reload (Python 3.11)
python -m venv docs-venv && source docs-venv/bin/activate
pip install -r requirements.txt
mkdocs serve            # http://localhost:8000/index.html

mkdocs build            # render static site into site/ (what the deploy pipeline runs)
```

There are no tests or linters. Verifying a change means running `mkdocs serve` (or
`build`) and confirming pages render without Jinja/Markdown errors and links resolve.

## Branch and deploy flow

Deployment is driven by CloudBuild triggers (`deploy/cloudbuild-*.yaml`), each of which
just runs `mkdocs build` and rsyncs `site/` to a bucket:

- **PR → `develop`**: preview at `https://storage.googleapis.com/arxiv-docs-prs/<branch>/<path>` (the home page is not previewed; direct commits to `develop` get no preview).
- **`develop`**: deploys to `info.dev.arxiv.org` (`docs-develop` bucket).
- **`master`**: deploys to production `info.arxiv.org` (~15 min after merge).

Normal path: branch → PR to `develop` → merge → PR `develop` to `master` → merge.
Merge `develop`→`master` promptly; lingering commits get swept into others' deploys.

## Authoring rules that bite

- **`use_directory_urls: false`** — the site is served with no web-server URL rewriting,
  so links must point at real files: `/help/gzip.html`, not `/help/gzip`. Use `.md` in
  source links (`[x](baz.md)` or `[x](/foo/baz.md)`); mkdocs rewrites them to `.html`.
- **Navigation is manual**: the left nav is `source/SUMMARY.md` (mkdocs-literate-nav),
  not auto-generated. New pages must be added there to appear in the nav.
- **Only `.md` files become styled pages.** Other files (including `.html`) pass through
  unchanged — this is how redirect stubs work.
- **Redirects**: simple renames go in `mkdocs.yml` `redirect_maps`; otherwise drop a
  hand-written `<meta refresh>` HTML file at the old path (relative URL if the target is
  inside mkdocs, absolute if outside). See `AUTHORING.md`.
- **Image styling** uses attr_list classes: `{.mkd-img-full}`, `.mkd-img-60`,
  `.mkd-img-thumb`, `.mkd-img-border`, `.mkd-img-left`, `.mkd-img-right` (combinable).
  Static assets sit alongside the `.md` that references them.
- Front-matter `title:` overrides the browser-tab/breadcrumb title; the first `# H1` is
  the nav name. Full authoring reference: `AUTHORING.md`.

## Theme / chrome architecture

- **`overrides/main.html`** is the mkdocs-material template override carrying the arXiv
  header/footer ("spinout chrome"). It is normally *generated* from `arxiv-base` via
  `make_arxiv_theme/prep_for_mkdocs.sh` (a Flask CLI: `flask generate mkdocs_template`),
  but is currently hand-maintained because the chrome-bearing arxiv-base isn't wired into
  that generator yet. Chrome CSS/JS/images are **not vendored** — they load from the
  shared versioned base-static route.
- **Per-environment roots** are set in `mkdocs.yml` `extra:` via `!ENV`. A dev build must
  override them so it stays inside dev:
  ```bash
  BASE_STATIC=https://static.dev.arxiv.org/static/base/1.0.1 \
  ARXIV_HOST=https://dev.arxiv.org INFO_HOST=https://info.dev.arxiv.org mkdocs build
  ```
- **`hooks/a11y.py`** is an `on_post_page` hook that string-patches WCAG fixes into
  Material's generated HTML (things unreachable via config), so no template is frozen
  against the theme.
- `overrides/404.html` handles extensionless→`.html` redirects (e.g. `/about/contact`).
- The docs-only controls (color-theme toggle, internal docs search, the "arXiv info"
  subsite tag) are **not** part of the shared chrome and must not propagate to other repos.
