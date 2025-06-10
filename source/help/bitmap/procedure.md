What is the easiest way to do bitmapping?
=========================================

It depends on your operating system:

-   Most platforms (including Windows): [ImageMagick](#shortImageM)
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

<span id="shortMac"></span>

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
