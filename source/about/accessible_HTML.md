#HTML as an accessible format for papers

Accessibility barriers in research are not new, but they are urgent. The message we have heard from our community is that arXiv can have the most impact in the shortest time by offering HTML papers alongside the existing PDF. Though not easy, accessible research papers is a goal within reach.
{ .intro }

The HTML papers project has launched its beta release providing HTML for nearly all newly submitted papers on arXiv along with a number of older ones. We are gradually backfilling HTML for arXiv's corpus of over 2 million papers over time. Not every paper can be successfully converted, so a small percentage of papers will not have an HTML version. We will work to improve conversion over time.

The link to the HTML format will appear on abstract pages below the existing PDF download link. Authors will have the opportunity to preview their paper’s HTML as a part of the submission process.

The beta rollout is just the beginning. We have a long way to go to improve HTML papers and will continue to solicit feedback from authors, readers, and the entire arXiv community to improve conversions from LaTeX.


## Why "experimental" HTML?

Did you know that 90% of submissions to arXiv are in TeX format, mostly LaTeX? That poses a unique accessibility challenge: to accurately convert from TeX—a very extensible language used in myriad unique ways by authors—to HTML, a language that is much more accessible to screen readers and text-to-speech software, screen magnifiers, and mobile devices. In addition to the technical challenges, the conversion must be both rapid and automated in order to maintain arXiv’s core service of free and fast dissemination.

Because of these challenges we know there will be some conversion and rendering issues. We have decided to launch in beta with “experimental” HTML because:

1. Accessible papers are needed now. We have talked to the arXiv community, especially researchers with accessibility needs, and they overwhelmingly asked us not to wait.
2. We need your help. The obvious work is done. Reports from the community will help us identify issues we can track back to specific LaTeX packages that are not converting correctly.

## Error messages you may see in HTML papers
HTML papers on arXiv.org are a work in progress and will sometimes display errors. As we work to improve accessibility we share with you the causes of these errors and what authors can do to help minimize them. [Learn more about error messages you may see in HTML papers](accessibility_html_error_messages.md)

## Ways to help

### 1) Read HTML papers and report issues
We encourage the community to try out HTML papers in your field:

#### Report an issue
- Go to the abstract page for a paper you are interested in reading.
- Look in the section where you find the link to the PDF download, and click the new link for HTML.
- Report issues by either **a)** clicking on the Open Issue button **b)** selecting text and clicking on the Open Issue for Selection button or **c)** use ```Ctrl+?``` on your keyboard. If you are using a screen reader, use ```Alt+y``` to toggle accessible reporting buttons per paragraph.

**Please do not create reports that the HTML paper doesn't look exactly like the PDF paper**

Our primary goal for this project is to make papers more accessible, so the focus during the beta phase will value function over form. HTML layouts that are incorrect or are illegible are important to report. But we do expect the HTML papers to present differently than the same paper rendered in PDF. Line breaks will occur in different places and there is likely to be more white space. In general, the HTML paper won't present as compactly. Intricate typographic layouts will not be rendered so intricately. This is by design.

HTML is a different medium and brings its own advantages versus PDF. In addition to being much more compatible with assistive technologies, HTML does a far better job adapting to the characteristics of the device you are reading on, including mobile devices.

### 2) Help improve the conversion from LaTeX
If you are an author you can help us improve conversions to HTML by following our guide to [LaTeX Markup Best Practices for Successful HTML Papers](../help/submit_latex_best_practices.md).

If you are a developer and have free development cycles, help us improve conversions! Our collaborators at LaTeXML maintain a [list of issues](https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML) and welcome feedback and developer contributions.

If you are a publisher, member of a society, or conference organizer you can help us improve conversions to HTML by reviewing the .cls files your organization recommends to authors for unsupported packages. Providing .cls files that use supported packages is an easy way to support and sow accessibility in the scientific community. 

## Thank you to our collaborators
First, we want to share a special thank you to all the scientists with disabilities who have generously shared their insights, expertise, and guidance throughout this project.

We want to thank two organizations without which HTML papers on arXiv would not be possible: The [LaTeX Project](https://www.latex-project.org/), and the [LaTeXML](https://math.nist.gov/~BMiller/LaTeXML/) team from NIST. We deeply thank each member of these teams for their knowledge, incredible work, and commitment to accessibility.
