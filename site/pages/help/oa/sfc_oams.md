   the Santa Fe Convention: the Open Archives Metadata Set

[![the Open Archives home page](http://www.openarchives.org/images/OA50.gif)](http://www.openarchives.org)

**[the Santa Fe Convention](http://www.openarchives.org/sfc/sfc_entry.htm) :** **The Open Archives Metadata Set**

**The Santa Fe Convention is discontinued. Please use the [Open Archives Initiative Protocol for Metadata Harvesting](http://www.openarchives.org/OAI/openarchivesprotocol.htm) instead.**

*   [Introduction](#oamsintro)
*   [Description of the semantics of the Open Archives Metadata Set](#oamsseman)
*   [XML DTD for the Open Archives Metadata Set](#oamsdtd)
*   [A sample record expressed according to the Open Archives Metadata Set XML DTD](#oamsrec)

<a name="oamsintro"></a>
Introduction
------------

The Santa Fe Convention provides recommendations for interoperability among archives.  Archives provide access to _records_.  The word _document_ is purposely avoided and the notion of a _record_ is purposely imprecise. Some archives may just provide access to metadata, others may also provide access to metadata and full content in some form, others may provide other services associated with the metadata and content such as access to the full content in various manifestations (formats) or structural decompositions (e.g., individual pages, chapters, and the like).

This document describes the elements of the Open Archives Metadata Set (OAMS).  The semantics of this set has purposely been kept simple in the interest of easy creation and widest applicability.  The expectation is that individual archives will maintain metadata with more expressive semantics and the [Open Archives Dienst Subset](http://www.cs.cornell.edu/cdlrg/dienst/Protocols/OpenArchivesDienst.htm) provides the mechanism for retrieval of this richer metadata.

Notes on the remainder of this document:

*   The transfer syntax of the OAMS is XML.  A DTD is given at the [end](#oamsdtd) of this document.
    
*   The semantics of the OAMS could be expressed using [Dublin Core Element Set](http://purl.org/DC/), with some qualification of those elements.  Where the semantics of an element in the OAMS exactly matches that of one in the Dublin Core Metadata Element Set, the definition of the Dublin Core element has been used.
    
*   Except where noted, values for elements are unformatted strings.
    
*   All dates in OAMS are encoded using the "[Complete date" variant of ISO8601](http://www.w3.org/TR/NOTE-datetime).  This format is CCYY-MM-DD where CC is the century, YY is the year, MM is the month of the year between 01 (January) and 12 (December), and DD is the day of the month between 01 and 28 or 29 or 30 or 31, depending on length of month and whether it is a leap year.
    
*   Elements that are mandatory are annotated with a \[M\]. 
*   Elements that are optional are annotated with a \[O\]. 
*   Elements that are repeatable are annotated with a \[R\].  Note that the fact that an element may be repeated implies that multiple values should not be associated with a single element (e.g.,  associating multiple authors with a single Author tag).

<a name="oamsseman"></a>
Description of the semantics of the Open Archives Metadata Set
--------------------------------------------------------------

### Title \[M\]

A name given to the record.

### Date of Accession \[M\]

The date when the record was entered into the archive.  It is assumed that in most cases this date will be created automatically by the archive rather than entered by a human user.  

### Display ID \[O\] \[R\]

A URL (Universal Resource Location) identifying a human readable page that provides access to the possible manifestations (e.g., PostScript, TeX) of the record.  For archives that have only one manifestation per record, this URL may point to that single manifestation.

### Full ID \[M\]

The full identifier for a record in an archive.  This full identifier is the concatenation of the following components:

1.  A unique archive identifier consisting only of alphanumerical characters \[a-z, A-Z, 0-9\]. Registration of this identifier is part of the Open Archives registration process for data providers, described in [Step 6](http://www.openarchives.org/sfc/sfc.htm#provider6) of [the core document of the Santa Fe Convention](http://www.openarchives.org/sfc/sfc.htm).
    
2.  Any printable non-alphanumeric character that will act as a delimiter (e.g., / : #)
    
3.  An identifier for the record that is unique within the archive.
    

The combination of these components produces a globally unique full identifier for each record in the nature of a URN.  An example of a Full ID is archive11/xxx4.

### Author \[M\] \[R\]

The author or corporate author who is responsible for creating the intellectual content of the record.  Each author may also have an optional institution affiliation. 

### Abstract \[O\]

Text summarizing the contents of the record.

### Subject \[O\] \[R\]

The topic of the content of the record expressed as keywords, key phrases or classification codes.

### Comment \[O\] \[R\]

A free-text value that contains information outside the scope of other defined elements that adds to the discoverability of the record.

### Date for Discovery \[O\] \[R\]

A date relevant to the record that may aid the user trying to find the document.  A common example of such a date would be an original publication date of a record that was placed in an archive at a later time (i.e., its date of accession is later than its date of publication).  

* * *
<a name=oamsdtd"></a>
XML DTD for the Open Archives Metadata Set
------------------------------------------

The plain text DTD file can be retrieved [here](http://www.openarchives.org/sfc/oams.dtd). The OAMS DTD can be embedded in a larger DTD.
```xml
<!-- Open Archives Metadata Set (OAMS) -->
<!-- This DTD can be used to represent the elements of the
Open Archives Metadata Set-->
<!-- Version 0.2, Mark Doyle Dec 27, 1999 -->
<!-- Dates are to be in encoded using the "Complete Date" variant of
ISO8601-->
<!ENTITY % doctype "oams">
<!ELEMENT %doctype; (title, accession, displayId\*, fullId, author+,
abstract?,subject\*,comment\*,discovery)>
<!ELEMENT title (#PCDATA)>
<!ELEMENT accession EMPTY>
<!ATTLIST accession date CDATA #REQUIRED>
<!ELEMENT displayId (#PCDATA)>
<!ELEMENT fullId (#PCDATA)>
<!ELEMENT author (name,organization\*)>
<!ELEMENT name (#PCDATA)>
<!ELEMENT organization (#PCDATA)>
<!ELEMENT abstract (#PCDATA)>
<!ELEMENT subject (#PCDATA)>
<!ELEMENT comment (#PCDATA)>
<!ELEMENT discovery EMPTY>
<!ATTLIST discovery date CDATA #REQUIRED>
<!-- ENTITY sets - lifted from MathML DTD -->
<!-- ISO 9573-13 -->
<!ENTITY % ent-isoamsa SYSTEM "isoamsa.ent" >
%ent-isoamsa;
<!ENTITY % ent-isoamsb SYSTEM "isoamsb.ent" >
%ent-isoamsb;
<!ENTITY % ent-isoamsc SYSTEM "isoamsc.ent" >
%ent-isoamsc;
<!ENTITY % ent-isoamsn SYSTEM "isoamsn.ent" >
%ent-isoamsn;
<!ENTITY % ent-isoamso SYSTEM "isoamso.ent" >
%ent-isoamso;
<!ENTITY % ent-isoamsr SYSTEM "isoamsr.ent" >
%ent-isoamsr;
<!ENTITY % ent-isogrk3 SYSTEM "isogrk3.ent" >
%ent-isogrk3;
<!ENTITY % ent-isogrk4 SYSTEM "isogrk4.ent" >
%ent-isogrk4;
<!ENTITY % ent-isomfrk SYSTEM "isomfrk.ent" >
%ent-isomfrk;
<!ENTITY % ent-isomopf SYSTEM "isomopf.ent" >
%ent-isomopf;
<!ENTITY % ent-isomscr SYSTEM "isomscr.ent" >
%ent-isomscr;
<!ENTITY % ent-isotech SYSTEM "isotech.ent" >
%ent-isotech;
<!-- ISO 8879 -->
<!ENTITY % ent-isobox SYSTEM "isobox.ent" >
%ent-isobox;
<!ENTITY % ent-isocyr1 SYSTEM "isocyr1.ent" >
%ent-isocyr1;
<!ENTITY % ent-isocyr2 SYSTEM "isocyr2.ent" >
%ent-isocyr2;
<!ENTITY % ent-isodia SYSTEM "isodia.ent" >
%ent-isodia;
<!ENTITY % ent-isogrk1 SYSTEM "isogrk1.ent" >
%ent-isogrk1;
<!ENTITY % ent-isogrk2 SYSTEM "isogrk2.ent" >
%ent-isogrk2;
<!ENTITY % ent-isolat1 SYSTEM "isolat1.ent" >
%ent-isolat1;
<!ENTITY % ent-isolat2 SYSTEM "isolat2.ent" >
%ent-isolat2;
<!ENTITY % ent-isonum SYSTEM "isonum.ent" >
%ent-isonum;
<!ENTITY % ent-isopub SYSTEM "isopub.ent" >
%ent-isopub;
<!-- MathML aliases for characters defined above -->
<!ENTITY % ent-mmlalias SYSTEM "mmlalias.ent" >
%ent-mmlalias;
<!-- MathML new characters -->
<!ENTITY % ent-mmlextra SYSTEM "mmlextra.ent" >
%ent-mmlextra;
<!-- end of ENTITY sets --> 
```
* * *
<a name="oamsrec"></a>
A sample record expressed according to the Open Archives Metadata Set XML DTD
-----------------------------------------------------------------------------

The plain text sample record can be retrieved [here](http://www.openarchives.org/sfc/oams_rec.txt).
```xml
<?xml version="1.0"?>
<!DOCTYPE oams SYSTEM "oams.dtd">
<oams xmlns='http://www.openarchives.org/sfc/sfc\_oams.htm'>
<title>Dilaton Contact Terms in the Bosonic and Heterotic
Strings</title>
<accession date="1992-01-30"/>
<displayId>http://arXiv.org/abs/hep-th/9201076</displayId>
<fullId>arXiv:hep-th/9201076</fullId>
<author><name>Mark Doyle</name><organization>Princeton University</organization></author>
<abstract>Dilaton contact terms in the bosonic and heterotic strings are examined following the recent work of Distler and Nelson on the bosonic and semirigid strings. In the bosonic case dilaton two-point functions on the sphere are calculated as a stepping stone to constructing a good coordinate family for dilaton calculations on higher genus surfaces. It is found that dilaton-dilaton contact terms are improperly normalized, suggesting that the interpretation of the
dilaton as the first variation of string coupling breaks down when other dilatons are present. It seems likely that this can be attributed to the tachyon divergence found in Ref 1. For the heterotic case, it is found that there is no tachyon divergence and that the dilaton contact terms are properly normalized. Thus, a dilaton equation analogous to the one in topological gravity is derived and the interpretation of the dilaton as the string coupling constant goes through.</abstract>
<subject>High Energy Physics - Theory</subject>
<comment>Journal-ref: Nucl. Phys. B381 (1992) 158-200</comment>
<discovery date="1999-12-06"/>
</oams> 
```
* * *

### Supporting information is available at:

*   [the Santa Fe Convention](http://www.openarchives.org/sfc/sfc_entry.htm)
*   the [core document of the Santa Fe Convention](http://www.openarchives.org/sfc/sfc.htm)
*   the [Open Archives Metadata Set](http://www.openarchives.org/sfc/sfc_oams.htm)
*   the [Open Archives Dienst Subset](http://www.openarchives.org/sfc/sfc_dienst.htm)
*   [the list of Open Archives data providers](http://www.openarchives.org/sfc/sfc_archives.htm), including their unique archive identifiers
*   [the list of Open Archives service providers](http://www.openarchives.org/sfc/sfc_services.htm)
*   [the list of metadata formats](http://www.openarchives.org/sfc/sfc_metadata.htm) used in the Open Archives context
*   the [template to be used by data providers](http://www.openarchives.org/sfc/data_provider_template.htm) to register as a Santa Fe compliant archive
*   the [template to be used by service providers](http://www.openarchives.org/sfc/service_provider_template.htm) to register as a Santa Fe compliant service

 

\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

[![the Open Archives home page](http://www.openarchives.org/images/OA50.gif)](http://www.openarchives.org)

_get in touch with the Open Archives initiative by contacting [openarchives@openarchives.org](mailto:openarchives@openarchives.org)_

 

_last updated January 17th 2000_
