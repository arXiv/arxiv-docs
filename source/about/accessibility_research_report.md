# Accessibility Research Report

<div class="a11y-report" markdown='1'>

## A framework for improving the accessibility of research papers on arXiv.org {.bold-paper-title}

*Shamsi Brinn, Christopher Cameron, David Fielding, Charles Frankston, Alison Fromme, Peter Huang, Mark Nazzaro, Stephanie Orphan, Steinn Sigurdsson, Ryan Tay, Miranda Yang, Qianyu Zhou*
{ .authors }

**Abstract:** The research content hosted by arXiv is not fully accessible to everyone due to disabilities and other barriers. This matters because a significant proportion of people have reading and visual disabilities, it is important to our community that arXiv is as open as possible, and if science is to advance, we need wide and diverse participation. In addition, we have mandates to become accessible, and accessible content benefits everyone. In this paper, we will describe the accessibility problems with research, review current mitigations (and explain why they aren’t sufficient), and share the results of our user research with scientists and accessibility experts. Finally, we will present arXiv’s proposed next step towards more open science: offering HTML alongside existing PDF and TeX formats.
{ .abstract-intro }

## Introduction
Improving access to research is a broad and inclusive effort, championed and moved forward by individuals and organizations around the world. In scientific publishing, arXiv has played an important role in open access for over 30 years by removing financial, institutional, and geographic barriers to research.

Truly open access, though, means more than free and available. When we say that arXiv is open we also must ask: open to whom? Accessibility is the practice of _ensuring access regardless of disability_. It is the next frontier in the open science movement.

## Barriers to access
Barriers to accessing research are broad and can be related to a permanent or temporary disability, or situational factors. Vision impairments and learning disabilities can impede access to written material. If content display is not flexible then using a mobile device can be a barrier. Language barriers or lack of internet access are broadly experienced impediments to accessing research.

Countless people around the globe encounter such barriers. People with disabilities are the world’s largest minority ([United Nations](#11 "United Nations. “Factsheet on Persons with Disabilities.” United Nations, Department of Economic and Social Affairs, https://www.un.org/development/desa/disabilities/resources/factsheet-on-persons-with-disabilities.html. Accessed 28 September 2022.")). More than a quarter of the world’s population has a diagnosed vision impairment ([World Health Organization](#16 "World Health Organization. World Report on Vision. 2019, https://www.who.int/publications-detail-redirect/9789241516570."")), and vision loss is among the top ten disabilities in the United States ([CDC](#3 "Centers for Disease Control and Prevention. “Burden of Vision Loss.” Centers for Disease Control and Prevention, 2020, https://www.cdc.gov/visionhealth/risk/burden.htm."")). For much of the world, including english speaking deaf, written English is not their first language ([Hrastinski and Wilbur](#7 "Hrastinski, Iva, and Ronnie B. Wilbur. “Academic Achievement of Deaf and Hard-of-Hearing Students in an ASL/English Bilingual Program.” Journal of Deaf Studies and Deaf Education, vol. 21, no. 2, 2016. https://www.jstor.org/stable/26172441.")). 20% of people in the United States have dyslexia ([Yale Center for Dyslexia and Creativity](#17 "Yale Center for Dyslexia and Creativity. “Dyslexia FAQ.” Yale Center for Dyslexia, https://dyslexia.yale.edu/dyslexia/dyslexia-faq/.")), and 26% of people in the United States self-report living with at least one disability ([Elavsky et al.](#6 "Elavsky, Frank, et al. “How accessible is my visualization? Evaluating visualization accessibility with Chartability.” Computer Graphics Forum, vol. 41, no. 3, 2022, https://www.frank.computer/chartability/.")). A wide array of temporary and situational impairments (such as bright or low light conditions, or a temporary loss of vision) affect many more who do not have a permanent disability diagnosis.

**“Is there really open and immediate access for everyone, if scholars and students with disabilities cannot access and use research articles?”**([Wentz et al.](#15 "Wentz, Brian, et al. “A Socio-Legal Framework for Improving the Accessibility of Research Articles for People With Disabilities.” Journal of Business & Technology Law, vol. 16, no. 223, 2021. DigitalCommons@UM Carey Law, https://digitalcommons.law.umaryland.edu/cgi/viewcontent.cgi?article=1333&context=jbtl"))

In the United States, 14.5% of K-12 students have a recognized disability ([National Center for Education Statistics](#9 "National Center for Education Statistics. “Children 3 to 21 years old served under Individuals with Disabilities Education Act, Part B, by age group and sex, race/ethnicity, and type of disability: 2020-21.” National Center for Education Statistics, 2021, https://nces.ed.gov/programs/digest/d21/tables/dt21_204.50.asp.")). Ever increasing numbers of high school students are participating in Computer Science curriculums ([Vegas and Fowler](#12 "Vegas, Emiliana, and Brian Fowler. “What do we know about the expansion of K-12 computer science education?” Brookings Institution, 4 August 2020, https://www.brookings.edu/research/what-do-we-know-about-the-expansion-of-k-12-computer-science-education/.")) and other STEM fields, so naturally the percent of students with disabilities in these courses is proportionally increasing as well ([Code.org](#5 "Code.org Advocacy Coalition, et al. “2022 State of Computer Science Education.” Code.org Advocacy Coalition, 2022, https://advocacy.code.org/2022_state_of_cs.pdf.")). These efforts will, over time, lead to more students with disabilities in higher education who will fully expect and demand equal access to the research output in their field.

Furthermore, in the United States there are clear mandates for equivalent access to websites and federally funded research. The need to make research more accessible to all is evident and pressing.

> **“We can only do so much to welcome people, but if they can’t participate fully it's all just nice talk.”**
>
> —Dr. Kimberly Arcand, data visualizer and science communicator

Feedback from arXiv users confirms the barriers to current participation:

**“There are not that many blind mathematicians and scientists because of all the stumbling blocks.”**

**“Most people veer away from STEM subjects towards text subjects because until a lot more content is accessible they need to work really hard to find it.”**

Despite the wealth of data around needs, and a web of regulations mandating equal access, the vast majority of research papers have low levels of accessibility, creating significant barriers for a large number of people.

## Mandates
Access is a critical effort in academia. In the USA, the White House recently released a policy [mandating open access for all federally funded research](https://www.whitehouse.gov/ostp/news-updates/2022/08/25/ostp-issues-guidance-to-make-federally-funded-research-freely-available-without-delay/), while [Plan S](https://www.coalition-s.org/) in Europe aims for no science to be locked behind paywalls. Internationally, we have the [FAIR principles](https://www.go-fair.org/fair-principles/) (of which arXiv is a signatory), and the [UNESCO recommendations on open science](https://en.unesco.org/science-sustainable-future/open-science/recommendation), among others. The movement towards open access is making clear and steady progress.

The movement towards _accessibility_ of research, however, has stalled. Accessibility should be part of every conversation about access. Accessibility is a requirement for most federally funded research in many countries, but in practice only a very low percentage of research papers pass accessibility criteria ([Wang et al.](#13 "Wang, Lucy, et al. “Improving the accessibility of scientific documents.” arXiv, 2021. arxiv.org, https://arxiv.org/pdf/2105.00076.")). And of these, even fewer pass a more careful human review ([Elavsky et al.](#6 "Elavsky, Frank, et al. “How accessible is my visualization? Evaluating visualization accessibility with Chartability.” Computer Graphics Forum, vol. 41, no. 3, 2022, https://www.frank.computer/chartability/.")).

There are formidable obstacles for researchers with disabilities to enter and participate in STEM fields. Foremost among them is equal access to research and data.

> **“The biggest barrier for me is the time you need to spend tracking down formats you can access in order to gain the same information available to everybody else.”**
>
> —Robin Williams, statistician

Existing legal mandates include making websites and federally funded content accessible to all users. Further regulations continue to gain momentum at the Federal level in the USA ([ADA Title III](#14 "“Website Accessibility Regulations On The Horizon: DOJ To Start Title II Rulemaking For State and Local Governments Next Year.” ADA Title III, Seyfarth, 29 July 2022, https://www.adatitleiii.com/2022/07/website-accessibility-regulations-on-the-horizon-doj-to-start-title-ii-rulemaking-for-state-and-local-governments-next-year/.")). Furthermore, educational experts have been hard at work for decades transforming primary education to be more inclusive, which will put pressure on all areas of higher education as more diverse students enter STEM, including on repositories of scientific research like arXiv.

> **“There is work going on earlier in the pipeline, for example making mathematical language accessible to high schoolers. As more people with disabilities enter STEM fields, students will have the expectation of accessing information.”**
>
> —Joe Zesski, Assistant Director, Northeast ADA Center

Most importantly, arXiv has a mandate from our global community to improve access. Scientists need this and the research community is asking for it. One way of meeting these mandates is through well formatted HTML.

HTML is also the foundation of machine readability with major repercussions for the future of scientific discovery. The science that researchers share on arXiv is important, and automated research flows using machine learning are increasingly relied upon for accelerating discovery.([Policy and Global Affairs et al.](#9 "Policy and Global Affairs, et al. Automated Research Workflows for Accelerated Discovery: Closing the Knowledge Discovery Loop. National Academies Press, 2022, https://nap.nationalacademies.org/catalog/26532/automated-research-workflows-for-accelerated-discovery-closing-the-knowledge-discovery. Accessed 14 October 2022.")) Semantic markup and accessibility for assistive technology is a good first step towards ensuring the arXiv repository better supports emerging approaches to conducting science.

arXiv’s long-term mission is simply to serve the needs of the scientific community. Everyone should be able to participate in the wealth of scientific knowledge contributed to arXiv by researchers from all over the world. Accessibility is the next logical step.

> **“Research should be accessible for everyone in the broadest possible way.”**
>
> —Dr. Shiri Azenkot, Associate Professor and Accessibility researcher

## Current state of research accessibility
Scientific research is primarily shared in PDF format, which mimics the printed page. It has been the primary format for decades, so any analysis of the accessibility of research inevitably becomes—in part—an analysis of the PDF format itself.

For authors, PDF offers a reliable visual format for sharing and disseminating their work. For publishers, it offers an archival format that won’t change over time. The accessibility of PDFs can be improved by tagging and adding descriptions.

However, the format has serious limitations that have had a profound impact on the accessibility of research. PDF is not a suitable format for the web and has low native accessibility. PDFs are challenging for people with a variety of reading disabilities, including blindness, low vision, dyslexia, and more. It is time consuming to improve the accessibility of PDFs, and even if this work is done it has no effect on its poor mobile performance.

> **“The best PDF will ever achieve is what HTML delivers. All it can do is catch up.”**
>
> —Dr. Jonathan Godfrey, Senior Lecturer in Statistics

Research from the Allen Institute reports a miserably low accessibility rate for research papers:

**“PDF accessibility adherence is low across all fields of study. Of the five accessibility criteria we assess, only 2.4% of the PDFs we assess demonstrate full compliance.”**([Wang et al.](#13 "Wang, Lucy, et al. “Improving the accessibility of scientific documents.” arXiv, 2021. arxiv.org, https://arxiv.org/pdf/2105.00076."))

Screen readers rely on semantic markup (for example headers, images, formulas, and so on) to correctly interpret content. PDFs do not natively include semantic properties, and it must be tagged with this information after the fact to make it accessible. Tagging is time consuming, takes specialized knowledge, and requires proprietary tools. These tools (and the expertise to use them) are not free, nor are they intuitive. Adobe’s own manual for making PDFs accessible is 94 pages long! ([Elavsky et al.](#6 "Elavsky, Frank, et al. “How accessible is my visualization? Evaluating visualization accessibility with Chartability.” Computer Graphics Forum, vol. 41, no. 3, 2022, https://www.frank.computer/chartability/.")) In addition, if you find you need to regenerate the PDF again for any reason, you must tag the document again from scratch.

It is perhaps not surprising then that efforts to promote tagging PDFs for accessibility have not become the norm in academic publishing.

**“In CHI 2014, a year in which considerable effort was spent giving author’s feedback on the accessibility of their documents, only 26.8% included any document tags at all.”**([Bingham et al.](#2 "Bingham, Jeffrey P., et al. “An Uninteresting Tour Through Why Our Research Papers Aren’t Accessible.” ACM CHI, 2016. http://dx.doi.org/10.1145/2851581.2892588."))

**“The criterion with the lowest rate of compliance is Alt-text, which has remained stable between 5–10% and has been lower in recent years. Since Alt-text is the only criterion of the five which always necessitates author intervention, we believe this is a sign that authors have not become more attuned to accessibility needs.”**([Wang et al.](#13 "Wang, Lucy, et al. “Improving the accessibility of scientific documents.” arXiv, 2021. arxiv.org, https://arxiv.org/pdf/2105.00076."))

Even when this manual work is done the resulting PDF is still only partially accessible: Two column layouts often confuse screen reader software; Text and graphics don’t reflow in mobile devices or with magnification; There is limited parsability for third party tools; And if math and data visualizations did have rich markup in the original source—such as a TeX formula or a SVG graph—the data are often flattened when the PDF is generated.

The typesetting software used to generate PDF results in differing levels of accessibility, with Microsoft Word producing the highest level of compliance, and LaTeX producing the lowest ([Wang et al.](#13 "Wang, Lucy, et al. “Improving the accessibility of scientific documents.” arXiv, 2021. arxiv.org, https://arxiv.org/pdf/2105.00076.")). In the scientific fields that arXiv covers, LaTeX is widely used, and 90% of arXiv’s corpus in recent years was submitted as TeX source. The LaTeX core team is working on generating more accessible PDFs, and we plan to incorporate this work into arXiv when it is released.

On mobile devices, PDFs are far behind standard and don’t meet basic user expectations. Research done by Adobe found that 65% of Americans find consuming content on mobile frustrating; 45% stopped reading or didn’t even try; and 72% say they would work on their mobile devices more if it were easier to read documents ([Adobe](#1 "Adobe. “The case for reimagining reading.” Adobe Blog, 5 December 2018, https://blog.adobe.com/en/fpost/2020/reimagining-reading-infographic.")). Mobile needs in academia vary widely, from a researcher catching up on a paper while traveling, to one with limited access to technology using their mobile phone as their only option for reading papers. Flexible reflow of content is a must to expand access and efficiency.

ACM conference have also found low accessibility rates of PDF, despite significant effort and have chosen HTML5 format as a goal to "ultimately make accessibility easier and more standardized." ([Mankoff, et al.](#8 "Mankoff, Jennifer, et al. “2019 Access SIGCHI report.” ACM SIGACCESS Accessibility and Computing, no. 126, 2020. https://doi.org/10.1145/3386280.3386287."))

> **“You can make PDF accessible, but screen readers are much more efficient when working with HTML. To tag PDF you need specialized skills and tools. For HTML, all these things are comparatively easier.”**
>
> —Avneesh Singh, chair, accessibility task force - W3C EPUB 3 Working Group and Publishing Community Group

PDF is the current standard, but our user research tells us that providing HTML—in addition to PDF and TeX source—will substantially increase accessibility to research posted to arXiv. Well formatted HTML will support and empower the many different ways that scientists consume research data.


### Existing tools
A great deal of work has been done by sung and unsung heroes in the accessibility space, and as arXiv explores our role in making research more accessible we know that we are standing on the shoulders of giants. Critical and transformative work has been achieved in the standardizing and formatting of math on the web; converting TeX to HTML (and PDF, Word and other formats to HTML as well); guiding researchers in writing alternative content for figures and images; making data in charts and graphs parseable by screen readers; translation services (including for Braille); identifying and measuring accessibility on the web; and the incredibly important and advanced work that has gone into screen readers and haptic displays.

We also want to take the opportunity to acknowledge the countless scientists with disabilities who have contributed invaluably to tools, standards, and community understanding over their careers. We have spoken to so many scientists who had to first invent or build the tools they use just to participate in their field. They have paved the way for countless others, as well as for the assistive software in use today. They donate their time to open source tools, guide new scientists in navigating the confusing landscape of access, generously share their expertise (including with arXiv), and endlessly advocate for equal access. All the while overcoming the daily obstacles they face in their own work. Thank you.

To the professors and teachers helping students overcome the formidable barriers built into how we share and publish research, thank you. To the researchers who make their work accessible, thank you.

We can make things easier and more equal for our colleagues. Making research available to everyone regardless of disability is the next stage of Open Science.

### The tool we need
You might ask, with so many tools already built, why do we need anything else? After thorough analysis we found that none of the existing tools, as they are, can provide a smooth experience for authors and readers. Authors should be able to submit their work with the software they currently use and without being an accessibility expert. To achieve that will require new technological solutions as well as cultural changes beyond arXiv, but we have an important role to play.

Our goal is to be able to say to the arXiv community: you bring your expertise in your field; we will help close the gap on all the rest. Thanks to the work of so many in the broad and complex field of accessibility, we believe this is achievable today, though still not easy.

## Researching accessibility in the arXiv ecosystem
We undertook to research the experience of people with a variety of disabilities and other barriers as it relates to accessing research articles, on arXiv and beyond. We also gathered input from experts in different fields: accessibility researchers; writers of web standards for accessibility, Math, and PDF; TeX and LaTeX experts; developers of screen reader and other assistive technologies; scholars of accessibility law; and science communicators.

Our research took two forms, a quantitative survey and a series of qualitative interviews.

### Survey
We developed a survey to investigate behavior and preferences related to accessing content on arXiv.

#### Process
We invited two groups of people to take this survey: researchers who directly rely on assistive technology, and professors who assist their students in accessing the research and data they need.

Out of a pool of 275 volunteers we had a response rate of 18% and received a total of 53 individual responses. Though this number appears small, it is above the industry expected ~6% when taking into account the long length and detail of the survey. The arXiv community again proved its generosity of spirit.

#### Demographics
Our respondents were primarily frequent arXiv users. 58% use arXiv daily and 25% weekly. 25% of respondents directly use assistive technology, while 75% are not direct users, but are involved in assisting people who are.

Respondents represent a variety of fields, with the highest number of respondents—42%—from Physics (includes Astrophysics), followed by Math and CS.

<table>
  <tr>
   <td>Field
   </td>
   <td>Percentage
   </td>
  </tr>
  <tr>
   <td>Physics
   </td>
   <td>31%
   </td>
  </tr>
  <tr>
   <td>Mathematics
   </td>
   <td>21%
   </td>
  </tr>
  <tr>
   <td>Computer Science
   </td>
   <td>13%
   </td>
  </tr>
  <tr>
   <td>Other
   </td>
   <td>13%
   </td>
  </tr>
  <tr>
   <td>Astrophysics
   </td>
   <td>12%
   </td>
  </tr>
  <tr>
   <td>Engineering
   </td>
   <td>6%
   </td>
  </tr>
  <tr>
   <td>Biology
   </td>
   <td>4%
   </td>
  </tr>
</table>

Respondents come from various, but not all, geographic regions. Europe had the highest representation at 44%, followed by Asia at 23%, North America at 21%, South America at 8%, and Africa at 4%. We continue to work towards greater global representation in our surveys.

The assistive technology reported in use by our respondents are:

<table>
  <tr>
   <td>Assistive technology
   </td>
   <td>Percentage
   </td>
  </tr>
  <tr>
   <td>Screen reader
   </td>
   <td>43%
   </td>
  </tr>
  <tr>
   <td>Adjust screen color/contrast
   </td>
   <td>24%
   </td>
  </tr>
  <tr>
   <td>Magnifier
   </td>
   <td>24%
   </td>
  </tr>
  <tr>
   <td>Voice command
   </td>
   <td>10%
   </td>
  </tr>
</table>

#### Survey Results

Access to research output
{ .section-head }

**Summary:** Our respondents heavily depend on access to research, but users of assistive technology report they only have access to 38% of the research they need without assistance. Overall, participants reported that access has improved somewhat over the last five years.
{ .section-summary }

---
Our respondents heavily depend on access to research, with 89% saying that research is completely or somewhat essential to their professional work:

<table>
  <tr>
   <td><em>Data table of respondent’s dependence on accessing research</em>
   </td>
   <td>Yes, use assistive technology
   </td>
   <td>No, don’t use assistive technology
   </td>
  </tr>
  <tr>
   <td>Completely Essential
   </td>
   <td>80%
   </td>
   <td>78%
   </td>
  </tr>
  <tr>
   <td>Somewhat Essential
   </td>
   <td>10%
   </td>
   <td>11%
   </td>
  </tr>
  <tr>
   <td>Somewhat Optional
   </td>
   <td>10%
   </td>
   <td>8%
   </td>
  </tr>
  <tr>
   <td>Completely Optional
   </td>
   <td>0%
   </td>
   <td>2%
   </td>
  </tr>
</table>

We next asked what level of access respondents have today, without requiring assistance from others. Overall the numbers were high: 89% report having access to all or most of the research they need without assistance. However, those numbers look quite different if the respondent uses assistive technology, with only 30% reporting access to all papers without assistance:

<table>
  <tr>
   <td><em>Data table on respondent’s current access to research without assistance</em>
   </td>
   <td>Yes, use assistive technology
   </td>
   <td>No, don’t use assistive technology
   </td>
  </tr>
  <tr>
   <td>All research is accessible
   </td>
   <td>30%
   </td>
   <td>56%
   </td>
  </tr>
  <tr>
   <td>Most research is accessible
   </td>
   <td>40%
   </td>
   <td>38%
   </td>
  </tr>
  <tr>
   <td>About half is accessible
   </td>
   <td>10%
   </td>
   <td>6%
   </td>
  </tr>
  <tr>
   <td>Most is not accessible
   </td>
   <td>20%
   </td>
   <td>
   </td>
  </tr>
</table>

We also asked whether access to research had improved in the last five years, and for the majority of users, including those who use assistive technology, it has improved at least somewhat:

<table>
  <tr>
   <td><em>Data table on improvements in access in the last 5 years</em>
   </td>
   <td>Yes, use assistive technology
   </td>
   <td>No, don’t use assistive technology
   </td>
  </tr>
  <tr>
   <td>It has improved a lot
   </td>
   <td>40%
   </td>
   <td>47%
   </td>
  </tr>
  <tr>
   <td>It has improved a little
   </td>
   <td>20%
   </td>
   <td>24%
   </td>
  </tr>
  <tr>
   <td>It is about the same
   </td>
   <td>30%
   </td>
   <td>26%
   </td>
  </tr>
  <tr>
   <td>It is worse
   </td>
   <td>10%
   </td>
   <td>3%
   </td>
  </tr>
</table>

Barriers to access
{ .section-head }

**Summary:** Survey respondents agree that PDF formatting is the biggest barrier. The main reason reported for not submitting accessible papers is a lack of understanding around requirements.
{ .section-summary }

---

When asked what the biggest barriers were to accessing papers, PDF formatting topped the list:

<table>
  <tr>
   <td><em>Data table on the biggest barriers to access</em>
   </td>
   <td>Yes, use assistive technology
   </td>
   <td>No, don’t use assistive technology
   </td>
  </tr>
  <tr>
   <td>PDF formatting
   </td>
   <td>22%
   </td>
   <td>25%
   </td>
  </tr>
  <tr>
   <td>Images
   </td>
   <td>15%
   </td>
   <td>10%
   </td>
  </tr>
  <tr>
   <td>Math
   </td>
   <td>12%
   </td>
   <td>12%
   </td>
  </tr>
  <tr>
   <td>Graphs and charts
   </td>
   <td>10%
   </td>
   <td>11%
   </td>
  </tr>
  <tr>
   <td>TeX macros
   </td>
   <td>7%
   </td>
   <td>10%
   </td>
  </tr>
  <tr>
   <td>Language
   </td>
   <td>7%
   </td>
   <td>5%
   </td>
  </tr>
  <tr>
   <td>Font size
   </td>
   <td>7%
   </td>
   <td>6%
   </td>
  </tr>
  <tr>
   <td>Colors
   </td>
   <td>7%
   </td>
   <td>2%
   </td>
  </tr>
  <tr>
   <td>Other
   </td>
   <td>5%
   </td>
   <td>4%
   </td>
  </tr>
  <tr>
   <td>Contrast
   </td>
   <td>5%
   </td>
   <td>4%
   </td>
  </tr>
  <tr>
   <td>arxiv.org website
   </td>
   <td>3%
   </td>
   <td>11%
   </td>
  </tr>
</table>

The arxiv.org website is not a significant barrier to users of assistive technology, which our interviews also highlighted for us and is good news. But we do not ignore that the website has barriers unrelated to accessibility (these include limited coverage of related fields and a poor search function), though beyond the scope of this report.

We asked respondents the reasons that stopped them from submitting accessible papers. For users who do not use assistive technology the top reason was not knowing what an accessible paper requires, while for users of assistive technology it was that they consider their papers to be accessible already.

<table>
  <tr>
   <td><em>Data table on reasons users are not submitting accessible papers</em>
   </td>
   <td>Yes, use assistive technology
   </td>
   <td>No, don’t use assistive technology
   </td>
  </tr>
  <tr>
   <td>Their own papers are accessible already
   </td>
   <td>50%
   </td>
   <td>21%
   </td>
  </tr>
  <tr>
   <td>Not knowing what an accessible paper requires
   </td>
   <td>25%
   </td>
   <td>43%
   </td>
  </tr>
  <tr>
   <td>arXiv requires submitting TeX, even if you have created an accessible PDF
   </td>
   <td>25%
   </td>
   <td>25%
   </td>
  </tr>
  <tr>
   <td>Lack of accessibility mandates
   </td>
   <td>25%
   </td>
   <td>11%
   </td>
  </tr>
  <tr>
   <td>Conference or journal guidelines are not accessible
   </td>
   <td>0
   </td>
   <td>11%
   </td>
  </tr>
  <tr>
   <td>Not knowing how to make TeX accessible
   </td>
   <td>0
   </td>
   <td>25%
   </td>
  </tr>
  <tr>
   <td>No access to authoring tools to create accessible content
   </td>
   <td>0
   </td>
   <td>11%
   </td>
  </tr>
</table>

Preferred format
{ .section-head }

**Summary:** Respondents who use assistive technology preferred HTML, while those who didn't preferred PDF. Use of specific types of assistive technology, such as screen magnification and color and contrast remediation, correlated with a strong preference for HTML.
{ .section-summary }

---

We asked survey respondents what their preferred format is for reading papers. Interestingly, the survey responses around format contradict the results from our interviews, where HTML was very strongly indicated as the preferred format for accessibility. We conjecture that this difference in result is due to several factors:

1. Our interview participants include a high percentage of accessibility and standards professionals, while the survey respondents are predominantly researchers who are less familiar with accessibility and the pros and cons of different formats.
2. The dominance of the PDF format in scientific publishing—and its resultant workflows—makes it difficult to imagine alternatives.
3. Many researchers like PDF. Based on user feedback it is clear that new formats for publishing must appear alongside existing options so researchers can interact with papers in their preferred way.

When asked what their preferred format would be**_ if well formatted HTML was available_**, 67% still indicated PDF would be preferred; among assistive technology users a small majority of 55% would prefer HTML:

<table>
  <tr>
   <td><em>Data table on preferred format if HTML was available</em>
   </td>
   <td>Yes, use assistive technology
   </td>
   <td>No, don’t use assistive technology
   </td>
  </tr>
  <tr>
   <td>HTML
   </td>
   <td>55%
   </td>
   <td>29%
   </td>
  </tr>
  <tr>
   <td>PDF
   </td>
   <td>45%
   </td>
   <td>67%
   </td>
  </tr>
  <tr>
   <td>TeX
   </td>
   <td>0%
   </td>
   <td>4%
   </td>
  </tr>
</table>

When respondents were asked which format would be **_most useful_** to them, there was a strong split between those who use assistive technology, and those who do not:

<table>
  <tr>
   <td><em>Data table on useful tools related to format</em>
   </td>
   <td>Yes, use assistive technology
   </td>
   <td>No, don’t use assistive technology
   </td>
  </tr>
  <tr>
   <td>Well formatted HTML
   </td>
   <td>45%
   </td>
   <td>16%
   </td>
  </tr>
  <tr>
   <td>Well formatted PDF
   </td>
   <td>45%
   </td>
   <td>69%
   </td>
  </tr>
</table>


Interestingly, respondents with specific barriers indicated a preference for HTML: those who need to adjust font size, color, or contrast; all barriers which indicate a vision impairment.

Also preferring HTML are professors who help students with translation or by describing images and charts. One professor described in the survey how HTML would help him: _“I translate material into braille for one user, which is highly specialized, but starting from html is much better than pdf.”_

Additional suggestions
{ .section-head }

Respondents were asked to select from a list of potential site improvements which they would find useful. The following two changes had the highest positive response rate:

1. The ability to build a customizable arXiv feed (73%), and
2. A quick way to get to a paper’s conclusions and references (58%).

Other suggestions included:

* Coverage of more scientific fields
* More use of AI and machine learning for categorization and discovery
* The option to enlarge fonts
* Improve TeX upload function
* Add dark mode, and
* To keep arXiv going:

**“I REALLY appreciate the arXiv service. I can't afford to subscribe to a plethora of physics journals. Hats off to the arXiv team!”**

### Interviews
To better understand the ecosystem arXiv is operating in, we interviewed a wide range of researchers from the larger arXiv community.

#### Process
We interviewed a total of 44 individuals. They include researchers with reading disabilities or other access barriers who use arXiv, professors who help students with disabilities, researchers whose focus is on various fields of accessibility, experts on standards for web content, and leaders in LaTeX, MathML, and other languages critical to the success of this project. Some participants fit into more than one category.

Our participants were recruited through our accessibility survey, two accessibility mailing lists, direct invitations, and word of mouth. The mode for interview length was 30 minutes with some going longer.

We conducted semi-structured interviews with individuals or small groups using video conferencing tools, and in two cases in person. An interview guide was developed and used as a loose guiding tool, but we prioritized the participants' conversational lead: we wanted to learn what they most wanted us to know. All participants were interviewed by the main interviewer, assisted by other members of arXiv staff and student assistants.

All personally identifying data relating to interviewees is omitted in this report in order to preserve anonymity.

#### Demographics
Our participants were diverse in terms of their career stage and included PhD students, professors, and researchers working in industry. Participants come from multiple fields of research including physics, math, statistics, computer science, legal, and regulatory. We interviewed a number of participants who serve on various W3C boards related to accessibility and web standards.

Participants were not asked to disclose their disability, but were asked to describe if and how their disability affected their access to research. In responding to this question participants disclosed the following: 7 participants disclosed blindness, 1 participant disclosed dyslexia, 1 participant disclosed ADHD, and 2 participants disclosed a movement disability.

#### Analysis
All interviews were transcribed by either the main interviewer, or by student assistants and then reviewed by the main interviewer. Transcripts were broken down into observations, then documented following Atomic Research principles by mapping each observation to a semantic layer to facilitate discovery.

All observations were anonymized prior to thematic analysis to protect the privacy of our interviewees. During analysis we looked for similarities, grouped them into themes, and asked ourselves ‘what are the opportunities for improvement within this feedback?’. Themes were also compared to data from the survey and analyzed for disparities and correlations.

#### Interview Results

##### User experience journey

An alternate, accessible display of the user journey, as well as the anonymized qualitative data behind it, is available in our [User Journey Table](https://docs.google.com/spreadsheets/u/0/d/1Uvb-A1ePpYyWETxAizVI7ExHobCCSbuLczwxkFN6Ss4/edit).

To evaluate the user journey we sorted feedback into five primary user goals: Find Research, Read Research, Participate in Scholarship, Prepare my Document, and Submit. When analyzing each of these steps we asked: “when it comes to accessing research, was the experience of the participant positive or negative?”

Most steps were dominated by negative experiences, with only Find Research being mostly positive.

![Stacked Bar Chart](../assets/pos-neg-stacked.png){alt='This graphic displays a stacked bar chart for each step of the user journey showing the percent of positive vs. negative experiences. Find research: 38% negative, 62% positive. Read papers: 83% negative, 17% positive. Participate in scholarship: 67% negative, 33% positive. Write papers: 89% negative, 11% positive. Submit papers: 57% negative, 43% positive.'}

*Figure 1. The stacked bar chart shows the percent of positive vs. negative experiences at each step in the user journey.*

*Read Research* elicited the highest number of comments, followed by *Prepare my Document*.

![Positive/Negative bar charts divided by step](../assets/pos-neg.png){alt='This graphic displays each of the five steps as an individual positive/negative bar chart. The number of bars at each step shows the number of experiences, while the height of each bar represent the impact score. Varying numbers of experiences were shared for each step, with Read eliciting the most by far. Find research: 12. Read papers: 57. Participate in scholarship: 17. Write papers: 27. Submit: 14.'}

*Figure 2. Each bar in this positive/negative bar chart represents one experience shared by a participant, while the height of each bar represents it’s impact. It is immediately clear that **Read Papers** elicited the most observations, and most are negative experiences of high impact.*

##### Themes

Our thematic analysis of interview feedback identified 5 themes:

1. The PDF format as a barrier.
2. The benefits of HTML as a format.
3. Skepticism on the potential for real change.
4. arXiv has a role to play in improving the accessibility of research papers.
5. HTML is just the beginning.


Theme 1: researchers who rely on assistive technology point to PDF as the biggest stumbling block to accessible research
{ .section-head }

Participants who rely on assistive technology are particularly aware of—and frustrated with—its shortcomings:

**“Forget PDF!”**

**“I would prefer HTML over PDF.”**

**“You can make a pdf accessible but it is still a PDF (poor mobile use, no magnification).”**

**“PDF is not the best thing from an accessibility point of view.”**

**“[with PDF] I need to borrow someone and say ‘hey can you help me look at this data set.’”**

**“Screen reader does not do equations. Figures are a crapshoot.”**

**“Even accessible PDF, that just means they are tagged. But how do you read math in PDF?”**

**“I have walked away from PDF. Why are you wasting your time and mine?”**

For researchers who _do not_ rely on assistive technology, and for whom PDF already is sufficient, is is challenging to visualize accessing research in new ways that might break their current PDF-dependent workflow:

**“For scientific documents PDF is still excellent, in my opinion. I would not be that interested in HTML papers.”**

**“It is universal, and can keep things quite simple.”**

**“I generally prefer PDF… it’s useful to have it as a single file to add it to Zotero or wherever.”**

Some interviewees who initially dismissed HTML point out its benefits as they thought about it more:

**“I want the PDF so I can add it to Paper Pile… Although, [HTML] would make it easier to quote parts of a paper.”**

Making PDF accessible is challenging:

**“For PDF you need specialized people who understand the PDF standard. For tagging, you need tools from Acrobat and skilled people.”**

Theme 2: HTML mitigates a wide range of access issues, positively addressing many disabilities and improving the experience for most users.
{ .section-head }

HTML has a significant edge for researchers with disabilities.

**“I prefer HTML versions. As an assistive tech user I find it much faster to navigate.”**

**“HTML also works for the deaf community. English is a second language to deaf readers… they would rather get ASL. There are tools for converting HTML to ASL.”**

**“What I hear from colleagues in astronomy who are blind or low vision is that HTML is the preferred delivery mechanism. It is the most accessible.”**

**“HTML gives you a lot more freedom. You can use software to change colors or typefaces.”**

**“I don’t see how an accessible PDF can be better than accessible HTML. I don’t see the upside to it.”**

**“With the HTML version, you can throw MathJax on your website as well, then be able to render that MathML and have it spoken correctly to AT users.”**

**“Screen readers are more efficient while working with HTML.”**

HTML offers benefits beyond disability access, such as for machine learning and mobile phones:

**“The parsability and adaptability of HTML is better than PDF.”**

**“With HTML, [researchers] can adjust the content to their needs. I'm all for HTML.”**

**“The PDF format is not the best suited to mobile phones.”**

**“Reading pdf articles on a smartphone is anyway difficult.”**

**“HTML5 is the right basis for longevity.”**

HTML also offers greater reduction of legal risks. Though not yet specified, the consensus of the legal scholars we spoke to was that legal mandates in the USA for user-uploaded content are inevitable and already underway.

**“Long term, user uploaded content will need to be accessible. But the standards aren't there yet.”**

**“Given how large your scope is it’s good that you are doing this now… you have such a massive volume of material it could be a headache.”**

**“arXiv is covered by the ADA. There is no pass for third-party submitted content.”**


Theme 3: There is deep skepticism, and even a sense of despair, around the likelihood of real change.
{ .section-head }

Researchers with disabilities feel their advocacy has gone unheard:

**“I have waited 20 years for PDF to do anything with accessibility. That is half a working lifetime.”**

**“Progress is not moving anywhere on accessible papers.”**

**“For a long time now accessibility has been viewed as a 'nice to have.' Pushing accessibility up the agenda is the biggest thing that can happen.”**

Making all research accessible is an enormous challenge that extends beyond arXiv:

**“arXiv can’t do it without the involvement of ordinary people.”**

**“Encouraging authors to tag will only be successful if the main players apply the new standards together.”**

**“It's an upward struggle because of how the blind reader space works. Screen readers want users to use their tool and don't provide APIs.”**

**“Even with much bigger technological steps you will still need buy-in from authors to do this.”**

We repeatedly heard we should not let the perfect be the enemy of good. Some improvement in accessibility is much better than no improvement:

**“There is no silver bullet. No point in waiting or looking for one, when you have tools that will do 80% of the work now.”**

**“70% great and another 15% good is not a terrible success rate.”**

**“Even a small stride is a great leap for the people it helps. Don't be discouraged.”**

Participants called out the need for more authoring tools and education if this effort is to succeed:

**“I think one of the biggest problems that we have is the paucity of tools that make it easy to make HTML.”**

**“​​The biggest problems [in making research papers accessible] is communicating the importance of this to authors. I hope awareness will grow over time.”**

**“There needs to be more [accessibility] guidance, especially if you want authors to do some of the work.”**


Theme 4: We heard from our community that arXiv can have a powerful and immediate impact.
{ .section-head }

We are part of an ecosystem, and we have a role to play in making research accessible:

**“arXiv is well set up [to impact accessibility] in a way that a single publisher isn't.”**

**“Your job at arXiv is just to put out proper HTML.”**

**“In a dreamworld every technical document will just work [with screen readers]. In a smaller dream world, it just works on arXiv.”**

**“My area in physics is stuck in its ways. Not many people want to go against the norm. And arXiv sets the norm.”**

Because arXiv has direct control over the submission pipeline, it opens up opportunities:

**“The good news is that the potential for significant impact is just right there. The fact that you are interested in this is very exciting to me. We could shift how we author papers in a way that doesn't add burden but makes life easier. It is a value-add for everyone in authoring and output.”**

**“If someone is in control of the pipeline there is a chance accessibility will get built in.”**

**“There is no polished product you can buy somewhere but all the pieces are coming together. And if we can show the user what they need to do on their end, this could work very beautifully. ArXiv has the content, and you are compiling your own content, and you have the traffic.”**

**“Your push on the pipeline-based tool is the right way because you cannot scale up on it in any other way for it to be automated.”**


Theme 5: HTML is just one step towards a greater vision of accessibility.
{ .section-head }

Research is consumed in different ways. The ultimate goal is flexibility and giving readers the ability to access the content in the way that works best for them:

**“In a perfect world I could be given the source files and reproduce and be in total control of the method I choose to consume.”**

**“I have a right to the information that the author was trying to communicate… There is an ethos in the blind community in [Country] that everyone consumes PDF, so we have the right to consume it as well. I believe I have the right to consume the _content_.”**

**“It really helps when people include the source.”**

**“I have written an add-on that can sonify a series... higher pitch for higher values and so on.”**

**“The ideal is that I get to choose how much information I skip over in the same way a sighted person does.”**

Current accessibility standards are only a starting point:

**“Accessibility has limitations; it is the bare minimum ground in its standards and is too legally driven. But the work of real access, making things work for people with disabilities, requires more.”**

Many interviewees with disabilities pointed out that a paper is just a portal to the knowledge behind it. They don’t necessarily need access to the paper if they can absorb the research itself.

**“Anything like tables are super helpful for me. Source data, or code, is much easier to understand. Then you don’t need to read the paper. If it is well written code then I would prefer that to reading the paper.”**

**“I would prefer if there was raw data available in an excel spreadsheet or similar. Then I can find how to make sense of the data. I would compile the statistics.”**


## arXiv Plan

HTML is an even older and more established standard than PDF. In fact, HTML was invented to facilitate the sharing of scientific knowledge (CERN). It has well defined criteria for achieving accessibility on the web and does not require proprietary tools to author or consume. HTML also provides a better foundation for machine readability, and can help usher in the next generation of tools that will help us all find and access research more efficiently.

Of course, HTML is not automatically accessible. When we refer to HTML in our accessibility plan we mean well-formatted, semantic HTML with necessary ARIA tags. There will be some limitations to what we can do based on the richness of the original uploaded TeX, but our plan is to achieve the most accessible HTML possible within those constraints.

PDF can theoretically be tagged for accessibility, too. But as presented in this paper, the reality is that only about 2.4% of PDFs are accessible and there are significant barriers to improving that number. One promising effort is that the LaTeX core working group are addressing accessibility now, and we plan on incorporating their work as soon as it is available so that we can also provide more accessible PDF documents on arXiv.

Based on provided feedback, we have rated how well we expect *the PDFs that arXiv generates now* will compare to *the well-formatted HTML that our plan will generate* to see how they score on a number of criteria.


### arXiv assessment of HTML and PDF

_Scale: 0 = non-functional, 1 = OK, 2 = good, 3 = excellent._

<table>
  <tr>
   <td>This table is arXiv’s assessment of the performance of HTML vs PDF on a number of criteria.
   </td>
   <td>PDF
   </td>
   <td>Well-formatted HTML
   </td>
  </tr>
  <tr>
   <td>Screen reader legible text
   </td>
   <td>2
   </td>
   <td>3
   </td>
  </tr>
  <tr>
   <td>Screen reader legible math
   </td>
   <td>1
   </td>
   <td>3
   </td>
  </tr>
  <tr>
   <td>Screen reader legible charts
   </td>
   <td>0
   </td>
   <td>0-1
   </td>
  </tr>
  <tr>
   <td>Screen reader legible images
   </td>
   <td>0
   </td>
   <td>0-1
   </td>
  </tr>
  <tr>
   <td>Screen magnifier compatibility
   </td>
   <td>0
   </td>
   <td>3
   </td>
  </tr>
  <tr>
   <td>Colors and contrast adjustment
   </td>
   <td>0
   </td>
   <td>3
   </td>
  </tr>
  <tr>
   <td>Mobile friendly
   </td>
   <td>0
   </td>
   <td>3
   </td>
  </tr>
  <tr>
   <td>Machine readability
   </td>
   <td>1
   </td>
   <td>3
   </td>
  </tr>
  <tr>
   <td>Portability
   </td>
   <td>3
   </td>
   <td>2
   </td>
  </tr>
  <tr>
   <td>Archival nature
   </td>
   <td>3
   </td>
   <td>3
   </td>
  </tr>
  <tr>
   <td>Ability to make accessible
   </td>
   <td>1
   </td>
   <td>2
   </td>
  </tr>
  <tr>
   <td>Established use in academia
   </td>
   <td>3
   </td>
   <td>0
   </td>
  </tr>
  <tr>
   <td>Open source
   </td>
   <td>1
   </td>
   <td>3
   </td>
  </tr>
  <tr>
   <td>Adjustable content*
   </td>
   <td>0
   </td>
   <td>3
   </td>
  </tr>
  <tr>
   <td>Legal risk mitigation
   </td>
   <td>1
   </td>
   <td>3
   </td>
  </tr>
  <tr>
   <td><strong>Total score</strong>
   </td>
   <td><strong>PDF: 16</strong>
   </td>
   <td><strong>HTML: 35</strong>
   </td>
  </tr>
</table>

_*examples: to meet publishers' requests to hide author names while the paper is under double blind review, or promoting best practices by displaying the license the author chose during submission on the work itself._

To offer the flexibility of well formatted HTML downstream requires, ironically, restrictions upstream during content creation. Well-structured, parseable content that follows established standards must be either provided or generated during submission.

And this is the difficulty. 90% of arXiv submissions are provided as TeX (mainly LaTeX), and converting to HTML is not easy due to its extensibility.

> **“On the one hand it's great that LaTeX is so extensible. On the other hand it is such a pain that it is so extensible.”**
>
> —Frank Mittelbach, Head of Development, LaTeX group

Incorporating the conversion into arXiv’s submission process will mean substantial changes to the pipeline behind the scenes, not visible to the author or affecting their submission experience. However we will need to lean on author engagement in two ways: to add alternative text for images and other content that can’t be parsed, and to view and approve their HTML output before submitting, just as they do their PDF output today. arXiv will then make this content available directly on the website alongside the PDF and TeX source.

Because the relationship between authors and the arXiv platform is direct—with no third party typesetting the documents before publishing—we have a tremendous opportunity to make small changes in the submission pipeline that have profound results on accessibility.

> **“arXiv has a closeness to the practitioner that is exciting for accessibility. A lot of remediations require a human touch.”**
>
> —Frank Elavsky, Data Visualization and Accessibility expert

## Conclusions
The level of accessibility of research papers is low, and we cannot claim to have achieved truly open science while those with disabilities are barred from equivalent access. Based on our user research the step our community wants arXiv to take is clear: offer well formatted, accessible HTML alongside existing sources.

Adding HTML will allow all researchers to experience its benefits, try new workflows, and adjust how papers are authored over time. It will support existing and new assistive technologies that work most efficiently with HTML, and normalize the format across more fields.

It is not an easy goal, but it is an achievable one. And because of arXiv’s reach across many fields and control over the submission pipeline we are positioned to leverage HTML in an impactful way.

## References
<div class="a11y-citations" markdown='1'>
<div id="1"></div>
Adobe. “The case for reimagining reading.” _Adobe Blog_, 5 December 2018, [https://blog.adobe.com/en/fpost/2020/reimagining-reading-infographic](https://blog.adobe.com/en/fpost/2020/reimagining-reading-infographic).
<div id="2"></div>
Bingham, Jeffrey P., et al. “An Uninteresting Tour Through Why Our Research Papers Aren’t Accessible.” _ACM CHI_, 2016. [http://dx.doi.org/10.1145/2851581.2892588](http://dx.doi.org/10.1145/2851581.2892588).
<div id="3"></div>
Centers for Disease Control and Prevention. “Burden of Vision Loss.” _Centers for Disease Control and Prevention_, 2020, [https://www.cdc.gov/visionhealth/risk/burden.htm](https://www.cdc.gov/visionhealth/risk/burden.htm).
<div id="4"></div>
CERN. “The birth of the Web.” _CERN_, [https://home.cern/science/computing/birth-web](https://home.cern/science/computing/birth-web).
<div id="5"></div>
Code.org Advocacy Coalition, et al. “2022 State of Computer Science Education.” Code.org Advocacy Coalition, 2022, [https://advocacy.code.org/2022_state_of_cs.pdf](https://advocacy.code.org/2022_state_of_cs.pdf).
<div id="6"></div>
Elavsky, Frank, et al. “How accessible is my visualization? Evaluating visualization accessibility with Chartability.” _Computer Graphics Forum_, vol. 41, no. 3, 2022, [https://www.frank.computer/chartability/](https://www.frank.computer/chartability/).
<div id="6"></div>
Hrastinski, Iva, and Ronnie B. Wilbur. “Academic Achievement of Deaf and Hard-of-Hearing Students in an ASL/English Bilingual Program.” _Journal of Deaf Studies and Deaf Education_, vol. 21, no. 2, 2016. [https://www.jstor.org/stable/26172441](https://www.jstor.org/stable/26172441).
<div id="7"></div>
Mankoff, Jennifer, et al. “2019 Access SIGCHI report.” _ACM SIGACCESS Accessibility and Computing_, no. 126, 2020. [https://doi.org/10.1145/3386280.3386287](https://doi.org/10.1145/3386280.3386287).
<div id="8"></div>
National Center for Education Statistics. “Children 3 to 21 years old served under Individuals with Disabilities Education Act (IDEA), Part B, by age group and sex, race/ethnicity, and type of disability: 2020-21.” _National Center for Education Statistics_, 2021, [https://nces.ed.gov/programs/digest/d21/tables/dt21_204.50.asp](https://nces.ed.gov/programs/digest/d21/tables/dt21_204.50.asp).
<div id="9"></div>
Policy and Global Affairs, et al. Automated Research Workflows for Accelerated Discovery: Closing the Knowledge Discovery Loop. National Academies Press, 2022, [https://nap.nationalacademies.org/catalog/26532/automated-research-workflows-for-accelerated-discovery-closing-the-knowledge-discovery](https://nap.nationalacademies.org/catalog/26532/automated-research-workflows-for-accelerated-discovery-closing-the-knowledge-discovery). Accessed 14 October 2022.
<div id="10"></div>
United Nations. “Factsheet on Persons with Disabilities.” _United Nations_, Department of Economic and Social Affairs, [https://www.un.org/development/desa/disabilities/resources/factsheet-on-persons-with-disabilities.html](https://www.un.org/development/desa/disabilities/resources/factsheet-on-persons-with-disabilities.html). Accessed 28 September 2022.
<div id="11"></div>
Vegas, Emiliana, and Brian Fowler. “What do we know about the expansion of K-12 computer science education?” _Brookings Institution_, 4 August 2020, [https://www.brookings.edu/research/what-do-we-know-about-the-expansion-of-k-12-computer-science-education/](https://www.brookings.edu/research/what-do-we-know-about-the-expansion-of-k-12-computer-science-education/).
<div id="12"></div>
Wang, Lucy, et al. “Improving the accessibility of scientific documents.” _arXiv_, 2021. _arxiv.org_, [https://arxiv.org/pdf/2105.00076](https://arxiv.org/pdf/2105.00076).
<div id="13"></div>
“Website Accessibility Regulations On The Horizon: DOJ To Start Title II Rulemaking For State and Local Governments Next Year.” _ADA Title III_, Seyfarth, 29 July 2022, [https://www.adatitleiii.com/2022/07/website-accessibility-regulations-on-the-horizon-doj-to-start-title-ii-rulemaking-for-state-and-local-governments-next-year/](https://www.adatitleiii.com/2022/07/website-accessibility-regulations-on-the-horizon-doj-to-start-title-ii-rulemaking-for-state-and-local-governments-next-year/).
<div id="14"></div>
Wentz, Brian, et al. “A Socio-Legal Framework for Improving the Accessibility of Research Articles for People With Disabilities.” _Journal of Business & Technology Law_, vol. 16, no. 223, 2021. _DigitalCommons@UM Carey Law_, [https://digitalcommons.law.umaryland.edu/cgi/viewcontent.cgi?article=1333&context=jbtl](https://digitalcommons.law.umaryland.edu/cgi/viewcontent.cgi?article=1333&context=jbtl)
<div id="15"></div>
World Health Organization. _World Report on Vision_. 2019, [https://www.who.int/publications-detail-redirect/9789241516570](https://www.who.int/publications-detail-redirect/9789241516570).
<div id="16"></div>
Yale Center for Dyslexia and Creativity. “Dyslexia FAQ.” _Yale Center for Dyslexia_, [https://dyslexia.yale.edu/dyslexia/dyslexia-faq/](https://dyslexia.yale.edu/dyslexia/dyslexia-faq/).

</div>
</div>
