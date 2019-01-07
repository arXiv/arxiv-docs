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



You can use the ``Makefile`` in the root of this repo to build a site.

You'll need [Docker](https://www.docker.com/products/docker-desktop) to do
this.


### Building a local site

To build a site from a local directory, you can do something like:

```bash
make local SOURCE_REF=0.1 SOURCE_DIR=/path/to/my/site IMAGE_NAME=somecoolsite
```

- ``SOURCE_REF=0.1`` This is the tag that you're building.
- ``IMAGE_NAME=arxiv/somecoolsite`` The name of the image that you're building.
- ``SOURCE_DIR=site`` The directory in the repo that contains the site.
- ``TARGET_DIR=site`` You should make this the same as the directory that contains your site. I know it's confusing, I'll fix it.

You should see lots of things happening, and maybe this will take a few minutes
if you have a big site. At the end, you should see something like:

```bash
Successfully built 297b169df71f
Successfully tagged arxiv/somecoolsite:0.1
```

Note that the tag is `${IMAGE_NAME}:${SOURCE_REF}``.

You can then run the site by doing:

```bash
docker run -it -p 8000:8000 arxiv/somecoolsite:0.1
```

In your browser, go to http://localhost:8000/specifics/coolstory (or whatever
page you want).


### Building a remote site

You can also build a site that is on GitHub, using a specific [tag](https://help.github.com/articles/working-with-tags/).

You will need to pick a place on your computer to do the building. Preferably
something in ``/tmp``.

```bash
make remote SOURCE_REF=0.1 BUILD_DIR=/tmp/build-it IMAGE_NAME=somecoolsite REPO_ORG=cul-it  REPO_NAME=arxiv-docs SOURCE_DIR=site
```

- ``SOURCE_REF=0.1`` This is the tag that you're building.
- ``BUILD_DIR=/tmp/build-it`` Make sure that you can write here.
- ``IMAGE_NAME=somecoolsite`` The name of the image that you're building.
- ``REPO_ORG=cul-it`` The organization that owns the repo.
- ``REPO_NAME=arxiv-docs`` The name of the repo.
- ``SOURCE_DIR=site`` The directory in the repo that contains the site.

This should work just like the local build, except that it might take a bit
longer because it has to download things.


### Configuration

| Parameter | Used in Build | Used at Runtime | Description |
| --- | :---: | :---: | --- |
| SITE_NAME | Yes | Yes | Name of the site, used for building links. Must be lowercase alphanumeric. |
| SOURCE_PATH | Yes | No | Path to the markdown source directory for the site. |
| BUILD_PATH | Yes | Yes | Path where the built site is/should be stored. |
| SITE_HUMAN_NAME | No | Yes | Human-readable name of the site. |
