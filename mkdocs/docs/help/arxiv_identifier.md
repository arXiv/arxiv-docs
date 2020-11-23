Understanding the arXiv identifier
==================================

*The canonical form of identifiers from January 2015 (1501) is
arXiv:YYMM.NNNNN, with 5-digits for the sequence number within the
month.*

The article identifier scheme used by arXiv was changed in April 2007.
All existing articles retain their [original identifiers](#old) but
newly announced articles have identifiers following the [new
scheme](#new). As of January 2015, the number of digits used in the
second part of the new identifier, the sequence number within the month,
is increased from 4 to 5. This will allow arXiv to handle more than 9999
submissions per month (see [monthly submission
rates](/stats/monthly_submissions)).

<span id="new"></span>

Identifier scheme since 1 April 2007 (0704-)
--------------------------------------------

All new articles have identifiers with the following form:

`arXiv:YYMM.number`

`e.g. arXiv:1501.00001 or arXiv:0706.0001`

where identifiers up to month 1412 are zero-padded to 4-digits in the
last block, and those from 1501 onward are zero-padded to 5-digits.
Specific versions are referred to by adding the version number:

`arXiv:YYMM.numbervV`

`e.g. arXiv:1501.00001v1 or arXiv:0706.0001v2`

In general, the form is `arXiv:YYMM.number{vV}`, where

-   `YY` is the two-digit year (07=2007 through 99=2099, and potentially
    up to 06=2106)
-   `MM` is the two-digit month number (01=Jan,...12=Dec)
-   `number` is a zero-padded sequence number of 4- or 5-digits. From
    0704 through 1412 it is 4-digits, starting at `0001`. From 1501 on
    it is 5-digits, starting at `00001`. 5-digits permits up to `99999`
    submissions per month. We cannot currently anticipate more than
    99999 submissions per month although extension to 6-digits would be
    possible.
-   `vV` is a literal `v` followed by a version number of 1 or more
    digits starting at `v1`.

Note that the identifier no longer contains any classification
information and thus reclassification after an article is announced is
possible. Classification information is indicated in other ways. For
example, the stamp added to the side of the PDF versions of arXiv
articles has the form:

`arXiv:0706.0001v1 [q-bio.CB] 1 Jun 2007`

which indicates `v1` of the article `arXiv:0706.0001` which has primary
classification `q-bio.CB`, and was submitted on 1 June 2007.

The identifier `arXiv:YYMM.numbervV` provides a complete and unique
citation for an arXiv article. Without the version number (e.g.
`arXiv:YYMM.number`), the identifier refers to the *most recent version*
of the article. We recommend that in citations the specific version
number, the subject classification and the date information be included
in the same way that it is in the stamp on the side of the PDF. See also
[References to and in arXiv
Documents](/help/faq/references).

<span id="old"></span>

Identifiers up to March 2007 (9107-0703)
----------------------------------------

Identifiers from 1991 through 2007-03 followed the form shown in the
image below. The full list of groups, archives and subject classes is
listed on the [front page](/):

![Each article identifier begins with an archive, such as 'astro-ph' or
'hep-ex'. Optionally, this is followed by a period and a subject class.
This is followed by a forward slash and seven digits. The first four
digits represent the year and month an article was added to arXiv. For
example, an article id whose first four digits are '0107' was published
on arXiv in July, 2001. The last three digits represent the unique
number of that article in a given month and
archive.](https://arxiv.org/icons/arxiv_identifier.png)

Subject classes do not exist for some of the older archives in the
**Physics** group. Instead, each archive represents a subject class,
e.g., **hep-ex**, **hep-lat**, **hep-ph**, and **hep-th**. The
**astro-ph** archive currently has no subject classes, while
**cond-mat** and **physics** are classified by subject classes that
appear only in the metadata (not in the identifier).

This scheme uses two upper-case characters to identify the subject
class, e.g., math (Geometric Topology) = **math.GT**, cs (Software
Engineering) = **cs.SE**, and nlin (Chaotic Dynamics) = **nlin.CD**.

Motivation for 2007 change of identifier scheme
-----------------------------------------------

Some change to the arXiv identifier scheme was needs to permit
submissions expected to exceed 1000 articles per month in some archives
in 2007 (likely `math`, `cond-mat` and `astro-ph`). The [old identifier
scheme](#old) imposed a limit of 999 submissions per month in any one
archive. Obviously, we could have just added an extra digit
(`arch-ive/YYMMNNNN`) or perhaps made the `NNN` alphanumeric. However,
we took the opportunity to address other issues too.

The primary motivation for removing subject-classification information
from the identifier was to decouple these two properties (identification
and classification). This will increase our flexibility to adjust the
classifications of individual articles as necessary (for example, it has
long been possible to adjust classification of articles *within* the
`cs` and `math` archives and we see this as beneficial). It also makes
it easier to adjust our classification schemes as disciplines and arXiv
usage evolve (for example, we need to sub-divide astro-ph since it
currently too large). Various schemes with optional or redundant
classification information in the identifier were considered (extending
from the redundant [2-letter subject classes in `math`](/list/math/info)
etc.) but these were rejected because such many-to-1 resolution of
identifier-to-article means that interacting services cannot compare
identifiers and know whether they refer to the same arXiv article
without local knowledge of arXiv's identifier scheme.

We feel that is a useful to have a single canonical form for identifiers
within a month, with the same number of digits following the period.
Thus identifiers from 0704 through 1412 have the sequence number (the
number following the period) padded to 4-digits. The use of 4-digits
places a limit of 9999 identifiers in a single month and it is possible
that this will be exceeded in 2015 (8871 articles in 1410, 8668 in
1409). To ensure that the canonical form changes at a convenient
year-boundary the sequence number is padded to 5-digits from month 1501
onward, starting with identifier 1501.00001.

Further information for interacting services
--------------------------------------------

There are additional (gruesome) details of [arXiv identifiers for
interacting services](arxiv_identifier_for_services). These are unlikely
to be of interest/use unless you are handling internal data distributed
by arXiv.
