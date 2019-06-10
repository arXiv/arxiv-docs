Submission of indexes for conference proceedings
================================================

We encourage conference organizers to use arXiv as a way to distribute
and archive conference papers. Conference proceedings may be made as a
single submission (which is handled in the normal way), or as a set of
individual papers with an index submission. **Note** individual papers 
within a proceedings must still conform to arXiv content polices and are
moderated, as usual. 
In general, we prefer arrangements where the respective authors submit 
the individual papers. We provide two ways of partially automating the 
process of creating HTML index submissions which are best suited to two 
different scenarios:

-   [Index submitted after the individual papers](#index_after). We have
    support for the automatic extraction of metadata from the individual
    submissions using special processing instructions from within an
    HTML index submission which lists the arXiv identifiers of the
    individual papers. A good example is
    [arXiv:1205.2597](/abs/1205.2597v1).
-   [Index submitted before the individual papers](#index_before). We
    have support for automatic linking to a search on the report number
    field. Conference organizers must instruct the submitters of
    individual papers to include a unique report number in the
    `Report-no:` field of their submission. The HTML index submission
    includes special processing instructions which create links to the
    report number search. An example using this approach is
    [arXiv:1108.3558](/abs/1108.3558v1).

Please note that conference announcements, or indexes without the
papers, are not permitted. We accept index submissions before the
submission of individual papers with the understanding that the majority
of papers at the conference will be submitted. If in doubt [contact
arXiv administrators](/contact).

<span id="index_after"></span>

Index submission after individual papers
----------------------------------------

The simplest way to make a proceedings or index entry is to create an
HTML submission using special `LIST:arXiv:YYMM.NNNN` or
`LIST:arch-ive/YYMMNNN` (only for [old identifiers](arxiv_identifier)
like hep-lat/9801024), directives which are expanded by arXiv's HTML
interpreter to the full title/author listings in the usual local format
(with the author names linked to the search; using whatever cookies the
users' browsers send to determine the output format; and all paper links
local to the same site the index is retrieved from).

Keep the HTML simple and be sure to include the `LIST:arXiv:YYMM.NNNN`
directives on separate lines without any leading whitespace. A good
example is [arXiv:1205.2597v1](/abs/1205.2597v1), for which the source
HTML is:

    <html>
    <head>
    <title>UAI 2010</title>
    </head>
    <body>
    <h1>UAI 2010 Proceedings</h1>

    Editors: Peter Grunwald, Peter Spirtes<br /><br />
    Catalina Island, CA, July 8  - July 11 , 2010<br />
    AUAI Press, Corvallis, Oregon, 2010, ISBN: 978-0-9749039-6-5<br /><br />

    <!-- Incorporating Side Information in Probabilistic Matrix Factorization  with Gaussian Processes -->
    LIST:arXiv:1003.4944
    <!-- Gaussian Process Topic Models -->
    LIST:arXiv:1203.3462
    <!-- Timeline: A Dynamic Hierarchical Dirichlet Process Model for  Recovering Birth/Death and Evolution of Topics in Text Stream -->
    LIST:arXiv:1203.3463
    <!-- Gibbs Sampling in Open-Universe Stochastic Languages -->
    LIST:arXiv:1203.3464
    <!-- Compiling Possibilistic Networks: Alternative Approaches to Possibilistic Inference -->
    LIST:arXiv:1203.3465

    ...

    </body>
    </html>

Unfortunately, if the index submission is made after the papers are
submitted then there is no easy way for the individual papers to link to
the index submission. Instead, submitters of the individual papers
should add an appropriate comment, e.g.

    Comments: Plenary talk presented at Lattice97

If organizers wish to have the papers of a proceedings link to the index
submission there is obviously a submission order problem. (Which came
first, the chicken or the egg?) As noted above, we will accept
submission of an 'empty' index submission given appropriate assurances
that the majority of the papers will be submitted. Any 'placeholder'
index submission should be made just in advance of the actual
submissions and should be updated (using [replace](replace)) promptly to
add links to the individual submissions.

### The individual papers

There need be no special considerations for the individual papers. If
the index submission identifier is known at the time of submission then
a link to the index submission may be included in the comments, e.g.

    Comments: 14 pages. Part of LATTICE 97 proceedings (arXiv:hep-lat/9801024)

the identifier in the comments will be automatically linked to the
abstract page, no explicit HTML link is necessary (or desired) in the
metadata submitted.

<span id="index_before"></span>

Index submitted before individual papers
----------------------------------------

The HTML index submission should consist of the title, author, etc., and
a report number for each paper. The report numbers must be included with
special `REPORT-NO:AIWorld/2003/01` directives which are expanded by
arXiv's HTML interpreter to link to the individual papers.

Keep the HTML simple and be sure to include the
`REPORT-NO:AIWorld/2003/01` directives on separate lines without any
leading whitespace. For example:

    <html>
    <head>
    <title>AI World Conference 2003</title>
    </head>
    <body>
    <h1>AI World Conference 2003</h1>

    <dl>
    <dt><b>New developments in AI</b></dt>
    <dd>Fred Bloggs, Bill Smith<br />
    (paper 
    REPORT-NO:AIWorld/2003/01
    )
    </dd>
    </dl>

    ...

    </body>
    </html>

which would be rendered as

**New developments in AI**
:   Fred Bloggs, Bill Smith  
    (paper [AIWorld/2003/01](#find_report_no_AIWorld/2003/01) )

The report numbers themselves should be chosen so that they will be
unique. This means that they should usually include the conference name
or abbreviation, the year and the paper number.

### Individual submissions

The individual submissions must include the appropriate report number in
the `Report-no` field. They should also include a link to the index
submission by including the identifier of the index submission in the
`Comments` field, e.g.

    Comments: Presented at AI World Conference, 2003 (arXiv:cs/0101200)
    Report-no: AIWorld/2003/01

The paper id in the comments will be linked in the abstract display
page. Additional report numbers may be included in the `Report-no` field
and should be separated with semicolon and a space, e.g.

    Report-no: AIWorld/2003/01; CornellCS-03-23

The individual submissions must be submitted to the same archive as the
index submission (the subject class may differ). This is because the
report number search from the index submission will be limited to that
archive.
