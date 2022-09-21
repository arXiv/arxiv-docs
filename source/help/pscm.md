Computer Modern Postscript Fonts in Adobe Type I Format
=======================================================

Postscript Type I fonts are device-independent and
resolution-independent outline fonts for use in Postscript documents.
There are four sets of Type I fonts of interest to users of the archives
and TeX users in general. These are the Bakoma, Blue-Sky, AMSFonts, and
Paradissa font sets. Depending on your software, they may also display
much better than traditional bitmap fonts (give them a try).

The Bakoma fonts are a version of Computer Modern (the standard TeX
font) which have been freely available for some time. The Blue-Sky fonts
are a version of Computer Modern which were made freely available in
early 1997. See [the
discussion](http://www.ams.org/tex/type1-cm-fonts.html) on the AMS
server for more information on the Blue-Sky font deal.

The Paradissa fonts are extra fonts, including the AMS fonts and some
Cyrillic fonts. The AMSFonts set includes the Euler, "extra symbol" and
cyrillic fonts in selected sizes; these were produced by Blue Sky
Research and made freely available in late 1997. See the [the
discussion](http://www.ams.org/tex/type1-cm-fonts.html) on the AMS
server and the [AMS ftp site](ftp://ftp.ams.org/pub/tex/psfonts/ams/)
for the AMSFonts.

What's the difference between Bakoma and Blue-Sky?
--------------------------------------------------

With two font sets of different origin some compatibility questions
arise, especially for documents with non-embedded fonts.

First of all, the two font sets are basically interchangeable.
Postscript or PDF documents with non-embedded fonts, which were created
based on one font set, can be displayed using either of the two font
sets.

There is a minor problem with naming conventions for case sensitive
operating systems. The Bakoma font names are all lowercase, while
Blue-Sky font names are all uppercase. If your fontfiles don't match the
font names in the Postscript or PDF file, you will have to translate the
font names in the document (note that we offer Postscript and PDF files
with a [choice of naming convention](psvariants.md); for example Macintosh
use fonts with upper case NAMES), or translate the case of your
fontfiles or make symbolic links from uppercase to lowercase names.

Blue-Sky fonts cover Knuth's 75 CM fonts (plus the extra LaTeX and
SliTeX fonts) *exactly*, but no others, while the combination of Bakoma
and Paradissa contains in addition the AMS fonts and some Cyrillic
fonts. You will need these additional fonts from Bakoma and Paradissa if
you want to read type 1 Postscript or PDF documents produced by arXiv.
You will see incorrect symbols especially in math formulas without them.

Which look better?
------------------

One thing in favor of Bakoma fonts is that they are slightly darker
(probably because of a different mode\_def setting); this is probably an
advantage since Computer Modern is a light font.

Blue-Sky fonts are said to render better on high quality rasterizers
like Adobe Type Manager (ATM), which make proper use of the "hinting"
information in the fonts. One cannot see much of a difference between
Blue-Sky and Bakoma fonts on a low quality font rasterizer.

List of additional fonts in Bakoma + Paradissa
----------------------------------------------

Bakoma + Paradissa contains in addition to the original 75 CM fonts the
AMS font set consisting of

*update:* AMS fonts in type 1 are now also available directly from the
AMS

> cmbsy6 cmbsy7 cmbsy8 cmbsy9 cmcsc8 cmcsc9 cmex7 cmex8 cmex9 cmmib6
> cmmib7 cmmib8 cmmib9 euex10 euex7 euex8 euex9 eufb10 eufb5 eufb6 eufb7
> eufb8 eufb9 eufm10 eufm5 eufm6 eufm7 eufm8 eufm9 eurb10 eurb5 eurb6
> eurb7 eurb8 eurb9 eurm10 eurm5 eurm6 eurm7 eurm8 eurm9 eusb10 eusb5
> eusb6 eusb7 eusb8 eusb9 eusm10 eusm5 eusm6 eusm7 eusm8 eusm9 msam10
> msam5 msam6 msam7 msam8 msam9 msbm10 msbm5 msbm6 msbm7 msbm8 msbm9

and some Cyrillic fonts that were derived from the CM fonts

> cmcb10 cmcbx10 cmcbx12 cmcbx5 cmcbx6 cmcbx7 cmcbx8 cmcbx9 cmcbxsl10
> cmcbxti10 cmccsc10 cmccsc8 cmccsc9 cmcitt10 cmcsc8 cmcsc9 cmcsl10
> cmcsl12 cmcsl8 cmcsl9 cmcsltt10 cmcss10 cmcss12 cmcss17 cmcss8 cmcss9
> cmcssbx10 cmcssdc10 cmcssi10 cmcssi12 cmcssi17 cmcssi8 cmcssi9 cmcssq8
> cmcssqi8 cmcti10 cmcti12 cmcti7 cmcti8 cmcti9 cmctt10 cmctt12 cmctt8
> cmctt9 cmcu10 cmcyr10 cmcyr12 cmcyr17 cmcyr5 cmcyr6 cmcyr7 cmcyr8
> cmcyr9
