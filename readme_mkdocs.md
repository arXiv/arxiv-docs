# arXiv docs and Mkdocs-Material 
mkdocs-material is a static site generator. That means it takes the
`.md` files and creates `.html` files for them that can be served
using a basic web server.

## How to use this
The `.md` files that are ued with mkdocs exist in `/source`. You can
preview them with

    mkdocs serve
    
and then you can view it with live updates at
[http://localhost:8000/index.html](http://localhost:8000/index.html)

For full documentation visit [mkdocs-material](https://squidfunk.github.io/mkdocs-material/).

## What markdown to use?
This uses python markdown which attempts to closely follow [Gruber's
markdown syntax](https://daringfireball.net/projects/markdown/syntax)

## Where can I find more about mkdocs?
This uses the material theme for
mkdocs. See [mkdocs-material/customization](https://squidfunk.github.io/mkdocs-material/customization/)

## CSS for a page
See [mkdocs-material additional CSS](https://squidfunk.github.io/mkdocs-material/customization/#additional-css)

## How to handle 'Missing end of comment tag'?
As of 2022-09 the macro plugin for mkdocs is disabled and this should
not be a problem. 

When using mkdocs and the macros plug in you can get a stack grace
with a Jinja error like message "Missing end of comment tag".  This is
often due to LaTeX or code samples with text like `{% raw %} "{{?}}"
{% endraw %}`.

See the [mkdocs-macros docs](https://mkdocs-macros-plugin.readthedocs.io/en/latest/advanced/#code-blocks-containing-similar-languages) for several ways to work around this.
