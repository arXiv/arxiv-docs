---
title: Metadata Formatting
---

[Metadata](http://en.wikipedia.org/wiki/Metadata) Formatting
=============================================================================

This help document explains the format of metadata fields for arXiv
submissions. The possible information fields are:

-   **[Title:](#title)** *required*
-   **[Authors:](#author)** *required*
-   **[Abstract:](#abstracts)** *required*
-   **[Comments:](#comments)** optional, but recommended

<!-- -->

-   **[DOI:](#doi)** reserved publication DOI
-   **[Journal Reference:](#journal)** reserved for publication info
-   **[Report-no:](#report)** *required only when supplied by author's
    institution)*

<!-- -->

-   **[MSC-class:](#msc)** math archives only
-   **[ACM-class:](#acm)** cs archives only

Please read our FAQ page "[Submissions in languages other than English
and multiple language submissions](faq/multilang)" if your submission is
in a language other than English or includes a version in a language
other than English.

<span id="bad_char"></span>

Character Formats
-----------------

Metadata fields now support Unicode characters or their
<span class="mathjax">$\\TeX$</span> equivalent (either through
[MathJax](/help/mathjax) entry or for proper names use the appropriate
[accents](#accents)).

Commonly used TeX expressions will render through [MathJax](/help/mathjax).
Check the display page preview (rendered in the "Final Preview" step) carefully
to ensure that all characters and expressions are being properly displayed.


<span id="infofields"></span>

Information Fields
------------------

### <span id="title"></span>Title: *required*

-   Do not use all uppercase letters.
-   Check your spelling.
-   Some <span class="mathjax>La$\\TeX$</span> is supported through [MathJax](/help/mathjax).
-   Expand out <span class="mathjax">$\\TeX$</span> macros that are mystifying,
    for example "Nonlinear Sigma Models" instead of "\\nlsm".
-   Certain [<span class="mathjax">$\\TeX$</span> accent commands](#accents)
    may be used in this field.
-   Format references to other arXiv articles in the pattern
    `arXiv:arch-ive/YYMMNNN` or `arXiv:YYMM.NNNN(N)` to automatically generate
    a link to the referenced article's abstract.

### <span id="author"></span>Authors: *required*

-   In order to automate indexing and searching, it is required that
    authors to be listed in a canonical format. List all author names in
    the order: Firstname Lastname or Firstname Middlename Lastname
    (where Lastname is the author's family name and Firstname is the author's
    given name).
-   First names and middle names may be abbreviated with an initial followed by
    a period and then a space.
-   Include the names of *all authors* instead of truncating the list
    with "*et al.*". This is necessary to support search and indexing.
    Separate multiple author names with a comma,

                E. L. Grossman, T. Zhou, E. Ben-Naim


    or with the word "and",

                Michael Dine, Yosef Nir and Yuri Shirman


-   Do not use all uppercase letters for names.
-   Do not enter a name that contains a comma or the word \`and'. If you
    must include \`Jr.' or similar suffix to a name, the suffix must not
    be separated from the main name by a comma (for example,
    `Bill Gates Jr` or `Fred Bloggs IV`). Names such as
    `John von Neumann` are entered exactly as illustrated.
-   Affiliations must be placed within parentheses. Do not enter full
    mailing address, as these are not needed in our metadata. If
    desired, at most, include a city and country (no zip codes, postal
    codes, or street addresses). If you have several authors from the
    same institution, you can use a footnote style for the affiliations.
    Here is an example (be sure to do it in the form presented here,
    including all parentheses, and using numbers and not letters):

        Authors: Author One (1), Author Two (1 and 2), Author Three (2)
               ((1) Institution One, (2) Institution Two)


-   If the authors constitute a named collaboration, the collaboration
    name should be used in addition to all authors. Preferred formats
    are:

        Authors: ABCD Collaboration: Author One, Author Two, Author Three


    which is taken to mean that the article was written by the ABCD
    Collaboration which is comprised of Author One, Author Two and
    Author Three.

        Authors: Author One, Author Two, for the ABCD Collaboration


    which is taken to mean that the article was written by Author One
    and Author Two, on behalf of the ABCD Collaboration.

        Authors: Author One, Author Two (the ABCD Collaboration)


    which is taken to mean that the article was written by Author One
    and Author Two, who are members of the ABCD Collaboration. This
    format has the disadvantage that the collaboration name will not be
    linked to a search.

-   Indicate roles — such as `editor`, or `appendix author` — within the
    [Comments](#comments) field, and include all names in the Authors list.
    Example:

        Authors: Author One, Author Two, Author Three
        Comments: Appendix by Author Two


-   [<span class="mathjax">$\\TeX$</span> accent commands](#accents) or Unicode
    may be used in this field.

### <span id="abstracts"></span>Abstract: *required*

Abstracts are automatically processed into the mailings, so it is
important to adhere to the formatting rules. Carriage returns will be
stripped unless they are followed by leading white spaces. So if you
want a new paragraph or a table of contents, be sure to indent the lines
after the carriage return.

-   Do not label your abstract with the word "Abstract".
-   Abstracts longer than 1920 characters will not be accepted; abridge your
    abstract if necessary.
-   Some <span class="mathjax">$\\TeX$</span> commands are supported via [MathJax](/help/mathjax).
-   As with the title, expand out opaque <span class="mathjax">$\\TeX$</span> macros.
-   Including <span class="mathjax">$\\TeX$</span> formatting commands such as
    `~ \, (backslash comma) and \ (backslash  space)` makes it difficult
    for people to read. Please omit these TeX-isms.
-   Omit font commands such as `\em` or `\it`, as these will not be processed
    into the display.
-   <span class="mathjax">$\\TeX$</span> formatting commands for names will not be processed.
-   Lines beginning with whitespace (spaces, tabs, etc.) will generate a
    carriage return. You might choose to use leading whitespace if your abstract
    contains multiple paragraphs or a table of contents.
-   Avoid unnecessary blank lines.
-   Format references to other arXiv articles in the pattern
    `arXiv:arch-ive/YYMMNNN` or `arXiv:YYMM.NNNN(N)` to automatically generate
    a link to the referenced article's abstract.

### <span id="comments"></span>Comments:

-   Indicate number of pages and number of figures. If desired, include
    <span class="mathjax>$\\TeX$</span> flavor or related comments.
-   Some <span clas="mathjax">$\\TeX$</span> commands are supported via [MathJax](/help/mathjax).
-   Standard HTTP(S) and FTP addresses are automatically converted into active
    links reading "this ftp URL" or "this http(s) URL"
    (try for a grammatically sensible substitution). **Add a space to separate
    any periods or text following a URL from the URL itself, so that it is not
    interpreted as part of the URL.** For example, the comment

        "for associated mpeg file, see http://myhost.domain/file.mpg"

    is displayed on the abstract page as "for associated mpeg file, see
    \<this http URL\>" .

-   Format references to other arXiv articles in the pattern
    `arXiv:arch-ive/YYMMNNN` or `arXiv:YYMM.NNNN(N)` to automatically generate
    a link to the referenced article's abstract.
-   This is the proper field for "to be published in" or "submitted to"
    information, including inclusion in conference proceedings. Please
    note that such entries will be frozen into this version, and is [not
    editable](/help/replace#minorchanges) after announcement.
-   This is the proper field for author roles, such as "Appendix by" or
    "Editor" information.
-   If this is a replacement, indicate the nature of the replacement and
    the severity of the changes so readers will know why it was
    replaced. You may wish to still include your original comments (e.g.
    number of pages), because the comments field is not cumulative.
-   **Do not put copyright statements in the comments, put them on the
    front page of the article.** Even there, do not put any copyright or
    license statement that contradicts the license you grant arXiv on
    submission! For more information see our [descriptions of available
    licenses](/help/license).

### <span id="report"></span>Report number: *required only when supplied by author's institution*

-   Enter your institution's locally assigned publication number.
-   Do not put any other information in this field.
-   Example: `Report-no: EFI-94-11`.

### <span id="journal"></span>Journal reference:

-   This field is **only** for a full bibliographic reference if the
    article has already appeared in a journal or a proceedings.
-   Indicate the volume number, year, and page number (or page range).
-   If your submission has not appeared yet, but you would still like to
    indicate where it will be published, use the [Comments:](#comments)
    field. Please note that the Comments field can only be updated by
    submitting a [replacement](replace).
-   If there are multiple full bibliographic references associated with
    the paper, for example the original and an erratum, then separate
    them with a semicolon and a space, e.g.
    `J.Hasty Results 1 (2008) 1-9; Erratum: J.Hasty Results 2 (2008) 1-2`
-   In most cases, submissions are not yet published, and so
    `Journal-ref` information is not available. A facility is provided
    for you to [add a journal reference](jref) to your previously
    submitted article at a later date without creating a new version.
-   Do not put URLs into this field.

### <span id="doi"></span>DOI:

-   This field is **only** for a DOI ([Digital Object
    Identifier](http://doi.org/)) that resolves (links) to another
    version of the article, in a journal for example.
-   DOIs have the form `10.1016/S0550-3213(01)00405-9`
-   If there are multiple DOIs associated with an article, separate each
    with a space.
-   Do not include any other information in this field. In most cases,
    submissions are not yet published, and so `DOI` information will be
    added by the author at a later date. A facility is provided for
    [adding a journal reference and DOI](jref) to a previously submitted
    article without creating a new version.

### <span id="msc"></span>MSC-class:

-   For submissions to the math archive, this field is used to indicate
    the mathematical classification code according to the [Mathematics
    Subject Classification](http://www.ams.org/msc/). Here is an example

        MSC-class: 14J60 (Primary) 14F05, 14J26 (Secondary)

    Put the "Primary" and "Secondary" keywords in parentheses. If there
    is only a Primary classification, the "Primary" keyword is optional.
    Separate multiple classification keys with commas.

### <span id="acm"></span>ACM-class:

-   For submissions to the cs archive, this field is used to indicate
    the classification code according to the [ACM Computing
    Classification System](http://www.acm.org/about/class/ccs98-html)
    (or see this
    [overview](http://www.acm.org/about-acm/class/how-to-use)). Here is
    an example

        ACM-class: F.2.2; I.2.7

    (Separate multiple classifications by a semicolon and a space.)


### <span id="accents"></span>Note on <span class="mathjax">La$\\TeX$</span> accent commands:

Two methods are supported for entering accented characters into arXiv.

1.  If your browser supports Unicode and you have the appropriate input
    method enabled on your computer, you can type them directly, and
    they will be converted into their <span class="mathjax">$\\TeX$</span> syntax.
2.  You can enter accented characters using a subset of <span class="mathjax">$\\TeX$</span> syntax.
    arXiv's subset of <span class="mathjax">$\\TeX$</span> supports many of the ways accented
    characters can be written in <span class="mathjax">$\\TeX$</span>, however, it only accepts
    characters from ISO Latin 1 (which is a subset of Unicode that can
    be represented as a single byte in UTF-8).

Here are the <span class="mathjax">La$\\TeX$</span> accents commands that can be used in the Title and
Authors fields.

<table border="1" cellpadding="3">
<tr><td ><b>&#196;</b>&nbsp;&nbsp;&nbsp;\"A</td><td ><b>&#228;</b>&nbsp;&nbsp;&nbsp;\"a</td><td ><b>&#193;</b>&nbsp;&nbsp;&nbsp;\'A</td><td ><b>&#225;</b>&nbsp;&nbsp;&nbsp;\'a</td><td ><b>&#550;</b>&nbsp;&nbsp;&nbsp;\.A</td><td ><b>&#551;</b>&nbsp;&nbsp;&nbsp;\.a</td><td ><b>&#256;</b>&nbsp;&nbsp;&nbsp;\=A</td></tr>
<tr><td ><b>&#257;</b>&nbsp;&nbsp;&nbsp;\=a</td><td ><b>&#194;</b>&nbsp;&nbsp;&nbsp;\^A</td><td ><b>&#226;</b>&nbsp;&nbsp;&nbsp;\^a</td><td ><b>&#192;</b>&nbsp;&nbsp;&nbsp;\`A</td><td ><b>&#224;</b>&nbsp;&nbsp;&nbsp;\`a</td><td ><b>&#260;</b>&nbsp;&nbsp;&nbsp;\k{A}</td><td ><b>&#261;</b>&nbsp;&nbsp;&nbsp;\k{a}</td></tr>
<tr><td ><b>&#197;</b>&nbsp;&nbsp;&nbsp;\r{A}</td><td ><b>&#229;</b>&nbsp;&nbsp;&nbsp;\r{a}</td><td ><b>&#258;</b>&nbsp;&nbsp;&nbsp;\u{A}</td><td ><b>&#259;</b>&nbsp;&nbsp;&nbsp;\u{a}</td><td ><b>&#461;</b>&nbsp;&nbsp;&nbsp;\v{A}</td><td ><b>&#462;</b>&nbsp;&nbsp;&nbsp;\v{a}</td><td ><b>&#195;</b>&nbsp;&nbsp;&nbsp;\~A</td></tr>
<tr><td ><b>&#227;</b>&nbsp;&nbsp;&nbsp;\~a</td><td ><b>&#262;</b>&nbsp;&nbsp;&nbsp;\'C</td><td ><b>&#263;</b>&nbsp;&nbsp;&nbsp;\'c</td><td ><b>&#266;</b>&nbsp;&nbsp;&nbsp;\.C</td><td ><b>&#267;</b>&nbsp;&nbsp;&nbsp;\.c</td><td ><b>&#264;</b>&nbsp;&nbsp;&nbsp;\^C</td><td ><b>&#265;</b>&nbsp;&nbsp;&nbsp;\^c</td></tr>
<tr><td ><b>&#199;</b>&nbsp;&nbsp;&nbsp;\c{C}</td><td ><b>&#231;</b>&nbsp;&nbsp;&nbsp;\c{c}</td><td ><b>&#268;</b>&nbsp;&nbsp;&nbsp;\v{C}</td><td ><b>&#269;</b>&nbsp;&nbsp;&nbsp;\v{c}</td><td ><b>&#270;</b>&nbsp;&nbsp;&nbsp;\v{D}</td><td ><b>&#271;</b>&nbsp;&nbsp;&nbsp;\v{d}</td><td ><b>&#203;</b>&nbsp;&nbsp;&nbsp;\"E</td></tr>
<tr><td ><b>&#235;</b>&nbsp;&nbsp;&nbsp;\"e</td><td ><b>&#201;</b>&nbsp;&nbsp;&nbsp;\'E</td><td ><b>&#233;</b>&nbsp;&nbsp;&nbsp;\'e</td><td ><b>&#278;</b>&nbsp;&nbsp;&nbsp;\.E</td><td ><b>&#279;</b>&nbsp;&nbsp;&nbsp;\.e</td><td ><b>&#274;</b>&nbsp;&nbsp;&nbsp;\=E</td><td ><b>&#275;</b>&nbsp;&nbsp;&nbsp;\=e</td></tr>
<tr><td ><b>&#202;</b>&nbsp;&nbsp;&nbsp;\^E</td><td ><b>&#234;</b>&nbsp;&nbsp;&nbsp;\^e</td><td ><b>&#200;</b>&nbsp;&nbsp;&nbsp;\`E</td><td ><b>&#232;</b>&nbsp;&nbsp;&nbsp;\`e</td><td ><b>&#552;</b>&nbsp;&nbsp;&nbsp;\c{E}</td><td ><b>&#553;</b>&nbsp;&nbsp;&nbsp;\c{e}</td><td ><b>&#280;</b>&nbsp;&nbsp;&nbsp;\k{E}</td></tr>
<tr><td ><b>&#281;</b>&nbsp;&nbsp;&nbsp;\k{e}</td><td ><b>&#276;</b>&nbsp;&nbsp;&nbsp;\u{E}</td><td ><b>&#277;</b>&nbsp;&nbsp;&nbsp;\u{e}</td><td ><b>&#282;</b>&nbsp;&nbsp;&nbsp;\v{E}</td><td ><b>&#283;</b>&nbsp;&nbsp;&nbsp;\v{e}</td><td ><b>&#288;</b>&nbsp;&nbsp;&nbsp;\.G</td><td ><b>&#289;</b>&nbsp;&nbsp;&nbsp;\.g</td></tr>
<tr><td ><b>&#284;</b>&nbsp;&nbsp;&nbsp;\^G</td><td ><b>&#285;</b>&nbsp;&nbsp;&nbsp;\^g</td><td ><b>&#290;</b>&nbsp;&nbsp;&nbsp;\c{G}</td><td ><b>&#291;</b>&nbsp;&nbsp;&nbsp;\c{g}</td><td ><b>&#286;</b>&nbsp;&nbsp;&nbsp;\u{G}</td><td ><b>&#287;</b>&nbsp;&nbsp;&nbsp;\u{g}</td><td ><b>&#486;</b>&nbsp;&nbsp;&nbsp;\v{G}</td></tr>
<tr><td ><b>&#487;</b>&nbsp;&nbsp;&nbsp;\v{g}</td><td ><b>&#292;</b>&nbsp;&nbsp;&nbsp;\^H</td><td ><b>&#293;</b>&nbsp;&nbsp;&nbsp;\^h</td><td ><b>&#542;</b>&nbsp;&nbsp;&nbsp;\v{H}</td><td ><b>&#543;</b>&nbsp;&nbsp;&nbsp;\v{h}</td><td ><b>&#207;</b>&nbsp;&nbsp;&nbsp;\"I</td><td ><b>&#239;</b>&nbsp;&nbsp;&nbsp;\"i</td></tr>
<tr><td ><b>&#205;</b>&nbsp;&nbsp;&nbsp;\'I</td><td ><b>&#237;</b>&nbsp;&nbsp;&nbsp;\'i</td><td ><b>&#304;</b>&nbsp;&nbsp;&nbsp;\.I</td><td ><b>&#298;</b>&nbsp;&nbsp;&nbsp;\=I</td><td ><b>&#299;</b>&nbsp;&nbsp;&nbsp;\=i</td><td ><b>&#206;</b>&nbsp;&nbsp;&nbsp;\^I</td><td ><b>&#238;</b>&nbsp;&nbsp;&nbsp;\^i</td></tr>
<tr><td ><b>&#204;</b>&nbsp;&nbsp;&nbsp;\`I</td><td ><b>&#236;</b>&nbsp;&nbsp;&nbsp;\`i</td><td ><b>&#302;</b>&nbsp;&nbsp;&nbsp;\k{I}</td><td ><b>&#303;</b>&nbsp;&nbsp;&nbsp;\k{i}</td><td ><b>&#300;</b>&nbsp;&nbsp;&nbsp;\u{I}</td><td ><b>&#301;</b>&nbsp;&nbsp;&nbsp;\u{i}</td><td ><b>&#463;</b>&nbsp;&nbsp;&nbsp;\v{I}</td></tr>
<tr><td ><b>&#464;</b>&nbsp;&nbsp;&nbsp;\v{i}</td><td ><b>&#296;</b>&nbsp;&nbsp;&nbsp;\~I</td><td ><b>&#297;</b>&nbsp;&nbsp;&nbsp;\~i</td><td ><b>&#308;</b>&nbsp;&nbsp;&nbsp;\^J</td><td ><b>&#309;</b>&nbsp;&nbsp;&nbsp;\^j</td><td ><b>&#310;</b>&nbsp;&nbsp;&nbsp;\c{K}</td><td ><b>&#311;</b>&nbsp;&nbsp;&nbsp;\c{k}</td></tr>
<tr><td ><b>&#488;</b>&nbsp;&nbsp;&nbsp;\v{K}</td><td ><b>&#489;</b>&nbsp;&nbsp;&nbsp;\v{k}</td><td ><b>&#313;</b>&nbsp;&nbsp;&nbsp;\'L</td><td ><b>&#314;</b>&nbsp;&nbsp;&nbsp;\'l</td><td ><b>&#315;</b>&nbsp;&nbsp;&nbsp;\c{L}</td><td ><b>&#316;</b>&nbsp;&nbsp;&nbsp;\c{l}</td><td ><b>&#317;</b>&nbsp;&nbsp;&nbsp;\v{L}</td></tr>
<tr><td ><b>&#318;</b>&nbsp;&nbsp;&nbsp;\v{l}</td><td ><b>&#323;</b>&nbsp;&nbsp;&nbsp;\'N</td><td ><b>&#324;</b>&nbsp;&nbsp;&nbsp;\'n</td><td ><b>&#325;</b>&nbsp;&nbsp;&nbsp;\c{N}</td><td ><b>&#326;</b>&nbsp;&nbsp;&nbsp;\c{n}</td><td ><b>&#327;</b>&nbsp;&nbsp;&nbsp;\v{N}</td><td ><b>&#328;</b>&nbsp;&nbsp;&nbsp;\v{n}</td></tr>
<tr><td ><b>&#209;</b>&nbsp;&nbsp;&nbsp;\~N</td><td ><b>&#241;</b>&nbsp;&nbsp;&nbsp;\~n</td><td ><b>&#214;</b>&nbsp;&nbsp;&nbsp;\"O</td><td ><b>&#246;</b>&nbsp;&nbsp;&nbsp;\"o</td><td ><b>&#211;</b>&nbsp;&nbsp;&nbsp;\'O</td><td ><b>&#243;</b>&nbsp;&nbsp;&nbsp;\'o</td><td ><b>&#558;</b>&nbsp;&nbsp;&nbsp;\.O</td></tr>
<tr><td ><b>&#559;</b>&nbsp;&nbsp;&nbsp;\.o</td><td ><b>&#332;</b>&nbsp;&nbsp;&nbsp;\=O</td><td ><b>&#333;</b>&nbsp;&nbsp;&nbsp;\=o</td><td ><b>&#212;</b>&nbsp;&nbsp;&nbsp;\^O</td><td ><b>&#244;</b>&nbsp;&nbsp;&nbsp;\^o</td><td ><b>&#210;</b>&nbsp;&nbsp;&nbsp;\`O</td><td ><b>&#242;</b>&nbsp;&nbsp;&nbsp;\`o</td></tr>
<tr><td ><b>&#336;</b>&nbsp;&nbsp;&nbsp;\H{O}</td><td ><b>&#337;</b>&nbsp;&nbsp;&nbsp;\H{o}</td><td ><b>&#490;</b>&nbsp;&nbsp;&nbsp;\k{O}</td><td ><b>&#491;</b>&nbsp;&nbsp;&nbsp;\k{o}</td><td ><b>&#334;</b>&nbsp;&nbsp;&nbsp;\u{O}</td><td ><b>&#335;</b>&nbsp;&nbsp;&nbsp;\u{o}</td><td ><b>&#465;</b>&nbsp;&nbsp;&nbsp;\v{O}</td></tr>
<tr><td ><b>&#466;</b>&nbsp;&nbsp;&nbsp;\v{o}</td><td ><b>&#213;</b>&nbsp;&nbsp;&nbsp;\~O</td><td ><b>&#245;</b>&nbsp;&nbsp;&nbsp;\~o</td><td ><b>&#340;</b>&nbsp;&nbsp;&nbsp;\'R</td><td ><b>&#341;</b>&nbsp;&nbsp;&nbsp;\'r</td><td ><b>&#342;</b>&nbsp;&nbsp;&nbsp;\c{R}</td><td ><b>&#343;</b>&nbsp;&nbsp;&nbsp;\c{r}</td></tr>
<tr><td ><b>&#344;</b>&nbsp;&nbsp;&nbsp;\v{R}</td><td ><b>&#345;</b>&nbsp;&nbsp;&nbsp;\v{r}</td><td ><b>&#346;</b>&nbsp;&nbsp;&nbsp;\'S</td><td ><b>&#347;</b>&nbsp;&nbsp;&nbsp;\'s</td><td ><b>&#348;</b>&nbsp;&nbsp;&nbsp;\^S</td><td ><b>&#349;</b>&nbsp;&nbsp;&nbsp;\^s</td><td ><b>&#350;</b>&nbsp;&nbsp;&nbsp;\c{S}</td></tr>
<tr><td ><b>&#351;</b>&nbsp;&nbsp;&nbsp;\c{s}</td><td ><b>&#352;</b>&nbsp;&nbsp;&nbsp;\v{S}</td><td ><b>&#353;</b>&nbsp;&nbsp;&nbsp;\v{s}</td><td ><b>&#354;</b>&nbsp;&nbsp;&nbsp;\c{T}</td><td ><b>&#355;</b>&nbsp;&nbsp;&nbsp;\c{t}</td><td ><b>&#356;</b>&nbsp;&nbsp;&nbsp;\v{T}</td><td ><b>&#357;</b>&nbsp;&nbsp;&nbsp;\v{t}</td></tr>
<tr><td ><b>&#220;</b>&nbsp;&nbsp;&nbsp;\"U</td><td ><b>&#252;</b>&nbsp;&nbsp;&nbsp;\"u</td><td ><b>&#218;</b>&nbsp;&nbsp;&nbsp;\'U</td><td ><b>&#250;</b>&nbsp;&nbsp;&nbsp;\'u</td><td ><b>&#362;</b>&nbsp;&nbsp;&nbsp;\=U</td><td ><b>&#363;</b>&nbsp;&nbsp;&nbsp;\=u</td><td ><b>&#219;</b>&nbsp;&nbsp;&nbsp;\^U</td></tr>
<tr><td ><b>&#251;</b>&nbsp;&nbsp;&nbsp;\^u</td><td ><b>&#217;</b>&nbsp;&nbsp;&nbsp;\`U</td><td ><b>&#249;</b>&nbsp;&nbsp;&nbsp;\`u</td><td ><b>&#368;</b>&nbsp;&nbsp;&nbsp;\H{U}</td><td ><b>&#369;</b>&nbsp;&nbsp;&nbsp;\H{u}</td><td ><b>&#370;</b>&nbsp;&nbsp;&nbsp;\k{U}</td><td ><b>&#371;</b>&nbsp;&nbsp;&nbsp;\k{u}</td></tr>
<tr><td ><b>&#366;</b>&nbsp;&nbsp;&nbsp;\r{U}</td><td ><b>&#367;</b>&nbsp;&nbsp;&nbsp;\r{u}</td><td ><b>&#364;</b>&nbsp;&nbsp;&nbsp;\u{U}</td><td ><b>&#365;</b>&nbsp;&nbsp;&nbsp;\u{u}</td><td ><b>&#467;</b>&nbsp;&nbsp;&nbsp;\v{U}</td><td ><b>&#468;</b>&nbsp;&nbsp;&nbsp;\v{u}</td><td ><b>&#360;</b>&nbsp;&nbsp;&nbsp;\~U</td></tr>
<tr><td ><b>&#361;</b>&nbsp;&nbsp;&nbsp;\~u</td><td ><b>&#372;</b>&nbsp;&nbsp;&nbsp;\^W</td><td ><b>&#373;</b>&nbsp;&nbsp;&nbsp;\^w</td><td ><b>&#376;</b>&nbsp;&nbsp;&nbsp;\"Y</td><td ><b>&#255;</b>&nbsp;&nbsp;&nbsp;\"y</td><td ><b>&#221;</b>&nbsp;&nbsp;&nbsp;\'Y</td><td ><b>&#253;</b>&nbsp;&nbsp;&nbsp;\'y</td></tr>
<tr><td ><b>&#562;</b>&nbsp;&nbsp;&nbsp;\=Y</td><td ><b>&#563;</b>&nbsp;&nbsp;&nbsp;\=y</td><td ><b>&#374;</b>&nbsp;&nbsp;&nbsp;\^Y</td><td ><b>&#375;</b>&nbsp;&nbsp;&nbsp;\^y</td><td ><b>&#377;</b>&nbsp;&nbsp;&nbsp;\'Z</td><td ><b>&#378;</b>&nbsp;&nbsp;&nbsp;\'z</td><td ><b>&#379;</b>&nbsp;&nbsp;&nbsp;\.Z</td></tr>
<tr><td ><b>&#380;</b>&nbsp;&nbsp;&nbsp;\.z</td><td ><b>&#381;</b>&nbsp;&nbsp;&nbsp;\v{Z}</td><td ><b>&#382;</b>&nbsp;&nbsp;&nbsp;\v{z}</td><td><b>&#229;</b>&nbsp;&nbsp;&nbsp;{\aa}</td><td><b>&#197;</b>&nbsp;&nbsp;&nbsp;{\AA}</td><td><b>&#230;</b>&nbsp;&nbsp;&nbsp;{\ae}</td><td><b>&#198;</b>&nbsp;&nbsp;&nbsp;{\AE}</td></tr>
<tr><td><b>&#208;</b>&nbsp;&nbsp;&nbsp;{\DH}</td><td><b>&#240;</b>&nbsp;&nbsp;&nbsp;{\dh}</td><td><b>&#273;</b>&nbsp;&nbsp;&nbsp;{\dj}</td>
<td ><b>&#272;</b>&nbsp;&nbsp;&nbsp;{\DJ}</td>
<td ><b>&#240;</b>&nbsp;&nbsp;&nbsp;{\eth}</td>
<td ><b>&#208;</b>&nbsp;&nbsp;&nbsp;{\ETH}</td>
<td ><b>&#305;</b>&nbsp;&nbsp;&nbsp;{\i}</td>
</tr>
<tr>
<td ><b>&#322;</b>&nbsp;&nbsp;&nbsp;{\I}</td>
<td ><b>&#321;</b>&nbsp;&nbsp;&nbsp;{\L}</td>
<td ><b>&#331;</b>&nbsp;&nbsp;&nbsp;{\ng}</td>
<td ><b>&#330;</b>&nbsp;&nbsp;&nbsp;{\NG}</td>
<td ><b>&#216;</b>&nbsp;&nbsp;&nbsp;{\O}</td>
<td ><b>&#248;</b>&nbsp;&nbsp;&nbsp;{\o}</td>
<td ><b>&#339;</b>&nbsp;&nbsp;&nbsp;{\oe}</td>
</tr>
<tr>
<td ><b>&#338;</b>&nbsp;&nbsp;&nbsp;{\OE}</td>
<td ><b>&#223;</b>&nbsp;&nbsp;&nbsp;{\ss}</td>
<td ><b>&#254;</b>&nbsp;&nbsp;&nbsp;{\th}</td>
<td ><b>&#222;</b>&nbsp;&nbsp;&nbsp;{\TH}</td><td>&nbsp;</td>
<td>&nbsp;</td><td>&nbsp;</td></tr>
</table>



<span id="examples"></span>Examples
-----------------------------------

The following are examples of how correctly completed metadata might
appear in plain text email announcements:

### Example 1

    Title: Recent Seminal Results in the Theory of Everything
      That I Have Been Working on Recently
    Authors: H.Z. Jarvey (Eastern Fundamental Institute)
    Comments: 12 pages, 3 Postscript figures, uses rotate.sty
    Report-no: EFI-94-11
    Journal-ref: Obsc. Unr. Jour. 51 (1994) 87-95

    This paper explains everything about everything, thereby making
    redundant all other papers in the field.  Applications to text
    compression should be obvious.

### Example 2

    Title: An interesting new theorem in algebraic geometry
    Authors: Jane B. Jones, John F. Jones, and Steven Q. Smith
    Comments: AMS-LaTeX v1.2, 24 pages with 3 figures
    Report-no: University of Northern Nowhere preprint UNN-MATH-96-04
    Subj-class: Algebraic Geometry
    MSC-class: 14J30 (Primary); 32H10 (Secondary)

    We extend the results of our previous papers in order to prove some
    well-known conjectures in differentio-algebraic geometric functional
    analysis.
