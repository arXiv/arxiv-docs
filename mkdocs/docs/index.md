# arXiv MKDocs genereated pages

## arXiv pages

[brand](brand) [help](help) [about](about) [corr](corr) [hypertex](hypertex) [labs](labs) [new](new)

## CSS for a page
To add a css file to a specfic page use the following example:

    {% raw %}{% block addl_head %}{% endraw %}
    <link rel="stylesheet" type="text/css" href="{{'/css/brand_guide.css' | urlize}}""/>
    {% raw %}{% endblock addl_head %}{% endraw %}

That will add the `<link>` tag to load
`arxiv-docs/mkdocs/docs/css/brand_guide.css` to the page it is
included on.

## Project layout

    arxiv-docs
        theme_generator/   # App to generate mkdocs theme from arxiv-base
        mkdocs/
            mkdocs.yml    # The configuration file.
            docs/
                index.md  # The documentation homepage.
                ...       # Other markdown pages, images and other files.

## How is the arxiv-base template custom theme created?
See the notes in `arxiv-docs/theme_generator/templates/generate_mkdocs_template.html`

## How to handle 'Missing end of comment tag'?
This is often due to LaTeX or code samples with text like `{% raw %} "{{?}}" {% endraw %}`.

See the [mkdocs-macros docs](https://mkdocs-macros-plugin.readthedocs.io/en/latest/advanced/#code-blocks-containing-similar-languages) for several ways to work around this.

## Commands

* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

[edit on github]({{ page.edit_url }})

[edit on github]({{ page.edit_url }})

## Help search
{% if 'search' in config['plugins'] %}
<h1 id="search">Search Results</h1>

<form action="search.html">
  <input name="q" id="mkdocs-search-query" type="text" >
</form>

<div id="mkdocs-search-results">
  Sorry, page not found.
</div>
{% endif %}

## Macro info
{{ macros_info() }}
