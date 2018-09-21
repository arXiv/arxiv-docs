Frequently Asked Questions
==========================

-   [What is a reasonable size for figures?](#size)
-   [What are the best formats for image types?](#format)
-   [What about other formats?](#other)
-   [How can readers view JPEG/GIF/PNG images?](#view)

------------------------------------------------------------------------

<span id="size"></span>

What is a reasonable size for figures?
--------------------------------------

Almost all figures can easily be reduced to less than 50kB each
(gzipped) without significant loss of quality, by using an appropriate
format.

If you cannot make your figure files smaller than this, you are probably
doing something wrong (e.g. using an inappropriate format, or
unnecessarily high resolution). All the figures we have encountered can
be compressed to less than 50kB without significant loss of quality.

Prioritize the figures for optimization by looking at the gzipped sizes,
and deal with the largest ones first.

<span id="format"></span>

What are the best formats for image types?
------------------------------------------

Most of the inefficient PostScript figures submitted to arXiv are one of
three types:

-   Photographic images (e.g., astronomical images):
-   3D plots, color contour plots, and screen shots:
-   Line drawings, diagrams, and PostScript output from data plotting
    programs with millions of points (e.g., graphs from Mathematica,
    Supermongo, paw, 3d surface plots, etc.).

These are all candidates for resaving as compressed **bitmapped
PostScript** that can be included in the paper (if the resulting file is
of a reasonably small size).

The **JPEG** format is specially designed for photographic images with
many colors, such as astronomical images, plates, etc. JPEG allows a
lossy compression so that files can be made manageably small without
sacrificing much in the quality of the image.

The **GIF** and **PNG** formats can be used for images with sharp edges
or fine detail -- they provide lossless compression, and work well with
color, greyscale, and black & white images.

Note that JPEG and GIF can be directly wrapped into level 2 PostScript
while preserving the compression see
[ImageMagick](procedure#shortImageM), [imgtops](software#imgtops), and
[jpeg2ps](software#jpeg2ps) for more details.

<span id="other"></span>

What about other formats?
-------------------------

You should only submit images as JPEG, PNG, GIF or PostScript. We do not
accept other formats, such as pbm, pgm, ppm, xbm, bmp, xwd, pcx, etc.
because they are either inefficient or viewers are not available for all
platforms. If you have a figure in one of these formats you should
convert it to JPEG, PNG, GIF or PostScript before submitting it.

<span id="view"></span>

How can readers view JPEG/GIF/PNG images?
-----------------------------------------

JPEG, PNG and GIF images can be included with the submission package,
and appear as separate files alongside the text (see, e.g.,
[astro-ph/0202056v1](http://arxiv.org/ps/astro-ph/0202056v1)). Graphical
web browsers, such as Internet Explorer, will display JPEG, PNG, and GIF
images automatically.

A preferable option, however, is to convert the JPEG/GIF/PNG image(s)
back into PostScript format; see [ImageMagick](procedure#shortImageM),
[imgtops](software#imgtops), and [jpeg2ps](software#jpeg2ps) for more
details.
