arXiv identifier scheme - information for interacting services
==============================================================

The form of arXiv identifiers for new articles changed on 1 April 2007,
and the number of digits in the sequence number changed again on 1
January 2015. All existing articles retain their identifiers. See
<http://arxiv.org/help/arxiv_identifier> for details of the external
appearance. This document details changes in our internal metadata
formats and policies associated with the identifier changes.

The table below shows the correspondence between old and new identifier
forms, internal and external identifiers, and semantics that can and
cannot be derived from the identifier:

<table>
<thead>
<tr class="header">
<th> </th>
<th>Internal identifier</th>
<th>Preferred external<br />
identifier</th>
<th>Year</th>
<th>Month</th>
<th>Version</th>
<th>Original primary<br />
classification</th>
<th>Primary classification</th>
<th>Secondary classification</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>Old scheme</td>
<td>hep-th/9901001<br />
hep-th/9901001v1<br />
math.CA/0611800v2</td>
<td>arXiv:hep-th/9901001<br />
arXiv:hep-th/9901001v1<br />
arXiv:math/0611800v2</td>
<td>1999<br />
1999<br />
2006</td>
<td>1 (Jan)<br />
1 (Jan)<br />
11 (Nov)</td>
<td>latest<br />
v1<br />
v2</td>
<td>hep-th<br />
hep-th<br />
math.CA</td>
<td>(in metadata)</td>
<td>(in metadata)</td>
</tr>
<tr class="even">
<td>New scheme</td>
<td>0704.0001<br />
0704.0001v1<br />
1412.7878<br />
1501.00001<br />
9912.12345v2</td>
<td>arXiv:0704.0001<br />
arXiv:0704.0001v1<br />
arXiv:1412.7878<br />
arXiv:1501.00001<br />
arXiv:9912.12345v2</td>
<td>2007<br />
2007<br />
2014<br />
2015<br />
2099</td>
<td>6 (Jun)<br />
6 (Jun)<br />
12 (Dec)<br />
1 (Jan)<br />
12 (Dec)</td>
<td>latest<br />
v1<br />
latest<br />
latest<br />
v2</td>
<td>(in announcement log)</td>
<td>(in metadata)</td>
<td>(in metadata)</td>
</tr>
</tbody>
</table>

The highlighted areas show information that is not available from the
identifier. In the new scheme it is not be possible to tell the original
primary classification from the identifier. However, both the primary
and secondary classifications are given (definitively) for all articles
by the `Categories:` in the metadata.

**Versioning.** The versioning semantics are consistent across the
different identifier schemes. An identifier with a version number
appended refers to that specific version. An identifier without a
version number refers to the *article* (a trackback, for example, is to
a article and not to a particular version), and in appropriate contexts
will resolve to the latest version (if supplied in an `/abs/` URL for
example).

**Extension.** The new scheme could be extended to use more than 4 or 5
digits for the sequence number. However, that would correspond to more
than 99999 submissions per month, or over 10 times the current
submission rate, and is thus not anticipated for many years.

Indications of classification
-----------------------------

The *stamp* added to the side of processed TeX submissions now shows the
primary classification in a standard way, and is also recommended as the
preferred citation format. Examples are:

    arXiv:hep-th/9901001v2 10 May 1999
    arXiv:gr-qc/0606006v1 6 Jun 2006

    arXiv:math/9901001v1 [math.GT] 1 Jan 1999
    arXiv:cs/0001002v1 [cs.AR] 2 Jan 2000
    arXiv:nlin/0201003v1 [nlin.AO] 3 Jan 2002
    arXiv:q-bio/0401004v1 [q-bio.BM] 4 Jan 2004

    arXiv:cond-mat/9901001v1 [cond-mat.supr-con] 1 Jan 1999
    arXiv:physics/9901001v1 [physics.optics] 1 Jan 1999

    arXiv:0706.0001v1 [cond-mat.soft] 1 Jun 2007
    arXiv:0706.0002v3 [astro-ph] 15 Mar 2008

    arXiv:1501.00001v1 [hep-th] 1 Jan 2015

Old papers in archives where the archive name matches the primary
subject classification (e.g. `hep-th`) do not have the square brackets
with primary subject classification. In all other cases, the square
brackets are added. This includes archives where the identifier has
optional subject-class information (`math`, `cs`, `nlin`, `q-bio`),
archives where the subject-class information is not included
(`cond-math`, `physics`), and all papers with identifiers in the new
scheme.

URLs for standard arXiv functions
---------------------------------

The URL patterns for all standard arXiv functions are consistent for the
different forms of the arXiv identifier. Some examples are given in the
table below:

|                              | Generic               | Example with old id (9107-0703) | Example with new id (0704-1412) | Example new id (1501-)    |
|------------------------------|-----------------------|---------------------------------|---------------------------------|---------------------------|
| Abstract (normal HTML)       | `/abs/id`             | `/abs/hep-th/9901001`           | `/abs/0706.0001`                | `/abs/1501.00001`         |
| Abstract (raw txt)           | `/abs/id?fmt=txt`     | `/abs/hep-th/9901001?fmt=txt`   | `/abs/0706.0001?fmt=txt`        | `/abs/1501.00001?fmt=txt` |
| PDF                          | `/pdf/id.pdf`         | `/pdf/hep-th/9901001.pdf`       | `/pdf/0706.0001.pdf`            | `/pdf/1501.00001.pdf`     |
| PS                           | `/ps/id`              | `/ps/hep-th/9901001`            | `/ps/0706.0001`                 | `/ps/1501.00001`          |
| Source (.gz,.tar.gz,.pdf...) | `/src/id`             | `/src/hep-th/9901001`           | `/src/0706.0001`                | `/src/1501.00001`         |
| Trackbacks                   | `/tb/id`              | `/tb/hep-th/9901001`            | `/tb/0706.0001`                 | `/tb/1501.00001`          |
| New listings                 | `/list/arch-ive/new`  | `/list/hep-th/new`              | `/list/hep-th/new`              | `/list/hep-th/new`        |
| Month listings               | `/list/arch-ive/yymm` | `/list/hep-th/0601`             | `/list/hep-th/0601`             | `/list/hep-th/0601`       |

Anyone using `/ftp/...` URLs should take the opportunity to change to
the URLs given above since we plan to disable all access to `/ftp/...`
URLs in the near future. Contact us if there is a particular issue.

2007-04: The old functionality of accepting partial identifiers and
displaying a form to enter remaining information has been removed. The
following now show "not found" error messages:
[`/abs/hep-th/01001`](http://arxiv.org/abs/hep-th/01001),
[`/abs/hep-th/1`](http://arxiv.org/abs/hep-th/1),
[`/abs/hep-th`](http://arxiv.org/abs/hep-th). These facilities were very
little used (a few accesses per week) and most accesses appeared to be
mistakes.

<span id="abs">Metadata (`?fmt=txt` URLs and `.abs` files)</span>
-----------------------------------------------------------------

See also [OAI-PMH metadata harvesting facilities](/help/oa) and [the
arXiv API](/help/api) which are the preferred ways to get arXiv
metadata.

Since December 2008 all internal metadata files have the identifier as
the third line using the standard, `arXiv:` prefixed form. The old form
identifier lines (e.g. `Paper: arch-ive/YYMMNNN` or
`Paper: arch-ive.SC/YYMMNNN`) were all be rewritten in the new form, and
do not include the old subject class (`.SC`). The following forms are
possible:

    arXiv:1501.00001
    arXiv:0704.0001
    arXiv:math/9901001
    arXiv:astro-ph/9901001

Other than the provisos above, existing and new submissions have
metadata in the long-used `.abs` file format. The `Categories:` line
contains the definitive classification information:

    ------------------------------------------------------------------------------
    \\
    arXiv:math-ph/9901001
    From: Jens Marklof
    Date: Tue, 5 Jan 1999 15:55:02 GMT   (18kb)
    Date (revised v2): Tue, 13 Apr 1999 11:54:24 GMT   (19kb)

    Title: Quantum unique ergodicity for parabolic maps
    Authors: Jens Marklof, Zeev Rudnick
    Categories: math-ph chao-dyn math.MP math.NT math.SP nlin.CD quant-ph
    Comments: Latex 2e, revised version
    MSC-class: 81Q50 (Primary) 11L05, 58F11, 81S30 (Secondary)
    \\
      We study the ergodic properties of quantized ergodic maps of the torus. It is
    known that these satisfy quantum ergodicity: For almost all eigenstates, the
    ...
    \\

where this paper has primary classification `math-ph` and secondary
classifications `chao-dyn math.MP math.NT math.SP  nlin.CD quant-ph`
(sorted in alphabetical order). Except in cases of subsumed archives
(e.g. `alg-geom` to `math.AG`), the primary classification match the
first part of the identifier at present. We may, at some later time,
abandon that rule to allow reclassification of old articles to any
category.

New `.abs` files will have the same format except that the new internal
identifiers will appear on the `arXiv:` line:

    ------------------------------------------------------------------------------
    \\
    arXiv:0811.0573
    From: Carl Lagoze
    Date: Tue, 4 Nov 2008 19:07:36 GMT   (134kb)

    Title: A Web-Based Resource Model for eScience: Object Reuse & Exchange
    Authors: Carl Lagoze, Herbert Van de Sompel, Michael Nelson, Simeon Warner,
      Robert Sanderson, Pete Johnston
    Categories: cs.DL
    License: http://arxiv.org/licenses/nonexclusive-distrib/1.0/
    \\
      Work in the Open Archives Initiative - Object Reuse and Exchange (OAI-ORE)
    focuses on an important aspect of infrastructure for eScience: the
    ...
    \\

All submissions since April 2007 include a `License` URI which resolves
to a license statement. At some stage a license URI will be added to all
arXiv records.
