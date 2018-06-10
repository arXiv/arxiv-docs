Gzipped Files
=============

In order to save network bandwidth and disk space, submissions are
compressed. The archive uses the [GNU](http://www.gnu.ai.mit.edu/)
*gzip* utility, which is free software.

Therefore, you or your system administrator should obtain and install
gzip, and start using it for all your compression needs. See our
[detailed utilities help](utilities.md#taretc) for instructions on
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
