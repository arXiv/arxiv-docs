# Using PSTricks on arXiv

>**Update April 2025:** arXiv now uses the
version of PSTricks that is available in the used version of TeX Live,
currently 2023. Please make sure that your PSTricks code is compatible
with this version.


>**Update October 2002:** arXiv now uses the
version of PSTricks which was current as of October 2002, namely
**pstricks.tex 97 patch 14**, to process submissions and replacements
received after the end of September 2002. This means that you can ignore
the instructions below if you wrote your paper on a TeX installation
that was reasonably up-to-date as of the fall of 2002.

-----

The PSTricks utilities can be used in submissions to arXiv. However, due
to version compatibility problems, we advise authors to include their
own PSTricks macro files and PostScript header files with their
submissions.

You have to determine which macro and header files are necessary and
copy them into the same working directory as your main latex file. You
should then use **tar** or **zip** to pack it all into a single archive
file for convenient submission.

## Determining which Files Need to be Supplied

### PSTricks (La-)TeX macros (.tex, .sty, .con)

There are quite a few macro files in the PSTricks
>     distribution:

> 
> 
>     dvipsone.con  pst-char.sty  pst-ghsb.tex  pst-plot.sty  pst-tree.tex
>     multido.sty   pst-char.tex  pst-gr3d.sty  pst-plot.tex  pstricks.bug
>     multido.tex   pst-coil.sty  pst-gr3d.tex  pst-poly.sty  pstricks.con
>     palette.sty   pst-coil.tex  pst-grad.sty  pst-poly.tex  pstricks.sty
>     pst-3d.sty    pst-eps.sty   pst-grad.tex  pst-slpe.sty  pstricks.tex
>     pst-3d.tex    pst-eps.tex   pst-key.sty   pst-slpe.tex  textures.con
>     pst-all.sty   pst-fill.sty  pst-key.tex   pst-text.sty  vtex.con
>     pst-blur.sty  pst-fill.tex  pst-node.sty  pst-text.tex
>     pst-blur.tex  pst-ghsb.sty  pst-node.tex  pst-tree.sty

but usually only 2 or 3 of these are used in a given paper. You have to
inspect the LaTeX diagnostics on screen or the LaTeX `.log` file to
determine which of the above files are included. A typical LaTeX screen
dialog should have a section that looks similar to this:

> 
> 
>     ...
>     (texmf/tex/generic/pstricks/pst-node.tex
>      v97 patch 9, 1999/04/14
>     (texmf/tex/generic/pstricks/pstricks.tex
>     `PSTricks' v97 patch 10  <1999/03/24> (tvz)
>     (texmf/tex/generic/pstricks/pstricks.con)))
>     ...

There are two pieces of information in this output: (i) it contains a
list of the included PSTricks macro files, and (ii) it specifies their
location. Simply copy the required files into your working directory.

### PSTricks PostScript header (.pro) files

Since PSTricks uses advanced PostScript specials for it to work
properly, you need the accompanying PostScript header files. From all
the special PSTricks header files that come with the
>     package:

> 
> 
>     pst-blur.pro  pst-dots.pro  pst-grad.pro  pst-slpe.pro  pstricks.pro
>     pst-coil.pro  pst-ghsb.pro  pst-node.pro  pst-text.pro

you should only include those which are actually required to process
your paper. To determine these, you have to read the diagnostic output
from dvips. The first few lines should look similar to:

> 
> 
>     % dvips test.dvi
>     This is dvips(k) 5.86 Copyright 1999 Radical Eye Software
>     (www.radicaleye.com)
>     ' TeX output 2002.02.08:1404' -> test.ps
>     <texc.pro><pstricks.pro><pst-dots.pro><pst-node.pro>
>     <8r.enc><texps.pro><special.pro>.....

From the above dvips message it is fairly obvious which PSTricks
PostScript header files are required for this paper, namely:

  - pstricks.pro
  - pst-dots.pro
  - pst-node.pro

You have to locate these files on your computer and copy them into the
same directory as your latex file. For a typical TeX installation a
generic location would be the directory:

> 
> 
>     /usr/local/teTeX/texmf/dvips/pstricks/

but this is dependent on your particular installation.

## Don't Forget to Check the PostScript\!

As always, carefully check the diagnostic messages sent to you upon
submission and <span class="note">verify the PostScript generated here
before the paper is announced</span>. Use the paper-id sent to you
immediately after a successful submission to access the abstract and
PostScript or PDF for a preview.
