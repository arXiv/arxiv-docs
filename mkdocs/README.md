# Static Site Generation with mkdocs
This directory contains a system to build the markdown help files into
static HTML pages.

## How to generate labs
  ./mklabs.sh
  # at this point the static site is in mkdocs/labs-site
  google-chrome mkdocs/labs-site/index.html

## Generate with auto refresh preview for editing
  cd arxiv-docs
  python3 -m venv ./env
  source ./env/bin/activate
  
  # This step makes the template and installs python packages
  ./prep_for_mkdocs.sh
  
  mkdocs serve -f mkdocs/mkdocs.yml
  google-chrome http://localhost:8000
  # edits to the html will be live updated in the browser

## Links in MD pages
This site is configured to use the mkdocs plugin `abs-to-rel` so links
become relative links in the HTML. This allows flexibility in where and
how the site can be served.

You write links that are absolute from the root of the `docs`
directory to the MD file to be linked.

Ex. `/about/reports/2010_usage.md` 

That is the link to use from all directories in the docs. Do not use
relative links. Use the suffix `.md` not `.html`. Link directly to
`index.md` files, linking to the parent directory does not work.

The goal here is to facilitate easy .md link editing. 

There is no need to add `../` to link to content in parent
directories. There is no need to consider how the name of the file
you'd like to link to need to be changed, `reports`, `reports.html`,
or `reports/index.html`.

Links to non-arXiv or `arxiv.org` pages outside of docs, use URLs with
protocols and domain names.  Ex. `https://home.cern/cheeses` or
`https://arxiv.org/auth`. Note that some of the `/stats` pages are not
part of the docs.

## CSS for a page
To add a css file to a specific page use the following example:

    {% raw %}{% block addl_head %}{% endraw %}
    <link rel="stylesheet" type="text/css" href="{{'/css/brand_guide.css' | urlize}}""/>
    {% raw %}{% endblock addl_head %}{% endraw %}

That will add the `<link>` tag to load
`arxiv-docs/mkdocs/docs/css/brand_guide.css` to the page it is
included on.

## LaTeX and How to handle 'Missing end of comment tag'?
This is often due to LaTeX or code samples with text like `{% raw %} "{{?}}" {% endraw %}`.

See the [mkdocs-macros docs](https://mkdocs-macros-plugin.readthedocs.io/en/latest/advanced/#code-blocks-containing-similar-languages) for several ways to work around this.

## Redirects
These are provided by the `redirect` plugin and are configured in the
`mkdocs.yml` file.

## Macros in python
Macros written in python can be added to `main.py`. See
[mkdocs-macros](https://mkdocs-macros-plugin.readthedocs.io/)

## The custom theme for mkdocs
The header and footer on the pages are from a mkdocs custom theme that
is generated from `arxiv-base` using the code in
`arxiv-docs/theme_generator` This includes a small Flask click app
that uses `base.html` from `arxiv-base` to build a template for use in
mkdocs.

Running `prep_for_mkdocs.sh` builds the template and puts it in place.

The template is at
`arxiv-docs/theme_generator/templates/generate_mkdocs_template.html`. If
you want new changes to that to be used in `mkdocs build` you need to
rerun `prep_for_mkdocs.sh`.
