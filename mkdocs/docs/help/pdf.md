Portable Document Format (PDF)
==============================

PDF is Adobe's Portable Document Format. It is closely related to
PostScript, but has built-in support for hyperlinking (for example, in
most of the PDF we generate, when you click on an equation number, the
page with the equation will be displayed). We generate PDF for all
papers submitted as TeX source or PostScript. On the other hand, papers
submitted in PDF are available only in PDF.

You can choose to make PDF your default format for downloading and
viewing papers by [setting a cookie](https://arxiv.org/cookies) in your browser.

Recommended Viewing Software
----------------------------

### Adobe's Acrobat Reader (Acroread)

Versions of Adobe's Acrobat Reader ("acroread" on Linux/Unix systems)
less than 6 were plagued with several problems, such as missing minus
signs and parentheses in PDF display and printout. **We therefore highly
recommend that you [download and install the current
version](http://www.adobe.com/).**

<span id="plugin"></span>

**Do not install Acroread as a plug-in**. Bugs in this arrangement mean
that the browser will sometimes generate multiple rapid-fire requests,
which may trigger one of our [robot-tripwires](/help/robots.md) and
block your access. Please download all PDFs to your local machine and
open them with the full Adobe Acrobat Reader application.

Xpdf
----

[Xpdf](http://www.foolabs.com/xpdf/) is an open source viewer for PDF
files. The Xpdf project also includes a PDF text extractor,
PDF-to-PostScript converter, and various other utilities.

This viewer will only display rotated fonts if using `t1lib`, or if your
X server is capable (most are not). If fonts can't be rotated, the paper
identifier printed at the left side of the page is displayed strangely,
but otherwise most papers will be fine.
