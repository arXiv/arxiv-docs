# Why doesn't my processed TeX submission look the way I expected it?

There are a number of common reasons why the processed version of TeX
submissions to arXiv may not appear the same as it does when processed
locally. In most cases there are fixes that can be applied and the
submission replaced to correct the problems.
 

   ## Lines in the table of contents don't wrap
   By default, papers are processed with the automatic addition of
  hyperlinks using the [HyperTeX](http://arxiv.org/hypertex) package.
  Hyperlinks in the table of contents can create a problem with
  latex's ability to break lines. This problem can be solved by passing the option `linktocpage` to hyperref. Include the line
    
   ``` 
       \PassOptionsToPackage{linktocpage}{hyperref}
  ```
    
  in the preamble. This will create a hyperlink for the the page numbers instead of the whole table of contents line, and thus avoid the line break problem.
    
  An alternative solution is to allow hyperref to break links and thus
  wrap lines. To enable this, add the following to the preamble:
    
   ``` 
       \usepackage[hyperindex,breaklinks]{hyperref}
   ```
    
  ## Hyperlinks overrun the page or column boundaries
  
arXiv's default behavior for [hyperref](../../help/hypertex/index.md) is to have hyperlinks (and any other clickable link) to remain on a single line. This means that any URL or linked text longer than the available `\columnwidth` or `\textwidth` values will not break into the next line. To disable this behavior, you must set the hyperref option `breaklinks` to be `true`. We recommend using a `\hypersetup` block, as this makes keeping your options easier to see. For example: 

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

    
  ## Fuzzy fonts in PDF 
  If you use the `fontenc` package and `T1` fonts you may find that the fonts appear fuzzy in PDF output from arXiv. Our suggested solution in most cases is to include packages `ae` and `aecompl` in the latex source. To do this add 2 additional lines after the `fontenc` inclusion:

  ``` 
      \usepackage[T1]{fontenc}
      \usepackage{ae}
      \usepackage{aecompl}
   ```
    
  CAREFULLY INSPECT the generated PDF for proper display of accented characters, character omissions, or other peculiarities. These problems can only be spotted by careful visual inspection, something which cannot be expected from arXiv admins and instead has to be performed by the author(s).
    
Here are some pointers to entries in the TeX FAQ that address this issue:
    
  - [Quality of PDF from
    PostScript](https://texfaq.org/FAQ-dvips-pdf)
  - [Fonts go fuzzy when you switch to
    T1](https://texfaq.org/FAQ-fuzzy-T1)
  - [Finding new scalable outline
    fonts](https://texfaq.org/FAQ-findfont)
  - [Finding '8-bit' Type 1
    fonts](https://texfaq.org/FAQ-type1T1)
  - [Weird characters in dvips
    output](https://texfaq.org/FAQ-charshift)
    

 ## PostScript figures lose quality in arXiv-generated PDFs
  arXiv uses Ghostscripts's PDF Writer device to generate the PDF versions of TeX submissions. A variety of parameters affects the conversion of PostScript to PDF. In particular bitmap figures are frequently downsampled to the target device resolution, and color spaces are converted as necessary. While arXiv's default settings, the defaults of Ghostscript's PDF Writer device, usually give reasonable quality, some figures may require individual parameter fine tuning for optimal quality of display and/or printout.
  
  To ensure the best display quality for your figures, please refer to the [Ghostscript documentation](https://www.ghostscript.com/documentation/index.html) for detailed information on output devices and image file formats.

  ## Extra white space around figures covers up some of the text   
  These problems are characteristic of PostScript figures that have
  been created from PowerPoint. Microsoft PowerPoint does not generate
  appropriate PostScript code. If you must use PowerPoint to generate
  figures, you should export the figure to another format such as
  JPEG. JPEG figures can be included directly using
  [PDFLaTeX](http://arxiv.org/help/submit_tex#pdflatex), or they can
  be converted back to PostScript using a program such as `jpeg2ps`.
  The `jpeg2ps` program is freely available for all platforms.
