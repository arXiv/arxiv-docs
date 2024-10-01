# LaTeX Markup Best Practices for Successful HTML Papers

To help authors achieve well formatted HTML, and to avoid errors during conversion, we recommend following these best practices. 

## Use LaTeX Packages that will lead to good HTML 

To improve conversion from LaTeX to HTML, use packages that are supported by the LaTeXML converter. [Please view the list of currently supported packages (ending in .ltxml)](https://corpora.mathweb.org/corpus/arxmliv/tex_to_html/info/loaded_file).

### What if my publisher requires me to use a package that is not supported?

If the package currently does not have support, we encourage you to reach out to your publisher and ask them to contribute a mapping to HTML for LaTeXML. A ‘mapping’ of LaTeX to HTML is an interpretation that allows the LaTeX converter to successfully translate the LaTeX package into functional HTML. LaTeXML is public domain software and is open to third-party contributions. Publishers can contribute directly to the [github project](https://github.com/brucemiller/LaTeXML/issues), or work with the [LaTeXML team](https://github.com/brucemiller/LaTeXML/blob/master/README.pod) on building support for their materials.

### Request support for your preferred packages

[Open new Github issue for the LaTeXML team](https://github.com/brucemiller/LaTeXML/issues), or add to an existing issue. 

## Use Macros that support accessibility

### Use a standardized front matter block

There are many ways that publishers build their front matter, but most packages follow a standard (if limited) layout such as: 

```
\title{My article’s title}
\author{Author One \AND Author Two…}
\begin{abstract}
…..
\end{abstract}
```
Following a standard layout is one step that can improve how your paper converts to HTML.

### Alt text for images

The popular package [graphicx.sty](https://ctan.org/pkg/graphicx) supports alt text which enhances accessibility by giving screen readers and other assistive technologies a description of the image. The alt style is straightforward to use: 
```
\includegraphics[alt={plain-text description of image}]{example-image-a}
```

Without alt text, images are essentially invisible to screen readers. Additionally, alt text improves discoverability of your content within full-text searches. Dr. Cynthia Bennett has written [this excellent guide](https://dis.acm.org/2023/creating-accessible-figures-and-tables/) to image descriptions and alt text.

## Select macros that describe structures

Use macros according to their meaning, not because of the way they appear visually. Try to steer clear of macros that fine tune placement, font, or other typesetting properties. As an example, to emphasize text use:

```
\emph{key phrase}
```

which will italicize the display and also relay its meaning.  
Don’t use:

```
{\it key phrase}
```

which will italicize only. One conveys meaning, the other is purely visual and assistive technologies will generally ignore it.

Another simple example is if you want your paper’s HTML to have good document navigation for accessibility, an author should use: 

```
\section{Introduction}
```

and avoid LaTeX that doesn’t convey meaning and is purely visual, like:

```
{ \normalfont\fontsize{12}{15}\bfseries Introduction }
```

 It may *visually* convey that it is a section, but it is not meaningfully conveyed in the LaTeX code. The result is it will not be included in your paper’s document navigation.

## Learning LaTeX? 

If you are new to LaTeX, [Overleaf’s tutorials](https://www.overleaf.com/learn) are a great place to start learning how to build your LaTeX documents. To best mimic arXiv’s processing environment, we recommend setting the Overleaf compiler to “stop on errors” mode, and using the most recent version of TeX Live available on their site.
