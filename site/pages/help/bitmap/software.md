Useful Software
===============

Ghostscript
-----------

Recent versions of [Aladdin Ghostscript](http://www.cs.wisc.edu/~ghost/)
come with much improved PostScript "distillers". Depending on filetype,
one of these:

      % ps2ps figure.ps newfigure.ps
      % eps2eps figure.eps newfigure.eps

frequently gives a reduction in file size while preserving visual
quality. There are certain rendering functions that do not work well
with this technique, and sometimes figure size actually increases.

XV
--

XV is widely available, and it might be already installed on your
machine. If not, visit the [XV homepage](http://www.trilon.com/xv/) and
download the latest version. It is reasonably easy to install if you
follow the instructions in the `INSTALL` file. Editing the Makefile to
switch off the TIFF library should avoid some possible compilation
problems.

Note that the XV license states that, "commercial, government, and
institutional users must register their copies of XV".

ImageMagick
-----------

Image Magick is a suite of very powerful and feature rich image
manipulation programs available for many platforms. The [ImageMagick
homepage](http://www.imagemagick.org/) is well worth a visit.

The GIMP
--------

The <span class="underline">G</span>NU <span
class="underline">I</span>mage <span
class="underline">M</span>anipulation <span
class="underline">P</span>rogram, or [*GIMP*](https://www.gimp.org) is a
"free", powerful, graphics and figure manipulation program. It is
available for most (if not all) architectures and platforms. It provides
much of the same functionality as expensive commercial software at no
cost.

<span id="imgtops"></span>

imgtops/epstoimg
----------------

[imgtops/epstoimg](http://imgtops.sourceforge.net/) are a pair of
command-line utilities for translating between bitmap images (JPEG, PNG,
GIF, Targa, BMP, etc.) and Level 2 PostScript files. Level 2 supports
more efficient encoding of image data than the original PostScript
standard, so the files produced by imgtops are significantly smaller
than those made by the `pnmtops` utility of the PBMPlus package or
`convert` utility of ImageMagick. This is especially true of JPEG files,
which Level 2 can handle directly but Level 1 implementations must first
decompress. Level 2 PostScript has been the standard for almost a decade
now (Level 3 is actually out now), so nearly all printers support it.

<span id="jpeg2ps"></span>

jpeg2ps
-------

`jpeg2ps` is a utility for converting JPEG images to compressed
PostScript. This allows efficient inclusion of JPEG images in LaTeX
documents. `jpeg2ps` is available for Unix/Linux/MacOSX and Windows
platforms.

If you use `jpeg2ps`, you should use the "`-h`" option which specifies
hex encoded output. This produces marginally larger PostScript but the
will not contain lines starting with "`%`" that can interfere with
PostScript DSC information. The increase in the compressed size is
minimal. Do not use the "`-b`" to select binary output as the PostScript
files produced in this way are not portable.

Windows Programs
----------------

There are many shareware graphics viewing, conversion and editing
programs available for Windows. You can locate these using your favorite
web search engine, or within the *Windows Store*.
