# Nota Bene (updated 30 Jun '97) 

Frequent complaint regarding multipart files:

> "when i retrieve them, the files gain a lot of junk at the beginning
> and end (things like ^@ all over)"

**Source links** point to compressed (gzipped) files. For papers without
figures, this file is just the gzipped text. If the paper has several
parts, e.g. TeX + multiple figures, they will be bundled together in a
single gzipped tar file for downloading.

You can recognize a tar file by the binary headers (^@ characters) at
the top of the file, followed by ordinary text. For info on unpacking
tar files, see our [unpacking help page](/help/unpack.md).

Most unix web browsers will uncompress gzipped files but not untar them.
Thus for multi-part files you need to use the **tar** command to unpack
individual TeX and PostScript files from the single file you download.
On Windows and Macintosh you will need to uncompress and untar (because
Windows and Macintosh browsers do not uncompress automatically).

**Postscript links** are sent out as compressed (gzipped) postscript
files, and your browser [needs to be configured to handle
this](/help/config_browser.md).

Further information can be found in our *[Frequently Asked
Questions](/help/faq/index.md)* pages.
