# Textures

For the most part, Textures uses normal TeX that can be submitted to
arXiv without modification. However, if the TeX file contains
`\SetTexturesEPSFSpecial` (used for figure inclusion), it will need to
be commented out:

``` 
     %\SetTexturesEPSFSpecial
```

and the following line added to replace it:

``` 
     \SetepsfEPSFSpecial
```

The command `\SetepsfEPSFSpecial` selects the standard way of dealing
with Encapsulated PostScript as opposed to the Textures specific method.

## The Messy Details

The `\SetepsfEPSFSpecial` and `\SetTexturesEPSFSpecial` commands are
defined in the input file `boxedEPS.tex`, which is included by Textures
with the command `\input BoxedEPS`. The functions of these commands are
described in the comments of `boxedEPS.tex`. We need to use
`\SetepsfEPSFSpecial` because we use dvips to generate PostScript from
the TeX output.

The fix described above is known to work with Textures v1.8 up to at
least v2.0.4 and `boxedEPS.tex` dated Feb 1995 and Nov 1995.
