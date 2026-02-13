# Oversized Submissions

Problems
--------

The usual reason for submissions to be very large is the presence of a
small number of inefficient figures. These submissions can be made
smaller by making the figures more efficient. We do not accept
submissions with omitted figures, see policy information below.

If you have trouble submitting a *very* long paper, such as a long
review article with many small figures, or a thesis, AND you are sure
that you have efficient figures, then [contact the arXiv
administrators](contact.md) to ask for an exception (be sure to quote
the automatic rejection identifier and to explain the large size).

Please think about the time it will take people to download your papers.
arXiv is a resource used throughout the world and many users do not have the
fast reliable network connections, fast computers, and printers with
large memory that are common in large universities.

Making Submissions Smaller
--------------------------

Use of the appropriate tools and image formats for figures is the key to
preparing an efficient submission that will be convenient for people to
download.

Most submissions to arXiv are fine, but some submissions include files
in inefficient and unnecessarily large formats. Most oversized figures
can easily be shrunk by appropriate choice of format or resolution.

Photographic images should usually use JPEG encoding. Diagrams and line
drawings should preferably use PDF, PNG, GIF or PostScript. For a discussion on
shrinking figures, see our [help on bitmapping](bitmap/index.md).

It is possible that you will receive a notification message asking you
to take a few simple steps to convert your biggest files into more
suitable formats before resubmitting.

Starting with February 2026, we will issue a warning during the submission
process if images larger than 34 Megapixel (this is about the size of a
full size A4 image at 600dpi) are found.

For PNG files that can be embedded into the resulting PDF without reencoding,
these warnings are suppressed.

Additional Policy Information
-----------------------------

If you include reduced size figures with your submission you are free to include
larger figures as [ancillary files](ancillary_files.md) or
provide links to larger alternative versions of figures stored at your
website.

We do not accept submissions with omitted figures.


Quickly Reducing File Size
--------------------------

It is possible to quickly reduce the overall file size of your
submission by running a simple `bash` shell command:

         for i in *ps; do ps2pdf -DEPSCrop $i; done;


This command will convert all the files matching filenames ending with
`ps` (which will cover both `.eps` as well as `.ps` figures). Please
check the resultant figures carefully, as we are not responsible for any
errors that may occur. However, this mechanism has proven quite
effective for rapidly converting whole directories into PDF files, using
the same file names.

Note that you may have to update the figure inclusion commands.


Optimizing PNG Images for Fast Processing
------------------------------------------

PNG image can be embedded by `pdflatex` without re-encoding and thus
very quickly assuming that the PDF does not contain one of the following
incompatible features:

- Palette/indexed color type
- Alpha channels (RGBA or transparency)
- Color profile chunks: gAMA, sRGB, cHRM, iCCP
- Metadata chunks: sBIT, bKGD, hIST, tRNS, sPLT
- Interlacing (Adam7)

Authors should check for these settings in the software used to originally
create the images.

Note that images that do not contain any of the above incompatible features
will not be flagged as oversized, but the size will still put a burden
on PDF **viewers** which need to decompress the embedded PNGs, which will
make page loading speed slow.


### Checking and converting images

The tool [`png-pdftex-tool`](https://github.com/norbusan/png-pdftex-tool)
(developed by an arXiv developer and TeX Live Team member), allows for
checking and converting images into an efficient format.

See the linked page for details and usage examples.

