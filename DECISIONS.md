# Decisions log

## 2022-10-01 move away from arxiv-marxdown
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

To acheive the use of the arxiv-base header and footer in a static
site is to have a click flask app that can be run to create a template
with a header and footer for the static site generator. Then a static
site generator can provide 80% of the benefits of arxiv-marxdown. An
example of this is in `prep_for_mkdocs.sh`
