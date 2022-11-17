# arXiv Help Documentation

Static sites for arXiv.

## Building a local site

To build the arXiv docs site, run:

```bash
python -m venv docs-venv
source docs-venv/bin/activate
pip install -r mkdocs-requirements.txt
./make_arxiv_theme/prep_for_mkdocs.sh
mkdocs serve
```

Then you will have the site served locally with hot reloading on
edits. In your browser, go to http://localhost:8000/index.html

## Site structure

Each site should be contained in a single directory. For example:

```
mysite/
├── index.md
├── specifics/
|   ├── impressive.png
|   └── coolstory.md
└── _templates
    └── mysite
        └── custom.html
```

The directory structure in the site directory determines the site map. A
file at ``foo/baz/bat.md`` will be served at
``https://some.site/foo/baz/bat.html`` and the file
``foo/baz/index.md`` will be served at ``https://some.site/foo/baz/index.html``.

## Links
Both absolute and relative links work. You can add a link in
``foo/index.md`` to ``foo/baz.md`` with either ``[click this absolute
link](/foo/baz.md)`` or ``[click this relative
link](baz.md)``. Relative links assist in movig directories of pages
around since a whole subdirectory can be moved and if all the pages in
it have relative links then those will not break. Absolute links
assist in moving pages around since the links on a single page do not
break if a single page is moved.

You can put static files in the same directory structure. If the page
``specifics/coolstory.md`` has an image tag like
``![my alt text](impressive.png)``, this will get rendered as
``https://some.site/specifics/impressive.png``.

Only ``.md`` (markdown) files will be treated like pages. Everything
else is won't get rendered like a page (fancy headers, etc).

Inside of your ``.md`` files, you can add some front-matter. For example,
if you want the title in the browser tab and breadcrumbs to be different from
whatever is in the content of the page, you could do:

```markdown
---
title: This is the title that I like in the browser tab
---
# This is the title that gets displayed as an H1 on the page.

Bacon ipsum dolor sit amet...
```

The first H1 tag will be used as the name of the page in navigtion.


## Templates, CSS, JS
`arxiv-docs` uses
[mkdocs-material](https://squidfunk.github.io/mkdocs-material) which
is theme for mkdocs. For information about customizing themes, CSS or
JS see:

https://squidfunk.github.io/mkdocs-material/customization/

## Controlling the HTTP response (deletion, redirects)

TODO: right now there we don't have redirects setup.

## Deployment & Configuration

``mkdocs build`` leaves a static site in `./site` This is a static
site with relative links that can be served with any system that hosts
a web site.

The cloud build YAML files combined with CloudBuild triggers in
`arxiv-production` comprise the deployment pipeline for `arxiv-docs`.

The bucket needs to be configured to use index.html pages for bare
paths and the 404 page:

```
gsutil web set -m index.html -e 404.html gs://arxiv-docs
```

