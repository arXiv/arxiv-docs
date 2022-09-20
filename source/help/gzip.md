Gzipped Files
=============

In order to save network bandwidth and disk space, submissions are
compressed. The archive uses the [GNU](https://www.gzip.org/)
*gzip* utility, which is free software.

See our
[detailed utilities help](/help/utilities.md#taretc) for instructions on
obtaining gzip.

Along with gzip you will always find *gunzip*, which decompresses
compressed files; gunzip can uncompress files in several different
compression formats.

Gzipped files usually have a `.gz` extension.

To gzip a file on the Unix command line do the following:

      > gzip filename

This will create a compressed file called `filename.gz` and delete the
original uncompressed version. To uncompress the file, do

      > gunzip filename.gz
