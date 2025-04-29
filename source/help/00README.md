# The `00README` File Format

>NOTE:
>See [`00README.XXX`](#00readmexxx) for historical information about the `000README.XXX` file format.

## `00README` JSON file format

The `00README` is a JSON file built automatically during the submission process for Submission System version 1.5, and later. It provides specific instructions to the compiler for consistent, reproducible compilations, and provides a permanent record of what options were selected at the time of submission. At present, the entries in a classic `00README.XXX` file format will be converted into JSON at the “Review Files” step. 

The goal of the [submission 1.5](submit_tex.md#latex-processing-changes--coming-early-2025) process is to eliminate any guesswork by providing a clear and unique compilation and post-processing path, as outlined in the 00README file. It is not required (nor recommended) to manually create this file prior to submission, with some exceptions and caveats. The following is presented as technical specifications for submitters who need to customize functionality in their submissions or for interested readers. This is also presented as a way to guide programmatic submitters who would not otherwise have access to the UI submission pipeline (e.g. [SWORD](submit_sword.md)).


### Supported `00README` formats

We support more expressive formats that can be written in either JSON or YAML format. The new formats described below will be the default, and old-style `00README` will be converted.


#### JSON format

A common case is where the submission contains only a TeX file, for example: `my_super_paper.tex`. This `my_super_paper.tex` is a top-level file which should be compiled with `pdflatex`.

```
{
  "process": {
     "compiler": "pdflatex'
  },
  "sources": [
    { "filename": "my_super_paper.tex", "usage": "toplevel" }
  ]
} 
```

#### YAML format

```
process:
  compiler: pdflatex
sources:
  - filename: my_super_paper.tex
    usage: toplevel
```

Note: as long as there is no other tag, the usage: `toplevel` is not necessary. Generated `00README` files will contain it, but parsing allows for leaving out the toplevel specification.

#### EPS file with alternative compilation path

In the following example, the paper includes an Encapsulated PostScript (eps) file; thus an alternative compilation path is required via `latex` followed by `dvips` and `ps2pdf`. This can be specified in a simple method as:

```
process:
  compiler: latex
sources:
  - filename: my_super_paper.tex
```

The `compiler: latex` is actually shorthand for `compiler: latex+dvips_ps2pdf` because this is the only path we are currently supporting.

We have not included the `usage: toplevel` line for `my_super_paper.tex`, since this will be automatically added.

#### Additional functionality

Additional functionality supported in the original `00README`include: the `landscape` and `keep_comments`. The example uses a toplevel tex file `my_super_paper.tex`, but requests it be compiled with `tex` (not `latex`), and the postprocessing makes sure that the generated `dvi` file is converted in landscape mode, and keeps comments (by using `-K0`).

```
process:
  compiler: tex+dvips_ps2pdf
sources:
  - filename: my_super_paper.tex
    usage: toplevel
  - filename: my_super_paper.dvi
    orientation: landscape
    keep_comments: true
```

The above example should be enough to write well-specified `00README` files in the new format as YAML or JSON files, covering most common cases.

### Formal specification

If you need more specific information, here is a more formal specification.
```
{
  "process": {
    "compiler": "<COMPILER STRING>" | <COMPILER_SPEC>,
    "bibliography": {
      "processor": "bibtex" | "biber" | ...,
      "pre_generated": true
    },
    "index": {
      "processor": "makeindex",
      "pre_generated": true
    }
  },
  "sources": [
    {
      "filename": "<FILENAME>",
      "usage": "toplevel" | "include" | "ignore",
      "orientation": "landscape" | "portrait",
      "keep_comments: <BOOL>
    },
    ...
  ],
  "stamp: <BOOL>,
  "nohyperref": <BOOL>
}
```
or as YAML:

```
process:
  compiler: <COMPILER_STRING> | <COMPILER_SPEC>
  bibliography:
    processor: bibtex | biber | ...
    pre_generated: true
  index:
    processor: makeindex
    pre_generated: true
sources:
  - filename: <FILENAME>
    usage: toplevel | include | ignore
    orientation: landscape | portrait
    keep_comments: <BOOL>
stamp: <BOOL>
nohyperref: <BOOL>
```
The `COMPILER_SPEC` allows configuring the single stages from TeX source code to the final output:

```
{
  "engine": "etex",
  "lang": "tex" | "latex" | "pdf" | "html",
  "output": "dvi" | "pdf",
  "postp": "dvips_ps2pdf"| "none"
}
```

The `lang: pdf` is for pdf-only submissions, and `lang: html` is for html-only submissions.

### Compilation Specifications

We are currently supporting the following `COMPILER_SPEC`s. In the following we also list the `COMPILER_STRING` equivalents. The `COMPILER_STRING` provides a “stringy” representation of the compilation paths.

- #### plain tex
    ```
    COMPILER_SPEC  
    {
    "engine": "etex",  
    "lang": "tex",  
    "output": "dvi",  
    "postp": "dvips_ps2pdf"  
    }
    ```
    Equivalent `COMPILER_STRING: tex` or `etex+dvips_ps2pdf`

- #### LaTeX with dvips/ps2pdf 
    ```
    COMPILER_SPEC  
    {  
    "engine": "etex",  
    "lang": "latex",  
    "output": "dvi",  
    "postp": "dvips_ps2pdf"  
    }
    ```
    Equivalent `COMPILER_STRING`: `latex` or `latex+dvips_ps2pdf`

- #### LaTeX with PDFLaTeX
    ```
    COMPILER_SPEC  
    {  
    "engine": "etex",  
    "lang": "latex",  
    "output": "pdf",  
    "postp": "none"  
    } 
    ```
    Equivalent `COMPILER_STRING: pdflatex`

#### Compilation order

The final output is assembled based on the following rules:

- any file tagged as `usage: toplevel` will be compiled with the specified compiler (including postprocessing, and in the future bibliography and index creation).

- the order of files is determined by the order given in the `00README` file.

- the arXiv watermark is applied to the final pdf top page if `stamp: true` (which is the default).

Note that as of now, all toplevel files are compiled with the same compiler. 

#### Additional notes  
- `process.compiler` – only those combinations listed above are currently supported. Other values will make the submission fail.  

- `process.bibliography` and `process.index` – we still require a pre-generated .bbl ssh file (or .idx) be included, meaning, we require that `pre_generated: true`.  

- `nohyperref` – this is only for backward compatibility and is completely ignored during compilation. We no longer add hyperref by default, and leave it to the document to load the hyperref package.



## `00README.XXX`

A file of this name can used to specify special handling for the submission and/or for individual files. The name of the file is spelled "zero-zero-README-dot-X-X-X".

The `00README.XXX` file is read line-by-line before files are processed by AutoTeX. The order of lines is unimportant.

*   [Ignoring files within the submission package](#ignoring)
*   [Including files normally ignored](#including)
*   [Declaring your top-level LaTeX file](#toplevel)
*   [Enabling Landscape mode in `dvips` submissions only](#landscape)
*   [Disabling HyperTeX for your submission](#nohypertex)
*   [Keep comments within figures during `dvips`](#keepcomments)
*   [Turn off the arXiv stamp on the generated PostScript and PDF files](#nostamp)

<a name="ignoring" id="ignoring"></a>

### Ignoring files

Include lines such as:

```
filename1.ext1 ignore
filename2.ext2 ignore
```

This is useful if you have included other files which are not necessary for processing and don't belong into a subdirectory for ancillary material either.

<a name="including" id="including"></a>

### Including files -- not ignoring and not reporting junk

Include lines such as:

```
filename1.whatever include
filename2.whatever include
```

This will stop detection of unknown file type and will thus stop the file being given to AutoTeX. This can be used to include extra files linked from an HTML submission.

<a name="toplevel" id="toplevel"></a>

### Declaring the top-level (parent) TeX file

It is very rarely necessary to do this explicitly because arXiv employs a series of heuristics which can usually determine the top-level file. For example, if only one of a set of LaTeX files contains a `\documentclass` command, that file is very likely the top-level file. (Note -- We intend to cease using these hueristics in April 2024. Extra .tex files containing `\documentclass` commands will be ignored, and the only way to get the old behavior will be the method documented here.)

If it is necessary (e.g., if you are using the `subfiles.cls` class in your document's structure), include a line that says:

```
myMainTexFile.tex toplevelfile
```

`myMainTexFile.tex` is the name of the parent TeX file. Note that this does not affect the final assembly order of the final pdf, which is always assembled in alphanumeric order.

Multiple toplevelfile declarations can be used to combine multiple .tex files, each containing a `\documentlcass` command into a single PDF ouput file. For example:

```
myMainTexFile.tex toplevelfile
AppendixSupplement.tex toplevelfile
```

will produce a single PDF called myMainTexFile.pdf containing the Preamble, myMainTexFile, and AppendixSupplement, in that order.

<a name="landscape" id="landscape"></a>

### Landscape mode

It is possible to tell AutoTeX to send a flag to `dvips` requesting landscape mode. This sometimes results in upside-down output, but there is currently no facility to fix this. The command is:

```
filename.dvi landscape
```

where `filename.dvi` is the name of the DVI file that TeX will produce when processing the submission, and `filename` is the main TeX file without the `.tex` extension. Also, we have an extensive help library on setting the [landscape environment](faq/landscape.md).

<a name="nohypertex" id="nohypertex"></a>

### Disable attempt to use HyperTeX

See also: [Disabling hypertex](faq/mistakes.md#nohypertex).

```
nohypertex
```

This stops any attempt by arXiv to automatically augment a paper with hyperlinks. However, it does not affect any facilities explicitly used within the paper's source. There is no filename associated with this switch.

<a name="keepcomments" id="keepcomments"></a>

### Keep comments when doing `dvips`

This is mostly needed when receiving a [`PS BAD` warning](faq/mistakes.md#psbad)

```
filename.dvi keepcomments
```

Sends the `-K0` flag to `dvips`, telling it not to strip comments. This is needed when PS/EPS figures (included in the DVI) contain binary data having '`%`' characters at the beginning of lines (by default, our `dvips` processor interprets these lines as comments), or if the comments are required for some other reason (e.g., Adobe Illustrator output).

Note that `filename.dvi` is the name of the DVI file that TeX will produce when processing the submission, and `filename` is the main TeX file without the `.tex` extension.

Also note that it may be necessary to rename your `.TEX` files to `.tex` for this function to work properly.

<a name="nostamp" id="nostamp"></a>

### Stopping the addition of the arXiv stamp

```
nostamp
```

This tells AutoTeX not to add the arXiv stamp to the left-hand edge of the page. No filename is specified.

