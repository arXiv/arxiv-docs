How to Prepare Pages for Landscape Printout
===========================================

*Note:* Because these instructions are exclusive to dvips, they are not
applicable to PDFLaTeX submissions, which produce PDF directly and do
not follow the LaTeX--\>DVI--\>PostScript--\>PDF conversion path.

If you have a wide table or other material that should be printed in
**landscape** mode, you should follow the instructions given in the
dvips info pages. For your convenience, we appended the two relevant
sections from the dvips documentation.

*Before you go on*, however, be warned that the standard paper size in
the US is **letter**, which is shorter than **A4** paper, i.e., less
wide in landscape mode, and that your landscape documents need to be
tuned to properly fit on letter paper. Otherwise text may be truncated
when printed in the US.

Note also that there are different conventions as to which way to rotate
pages, and this (apart from being upside down on screen) affects the
margins. Always check the postscript we generate here and make
adjustments as necessary.

------------------------------------------------------------------------

Paper Size and Landscape Orientation
------------------------------------

Although most TeX documents at a particular site are designed to use the
standard paper size (letter size in the United States, A4 in Europe),
the [dvips program can be customized](dvips), either site-wide or for a
particular printer.

Many documents are designed for other paper sizes. For instance, you may
want to design a document that has the long edge of the paper
horizontal. This can be useful when typesetting booklets, brochures,
complex tables, or many other documents. This type of paper orientation
is called "landscape" orientation (the default orientation is
"portrait"). Alternatively, a document might be designed for ledger or
A3 paper.

Since the intended paper size is a document design decision, not a
printing decision, such information should be given in the TeX file and
not on the dvips command line. For this reason, dvips supports a
**papersize special**. It is hoped that this special will become
standard over time for TeX previewers and other printer drivers.

### The Papersize Special

The format of the papersize special is:

         \special{papersize=WIDTH,HEIGHT}

`WIDTH` is the horizontal size of the page, and `HEIGHT` is the vertical
size. The dimensions supported are the same as for TeX; namely, in
(inches), cm (centimeters), mm (millimeters), pt (points), sp (scaled
points), bp (big points, the same as the default PostScript unit), pc
(picas), dd (didot points), and cc (ciceros).

For a US letter size landscape document, the papersize would be:

         \special{papersize=11in,8.5in}

An alternate specification of landscape:

         \special{landscape}

is supported for backward compatibility, but it is hoped that eventually
the papersize comment will dominate.

Of course, such a `\special` only informs dvips of the desired paper
size; you must also adjust `\hsize` and `\vsize` in your TeX document
typeset to those dimensions.

The papersize special must occur somewhere on the first page of the
document.

------------------------------------------------------------------------

How to Pass a Papersize Flag to our Postscript Generator
--------------------------------------------------------

If for some reason the method described above does not work for you, all
hope is not lost. You can alternatively pass a landscape flag to our
automated postscript generator to be used by dvips.

### Example

Suppose you have TeX source for some wide tables that were prepared to
be printed in landscape mode; let's call them `mywidetable1.tex` and
`mywidetable2.tex`. On your local system, these can be processed with:

         $ dvips -t landscape mywidetable1.dvi
         $ dvips -t landscape mywidetable2.dvi

On our system, this can be accomplished by including a file with special
instructions for our postscript generator in your submission. This file
has to be called `00README.XXX` — *the filename has to be all uppercase,
it starts with two zeros, and it has to be in the top level directory of
your submission*. In our example, `00README.XXX` should contain one line
for each table to be processed with the landscape flag:

         mywidetable1.dvi landscape
         mywidetable2.dvi landscape

Note that the file extensions are `.dvi` (**not `.tex`**) because the
instruction applies to the dvi to ps stage, not to the tex to dvi stage.
