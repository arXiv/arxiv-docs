# Careers at arXiv

 arXiv is part of Cornell Tech, the graduate campus and research center of Cornell University. All arXiv employees are Cornell University employees.

 - Positions at arXiv are [staff positions with benefits (endowed)](https://hr.cornell.edu/understand-your-benefits).
 - Visa sponsorship is not available. You must already possess the legal right to work in the US.
 - arXiv is headquartered at the [Cornell Tech campus on Roosevelt Island in New York City](https://tech.cornell.edu/). When hiring, there is a strong preference for candidates who can report to work at that location, but hybrid and/or remote work may be an option.

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

There are no job openings at this time.
