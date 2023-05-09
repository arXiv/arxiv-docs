# Papersize/Layout Problems: Margins are Different and/or Text is Truncated

**Note:** prior to arXiv's [TeXLive 2020 upgrade](texlive.md), all submissions were forced into US Letter page dimensions. The current practice is to allow other paper sizes when explicitly stated, with `letterpaper` being the default page size. The information below may still be of use for diagnosing odd behavior around local display or printing problems. 

There are many possible reasons for a papersize/layout problem. It may
be due to differences in style files used, variations in layout
parameters of the TeX installation, badly adjusted printer offsets, etc.

The most common cause, however, is due to the differences in
**papersize**. The standard papersize in the US is **US letter**, which
is shorter and wider than **(European) DIN A4** paper, as shown in the
table below:


| Tables        | Inches       | Inches       | Cm          | Cm  |
| ------------- | ------------- | ------------- |:-------------:| -----:|
| US Letter | 8.5    | 11    | 21.59 | 27.94 |
| Din A4    | 8.26   | 11.69 | 20.99 | 29.70 |

In order for your submission to print well for most interested readers,
you need to tune the layout to fit on both papersizes. This mainly
affects the margins you choose and the style file options.

### Solution

The easiest way to adjust margins without changing page or line breaks
is to use the (La)TeX commands `\voffset` and `\hoffset` in the document
header. For example, for a shift of 0.8 inches upwards use:

``` 
     \voffset=-0.8in
```

somewhere before `\begin{document}`.

Moreover, if the style file or documentclass allow for papersize
selection, you should always use the letter option for submission to
arXiv; e.g.,

``` 
     \documentclass[letterpaper]{article}
```

For a more general solution, see the [geometry
package](arXiv-texsize.ps.gz).

If you suspect style file differences to be responsible for layout
and/or margin variations, you should bundle the style file(s) in
question with your submission. Files that unpack in the same directory
as your main TeX file will be used instead of system files with the same
name.

## Testing

Some postscript display programs, like Ghostview, GSview, and GV, allow
explicit papersize settings and/or display the paper boundaries
according to the papersize setting in the postscript file, and thus
allow for easy interactive layout tuning for optimal printout on
lettersize and A4 paper.

Also remember that you can and should replace as often as necessary
before 16:00 US Eastern time on the day of submission to tune layout and
to make other changes without bumping the revision number.

## dvips Settings

If the postscript generated at arXiv displays as you expect, but prints
with different margins or is truncated at the top or bottom, the likely
reason is a difference in offsets used. For printing with `dvips`,
offsets are configurable on a per printer basis, and capable sysadmins
tune these to specific printers.

A frequent pitfall is the default papersize setting and corresponding
offsets. Check the file `config.ps` for papersize settings, or look at
the comments at the top of the postscript file for a line
`%%DocumentPaperSizes: Letter`, or try:

``` 
     dvips -t letter -o usletter.ps your.dvi
```

versus

``` 
     dvips -t a4 -o europeanpaper.ps your.dvi
```

to see the difference. Recent versions of teTeX come with `a4` as
default.
