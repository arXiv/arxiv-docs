Downloaded `.gz` Files that are not Gzipped
===========================================

PostScript and source files are always supplied [gzip
compressed](/help/unpack#gunzip).

Most browsers can automatically uncompress these files when they are
downloaded. When they do this, they should also remove the `.gz`
extension, but unfortunately some non-conforming browsers do not. Thus,
you may end up with a saved file that has a `.gz` extension but will not
uncompress (because it is in fact not compressed); in these cases,
you'll receive an error message like:

         gunzip: file.gz: not in gzip format

This is a browser problem, and you will have to work around it. The
simplest thing to do is rename the file by removing the `.gz` extension.
