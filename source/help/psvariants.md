PostScript Variants
===================

The default resolution of a file obtained by clicking on the
**PostScript** link is 600 dpi, and the default fonts are bitmapped
fonts. There are other types of PostScript available from arXiv,
obtained by going to the **More Options** page for any paper.

If you consistently prefer a different format, you can change the
default to one of the formats discussed below by setting a cookie on the
**More Options** page.

PostScript with Bitmapped fonts at 300 and 600 dpi
--------------------------------------------------

These are the most common printer resolutions, and our default
resolution is 600 dpi. Be sure to choose the resolution that matches
your printer. If you ask for 600 dpi when you only have a 300 dpi
printer you will get bad results. Also, the size of the PostScript file
grows with the resolution selected.

Bitmapped PostScript formats should work with any PostScript printer or
viewer. You don't need to install any fonts to use them.

PostScript with Type 1 fonts (non-embedded)
-------------------------------------------

Type I fonts contain explicit PostScript instructions for drawing each
character, rather than just a bitmap of the result. They are always
rendered at the correct resolution for whatever device you are using to
view or print the PostScript.

To view and print PostScript with Type 1 fonts you will need to install
the fonts on your local system.

Note that there are several versions of the Type I Computer Modern fonts
and that they use different naming conventions. For instance, the Bakoma
fonts use a lowercase "cm" in their naming scheme, while the Blue-Sky
fonts use an uppercase "CM". You can select which naming convention your
installation uses.

For more information on the different Type I fonts available, see our
[discussion of Computer Modern Type I PostScript Fonts](pscm.md).

DVI
---

Not a PostScript format, but if you aren't happy with the choices
offered, you can also get the dvi file itself and run dvips with your
preferred options.

Note that if there are any PostScript figures for the paper, they are
delivered together with the dvi file in a gzipped tar-file.

PDF
---

PDF (Portable Document Format) is an alternate format which produces
larger files, but allows Hyperlinks, and can be printed without a
postscript printer. See [the discussion of PDF](pdf.md) for details.
