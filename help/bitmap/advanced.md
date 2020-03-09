---
title: 'Advanced Bitmapping'
---
Advanced Bitmapping
===================

<span class="note">Note:</span> Advanced doesn't necessary equate to
better. The [basic procedures](procedure) will often yield superior
results with considerably less effort.

The first stage in advanced bitmapping of PostScript is to use
Ghostscript to create a portable bitmap (pbm) file from the original
inefficient PostScript. Then the pbm file can be converted into GIF,
JPEG, or back into PostScript. With luck one of these formats will be
more compact. **Do not submit the pbm, pgm or ppm files themselves, as
these are inefficient formats.** You must convert all pbm, pgm and ppm
files to GIF, JPEG, or PostScript before submitting them.

Using Ghostscript to Create Bitmapped Figures
---------------------------------------------

The first step is to create a portable bitmap using Ghostscript. To
create a pbm file from a PostScript file, try a command like this,

         cat fig.ps | gs -q -sDEVICE=pbmraw -sOutputFile=- -r75 - > fig.pbm

The resolution of the bitmap in dots-per-inch is given by the "`-r`"
option; 75dpi is a good choice.

For an encapsulated PostScript (eps) file, it may be necessary to add a
`showpage` command to the end of the eps file (or the output file will
be empty). One way would be something like this,

         (cat fig.eps ; echo showpage ) |
           gs -q -sDEVICE=pbmraw -sOutputFile=- -r75 - > fig.pbm

To make greyscale or color bitmaps instead, choose "`-sDEVICE=pgmraw`"
(greymap) or "`-sDEVICE=ppmraw`" (color pixmap), respectively.

Now you should have a **pbm** file of your figure. You must convert it
to GIF, JPEG or PostScript before submitting it. You can either load it
into XV to save it in one of these formats, or use the [PBM
tools](software) to do the same.

Converting a .pgm or .ppm Bitmap File to GIF or JPEG
----------------------------------------------------

With **XV** this is straightforward -- just load in the image and save
it as the appropriate type.

With **PBM**, use the `ppmtogif` command to make gifs,

         ppmtogif fig.pbm > fig.gif

PBM does not include a tool for making JPEG files. You need the `cjpeg`
utility (mentioned below), and a command like this:

         cjpeg fig.ppm > fig.jpeg

Note that only color .ppm or greyscale .pgm images can be converted to
jpegs using cjpeg (if Ghostscript finds only black and white in the
image, then it will output a simpler .pbm file).

Converting a .pbm Bitmap File to PostScript
-------------------------------------------

In most cases you will want to get the figure back into PostScript
format. You can use the XV "Save as PostScript" option, or you can use
the `pnmtops` utility in the PBM toolset.

If you are using PBM, the command is:

         pnmcrop fig.pbm | pnmtops -noturn -rle > fig.new.ps

The `pnmcrop` utility trims the margins down to the right size (you can
get the same effect by clicking the "Autocrop" button in XV), the
"`-noturn`" option keeps the image in the same orientation (otherwise it
would be rotated to fit the page better under certain circumstances),
and the "`-rle`" option does run length encoding, making the
uncompressed image more efficient, so you should **definitely use it**.
We do not want PostScript bitmaps generated without this option because
they can be many megabytes in size when unzipped.

We have found that the pnmtops command supplied with the PBM tools does
not do a particularly good job. It drops pixels and down-samples the
image, giving quite a bad result. We made a modified version, called
`pnmtops2`, which we use here and usually looks better. It is included
in our autoconf version of pbm mentioned below.

Take a look at the new PostScript file with Ghostscript and print it out
(the printout generally looks much better than the on-screen version).
Hopefully the quality will be acceptable. If not, go back and try
bitmapping with a higher resolution.

Once the figure is acceptable, gzip both the original and new PostScript
files and check the saving. If it is substantial then the bitmap may be
a better choice for submitting with the paper.
