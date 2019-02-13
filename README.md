# arXiv Help Documentation

This project implements a markdown-driven static site for arXiv help
documentation.

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

Custom templates go in ``_templates/<SITE NAME>``.

### Pages

The directory structure in the site directory determines the site map. A
file at ``foo/baz/bat.md`` will be served at
``https://some.site/foo/baz/bat``. But note that the file
``foo/baz/index.md`` will be served at ``https://some.site/foo/baz``.

Everything is relative. You can add a link in ``foo/baz/index.md``
like ``[click here for cool](bat)``, and the link will be rendered as
``https://some.site/foo/baz/bat``.

You can put static files in the same directory structure. If the page
``specifics/coolstory.md`` has an image tag like
``![my alt text](impressive.png)``, this will get rendered as
``https://some.site/specifics/impressive.png``. In other words, it will just
work.

Only ``.md`` (markdown) files will be treated like pages. Everything else is
general static content and won't get rendered like a page (fancy headers,
etc).

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

### Templates

You can add custom templates (otherwise a generic arXiv template gets used,
with nice breadcrumbs). For example, in one of your pages you could choose to
use the template at ``_templates/mysite/custom.html`` by setting the
frontmatter:

```markdown
---
template: mysite/custom.html
---
```

## Building a site

### Building a local site with Flask

To build a site from markdown sources, you will need to specify the ``SITE_NAME``, ``SOURCE_PATH``, and ``BUILD_PATH`` (see [configuration](#configuration), below).

The application for building and serving the site is located in ``markdown/`` (a submodule, pointing at https://github.com/arxiv/arxiv-markdown).

If you're using this for the first time, you may need to do:

```bash
git submodule update --init
cd markdown
pipenv install
```

Then you can build with (from inside `./markdown`):

```bash
SITE_NAME=mysite SOURCE_PATH=/path/to/mysite BUILD_PATH=/tmp/mysite pipenv run python build.py
```

You can serve the site with Flask, using:

```bash
SITE_NAME=mysite SOURCE_PATH=/path/to/mysite BUILD_PATH=/tmp/mysite  FLASK_APP=app.py pipenv run flask run
```

Note that if you're trying to serve stuff in this repo, you can use a relative
path like:

```bash
SOURCE_PATH=../help
```

### Building a local site with Docker

You can use the ``Makefile`` in the root of this repo to build a site.

You'll need [Docker](https://www.docker.com/products/docker-desktop) to do
this.

To build a site from a local directory, you can do something like:

```bash
make local SOURCE_REF=0.1 SOURCE_DIR=/path/to/my/site SITE_NAME=mysite IMAGE_NAME=arxiv/mysite
```
Note that as each folder in the root directory is served separately SOURCE_DIR needs to include the specific folder (ex 'help', 'about').

You should see lots of things happening, and maybe this will take a few minutes
if you have a big site. At the end, you should see something like:

```bash
Successfully built 297b169df71f
Successfully tagged arxiv/mysite:0.1
```

Note that the tag is `${IMAGE_NAME}:${SOURCE_REF}``.

You can then run the site by doing:

```bash
docker run -it -p 8000:8000 arxiv/mysite:0.1
```

In your browser, go to http://localhost:8000/mysite (or whatever
page you want). Note http://localhost:8000 is what works in Ubuntu.

### Building a remote site

You can also build a site that is on GitHub, using a specific [tag](https://help.github.com/articles/working-with-tags/).

You will need to pick a place on your computer to do the building. Preferably
something in ``/tmp``.

```bash
make remote SOURCE_REF=0.1 IMAGE_NAME=arxiv/mysite REPO_ORG=arxiv REPO_NAME=arxiv-docs SOURCE_DIR=help
```

- ``SOURCE_REF=0.1`` This is the tag that you're building.
- ``IMAGE_NAME=arxiv/mysite`` The name of the image that you're building.
- ``REPO_ORG=arxiv`` The organization that owns the repo.
- ``REPO_NAME=arxiv-docs`` The name of the repo.
- ``SOURCE_DIR=help`` The directory in the repo that contains the site.

This should work just like the local build, except that it might take a bit
longer because it has to download things.

### Configuration

| Parameter | Used in Build | Used at Runtime | Description |
| --- | :---: | :---: | --- |
| SITE_NAME | Yes | Yes | Name of the site, used for building links. Must be lowercase alphanumeric. |
| SOURCE_PATH | Yes | No | Path to the markdown source directory for the site. |
| BUILD_PATH | Yes | Yes | Path where the built site is/should be stored. |
| SITE_HUMAN_NAME | No | Yes | Human-readable name of the site. |
| SITE_URL_PREFIX | No | Yes | Path where the site should be served. Must start with ``/`` (default: ``/``). |
| SITE_SEARCH_ENABLED | Yes | Yes | If set to 0, the search feature is excluded (default: 1). |


## Search

You can access the search page at ``<SITE_URL_PREFIX>/search``.

## Controlling the HTTP response (deletion, redirects)

You can control the HTTP response to the user's agent using the ``response``
key in the frontmatter. The following parameters are supported:

| Parameter | Type | Default | Description |
| :--- | :---: | :---: | :--- |
| ``response.status`` | int | ``200`` | The HTTP status code for the response. |
| ``response.location`` | str | None | Sets the ``Location`` header; this can be used to redirect the user. |
| ``response.deleted`` | bool | ``false`` | If ``true``, a status code of ``404`` will be returned, and a special "deleted" template will be rendered. |

### Example of a deleted page

```
---
response:
  deleted: true
---
This page was deleted because it was not that great.
```


### Example of a redirect

```
---
response:
  status: 301
  location: the/new/location
---
```
