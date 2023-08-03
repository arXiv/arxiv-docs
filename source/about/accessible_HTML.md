# HTML as an accessible format for papers

The message we have heard from our community is that arXiv can have the most impact in the shortest time by offering HTML alongside the existing PDF and source files. Accessible research papers is a goal within reach!
{ .intro }

## Latest updates
The HTML papers project is in Closed Experimental stage, soon to enter the Public Experimental stage and be shared with the entire community. We will be making links to HTML papers available on abstract pages, list pages, and (at a later phase) as a review step in the submission process.

We know at this experimental stage there will be bugs, so why not wait until it is perfect?

1. First, because our community has asked us not to wait. We heard: "We need HTML now. Do not let perfect be the enemy of good."
2. And second, because we need your help identifying rendering issues. The low hanging fruit is done. Now we need to identify issues we can track back to specific LaTeX packages that are not converting correctly. Reports from the community will help.

Did you know that 90% of submissions to arXiv are in TeX format, mostly LaTeX? That poses a unique accessibility challenge: to accurately convert from TeX, a very extensible language used in myriad unique ways by authors. We invite you to report on the accessibility and accuracy of the HTML by following the simple steps below.

## How to provide feedback

- Go to the abstract page for a paper you are interested in reading.
- Look in the section where you find the link to the PDF download, and click the new link for HTML.
- Either click on the button to open an issue or click **Ctrl+?**, or if you are using a screenreader use **Alt+y** to toggle accessible reporting buttons per paragraph.
- You can also reference a quick glossary of keyboard commands and instructions in the footer of the HTML paper page.

We expect the HTML papers to present differently than the same paper rendered in PDF. Line breaks will occur in different places and there is likely to be more white space. In general, the HTML paper won't present as compactly. Intricate typographic layouts will not be rendered so intricately. This is by design. HTML is a different medium, and brings its own advantages versus PDF -- aside from being much more friendly to screen readers and the like, HTML does a far better job adapting to the characteristics of the device you're reading on -- whether that's your particular monitor geometry or your smartphone. Please do not create reports that the HTML paper doesn't look just like the PDF paper. However, if you HTML layout that's incorrect, or just not very good, please report those.

## Project collaborators
First, we want to share a special thank you to all of the scientists with disabilities who have generously shared their insights, expertise, and guidance throughout this project.

We are working closely with two organizations on this effort: The [LaTeX Project](https://www.latex-project.org/), and the [LaTeXML](https://math.nist.gov/~BMiller/LaTeXML/) team from NIST. We deeply thank each member of these teams for their knowledge, incredible work, and commitment to accessibility.

## Get involved
Conversion to HTML is complicated by the extensibility of LaTeX. Our collaborators at LaTeXML maintain a [https://github.com/brucemiller/LaTeXML/issues](list of issues in github) related to packages that need conversion, and welcome both feedback and developer contributions.
