# arXiv is hiring!

We are looking for a community engagement manager, a few good developers, a program manager, a tech writer/documentation specialist and more.

 - arXiv is part of Cornell University. All arXiv employees are Cornell University employees.
 - The positions listed on this page are all full time [staff positions with benefits (endowed)](https://hr.cornell.edu/understand-your-benefits).
 - Visa sponsorship is not available for these positions.
 - Unless otherwise stated, these are 3-year renewable appointments
 - arXiv is headquartered at the [Cornell Tech campus on Roosevelt Island in New York City](https://tech.cornell.edu/). There is a strong preference for candidates who can report to work at that location, but there are options for hybrid remote work.

We are presently looking for [Software Developers](#software-developers), a [Project Manager](#project-manager), a [Documentation Manager](#documentation-manager), and a [Community Engagement Manager](#community-engagement-manager).

<div style="text-align:center; font-weight:bold; border: 2px solid green; padding-top:6pt; padding-bottom:4pt">

<a href="https://cornell.wd1.myworkdayjobs.com/en-US/CornellCareerPage/?q=arxiv">Click here to view all active arXiv job listings on Cornell's HR site.</a>

</div>

## Software development

We are already underway on the arXiv CE ("Cloud Edition") project. This is a project to re-home all arXiv services from VMs at Cornell to a cloud provider ([Google Cloud](https://cloud.google.com/)). There are a number of reasons for this transition, including improving arXiv's scalability while modernizing our infrastructure. This will not be a simple port of the existing arXiv code base because this project will:

 - replace the portion of our backends still written in perl and PHP
 - re-architect our article processing to be fully asynchronous, and provide better insight into the processing workflows
 - containerize all, or nearly all arXiv services so we can deploy via Kubernetes or services like [Google Cloud Run](https://cloud.google.com/run/)
 - improve our monitoring and logging facilities so we can more quickly identify and manage production issues with arxiv.org
 - create a robust CI/CD pipeline to give us more confidence that changes we deploy will not cause services to regress

The cloud transition is a pre-requisite to modernizing arXiv as a service. The modernization will enable:
 - arXiv to expand the subject areas that we cover
 - improve the metadata we collect and make available for articles, adding fields that the research community has requested such as funder identification
 - deal with the problem of ambiguous author identities
 - improve accessibility to support users with impairments, particularly visual impairments
 - improve usability for the entire arXiv community

### Software Developers

We want to build a team of Software Developers with a range of backgrounds and capabilities. We are particularly interested in people with DevOps and TeX expertise (see below) -- but do not let the lack of such expertise discourage anyone from applying.

We'll be hiring several developers and we don't expect any single developer to be expert in the full range of technologies we'll be using. But we do expect applicants to have a demonstrated record of quickly being able to learn, and be productive in, any environments they may encounter.

 - DevOps &ndash; We want at least one developer to lead the effort of modernizing our devops system so we can efficiently, reliably, and securely deploy new code, using Infrastructure as code principles. This task will likely involve a fair amount of automation via [gitops](https://github.com/readme/featured/defining-gitops). The devops lead will also put in place a robust CI/CD pipeline

 - TeX/LaTeX rationalization &ndash; arXiv accepts the bulk of its content in TeX format. We have TeX or LaTeX source for 90% of our articles. However, compiling all the TeX source we have into viewable papers (in PDF and increasingly also in HTML) can be difficult. We maintain a principle that we can rebuild any TeX submission accepted in the last 32 years. Preserving this capability, while being able to accept submissions that depend on the latest and greatest versions of TeX or LaTeX has become increasingly challenging. It is not unusual for a new release of [TeX Live](https://tug.org/texlive/) to include changes that cause older papers to no longer build properly. We have an opening for a <b>TeX/LaTeX</b> expert to rationalize our TeX pipeline. This task may include getting deeply involved in the TeX community and contributing to projects that support arXiv's goals.

We have three Software Developer listings corresponding to various levels of seniority. We may hire more than one developer each for some of these positions. Below are links to the job postings at Cornell:

 - [Software Engineer III](https://cornell.wd1.myworkdayjobs.com/en-US/CornellCareerPage/?q=arxiv)
 - [Software Engineer IV](https://cornell.wd1.myworkdayjobs.com/en-US/CornellCareerPage/?q=arxiv) (Software Engineer)
 - [Software Engineer V](https://cornell.wd1.myworkdayjobs.com/en-US/CornellCareerPage/?q=arxiv) (Senior Software Engineer)

### Project Manager

We need a Program Manager/Project Manager to organize the arXiv CE effort. This job is modelled on the Program Manager roles found at a lot of modern tech companies like Microsoft and Google. The simple description is the PM does whatever needs to be done &ndash; short of writing code (although that's not out of the question), to support the goals of the project. A secondary description is to take some of the load for managing day to day details away from the Technical Director, so the TD can focus on higher level tasks. Some things the PM might do:

 - Determine the proper ordering of tasks, so prerequisite dependency mesh with the project that need them
 - Manage tickets in JIRA (for both tasks and bug report)
 - Write specs and requirements
 - Solicit user feedback and make sure the project takes it into account

Note &ndash; the PM manages the project, not people. To be successful in this role, the candidate must be capable of exercising influence without authority.

 - [IT Project Manager IV](https://cornell.wd1.myworkdayjobs.com/en-US/CornellCareerPage/?q=arxiv) (Project Manager)

### Documentation Manager

We need someone who can create and organization all of our documentation &ndash; both internal and external.

As we proceed with the arXiv CE effort, we'll need internal documentation of our techniques and processes, the details functions of each module, etc. Bonus points to someone who can document code (mostly Python) just by reading it. Note that we intend for most documentation on the arXiv CE project to be public, where we'll be soliciting feedback on what we are doing. The Tech Writer will be expected to write much of that documentation and moderate the process, and perhaps sometime author responses.

In addition, the Tech Writer will take charge of our public documentation, in order to assist users of arXiv &ndash; the scientists who use our platform individually, as well as institutional partners who need detailed information about our APIs.

1. [IT Tech Writer III](https://cornell.wd1.myworkdayjobs.com/en-US/CornellCareerPage/?q=arxiv) (Documentation Manager)

## Community Engagement Manager

arXiv is looking for a self-starter with an entrepreneurial mindset to join our leadership team as our next Community Engagement Manager. The Community Engagement Manager is responsible for defining and implementing arXiv’s communication strategy and managing and expanding our membership and sponsorship programs.

The Community Engagement Manager will:

 - serve as a creative communications strategist, leveraging emerging communications trends, research, and techniques to connect to key audiences and stakeholders around the globe
 - develop campaigns to support arXiv’s mission, vision, project goals, and brand identity
 - develop, manage, and maintain successful relationships with arXiv stakeholders in academic libraries and library consortia, professional societies, research institutes, and other mission-aligned organizations to ensure a thriving membership and sponsorship program
 - cultivate relationships through in-person meetings, webinars, and other outreach and develop marketing materials
 - organize and implement giving campaigns to solicit support from individual arXiv users

The full job description and instructions on how to apply are [here](https://cornell.wd1.myworkdayjobs.com/en-US/CornellCareerPage/details/Community-Engagement-Manager--arXiv--Cornell-Tech_WDR-00037212)



