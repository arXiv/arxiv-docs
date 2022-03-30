# Static Site Generation with mkdocs
This directory contains a system to build the markdown help files into
static HTML pages.

## How to generate labs
  ./mklabs.sh
  # at this point the statis site is in mkdocs/labs-site
  google-chrome mkdocs/labs-site/index.html

## Auto refresh preview for editing
  python3 -m venv /tmp/mkdocsvenv
  source /tmp/mkdocsvenv/bin/activate
  ./prep_for_mkdocs.sh
  cd mkdocs
  mkdocs serve
  google-chrome http://localhost:8000
  # edits to the html will be live updated in the browser

## Display raw text
The jinja2 `raw` directive can be used:

`{% raw %}something &gt; otherthing{% endraw %}`

## Redirects
These are provided by a redirect plugin and are configured in the
`mkdocs-SITE.yml` file.

## Macros in python
Macros written in python can be added to `main.py`. See
[mkdocs-macros](https://mkdocs-macros-plugin.readthedocs.io/)
