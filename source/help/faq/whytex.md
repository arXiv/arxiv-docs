# Why Submit the TeX/LaTeX Source?

1. TeX has many advantages that make it ideal as a format for the archives: It is plain text, it is compact, it is freely available for all platforms, it produces extremely high-quality output, and it retains [contextual information](#contextual).
2. It is thus more likely to be a good source from which to generate newer formats, e.g., HTML, MathML, various ePub formats, etc.. Possession of the source thus provides many additional options for future document formats and other uses.
3. Having TeX source allowed us to introduce packages such as `hyperref`, which brought clickable hyperlinks to PDF (and HTML).
4. We recently started creating HTML versions of all papers. This was done primarily to make arXiv's content available to the visually impaired, but it also has benefits for sighted people who might be reading an article from a mobile phone, or other non-traditional devices. We expect continuous improvements in the HTML conversion process and this format to become predominant. It also makes arXiv ready to comply with legal requirements around accessibility.

<span id="contextual"></span>

What is "Contextual" Information, and Why is it Important?
----------------------------------------------------------

We mean by this the relationship between equations and their labels, references and their numbers, subsection headings and their entries in the table of contents, and so on. While ordinarily readily available in TeX/LaTex source, conversion to Postscript irretrievably loses this structural information. The loss is unfortunate because with new formats such as PDF, the information can be used to provide active hyperlinks: e.g., in a PDF viewer you can click on an equation number and jump back to the specified equation. Moreover TeX itself can be processed as HyperTeX and, with the proper dvi previewer, clicking on equation numbers will bring up the desired equation in a separate window, or even retrieve other papers specified by their proper arch-ive/papernum identifier. HyperTeX works by redefining the standard macros and works retroactively for pre-existing TeX/LaTeX source -- HyperTeX conversion is accomplished by merely re-TeXing with the modified macros. Since information is ordinarily lost in each stage of processing, TeX source contains (close to) the maximal amount of contextual information that can be retroactively processed into any future format which can take advantage of it. For more information, see [hypertex help](../../help/hypertex/index.md).


Why doesn't arXiv Accept Preprocessed Submissions?
-------------------------------------------------------------

  *  arXiv cannot easily process pre-processed documents into more accessible formats such as HTML. 
  *  Source files are of higher archival value than converted documents because they can provide a foundation upon which we can develop future services and applications to maintain access and readability of papers indefinitely.
  *  Source files can offer greater insight than just the full text that they extract, such as understanding the techniques the author used to implement specific functions or features in their code, which can offer learning opportunities to the next generation of scientists without having to re-invent macros that may be well written in your code.


Frequent Red Herring Concerns:
------------------------------

*   **Will the auto-TeXing embed figures?**

    Yes. Our TeX installation can do anything that yours can. Any macros you use that we do not support can be included in your submission (or sent to us separately so we can put them on-line).

*   **Won't TeX source make it easy to plagiarize?**

    There is no file format or other technological device that can protect you from this. At the very least, unscrupulous re-typers would always remain a threat. Postscript does not provide a barrier in any event: it is quite simple for someone with a little knowledge to extract any text from a Postscript file. Moreover a plagiarist who cuts-and-pastes directly from your TeX source is all the more easily detected, since the source is easily identified. We archive all versions of papers so that we can assist in any priority or plagiarism disputes.

*   **I worked hard to make my figures and I don't want people to steal them. Shouldn't I hide them by embedding them?**

    As with the above question, it is quite easy for someone with a little knowledge to extract anything they like from the output PDF or Posctript file. Furthermore, unauthorized or un-attributed use of figures counts as plagiarism, just as above, so the rest of the above discussion applies here as well.

<span id="comments"></span>

*   **What if my TeX source has potentially embarrassing self-comments in it?**

    Well... you should probably take them out. It is easy to strip these out in advance of submitting. Here is a Perl filter to do it. Please, please do not hurt yourself with this script; save your file and do not write over the backup copy... just in case.

```perl  
  #!/usr/local/bin/perl  
  while(<STDIN>){ s/^\%.*$/\%/; s/([^\\])\%.*$/\1\%/g; print; }  
  exit(0);  
```

or use the one line command

```bash    
  perl -pe 's/(^|[^\\])%.*/\1%/' < old.tex > new.tex
```

or use this third-party tool, [`arxiv-latex-cleaner`](https://github.com/google-research/arxiv-latex-cleaner)&mdash;which can remove comments, remove auxiliary files, and shrink images. Note that arXiv will provide no user support for this tool, so use with care.

```bash
  arxiv_latex_cleaner /path/to/tex/
```

*   **I use the Textures program. Won't the archive destroy my paper's beautiful formatting?**

    We have many Textures submissions here. Figures will, of course, be placed exactly where you put them (why would you expect otherwise?). Textures does use a non-standard command to control the way figures are included, please read our [notes on submitting Textures generated papers](textures.md).
