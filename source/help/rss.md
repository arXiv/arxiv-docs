# RSS news feeds

Daily updated RSS news feed pages are available for all active subject
areas within arXiv. The URL for each category (whole archive or subject
class) is constructed by appending the category name to
`http://rss.arxiv.org/rss/`. For example, the URL for the RSS page for the
Computer Science archive is [http://rss.arxiv.org/rss/cs]().

News feeds are also available for individual subject classes of archives
that have subject classes. A specific subject class is selected by
appending a period (.) and the subject class letters to the URL. For
example, the URL for the RSS page for Mathematics -- Quantum Algebra is
[http://rss.arxiv.org/rss/math.QA]().

Please review the [Terms of Use for arXiv APIs](api/tou.md) before using the
arXiv RSS feeds.

### January 2024 update

Changes from the old RSS feed:

 - new base URL of rss.arxiv.org, instead of just arxiv.org (arxiv.org/rss will redirect to rss.arxiv.org)

 - status page at /feed/status

 - new content updated at arxiv midnight

 - categories are no longer case sensitive, cs.ai==cs.AI==CS.AI==CS.ai

 - can request multiple categories with + hep-lat+math.CO

 - limit of 2000 items
 
 - categorization and order of new, cross, replace and replace-cross now matches listings

 - An author list is now provided for each paper

The RSS output complies with the [RSS 2.0 specification](https://www.rssboard.org/rss-specification). RSS 0.91, and 1.0 are no longer supported. Atom format is still supported -- for example [http://rss.arxiv.org/atom/math]().

Looking for search results in an *RSS-like* format? See the [arXiv search
API](api/index.md) for more information and usage instructions.
