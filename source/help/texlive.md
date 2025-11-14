# TeX Live at arXiv

*   [Supported TeX Live versions](#supported-tex-live-versions)
*   [Supported TeX processors](#supported-processors)
*   [Notes concerning the use of `xelatex`](#xelatex-use)
*   [Important changes introduced in TeX Live 2025](#changes-2025)




<span id="supported-tex-live-versions"></span>
## Supported TeX Live versions

arXiv currently supports TeX Live 2023 and TeX Live 2025, with 2025 being the default.
Submissions can select either of the two.

State of TeX Live in use:

*   TeX Live 2023: state from 2023-05-21
*   TeX Live 2025: state from 2025-08-03


<span id="supported-processors"></span>
## Supported TeX processors

We are currently only supporting the following types of TeX submissions:

*   plain TeX submissions named `tex` during the submission: those are converted using `etex` followed by `dvips` and `ps2pdf`;
*   plain TeX submissions named `pdftex` during the submission: those are converted using `pdfetex`.
*   LaTeX submissions in DVI mode named `latex` during the submission: those are converted using `latex` followed by `dvips` and `ps2pdf`;
*   LaTeX submissions in PDF mode named `pdflatex` during the submission: those are converted using `pdflatex`.
*   LaTeX submissions in PDF mode named `xelatex` during the submission: those are converted using `xelatex`.

During the submission process, you will be asked which of the processor you want to use for your
submission.


### Selecting the correct processor

Selecting the correct processor is generally an easy task, because we will offer you the hopefully correct
one automatically during submission. If you want to decide by yourself, here is a quick guide:

*   if it is plain TeX, select `tex` or `pdftex`;
*   if it is a LaTeX document that includes `eps` files, select `latex`;
*   if it is a LaTeX document that includes `jpg`, `png` (and some more) files, select `pdflatex`;
*   if it is a LaTeX document that includes both `eps` and `jpg`/`png`/`pdf` files, select `xelatex`;
*   if you don't know, select `pdflatex`

Note that at the moment, the processor type is fixed for all parts of a multi-file submission.


<span id="xelatex-use"></span>
## Notes concerning the use of `xelatex`

XeLaTeX ([TUG page](https://tug.org/xetex/), [Wikipedia entry](https://en.wikipedia.org/wiki/XeTeX)) has been
introduce as possible processor option in November 2025. The main changes compared to `pdflatex` are:

* Unicode support
* Support for TrueType and OpenType fonts

Note that font lookups in XeLaTeX using the `fontspec` package can be done in two ways: Using the **Font Name**
and using the **File Name**. For lookups using the font name, `fontconfig` support is necessary, and fonts need
to be registered with `fontconfig`. At arXiv, practically no fonts are registered with `fontconfig` (only a small
set of system fonts).

Thus, to use any of the long list of TrueType or OpenType fonts shipped by TeX Live, one needs use the file name
lookup method.

Example for the `TeX Gyre Pagella` font:

Correct: Lookup via filename

    \setmainfont{TeX Gyre Pagella}[...]

Incorrect/will not work: Lookup via font name

    \setmainfont{texgyrepagella-regular.otf}[...]

For more details see the [documentation of the fontspec](https://mirrors.ctan.org/macros/unicodetex/latex/fontspec/fontspec.pdf) package.


<span id="changes-2025"></span>
## Important changes introduced in TeX Live 2025

We list the most common errors we have seen in the set of current submissions.
Further information can be found at the [Overleaf announcement that TeX Live 2025
is now available](https://www.overleaf.com/blog/tex-live-2025-is-now-available).

### Issues with the `array` package

Under various circumstances, in particular when using a `revtex` documentclass together with the `array`
package, compilation issue might arise.

We suggest either selecting TeX Live 2023, or requesting an older version or the array package using

```
\usepackage{array}[=2016-10-06]
```

### Usage of `cleveref` package

The `cleveref` package has not been updated to work with TeX Live 2025. When using it in a submission
with TeX Live 2025, references will all include the same name (i.e., all `\cref{...}` will have the
same "name" like "Proposition").

Either select TeX Live 2023 for your submission, or add, for each definition of a theorem-like environment
you use, the necessary `\crefalias`.

Example: If there is

```
\newtheorem{theorem}{Theorem}[section]
```

then a line as follows needs to be added:

```
\AddToHook{env/theorem/begin}{\crefalias{section}{theorem}}
```

### Loading of packages outside the toplevel

Loading packages using `\usepackage` or `\RequirePackage` will now fail when happening in a group `{...}`.
This manifests itself most prominently in the use of `\singlespace`, `\doublespace` etc from the `setspace`
package. These are environments (!) and need to be started/ended with `\begin{...} ... \end{...}`.

If e.g. `\doublespace` is used as is, it only starts the environment but does not close it. Any `\usepackage`
further down will throw an error.

Solution: Either use proper environments with `\begin{...}` and `\end{...}`, or use the -ing commands
like `\doublespacing` instead.

### `minted` and other "frozen cache" packages

Caches generated by `minted` or any other package in the same vein require the same
TeX Live version during generation of the cache and the one used at arXiv.

Note in particular that `minted` got a completely new version in TeX Live 2025, and
the previous behavior and arguments to the `\usepackage[...]{minted}` call need revision.
Most recipes given on the internet are still referring to minted **version 2** or below, while
TeX Live 2025 uses **minted version 3**.

As a simple recipe:

* Use `\usepackage{minted}` in your document, and run `(pdf)latex` once with `-shell-escape`. This should create a directory `_minted`.
* Include the `_minted` directory in your upload. No further changes are necessary. In particular, using options like `frozencache` etc are now unnecessary.

You can check success by running `(pdf)latex -no-shell-escape` and check whether errors related to `minted` occur.

### Loading order of `hyperref` and `hyperxmp`

The package `hyperxmp` introduced a requirement that `hyperref` is begin loaded **before** `hyperxmp`.
Since many times, the loading of `hyperref` also did set various parameters, this has to be changed.

Before -- this does not work with TeX Live 2025:

```
\usepackage{hyperxmp}
\usepackage[pdfauthor={...},...]{hyperref}
```

needs to be converted to

```
\usepackage{hyperref}
\usepackage{hyperxmp}
\hypersetup{pdfauthor={...},...}
```

### Other packages and classes that are known to have problems

*  `aastex` version 6 and 7: similar to the array problem mentioned above, but the fix does not work.
*  `revtex`: problems with array package mentioned above. Can usually be fixed as mentioned above.
