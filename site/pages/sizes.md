Oversized Submissions
=====================

Problems
--------

The usual reason for submissions to be very large is the presence of a
small number of inefficient figures. These submissions can be made
smaller by making the figures more efficient. We do not accept
submissions with omitted figures, see policy information below.

If you have trouble submitting a *very* long paper, such as a long
review article with many small figures, or a thesis, AND you are sure
that you have efficient figures, then [contact the archive
administrators](/help/contact) to ask for an exception (be sure to quote
the automatic rejection identifier and to explain the large size).

Please think about the time it will take people to download your papers.
arXiv is a resource used throughout the world and many users do have the
fast reliable network connections, fast computers, and printers with
large memory that are common in large universities. Access logs (June
2008) for arXiv show that the median download speed is about 70kB/s,
with 10% of downloads running at \<6kB/s. At 6kB/s a 1MB PDF will take
almost 3 minutes to download.

Making Submissions Smaller
--------------------------

Use of the appropriate tools and image formats for figures is the key to
preparing an efficient submission that will be convenient for people to
download.

Most submissions to arXiv are fine, but some submissions include files
in inefficient and unnecessarily large formats. Most oversized figures
can easily be shrunk by appropriate choice of format or resolution.

Photographic images should usually use JPEG encoding. Diagrams and line
drawings should preferably use a scalable format like PDF or PostScript.
Depending on tools available, conversion to a PNG, GIF or PostScript
bitmap may be an option for smaller filesizes. For a discussion on
shrinking figures, see our [help on bitmapping](bitmap).

All submissions are examined automatically using a number of heuristics.
It is possible that you will receive a notification message asking you
to take a few simple steps to convert your biggest files into more
suitable formats before resubmitting.

Additional Policy Information
-----------------------------

If you include reduced size figures with your submission you are free to
provide links to larger alternative versions of figures stored at your
local site, e.g. at higher resolution, in color, or with special screen
formatting, if desired. Note that readers regularly report their
preference for readily available figures from the archive, even if they
do not provide the highest quality rendering; by examining such a
figure, readers can decide whether or not it is useful for them to
retrieve the highest quality rendering from your local site.

We do not accept submissions with omitted figures. In addition to user
preference noted above, omitting figures greatly reduces the archival
value of your submission. Are you sure that your local web or ftp site
will still be serving the figures from the same URL in 1, 5 or 10 years
time? One only need look at old submissions in the archive to see how
many broken links there are to authors' web sites.

Quickly Reducing File Size
--------------------------

It is possible to quickly reduce the overall file size of your
submission by running a simple `bash` shell command:

         for i in *ps; do ps2pdf -DEPSCrop $i; done;
      

This command will convert all the files matching filenames ending with
`ps` (which will cover both `.eps` as well as `.ps` figures). Please
check the resultant figures carefully, as we are not responsible for any
errors that may occur. However, this mechanism has proven quite
effective for rapidly converting whole directores into PDF files, using
the same file nams.

Note that you may have to update the figure inclusion commands.
