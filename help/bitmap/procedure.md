What is the easiest way to do bitmapping?
=========================================

It depends on your operating system:

-   Most platforms (including Windows): [ImageMagick](#shortImageM)
-   Unix/Linux: [XV screen grab](#shortXV)
-   Mac: [Mac screen capture](#shortMac)

------------------------------------------------------------------------

<span id="shortImageM"></span>

ImageMagick
-----------

Image Magick is a suite of very powerful and feature rich image
manipulation programs available for many platforms. The [ImageMagick
homepage](https://www.imagemagick.org/) is well worth a visit.

Frequently the following two conversions give a significant reduction in
filesize with very reasonable visual quality:

-   Making a GIF-encoded PostScript:

          % convert figure.ps figure.gif
          % convert figure.gif newfigure.ps

-   Making a JPEG-encoded PostScript:

          % convert figure.ps figure.jpg
          % convert figure.jpg newfigure.ps

You may need to adjust the BoundingBox of the original or use the size
option with `convert`. You can also try some of the many of `convert`'s
options, like monochrome, sharpen, etc. to achieve better visual quality
(refer to ImageMagick documentation for more details).

<span id="shortXV"></span>

Shortcut to getting a bitmap version of any figure using XV
-----------------------------------------------------------

If you have [XV](http://www.trilon.com/xv/) installed, there is an easy
way to make a bitmap version of any figure.

First, display the original figure on the screen somehow, e.g. with
ghostview. **DO NOT** open PostScript figures with XV -- this simply
uses ghostscript as a backend to generate a low resolution ppmraw
bitmap. It is better to display the PostScript file at the desired size
with your favorite viewer and then grab the image from screen as
described below.

Next, use the "Grab" button in XV to snatch a copy of the displayed
image into XV's buffer (after selecting "Grab" you can do this either by
clicking the left mouse button on the desired window -- which grabs the
whole window, or by holding down the middle mouse button and dragging --
which selects a region).

Once the image is in XV's buffer, you can manipulate it. You should use
"Autocrop" or "Crop" to remove any excess margins around the figure.
Then save it as a color or greyscale PostScript.

> <span class="note">Note: </span>**When resaving as PostScript, you
> must click the XV "compress" box; this vastly reduces the file size
> with no loss of quality.**

![A picture of the XV Save window showing the compress checkbox
ticked](https://arxiv.org/icons/help/xvcompress.gif)

> The "compress" option is available only when XV is in 8bit mode, this
> is selected from the `24/8 Bit` menu in the `XV controls` window. You
> almost certainly do not need a 24bit color map so you should use 8bit
> mode. Also, you should save as `Greyscale`, `Full Color` or
> `Reduced Color` rather than `B/W Dithered` which does not allow
> compression. **We do not want PostScript bitmaps generated without
> this option because they can be many megabytes in size when
> unzipped.**

Finally, make sure that the size of the newly saved image is smaller
than the original. In addition, the uncompressed size of a figure should
not exceed 500kB. <span id="shortMac"></span>

Shortcut to getting a bitmap version of any figure using Macintosh
------------------------------------------------------------------

The easiest way to create a bitmap off the screen on a Mac is to follow
this procedure:

1.  Capture the screen: Press command - shift - 3 (That is the
    "clover"-key, the shift-key and the 3-key simultaneously). This
    saves a pict-file of the entire screen onto your hard drive.
2.  Use one of the many shareware/freeware programs to crop the figure
    and save it in your favorite file format. A free one is Imagery 1.9
    Graphics Converter, which is available from any [info-mac
    site](http://www.pht.com/info-mac/index_text.html). A particularly
    powerful one is the shareware program Graphic Converter 2.5 from the
    same site.
