# Submission Guidelines

<span id="guidelines"></span>

While submission to arXiv is free for authors, we do ask authors to carefully prepare their work according to these guidelines. This will improve discoverability of the work and reduce the likelihood of delays before announcement.

Submissions to arXiv should be topical and refereeable scientific contributions that follow accepted standards of scholarly communication.

-   We only accept submissions from [registered authors](../registerhelp.md). If you are a new user or are submitting to a new category, you may be required to find [endorsements](../endorsement.md).
-   All submissions are subject to a [moderation process](../moderation/index.md) that verifies material is appropriate and topical. Material that contains offensive language, non-scientific content, or is plagiarized may be removed.  
-   Authors must grant arXiv.org an [irrevocable license to distribute](../license/index.md) the work.
-   Authors must agree to the [Submission Terms and Agreement](../policies/submission_agreement.md).
-   Authors are expected to self-submit. Submissions by a third party are only accepted under limited conditions. See instructions for [third-party submissions](../third_party_submission.md) and [index submissions](../submit_index.md) for conference proceedings.
-   New submissions received by 14:00 (Eastern Daylight/Standard Time Zone) are generally made available at 20:00 (Eastern) based on the [schedule for availability](../availability.md). Also see [versions help pages](../versions.md).

## Submission Preparation

-   [Formats for text submission](#text)
-   [Changes  to (La)TeX processing](#newtex)
-   [Formats for figures](#figures)
-   [Policies for format requirements](help/policies/format_requirements.md)
-   [File names and case sensitivity](#files)
-   [Inclusion of data sets and ancillary files (data, programs,
    etc.)](#datasets)
-   [Title and abstract preparation](#prep)
-   [Verify and correct your submission](#correct)
-   [Edit or replace your submission](#replace)


To submit an article, use the [submit form](http://arxiv.org/submit)
    or select "START NEW SUBMISSION" from your [user
    page](http://arxiv.org/user).

<span id="text"></span>

## Formats for text of submission


Accepted submission formats
(in order of preference):

-   [(La)TeX, AMS(La)TeX, PDFLaTeX](../submit_tex.md)
    - [(La)TeX Markup Best Practices for Successful HTML Papers](../submit_latex_best_practices.md)
-   [PDF](../submit_pdf.md)
-   [HTML with JPEG/PNG/GIF images](../submit_index.md)

Our goal is to store articles in formats that are highly portable and
stable over time. Currently, the best choice is TeX/LaTeX.

We do not accept [dvi, PS, or PDF created
from TeX/LaTeX source](../faq/whytex.md), and we
do not accept scanned documents, regardless of format.


<span id="newtex"></span>
## (La)TeX processing changes &mdash; April 2024

We will soon be rolling out changes to how arXiv process (La)TeX submissions. These changes should not be noticable to most of our users. We will be retiring the arXiv-developed "AutoTeX" system that we have used for decades in favor of a simpler, more straight-foward process of converting (La)TeX submissions to PDFs.

 1. The AutoTeX system would try different versions of TeX to see which one successfully builds a PDF. Going forward we will only use the version of TeX currently used by arXiv.
    - Our plan is that arXiv's "current" version closely track the annual TeX Live releases. In the past, we have often gone a few years between TeX updates.
 1. The AutoTeX system would attempt to detect image files that were not referenced in the (La)TeX source for the paper and append those images to the end of the PDF for the paper. Based on recent feedback, we find that most authors are surprised by this behvior, and we will thus be discontinuing this practice. If an author wants images at the end of their paper, just use the normal TeX procedures for this (see https://latex-tutorial.com/tutorials/figures/).
  1. The AutoTeX system would pre-load the LaTeX hyperref package to LaTeX submissions that do not already include it. This package add changes various references to active links in the PDF document (eg, clicking on a reference jumps to the entry in the bibliography section). We will no longer automatically try to add this package. (Note – before you add a \usepackage{hyperref} to your main TeX file, check to see if the template you are using already has a reference by checking the PDF for clickable links; most do).
1. The AutoTeX system would look for any references in a paper that looked like an arXiv paper ID (such as 	arXiv:2402.08954, or 2402.08954), and turn the into a hyperlink to the paper on arXiv. 
We will not do that anymore. Authors should just write out `\href{https://doi.org/10.48550/arXiv.2402.08954}{2402.08954}`. See the [Hyperref documentation for more info](https://mirror.math.princeton.edu/pub/CTAN/macros/latex/contrib/hyperref/doc/hyperref-doc.html).
   - While changes like these arguably made for a better viewing experience, they also made our TeX processing complex and opaque. When we make modifications to user source like this, the paper on arXiv presents differently than the paper on the user's local machine.

1. arXiv presently has about 70 LaTeX packages we supply that papers can use without needing to upload their own copies. But we've found that only 0.65% of recent submissions depend on this. In some cases these packages are woefully out of date
   - We are going to eliminate these packages, and provide only those packages that are distributed with each annual TeX Live release. If you use any packages or style files that are not part of Tex Live, please upload them with your submission
 
At present, the documentation below is still largely accurate, but we are actively re-examining our (La)TeX processing, and there may be more changes in the future. If you have suggestions for changes we should make, please respond to the post about this change on the [arXiv Blog](https://blog.arxiv.org/).

<span id="figures"></span>

## Formats for figures

Accepted figure formats:

-   PostScript (PS, EPS) &mdash; requires [LaTeX processing](../submit_tex.md#latex)
-   JPEG, GIF, PNG or PDF figures &mdash; requires [PDFLaTeX processing](../submit_tex.md#pdflatex)

We do not accept submissions with omitted figures, even if you provide links to view figures externally.

If you submit figures with your (La)TeX source, use standard macro
packages (e.g., the `graphics` and `graphicx` packages) to have
figures appear in the document. arXiv administration
cannot provide help with TeX-related issues.

<span id="files"></span>

## File names and case sensitivity

arXiv will accept only the following characters in file names:

> `a-z A-Z 0-9 _ + - . , = `

File names that contain other characters (e.g., spaces, question marks,
asterisks) will be rejected. These restrictions ensure maximum portability of the stored
files and minimize archival risk.

File names and extensions are also case sensitive on our system. The
file names `Figure1.PDF` and `figure1.pdf` are not the same. Whether
your local system is case sensitive (e.g., Unix) or not (e.g., Windows)
you must ensure that internal file references, such as LaTeX figure
inclusion commands, match case exactly.

<span id="datasets"></span>

## Inclusion of ancillary files

There are limited facilities for including data sets and ancillary files
(data, programs, etc.) that are associated with articles submitted to
arXiv. See [separate instructions](../ancillary_files.md) about including data sets
and ancillary files.

<span id="prep"></span>

## Title and abstract preparation

See [separate instructions for preparing the title and abstract](../prep.md) for inclusion in metadata. This information is used on the
abstract pages, in announcements, in RSS feeds, and to support
searching.

<span id="correct"></span>

## Verify and correct your submission

Before you make the final "Submit Article" step in the submission
process, be sure to carefully check the title and abstract (metadata)
and the processed files, and correct any errors. [Contact arXiv
administrators](../contact.md) for help.

If you discover an error after submission but before public announcement,
select the "Unsubmit" (![unsubmit icon](../../assets/unsubmit.png)) icon
next to the submission on your [user page](http://arxiv.org/user). This will
return it to [incomplete status](../submit_status.md#incomplete) and allow you to
modify your files and resubmit.

Unsubmitting an article takes the article out of the processing queue, and announcement will be scheduled based on the later resubmission time. See the schedule of [availability](../availability.md).

<span id="replace"></span>

## Edit or replace your submission

No additional [versions](../versions.md) are generated when edits are done before the submission is publicly announced.

The date stamp associated with the submission will
be the time that the final "Submit Article" step is completed. Edits and
final submission before 14:00 US Eastern Time (EDT/EST) Monday through
Friday will not delay announcement. You may wish to check [current local
time](http://arXiv.org/localtime).

We encourage authors to update and to make corrections to their
articles. **DO NOT** make a new submission for a corrected article or
for an erratum. Instead, [replace](../replace.md) the original submission.

<span id="availability"></span>

## Availability of submissions

For more information see our [public submission availability page](../availability.md).
