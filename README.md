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

### Building a local site with Docker

You'll need [Docker](https://www.docker.com/products/docker-desktop) to do
this.

To build the arXiv docs site, run:

```bash
docker build . -t arxiv/docs:mytag
```

You should see lots of things happening, and maybe this will take a few minutes
if you have a big site. At the end, you should see something like:

```bash
Successfully built 297b169df71f
Successfully tagged arxiv/docs:mytag
```

You can then run the site by doing:

```bash
docker run -it -p 8000:8000 arxiv/docs:mytag
```

In your browser, go to http://localhost:8000/about (or whatever
page you want).

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


## Deployment & configuration

As of marXdown 0.2.1, multiple sites can be served in the same uWSGI process,
and therefore in a single Docker container with a single entrypoint. This
saves a lot of resources on overhead, especially for low-traffic sites.

Since marXdown relies heavily on start-up configuration, however, the trade-off
is that (a) we need to use configuration files to keep configs separate for
each app rather than using environment variables, and (b) that means we need to
be able to define the Flask "instance path" at app creation time (i.e. before
configuration) which means that we need a custom WSGI entrypoint for each app.

Places where relevant paths and parameters are defined:

- ``deploy/[site]/wsgi.py`` is the custom WSGI entrypoint for the site/app.
  This gets added at ``/opt/arxiv/[site]/wsgi.py`` in the Docker image.
- ``deploy/[site]/instance/application.cfg`` is a Python script with config
  parameters. This gets added at ``/opt/arxiv/[site]/instance/application.cfg``
  in the Docker image.
- ``Dockerfile`` is where all of the above gets added to the Docker image, and
  the build script for each site/app is invoked.

We use the ``arxiv/marxdown`` Helm chart to deploy to Kubernetes. See
