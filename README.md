# arXiv Help Documentation

This project implements a markdown-driven static site for arXiv help
documentation.

## Site map and pages

The site content and structure are defined in [``site/``](site/).

The overall structure of the site is defined by a [YAML](http://yaml.org/)
file, [``site/sitemap.yaml``](site/sitemap.yaml).

Each page should have at minimum the ``title`` and ``content_path`` properties.
The ``title`` is used to generate the human-readable title in navigation,
search, browser window, etc. The ``content_path`` is the path (relative to
the sitemap) to a
[markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)
document containing the content of the page.

The root of the sitemap is a single page. For example:

```
title: "arXiv Help & Documentation"
content_path: pages/index.md
pages:
  submission:
    title: "Submission Policy"
    content_path: pages/submission-policy.md
  moderation:
    title: "Moderation"
    content_path: pages/moderation.md
    pages:
      ...
```

The ``pages`` property defines all of the child pages. Each key in ``pages``
is the URL sub-path (relative to its parent) for that page. In the example
above, a page with the title "Submission policy" will be served at
``/submission``, using content from the document
``pages/submission-policy.md``.

There is no limit to the number of levels into which pages can be nested in
this way.

**Note:** the path ``/search`` is reserved for the search interface.

## Document rendering app

The application that serves the site is located in ``docs/``.

The easiest way to build and run the site is via
[Docker](https://www.docker.com/).

To build the site (from the root of this repository):

```bash
$ docker build ./ -t arxiv/docs
```

To run the site:

```bash
$ docker run -it -p 8000:8000 arxiv/docs
```

Point your browser at http://127.0.0.1:8000 ; you should see the root page of
the site.
