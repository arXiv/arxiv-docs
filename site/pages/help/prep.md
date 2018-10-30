Title and Abstract Fields ([Metadata](http://en.wikipedia.org/wiki/Metadata))
=============================================================================

This help document explains the format of metadata fields for arXiv
submissions — it explains how to fill out the various fields on the web
submission form. The possible information fields are:

-   **[Title:](#title)** *required*
-   **[Authors:](#author)** *required*
-   **[Abstract:](#abstracts)** *required*
-   **[Comments:](#comments)** optional, but recommended
-   **[Report-no:](#report)** *required (when supplied by author's
    institution)*
-   **[Category:](#subj)** depends on archive
-   **[Journal-ref:](#journal)** reserved for publication info
-   **[DOI:](#doi)** reserved publication DOI

<!-- -->

-   **[MSC-class:](#msc)** math archives only
-   **[ACM-class:](#acm)** required for cs archives only

Please read our FAQ page "[Submissions in languages other than English
and multiple language submissions](faq/multilang)" if your submission is
in a language other than English or includes a version in a language
other than English.

<span id="bad_char"></span>

Bad character(s)
----------------

Our metadata fields only accept ASCII input. Unicode charcters should be
conveted to its <span class="mathjax">$\\TeX$</span> equivalent (either through
[MathJax](/help/mathjax) entry or for proper names use the appropriate
[accents](#accents)).

A common problem experienced during submission, *Bad character(s) in
field...*, is reporting UTF chracters being entered into a field that
expects ASCII character entry. This is usually caused by the UTF
characters being copied from your pdf viewer and then pasted as such
during this step, rather than being entered as ASCII text. The most
common culprits are the curved quotation marks (for example “ and ”
instead of keyboard entry), long-hyphens (— or –), and fi/ff copied as a
single character).  
*If you can't figure it out, type it out.*

<span id="infofields"></span>

Information Fields
------------------

### <span id="title"></span>Title: *required*

-   Do not use all uppercase letters.
-   Do not use unicode characters.
-   Some <span class="mathjax>La$\\TeX$</span> is supported through [MathJax](/help/mathjax).
-   Expand out <span class="mathjax">$\\TeX$</span> macros that are mystifying, e.g. "Nonlinear Sigma
    Models" instead of "\\nlsm".
-   Check your spelling.
-   Certain [<class span="mathjax">$\\TeX$</span> accent commands](#accents) may be used in this
    field.
-   References to other articles in other archives should be given in
    the standard `arXiv:arch-ive/YYMMNNN` or `arXiv:YYMM.NNNN(N)` format
    so that our Web interface can turn the reference into a link to the
    article's abstract.

### <span id="author"></span>Authors: *required*

-   In order to automate indexing and searching, it is required that
    authors to be listed in a canonical format. Names should be given in
    the order: Firstname Lastname or Firstname Middlename Lastname
    (where Lastname is your family name).
-   Include the names of *all authors* instead of truncating the list
    with "*et al.*". This is necessary to support search and indexing.
    Multiple author names should be separated with a comma,

                E. L. Grossman, T. Zhou, E. Ben-Naim
            

    or with the word "and",

                Michael Dine, Yosef Nir and Yuri Shirman
            

-   First names and middle names may be abbreviated with just an
    initial. Initials should be followed by a period and then a space.
    Do not use all uppercase letters for names.
-   Do not enter a name that contains a comma or the word \`and'. If you
    must include \`Jr.' or similar suffix to a name then they must not
    be separated from the main name by a comma, enter simply
    `Bill Gates Jr` or `Fred Bloggs IV`. Names such as
    `John von Neumann` are entered exactly as illustrated.
-   Affiliations must be placed within parantheses. Do not enter full
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

-   Roles — such as `editor`, or `appendix author` — *may not* be
    indicated within the Authors field, rather roles should be indicated
    within the [Comments](#comments) field. Their names should be
    included in the Authors list. Such as:

        Authors: Author One, Author Two, Author Three
        Comments: Appendix by Author Two
             

-   Certain [<span class="mathjax">$\\TeX$</span> accent commands](#accents) may be used in this
    field.

### <span id="abstracts"></span>Abstract: *required*

Abstracts are automatically processed into the mailings, so it is
important to adhere to the formatting rules. Carriage returns will be
stripped unless they are followed by leading white spaces. So if you
want a new paragraph or a table of contents, be sure to indent the lines
after the carriage return. When the abstracts is formatted for email
announcement, it will be wrapped to 80 characters.

-   Do not include the word "Abstract".
-   Some <span class="mathjax">$\\TeX$</span> commands are supported via [MathJax](/help/mathjax).
-   As with the title, expand out opaque <span class="mathjax">$\\TeX$</span> macros. Including
    <span class="mathjax">$\\TeX$</span> formatting commands such as
    `~ \, (backslash comma) and \ (backslash  space)` makes it difficult
    for people to read. Please omit these TeX-isms. Also omit font
    commands such as `\em` or `\it`, as these will not be processed into
    the display. Additionally, <span class="mathjax">$\\TeX$</span> formtting commands for names will
    not be processed, and unicode character entry is not supported.
-   Do not start lines with whitespace (spaces, tabs, etc.) unless you
    are trying to prevent our automatic line wrapping. You might choose
    to use leading whitespace if for example your abstract is a table of
    contents. Avoid unnecessary blank lines.
-   Keep it short — abstracts longer than 1920 characters will not be
    accepted; abridge your abstract if necessary.
-   References to other articles in other archives should be given in
    the standard `arXiv:arch-ive/YYMMNNN` or `arXiv:YYMM.NNNN(N)` format
    so that our Web interface can turn the reference into a link to the
    article's abstract.

### <span id="comments"></span>Comments:

-   Indicate number of pages and number of figures. If desired, include
    <span class="mathjax>$\\TeX$</span> flavor or related comments.
-   Some <span clas="mathjax">$\\TeX$</span> commands are supported via [MathJax](/help/mathjax).
-   <span id="URL">Anonymous FTP and World Wide Web</span> locations
    should be given in the standard Uniform Resource Locator (URL)
    format. We automatically convert these into an active link reading
    "this ftp URL" and an http URL into a link reading "this http URL"
    (try for a grammatically sensible substitution). The location of
    related files or information should be given here. **Also, you
    should add a space to separate any periods or text following a URL
    from the URL itself, so that it is not interpreted as part of the
    URL.** For example, the comment

        "for associated mpeg file, see http://myhost.domain/file.mpg"
            

    when accessed via the archive WWW interface views as "for associated
    mpeg file, see \<this URL\>" .

-   References to other articles in other archives should be given in
    the standard `arXiv:arch-ive/YYMMNNN` or `arXiv:YYMM.NNNN(N)` format
    so that our Web interface can turn the reference into a link to the
    article's abstract.
-   This is the proper field for "to be published in" or "submitted to"
    information, including inclusion in conference proceedings. Please
    note that such entries will be frozen into this version, and is [not
    editable](/help/replace#minorchanges) after announcement.
-   This is the proper field for author roles, such as "Appendix by" or
    "Editor" information.
-   If this is a replacement, indicate the nature of the replacement and
    the severity of the changes so readers will know why it was
    replaced. You may with to still include your original comments (e.g.
    number of pages), because the comments field is not cumulative.
-   **Do not put copyright statements in the comments, put them on the
    front page of the article.** Even there, do not put any copyright or
    license statement that contradicts the license you grant arXiv on
    submission! For more information see our [descriptions of available
    licenses](/help/license).

### <span id="report"></span>Report-no: *required only when supplied by author's institution*

-   Enter your institution's locally assigned publication number.
-   Do not put any other information in this field.
-   Example: `Report-no: EFI-94-11`.

### <span id="subj"></span>Category:

Each arXiv article has a primary category and may also have one or more
cross-lists to other categories. The categories control what mailings an
article is announced in, and also provide a way to limit searches to
subsets of arXiv.

Some categories have just an archive name, such as `hep-th` or
`quant-ph`. Others are broken into subject classes to give finer subject
granularity:

-   For the `'astro-ph'` archive see [list of astro-ph subject
    classes](/archive/astro-ph).
-   For the `'cond-mat'` archive see [list of cond-mat subject
    classes](/archive/cond-mat).
-   For the `'physics'` archive see [list of physics subject
    classes](/archive/physics).
-   For the `'math'` archive see [list of math subject
    classes](/archive/math).
-   For the `'nlin'` archive see [list of nlin subject
    classes](/archive/nlin).
-   For the `'cs'` archive see [list of cs subject
    classes](http://arxiv.org/corr/subjectclasses).
-   For the `'q-bio'` archive see [list of q-bio subject
    classes](/archive/q-bio).
-   For the `'q-fin'` archive see [list of q-fin subject
    classes](/archive/q-fin).
-   For the `'stat'` archive see [list of stat subject
    classes](/archive/stat).
-   For the `'eess'` archive see [list of eess subject
    classes](/archive/eess).
-   For the `'econ'` archive see [list of econ subject
    classes](/archive/econ).

### <span id="journal"></span>Journal-ref:

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
    submitted article at a later date.
-   Do not put URLs into this field, as they will not be converted into
    links.

### <span id="doi"></span>DOI:

-   This field is **only** for a DOI ([Digital Object
    Identifier](http://doi.org/)) that resolves (links) to another
    version of the article, in a journal for example.
-   DOIs have the form `10.1016/S0550-3213(01)00405-9`
-   If there are multiple DOIs associated with an article, separate them
    with a space.
-   Do not include any other information in this field. In most cases,
    submissions are not yet published, and so `DOI` information will be
    added by the author at a later date. A facility is provided for
    [adding a Journal-ref and DOI](jref) to a previously submitted
    article.

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

### <span id="is_an_author"></span>Are you an author of this paper?

-   Although arXiv encourages authors to submit their own articles, some
    articles may be submitted by [third
    parties](/help/third_party_submission) (co-workers, administrative
    assistants, overlay journals, etc.). Prior authorization is required
    for such submissions. If you are not the author this work you must
    [contact](/help/contact) arXiv administrators for permission.
    Submissions without prior authorization will be removed.
-   The submitter of an article is automatically registered as an
    *owner* of the article, someone who has authorization to make
    changes to the article, such as replacing it or adding a
    cross-reference. Other people can become owners if they supply the
    paper password, or request ownership. See our [authority
    records](/help/authority) help page for more information.
-   When someone is registered as an *owner* of an article, they have a
    chance to specify if they are also an *author* — to get all of their
    rights and privileges, authors of arXiv articles should take
    ownership of their articles and designate themselves as an author.
-   Select *yes* if you are a listed author of the article you are
    submitting and *no* otherwise.

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

Here are the LaTeX accents commands that can be used in the Title and
Authors fields.

|                |                |                |                |                 |                 |                |
|----------------|----------------|----------------|----------------|-----------------|-----------------|----------------|
| **Ä**   \\"A   | **ä**   \\"a   | **Á**   \\'A   | **á**   \\'a   | **Ȧ**   \\.A    | **ȧ**   \\.a    | **Ā**   \\=A   |
| **ā**   \\=a   | **Â**   \\\^A  | **â**   \\\^a  | **À**   \\\`A  | **à**   \\\`a   | **Ą**   \\k{A}  | **ą**   \\k{a} |
| **Å**   \\r{A} | **å**   \\r{a} | **Ă**   \\u{A} | **ă**   \\u{a} | **Ǎ**   \\v{A}  | **ǎ**   \\v{a}  | **Ã**   \\\~A  |
| **ã**   \\\~a  | **Ć**   \\'C   | **ć**   \\'c   | **Ċ**   \\.C   | **ċ**   \\.c    | **Ĉ**   \\\^C   | **ĉ**   \\\^c  |
| **Ç**   \\c{C} | **ç**   \\c{c} | **Č**   \\v{C} | **č**   \\v{c} | **Ď**   \\v{D}  | **ď**   \\v{d}  | **Ë**   \\"E   |
| **ë**   \\"e   | **É**   \\'E   | **é**   \\'e   | **Ė**   \\.E   | **ė**   \\.e    | **Ē**   \\=E    | **ē**   \\=e   |
| **Ê**   \\\^E  | **ê**   \\\^e  | **È**   \\\`E  | **è**   \\\`e  | **Ȩ**   \\c{E}  | **ȩ**   \\c{e}  | **Ę**   \\k{E} |
| **ę**   \\k{e} | **Ĕ**   \\u{E} | **ĕ**   \\u{e} | **Ě**   \\v{E} | **ě**   \\v{e}  | **Ġ**   \\.G    | **ġ**   \\.g   |
| **Ĝ**   \\\^G  | **ĝ**   \\\^g  | **Ģ**   \\c{G} | **ģ**   \\c{g} | **Ğ**   \\u{G}  | **ğ**   \\u{g}  | **Ǧ**   \\v{G} |
| **ǧ**   \\v{g} | **Ĥ**   \\\^H  | **ĥ**   \\\^h  | **Ȟ**   \\v{H} | **ȟ**   \\v{h}  | **Ï**   \\"I    | **ï**   \\"i   |
| **Í**   \\'I   | **í**   \\'i   | **İ**   \\.I   | **Ī**   \\=I   | **ī**   \\=i    | **Î**   \\\^I   | **î**   \\\^i  |
| **Ì**   \\\`I  | **ì**   \\\`i  | **Į**   \\k{I} | **į**   \\k{i} | **Ĭ**   \\u{I}  | **ĭ**   \\u{i}  | **Ǐ**   \\v{I} |
| **ǐ**   \\v{i} | **Ĩ**   \\\~I  | **ĩ**   \\\~i  | **Ĵ**   \\\^J  | **ĵ**   \\\^j   | **Ķ**   \\c{K}  | **ķ**   \\c{k} |
| **Ǩ**   \\v{K} | **ǩ**   \\v{k} | **Ĺ**   \\'L   | **ĺ**   \\'l   | **Ļ**   \\c{L}  | **ļ**   \\c{l}  | **Ľ**   \\v{L} |
| **ľ**   \\v{l} | **Ń**   \\'N   | **ń**   \\'n   | **Ņ**   \\c{N} | **ņ**   \\c{n}  | **Ň**   \\v{N}  | **ň**   \\v{n} |
| **Ñ**   \\\~N  | **ñ**   \\\~n  | **Ö**   \\"O   | **ö**   \\"o   | **Ó**   \\'O    | **ó**   \\'o    | **Ȯ**   \\.O   |
| **ȯ**   \\.o   | **Ō**   \\=O   | **ō**   \\=o   | **Ô**   \\\^O  | **ô**   \\\^o   | **Ò**   \\\`O   | **ò**   \\\`o  |
| **Ő**   \\H{O} | **ő**   \\H{o} | **Ǫ**   \\k{O} | **ǫ**   \\k{o} | **Ŏ**   \\u{O}  | **ŏ**   \\u{o}  | **Ǒ**   \\v{O} |
| **ǒ**   \\v{o} | **Õ**   \\\~O  | **õ**   \\\~o  | **Ŕ**   \\'R   | **ŕ**   \\'r    | **Ŗ**   \\c{R}  | **ŗ**   \\c{r} |
| **Ř**   \\v{R} | **ř**   \\v{r} | **Ś**   \\'S   | **ś**   \\'s   | **Ŝ**   \\\^S   | **ŝ**   \\\^s   | **Ş**   \\c{S} |
| **ş**   \\c{s} | **Š**   \\v{S} | **š**   \\v{s} | **Ţ**   \\c{T} | **ţ**   \\c{t}  | **Ť**   \\v{T}  | **ť**   \\v{t} |
| **Ü**   \\"U   | **ü**   \\"u   | **Ú**   \\'U   | **ú**   \\'u   | **Ū**   \\=U    | **ū**   \\=u    | **Û**   \\\^U  |
| **û**   \\\^u  | **Ù**   \\\`U  | **ù**   \\\`u  | **Ű**   \\H{U} | **ű**   \\H{u}  | **Ų**   \\k{U}  | **ų**   \\k{u} |
| **Ů**   \\r{U} | **ů**   \\r{u} | **Ŭ**   \\u{U} | **ŭ**   \\u{u} | **Ǔ**   \\v{U}  | **ǔ**   \\v{u}  | **Ũ**   \\\~U  |
| **ũ**   \\\~u  | **Ŵ**   \\\^W  | **ŵ**   \\\^w  | **Ÿ**   \\"Y   | **ÿ**   \\"y    | **Ý**   \\'Y    | **ý**   \\'y   |
| **Ȳ**   \\=Y   | **ȳ**   \\=y   | **Ŷ**   \\\^Y  | **ŷ**   \\\^y  | **Ź**   \\'Z    | **ź**   \\'z    | **Ż**   \\.Z   |
| **ż**   \\.z   | **Ž**   \\v{Z} | **ž**   \\v{z} | **å**   {\\aa} | **Å**   {\\AA}  | **æ**   {\\ae}  | **Æ**   {\\AE} |
| **Ð**   {\\DH} | **ð**   {\\dh} | **đ**   {\\dj} | **Đ**   {\\DJ} | **ð**   {\\eth} | **Ð**   {\\ETH} | **ı**   {\\i}  |
| **ł**   {\\I}  | **Ł**   {\\L}  | **ŋ**   {\\ng} | **Ŋ**   {\\NG} | **Ø**   {\\O}   | **ø**   {\\o}   | **œ**   {\\oe} |
| **Œ**   {\\OE} | **ß**   {\\ss} | **þ**   {\\th} | **Þ**   {\\TH} |                 |                 |                |

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
