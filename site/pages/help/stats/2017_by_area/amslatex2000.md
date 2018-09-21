AMS LaTeX packages and AMS Journal styles
=========================================

arXiv uses the versions of **AMS-TeX**, **AMS-LaTeX**, and **AMSFonts**
which are current as of October 2002. These are used to process new
submissions and replacements received after the end of September 2002.
If you use older style files you may have to include them with your
submission.

Don't forget to check the PostScript
------------------------------------

As always, carefully check the diagnostic messages sent back to you upon
submission and **verify the PostScript** generated here **before the
paper is released**. Use the paper password sent to you immediately
after a successful submission to access the abstract and PostScript or
PDF for preview.

Submissions prior to October 2002
---------------------------------

The AMS kept releasing new and updated versions of AMS-LaTeX which were
not fully compatible with previous versions, added or removed commands,
changed layout parameters, and came with the same name. Since we needed
to ensure that previously archived papers were not adversely affected by
these updates, we could not simply install the latest version. As a
temporary solution to avoid version mix and dependency issues, we
attached version qualifiers to all AMS LaTeX class and style files
released and updated in 2000 in our TeX installation. These were
selected using the following version-tagged files:

**amsart**2000.cls, **amsbook**2000.cls, **amsbsy**2000.sty,
**amscd**2000.sty, **amsdtx**2000.cls, **amsgen**2000.sty,
**amsldoc**2000.cls, **amsmath**2000.sty, **amsopn**2000.sty,
**amsproc**2000.cls, **amstex**2000.sty, **amstext**2000.sty,
**amsthm**2000.sty, **amsxtra**2000.sty, **upref**2000.sty

For example, a latex document in arXiv from September 2002 may contain:

    \documentclass[...]{amsart2000}
    \RequirePackage[...]{amsmath2000}
    \usepackage[...]{amsthm2000}

We modified the class and style files to use the corresponding versions
of include files so that these dependencies are correctly resolved.
NOTE: the AMSFonts package is not affected by this.
