# Why are there Problems with my PostScript File?

When processing TeX submissions with PostScript (PS/EPS) figures, or
submissions comprised of only PostScript files, arXiv's AutoTeX system
will attempt to convert the resulting PostScript file to PDF (which is
by far the most common download format). Submissions that can be
processed fine to this point may fail PostScript to PDF conversion for a
number of reasons. Various fixes and work-arounds are listed below.

## Embedded % signs in PS/EPS figures

Some graphics programs embed images as binary data. This leads to all
sorts of characters appearing in the file, including '`%`' characters. A
line beginning with a '`%`' character is a postscript comment, and by
default dvips removes any postscript comments from included postscript
files (for DSC compliance and to make the final postscript file
smaller). Consequently any postscript files containing binary data can
have random lines stripped out.

To find the lines of a file which begin with '%' use

``` 
    grep '^%' fig.ps
```

Any lines of binary data indicate a problem. Proper PostScript comments
should be human readable, or at least contain only printable characters
(`0-9, A-Z, a-z`).

To work around this, you can [pass a special flag to our AutoTeX
processor](mistakes.md#psbad) to keep all lines beginning with
'`%`' (at the cost of portability). To do this, include a file
`00README.XXX` which includes an instruction specific to the filename of
the dvi file for your submission, usually `filename.dvi` if your TeX
file is `filename.tex`:

``` 
     filename.dvi keepcomments
```

## Errors in individual PS/EPS figures

To debug postscript errors, run ghostscript individually on each figure.
This should determine which one contains the problem; a valid postscript
file should not produce any errors from ghostscript. An example of a
postscript error detected by ghostscript is:

``` 
    $ gs fig1.ps
    Aladdin Ghostscript 6.01 (2000-03-17)

    Error: /limitcheck in --moveto--
    Operand stack:
        2147483647 0
    Unexpected interpreter error -21.
    Current file position is 11858
```

The "`Current file position`" gives the character position of the error
(e.g. in emacs, use `M-x goto-char` to jump to this point).

The checking performed by ghostscript is strict. A postscript printer
will ignore some errors in an attempt to output the file. However, it is
worth making your postscript file work without any errors so that it can
be viewed on screen.

## Trailing or leading garbage

Trailing characters at the end of a postscript file will cause problems
when the file is included in the paper (e.g., using
`\usepackage{graphics}`) or combined figures. Note that trailing
characters **will not be detected** by checking with ghostscript, since
they follow the end of the postscript.

Leading garbage, such as mail headers, can also cause problems. You can
load the postscript file into a text editor to see if there are obvious
garbage lines (e.g., your email signature file).

## Out of range coordinates

Buggy graphics programs occasionally output spurious large coordinates
which overflow the normal range of integers. For example,

``` 
    2147483647 0 moveto
```

Note that `2^31-1=2147483647` in the above example is a textbook case of
common programming errors. Check for more recent and hopefully bug fixed
versions of your graphics software. In particular, if you use ACE/gr
(Xmgr), have a look at its descendant
[Grace](http://plasma-gate.weizmann.ac.il/Grace/).

The offending coordinate(s) can usually be replaced by zero without
affecting the final output, because it is usually followed by a valid
moveto command which cancels its effect. Load the file into a text
editor and zero the excessive coordinate, then, check that the resulting
figure looks unchanged when viewed. Report the bug to the author of the
graphics program you used.

## Figures encoded with 8-bit characters (^D)

Figures containing 8-bit characters will appear fine individually, but
may cause display problems when embedded in a paper. The problem with
these figures is that they contain literal JPEG wrapped in a postscript
envelope, e.g.:

``` 
    $ tail +172 Fig3a.eps | file -
    /dev/stdin: JPEG image data, JFIF standard 1.01, resolution (DPI), 72 x 72
```

This is perfectly legal to do, however the arXiv version of `dvips`
cannot handle the `0x04` characters (i.e., `^D`) in the JPEG stream. In
this case, it is not the format that needs to be changed, but the the
encoding of the image data within the EPS file.

One way around this is to convert the JPEG to EPS format using
[jpeg2ps](../../help/bitmap/software.md#jpeg2ps) with the `-h` flag to avoid the
8 bit data:

``` 
    $ jpeg2ps -?

    -b        binary mode: output 8 bit data (default: 7 bit with ASCII85)
    -h        hex mode: output 7 bit data in ASCIIHex encoding
```

## Beware of false alarms

We do the PostScript syntax check with "`gs -DNODISPLAY ... `", and in
rare circumstances this leads to spurious error messages due to missing
device initialization. This will typically report something like:

``` 
    "Error: /undefinedresult in --currentpoint--".
```

If you receive an automated **PS BAD** warning, but there seems to be
nothing wrong with your submission, you should request **PDF**. If PDF
can be generated here, the PostScript is almost certainly syntactically
correct.
