# The 00README.XXX file

A file of this name can used to specify special handling for the submission and/or for individual files. The name of the file is spelled "zero-zero-README-dot-X-X-X".

The `00README.XXX` file is read line-by-line before files are processed by AutoTeX. The order of lines is unimportant.

*   [Ignoring files within the submission package](#ignoring)
*   [Including files normally ignored](#including)
*   [Declaring your top-level LaTeX file](#toplevel)
*   [Enabling Landscape mode in `dvips` submissions only](#landscape)
*   [Disabling HyperTeX for your submission](#nohypertex)
*   [Keep comments within figures during `dvips`](#keepcomments)
*   [Turn off the arXiv stamp on the generated PostScript and PDF files](#nostamp)
*   [Defining a custom fontmap file](#fontmap)

<a name="ignoring" id="ignoring"></a>

## Ignoring files

Include lines such as:

```
filename1.ext1 ignore
filename2.ext2 ignore
```

This is useful if you have included other files which are not necessary for processing and don't belong into a subdirectory for ancillary material either.

<a name="including" id="including"></a>

## Including files -- not ignoring and not reporting junk

Include lines such as:

```
filename1.whatever include
filename2.whatever include
```

This will stop detection of unknown file type and will thus stop the file being given to AutoTeX. This can be used to include extra files linked from an HTML submission.

<a name="toplevel" id="toplevel"></a>

## Declaring the top-level (parent) TeX file

It is very rarely necessary to do this explicitly because arXiv employs a series of heuristics which can usually determine the top-level file. For example, if only one of a set of LaTeX files contains a `\documentclass` command, that file is very likely the top-level file.

If it is necessary, however, include a line that says:

```
myMainTexFile.tex toplevelfile
```

where `myMainTexFile.tex` is the name of the parent TeX file. Note that this does not affect the final assembly order of the pdf output. That is always done alphanumerically. 

<a name="landscape" id="landscape"></a>

## Landscape mode

It is possible to tell AutoTeX to send a flag to `dvips` requesting landscape mode. This sometimes results in upside-down output, but there is currently no facility to fix this. The command is:

```
filename.dvi landscape
```

where `filename.dvi` is the name of the DVI file that TeX will produce when processing the submission, and `filename` is the main TeX file without the `.tex` extension. Also, we have an extensive help library on setting the [landscape environment](faq/landscape "arXiv landscape help page").

<a name="nohypertex" id="nohypertex"></a>

## Disable attempt to use HyperTeX

See also: [Disabling hypertex](faq/mistakes#nohypertex).

```
nohypertex
```

This stops any attempt by arXiv to automatically augment a paper with hyperlinks. However, it does not affect any facilities explicitly used within the paper's source. There is no filename associated with this switch.

<a name="keepcomments" id="keepcomments"></a>

## Keep comments when doing `dvips`

This is mostly needed when receiving a [`PS BAD` warning](faq/mistakes#psbad)

```
filename.dvi keepcomments
```

Sends the `-K0` flag to `dvips`, telling it not to strip comments. This is needed when PS/EPS figures (included in the DVI) contain binary data having '`%`' characters at the beginning of lines (by default, our `dvips` processor interprets these lines as comments), or if the comments are required for some other reason (e.g., Adobe Illustrator output).

Note that `filename.dvi` is the name of the DVI file that TeX will produce when processing the submission, and `filename` is the main TeX file without the `.tex` extension.

Also note that it may be necessary to rename your `.TEX` files to `.tex` for this function to work properly.

<a name="nostamp" id="nostamp"></a>

## Stopping the addition of the arXiv stamp

```
nostamp
```

This tells AutoTeX not to add the arXiv stamp to the left-hand edge of the page. No filename is specified.

<a name="fontmap" id="fontmap"></a>

## Defining a custom font mapping

You can bundle non-standard or custom fonts with your submission and instruct `dvips` to use an additional font map file, e.g. `myfonts.map`, so that `dvips` is executed with the fontmap option:

`dvips -u+./myfonts.map`

by adding a file called 00README.XXX to your submission with the directive:

```
myfonts.map fontmap
```

which identifies your private font map file as a `dvips` fontmap. For map file syntax consult the dvips info pages. Many font bundles from [CTAN](http://www.ctan.org/) come with their custom font map files, and you can use these as is with this directive. The file name of the font map file must have extension "`.map`" and it must consist of letters `A-Z, a-z` only.
