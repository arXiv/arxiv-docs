Possible Problems
=================

The bitmapped PostScript file is bigger than the original
---------------------------------------------------------

Make sure you gzip both files before comparing their sizes. If the new
figure has a gzipped size greater than that of the old figure, then
there are several things you can try.

-   Try reducing the resolution of the bitmap.
-   Try reducing the number of colors used.
-   Try switching to greyscale instead of color, or black/white instead
    of greyscale.

Finally remember that bitmapping is not magic It can reduce the size of
some figures, but will make others larger. Some skill is required in
judging which images will bitmap well.

Bitmapping works whenever the original PostScript was so inefficient
that it actually takes less space to specify the entire image
pixel-by-pixel than using the original form (modulo differences in
compression). Obviously the original PostScript has to be very
inefficient for this to be the case, but there are plenty of programs
which do generate such really inefficient output.

The bitmap has strange checkerboard patterns or stripes
-------------------------------------------------------

If the original PostScript itself was a bitmap (e.g. produced by IDL or
some other numerical package) don't attempt to bitmap it again. A bitmap
PostScript file contains lots of hexadecimal digits and looks something
like this:

            $ more bitmap.ps
            %!PS-Adobe-2.0 EPSF-2.0
            ......
            [ 1768 0 0 -2698 0 2698 ]
            { picstr readstring }
            image
            ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
            ffffffffffffffffffffffe0007fffff1ffffffe7ffffff0007fffffffff

Re-bitmapping a bitmap can produce all sorts of horrible aliasing
effects. Instead, go back to the original data and produce something
more efficient from it (e.g., GIF or JPEG, or lower resolution
PostScript).

The bitmap file has huge amounts of whitespace around it
--------------------------------------------------------

You need to crop the image using XV's "Autocrop" or the PBM `pnmcrop`
command. For example, Ghostscript produces a bitmap which fills the
page, and the image usually only occupies a small part of it.

The bitmap version doesn't look very good on the screen
-------------------------------------------------------

Bitmapped figures usually look much better when printed (at 300dpi) than
when viewed on a monitor (at &lt;100dpi).
