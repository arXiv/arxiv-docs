Automated DOI and journal reference updates from publishers
===========================================================

arXiv believes that linkage between arXiv and publisher versions of articles benefits the community. To facilitate this, we accept feeds of DOI and journal reference metadata from publishers and other trusted third-parties. Organizations that are interested in providing a feed to arXiv should contact us through our [user support portal](https://arxiv-org.atlassian.net/servicedesk/customer/portal/1)

DOI and journal reference update data format
--------------------------------------------

The metadata feeds use a simple XML format to convey DOI and/or journal reference information for a published version of the arXiv article. The XML should use the following schema:


-   <http://arxiv.org/schemas/doi_feed.xsd>

Please view example documents at:

-   <http://arxiv.org/schemas/doi_feed_test.xml>
-   <http://arxiv.org/schemas/doi_feed_test2.xml>
-   <http://arxiv.org/schemas/doi_feed_test3.xml>

The body of the feed comprises `<article>` elements which must have a
`preprint_id` attribute and either one or both  `doi` and `journal_ref`
attributes:

-   `preprint_id` - The identifier of the arXiv article that the `doi`
    and/or `journal_ref` are associated with (e.g. `arXiv:1212.1212` or
    `arXiv:hep-th/9901001`).
-   `doi` - One or more DOIs associated with the article. Multiple DOIs
    should be separated with spaces. There is no facility to qualify one
    as the main article and another as an erratum or such but it is
    helpful to list the main article DOI first (e.g.
    `10.1016/S0550-3213(01)00405-9`, see also [DOI metadata
    notes](prep.md#doi)).
-   `journal_ref` - One or more full bibliographic references to a
    published version of the article. Multiple references should be
    separated with a semicolon and a space. Additional human-readable
    qualifiers such as "Erratum" may be used (e.g.
    `Phys.Lett. B541 (2002) 273-280; Erratum-ibid. B562 (2003) 367`, see
    also [journal reference metadata notes](prep.md#journal)).

-   The XML format has a few historical irregularities. The `identifier` attribute
on the root element is used to check we have the feed we expect and should not change for a given publisher/source.
-   The contents of the `<date>` element are not used during updates. It is useful for human
debugging however, and should be set to the date the feed was generated.

Update protocol
---------------

After establishing that an update source has reliable and correctly formatted metadata we arrange to poll a particular URL on a weekly or monthly schedule. Updates that appear in more than one polling are ignored. For very small feeds (up to 1,000 entries) it is reasonable to simply append them to a growing list of updates. For most feeds only recent updates should be included. We recommend that two polling periods worth of updates are included so that updates won't be missed if something goes wrong with one of the polling cycles.


Problems or errors
-------------------

Updates are automatic so it is important that feeds contain reliable data.
Details of errors or other problems should be [communicated to arXiv
administrators](../help/contact.md) as soon as possible. 
