# Common Mistakes that cause Automated Processing to Fail

For information about our current TeX installation please see [Notes about arXiv's TeXLive Version](texlive.md).

### Look through these common mistakes if your TeX/LaTeX submission failed:

  - [Absolute filenames](#abs_filenames)
  - [Spaces and other inappropriate characters in filenames](#space_filenames)
  - [Missing style/macro files](#missing_macro)
  - [Last minute untested changes](#untested)
  - [User intervention](#intervention)
  - [Multiple files concatenated](#concatenated)
  - [Use of old or non-standard style files](#old_style)
  - [Style files incompatible with dvips](#dvips_clash)
  - [Sources that rely on something other than TeX or
    LaTeX](#other_formats)
  - [Use of unusual/uncommon fonts](#fonts)
  - [Unprotected `\cite` and other macros inside figure `\caption`
    commands, "`line too long`" error](#protect)
  - [Marking files to be ignored](#auto_ignore)
  - ["`! Missing number, treated as zero`" error](#bbox)
  - ["`Can't write subdir/file.aux`" and other problems with write
    permissions during TeX processing](#include_subdir)
  - ["`! Double subscript/superscript`" errors](#double_subscript)
  - [PDF conversion failure in papers with complex section
    structure](#bad_pdfmark)
  - [arXiv system attempts processing with PDFLaTeX for submissions
    which are regular latex](#ifpdf)
  - [Why does my submission fail the automatic TeXing procedure when I
    use Feynmf?](feynmf.md#overwrite)
  - [Mixed figure file types](#mixed)
  - ["`! LaTeX Error: Command \Bbbk already defined.`"](#Bbbk)
  - [Notes for using `minted.sty` in arXiv](#minted)
  - [bbl file version mismach](#bblmismatch)
  - [breqn and Labels might have changed problem](#breqn)
-----

  

<span id="abs_filenames"></span>
## Absolute filenames

When including figures/style/class/macro files, you must use
relative filenames instead of absolute filenames. For example,
    
  ``` 
      myfigure.png
  ```
    
is correct, while:
  
  ``` 
     /users/staff/fred/myarticle/myfigure.png
  ```
    
is not.
    
Absolute filenames make it impossible for anyone to use the source
without modifying it. Unless your TeX system happens to have the
same directory structure as ours, then our automated processing will
fail.
    
      
<span id="space_filenames"></span>
## Spaces and other inappropriate characters in filenames

Do not use spaces in filenames, in either your figure inclusion commands or directory names. Do not use common filesystem delimiters in file names (*i.e* `/`, `\`, `:`, etc.). Certain symbols such as the ampersand (`&`) can cause problems as well, and should be avoided. 

During file upload these examples will be programmatically converted to an underscore character (the `_` character) in the file names only. You are responsible for updating any inclusion or input commands in your source.  

<span id="missing_macro"></span>
## Missing style/macro files
Some authors write their own style/macro files (or modify standard
ones), but forget to include them with the source. Be sure to
include with the source any style/macro files that are not included in our current [TeX Live](texlive.md) release.

**Note:** non-standard style/macro files provided along with the
source must **NOT be attached** to a paper. Instead, submit them as
separate files, or use **tar** or **zip** to combine them with the
source files before submitting.

  

<span id="untested"></span>
## Last minute untested changes
All too often, an author will make last minute changes to the
source, but won't test it to see if the results will TeX correctly.
You can save yourself a lot of trouble by testing that everything
works properly before submitting your paper.

<span id="intervention"></span>
## User intervention
Our source to postscript conversion system (called "AutoTeX") is
*fully automated*. There is no genie present to answer questions
such as:

``` 
  Would you like (P)ortrait or (L)andscape ? - answer P/L
```

If your source needs to ask these types of question, please create a
file called `filename.inp` (where `filename` matches the file it is
to act on) that contains suitable responses.

Your `.inp` file can be first tested on your local machine by
running the following command:
 
``` 
  $ cat filename.inp | tex filename.tex
```



<span id="concatenated"></span> 
## Multiple files concatenated 
Do not submit several files all concatenated into one file, such as
the Scientific Workplace's `.rap` file type -- such files cannot be
separated automatically and may fail to process in unexpected ways.
Instead, please create a `.tar.gz` or `.zip` file.



<span id="old_style"></span> 
## Use of old or non-standard style files  
Style files change with time, and you (or we) might be using old
versions of style files. We try to keep up to date, so if problems
arise due to style files, please check that the version you are
using is current.

Some well-known style files, e.g., `epsf.sty` and `epsfig.sty`, have
been altered by TeX programmers, then uploaded to web sites under
the same filename. This is **very bad practice** and anti-social
behavior, since we end up with multiple versions of *standard*
styles. arXiv will make every effort to support the most recent
**and** official versions of standard style files.

As an example, the `graphics` and `graphicx` packages have been
standard since the release of LaTeX 2e and are the recommended
graphics inclusion macros. These packages provide the most portable
and reliable method of including graphics.

<span id="dvips_clash"></span> 
## Style files incompatible with dvips
Style files that are incompatible with `dvips`, e.g., `epsbox.sty`,
can cause problems. If the DVI requires exotic versions of `dvips`
(e.g., `jdvi2kps`) to produce postscript, then our automated system
will **fail**.

Please make every effort to avoid using non-standard styles and
`dvi2ps` utilities. Few people will be able to process papers in
these non-standard formats.



<span id="other_formats"></span> 
## Sources that rely on something other than TeX or LaTeX 
All papers should be formatted so they work with TeX or LaTeX (as
appropriate). If you use other formats (as opposed to style files or
macros), e.g., **AMS-TeX**, **AMS-LaTeX**, or **aatex**, then please
add the appropriate line to the top of the source, e.g.:

``` 
    %&amslplain
```

for **AMS-LaTeX** (based on amslatex version 1.1),

``` 
    \input amstex
```

or

``` 
    %&amstex
```

for **AMS-TeX**, and

``` 
    \input cp-aa.tex
```

or

``` 
    %&cp-aa
```

for Springer-Verlag's Plain TeX Astronomy & Astrophysics macros,
**cp-aa** (also known as **aatex**).

Anything that relies on something **other than TeX or (PDF)LaTeX**
will fail. At this time arXiv does not support processing with:
XeTeX and its variants including LuaTeX, LyX, or PDFTeX.



<span id="fonts"></span> 
## Use of unusual/uncommon fonts  
Authors should keep in mind that if they use unusual fonts, many
potential readers of their work won't have them installed.

Because it would require significant admin time to install and
maintain non-standard fonts, we do not generally support such fonts.



<span id="protect"></span> 
## Unprotected `\cite` and other macros inside figure `\caption` commands, "`line too long`" error
In LaTeX, any citations inside a figure `\caption` should be
protected using the `\protect` command; e.g., `\caption{Electron
spectral function from \protect\cite{spectral}}`. This delays the
expansion of the citation until the second latex pass, i.e., when
the reference has been defined.



<span id="auto_ignore"></span> 
## Marking files to be ignored 
If you need to include files in the source that should not be
processed by the automated system, you need to include a
[`00README file`](../../help/00README.md#ignore) with your submission.
See the previous link for the correct format to ignore files.



<span id="bbox"></span> 
## "`! Missing number, treated as zero`"error  
If you use `epsf` to include PostScript figures you must make sure
that the `%%BoundingBox` definitions are near the start of the
PostScript figure files. In order to reduce processing time, our TeX
system does not scan the whole of each included file.

If you have a file with the following structure:

``` 
    %!PS-Adobe-3.0 ...
    ...
    %%BoundingBox: (atend)
    ...
    [ bulk of PS file in here ]
    ...
    %%BoundingBox: 0 10 234 456
    ...
    %%EOF
```

then simply move the `%%BoundingBox` line to the top:

``` 
    %!PS-Adobe-3.0 ...
    ...
    %%BoundingBox: 0 10 234 456
    ...
    [ bulk of PS file in here ]
    ...
    %%EOF
```


<span id="include_subdir"></span> 
## "`Can't write subdir/file.aux`" and other problems with write permissions during TeX processing
In our system, only the top level directory is granted write
permission during processing. Attempts to write files to
subdirectories will fail.

All files included via `\include` instead of `\input` must be in the
top level directory. This is because the `\include` command attempts
to write a separate `.aux` file in the same directory as the
included file. For example:

``` 
    \input{file}           %OK, does not create separate .aux file
    \input{subdir/file}    %OK, does not create separate .aux file

    \include{file}         %OK because file.aux can be written
    \include{subdir/file}  %WILL FAIL fail because sub/file.aux cannot be written
```



<span id="double_subscript"></span>
## "`! Double subscript/superscript`" errors  
Our TeX system complains about double subscripts (and superscripts)
because `a_x_y` could be read as `a_{x_y}` or `{a_x}_y` or `a_x{}_y`
or even `a_{xy}`. These are not the same since the character size
and position is affected.

Some older TeX systems would automatically substitute `a_x{}_y`
without the need for user intervention, but current TeX systems
(including ours) will not do this. As a result, **the appropriate
interpretation must be explicitly specified**.

If you are curious about the differences, see [these
examples](doublesubscript.md).



<span id="bad_pdfmark"></span> 
## PDF conversion failure in papers with complex section structure
In some papers with "elaborate" section structure, hyperref can
generate PostScript that contains bad pdfmarks which break PDF
conversion. This problem affects mostly longer papers, reviews,
theses, etc., i.e. those papers where a linked table of contents
(TOC) and document outline would be most useful\!

The reason is that the section counter (used for the names of
destination links) is reset by authors and certain macros to control
the numbering of appendix sections. The result is failure of ps2pdf
conversion due to ambiguous pdfmarks or conflicting subsection count
in the pdfmarks.

The simple cure is to disable HyperTex but a better
work-around is to simply switch off bookmarks (i.e. document
outline) while leaving normal document linking on. You can do this
by adding the following line to the
preamble:

``` 
  \usepackage[bookmarks=false]{hyperref}
```



<span id="ifpdf"></span>
## arXiv system attempts processing with PDFLaTeX for submissions which are regular latex
A common mistake made by authors as well as many macro packages is
incorrect testing for \\pdfoutput to decide whether pdflatex is run
in dvi mode or pdf mode, or whether the processing is done in
regular latex mode. The underlying engines used to be different and
a simple test for \\ifx\\pdfoutput\\undefined was sufficient to
distinguish between all options. This is no longer the case, because
the underlying engine is the same for all 3 cases and therefore the
value of the \\pdfoutput parameter has to be tested, too.

That is, a common (but incorrect) testing sequence might look like:
"\\ifx\\pdfoutput\\undefined .... \\else ..... \\fi". Symptoms of
this mistake might be:

- error messages "Option clash for package ...."
- some unexpected message about various pdf operators
- failing figure inclusions (due to unrecognized extension)

The most reliable way to accomplish conditional branching in the TeX
source where necessary is instead via the ifpdf package:

```
\usepackage{ifpdf}
\ifpdf
do something pdflatex specific here
\else
do something for regular latex or pdflatex in dvi mode
\fi
```
Note that the graphics package and the hyperref package are smart
enough to figure this out on their own. You do **not** need to
specify any driver for these packages.

For more information, see:

https://www.ctan.org/pkg/ifpdf

You can download the ifpdf macro from the above link as well, if it
is not already a part of your tex tree.

In the extremely rare event that your submission still does not
correctly identify itself as latex, and you are absolutely sure, you
can add the line:    
``` 
%&latex 

```
as the very first line of your tex file.


<span id="mixed"></span> 
## Mixed figure file formats

arXiv does not perform any "on the fly" figure file conversions from PostScript to PDF, so your
figure files must be in the same format expected for your processing engine. This means PDFLATeX would accept any combination of `.pdf`, `.jpg`, and/or `.png`, and that (La)TeX accepts `.ps` and/or `.eps` only. You can tell this has been done locally because the converted figures will typically appear with names like "`-eps-converted-to.pdf`" in addition to the original `.eps` file.

One could convert all PostScript figures in a directory to PDF simply by running from a BASH prompt: 
```
  $ for i in *ps; do ps2pdf -DEPSCrop $i; done;
```
then proceeding to update the figure file inclusion commands in your tex. Note that there are many ways to accomplish this step (e.g. one could use [ImageMagick](../../help/bitmap/procedure.md#shortImageM)), and this is provided as an example only. It is your responsibility as the submitter to ensure that the figures are scientifically accurate in the format as submitted. 



<span id="Bbbk"></span> 
## "`! LaTeX Error: Command \Bbbk already defined.`"

A new issue seen beginning with the upgrade to [TeXLive 2020](texlive.md) in arXiv is the error: 
```
  ! LaTeX Error: Command `\Bbbk' already defined.
```
This error appears most frequently when using the `mnras.cls` template for their tex source file, although there are other causes for this same error. The error is caused by multiple packages attempting to define this math symbol. Most commonly in arXiv appear to be the interaction of the `newtxmath.sty` and `amssymb.sty` packages, which both define this shape. Ideally, you will know which one is the correct one for your use and plan in advance to use one or the other. If you insist on using both, one or the other will need to have its definition of this macro reset prior to the call of the other package. This can be done by adding the line: 
```
  \let\Bbbk\relax 
```
immediately after the call to the first package (usually the `newtxmath.sty` package call). If you choose to go this route, please *carefully* inspect the output, as this may have unexpected results. If you determine that the output is other than what you would expect for this symbol, please swap the package inclusion order, to "`\relax`" the other package's definition of this symbol.


<span id="minted"></span> 
## Notes for using `minted.sty` in arXiv

arXiv cannot process using the `--shell-escape` option, as this is disabled in arXiv's system for security reasons. 

Authors who make use of `minted.sty`'s syntax highlighting are warned against using so called "hidden" cache directories in arXiv. This means that if you are running with their recommended `[frozencache]` option to the package, you will need to specify a cache directory. **Do not use a hidden directory name!** Hidden directories begin with the special `.` character, such as `.minted-cache` (which may be the default). Such options will break at publish time, as these files are not saved between compilation and publication (and are not able to be regenerated). To account for this, do not use them. An example of a correct call looks like: 
```
  \usepackage[frozencache=true,cachedir=minted-cache]{minted} 
```
This assumes that you've already correctly created the cache first using their `[finalizecache]` option. Consult the [package manual](http://mirrors.ctan.org/macros/latex/contrib/minted/minted.pdf#page=11) for further details (at time of this writing, the package options begin on page 12 in section 5).

<span id="bblmismatch"></span>
## .bbl version mismatch

arXiv's TeX Processing system is built on a specific version of [TeX Live](texlive.md). This means that as new versions of software are released, arXiv may fall
behind with the state of the art  for systems like BibLaTeX. As such, one may recieve an error from the submission system or tex processor which indicates a version 
mismatch. This error may look something like: 
```
bbl version mismatch: Expected 3.2 but got 3.3, at file [mydoc.bbl]
```
The _only_ solution to this state is to compile your BibLaTeX with the _same version of TeX Live_ that arXiv uses. If you built your submission using overleaf
we recommend that you use their system to up or downgrade your proecessing engine, recompile your pdf fully, and then [download the .bbl file again](
https://www.overleaf.com/learn/how-to/How_do_I_download_the_automatically_generated_files_(e.g._.bbl%2C_.aux%2C_.ind%2C_.gls)_for_my_project%3F_My_publisher_asked_me_to_include_them_in_my_submission). 

<span id="breqn"></span>
## breqn and Labels might have changed problem

When the `breqn` package is combined with `hyperref` package, and math code is embedded in
caption of formulas or images, LaTeX might report at the end of **every** compilation, even if
running many times in a row, the following warning:

```
LaTeX Warning: Label(s) may have changed. Rerun to get cross-references right.
```

This is a known issue (see this [SX entry](https://tex.stackexchange.com/a/331220)) and can be fixed by
adding the following code immediaetely after the `\usepackage{breqn}` line in the preamble:

```
\makeatletter
\AtBeginDocument{%
    \catcode`_=12
    \begingroup\lccode`~=`_
    \lowercase{\endgroup\let~}\sb
    \mathcode`_="8000
    \immediate\write\@auxout{\catcode`_=12 }%
    \immediate\write\@auxout{\catcode`^=12 }%
}
\makeatother
```
