RSS news feeds for arXiv updates
================================

Daily updated RSS news feed pages are available for all active subject
areas within arXiv. The URL for each category (whole archive or subject
class) is constructed by appending the category name to
`http://arxiv.org/rss/`. For example, the URL for the RSS page for the
Computer Science archive is `http://arxiv.org/rss/cs`.

News feeds are also available for individual subject classes of archives
that have subject classes. A specific subject class is selected by
appending a period (.) and the subject class letters to the URL. For
example, the URL for the RSS page for Mathematics -- Quantum Algebra is
`http://arxiv.org/rss/math.QA`.

Please review the [Terms of Use for arXiv APIs](api/tou.md) before using the
arXiv RSS feeds.

### Customization

By default arXiv links within the RSS pages are to the main site. You
may optionally specify a parameter `mirror=fr`, where `fr` is the
country code of the mirror links should point to (France, `fr.arxiv.org`
in this case). The complete URL thus becomes
`http://arxiv.org/rss/cs?mirror=fr`.

By default the RSS output complies with the [RSS 1.0
specification](http://web.resource.org/rss/1.0/). The optional `version`
parameter may be used to specify alternate RSS versions. Versions
[0.91](http://backend.userland.com/rss091),
[1.0](http://web.resource.org/rss/1.0/), and
[2.0](http://blogs.law.harvard.edu/tech/rss) are supported. This
parameter may be combined with the `mirror` parameter. For example,
`http://arxiv.org/rss/cs?mirror=fr&version=0.91` requests RSS version
0.91 output with links to the French mirror.

Looking for search results in an *RSS-like* format? See the [arXiv search 
API](api/index.md) for more information and usage instructions.