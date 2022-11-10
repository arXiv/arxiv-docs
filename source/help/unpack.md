Unpacking Retrieved Papers
==========================

This page explains what to do with the package that you receive if you
select the **Download source** option from the web. In order to save
network bandwidth and disk space, submissions are compressed. arXiv uses
the **gzip** and **tar** utilities. See our [detailed utilities
help](utilities.md#taretc) for instructions on obtaining gzip and tar.

Papers downloaded from the web will be packed in one of two ways:

-   as a gzipped TeX file (for downloads consisting of a single file
    only), or
-   as a gzipped tar file (for downloads consisting of multiple files).

In either case, the first step is to [gunzip](#gunzip) the file (though
this may not be necessary; see below). A tarred file should then be
[untarred](#untar).

If you do not have *tar* or *gunzip* you will have to install them; see
our [utilities help](utilities.md) for information on how to obtain
tar and gzip programs for different platforms.

<span id="gunzip"></span>

Unpacking Gzipped Files
-----------------------

<span class="note">Note:</span> Many browsers will gunzip downloaded
files automatically, so that the instructions in this section can be
ignored. However, a problem may arise if the resulting [file is not
renamed properly](faq/browsergunzip.md) by the web browser.

The utility gunzip, which decompresses files in several different
compression formats, is always made available with gzip. To uncompress
the file using gunzip on a Unix/Linux command line, do:

>     $ gunzip filename.gz

for gzipped single PostScript or TeX files, or

>     $ gunzip filename.tar.gz

for tarred, gzipped multi-file packages. This will create a file named
`filename` in the former case, or `filename.tar` in the latter. The
`filename.gz` file will be deleted.

<span id="untar"></span>

Unpacking a Tarred Package
--------------------------

If you have a `.tar` file at this stage, then you must untar it. On the
Unix command line you do the following:

>     $ tar -xvf filename.tar

The various files contained in the tar file are extracted by this
command. You will see them listed as they are extracted. At this point
you will have one or more TeX files and probably some figure files, and
you will have to run TeX as necessary to produce output that you can
print or view on the screen.

**Note**, you should always make a separate subdirectory for unpacking a
new eprint file. The tarfiles on the archives are "flat", and do not
automatically unpack into separate directories.
