# Welcome to MkDocs

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## arXiv pages
[help](help)

[about](about)

[corr](corr)

[hypertex](hypertex)

[labs](labs)

[new](new)

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

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml    # The configuration file.
    docs/
        index.md  # The documentation homepage.
        ...       # Other markdown pages, images and other files.

## Macro info
{{ macros_info() }}
