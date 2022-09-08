# Why doesn't my processed TeX submission look the way I expected it?

There are a number of common reasons why the processed version of TeX
submissions to arXiv may not appear the same as it does when processed
locally. In most cases there are fixes that can be applied and the
submission replaced to correct the problems.

  - [Lines in the table of contents don't wrap](#toc_links)
  - [Hyperlinks overrun the page or column boundaries](#breaklinks)
  - [Fuzzy fonts in PDF](#fuzzy_pdf)
  - [PostScript figures lose quality in the arXiv-generated
    PDF](#distiller_params)
  - [Extra white space around figures covers up some of the
    text](#powerpoint)
  - [Why don't the labels for my figures appear when I use
    Feynmf?](feynmf#nolabel)
  - [Why are the margins different? Why is my text truncated?](dvips)
  - [Why does my paper give the wrong date?](today)
  - [Why do my citations appear in long form `[1,2,3,4]` instead of
    short form `[1-4]`?](citelinks)
  - [Why do my user defined symbols (e.g., `\i, \l, \L, \o, \ae,` etc.)
    display incorrectly in the processed document?](pd1enc)
  - [Why are there problems with my postscript file?](/help/faq/psbad)
  - [Why are some pages in the generated PDF file rotated and how do I
    avoid this?](/help/faq/pdfrotate)

-----

  

  - <span id="toc_links"></span>**Lines in the table of contents don't
    wrap**  
    By default, papers are processed with the automatic addition of
    hyperlinks using the [HyperTeX](http://arxiv.org/hypertex) package.
    Hyperlinks in the table of contents can create a problem with
    latex's ability to break lines. This problem can be solved by
    passing the option `linktocpage` to hyperref. Include the line
    
    ``` 
        \PassOptionsToPackage{linktocpage}{hyperref}
    ```
    
    in the preamble. This will create a hyperlink for the the page
    numbers instead of the whole table of contents line, and thus avoid
    the line break problem.
    
    An alternative solution is to allow hyperref to break links and thus
    wrap lines. To enable this, add the following to the preamble:
    
    ``` 
        \usepackage[hyperindex,breaklinks]{hyperref}
    ```
    
  - <span id="breaklinks"></span>**Hyperlinks overrun the page or column boundaries**
  
arXiv's default behavior for [hyperref](/help/hypertex) is to have hyperlinks (and any other clickable link) to remain on a single line. This means that any URL or linked text longer than the available `\columnwidth` or `\textwidth` values will not break into the next line. To disable this behavior, you must set the hyperref option `breaklinks` to be `true`. We recommend using a `\hypersetup` block, as this makes keeping your options easier to see. For example: 

```TeX
        \hypersetup{
           breaklinks=true,   % splits links across lines
           colorlinks=true,   % displays links as colored text instead of blocks
           pdfusetitle=true,  % \title and \author values into pdf metadata
                              % etc.
        }
```

For more information please consult the [hyperref manual](https://ctan.org/pkg/hyperref). 

Note that this primarily impacts links that are created with the `\href` construct. If you are trying to make use of long
URL with the `\url` construct, we recommend that you make use of the `url` package with the `[hyphens]` option ([see its documentation](https://ctan.org/pkg/url)). This package typically has to be loaded before hyperref. If this 
doesn't provide the functionality you seek (e.g. in dvi mode), you may wish to use the `breakurl` package, which performs some 
of these same features. Consult [the package documentation](https://ctan.org/pkg/breakurl) for usage instructions.



    
  - <span id="fuzzy_pdf"></span>**Fuzzy fonts in PDF**  
    If you use the `fontenc` package and `T1` fonts you may find that
    the fonts appear fuzzy in PDF output from arXiv. Our suggested
    solution in most cases is to include packages `ae` and `aecompl` in
    the latex source. To do this add 2 additional lines after the
    `fontenc` inclusion:
    
    ``` 
        \usepackage[T1]{fontenc}
        \usepackage{ae}
        \usepackage{aecompl}
    ```
    
    CAREFULLY INSPECT the generated PDF for proper display of accented
    characters, character omissions, or other peculiarities. These
    problems can only be spotted by careful visual inspection, something
    which cannot be expected from arXiv admins and instead has to be
    performed by the author(s).
    
    Here are some pointers to entries in the TeX FAQ that address this
    issue:
    
      - [Quality of PDF from
        PostScript](http://www.tex.ac.uk/cgi-bin/texfaq2html?label=dvips-pdf)
      - [Fonts go fuzzy when you switch to
        T1](http://www.tex.ac.uk/cgi-bin/texfaq2html?label=fuzzy-T1)
      - [Choice of scalable outline
        fonts](http://www.tex.ac.uk/cgi-bin/texfaq2html?label=psfchoice)
      - [Finding '8-bit' Type 1
        fonts](http://www.tex.ac.uk/cgi-bin/texfaq2html?label=type1T1)
      - [Weird characters in dvips
        output](http://www.tex.ac.uk/cgi-bin/texfaq2html?label=charshift)
    
      

  - <span id="distiller_params"></span>**PostScript figures lose quality
    in the arXiv-generated PDF**  
    arXiv uses Ghostscripts's PDF Writer device to generate the PDF
    versions of TeX submissions. A variety of parameters affects the
    conversion of PostScript to PDF. In particular bitmap figures are
    frequently downsampled to the target device resolution, and color
    spaces are converted as necessary. While arXiv's default settings,
    the defaults of Ghostscript's PDF Writer device, usually give
    reasonable quality, some figures may require individual parameter
    fine tuning for optimal quality of display and/or printout.
    
    Clearly arXiv's automated service cannot provide that level of
    individual tuning for authors. However it is possible to augment
    PostScript figures with hints (distiller parameters) to be used by
    the PDF converter. So authors can directly control the resulting
    image quality themselves via the following modification to their
    PostScript figure file(s).
    
    In the Prolog section of the affected figure(s) insert a text block
    like:
    
        /setdistillerparams where {pop}{userdict /setdistillerparams {pop} put}ifelse
        << /AutoFilterColorImages false
        /AutoFilterGrayImages false
        /ColorImageFilter /FlateEncode
        /GrayImageFilter /FlateEncode
        /UseCIEColor true
        /ColorACSImageDict .printerACSImageDict >>
        setdistillerparams
    
    These parameter settings often improve the appearance of (high
    resolution bitmap) figures in PDFs generated by arXiv. Other
    parameters are available, however. For a list, see the table
    available near the end of the Options section of the help page for
    the Ghostscript PDF Writer device:
    
    <http://pages.cs.wisc.edu/~ghost/doc/cvs/Ps2pdf.htm#Options>
    
    All `ps2pdf` parameters can be set in PostScript prologs via
    definition of a dictionary (key-value lookup table) as a list of
    key-value
        pairs:
    
        /setdistillerparams where {pop}{userdict /setdistillerparams {pop}put}ifelse
        << /key1 /value1 /key2 /value2  ....    >> setdistillerparams
    
    either in a particular PostScript figure or via a literal PostScript
    `\special` in the TeX source.

  - <span id="powerpoint"></span>**Extra white space around figures
    covers up some of the text**  
    These problems are characteristic of PostScript figures that have
    been created from PowerPoint. Microsoft PowerPoint does not generate
    appropriate PostScript code. If you must use PowerPoint to generate
    figures, you should export the figure to another format such as
    JPEG. JPEG figures can be included directly using
    [PDFLaTeX](http://arxiv.org/help/submit_tex#pdflatex), or they can
    be converted back to PostScript using a program such as '`jpeg2ps`'.
    The '`jpeg2ps`' program is freely available for all platforms.
