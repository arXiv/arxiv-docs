Why doesn't my paper have the arXiv id stamped on the side of the page?
=======================================================================

Most of the articles in arXiv have the arXiv id added as a stamp on left
hand side of the PDF and PostScript. The form of the stamp is:

> arXiv:hep-lat/0105002v1   2 May 2001

This stamp may not appear for different reasons depending on whether the
source format is [TeX](#tex), [PDF](#pdf) or [PostScript](#ps).

<span id="tex"></span>

TeX (and latex etc.) submissions
--------------------------------

1.  The stamping may have been explicitly disabled. This facility is
    provided for journals using arXiv that wish the output to look as
    similar as possible to the journal version.
2.  There may be commands in the TeX source or an included macro package
    that write over the stamp making it invisible. This could be the
    result of a figure that goes to the edge of the page, or something
    that "clears the page". For example, using the `color` package and
    setting the `pagecolor` will erase the page (even if the color is
    white). To fix, simply comment out the `\pagecolor` command, e.g.:

        ...
        \usepackage{color}
        ...
        %\pagecolor{white} %comment this line
        ...

<span id="pdf"></span>

PDF submissions
---------------

-   We do not stamp PDF submissions because we have not developed the
    software necessary to do it.

<span id="ps"></span>

PostScript submissions
----------------------

-   The PostScript may overwrite the stamp. You should check that the
    PostScript does not, for example, write a big white box to "clear"
    the page.

<span id="docx"></span>

DOCX submissions
----------------

-   As with PDF submissions, we have not developed the software
    necessary to do so.

<span id="html"></span>

HTML submissions
----------------

-   We do not stamp HTML files, as they are intended to be viewed within
    the web browser.
