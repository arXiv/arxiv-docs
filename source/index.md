# Initiative to move arXiv docs from arxiv-markdown to MKDocs static generated pages

## Why move away from arxiv-marxdown?
At this point it seems that arxiv-marxdown was not a good approch. It
appears the main constraint that drove the development of
arxiv-marxdown was to reuse the header and footer from arxiv-base.

arxiv-marxdown handled this by creating a flask app that rendered
markdown and wrapped it in the header and footer like the other arxiv
Python web apps. This approch required that the docs pages be seved by
a python process that is handling HTTP requests. In production this
was done with mod_wsgi in a that was subject to constraints from other
arxiv flask apps. Also both arxiv-marxdown and arxiv-docs needed to
have their dependencies mmaintained and needed to track arxiv-base. 

The arxiv-marxdown becomes a liability especially when compared to a
static site generator like mkdocs or jekyll. Mkdocs has extensive
documentation, themes and plugsins.

An alternative to arxiv-marxdown is to have a click flask app that can
be run to create a template with a header and footer for a static site
generator. Then a static site generator can provide 80% of the
benifits of arixv-marxdown. An example of this is in
`prep_for_mkdocs.sh`

A further alterantive is to just not reuse the header and footer from
arxiv-base.

## How to use this
Edit the docs in `/source`  then you can preview them with 

    mkdocs serve
    
and then you can view it with live updates at [http://localhost:8000/index](http://localhost:8000/index)

Other commands are:

* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## Where can I find more about mkdocs?
This uses the material theme for mkdocs. [mkdocs-material/customization](https://squidfunk.github.io/mkdocs-material/customization/)
## CSS for a page
To add a css file to a specfic page use the following example:

    {% raw %}{% block addl_head %}{% endraw %}
    <link rel="stylesheet" type="text/css" href="{{'/css/brand_guide.css' | urlize}}""/>
    {% raw %}{% endblock addl_head %}{% endraw %}

That will add the `<link>` tag to load
`arxiv-docs/mkdocs/docs/css/brand_guide.css` to the page it is
included on.

## How is the arxiv-base template custom theme created?
See the notes in `arxiv-docs/mkdocs/theme_generator/templates/generate_mkdocs_template.html`

## How to handle 'Missing end of comment tag'?
This is often due to LaTeX or code samples with text like `{% raw %} "{{?}}" {% endraw %}`.

See the [mkdocs-macros docs](https://mkdocs-macros-plugin.readthedocs.io/en/latest/advanced/#code-blocks-containing-similar-languages) for several ways to work around this.

