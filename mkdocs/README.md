# Static Site Generation with mkdocs
This directory contains a system to build the markdown help files into
static HTML pages.

## How to generate labs
  ./mklabs.sh
  # at this point the statis site is in mkdocs/labs-site
  google-chrome mkdocs/labs-site/index.html

## Generate with auto refresh preview for editing
  cd arxiv-docs
  python3 -m venv ./env
  source ./env/bin/activate
  ./prep_for_mkdocs.sh
  mkdocs serve -f mkdocs/mkdocs.yml
  google-chrome http://localhost:8000
  # edits to the html will be live updated in the browser

## Redirects
These are provided by a redirect plugin and are configured in the
`mkdocs-SITE.yml` file.

## Macros in python
Macros written in python can be added to `main.py`. See
[mkdocs-macros](https://mkdocs-macros-plugin.readthedocs.io/)
