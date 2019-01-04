# Using Feynmf on arXiv

<span id="overwrite"></span>

## Why does my submission fail the automatic TeXing procedure when I use Feynmf?

When using Feynmf to create graphs, the latex compiler generates
metafont files for each figure (with the extension '`.mf`'). Because our
latex processor is not allowed to overwrite any files that are
submitted, it will freeze during processing if these files were included
in the submission package. When submitting TeX source that uses feynmf,
*do not* include `.mf` files.

<span id="nolabel"></span>

## Why don't the labels for my figures appear when I use Feynmf?

The label files (with the extension `.t#` where '`#`' is a number)
*should* be included. Due to intricacies of the on-demand font
generation, arXiv does not generate those label files. (The label files
require the intermediate `fd.log` files to be present for the second
latex pass, but when metafont is automatically run from the latex
process to generate `.tfm` files on demand, it cleans up after itself
and removes the `fd.log` file, preventing the label files from being
generated.)
