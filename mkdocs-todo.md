# Migration to mkdocs

### TODO Review content and nav 
>
- Support confirm and membership confirm seems like duplicates? (I think they are different. Left as is)

- Our supporters and our members seem like duplicates? (left as is. Will tackle this question with Jim and Alison during future planned content rehaul)

- Get rid of User testing api email form? (Kept for now)

- marxdown redirect pages:
  [/help/announcement.html](help/announcement.md) 
  [/help/submit_html.html](help/submit_html.md) 

### TODO Membership banner for arxiv-docs mkdocs
### TODO Write instructions for use of arxiv-docs that work for SB JE and AF (BC)
### TODO Duplicate any edits made in master to the mkdocks-material branch (BC)
As of 2022-10-21, done up through 2022-10-17

### TODO Add redirects to httpd for arxiv.org to docs.arxiv.org
BC has a set of code in arxiv-httpd that does this.

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

### DONE Second pass (SB)
- Problem [/about/ourmembers.html](about/ourmembers.md) Top 100 and others a bit strange due to custom styles (DONE)

- Very broken due to custom jinja code [/about/people/leadership_team.html](about/people/leadership_team.md) (DONE)

- [/about/reports/whitepaper.html ](/about/reports/whitepaper.html ) could use a better name  (DONE)

- User testing api and user testing group seem very similar? (Kept both, they are unique use cases. Differentiated title more)


- No content on these pages:  (DONE. removed empty pages below, + others as found)
[/help/donate.html](help/donate.md) 
[/help/general.html](help/general.md) 
[/help/primer.html](help/primer.md) 
[/help/submission-policy.html](help/submission-policy.md) 
[/help/support.html](help/support.md) 
[/help/terms_of_submission.html](help/terms_of_submission.md) 
[/help/toc.html](help/toc.md) 

- [/help/whytex.html](help/whytex.md) fix link to [/help/textures](help/faq/textures.md)  (DONE)

- Broken images on [/help/withdraw.html](help/withdraw.md) (DONE)

- very broken: [/labs/showcase.html](labs/showcase.md) (DONE)

- Remove GZip help (DONE)

- Remove my.arxiv.org page. my.arxiv.org no longer exists  (DONE)
[/help/my_arxiv.html](help/my_arxiv.md)

- Images broken on [/help/orcid.html](help/orcid.md) (DONE)

- Are we trying to get TeX on this page on the subject heading "Notes on Note on La$\TeX$ accent commands" ? [/help/prep.html](help/prep.md) (I think it is correct so left as is. But pending feedback from Jake or Jim)

- Can probably get rid of this page: [/help/ssl.html](help/ssl.md) It's old news and standard practice.  (DONE)

- [/help/submit_index.html](help/submit_index.md) needs better title.  (DONE)


### TODO Fix titles of many pages  (DONE)
