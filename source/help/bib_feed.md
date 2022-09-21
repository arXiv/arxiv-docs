Automated DOI and journal reference updates from publishers
===========================================================

arXiv collaborates with Inspire (formerly SPIRES) to automatically
update arXiv metadata with the DOI and journal references of published
versions. In 2006 this facility was extended to accept feeds of DOI and
journal reference metadata associated with arXiv articles from
publishers and other trusted parties. We believe that linkage between
arXiv and publisher versions of articles is of benefit to both arXiv
users and publishers. Prospective users should contact arXiv
administrators to discuss possible use of this facility, *after* making 
the XML feed available on their site for ingestion. 

DOI and journal reference update data format
--------------------------------------------

The update information uses a simple XML format to convey DOI and/or
journal reference information for a published version of the arXiv
article. The XML should use the following schema:

-   <http://arxiv.org/schemas/doi_feed.xsd>

and there are some example documents are at:

-   <http://arxiv.org/schemas/doi_feed_test.xml>
-   <http://arxiv.org/schemas/doi_feed_test2.xml>
-   <http://arxiv.org/schemas/doi_feed_test3.xml>

The body of the feed comprises `<article>` elements which must have a
`preprint_id` attribute and either of both of the `doi` or `journal_ref`
attributes:

-   `preprint_id` - The identifier of the arXiv article that the `doi`
    and/or `journal_ref` are associated with (e.g. `arXiv:1212.1212` or
    `arXiv:hep-th/9901001`).
-   `doi` - One or more DOIs associated with the article. Multiple DOIs
    should be separated with spaces. There is no facility to qualify one
    as the main article and another as an erratum or such hut it is
    helpful is the main article DOI is first (e.g.
    `10.1016/S0550-3213(01)00405-9`, see also [DOI metadata
    notes](prep.md#doi)).
-   `journal_ref` - One or more full bibliographic references to a
    published version of the article. Multiple references should be
    separated with a semi-colon and a space. Addition human-readable
    qualifiers such as "Erratum" may be used (e.g.
    `Phys.Lett. B541 (2002) 273-280; Erratum-ibid. B562 (2003) 367`, see
    also [journal reference metadata notes](prep.md#journal)).

The XML format has a few historical oddities. The `identifier` attribute
on the root element is used to check that we have the feed we expect and
so should not change for a given publisher/source. The contents of the
`<date>` element are not used during updates. It is useful for human
debugging however, and should be set to the date the feed was generated.

Update protocol
---------------

After establishing that an update source has reliable and correctly
formatted metadata we usually arrange to poll a particular URL on a
weekly or monthly schedule. Updates that appear in more than one polling
are ignored. For very small feeds (up to 1000 entries say) it is
reasonable to simply append to a growing list of updates. For most feeds
only recent updates should be included. We recommend that two
polling-periods worth of updates are included so that updates won't be
missed if something goes awry with one polling cycle.

Problems, errors...
-------------------

Updates are automatic so it is vital that feeds contain reliable data.
Details of errors or other problem should be communicated to arXiv
administrators as soon as possible.
