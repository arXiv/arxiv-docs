# Open Archives Initiative (OAI)

arXiv supports and participates in the [Open Archives Initiative](http://www.openarchives.org/) (OAI). arXiv is a registered OAI-PMH [data-provider](http://www.openarchives.org/Register/BrowseSites.pl) and provides metadata for all submissions which is updated each night shortly after new submissions are announced. Metadata for arXiv articles may be reused in non-commercial and commercial systems.

Please review the [Terms of Use for arXiv APIs](../../help/api/tou.md) before using the
arXiv OAI-PMH interface.

Notes for harvesters
--------------------

**Base URL**

arXiv supports [OAI\_PMH v2.0](http://www.openarchives.org/OAI/2.0/openarchivesprotocol.htm) at the baseURL [https://oaipmh.arxiv.org/oai?verb=Identify](https://oaipmh.arxiv.org/oai?verb=Identify).

**Identify response and policies**

Policy links and various other details are included in the [Identify](https://oaipmh.arxiv.org/oai?verb=Identify) response.

**Item = Article**

Each article in arXiv is modeled as an Item in the OAI-PMH interface. Only the most recent version of each article is exposed via this interface (some metadata formats include the version history).

**Metedata formats**

Metadata for each item (article) is available in several formats, all formats are supported for all articles. The available formats include:

*   `oai_dc` - Simple Dublin Core. See [example in `oai_dc` format](https://oaipmh.arxiv.org/oai?verb=GetRecord&identifier=oai:arXiv.org:0804.2273&metadataPrefix=oai_dc).
*   `arXiv` - arXiv specific metadata format which includes author names separated out, category and license information. See [example in `arXiv` format](https://oaipmh.arxiv.org/oai?verb=GetRecord&identifier=oai:arXiv.org:0804.2273&metadataPrefix=arXiv).
*   `arXivRaw` - arXiv specific metadata format which is very close the internal format stored at arXiv. Includes version history. See [example in `arXivRaw` format](https://oaipmh.arxiv.org/oai?verb=GetRecord&identifier=oai:arXiv.org:0804.2273&metadataPrefix=arXivRaw).

You may request a list of all the metadata formats supported with the [ListMetadataFormats](https://oaipmh.arxiv.org/oai?verb=ListMetadataFormats) verb.

**Datestamps**

Every OAI-PMH metadata record has a [`datestamp`](http://www.openarchives.org/OAI/2.0/openarchivesprotocol.htm#Datestamp) associated with it, which is the last modification time of that record. Because arXiv has updated metadata records in bulk on several occasions, the OAI-PMH `datestamp` values do not correspond with the original submission or replacement times for older articles, and may not for newer articles because of administrative and bibliographic updates. The earliest datestamp is given then the `<earliestDatestamp>` element of the [Identify](http://oaipmh.arxiv.org/oai?verb=Identify) response.

_The OAI-PMH interface does not support selective harvesting based on submission date. The datestamps are designed to support incremental harvesting of updates on an ongoing basis. It is not possible to selectively harvest only, say, articles submitted in February 2001._ Except for selective harvesting based on subject areas (see description of Sets below) the interface is designed to support copying and synchronization of a complete set of arXiv metadata. In order to harvest metadata for all articles, either make requests without a datestamp range (recommended), or make requests from the `<earliestDatestamp>` through to the present (but beware that because of bulk updates there are some dates on which there were large numbers of updates).

Once an initial harvest has been completed, the copy may be maintained by making incremental harvesting requests with the `from` date set to the date of last harvest (`from` is best taken from the last server response; don't set the `until` date).

**Sets**
Specific categories, archives, and groups are available for selective harvesting. Archives are subsets of groups and categories are subsets of archives. This means that a single catgory can be selected for harvesting with the set `cs:cs:AI`, a whole archive with the set `physics:hep-th`, or all physics archives with the set `physics`. Alternatively all of arXiv can be harvested by not specifying a `setSpec`. You may request a list of all the sets supported with the [ListSets](https://oaipmh.arxiv.org/oai?verb=ListSets) verb.

**Update schedule**

New papers are accepted daily and metadata is made available via the OAI-PMH interface once they are announced, typically around 10:30pm EST Sunday through Thursday. Occasional small changes to paper data may happen intermittently throughout the day. 

### Chronology
March 2025
A total rewrite of the system.

Major differences:
*   base URL  updated from `http://export.arxiv.org/oai2` to `https://oaipmh.arxiv.org/oai`
*   Earliest start date: from 2007-05-23 to 2005-09-16
	*   All papers modified before 2005 are now included, but all share the same earliest modified date
*   Change to historical modified dates for a small number of papers
*   Set expansion
	*    The set structure has become more precise to include group, archive, and category specification
	*   All previous set memberships are still valid, but sets can be requested and will be identified more specifically now
	*   Follows structure group:archive:CATEGORY Example math:math:NA or physics:hep-lat
	*   Full list can be found at [ListSets](https://oaipmh.arxiv.org/oai?verb=ListSets)
    
Minor differences:
*   Papers in alias categories included in both sets
*   Resumption token no long counts total items in list, or cursor. Expires daily
*   Increased limit on results
*   Source flags appear more consistently in arXivRaw format
*   Change in order of record items to match schema

12 April 2007

The arXiv OAI baseURL changed to `http://export.arxiv.org/oai2` from `http://arxiv.org/oai2`. The old URL will issue a redirect for some time but please update your harvester to use the new baseURL.

1 April 2007

Support for the long-deprecated [OAI\_PMH v1.1](http://www.openarchives.org/OAI/2.0/openarchivesprotocol.htm) at baseURL `http://arXiv.org/oai1` has been discontinued. Please use our v2.0 interface instead.

29 December 2006

arXiv Dienst interface disabled. The Dienst protocol was replaced by the OAI-PMH and arXiv's interface hasn't been used regularly by any service for a few years and not at all in the last few months.

2 July 2003

[Open Archives Initiative Protocol for Metadata Harvester v2.0](http://www.openarchives.org/OAI/2.0/openarchivesprotocol.htm) is released. arXiv supports both OAI-PMH v1.1 and v2.0; v1.1 is deprecated.

20 June 2001

Minor update of the OAI protocol to follow changes in the XML Schema specification, arXiv updated to support [OAI-PMH v1.1](http://www.openarchives.org/OAI/1.1/openarchivesprotocol.htm).

21 January 2001

[Open Archives Initiative Protocol for Metadata Harvester v1.0](http://www.openarchives.org/OAI/1.0/openarchivesprotocol.htm) released, the Santa Fe Convention is discontinued. See [OAI website](http://www.openarchives.org/) for details of the latest protocol.

15 February 2000

[The Santa Fe Convention](http://www.openarchives.org/sfc/sfc_entry.htm) officially released, arXiv is compliant.

27 January 2000

arXiv Dienst implementation for Santa Fe Convention compliance announced to participants in the Open Archives initiative.

21-22 October 1999

[The Santa Fe Convention](http://www.openarchives.org/sfc/sfc_entry.htm) was the result of a meeting of the Open Archives initiative held in Santa Fe, New Mexico, USA.
