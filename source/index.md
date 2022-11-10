# Initiative move arxiv-docs to static HTML pages

## Why move away from arxiv-marxdown?
At this point it seems that arxiv-marxdown was not a good approach. It
appears the main constraint that drove the development of
arxiv-marxdown was to reuse the header and footer from arxiv-base.

The code in arxiv-marxdown is a liability since it needs to be
maintained. There are dozens of static site generators that meet 98% of
our needs. Also a static site does not need python and flask to serve
it. This drastically reduces the operations complexity.

arxiv-marxdown handled this by creating a flask app that rendered
markdown and wrapped it in the header and footer like the other arxiv
Python web apps. This approach required that the docs pages be served by
a python process that is handling HTTP requests. In production this
was done with mod_wsgi in a that was subject to constraints from other
arxiv flask apps. Also both arxiv-marxdown and arxiv-docs needed to
have their dependencies maintained and needed to track arxiv-base. 

The arxiv-marxdown becomes a liability especially when compared to a
static site generator like mkdocs or Jekyll. Mkdocs has extensive
documentation, themes and plugins.

An alternative to arxiv-marxdown is to have a click flask app that can
be run to create a template with a header and footer for a static site
generator. Then a static site generator can provide 80% of the
benefits of arxiv-marxdown. An example of this is in
`prep_for_mkdocs.sh`

A further alternative is to just not reuse the header and footer from
arxiv-base.

## How to use this
Edit the docs in `/source`  then you can preview them with 

    mkdocs serve
    
and then you can view it with live updates at [http://localhost:8000/index.html](http://localhost:8000/index.html)

For full documentation visit [mkdocs.org](https://www.mkdocs.org).

## What markdown to use?
This uses python markdown which attempts to closely follow [Gruber's markdown syntax](https://daringfireball.net/projects/markdown/syntax)

## Where can I find more about mkdocs?
This uses the material theme for mkdocs. [mkdocs-material/customization](https://squidfunk.github.io/mkdocs-material/customization/)

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

## TODO

### TODO Review content and nav 
- Problem [/about/ourmembers.html](about/ourmembers.md) Top 100 and others a bit strange due to custom styles

- Very broken due to custom jinja code [/about/people/leadership_team.html](about/people/leadership_team.md)

- Support confirm and membership confirm seems like duplicates?

- Our supporters and our members seem like duplicates?

- Get rid of User testing api email form?

- marxdown redirect pages:
  [/help/announcement.html](help/announcement.md) 
  [/help/submit_html.html](help/submit_html.md) 


- User testing api and user testing group seem very similar?

- [/about/reports/whitepaper.html ](/about/reports/whitepaper.html ) could use a better name 

- No content on these pages: [/help/donate.html](help/donate.md) 
[/help/general.html](help/general.md) 
[/help/primer.html](help/primer.md) 
[/help/submission-policy.html](help/submission-policy.md) 
[/help/support.html](help/support.md) 
[/help/terms_of_submission.html](help/terms_of_submission.md) 
[/help/toc.html](help/toc.md) 

- [/help/whytex.html](help/whytex.md) fix link to [/help/textures](help/faq/textures.md) 

- Broken images on [/help/withdraw.html](help/withdraw.md)

- very broken: [/labs/showcase.html](labs/showcase.md)

- Remove GZip help

- Remove my.arxiv.org page. my.arxiv.org no longer exists
[/help/my_arxiv.html](help/my_arxiv.md)

- Images broken on [/help/orcid.html](help/orcid.md)

- Are we trying to get TeX on this page on the subject heading "Notes on Note on La$\TeX$ accent commands" ? [/help/prep.html](help/prep.md)

- Can probably get rid of this page: [/help/ssl.html](help/ssl.md) It's old news and standard practice. 

- [/help/submit_index.html](help/submit_index.md) needs better title. 


### TODO Fix titles of many pages
### TODO Write instructions for use of arxiv-docs that work for SB JE and AF (BC)
### TODO Duplicate any edits made in master to the mkdocks-material branch (BC)
As of 2022-10-21, done up through 2022-10-17

### TODO Add redirects to httpd for arxiv.org to docs.arxiv.org

### TODO Find and fix Broken pages second pass 

    | source md file                                                | problem URL                      |
    |---------------------------------------------------------------+----------------------------------|
    | source/about/reports/2021_usage.md                            | /stats/main                      |
    | source/about/reports/2020_institution_downloads_by_archive.md | /category_taxonomy               |
    | source/about/reports/whitepaper.md                            | /help/support/faq                |
    | source/new/index.md                                           | /help/support/faq                |
    | source/help/index.md                                          | ../cookies                       |
    | source/new/index.md                                           | /help/psnonunix                  |
    | source/new/index.md                                           | /x-eprint                        |
    | source/new/index.md                                           | /blurb/sep96news                 |
    | source/about/reports/arxiv_busplan_Dec2010.md                 | /help/support/2011_budget        |
    | source/about/reports/2020_usage.md                            | Mailto:membership@arXiv.org      |
    | source/new/94-96.md                                           | /help/uploads                    |
    | source/new/index.md                                           | /help/social_bookmarking         |
    | source/new/index.md                                           | /help/psmacs                     |
    | source/new/index.md                                           | /help/faqindex                   |
    | source/new/index.md                                           | /help/psvms                      |
    | source/help/moderation/appeals.md                             | /category_taxonomy               |
    | source/about/reports/whitepaper.md                            | 2010_budget                      |
    | source/about/reports/submission_category_by_year.md           | /stats/main                      |
    | source/about/reports/arxiv_busplan_July2011.md                | /help/support/2011_budget        |
    | source/new/index.md                                           | /help/pswindows                  |
    | source/about/reports/arxiv_busplan_July2010.md                | /help/support/2010_budget        |
    | source/help/subscribe.md                                      | /category_taxonomy               |
    | source/new/index.md                                           | /servers                         |
    | source/new/index.md                                           | physsub                          |
    | source/new/index.md                                           | /help/submit_nb                  |
    | source/help/author_identifiers.md                             | /auth                            |
    | source/new/index.md                                           | interruption                     |
    | source/about/reports/2020_usage.md                            | /stats/main                      |
    | source/new/index.md                                           | /help/search                     |
    | source/about/reports/2020_update.md                           | /help/policies/code\_of\_conduct |
    | source/about/reports/arxiv_busplan_Jan2012.md                 | /help/support/2012_budget        |
    | source/new/index.md                                           | /help/submit_docx                |
    | source/about/supporters.md                                    | members                          |
    | source/help/moderation/index.md                               | /category_taxonomy               |
    | source/about/index.md                                         | /stats/main                      |
    | source/new/index.md                                           | /help/faq/y2k                    |
    | source/new/index.md                                           | /new/q-fin_announcement          |
    | source/about/reports/2021_usage.md                            | Mailto:membership@arXiv.org      |
    | source/about/reports/2020_update.md                           | /help/policies/privacy\_policy   |
    | source/about/reports/arxiv_busplan_Dec2010.md                 | /help/support/2010_budget        |
    | source/about/reports/submission_category_by_year.md           | /category_taxonomy               |
    | source/help/prep.md                                           | /category_taxonomy               |
    | source/new/index.md                                           | /help/facebook                   |
    | source/new/q-fin_announce.md                                  | /help/uploads                    |
    | source/about/reports/arxiv_busplan_Apr2011.md                 | /help/support/2011_budget        |
    | source/help/api/user-manual.md                                | /category_taxonomy               |
    | source/new/q-bio_announce.md                                  | /help/uploads                    |
    | source/about/reports/arxiv_busplan_Oct2011.md                 | /help/support/2011_budget        |
    | source/about/reports/2019_update.md                           | /about/reports/2019roadmap       |
    | source/new/condreorg.md                                       | /help/uploads                    |

### Check for broken links
``
    pip install linkchecker 
    mkdocs serve > /dev/null 2>&1 &
    linkchecker http://localhost:8000/about/index.html --no-follow-url=".*/abs/.*"``
``

## Done items
### DONE Initial move of markdown files from marxdown to mkdocs (BC)
### DONE arxiv-base, browse and search with links to docs.arxiv.org (BC)
### DONE CICD for edits at github to docs.arxiv.org (BC)
### DONE site and cert for docs.arxiv.org (BC)
### DONE Fix links (BC)
Using `urlchange.py` script from commit 705745c to create changes in 17fa1d1

### DONE Find and fix Broken pages first pass (BC)
- DONE Problem [/about/governance.html](about/governance.md) stringe text {mk-png-60}
- DONE [/about/principles.html](about/principles.md) strange text like <sup1</sup
- DONE [/help/submit_sword.html](help/submit_sword.md) Link to arxiv.org/help/contact
- DONE Has bad raw jinja: `{% raw %}\hypersetup` [/help/submit_tex.html](help/submit_tex.md) 

