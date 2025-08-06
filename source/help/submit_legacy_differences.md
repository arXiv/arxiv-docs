### Legacy Submission System 

This page explains our older legacy submission system (Submissions 1.0) and how it differs from our current practices in Submission 1.5. While arXiv's submission process has since been updated, this information can still be useful for understanding older submissions or resolving specific issues related to them. Keep in mind that the guidelines and behaviors described here apply mainly to the legacy system and may not be relevant to the current arXiv submission workflow.

 
 *   [Submission 1.0 and 1.5 Comparison](#comparison)
 *   [Submission 1.0 and 1.5 differences in detail](#detail)
 *   [Submissions are automatically processed](#autoproc)
 *   [Considerations for (La)TeX submissions](#latex)
 *   [Considerations for PDFLaTeX submissions](#pdflatex)
 *   [We probably have your style files or macros](#wegotem)
 *   [Do not submit in double-spaced "referee" mode](#double)
 *   [Prepare the references carefully](#refs)
 *   [Include `.bib` or `bbl` files if you use BibTeX/Biber](#bibtex)
 *   [Potential problems with biblatex `.bbl` files](#biblatex)
 *   [Include `.ind` files if you used `makeindex`](#makeindex)
 *   [Include `.gls` or `.nls` files if you have a glossary or nomenclature section](#glossary)
 *   [Supplemental material](#autoignore)
 *   [Avoid mistakes in the text](#mistakes)
 *   [Problems with special TeX characters in hyperlinks (URLs) -- in particular JHEP3.cls](#jhep3)
 *   [Hidden files will be deleted upon announcement](#hidden)
 
 * * *

<span id="comparison"></span>
### Submission 1.0 and 1.5 Comparison
For a quick overview of the changes to our Submission system view our chart below.

| **Feature** | **Submission System 1.0** | **Submission System 1.5** |
| :---------  | :-----------------------  | :------------------------ |
|**Bundled LaTeX Packages**| Supplied ~70 LaTeX packages and class files (many outdated) | Only provides packages included in the current [TeX Live release](faq/texlive.md). Authors with journal style files must now include them with their TeX source. |
|**PDF Compilation**| Tried multiple TeX processors to compile | Uses only the specific TeX processor set in the Review Files step |
|**TeX Versioning**| Infrequent updates (years between updates) | Follows annual TeX Live releases going forward dependent upon arXiv resources |
|**File Detection**| Detects toplevel files by looking for `\documentclass` or `\bye`. All `.tex` files attempted, if none found. | Scan for toplevel files using upt to 40 standard commands.|
|**Extraneous  File Detection**| Did not detect files unrelated to the submission | Detects potentially unused files; flagging them for review |
|**Handling Multiple .tex Files**| Compiled all `.tex` files with `\documentclass` and appended extraneous postscripts figures at the end. Plain TeX, processed by looking for `\bye.` | At the start, assumes just one top-level TeX file.  Submitter can add additional top-level TeX files in the Review Files interface. These will be compiled and the results appended to the output document.  It is preferred that the submitter use `\include` or `\input` directives to embed other TeX files in a document.  For special cases not supported by either of those options please refer to: [The `00README.XXX` file format](00README.md). |
|**Image Files (JPG, PNG, PDF)**| Appended image files verbatim to final PDF in postscript mode, otherwise image files remain in source directory | Images must be included using standard [TeX commands](https://latex-tutorial.com/tutorials/figures/).|
|**hyperref Package**| Automatically added if not present, skipped if there is an error |  No longer modifies IDs; authors should use `\href{}` explicitly, or packages that define it. |
|**Maintenance**| Complex, opaque process | Simpler, more transparent and maintainable system |
|**Transparency**| Opaque and convoluted. It was nearly impossible for authors to build the documents locally in the same manner as arXiv. | The 00README.json file documents all the details used to build a paper, and other services can make use of this format. |


<span id="detail"></span>
### Submission 1.0 and 1.5 differences in detail
 

 1. Submission 1.0 would try different versions of TeX to see which one successfully builds a PDF. From this point on, we will only use the version of TeX currently in use by arXiv.
    - Our plan is for arXiv's "current" version to closely follow the annual TeX Live releases. In the past, we often went several years between TeX updates.
 1. Submission 1.0 would attempt to determine which files in a submission were part of the main document and which were not. We are no longer going to do this.
      - If there were multiple files ending in `.tex`, it would create PDFs for those extra files and append them to main paper's PDF. Now, if authors want a .tex file to be part of their main paper, they should use \include or \input commands to include the file. See [https://www.baeldung.com/cs/latex-include-vs-input](https://www.baeldung.com/cs/latex-include-vs-input).
      - If authors need the previous apppend behavior for a submission with multiple `.tex` files, please follow the instructions here: [The `00README` File Format](https://info.arxiv.org/help/00README.html).
      - If image files (JPG, PNG, PDF) were found, they would be rendered and appended verbatim to the main paper's PDF. If authors want to include images anywhere in their paper, they should use the normal TeX contructs for this. See [https://latex-tutorial.com/tutorials/figures/](https://latex-tutorial.com/tutorials/figures/). 
  
  1. Submission 1.0 would preload the LaTeX hyperref package to LaTeX submissions that did not already include it. This package adds various references to active links in the PDF document (e.g., clicking on a reference jumps to the entry in the bibliography section). We will no longer automatically try to add this package. (Note – before you add a \usepackage{hyperref} to your main TeX file, check to see if the template you are using already has a reference by checking the PDF for clickable links; most do).
 1. Submission 1.0 would look for any references in a paper that looked like an arXiv paper ID (such as arXiv:2402.08954, or 2402.08954) and turn the ID into a hyperlink to the paper on arXiv. We will not do that anymore. Authors should just write out `\href{https://doi.org/10.48550/arXiv.2402.08954}{2402.08954}`. See the [Hyperref documentation for more info](https://mirror.math.princeton.edu/pub/CTAN/macros/latex/contrib/hyperref/doc/hyperref-doc.html).
      - While changes like these arguably made for a better viewing experience, they also made our TeX processing complex and opaque. When we make modifications to user source like this, the paper on arXiv presents differently than the paper on the user's local machine.

1. arXiv presently has about 70 LaTeX packages we supply that papers can use without needing to upload their own copies. We have found that only 0.65% of recent submissions depend on this and, in some cases these packages are woefully out of date.
      - We are eliminating these packages and providing only packages that are distributed with each annual TeX Live release. If you use any packages or style files that are not part of arXiv's current version of TeX Live, please upload them with your submission.
 
At present, the documentation below is still largely accurate, however we are actively reexamining our (La)TeX processing, and there may be more changes in the future. If you have suggestions for changes we should make, please respond to the post about this change on the [arXiv Blog](https://blog.arxiv.org/).

<span id="autoproc"></span>

### Submissions are automatically processed

Your (La)TeX, AMS(La)TeX, or PDFLaTeX submission will be processed automatically by our AutoTeX software.

This is a complex task, and the processing does not always lead to the desired or expected results. It is important for you, the author/submitter, to carefully check and verify the resulting PDF. You will be required to view the PDF during the submission process before you will be able to complete your submission.

You can submit a collection of TeX input/include files, e.g. separate chapters, foreword, appendix, etc, and custom macros ([see below](#wegotem)) packaged in a (possibly compressed) `.tar` or `.zip` file. AutoTeX will generally figure out how to properly process multi-part submissions, and you do not need to adhere to special packaging rules or naming conventions for your tex files. However, there are certain caveats. Naming your primary (or toplevel) file `ms.tex` will cause AutoTeX to process that file first in (La)TeX mode. Under PDFLaTeX modes, and in all other cases, the tex files will be processed in _alphanumeric order._

That said, it is important that you do not include extraneous files (including unused figure files), leftover files, backup files, anything which does not belong to the paper you are submitting or is not needed for processing. Do not include journal templates, referee letters, or man pages. Tidy your submission before you pack it up.

You must submit any figures that go along with your paper. We recommend that you use appropriate TeX commands to include the figures inline with your paper (see below), as this is more readable than separate or appended figures.

_Note:_ arXiv recommends against using the `\today` macro in the standard `\date` field. Because pdf are occasionally rebuilt this date will change and may cause confusion, as outlined in our [FAQ page for this topic](faq/today.md). To avoid this issue, do not use it unless you are comfortable with the displayed date changing periodically. 

<span id="latex"></span>

### Considerations for (La)TeX submissions

By default, LaTeX files are processed using LaTeX2e (the current version of LaTeX). Although there is a LaTeX2.09 compatibility mode, it is highly recommended that you use LaTeX2e whenever possible, to take advantage of all its features and improvements and to avoid complications which may arise in compatibility mode (note that LaTeX2e has been the default latex version for many years).

If you have a file named foo.tex, then do not include any associated auxiliary file or intermediate or resulting output file, e.g. foo.ps (or foo.aux, foo.log, foo.toc, foo.lot, foo.lof, foo.dvi, foo.pdf) in your submission. These will be automatically removed to allow the creation of an output file from your TeX file. Index (`.ind`) files are an exception, [see below](#bibtex).

<span id="figures"></span>
#### Figure inclusion in LaTeX submissions

Note that TeX/LaTeX can only include (encapsulated) PostScript (**.ps** or **.eps**), figures directly. Other formats are not supported in native (La)TeX. See [Useful Software](bitmap/software.md) for figure conversion tools. If you are making use of [PDFLaTeX](#pdftex) you may embed your `.pdf, .png, .jpg` figures using the same mechanisms. Please note that arXiv does not perform "on the fly" figure file conversion during tex processing (i.e. "`-eps-converted-to.pdf`" files being present in your source directory). You must perform such conversion yourself, before uploading, updating any effected inclusion command. This process ensures that you have examined the results of any figure conversion to ensure that the figures still contain scientifically correct information and that arXiv is not responsible for the scientific accuracy of your figures.

The most flexible and robust figure inclusion is provided by the `graphics` and `graphicx` packages and the `\includegraphics` command defined therein. We highly recommend you use them for your figure inclusion. arXiv does not support the `psfig` package any longer. You may not include your own `psfig.sty`, as this will cause your source to fail. The functionality it required was deprecated prior to
[TeXLive 2016](http://tug.org/pipermail/texhax/2016-October/022493.html) and this is not something we can control. Older submissions that have already been announced with the `psfig` package will still work. Please update your source to a more modern inclusion command.


Note that some software will permit you to include a mix of PostScript and PDFLaTeX-compatible figures and will perform the conversions to the appropriate format for you on the fly. arXiv does not permit such software to run during the AutoTeX processing. Why? It is possible for conversion issues to arise that can alter the scientific meaning or interpretation of your figure. Rather than invite such possibilities, we require that you use a unified figure format.

#### Avoid embedding JavaScript in your PDF files

Do not include embedded JavaScript such as animated gifs, movies, or HTML in your PDF. Submissions with embedded JavaScript are automatically rejected due to the potential security risks posed to arXiv systems. 
- Submit all movies and animated GIFS as separate(non-JavaScript) ancillary files. 
- Remove or disable JavaScript when building your PDF or generate PDFs using standard tools such as Adobe Distiller. 


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
*   Some packages may require a particular back-end driver, in the form of a package option, e.g. `\usepackage[pdftex]{...}`. However, the graphics and hyperref packages determine the proper driver automatically; you do not have to make this explicit choice and should not do so to avoid conflicts.
*   You can use the full range of pdf specific [hypertex](ftp://tug.ctan.org/pub/tex-archive/macros/latex/contrib/hyperref/doc/manual.pdf) [options](ftp://tug.ctan.org/pub/tex-archive/macros/latex/contrib/hyperref/doc/options.pdf) to augment metadata in the PDF file, e.g. `\hypersetup{pdfauthor={some author},pdftitle={eye-catching title}}`
*   Figures can be included in **JPEG**, **PNG**, or **PDF** format with the standard graphics package. For security reasons arXiv does not allow for automated format conversion, so your figures must be in the proper format already.
*   Unlike native LaTeX, the default output format for PDFLaTeX is PDF, with no intermediate DVI or PostScript. Thus, these formats are _not_ available for download for PDFLaTeX submissions.

<span id="wegotem"></span>

### We probably have your style files or macros

You probably do not need to submit any style files since we have copies of all the common scientific style files. Try submitting without style files. If you find that this does not work because we do not have the style file you need, then you can include the necessary style file in your submission and resubmit.

_Note:_ A&A, pstricks, elsart, and by now to a lesser degree [AMSLaTeX](faq/amslatex2000.md), iopart, and revtex4 users, you may need to include your own version of those style/class files with your submission. arXiv can process standard `zip` and `tar` files. Simply bundle the necessary files together with your (La-)TeX file(s) in the same directory (or do a less convenient multi-file submission).

Do not ask us to update those particular style and class files in our installation. They are not backwards compatible.

<span id="double"></span>

### Do not submit in double-spaced "referee" mode

Avoid inadvertently submitting your paper in double-spaced referee mode, since it wastes paper on a global scale. Readers prefer to have a compact single-spaced version, as it would appear in a printed journal.

<span id="refs"></span>

### Prepare the references carefully

We strongly encourage you to include arXiv's `YYMM.NNNNN`, [identifiers](arxiv_identifier.md) in your reference list for both published and unpublished papers. Note also that many publishers allow e-print identifiers to appear in the references of papers submitted.

If you use standard identifiers of the form 1510.00322, arXiv:1510.00322, 0901.0512, arXiv:0901.0512, hep-ph/9409201 or arXiv:hep-ph/9409201, they can be easily harvested by automatic software. For example,

> `\bedim{upsilon}
> C.T.H. Davies {\em et al.}, Phys. Rev {\bf D} 50 (1994) 6963, hep-lat/9406017.`

Do not include extraneous font commands, spaces, tildes, braces or line-breaks within the e-print identifier: this will cause your references to be missed by automated extraction software. See also notes about [references to and in arXiv documents](faq/references.md) and [collection of references at INSPIRE](https://inspirehep.net/). Use of e-print identifiers is a significant aid to the INSPIRE database. It also facilitates automatic network hyperlinks of references from within papers.

If you use BibTeX there are some BibTeX styles which support e-print identifiers (see [BibTeX and Eprints](hypertex/bibstyles/index.md)).

If you are submitting a group of `.tex` files, automated reference extraction by INSPIRE and others will be more accurate and faster if your references are all in one file. This file should have the `\begin{thebibliography}` or similar command within it, and should be called `foo.bbl` to correspond to a given `foo.tex` source file.

Note for submitters who use Overleaf: Please refer to [their help documentation](https://www.overleaf.com/learn/how-to/How_do_I_download_the_automatically_generated_files_(e.g._.bbl%2C_.aux%2C_.ind%2C_.gls)_for_my_project%3F_My_publisher_asked_me_to_include_them_in_my_submission) regarding how to prepare your document for submission to arXiv.

<span id="bibtex"></span>

### Include `.bib` or `bbl` files if you use BibTeX/Biber

arXiv now provides support for bib file processing using various processors like `bibtex` and `biber`.

It is also possible to upload a pre-generated `.bbl` file for your paper. In this case, the name of the `.bbl` file _must_ match the name of the main `.tex` file for the system to process the references correctly.

Note that packages such as `xr` and `xref` that rely on the `\externaldocument` command will not work in arXiv. They require the presence of a `.aux` file in order to set up their linking structure. Since our AutoTeX system deletes the `.aux` files between tex runs, packages that need these files to be present will not function correctly, and will not report any critical error during processing. Instead we require that you update your `.bbl` files to include the appropriate references for both documents.

Note for submitters who use Overleaf: Please refer to [their help documentation](https://www.overleaf.com/learn/how-to/How_do_I_download_the_automatically_generated_files_(e.g._.bbl%2C_.aux%2C_.ind%2C_.gls)_for_my_project%3F_My_publisher_asked_me_to_include_them_in_my_submission) regarding how to prepare your document for submission to arXiv.

<span id="biblatex"></span>

### Potential problems with biblatex `.bbl` files

#### The `.bbl` file and paper submission were produced by different programs

Biblatex can run on a dedicated Biber backend or BibTeX; however, when submitting a biblatex `.bbl` file, your paper and `.bbl` file must be created by the same program. e.g.

- If you use biblatex with Biber as a backend to produce your document, then your document will expect a `.bbl` produced by Biber.

- If you use biblatex with BibTeX as a backend to produce your document, then your document will expect a `.bbl` produced by BibTeX.

Do not mix and match papers produced by Biber with a .bbl produced by BibTeX or vice versa. This will only result in errors and frustration. [Lean more information about biblatex, BibTeX and Biber.](https://tex.stackexchange.com/questions/429436/making-the-arxiv-accept-a-bibtex-bbl-may-2018/429445#429445)

#### The `.bbl` file version is not compatible with biblatex or Biber on arXiv

We are currently supporting `.bbl` files generated from `biber` in format 3.2 and 3.3, which spans TeX Live 2022 to TeX Live 2025. Do not upload `.bbl` files in older or newer formats.

<span id="makeindex"></span>

### Include `.ind` files if you use `makeindex`

We do not run `makeindex` in the auto-TeXing procedure. If you use it, include in your submission the `.ind` file that `makeindex` produces on your own machine; otherwise your index will not appear.

It is difficult to automatically perform `makeindex` processing to the authors' expectations because of the multiple optional arguments and optional style selections. Therefore arXiv asks authors to provide their pre-processed `.ind` file(s) along with their (La)TeX source file(s).

Note for submitters who use Overleaf: Please refer to [their help documentation](https://www.overleaf.com/learn/how-to/How_do_I_download_the_automatically_generated_files_(e.g._.bbl%2C_.aux%2C_.ind%2C_.gls)_for_my_project%3F_My_publisher_asked_me_to_include_them_in_my_submission) regarding how to prepare your document for submission to arXiv.


<span id="glossary"></span>

### Include your `.gls` or `.nls` if you use any glossary or nomenclature packages

Similar to [index](#makeindex) files, we do not process `.glo` or `.nlo` into the resultant `.gls` or `.nls` files. You must provide these files if you have any special nomenclature in your document.

Note for submitters who use Overleaf: Please refer to [their help documentation](https://www.overleaf.com/learn/how-to/How_do_I_download_the_automatically_generated_files_(e.g._.bbl%2C_.aux%2C_.ind%2C_.gls)_for_my_project%3F_My_publisher_asked_me_to_include_them_in_my_submission) regarding how to prepare your document for submission to arXiv.


<span id="autoignore"></span>

### How to include supplemental material

TeX-based supplemental material should be included in the main document root directory, and will be compiled into the final output pdf. Both files must use the same TeX-engine (either both latex, both pdflatex, or both plain tex). The final output will be assembled in alphanumeric order. For example, given the following files:

```
  ./ms.tex
  ./ms.bbl
  ./myfig.eps
  ./supplement.tex
  ./supplement.bbl
```

contained within your .zip or .tar.gz file the final pdf would place the contents of your `ms.tex` file first. We recommend assembling your files in this manner rather than placing any compiled pdf into an [ancillary files](ancillary_files.md) directory, as these are not indexed for discovery and access. Note that adding a [`00README.XXX`](00README.md#toplevel) with a `toplevelfile` directive will only effect the processing order and not the final assembly order of the pdf. `pdflatex` users should also take care in naming conventions, as the final assembled pdf will always appear in alphanumeric order.

We highly recommend that if you plan to include any non-TeX files with your source package that you include them as [ancillary files](ancillary_files.md) inside their own `/anc` directory off your document's root directory. For additional information please see that [help page](ancillary_files.md). For legacy reasons, we still support individual file inclusion, as follows.

If your submission includes any plain text files which should not be processed (e.g. Fortran source code, data files), and you do not want them available for separate download as [ancillary files](ancillary_files.md) then make the first line of those files

> `%auto-ignore`

This ensures that they will be ignored by the auto-postscript generator.

**NOTE**: `pdflatex` users who submit using the above formatting recommendations will have any final hyperlinking removed due to a [known issue](http://mirrors.ctan.org/macros/latex/contrib/pdfpages/pdfpages.pdf#page=2) in the `pdfpages.sty` package.

Note for submitters who use Overleaf: Please refer to [their help documentation](https://www.overleaf.com/learn/how-to/How_do_I_download_the_automatically_generated_files_(e.g._.bbl%2C_.aux%2C_.ind%2C_.gls)_for_my_project%3F_My_publisher_asked_me_to_include_them_in_my_submission) regarding how to prepare your document for submission to arXiv.


<span id="mistakes"></span>

### Avoid mistakes in the text

Common mistakes can be avoided by following some simple [guidelines](faq/mistakes.md). If your submission does not TeX properly, you will receive the log from our auto-TeXing script at the _Process_ step. The information contained in this complete log should be sufficient to identify the problem, so examine it carefully; check the end of the log for TeX errors. Be sure to [note any programmatically changed](faq/mistakes.md#space_filenames) filenames during file upload.

<span id="jhep3"></span>

### Problems with special TeX characters in hyperlinks (URLs) -- in particular JHEP3.cls

If hyperlinks for URLs containing '#' appear as '\\#' in arXiv generated PDF, the macro package being used to generate these hyperlinks does not properly escape special characters in pdf strings. Either refer to the [CTAN website](https://ctan.org/) for detailed information about the current hyperTeX or define the URLs with the following workaround: instead of _e.g._:

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

Please do not use hidden files or directories in your source package. These hidden files (i.e. files or directories beginning with a period character, such as `.cache/`) will be deleted upon announcement, but *may* work at the _Process_ or _Preview_ submission stages. The rationale being that such files may cruft from version control systems, etc. and should not be a part of an archival version of your source. This means that any packages that allow for or rely upon these structures (e.g. `minted.sty`) may function on your machine, but will fail once announced.
