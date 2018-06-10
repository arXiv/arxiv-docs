Ancillary files
===============

arXiv is primarily an [archive and distribution service for research
articles](primer.md). There are limited facilities for including ancillary
files of modest size (up to a few MB) with articles. Such ancillary
files might include:

-   Raw data for tables and plots in the article
-   Program code
-   Additional images or movies
-   Workbooks and spreadsheets

arXiv accepts ancillary material only in support of research articles
submitted.

Submission of ancillary files
-----------------------------

Ancillary files are included with an arXiv submission by placing them in
a directory `anc` at the root of the submission package. For example, if
the submission has one TeX file, one image, and C++ program the
submission package might be:
```
    /article.tex
    /figure1.pdf
    /anc/my_program.cpp
```
Ancillary files are stored with a particular version of an article and
thus cannot be changed independently from the article. Different
ancillary files may appear with each version. Please note that ancillary
files are not supported with [PDF submissions](submit_pdf.md) at this
time.

Display and download
--------------------

The abstract pages for articles that include ancillary files will
include additional links below the usual article download links. See,
for example, [arXiv:0811.2625v2](/abs/0811.2625v2). There is also a
separate page that lists all ancillary files with greater detail than
there is room for on the abstract page. See, for example, [ancillary
files for arXiv:0905.2326v1](/src/0905.2326v1/anc). In both cases there
are links to each file for individual download. Ancillary files are also
included in the complete article source that may be downloaded from the
[other formats](/format/0905.2326v1) page.
