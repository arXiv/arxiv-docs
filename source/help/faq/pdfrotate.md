# Why are some pages in the generated PDF file rotated?

Automatic page rotation depending on page content is an optional feature
of the PostScript to PDF conversion. It is enabled by default.

# How do I avoid page rotation?

Page rotation can be disabled with the following PostScript literal,
which sets the **AutoRotatePages** parameter for the distillation
process:

``` 
 /setdistillerparams where {pop}{userdict /setdistillerparams {pop} put}ifelse
 <</AutoRotatePages /None>> setdistillerparams
```

The above snippet can be directly inserted in the `%%Prolog` section of
a PostScript figure or via a PostScript literal `\special{! ....}` in
the preamble of the (La)TeX source (Note: there is a `"!"` after the
opening parenthesis).

**Note:** It appears that `emulateapj.cls` prevents `\special{! ...}`
from being passed through to the PostScript, so if you use
`emulateapj.cls` you have to insert the distiller settings directly into
a .eps figure to take effect.

Obviously this technique allows for customization of all other distiller
parameters, too, see [distiller
options](texprobs.md#distiller_params).
