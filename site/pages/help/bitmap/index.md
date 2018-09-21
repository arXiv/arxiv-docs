Bitmapping Figures
==================

Many graphics and plotting programs do not take into account that people
might want to send their output over the internet instead of to a local
printer. These programs produce output files which can be orders of
magnitude bigger than necessary.

For example, many data-plotting programs use unnecessarily long
PostScript commands when plotting a point or line. If there are large
numbers of data points, then this can add hundreds of kilobytes to the
file size. For figures produced from programs like this, it is more
efficient to use a bitmap to describe the entire image.

**Note:**  
If you have **eps** figures, which have been flagged by the arXiv system
as inefficient, one of the first things you should consider is to use
[`pdflatex`](http://arxiv.org/help/submit_tex#pdflatex) instead of
`latex`.  
`pdflatex` allows to directly include **.jpg**, **.png**, and **.pdf**
figures and frequently these figure formats are the original figure
formats and for technical reasons having to do with image compression
and encoding they are likely a better choice than **.eps**. Also, simple
conversion of **EPS** figures to **PDF** figures often results in
drastic reductions in file size.

The following pages explain how to optimize figures for file size so
that they are easier for your readers to download:

-   [Frequently asked questions (FAQs)](faq)
    -   [What is a reasonable size for figures?](faq#size)
    -   [What are the best formats for image types?](faq#format)
    -   [What about other formats?](faq#other)
    -   [How can readers view JPEG/GIF/PNG images?](faq#view)
-   [Basic bitmapping procedure](procedure)
    -   [ImageMagick](procedure#shortImageM) (most platforms)
    -   [XV](procedure#shortXV) (unix/linux)
    -   [Macintosh](procedure#shortMac)
-   [Advanced bitmapping](advanced)
-   [Possible problems](problems)
-   [Useful software](software)
