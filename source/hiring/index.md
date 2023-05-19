# arXiv is hiring!

We're looking for a community engagement manager, a few good developers, a program manager, a tech writer/documentation specialist and more.

 - arXiv is part of Cornell University. All arXiv employees are Cornell University employees.
 - The positions listed on this page are all full time [staff positions with benefits (endowed)](https://hr.cornell.edu/understand-your-benefits).
 - Visa sponsorship is not available for these positions.
 - arXiv is headquartered at the [Cornell Tech campus on Roosevelt Island in New York City](https://tech.cornell.edu/). There is a strong preference for candidates who can report to work at that location, but there are options for hybrid remote work.

## Community Engagement Manager

To be filled in by @stephanie

## Software development

We're already underway on the arXiv CE ("Cloud Edition") project. This is a project to re-home all arXiv services from VMs at Cornell to a cloud provider ([Google Cloud]https://cloud.google.com/)). There are a number of reasons for this transition, including improving arXiv's scalability while modernizing our infrastructure. This will not be a simple port of the existing arXiv code base because this project will:

 - replace the portion of our backends still written in perl and PHP
 - containerize all, or nearly all arXiv services so we can deploy via Kubernetes or services like [Google Cloud Run](https://cloud.google.com/run/)
 - improve our monitoring and logging facilities so we can more quickly identify and manage production issues with arxiv.org
 - create a robust CI/CD pipeline to give us more confidence that changes we deploy will not cause services to regress

The cloud transition is a pre-requisite to modernizing arXiv as a service. The modernization will enable:
 - arXiv to expand the subject areas that we cover
 - improve the metadata we collect and make available for articles, adding fields that the research community has requested such as funder identification
 - deal with the problem of ambiguous author identiies
 - improve accessibility to support users with impairments, particularly visual impairments

### Software Developers

We want to build a team of Software Developers with a range of backgrounds and capabilities. Particular areas of interest right now are:

 - DevOps &ndash; We want at least one developer to lead the effort of modernizing our devops system so we can efficiently, reliably, and securely deploy new code, using Infrastructure as code principles. This task will likely involve a fair amount of automation via [gitops](https://github.com/readme/featured/defining-gitops). The devops lead will also put in place a robust CI/CD pipeline
 - TeX/LaTeX rationalization &ndash; arXiv accepts the bulk of its content in TeX format. We have TeX or LaTeX source for 90% of our articles. However, compiling all the TeX source we into viewable papers (in PDF and increasingly also in HTML) can be difficult. We maintain a principle that we can rebuild any TeX submission accepted in the last 32 years. Preserving this capability, while being able to accept submissions that depend on the latest and greatest versions of TeX or LaTeX has become increasingly challenging. It is not unusual for a new release of texlive to include changes that cause older papers to no longer build properly. We have an opening for a <b>TeX/LaTeX</b> expert to rationalize our TeX pipeline. This task may include getting deeply involved in the TeX community and contributing to projects that support arXiv's goals.

But if you're simply a software generalist, front-end, back-end, or whatever, that's fine too. As long as you have the requisite background (combination of education and experience <i>and can quickly learn new technologies</i> we encourage you to apply.

We have three Software Developer listings corresponding to various levels of seniority. We may hire two developers each at the IV and V levels. Below are links to the job postings at Cornell:

1. Software Developer III
1. Software Developer IV
1. Software Developer V

### Program Manager

We need a Program Manager/Project Manager to organize the arXiv CE effort. This job is modelled on the Program Manager roles found at a lot of modern tech companies like Microsoft and Google. The simple description is the PM does whatever needs to be done &ndash; short of writing code (although that's not out of the question), to support the goals of the project. A secondary description is to take some of the load for managing day to day details away from the Technial Director, so the TD can focus on higher level tasks. Some things the PM might do:

 - Determine the proper ordering of tasks, so prerequisite dependency mesh with the project that need them
 - Manage tickets in JIRA (for both tasks and bug report)
 - Write specs and requirements
 - Solicit user feedback and make sure the project takes it into account

Note &ndash; the PM manages the project, not people. To be successful in this role, the candidate must be capable of exercising influece without authority.

### Tech Writer/Documentation Person

We need someone who can create and organization all of our documentation &ndash; both internal and external.

As we proceed with the arXiv CE effort, we'll need internal documentation of our techniques and processes, the details functions of each module, etc. Bonus points to someone who can document code (mostly Python) just by reading it. Note that we intend for most documentation on the arXiv CE project to be public, where we'll be soliciting feedback on what we're doing. The Tech Writer will be expected to write much of that documentation and moderate the process, and perhaps sometime author responses.

In addition, the Tech Writer will take charge of our public documentation, in order to assist users of arXiv &ndash; the scientists who use our platform individually, as well as institutional partners who need detailed information about our APIs.

1. IT Tech Writer III




