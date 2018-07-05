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

```
help:   # Here's the page at /help
  title: "arXiv Help & Documentation"
  content_path: pages/index.md
  pages:
    submission:     # Here's the page at /help/submission
      title: "Submission Policy"
      slug: submission-policy
      content_path: pages/submission-policy.md
    moderation:     # This one is /help/moderation
      title: "Moderation"
      slug: moderation
      content_path: pages/moderation.md
      pages:
        ...
contact:    # Here's the page at /contact
  title: "Contact arXiv staff"
  ...
```

The ``pages`` property defines all of the child pages. Each key in ``pages``
is the URL sub-path (relative to its parent) for that page. In the example
above, a page with the title "Submission policy" will be served at
``/help/submission``, using content from the document
``pages/submission-policy.md``.

There is no limit to the number of levels into which pages can be nested in
this way.

**Note:** the path ``/search`` is reserved for the search interface.

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

## Document rendering app

The application that serves the site is located in [``docs/``](docs/).

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
