# Media types

This page describes the
[standard](https://www.iana.org/assignments/media-types/media-types.xhtml)
and non-standard MIME or [Media
types](https://en.wikipedia.org/wiki/Media_type) used by arXiv for
sending PDF, PostScript, Source (TeX) and DVI files. Web browsers use
the media types of files in order to determine how to handle them, for
example in choosing helper applications.

In the following we list the delivery types and their associated
`Content-Type` headers. Any file types not listed here will use standard
media type headers (e.g. `text/html` for HTML).

PDF (pdf)
---------

PDF is delivered as a plain PDF file (not gzipped) with content type
`application/pdf`, e.g.:

      > curl -# -I http://arxiv.org/pdf/1501.00001v1.pdf | grep Content-Type

      Content-Type: application/pdf

PostScript (ps)
---------------

PostScript is delivered as a gzipped PostScript file with both
`Content-Type` and `Content-Encoding` headers, e.g:

      > curl -# -I http://arxiv.org/ps/adap-org/9708007v1 | grep -p 'Content-[TE]'

      Content-Type: application/postscript
      Content-Encoding: x-gzip

Source files
------------

arXiv supports two different URI patterns for accessing source files,
`/e-print/ID` and `/src/ID`. The `/e-print/ID` form delivers a single
file with the appropriate content type for single-file submission, or a
gzipped tar file for multiple source files (most TeX s ubmissions or
multi-file PS). The `/src/ID` form always delivers a gzipped tar file.

### Multiple source files example

Article [arXiv:hep-lat/9107001](https://arxiv.org/abs/hep-lat/9107001v1) has multiple
file TeX source. Via both the `/e-print/` and `/src/` URIs a gzipped tar
file is supplied.

      > curl -# -I http://arxiv.org/src/hep-lat/9107001v1 | grep -p 'Content-[TE]'

      Content-Encoding: x-gzip
      Content-Type: application/x-eprint-tar

      > curl -# -I http://arxiv.org/e-print/hep-lat/9107001v1 | grep -p 'Content-[TE]'

      Content-Encoding: x-gzip
      Content-Type: application/x-eprint-tar

### Single TeX file example

Article [arXiv:hep-lat/9107002](https://arxiv.org/abs/hep-lat/9107002v1) has a single TeX
file as source. Via the `/e-print/` URI this is supplied directly, via
the `/src/` URI a gzipped tar file is supplied.

      > curl -# -I http://arxiv.org/e-print/hep-lat/9107002v1 | grep -p 'Content-[TE]'

      Content-Encoding: x-gzip
      Content-Type: application/x-eprint

      > curl -# -I http://arxiv.org/src/hep-lat/9107002v1 | grep -p 'Content-[TE]'

      Content-Encoding: x-gzip
      Content-Type: application/x-eprint-tar

DVI (dvi)
---------

Although little used now, arXiv supports access to dvi files from the
"Other Formats" link on the download screen. In the case of a single dvi
file, it is delivered as a gzipped dvi file:

      > curl -# -I http://arxiv.org/dvi/hep-lat/9107002v1 | grep -p 'Content-[TE]'

      Content-Type: application/x-dvi
      Content-Encoding: x-gzip

In the case of multiple files (dvi file + figures), is delivered as a
gzipped tar file:

      > curl -# -I http://arxiv.org/dvi/hep-lat/9107001v1 | grep -p 'Content-[TE]'

      Content-Type: application/x-eprint-tar
      Content-Encoding: x-gzip
