Configuring Your Browser
========================

In order to seamlessly download and view documents from arXiv, you may
have to configure your web browser. It must be told what types of files
to expect and what to do with them when it gets them. In some cases, you
may need to know the [appropriate MIME types delivered by
arXiv](mimetypes.md).

Delivery of Compressed Formats (PostScript, DVI, source)
--------------------------------------------------------

Note that PostScript, DVI, and source files are delivered in gzip
compressed format (a standard compression method). Submissions
consisting of several files are bundled together in a single tar file
**before** being gzipped. Downloaded PS, DVI, and source files must
therefore first be gunzipped, and then possibly untarred. See our
[unpacking notes](unpack.md) for more information.

Depending on how your web browser is configured, it may uncompress the
downloaded file(s) automatically. This may present a problem if the
browser does not then properly rename the formerly gunzipped file. In
these cases, users will complain that the downloaded file will not
gunzip. See [Downloaded .gz Files that are not
Gzipped](faq/browsergunzip) for a explanation of the problem.

<span id="ps"></span>

PostScript
----------

As stated above, arXiv delivers PostScript in gzipped format. We
sometimes receive complaints that the compressed PostScript articles do
not uncompress, or that is, it seems they do not, as the downloaded
files can be viewed unproblematically if first saved to disk. See
[Downloaded .gz Files that are not Gzipped](faq/browsergunzip) for a
explanation of the problem.

There are many standard programs available to view PostScript documents.
**We highly recommend the Ghostscript suite of tools**, which is freely
available at <http://www.cs.wisc.edu/~ghost> for most common operating
systems. After installation, you will want to assign the PostScript MIME
type with the appropriate viewer either via a download wizard (prompts
which program you'd like to associate with this filetype at download
time) or through the appropriate menu option (e.g.,
`Edit->Preferences->Downloads` in Firefox).

<span id="pdf"></span>

PDF
---

The most common programs used to view PDF are:

-   [Adobe's free Acrobat
    Reader](http://www.adobe.com/products/acrobat/readermain.html) (also
    known as "acroread" on Linux/Unix systems), available on most
    platforms
-   Apple's Preview, which comes preinstalled on Mac systems and
    preconfigured in the Safari browser
-   [xpdf](http://www.foolabs.com/xpdf/home.html), an open source viewer
    freely available for Linux/Unix platforms

After installation, you will want to assign the PDF MIME type with the
appropriate viewer either via a download wizard (prompts which program
you'd like to associate with this filetype at download time) or through
the appropriate menu option (e.g., `Edit->Preferences->Downloads` in
Firefox).

<span id="source"></span>

Source
------

The source files for a paper are sent as a single compressed file. For
papers without figures, this file is just the gzipped TeX/LaTeX source
file. If the paper has several parts (e.g., LaTeX plus multiple
figures), they will be bundled together in a single gzipped tar file for
downloading. See our [unpacking notes](unpack.md).

Most Unix/Linux web browsers will uncompress gzipped files but not untar
them. Thus for multi-part files you need to use the **tar** command to
unpack individual TeX and PostScript files from the single file you
download. On Windows and Macintosh you will probably need to both
uncompress and untar, because browsers on these platforms typically will
not uncompress automatically.

<span class="note">Note:</span> You can recognize a tar file by the
binary headers (\^@ characters) at the top of the file, followed by
ordinary text. For info on unpacking tar files, see our [unpacking help
page](unpack.md).
