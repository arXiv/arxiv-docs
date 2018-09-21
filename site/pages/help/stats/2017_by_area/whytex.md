Why Submit the TeX/LaTeX Source?
================================

1.  TeX has many advantages that make it ideal as a format for the
    archives: It is plain text, it is compact, it is freely available
    for all platforms, it produces extremely high-quality output, and it
    retains [contextual information](#contextual).  
    It is thus more likely to be a good source from which to generate
    newer formats, e.g., MathML \[namely HTML, or more specifically XML,
    that handles mathematics correctly -- note that the MathML people
    plan a LaTeX to MathML translator, but dvi/ps/pdf lack the necessary
    document structuring concepts\]. Possession of the source thus
    provides many additional options for future document migrations.
2.  Using emerging new technology, most of the Postscript generated from
    the source contains [hyperlinks](/hypertex/), so that using new
    versions of PostScript previewers (e.g., the next version of
    Ghostscript/Ghostview), readers can point-and-click to navigate
    within the paper, and even over the web itself.  
    And by archiving the source, we maximize the potential for seamless
    adoption of future technological improvements. Archived papers can
    be repeatedly rejuvenated by automated reprocessing.
3.  We distill the source into Adobe's PDF format. The hyperlinks can
    then be [viewed using Acroread or an equivalent reader](/help/pdf).
    In addition, this means that the hyperlink overlay will be directly
    available to those web browsers with built-in PDF support (thus
    combining the network transport capabilities of html with a more
    serious page markup language). Having the paper available in PDF
    means that problems discussed below with Mac and PC browsers can be
    avoided.
4.  There is no single Postscript standard! We provide Postscript in
    many formats; this is not possible if the author submits a single
    Postscript file. For a historical example, Preview.app under
    NeXTstep displayed bitmapped fonts poorly, and for historical
    reasons (TeX predated common use of Postscript) these fonts are
    still most commonly used by TeX and dvips. By requesting type 1
    fonts from the "More options" page, screen readability is improved.
5.  Cross-referencing within arXiv is added automatically with
    hyperlinked Postscript. Authors should specify
    [**arXiv:YYMM.NNNNN**](/help/arxiv_identifier) or the older format
    of **arch-ive/papernum** (e.g., hep-ph/9503456) references whenever
    available, and these strings will be pattern-matched and replaced
    with suitable hyperlinks back to arXiv. Similarly, any occurrences
    of **http://...** or **ftp://...** url's are detected and converted
    to hyperlinks.

------------------------------------------------------------------------

<span id="contextual"></span>

What is "Contextual" Information, and Why is it Important?
----------------------------------------------------------

We mean by this the relationship between equations and their labels,
references and their numbers, subsection headings and their entries in
the table of contents, and so on. While ordinarily readily available in
TeX/LaTex source, conversion to Postscript irretrievably loses this
structural information. The loss is unfortunate because with new formats
such as PDF, the information can be used to provide active hyperlinks:
e.g., in a PDF viewer you can click on an equation number and jump back
to the specified equation. Moreover TeX itself can be processed as
HyperTeX and, with the proper dvi previewer, clicking on equation
numbers will bring up the desired equation in a separate window, or even
retrieve other papers specified by their proper arch-ive/papernum
identifier. HyperTeX works by redefining the standard macros and works
retroactively for pre-existing TeX/LaTeX source -- HyperTeX conversion
is accomplished by merely re-TeXing with the modified macros. Since
information is ordinarily lost in each stage of processing, TeX source
contains (close to) the maximal amount of contextual information that
can be retroactively processed into any future format which can take
advantage of it. For more information, see
[https://arxiv.org/hypertex/](/hypertex/).

------------------------------------------------------------------------

Why doesn't arXiv Accept Preprocessed Postscript Submissions?
-------------------------------------------------------------

1.  Postscript from TeX usually contains bitmapped fonts at a fixed
    resolution. Your favorite resolution is inappropriate for other
    users and may make your paper difficult or impossible to read. We
    will make available many versions of the Postscript including 300
    dpi, 400 dpi, or 600 dpi bitmapped fonts, as well as Postscript with
    (un-embedded) Type 1 fonts.
2.  Different dvi to PS drivers produce Postscript that ranges from
    completely non-compliant with Adobe's Document Structuring Comments
    to only marginally compliant. We will always have the latest dvi to
    PS software installed and will produce DSC compliant PS.
3.  Postscript loses contextual information that is implicit in the TeX.
    This information is required to provide hyperlinked overlays to
    papers (so that users with the proper viewers can, for example,
    click on a reference number and jump to the reference \[which can
    also include a web URL which can be automatically passed off to a
    web browser\]). To do the hyperlinking, we use HyperTeX macros. The
    Postscript we produce is HyperPostscript which can be distilled into
    Adobe's Portable Document Format (PDF). Our software makes web URL's
    out of all references of the form YYMM.NNNNN or arch-ive/yymmnnn
    (e.g., 1510.00322 will be converted to a hyperlink for
    https://arxiv.org/abs/1510.00322, hep-th/9511053 will be converted
    to a hyperlink for https://arxiv.org/abs/hep-th/9511053).
4.  TeX source is more compact and space-efficient.

------------------------------------------------------------------------

Frequent Red Herring Concerns:
------------------------------

-   **Will the auto-TeXing embed figures?**

    Yes. Our TeX installation can do anything that yours can. Any macros
    you use that we do not support can be included in your submission
    (or sent to us separately so we can put them on-line).

-   **Won't TeX source make it easy to plagiarize?**

    There is no file format or other technological device that can
    protect you from this. At the very least, unscrupulous re-typers
    would always remain a threat. Postscript does not provide a barrier
    in any event: it is quite simple for someone with a little knowledge
    to extract any text from a Postscript file. Moreover a plagiarist
    who cuts-and-pastes directly from your TeX source is all the more
    easily detected, since the source is easily identified. We archive
    all versions of papers so that we can assist in any priority or
    plagiarism disputes.

-   **I worked hard to make my figures and I don't want people to steal
    them. Shouldn't I hide them by embedding them?**

    As with the above question, it is quite easy for someone with a
    little knowledge to extract anything they like from the output PDF
    or Posctript file. Furthermore, unauthorized or un-attributed use of
    figures counts as plagiarism, just as above, so the rest of the
    above discussion applies here as well.

-   **What if my TeX source has potentially embarrassing self-comments
    in it?**

    Well... you should probably take them out. It is easy to strip these
    out in advance of submitting. Here is a Perl filter to do it.
    Please, please do not hurt yourself with this script; save your file
    and do not write over the backup copy... just in case.

    > ` #!/usr/local/bin/perl while(<STDIN>){ s/^\%.*$/\%/; s/([^\\])\%.*$/\1\%/g; print; } exit(0);`

    or use the one line command

    > ` perl -pe 's/(^|[^\\])%.*/\1%/' < old.tex > new.tex`

-   **I use the Textures program. Won't the archive destroy my paper's
    beautiful formatting?**

    We have many Textures submissions here. Figures will, of course, be
    placed exactly where you put them (why would you expect otherwise?).
    Textures does use a non-standard command to control the way figures
    are included, please read our [notes on submitting Textures
    generated papers](textures).
