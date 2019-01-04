arXiv Bulk Data Access - Amazon S3
==================================

This page describes arXiv bulk data available from Amazon S3. See also
[details of other bulk data feeds from arXiv](bulk_data.md). Note that
arXiv's S3 buckets are located in the Eastern US (N. Virginia) region.

*Note: Most articles submitted to arXiv are submitted with the [default
arXiv
license](http://arxiv.org/licenses/nonexclusive-distrib/1.0/license.html),
which grants arXiv a perpetual, non-exclusive license to distribute the
article, but does not assign copyright to arXiv, nor grant arXiv the
right to grant any specific rights to others. We are thus unable to
grant others the right to distribute arXiv articles. If you build
indexes or tools based on the full-text, you must link back to arXiv for
downloads. A small fraction of submissions are made with [other
licenses](license.md) and this information is available in the
OAI-PMH metadata.*

Update 2011-01-03: Source files also available from S3, see
[below](#src).  
Update 2010-08-31: The arXiv PDF dataset has been updated and moved to a
new bucket (`arxiv`). The locations below have been updated.  
Update 2016-09-23: Tools section has been revised to reflect newer
version of `s3cmd`.

Bulk PDF Access
---------------

The complete set of processed arXiv PDF files available from Amazon S3
in requester pays buckets (i.e. the downloader pays Amazon for the
download based on bandwidth used, see [Requester Pays
Buckets](http://docs.amazonwebservices.com/AmazonS3/latest/dev/RequesterPaysBuckets.html)
in the [Amazon S3
Guide](http://docs.amazonwebservices.com/AmazonS3/latest/dev/). Please
consult Amazon's aws S3 pricing page for their current rates for Data
Retrival, available at [Amazon S3
pricing](https://aws.amazon.com/s3/pricing/).) Our use of Amazon
requester pays means that we can open downloads to anyone with
predictable cost, and avoids putting any additional load on our servers
that might impact interactive performance. Note that arXiv's buckets are
located in the Eastern US (N. Virginia) region.

PDFs are available on S3 in the `arxiv` requester pays bucket. They are
grouped into `.tar` files of \~500MB each (which we've found is a good
size chunk). The complete set of PDFs is about 270GB, source files about
190GB, and we make about 40GB of additions/updates each month (2012-02).
Examples keys for these files with the `arxiv` bucket are:

    pdf/arXiv_pdf_1001_001.tar         (s3://arxiv/pdf/arXiv_pdf_1001_001.tar in s3cmd URI style)
    pdf/arXiv_pdf_1001_002.tar         (s3://arxiv/pdf/arXiv_pdf_1001_002.tar)
    pdf/arXiv_pdf_1001_003.tar         (s3://arxiv/pdf/arXiv_pdf_1001_003.tar)

Which are chunks 1, 2 and 3 for month 1001 (2010-01). The complete list
of all chunks if provided in a manifest with some additional information
including dates and checksums. The manifest is:

    pdf/arXiv_pdf_manifest.xml         (s3://arxiv/pdf/arXiv_pdf_manifest.xml)

and has the following format:

    <?xml version='1.0' standalone='yes'?>
    <arXivPDF>
      <file>
        <content_md5sum>1852974c8570cdafd91522ee93719ee5</content_md5sum>
        <filename>pdf/arXiv_pdf_0001_001.tar</filename>
        <first_item>astro-ph0001001</first_item>
        <last_item>hep-th0001208</last_item>
        <md5sum>4b5eeb603fd68bb05b9dd3341e9067fb</md5sum>
        <num_items>1751</num_items>
        <seq_num>1</seq_num>
        <size>526080000</size>
        <timestamp>2009-12-23 14:41:24</timestamp>
        <yymm>0001</yymm>
      </file>
      <file>
        <content_md5sum>650da80f3bcd1f4cd3d994b572ecdbb9</content_md5sum>
        <filename>pdf/arXiv_pdf_0001_002.tar</filename>
        <first_item>hep-th0001209</first_item>
        <last_item>quant-ph0001119</last_item>
        <md5sum>eedc2d7c09cf11fda188d8600c966104</md5sum>
        <num_items>565</num_items>
        <seq_num>2</seq_num>
        <size>139560960</size>
        <timestamp>2009-12-23 14:42:52</timestamp>
        <yymm>0001</yymm>
      </file>
      ...
    </arXivPDF>

where there is one `<file>` for each chunk file. The elements are:

`content_md5sum`
:   MD5 sum of all the files in the tar package concatenated but not
    packaged. Use md5sum for the md5sum of the tar package which should
    match the S3 MD5 sum.

`filename`
:   Name of file within bucket, prefix bucket name `s3://arxiv/` for
    complete identifier

`first_item ` and `last_item`
:   arXiv identifier of article PDF first in tar package, and last in
    tar package

`md5sum`
:   MD5 sum of tar package, can be used as check against downloaded file

`num_items`
:   Number of PDF files in tar package

`seq_num`
:   Sequence number within month `yymm`

`size`
:   Size of tar package in bytes

`timestamp`
:   Timestamp of tar package (unix mtime when created, expressed at
    YYYY-MM-DD HH:MM::SS)

`yymm`
:   Two digit year and month of items in the tar package. Starts with
    9108 for 1991-08, rolls past y2k to 0001 for 2000-01, 1008 for
    2010-08 etc.

<span id="src">Bulk Source File Access</span>
---------------------------------------------

Similar to the processed PDF files, the arXiv source files (mostly
TeX/LaTeX with figures in tar.gz format) available from Amazon S3 in
requester pays buckets.

The source files are available on S3 in the `arxiv` requester pays
bucket using an arrangement similar to the PDF files described above.
They are grouped into `.tar` files of \~500MB each and the complete set
of source files is about 150GB (2011-01). Examples are:

    src/arXiv_src_1001_001.tar         (s3://arxiv/src/arXiv_src_1001_001.tar in s3cmd URI style)
    src/arXiv_src_1001_002.tar         (s3://arxiv/src/arXiv_src_1001_002.tar)
    src/arXiv_src_1001_003.tar         (s3://arxiv/src/arXiv_src_1001_003.tar)

Which are chunks 1, 2 and 3 for month 1001 (2010-01). The complete list
of all chunks if provided in a manifest with some additional information
including dates and checksums. The manifest is:

    src/arXiv_src_manifest.xml         (s3://arxiv/src/arXiv_src_manifest.xml)

See notes above for the format of this manifest which has root element
`arXivSRC`.

Update frequency
----------------

We update both the bulk PDFs and source files to add new content on an
approximately monthly schedule. Updates to existing files are less
frequent. Please [contact arXiv administrators](contact.md) if you
propose to build a service relying upon a particular update schedule.

Tools<span id="tools"></span>
-----------------------------

We do not track development of tools interacting with Amazon S3, nor
endorse any particular tool. However, in development of this facility on
a Linux platform we have found [`s3cmd`](http://s3tools.org/s3cmd)
useful. The example output below was generated with `s3cmd` version
1.6.1.

`s3cmd` will allow you to use a URI-like syntax (e.g. `s3://bucket/key`
to refer to a file called `key` in bucket `bucket`) with list and get
commands as follows. Prior to using `s3cmd`, you will need to go through
several configuration steps which include specifying your AWS access key
and secret key. Note that you will be charged for the requests and
bandwidth when you issue requester pays requests by specifying the
`--requester-pays` flag.

    # s3cmd ls --requester-pays s3://arxiv/pdf 
                           DIR   s3://arxiv/pdf/
    # s3cmd ls --requester-pays s3://arxiv/pdf/\*
    2010-07-29 19:56 526202880   s3://arxiv/pdf/arXiv_pdf_0001_001.tar
    2010-07-29 20:08 138854400   s3://arxiv/pdf/arXiv_pdf_0001_002.tar
    2010-07-29 20:14 525742080   s3://arxiv/pdf/arXiv_pdf_0002_001.tar
    2010-07-29 20:33 156743680   s3://arxiv/pdf/arXiv_pdf_0002_002.tar
    2010-07-29 20:38 525731840   s3://arxiv/pdf/arXiv_pdf_0003_001.tar
    2010-07-29 20:52 187607040   s3://arxiv/pdf/arXiv_pdf_0003_002.tar
    2010-07-29 20:58 525731840   s3://arxiv/pdf/arXiv_pdf_0004_001.tar
    2010-07-29 21:11  44851200   s3://arxiv/pdf/arXiv_pdf_0004_002.tar
    2010-07-29 21:14 526305280   s3://arxiv/pdf/arXiv_pdf_0005_001.tar
    2010-07-29 21:27 234711040   s3://arxiv/pdf/arXiv_pdf_0005_002.tar
    ...
    # s3cmd ls --requester-pays s3://arxiv/pdf/arXiv_pdf_manifest.xml
    2011-02-15 04:12    246144   s3://arxiv/pdf/arXiv_pdf_manifest.xml
    # s3cmd get --requester-pays s3://arxiv/pdf/arXiv_pdf_manifest.xml
    s3://arxiv/pdf/arXiv_pdf_manifest.xml -> ./arXiv_pdf_manifest.xml  [1 of 1]
     246144 of 246144   100% in    0s   377.85 kB/s  done
    #ls -l arXiv_pdf_manifest.xml 
    -rw-r--r-- 1 user   user   246144 Mar 30 13:44 arXiv_pdf_manifest.xml
