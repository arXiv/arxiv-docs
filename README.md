# arXiv Help Documentation

This project implements a markdown-driven static site for arXiv help
documentation.

## Site structure

Each site should be contained in a single directory, with subdirectories for
content, templates, and reusable components. For example:

```
mysite/
├── pages
|   ├── index.md
|   └── specifics/
|       ├── impressive.png
|       └── coolstory.md
|
├── components
|   └── my
|       └── component.md
└── templates
    └── custom.html
```

### Pages

The directory structure in the ``pages/`` directory determines the site map. A
file at ``pages/foo/baz/bat.md`` will be served at
``https://some.site/foo/baz/bat``. But note that the file
``pages/foo/baz/index.md`` will be served at ``https://some.site/foo/baz``.

Everything is relative. You can add a link in ``pages/foo/baz/index.md``
like ``[click here for cool](bat)``, and the link will be rendered as
``https://some.site/foo/baz/bat``.

You can put static files in the same directory structure. If the page
``pages/specifics/coolstory.md`` has an image tag like
``![my alt text](impressive.png)``, this will get rendered as
``https://some.site/specifics/impressive.png``. In other words, it will just
work.

Only ``.md`` (markdown) files will be treated like pages. Everything else is
general static content and won't get rendered like a page (fancy headers,
etc).

Inside of your ``.md`` files, you can add some front-matter. For example,
if you want the title in the browser tab and breadcrumbs to be different from
whatever is in the content of the page, you could do:

```
---
title: This is the title that I like in the browser tab
slug: persistent-slug-for-this-page
---
# This is the title that gets displayed as an H1 on the page.

Bacon ipsum dolor sit amet...
```

Note: you don't have to set a slug, but it may be useful for persistent links.
See below.


### Components

Components are bits of content and data that you want to use in various places.
They look a lot like pages, for example the file
``components/my/component.md``:

```
---
arbitrary: data
---
Some content that I'd like to use again and again and again.
```

You can use this in your pages and templates like:

```
The arbitrary value is: {{ components.my.component.data.arbitrary }}

And here is some content: {{ components.my.component.data.content }}
```

At some point we'll make these transportable outside of a site. Right now they
only work within a site.

That should work in both ``.md`` files and templates, by the way.

### Templates

You can add custom templates (otherwise a generic arXiv template gets used,
with nice breadcrumbs). For example, in one of your pages you could choose to
use the template at ``templates/custom.html`` by setting the frontmatter:

```
template: custom.html
```

## Persistent links to pages

Sometimes you will need to move a page to a different part of the site map.
Updating all of the links to a page that is moved can be an ordeal. To avoid
that kind of pain and suffering, use the ``slug`` key on each page element
to give it a unique name.

When writing links in markdown, you can use the slug ``submission-policy``
instead of the relative URL for the page and it will be automagically converted
to the URL of that page wherever it might reside.

E.g. this markdown...

```
Be sure to read about our [submission policies](submission-policy) before
submitting a paper.
```

Will generate this HTML:

```
Be sure to read about our <a href="/help/submission">submission policies</a>
before submitting a paper.
```

## Building a site

You can use the ``Makefile`` in the root of this repo to build a site.

You'll need [Docker](https://www.docker.com/products/docker-desktop) to do
this.


### Building a local site

To build a site from a local directory, you can do something like:

```
make local SOURCE_REF=0.1 SOURCE_DIR=/path/to/my/site IMAGE_NAME=somecoolsite
```

- ``SOURCE_REF=0.1`` This is the tag that you're building.
- ``IMAGE_NAME=arxiv/somecoolsite`` The name of the image that you're building.
- ``SOURCE_DIR=site`` The directory in the repo that contains the site.
- ``TARGET_DIR=site`` You should make this the same as the directory that contains your site. I know it's confusing, I'll fix it.

You should see lots of things happening, and maybe this will take a few minutes
if you have a big site. At the end, you should see something like:

```
Successfully built 297b169df71f
Successfully tagged arxiv/somecoolsite:0.1
```

Note that the tag is `${IMAGE_NAME}:${SOURCE_REF}``.

You can then run the site by doing:

```
docker run -it -p 8000:8000 arxiv/somecoolsite:0.1
```

In your browser, go to http://localhost:8000/specifics/coolstory (or whatever
page you want).


### Building a remote site

You can also build a site that is on GitHub, using a specific [tag](https://help.github.com/articles/working-with-tags/).

You will need to pick a place on your computer to do the building. Preferably
something in ``/tmp``.

```
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
