# Why is my PostScript File so Large?

Many current word processors and graphics programs create excessively
large PostScript files which include large amounts of "postscript junk".

Macintosh and Windows programs seem to have the worst problems. Using
programs on one of these platforms, it is all too easy to unknowingly
create outrageously huge files. Such files will be much harder for
readers to download, and some readers with poor network connections
(such as in some developing countries) will not be able to obtain these
files at all.

### What can I do about it?

Authors who are aware of the problem can make an effort to check for
"junk" PostScript, and even remove it manually from their files if
necessary. The most common sources of unnecessarily large PostScript
files are:

  - [unnecessary font inclusion](#fonts)
  - [unnecessary preview inclusion](#previews)

There are easy ways to avoid these, as described below.

See also our [sizes](/help/sizes.md) and [bitmap](/help/bitmap/index.md) help pages.

<span id="fonts"></span>

## Dealing with Unnecessary Fonts

The most prevalent cause of huge amounts of junk in PostScript files is
the inclusion of font information. For instance, simple figures often
have labels or captions. If the font used for this is not in the
standard PostScript font families of

> Helvetica, Times, Courier, and Symbol

then the full font definition will be included in the PostScript file.
This adds anywhere from 50-200kB per font (in some cases just to print a
single letter\!\!). Some poorly-written software will even include all
the standard fonts as well. This is intolerable, since every PostScript
interpreter is *required* to have these four font families built-in
already.

You can check to see which fonts are included in your file by looking
for

``` 
     %%BeginFont
```

or

``` 
     %%BeginResource: font
```

lines (and the corresponding `%%End...` lines) in your file.

If you find non-standard fonts present (i.e., anything outside of
Helvetica, Times, Courier, and Symbol), then you should try to find an
option in your program to switch them to one of the four standard
families.

If you find font information for the standard fonts, you can safely slim
down your file by removing them. Load the file into a text editor and
manually delete the lines from `%%BeginFont` to `%%EndFont` (inclusive).
After making any modifications you will want to check that your file
still prints and views correctly, just in case any accidents occurred
while editing the file.

<span id="previews"></span>

## Dealing with unnecessary Previews

Some applications, particularly on Macs and PCs, include a large
uncompressed "preview" bitmap in every postscript file. This is supposed
to allow a very crude approximation of the PostScript file to be
rendered on screen when viewed in a non-PostScript viewer. This preview
is low quality, and is superfluous for figures submitted to arXiv in any
case.

Previews are easy to find and eliminate. Submitters should look for any:

``` 
     %%BeginPreview
```

lines followed by hexadecimal data (e.g., `092f62696e2f...`), and ending
with:

``` 
     %%EndPreview
```

Remove all the hexadecimal data and the `%%BeginPreview` and
`%%EndPreview` lines to eliminate the preview completely.

Note that the savings can be considerable. One example had two figures
with preview bitmaps. One started as a 482kB file and slimmed to 154kB,
the other was reduced from 550kB to 146kB\! Removing the bitmaps thus
made the file much easier for readers to download.
