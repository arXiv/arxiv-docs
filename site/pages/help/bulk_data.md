arXiv Bulk Data Access
======================

We believe that *open access* should permit computation on collections
of articles as well as human access to individual articles, and that the
results of such computation will include better tools to find, browse,
use and assess articles. There are, however, practical and financial
constraints on the services we are able to offer for the arXiv
collection. We must balance the desire to promote research and
development based on the arXiv collection against these constraints.
Access mechanisms provided are grouped into metadata and full-text
services below.

Bulk Metadata Access
--------------------

#### OAI-PMH

arXiv supports the [OAI protocol for metadata harvesting](/help/oa)
(OAI-PMH) to provide access to metadata for all articles, updated daily
with new articles. This is the preferred way to bulk-download or keep an
up-to-date copy of arXiv metadata.

#### API

arXiv supports real-time programmatic access to metadata and our search
engine via the [arXiv API](/help/api/index). Results are returned using
the Atom XML format for easy integration with web services and toolkits.

#### RSS

arXiv provides [RSS feeds of new updates](rss.md) each day. These are
intended primarily for human consumption but do use well defined XML
formats and thus might be useful to machine applications.

Bulk Full-Text Access
---------------------

*Note: Most articles submitted to arXiv are submitted with the [default
arXiv
license](http://arxiv.org/licenses/nonexclusive-distrib/1.0/license.html)
which grants arXiv a perpetual, non-exclusive license to distribute the
article, but does not assign copyright to arXiv, nor grant arXiv the
right to grant any specific rights to others. We are thus unable to
grant others the right to distribute arXiv articles. If you build
indexes or tools based on the full-text, you must link back to arXiv for
downloads. A small fraction of submissions are made with [other
licenses](license.md) and this information is available in the
OAI-PMH metadata.*

#### KDD cup dataset

A sample of arXiv source files was collected in 2003 for the KDD cup
competition. This dataset may be [downloaded from the KDD cup
website](http://www.cs.cornell.edu/projects/kddcup/datasets.html). This
dataset also includes extracted citation data.

#### Amazon S3

For all articles the [processed PDF and source files available from
Amazon S3](bulk_data_s3.md). We recommend this method for bulk access to
the full-text of arXiv articles.
