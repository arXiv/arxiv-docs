Institutional Repository (IR) Interoperability
==============================================

arXiv places no restrictions on whether articles also appear in local
institutional repositories. Authors are welcome to download copies of
their own articles from arXiv in order to submit to a local repository.
This page describes ways in which institutional repository managers may
approach finding and copying local researchers' content from arXiv.

Copying content from arXiv to an IR
-----------------------------------

Some institutions require or request that copies of articles written by
their researchers are deposited in their local institutional repository
in addition to arXiv. Everything necessary to pull complete metadata and
fulltext from arXiv is available. However, the usual sticking point is
the permission required to copy the fulltext into the institutional
repository: arXiv does not have the right to grant such permission so in
the general case permission must be obtained from the article authors.
Obtaining permission from the article authors may not be necessary if:

1.  there is a license permitting such copying associated with the
    article. The [default arXiv
    license](http://arxiv.org/licenses/nonexclusive-distrib/1.0/) simply
    grants arXiv the right to distribute the article but does not
    authorize reposting in another repository. Licenses such as the
    Creative Commons Attribution license (CC BY) or the Public Domain
    Dedication do permit such reposting (see [arXiv License
    Information](/help/license/index.md) for information about licenses
    supported).
2.  there is some local rule or law that permits copying local
    researchers' articles into an institutional repository.

### Procedure

We will consider the article [arXiv:1410.6579](https://arxiv.org/abs/1410.6579) as an
example.

#### Step 1 - Get metadata

Metadata from arXiv is available via our [OAI-PMH interface](/help/oa/index.md),
the URI for different metadata formats is constructed based on the
article identifier. For example, to get `oai_dc` metadata the request
is:

`http://export.arxiv.org/oai2?verb=GetRecord&identifier=oai:arXiv.org:1410.6579&metadataPrefix=oai_dc`

or to get `arXiv` format metadata, which has the license information
expressed as a URI, the request is:

`http://export.arxiv.org/oai2?verb=GetRecord&identifier=oai:arXiv.org:1410.6579&metadataPrefix=arXiv`

#### Step 2 - Check the license

In the case of arXiv:1410.6579 the license is the [Creative Commons
Public Domain
Dedication](http://creativecommons.org/licenses/publicdomain/) which is
represented in the `arXiv` format metadata as:

    ...
      <license>http://creativecommons.org/licenses/publicdomain/</license>
    ...

The Public Domain Dedication allows and article to be copied to another
repository without the need to ask for permission. Most submissions to
arXiv use the default license however, expressed with the URI:

     
    ...
      <license>http://arxiv.org/licenses/nonexclusive-distrib/1.0/</license>
    ...

In these cases it is necessary to obtain permission from the article
authors before the article may be copied to another repository.

#### Step 3 - Copy the PDF and/or source files

In the case of arXiv:1410.6579 the submission was in PDF format and the
URI to download it is:

-   PDF: <http://arxiv.org/pdf/1410.6579>

In all cases links to the processed and the source files (where the
submission is in TeX format) are provided on the normal abstract page
(e.g. [arXiv:1306.1073](https://arxiv.org/abs/1306.1073)), they may also be constructed
from the article identifier.

-   PDF: <http://arxiv.org/pdf/1306.1073>
-   Source: <http://arxiv.org/src/1306.1073>

See [arXiv identifier scheme - information for interacting
services](/help/arxiv_identifier_for_services.md) and [Media types
delivered by arXiv](/help/mimetypes.md) for further technical details.

If you want to download just a few articles then there should be no
problem provided a useful [User-Agent
string](https://tools.ietf.org/html/rfc7231#section-5.5.3) is sent in
the HTTP requests, or if requests are made manually through a normal web
browser. If you would like to download a significant number of articles
then accesses should be spaced by at least 3 seconds to avoid our
denial-of-service attack detector cutting off access, please contact
[arXiv support](/help/support.md) if you intend to download more than a
thousand articles.

Identifying articles by your institution's researchers
------------------------------------------------------

Unfortunately, most arXiv articles do not have any affiliation
information included by submitters, and when it is present there is wide
variation in the writing of institution names which makes matching
difficult. However, arXiv does maintain [authority
records](/help/authority.md) linking articles to author accounts. This
linkage is automatic for the submitting author but co-authors must
claim-ownership after announcement in order to be linked. Additionally,
user accounts may be linked with [ORCID iDs](/help/orcid.md) and then a
public display of all arXiv articles linked to that ORCID iD is
available on arXiv in both human an machine-readable forms. With these
linkages in place, if you know the ORCID iDs of your institutions'
researchers it is then possible to find all their articles on arXiv.

The ability to link arXiv accounts with [ORCID iDs](/help/orcid.md) was
introduced in early 2015 and we suggest that institutions interested in
identifying articles by their researchers encourage both claiming
article ownership and ORCID iD linkage.

### Example

Consider the article [arXiv:1505.00009](https://arxiv.org/abs/1505.00009) which was
submitted by first author Jonathan Heckman. Ownership was later claimed
by co-author David R. Morrison who has also associated his ORCID iD with
his arXiv account. If staff at UC Santa Barbara (UCSB), where David R.
Morrison is faculty, wanted to find papers on arXiv but UCSB researchers
they could query based on ORCID iDs. David's ORCID iD is
<http://orcid.org/0000-0001-6286-1277> and one can query arXiv using a
URI of the form `http://arxiv.org/a/ORCID`, putting either the full URI
or just the 16-digit part of the ORCID iD in place of `ORCID`, e.g.:

`http://arxiv.org/a/http://orcid.org/0000-0001-6286-1277`

or

`http://arxiv.org/a/0000-0001-6286-1277`

If accessed in a web browser these URIs return HTML pages. It is
possible to request a machine-readable form either by explicitly
appending `.atom` or `.atom2` (see [Author
Identifiers](/help/author_identifiers.md) for details of the two Atom
formats), e.g.

`http://arxiv.org/a/http://orcid.org/0000-0001-6286-1277.atom2`

or using [HTTP content
negotiation](https://en.wikipedia.org/wiki/Content_negotiation) with the
header `Accept: application/atom+xml`, e.g.

    $ curl -L --header "Accept: application/atom+xml" http://arxiv.org/a/0000-0001-6286-1277
    <?xml version="1.0" encoding="UTF-8"?>
    <feed xmlns="http://www.w3.org/2005/Atom">
      <title>David R. Morrison's articles on arXiv</title>
      <link rel="describes" href="http://orcid.org/0000-0001-6286-1277"/>
      <updated>2015-09-23T00:00:00-04:00</updated>
      <id>http://arxiv.org/a/morrison_d_1</id>
      <link href="http://arxiv.org/a/morrison_d_1.atom2" rel="self" type="application/atom+xml"/>
      <link rel="describes" href="http://arxiv.org/a/morrison_d_1"/>
      <entry>
        <id>http://arxiv.org/abs/1507.05965v2</id>
        <updated>2015-09-23T08:31:55-04:00</updated>
        <published>2015-07-21T16:00:43-04:00</published>
        <title>On Gauge Enhancement and Singular Limits in $G_2$ Compactifications of M-theory</title>
        ...
      </entry>
      ...
    </feed>

An attempt to request information for an ORCID that does not exist or is
not linked to an arXiv account will result in an HTTP 404 Not Found
response, e.g.:

`http://arxiv.org/a/http://orcid.org/0123-0123-0123-0123.atom`
