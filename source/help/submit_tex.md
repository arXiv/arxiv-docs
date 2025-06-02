# TeX Submissions

*   [(La)TeX processing changes &mdash; April 2025](#newtex)
*   [Comparison between the Legacy Submission System and the current one](#comparison)
*   [Supported TeX processors](#supported-processors)
*   [Submissions are automatically processed](#autoproc)
*   [Considerations for LaTeX submissions](#latex)
*   [Considerations for PDFLaTeX submissions](#pdflatex)
*   [We don't have your style files or macros](#wedonthavethem)
*   [Do not submit in double-spaced "referee" mode](#double)
*   [Prepare the references carefully](#refs)
*   [Include `.bbl` files if you use BibTeX](#bibtex)
*   [Potential problems with biblatex `.bbl` files](#biblatex)
*   [Include `.ind` files if you used `makeindex`](#makeindex)
*   [Include `.gls` or `.nls` files if you have a glossary or nomenclature section](#glossary)
*   [Avoid mistakes in the text](#mistakes)
*   [Problems with special TeX characters in hyperlinks (URLs) -- in particular JHEP3.cls](#jhep3)
*   [Hidden files will be deleted upon announcement](#hidden)

* * *

<span id="newtex"></span>
### (La)TeX processing changes &mdash; April 2025

Beginning with April 2025, we are rolling out changes to how arXiv process (La)TeX submissions. These changes
should not be noticeable to most of our users. We will retire the long-used "AutoTeX" (Submission 1.0) system
that we have used for decades in favor of a simpler, more straightforward process of converting (La)TeX
submissions to PDFs in Submission 1.5.

<span id="comparison"></span>
### Comparison between the Legacy Submission System and the current one

For detailed documentation of the Legacy Submission System and its differences to the current one,
please see [Legacy Submission System](submit_legacy_differences.md).

<span id="supported-processors"></span>
### Supported TeX processors

As with the legacy system, we are currently only supporting the following types of TeX submissions:

  * plain TeX submissions: those are converted using `etex` followed by `dvips` and `ps2pdf`;
  * LaTeX submissions in DVI mode: those are converted using `latex` followed by `dvips` and `ps2pdf`;
  * LaTeX submissions in PDF mode: those are converted using `pdflatex`.

During the submission process, you will be asked which of the processor you want to use for your
submission. 

#### Selecting the correct processor

Selecting the correct processor is generally an easy task, because we will offer you the hopefully correct
one automatically during submission. If you want to decide by yourself, here is a quick guide:

  * if it is plain TeX, select it;
  * if it is a LaTeX document that includes `eps` files, use "LaTeX in DVI mode";
  * if it is a LaTeX document that includes `jpg`, `png` (and some more) files, use "LaTeX in PDF mode";
  * if you don't know, use "LaTeX in PDF mode"

Note that at the moment, the processor type is fixed for all parts of a multi-file submission.

<span id="autoproc"></span>

### Submissions are automatically processed

Your submission will be processed automatically according to the processor selected during the submission step.

This is a complex task, and the processing does not always lead to the desired or expected results. It is
important for you, the author/submitter, to carefully check and verify the resulting PDF. You will be required
to view the PDF during the submission process before you will be able to complete your submission.

You can submit a collection of TeX input/include files, e.g. separate chapters, foreword, appendix, etc, and
custom macros ([see below](#wedonthavethem)) packaged in a (possibly compressed) `.tar` or `.zip` file. Main files
(or "Toplevel files") can be in the root or in a subdirectory, but note that compilation is **always** done
from the root of your submission directory, even if the main file is in a subdirectory. This is important
when you use `\include` or `\input` or any other command that includes data from external files.

That said, it is important that you do not include extraneous files (including unused figure files), leftover
files, backup files, anything that does not belong to the paper you are submitting or is not needed for processing.
Do not include journal templates, referee letters, or man pages. Tidy your submission before you pack it up.

You must submit any figures that go along with your paper. We recommend that you use appropriate TeX commands
to include the figures inline with your paper (see below).

_Note:_ arXiv recommends against using the `\today` macro in the standard `\date` field. Because pdf are
occasionally rebuilt this date will change and may cause confusion, as outlined in
our [FAQ page for this topic](faq/today.md). To avoid this issue, do not use it unless you are comfortable with the
displayed date changing periodically. 


<span id="latex"></span>
### Considerations for (La)TeX submissions

If you have a file named foo.tex, then do not include any associated auxiliary file or intermediate or
resulting output file, e.g. foo.ps (or foo.aux, foo.log, foo.toc, foo.lot, foo.lof, foo.dvi, foo.pdf)
in your submission. These will be automatically removed to allow the creation of an output file from
your TeX file. Index (`.ind`) and processed bibtex (`.bbl`) files are an exception, [see below](#bibtex).


<span id="figures"></span>
#### Figure inclusion in LaTeX submissions

Depending on the selected processor (see above), only certain types of images can be included without
conversion:

  * for plain TeX, and for "LaTeX in DVI mode", only (encapsulated) PostScript (**.ps** or **.eps**) are supported;
  * for "LaTeX in PDF mode", you may embed your `.pdf, .png, .jpg` figures using the same mechanisms.

Please note that arXiv does not perform "on the fly" figure file conversion during tex processing
(i.e. "`-eps-converted-to.pdf`" files being present in your source directory). You must perform such conversion
yourself before uploading, updating any effected inclusion command. This process ensures that you have
examined the results of any figure conversion to ensure that the figures still contain scientifically correct
information and that arXiv is not responsible for the scientific accuracy of your figures.

The most flexible and robust figure inclusion is provided by the `graphics` and `graphicx` packages and the
`\includegraphics` command defined therein. We highly recommend you use them for your figure inclusion.
arXiv does not support the `psfig` package any longer. You may not include your own `psfig.sty`, as this will
cause your source to fail. The functionality it required was deprecated prior to
[TeXLive 2016](http://tug.org/pipermail/texhax/2016-October/022493.html) and this is not something we can control.
Older submissions that have already been announced with the `psfig` package will still work.
Please update your source to a more modern inclusion command.


Note that some software will permit you to include a mix of PostScript and PDFLaTeX-compatible figures and
will perform the conversions to the appropriate format for you on the fly. arXiv does not permit such
software to run during the TeX processing. Why? It is possible for conversion issues to arise that
can alter the scientific meaning or interpretation of your figure. Rather than invite such possibilities,
we require that you use a unified figure format.

#### Avoid embedding JavaScript in your PDF files

Do not include embedded JavaScript such as animated gifs, movies, or HTML in your PDF. Submissions with
embedded JavaScript are automatically rejected due to the potential security risks posed to arXiv systems.
  - Submit all movies and animated GIFS as separate(non-JavaScript) ancillary files.
  - Remove or disable JavaScript when building your PDF or generate PDFs using standard tools such as Adobe Distiller.

#### Figure inclusion in plain TeX

For plain TeX submissions, use the plain tex interface to the graphics package (`graphicx.tex`) or a macro
package like `epsf` or `epsfig`.

arXiv does not presently support PDFTeX.

<span id="pdflatex"></span>

### Considerations for PDFLaTeX submissions

arXiv fully supports and automatically recognizes PDFLaTeX. 

*   Should you need conditional branching in your source, use the [ifpdf](ftp://tug.ctan.org/pub/tex-archive/macros/latex/contrib/oberdiek/ifpdf.pdf) package. Do not re-invent the wheel.
    [ifpdf](ftp://tug.ctan.org/pub/tex-archive/macros/latex/contrib/oberdiek/ifpdf.pdf) provides a robust and well tested mechanism to distinguish between pdflatex in pdf mode and other
    modes or engines.
*   Some packages may require a particular back-end driver, in the form of a package option, 
    e.g. `\usepackage[pdftex]{...}`. However, the graphics and hyperref packages determine the proper driver
    automatically; you do not have to make this explicit choice and should not do so to avoid conflicts.
*   Figures can be included in **JPEG**, **PNG**, or **PDF** format with the standard graphics package. For
    security reasons arXiv does not allow for automated format conversion, so your figures must be in the proper
    format already.
*   Unlike native LaTeX, the default output format for PDFLaTeX is PDF, with no intermediate DVI or PostScript.
    Thus, these formats are _not_ available for download for PDFLaTeX submissions.


<span id="wedonthavethem"></span>

### We do **not** have your style files or macros

We don't provide any further packages besides what is provided by the TeX Live system.
That means in particular that some publisher styles will not be available. Please check
the list of TeX Live packages provided by arXiv at the current time is
[here](texlive_package_list.md).

<span id="double"></span>

### Do not submit in double-spaced "referee" mode

Avoid inadvertently submitting your paper in double-spaced referee mode, since it wastes paper on a global scale.
Readers prefer to have a compact single-spaced version, as it would appear in a printed journal.

<span id="refs"></span>

### Prepare the references carefully

We strongly encourage you to include arXiv's `YYMM.NNNNN`, [identifiers](arxiv_identifier.md) in your reference list for both
published and unpublished papers. Note also that many publishers allow e-print identifiers to appear in the
references of papers submitted.

If you use standard identifiers of the form 1510.00322, arXiv:1510.00322, 0901.0512, arXiv:0901.0512,
hep-ph/9409201 or arXiv:hep-ph/9409201, they can be easily harvested by automatic software. For example,

> `\bedim{upsilon}
> C.T.H. Davies {\em et al.}, Phys. Rev {\bf D} 50 (1994) 6963, hep-lat/9406017.`

Do not include extraneous font commands, spaces, tildes, braces, or line-breaks within the e-print identifier:
this will cause your references to be missed by automated extraction software. See also notes
about [references to and in arXiv documents](faq/references.md) and [collection of references at INSPIRE](https://inspirehep.net/).
Use of e-print identifiers is a significant aid to the INSPIRE database. It also facilitates automatic
network hyperlinks of references from within papers.

If you use BibTeX there are some BibTeX styles which support e-print identifiers (see [BibTeX and Eprints](hypertex/bibstyles/index.md)).

If you are submitting a group of `.tex` files, automated reference extraction by INSPIRE and others will be
more accurate and faster if your references are all in one file. This file should have
the `\begin{thebibliography}` or similar command within it, and should be called `foo.bbl` to correspond
to a given `foo.tex` source file.

Note for submitters who use Overleaf: Please refer to [their help documentation](https://www.overleaf.com/learn/how-to/How_do_I_download_the_automatically_generated_files_(e.g._.bbl%2C_.aux%2C_.ind%2C_.gls)_for_my_project%3F_My_publisher_asked_me_to_include_them_in_my_submission) regarding how to prepare your document for submission to arXiv.

<span id="bibtex"></span>

### Include `.bbl` files if you use BibTeX

We do not run BibTeX in the auto-TeXing procedure. If you use it, include in your submission the `.bbl` file that
BibTeX produces on your own machine; otherwise your references will not come out correctly. We do not run BibTeX
because the `.bib` database files can be quite large, and the only thing necessary to resolve the references for
a given paper is the `.bbl` file. You may still include them if you wish, but they must also match your .tex file name.

The name of the `.bbl` file _must_ match the name of the main `.tex` file for the system to process the references
correctly.

Note that packages such as `xr` and `xref` that rely on the `\externaldocument` command will not work in arXiv.
They require the presence of a `.aux` file in order to set up their linking structure. Since our TeX system
deletes the `.aux` files between tex runs, packages that need these files to be present will not function correctly,
and will not report any critical error during processing. Instead, we require that you update your `.bbl` files to
include the appropriate references for both documents.

Note for submitters who use Overleaf: Please refer to [their help documentation](https://www.overleaf.com/learn/how-to/How_do_I_download_the_automatically_generated_files_(e.g._.bbl%2C_.aux%2C_.ind%2C_.gls)_for_my_project%3F_My_publisher_asked_me_to_include_them_in_my_submission) regarding how to prepare
your document for submission to arXiv.

<span id="biblatex"></span>

### Potential problems with biblatex `.bbl` files

#### The `.bbl` file and paper submission were produced by different programs

Biblatex can run on a dedicated Biber backend or BibTeX; however, when submitting a biblatex `.bbl` file,
your paper and `.bbl` file must be created by the same program. e.g.

-   If you use biblatex with Biber as a backend to produce your document, then your document will expect
  a `.bbl` produced by Biber.

-   If you use biblatex with BibTeX as a backend to produce your document, then your document will expect
  a `.bbl` produced by BibTeX.

Do not mix and match papers produced by Biber with a .bbl produced by BibTeX or vice versa. This will only
result in errors and frustration.
[Lean more information about biblatex, BibTeX and Biber.](https://tex.stackexchange.com/questions/429436/making-the-arxiv-accept-a-bibtex-bbl-may-2018/429445#429445)

#### The `.bbl` file version is not compatible with biblatex or Biber on arXiv

When uploading the .bbl file for biblatex, it must be compatible with the version of biblatex or Biber on the arXiv
at the present time. If your .bbl for biblatex is not compatible, then your submission will have errors.
During submission, you should see a warning about incompatible bbl versions.
[View arXiv's current version of TeXLive.](https://info.arxiv.org/help/faq/texlive.html)

To be more specific: arXiv uses TeX Live 2023, which includes biblatex 3.19, Biber 2.19, and uses
the bbl format 3.2. TeX Live 2024 and 2025 include biblatex 3.20, Biber 2.20, and use bbl format 3.3.

We have taken steps to ensure that both bbl formats, 3.2 (TeX Live 2023) and 3.3 (TeX Live 2024 and 2025),
are supported by arXiv.

<span id="makeindex"></span>

### Include `.ind` files if you use `makeindex`

We do not run `makeindex` in the auto-TeXing procedure. If you use it, include in your submission the `.ind`
file that `makeindex` produces on your own machine; otherwise your index will not appear.

It is difficult to automatically perform `makeindex` processing to the authors' expectations because of the
multiple optional arguments and optional style selections. Therefore, arXiv asks authors to provide their
pre-processed `.ind` file(s) along with their (La)TeX source file(s).

Note for submitters who use Overleaf: Please refer to
[their help documentation](https://www.overleaf.com/learn/how-to/How_do_I_download_the_automatically_generated_files_(e.g._.bbl%2C_.aux%2C_.ind%2C_.gls)_for_my_project%3F_My_publisher_asked_me_to_include_them_in_my_submission)
regarding how to prepare your document for submission to arXiv.


<span id="glossary"></span>

### Include your `.gls` or `.nls` if you use any glossary or nomenclature packages

Similar to [index](#makeindex) files, we do not process `.glo` or `.nlo` into the resultant `.gls` or `.nls` files.
You must provide these files if you have any special nomenclature in your document.

Note for submitters who use Overleaf: Please refer to
[their help documentation](https://www.overleaf.com/learn/how-to/How_do_I_download_the_automatically_generated_files_(e.g._.bbl%2C_.aux%2C_.ind%2C_.gls)_for_my_project%3F_My_publisher_asked_me_to_include_them_in_my_submission)
regarding how to prepare your document for submission to arXiv.

<span id="mistakes"></span>

### Avoid mistakes in the text

Common mistakes can be avoided by following some simple [guidelines](faq/mistakes.md).
If your submission does not TeX properly, you will receive the log from our TeX processing at the _Process_ step.
The information contained in this complete log should be sufficient to identify the problem, so examine it
carefully; check the end of the log for TeX errors. Be sure to
[note any programmatically changed](faq/mistakes.md#space_filenames) filenames during file upload.

<span id="jhep3"></span>

### Problems with special TeX characters in hyperlinks (URLs) -- in particular JHEP3.cls

If hyperlinks for URLs containing '#' appear as '\\#' in arXiv generated PDF, the macro package being used
to generate these hyperlinks does not properly escape special characters in pdf strings. Either refer to
the [CTAN website](https://ctan.org/) for detailed information about the current hyperTeX or define the
URLs with the following workaround: instead of _e.g._:

> `\href{http://example.com/some-page.html\#destination}{destination}`

use:

> `\href{http://example.com/some-page.html\string#destination}{destination}`


If you use macros like:

> `\newcommand{\link}[2]{\href{http://example.com/some-page.html\##1}{#2}`

define:

> ``\bgroup\catcode`\#=12\gdef\hash{#}\egroup \newcommand{\link}[2]{\href{http://example.com/some-page.html\hash #1}{#2}``

instead.

<span id="hidden"></span>

### Hidden files will be deleted upon announcement

Please do not use hidden files or directories in your source package. These hidden files (i.e. files or directories
beginning with a period character, such as `.cache/`) will be deleted upon announcement, but *may* work at the
_Process_ or _Preview_ submission stages. The rationale being that such files may cruft from version control
systems, etc. and should not be a part of an archival version of your source. This means that any packages
that allow for or rely upon these structures (e.g. `minted.sty`) may function on your machine,
but will fail once announced.
