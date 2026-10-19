# Theme generator
Generates the mkdocs-material theme override (`overrides/main.html`) with the arXiv design
system's head/header/footer. The chrome comes from the `arxiv-brand-templates` package,
taken from the design-system branch (`DS_REF` in `prep_for_mkdocs.sh`) and rendered by a
plain Jinja script (`app.py`); mkdocs itself needs no design-system dependency. The committed
override is the pinned result: updating the chrome is regenerating and committing it.

# Instructions
To change the page, edit `make_arxiv_theme/templates/main.html` (two Jinja levels: bare
directives expand the design-system chrome at generation, `{% raw %}` blocks pass through
to mkdocs), then regenerate `overrides/main.html` (never edit it by hand):

```bash
cd arxiv-docs
./make_arxiv_theme/prep_for_mkdocs.sh          # design-system master (or DS_REF=<branch or sha>)
```

The override is environment-independent: the chrome's hosts and asset route are mkdocs
expressions resolved at build time from `mkdocs.yml` (`ARXIV_HOST`, `INFO_HOST`, `BRAND_STATIC_BASE`):

```bash
ARXIV_HOST=https://dev.arxiv.org INFO_HOST=https://info.dev.arxiv.org mkdocs build
```
