# Submission Guidelines

<span id="guidelines"></span>

While submission to arXiv is free for authors, we do ask authors to carefully prepare their work according to these guidelines. This will improve discoverability of the work and reduce the likelihood of delays before announcement.

Submissions to arXiv should be topical and refereeable scientific contributions that follow accepted standards of scholarly communication.

-   We only accept submissions from [registered authors](../registerhelp.md). If you are a new user or are submitting to a new category, you may be required to find [endorsements](../endorsement.md).
-   All submissions are subject to a [moderation process](../moderation/index.md) that verifies material is appropriate and topical. Material that contains offensive language, non-scientific content, or is plagiarized may be removed.  
-   Authors must grant arXiv.org an [irrevocable license to distribute](../license/index.md) the work.
-   Authors must agree to the [Submittal Agreement](../policies/submission_agreement.md), as well as the [code of conduct](/help/policies/code_of_conduct.html), [moderation](/help/moderation/index.html), and [privacy](/help/policies/privacy_policy.html) policies.
-   Authors are expected to self-submit. Submissions by a third party are only accepted under limited conditions. See instructions for [third-party submissions](../third_party_submission.md) and [index submissions](../submit_index.md) for conference proceedings.
-   New submissions received by 14:00 (Eastern Daylight/Standard Time Zone) are generally made available at 20:00 (Eastern) based on the [schedule for availability](../availability.md). Also see [versions help pages](../versions.md).

## Submission Preparation

-   [Formats for text submission](#formats-for-text-of-submission)
-   [Formats for figures](#figures)
-   [Policies for format requirements](../policies/format_requirements.md)
-   [File names and case sensitivity](#files)
-   [Inclusion of data sets and ancillary files (data, programs, etc.)](#datasets)
-   [Title and abstract preparation](#prep)
-   [Upload and prepare your submission](#upload)
-   [Verify and correct your submission](#correct)
-   [Edit or replace your submission](#replace)

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

<span id="upload"></span>
## Upload and prepare your submission file

To submit an article, select the "START NEW SUBMISSION" button. 

### Submission v1.5 Coming April 2025

The following instructions will guide you through version 1.5 of our submission system when you select “START NEW SUBMISSION v1.5" from your [user page](https://arxiv.org/user).

1. On the **Prepare Files** page click on **Choose File**.
    - Select the file(s) you wish to upload. You can use zip or tar.gz to upload multiple files, uploading source that uses subfolders, and source that includes ancillary files. 
        - Please note: The option to drag files from your computer into the submission window in the browser is not currently available.

    - Click **Upload**.
    - The screen will refresh and will display the files that have been uploaded. 
    - Review your files and delete any files that may not be necessary.
    - Click on the trashcan icon to delete single files.
    - If you would like to start over, click on **Delete All** to delete all the files and start the upload process again.

2. Once you have reviewed your uploaded files, click **Check Files**.
    - Your files will be analyzed  to identify the correct processor, the top level TeX file, and any potential extraneous files for deletion.

3. Notice which compiler was auto detected. 
    - Use the dropdown menu if you would like to select a different compiler.

4. Note which file was auto-detected as the **Top-Level TeX** file.
    - Use the dropdown menu if you would like to select a different file Top-Level TeX file.
    - Only TeX files containing \documentclass directives will be shown on this list. You may choose multiple Top-Level files and the resulting article will contain the TeX output of all the selected files, concatenated together, in order. 

5. Carefully review the Auto-detected Notes for the files.
    - Note which files are recommended for deletion.
        - Uncheck if the file should not be deleted.
        - If at any point you would like to start over with your submission, you may click on the **Return to Upload Step**.

6. **Click Accept and Continue**.
    - A pop up window will prompt you to confirm the files you want to delete.

7. Click **Confirm**.

8. The next page will display if your file compiled successfully and the compilation log. 
    - If your file compiled successfully, you may **Preview your PDF**.
    - Click **Continue** to proceed to the Metadata page. 
    - If your file does not compile successfully and you receive an error, please review your submission for the five most common mistakes made when submitting papers: 
        - Mixed figure file formats. If you are using PDFLaTeX then all figures must be .pdf, .jpg, or .png formats. If your document uses (La)TeX all figures must be .ps or .eps. arXiv does not perform figure file conversion for you, please [ensure your files are converted to the appropriate format](../faq/mistakes.md#mixed) before uploading.
        - File-name [upper/lower-case mismatch](../faq/mistakes.md#case_filenames) between TeX source and figure or included files. arXiv's file system is case sensitive.
        - Default hyperref failures ("Option clash for package hyperref") are not a reason to report a failure to arXiv. Continue scrolling in the log to find the specific errors that are being flagged.
        - Missing customized or differing version of [style files](../faq/mistakes.md#missing_macro).
        - Missing, misnamed, or local complete paths to [figure files](../faq/mistakes.md#abs_filenames). arXiv's file system is case sensitive.

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
