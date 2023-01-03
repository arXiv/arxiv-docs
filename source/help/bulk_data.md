# arXiv Bulk Data Access


We believe that *open access* should permit computation on collections
of articles as well as human access to individual articles, and that the
results of such computation will include better tools to find, browse,
use and assess articles. There are, however, practical and financial
constraints on the services we are able to offer for the arXiv
collection. We must balance the desire to promote research and
development based on the arXiv collection against these constraints.
Access mechanisms provided are grouped into metadata and full-text
services below.

Please review the [Terms of Use for arXiv APIs](api/tou.md) before using any of
the access options below.

## Bulk Metadata Access


### OAI-PMH

arXiv supports the [OAI protocol for metadata harvesting](oa/index.md)
(OAI-PMH) to provide access to metadata for all articles, updated daily
with new articles. This is the preferred way to bulk-download or keep an
up-to-date copy of arXiv metadata.

### API

arXiv supports real-time programmatic access to metadata and our search
engine via the [arXiv API](api/index.md). Results are returned using
the Atom XML format for easy integration with web services and toolkits.

### RSS

arXiv provides [RSS feeds of new updates](rss.md) each day. These are
intended primarily for human consumption but do use well defined XML
formats and thus might be useful to machine applications.

## Bulk Full-Text Access

*Note: Most articles submitted to arXiv are submitted with the [default
arXiv
license](http://arxiv.org/licenses/nonexclusive-distrib/1.0/license.html)
which grants arXiv a perpetual, non-exclusive license to distribute the
article, but does not assign copyright to arXiv, nor grant arXiv the
right to grant any specific rights to others. We are thus unable to
grant others the right to distribute arXiv articles. If you build
indexes or tools based on the full-text, you must link back to arXiv for
downloads. A small fraction of submissions are made with [other
licenses](license/index.md) and this information is available in the
OAI-PMH metadata.*

### Kaggle - Full Text
The full, machine-readable arXiv dataset is [available on Kaggle](https://www.kaggle.com/Cornell-University/arxiv). This includes all available articles and related features such as article titles, authors, categories, abstracts, full text PDFs, and more.


### Amazon S3 - Full Text

For all available articles the processed PDF and source files are [available from Amazon S3](bulk_data_s3.md). 

### KDD cup dataset

A sample of arXiv source files was collected in 2003 for the KDD cup
competition. This dataset may be [downloaded from the KDD cup
website](http://www.cs.cornell.edu/projects/kddcup/datasets.html). This
dataset also includes extracted citation data.

<span id="harvest"></span>
### Custom Programmatic Harvesting 
----------------------------------

As stated on our [robots](robots.md) page, arXiv has limited server capacity 
and our first priority is to support interactive use by human users. That said, 
we are plainly aware that interested parties will want to make use of our corpus.

### Play nice

We ask that users intent on harvesting use the dedicated site `export.arxiv.org` 
for these purposes, which contains an up-to-date copy of the corpus and is specifically 
set aside for programmatic access. This will mitigate impact on readers who are
using the main site interactively.  

There are many users who want to make use of our data, and millions of distinct 
URLs behind our site. If everyone were to crawl the site at once without regard
to a reasonable request rate, the site could be dragged down and unusable. 
For these purposes we suggest that a *reasonable rate* to be bursts
at 4 requests per second with a 1 second `sleep`, per burst.

### Consider the impact

arXiv already operates with limited resources, and mindlessly downloading 
all of the URLs of this site will return terabytes of data. This represents
both a [financial burden](../about/give.md) to arXiv, as well as a practical 
problem for the unwary. 

*Please do not attempt to download the complete corpus programmatically.* 
The [Amazon S3](bulk_data_s3.md) buckets are the accepted mechanism to download 
the complete corpus, but you are welcome to "play catch-up" programmatically
between updates of the buckets.

