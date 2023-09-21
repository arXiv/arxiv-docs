# HTML as an accessible format for papers

Accessibility barriers in research are not new, but they are urgent. The message we have heard from our community is that arXiv can have the most impact in the shortest time by offering HTML papers alongside the existing PDF. Though not easy, accessible research papers is a goal within reach.
{ .intro }

## Latest updates
The HTML papers project has reached a milestone: having completed our targeted public experimental testing phase, *we will be rolling out a beta of HTML papers for all readers later in October.*

The link to the experimental HTML format will appear on all abstract pages below the existing PDF download link. In addition, authors will have the opportunity to preview their paper’s HTML as a part of the submission process.

The beta rollout is just the beginning. We have a long way to go to improve HTML papers and will continue to solicit feedback from authors, readers, and the entire arXiv community to improve conversions from LaTeX.

## Why "experimental" HTML?

Did you know that 90% of submissions to arXiv are in TeX format, mostly LaTeX? That poses a unique accessibility challenge: to accurately convert from TeX—a very extensible language used in myriad unique ways by authors—to HTML, a language that is much more accessible to screen readers and text-to-speech software, screen magnifiers, and mobile devices. In addition to the technical challenges, the conversion must be both rapid and automated in order to maintain arXiv’s core service of free and fast dissemination.

Because of these challenges we know there will be some conversion and rendering issues. We have decided to launch in beta with “experimental” HTML because:

1. Accessible papers are needed now. We have talked to the arXiv community, especially researchers with accessibility needs, and they overwhelmingly asked us not to wait.
2. We need your help. The obvious work is done. Reports from the community will help us identify issues we can track back to specific LaTeX packages that are not converting correctly.

## Ways to help

### Read HTML papers and report issues
Once this feature is live in October we encourage the community to try out HTML papers in your field:
- Go to the abstract page for a paper you are interested in reading.
- Look in the section where you find the link to the PDF download, and click the new link for HTML.
- Report issues by either *a)* clicking on the Open Issue button b) selecting text and clicking on the Open Issue for Selection button or c) use Ctrl+? on your keyboard. If you are using a screen reader, use Alt+y to toggle accessible reporting buttons per paragraph.

**Please do not create reports that the HTML paper doesn't look exactly like the PDF paper**

Our primary goal for this project is to make papers more accessible, so the focus during the beta phase will value function over form. HTML layouts that are incorrect or are illegible are important to report. But we do expect the HTML papers to present differently than the same paper rendered in PDF. Line breaks will occur in different places and there is likely to be more white space. In general, the HTML paper won't present as compactly. Intricate typographic layouts will not be rendered so intricately. This is by design.

HTML is a different medium and brings its own advantages versus PDF. In addition to being much more compatible with assistive technologies, HTML does a far better job adapting to the characteristics of the device you are reading on, including mobile devices.

### Help improve the conversion from LaTeX
- Once a package issue is identified, it still needs to be corrected to improve accessibility
- If you are a developer and have free development cycles, help us improve conversions!
- Our collaborators at LaTeXML maintain a list of issues related to packages that need conversion, and welcome feedback and developer contributions.

## Thank you to our collaborators
First, we want to share a special thank you to all the scientists with disabilities who have generously shared their insights, expertise, and guidance throughout this project.

We want to thank two organizations without which HTML papers on arXiv would not be possible: The [LaTeX Project](https://www.latex-project.org/), and the [LaTeXML](https://math.nist.gov/~BMiller/LaTeXML/) team from NIST. We deeply thank each member of these teams for their knowledge, incredible work, and commitment to accessibility.
