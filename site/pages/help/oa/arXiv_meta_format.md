`arXiv` meta-data format
========================

**The Santa Fe Convention is discontinued. Please use the [Open Archives Initiative Protocol for Metadata Harvesting](http://www.openarchives.org/OAI/openarchivesprotocol.htm) instead.**

The arXiv Dienst interface implements this format in addition to other, standard formats to allow users to access unparsed and uninterpreted meta-data stored for arXiv records. We have adopted a simple XML transport similar to that used for OAMS meta-data.

For more details of Dienst and the Open Archives Initiative, see: [Open Archives Initiative and arXiv](index).

Syntax/Fields
-------------

The fields `Id`, `Title`, `Authors` and `Abstract` should always be present. Other fields are optional. No fields are repeated.

`Id`

The internal paper identifier without arXiv prefix or subject class

`Title`

Paper title

`Authors`

Authors and affiliations, usually a comma separated list with affiliations in parenthesis.

`Comments`

Free text comments

`Subj-class`

Subject class within the archive. Can a a semicolon separated list; first entry is primary subject class, other entries are cross lists.

`MSC-class`

Only present for paper in the math archive. MSC classifications (author supplied, not checked)

`Report-no`

Report number or numbers from author(s) institution(s).

`Journal-ref`

Should be a full bibliographic reference to a published version of the e-print

`Abstract`

Abstract, ideally in plain text but often with TeX/LaTeX code included

XML Transport
-------------

The general reply format is:
```xml
Content-type: text/xml

<?xml version="1.0" encoding="UTF-8"?>
 <Disseminate version="1.0">
  <arXiv:arXiv xmlns:arXiv="http://arXiv.org/help/oa/arXiv\_meta\_format">
    <arXiv:\_FIELD1\_>\_DATA1\_</arXiv:\_FIELD1\_>
    <arXiv:\_FIELD2\_>\_DATA2\_</arXiv:\_FIELD2\_>
    ...
  </arXiv:arXiv>
 </Disseminate>
```
Where `_FIELD#_` is the field name and `_DATA#_` is the value of that field. The fields are described above.

Example [https://arxiv.org/dienst/Repository/1.0/Disseminate/arXiv:math.CO/9901016/%23arXiv/xml](https://arxiv.org/dienst/Repository/1.0/Disseminate/arXiv:math.CO/9901016/%23arXiv/xml):  
```xml
Content-type: text/xml

<?xml version="1.0" encoding="UTF-8"?>
 <Disseminate version="1.0">
  <arXiv:arXiv xmlns:arXiv="http://arXiv.org/help/oa/arXiv\_meta\_format">
   <arXiv:Id>math/9901016</arXiv:Id>
   <arXiv:Title>Positivity for special cases of $(q,t)$-Kostka coefficients and standard
    tableaux statistics</arXiv:Title>
   <arXiv:Authors>Mike Zabrocki</arXiv:Authors>
   <arXiv:Comments>LaTEX, 37 pages, Replacement of submission with vertex operators only</arXiv:Comments>
   <arXiv:Subj-class>Combinatorics</arXiv:Subj-class>
   <arXiv:MSC-class>05E10</arXiv:MSC-class>
   <arXiv:Journal-ref>Electron. J. Combinat. 6, R41 (1999), 36pp.</arXiv:Journal-ref>
   <arXiv:Abstract>  We present two symmetric function operators $H\_3^{qt}$ and $H\_4^{qt}$ that
   have the property $H\_{3}^{qt} H\_{(2^a1^b)}\[X;q,t\] = H\_{(32^a1^b)}\[X;q,t\]$ and
   $H\_4^{qt} H\_{(2^a1^b)}\[X;q,t\] = H\_{(42^a1^b)}\[X;q,t\]$. These operators are
   generalizations of the analogous operator $H\_2^{qt}$ and also have expressions
   in terms of Hall-Littlewood vertex operators. We also discuss statistics,
   $a\_{\\mu}(T)$ and $b\_{\\mu}(T)$, on standard tableaux such that the $q,t$ Kostka
   polynomials are given by the sum over standard tableaux of shape $\\la$,
   $K\_{\\la\\mu}(q,t) = \\sum\_T t^{a\_{\\mu}(T)} q^{b\_{\\mu}(T)}$ for the case when when
   $\\mu$ is two columns or of the form $(32^a1^b)$ or $(42^a1^b)$. This provides
   proof of the positivity of the $(q,t)$-Kostka coefficients in the previously
   unknown cases of $K\_{\\la (32^a1^b)}(q,t)$ and $K\_{\\la (42^a1^b)}(q,t)$. The
   vertex operator formulas are used to give formulas for generating functions for
   classes of standard tableaux that generalize the case when $\\mu$ is two
   columns.</arXiv:Abstract>
  </arXiv:arXiv>
 </Disseminate>
```
