# Initiative move arXiv docs to MKDocs static HTML pages

## TODO
### DONE Initial move of markdown files from marxdown to mkdocs (BC)
### DONE arxiv-base, browse and search with links to docs.arxiv.org (BC)
### DONE CICD for edits at github to docs.arxiv.org (BC)
### DONE site and cert for docs.arxiv.org (BC)
### Fix links
Using ``linkchecker http://localhost:8000/about/index.html --no-follow-url=".*/abs/.*"``

### Find and fix Broken pages first pass (BC)
- DONE Problem [/about/governance.html](/about/governance.md) stringe text {mk-png-60}

- DONE [/about/principles.html](/about/principles.md) strange text like <sup1</sup

- marxdown redirect pages:
  [/help/announcement.html](/help/announcement.md) 
  [/help/submit_html.html](/help/submit_html.md) 
  
- DONE [/help/submit_sword.html](/help/submit_sword.md) Link to arxiv.org/help/contact

- Has bad raw jinja: " {% raw %}\hypersetup{pdfauthor={some author},pdftitle={eye-catching title}}{% endraw %}." [/help/submit_tex.html](/help/submit_tex.md) 


### Find and fix Broken pages second pass 
### Review content and nav 
- Problem [/about/ourmembers.html](/about/ourmembers.md) Top 100 and others a bit strange due to custom styles

- Very broken due to custom jinja code [/about/people/leadership_team.html](/about/people/leadership_team.md)

- Support confirm and membership confirm seems like duplicates?

- Our supporters and our members seem like duplicates?

- Get rid of User testing api?

- User testing api and user testing group seem very similar?

- [/about/reports/whitepaper.html ](/about/reports/whitepaper.html ) could use a better name 

- No content on these pages: [/help/donate.html](/help/donate.md) 
[/help/general.html](/help/general.md) 
[/help/primer.html](/help/primer.md) 
[/help/submission-policy.html](/help/submission-policy.md) 
[/help/support.html](/help/support.md) 
[/help/terms_of_submission.html](/help/terms_of_submission.md) 
[/help/toc.html](/help/toc.md) 

- [/help/whytex.html](/help/whytex.md) fix link to [/help/textures](/help/faq/textures.md) 

- Broken images on [/help/withdraw.html](/help/withdraw.md)

- very broken: [/labs/showcase.html](/labs/showcase.md)

- Remove GZip help

- Remove my.arxiv.org page. my.arxiv.org no longer exists
[/help/my_arxiv.html](/help/my_arxiv.md)

- Images broken on [/help/orcid.html](/help/orcid.md)

- Are we trying to get TeX on this page on the subject heading "Notes on Note on La$\TeX$ accent commands" ? [/help/prep.html](/help/prep.md)

- Can probably get rid of this page: [/help/ssl.html](/help/ssl.md) It's old news and standard practice. 

- [/help/submit_index.html](/help/submit_index.md) needs better title. 


### Fix titles of many pages
### Write instructions for use of arxiv-docs that work for SB JE and AF (BC)
### Duplicate any edits made in master to the mkdocks-material branch (BC)
### Add redirects to httpd for arxiv.org to docs.arxiv.org

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

## What markdown to use?
This uses python markdown which attempts to closely follow [Gruber's markdown syntax](https://daringfireball.net/projects/markdown/syntax)

## Where can I find more about mkdocs?
This uses the material theme for mkdocs. [mkdocs-material/customization](https://squidfunk.github.io/mkdocs-material/customization/)
## CSS for a page
See https://squidfunk.github.io/mkdocs-material/customization/#additional-css


## How is header and footer theme created?
See the notes in [theme-generator](https://github.com/arXiv/arxiv-docs/theme_generator/README.md)

## How to handle 'Missing end of comment tag'?
When using mkdocs and the macros plug in you can get a stack grace
with a Jinja error like message "Missing end of comment tag".  This is
often due to LaTeX or code samples with text like `{% raw %} "{{?}}"
{% endraw %}`.

As of 2022-09 the macro plugin for mkdocs is disabled and this should
not be a problem. 

See the [mkdocs-macros docs](https://mkdocs-macros-plugin.readthedocs.io/en/latest/advanced/#code-blocks-containing-similar-languages) for several ways to work around this.
