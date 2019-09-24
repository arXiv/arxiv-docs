Considerations for TeX Submissions
==================================

*   [Submissions are automatically processed](#autoproc)
*   [Considerations for (La)TeX submissions](#latex)
*   [Considerations for PDFLaTeX submissions](#pdflatex)
*   [We probably have your style files or macros](#wegotem)
*   [Do not submit in double-spaced "referee" mode](#double)
*   [Prepare the references carefully](#refs)
*   [Include `.bbl` files if you use BibTeX](#bibtex)
*   [Include `.ind` files if you used `makeindex`](#makeindex)
*   [Include `.gls` files if you have a glossary](#glossary)
*   [Supplemental material](#autoignore)
*   [Avoid mistakes in the text](#mistakes)
*   [Problems with special TeX characters in hyperlinks (URLs) -- in particular JHEP3.cls](#jhep3)

* * *
<span id="autoproc"></span>

### Submissions are automatically processed

Your (La)TeX, AMS(La)TeX, or PDFLaTeX submission will be processed automatically by our AutoTeX software.

This is a complex task, and the processing does not always lead to the desired or expected results. It is important for you, the author/submitter, to carefully check and verify the resulting PDF. You will be required to view the PDF during the submission process before you will be able to complete your submission.

You can submit a collection of TeX input/include files, e.g. separate chapters, foreword, appendix, etc, and custom macros ([see below](#wegotem)) packaged in a (possibly compressed) `.tar` or `.zip` file. AutoTeX will generally figure out how to properly process multi-part submissions, and you don't need to adhere to special packaging rules or naming conventions for your tex files. However, there are certain caveats. Naming your primary (or toplevel) file `ms.tex` will cause AutoTeX to always process that file first. Otherwise, tex files will be processed in _alphanumeric order._

That said, it is important that you do not include extraneous files (including unused figure files), leftover files, backup files, anything which does not belong to the paper you are submitting or is not needed for processing. Do not include journal templates, referee letters, or man pages. Tidy your submission before you pack it up.

You must submit any figures that go along with your paper. We recommend that you use appropriate TeX commands to include the figures inline with your paper (see below), as this is more readable than separate or appended figures.

_Note:_ In the past, it was possible to include a generic arXiv identifier in the TeX source that the processor would automatically translate into the identifier of the current submission. This practice is no longer necessary, nor supported. All TeX-type submissions receive the arXiv watermark, including the canonical identifier, version number, primary classification, and a link back to the correct version on the arXiv site. Again, `arch-ive/yymmnnn` (and, by extension, `yymm.nnnnn`) will _not_ be translated to the correct identifier for your submission.

<span id="latex"></span>

### Considerations for (La)TeX submissions

By default, LaTeX files are processed using LaTeX2e (the current version of LaTeX). Although there is a LaTeX2.09 compatibility mode, it is highly recommended that you use LaTeX2e whenever possible, to take advantage of all its features and improvements and to avoid complications which may arise in compatibility mode (note that LaTeX2e has been the default latex version for many years).

If you have a file named foo.tex, then do not include any associated auxiliary file or intermediate or resulting output file, e.g. foo.ps (or foo.aux, foo.log, foo.toc, foo.lot, foo.lof, foo.dvi, foo.pdf) in your submission. These will be automatically removed to allow the creation of an output file from your TeX file. Index (`.ind`) and processed bibtex (`.bbl`) files are an exception, [see below](#bibtex).

#### Figure inclusion in LaTeX submissions

Note that TeX/LaTeX can only include (encapsulated) PostScript (**.ps** or **.eps**), figures directly. Other formats are not supported in native (La)TeX. See [Useful Software](/help/bitmap/software) for figure conversion tools. If you are making use of [PDFLaTeX](#pdftex) you may embed your `.pdf, .png, .jpg` figures using the same mechanisms.

The most flexible and robust figure inclusion is provided by the `graphics` and `graphicx` packages and the `\includegraphics` command defined therein. We highly recommend you use them for your figure inclusion. arXiv does not provide the `psfig` package any longer. You must include your own `psfig.sty` if you use it. In general, if things go wrong or don't look as desired you may have to include your version of [older macros](/help/faq/mistakes#old_style).

Note that some software will permit you to include a mix of PostScript and PDFLaTeX-compatible figures and will perform the conversions to the appropriate format for you on the fly. arXiv does not permit such software to run during the AutoTeX processing. Why? It is possible for conversion issues to arise that can alter the scientific meaning or interpretation of your figure. Rather than invite such possibilities, we require that you use a unified figure format.

#### Separate figures with LaTeX submissions

Figures in **jpeg**, **png**, or **gif** format may be submitted alongside native (La)TeX submissions provided that they are **not** included in the source file.. PDF or other formats not listed above are not permitted with (La)TeX submission; use [PDFLaTeX](#pdflatex) instead for PDF, jpeg, or png figures.

Figures which are not incorporated in the main body of the paper will be listed separately. They should be given names of the form `figure<number><optional letter>.ext`, e.g. `figure1.jpg`, `figure2a.gif`, `figure2b.png`, so that they can be automatically sorted into the correct order for the "combined figures" link.

#### Figure inclusion in plain TeX

For plain TeX submissions, use the plain tex interface to the graphics package (`graphicx.tex`) or a macro package like `epsf` or `epsfig`.

arXiv does not presently support PDFTeX.

<span id="pdflatex"></span>

### Considerations for PDFLaTeX submissions

arXiv fully supports and automatically recognizes PDFLaTeX. You can ensure pdflatex processing by setting the flag **\\pdfoutput=1** within the first 5 lines of the preamble of the main `.tex` file. You should not need any other special flag.

*   Should you need conditional branching in your source, use the [ifpdf](ftp://tug.ctan.org/pub/tex-archive/macros/latex/contrib/oberdiek/ifpdf.pdf) package. Do not re-invent the wheel. [ifpdf](ftp://tug.ctan.org/pub/tex-archive/macros/latex/contrib/oberdiek/ifpdf.pdf) provides a robust and well tested mechanism to distinguish between pdflatex in pdf mode and other modes or engines.
*   Some packages may require a particular back-end driver, in the form of a package option, e.g. `\usepackage[pdftex]{...}`. However, the graphics and hyperref packages determine the proper driver automatically; you don't have to make this explicit choice and should not do so to avoid conflicts.
*   You can use the full range of pdf specific [hypertex](ftp://tug.ctan.org/pub/tex-archive/macros/latex/contrib/hyperref/doc/manual.pdf) [options](ftp://tug.ctan.org/pub/tex-archive/macros/latex/contrib/hyperref/doc/options.pdf) to augment metadata in the PDF file, e.g. `\hypersetup{pdfauthor={some author},pdftitle={eye-catching title}}`.
*   Figures can be included in **JPEG**, **PNG**, or **PDF** format with the standard graphics package. For security reasons arXiv does not allow for automated format conversion, so your figures must be in the proper format already.
*   Unlike native LaTeX, the default output format for PDFLaTeX is PDF, with no intermediate DVI or PostScript. Thus, these formats are _not_ available for download for PDFLaTeX submissions.

<span id="wegotem"></span>

### We probably have your style files or macros

You probably do not need to submit any style files since we have copies of all the common scientific style files. Try submitting without style files. If you find that this does not work because we do not have the style file you need, then you can include the necessary style file in your submission and resubmit.

_Note:_ A&A, pstricks, elsart, and by now to a lesser degree [AMSLaTeX](/help/faq/amslatex2000), iopart, and revtex4 users, you may need to include your own version of those style/class files with your submission. arXiv can process standard `zip` and `tar` files. Simply bundle the necessary files together with your (La-)TeX file(s) in the same directory (or do a less convenient multi-file submission).

Do not ask us to update those particular style and class files in our installation. They are not backwards compatible.

<span id="double"></span>

### Do not submit in double-spaced "referee" mode

Avoid inadvertently submitting your paper in double-spaced referee mode, since it wastes paper on a global scale. Readers prefer to have a compact single-spaced version, as it would appear in a printed journal.

<span id="refs"></span>

### Prepare the references carefully

We strongly encourage you to include arXiv's `YYMM.NNNNN`, [identifiers](/help/arxiv_identifier) in your reference list for both published and unpublished papers. Note also that many publishers allow e-print identifiers to appear in the references of papers submitted.

If you use standard identifiers of the form 1510.00322, arXiv:1510.00322, 0901.0512, arXiv:0901.0512, hep-ph/9409201 or arXiv:hep-ph/9409201, they can be easily harvested by automatic software. For example,

> `\bedim{upsilon}
> C.T.H. Davies {\em et al.}, Phys. Rev {\bf D} 50 (1994) 6963, hep-lat/9406017.`

Do not include extraneous font commands, spaces, tildes, braces or line-breaks within the e-print identifier: this will cause your references to be missed by automated extraction software. See also notes about [references to and in arXiv documents](/help/faq/references) and [collection of references at INSPIRE](http://inspirehep.net/). Use of e-print identifiers is a significant aid to the INSPIRE database. It also facilitates automatic network hyperlinks of references from within papers.

If you use BibTeX there are some BibTeX styles which support e-print identifiers (see [https://arxiv.org/hypertex/bibstyles](/hypertex/bibstyles)).

If you are submitting a group of `.tex` files, automated reference extraction by INSPIRE and others will be more accurate and faster if your references are all in one file. This file should have the `\begin{thebibliography}` or similar command within it, and should be called `foo.bbl` to correspond to a given `foo.tex` source file.

<span id="bibtex"></span>

### Include `.bbl` files if you use BibTeX

We do not run BibTeX in the auto-TeXing procedure. If you use it, include in your submission the `.bbl` file that BibTeX produces on your own machine; otherwise your references will not come out correctly. We do not run BibTeX because the `.bib` database files can be quite large, and the only thing necessary to resolve the references for a given paper is the `.bbl` file. You may still include them if you wish, but they must also match your .tex file name.

The name of the `.bbl` file _must_ match the name of the main `.tex` file for the system to process the references correctly.

Note that packages such as `xr` and `xref` that rely on the `\externaldocument` command will not work in arXiv. They require the presence of a `.aux` file in order to set up their linking structure. Since our AutoTeX system deletes the `.aux` files between tex runs, packages that need these files to be present will not function correctly, and will not report any critical error during processing. Instead we require that you update your `.bbl` files to include the appropriate references for both documents.

<span id="makeindex"></span>

### Include `.ind` files if you use `makeindex`

We do not run `makeindex` in the auto-TeXing procedure. If you use it, include in your submission the `.ind` file that `makeindex` produces on your own machine; otherwise your index will not appear.

It is difficult to automatically perform `makeindex` processing to the authors' expectations because of the multiple optional arguments and optional style selections. Therefore arXiv asks authors to provide their pre-processed `.ind` file(s) along with their (La)TeX source file(s).

<span id="glossary"></span>

### Include your .gls if you use a glossary

Similar to [index](#makeindex) files, we do not process `.glo` into the resultant `.gls` files. You must provide these files if you have any special nomenclature in your document.

<span id="autoignore"></span>

### How to include supplemental material

TeX-based supplemental material should be included in the main document root directory, and will be compiled into the final output pdf. Both files must use the same TeX-engine (either both latex, both pdflatex, or both plain tex). You may either create a [`00README.XXX` file](/help/00README) which specifies the top-level file, or they will be assembled in alphanumeric order. For example, given the following files:

```
  ./ms.tex
  ./ms.bbl
  ./myfig.eps
  ./supplement.tex
  ./supplement.bbl
```

contained within your .zip or .tar.gz file the final pdf would place the contents of your `ms.tex` file first. We recommend assembling your files in this manner rather than placing any compiled pdf into an [ancillary files](/help/ancillary_files) directory, as these are not indexed for discovery and access.

We highly recommend that if you plan to include any non-TeX files with your source package that you include them as [ancillary files](/help/ancillary_files) inside their own `/anc` directory off your document's root directory. For additional information please see that [help page](/help/ancillary_files). For legacy reasons, we still support individual file inclusion, as follows.

If your submission includes any plain text files which should not be processed (e.g. Fortran source code, data files), and you don't want them available for separate download as [ancillary files](/help/ancillary_files) then make the first line of those files

> `%auto-ignore`

This ensures that they will be ignored by the auto-postscript generator.

**NOTE**: `pdflatex` users who submit using the above formatting recommendations will have any final hyperlinking removed due to a [known issue](http://mirrors.ctan.org/macros/latex/contrib/pdfpages/pdfpages.pdf#page=2) in the `pdfpages.sty` package. 

<span id="mistakes"></span>

### Avoid mistakes in the text

Common mistakes can be avoided by following some simple [guidelines](faq/mistakes). If your submission does not TeX properly, you will receive the log from our auto-TeXing script at the _Process_ step. The information contained in this complete log should be sufficient to identify the problem, so examine it carefully; check the end of the log for TeX errors.

<span id="jhep3"></span>

### Problems with special TeX characters in hyperlinks (URLs) -- in particular JHEP3.cls

If hyperlinks for URLs containing '#' appear as '\\#' in arXiv generated PDF, the macro package being used to generate these hyperlinks does not properly escape special characters in pdf strings. Either use the [hyperref package](/hypertex/) or define the URLs with the following workaround:
instead of _e.g._:

> `\href{http://example.com/some-page.html\#destination}{destination}`

use:

> `\href{http://example.com/some-page.html\string#destination}{destination}`


If you use macros like:

> `\newcommand{\link}[2]{\href{http://example.com/some-page.html\##1}{#2}`

define:

> ``\bgroup\catcode`\#=12\gdef\hash{#}\egroup \newcommand{\link}[2]{\href{http://example.com/some-page.html\hash #1}{#2}``

instead.
