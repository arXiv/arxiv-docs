# arXivLabs: An invitation to collaborate

![arXiv Labs icon](images/smileybones-labs-icon.png){.mkd-img-thumb align=right alt='a bubbling beaker with a smiling face and crossedbones behind it' role=presentation}

We welcome proposals from the community for arXivLabs integrations. Proposed features must **add value to arXiv content, benefit the scientific community,** and be based on underlying services that are **free of charge** or operate on a freemium model.

<a class="button-reg" href="#arxivlabs-proposal-criteria">Review Proposal Criteria</a>

> ### How does it work ###
> arXiv Labs lets the community contribute new, useful features to arXiv. These integrations are available to readers through a series of tabs at the bottom of the abstract page. 
> <img src="images/arXivLabsFeatures-01.png" width="400" align="left">
> 
> Useful feature include bibliographic info, demos, and links to code. Explore arXiv abstract pages or the [Labs Showcase](showcase.html) to see examples.
> 
> To submit, review our proposal criteria below and then follow the steps at the end of this page. Note that the final decision for approving an arXivLabs project is made by arXiv management and teams.
><p></p>
>

### arXivLabs is not: ###

- A source of research funding.
- The venue for proposing formal collaboration with arXiv.
- A laboratory space for scientific research.
- A place to tell us about your latest scientific breakthrough. 
- Part of the standard arXiv workflow, including submitting a paper and getting endorsed.

If you have questions about collaborating with arXiv on something that is not aligned with arXivLabs, contact us through our [user support portal](https://arxiv-org.atlassian.net/servicedesk/customer/portal/6). If you need information on how to submit a paper to arXiv, please visit our [help pages](/help/submit_index.html). 

## arXivLabs Proposal Criteria

All arXiv-affiliated projects are expected to abide by the [arXiv Community Code of Conduct](/help/policies/code_of_conduct.html). The project must align with the overall arXiv mission and values of openness, community, excellence, and user data privacy. Commercial projects may be considered as long as they provide useful services in a permanently free tier. Except when specifically authorized in writing, the use of the name “arXiv” or “arXiv.org” is prohibited in non-arXiv organization names or projects, [advertising and other promotional vehicles](/brand/brand-guidelines.html).


### Responsibilities

If you propose an arXivLabs project, you must submit the project via pull request (PR) and are responsible for developing and maintaining the Labs component that you have created.

#### Documentation

The project must provide and maintain clear and complete documentation that is available in the same public repository as the project source code. Some examples of what the documentation should include are:
- The technical dependencies of the project.
- A description of any external APIs or data sources the project uses.

#### Ownership Rights and Responsibilities

We encourage all contributors to Labs to continue to update and maintain their code. However, all source code used to integrate a Labs project with arXiv systems will be considered property of arXiv.

#### UI/UX

- Projects with user-facing components must adopt [WCAG 2.1](https://www.w3.org/TR/WCAG21/) Level AA (Web Content Accessibility Guidelines). Higher levels of accessibility (i.e. AAA) are encouraged and welcome.
- Any user-facing or promotional content must clearly indicate that the project is an arXivLabs project.
- As an arXiv-affiliated project, naming, content, and graphical elements must be consistent with the norms of professional conduct, including the arXiv Code of Conduct and [Brand and Style Guide](/brand/index.html).
  - The use of the name “arXiv”, “arXiv.org”, and our logo are protected by copyright and registered trademarks. Use of our name and logo, except to acknowledge arXiv, is prohibited.
  - When Labs projects use arXiv’s name or logo in an unauthorized manner it confuses users and adds to arXiv’s heavy user feedback load.

#### Security & Privacy
- Projects with UI components are reviewed for vulnerabilities that might put users or the arXiv platform itself at risk or leak user information. In cases where vulnerabilities are discovered, Labs partners will be responsible for correcting the issue or risk having their project rejected or terminated.
- The PR must contain all the code that is to be run on the abs page for the project integration. It must not load code from any other source, or for any other purpose.
- Projects must not circumvent or undermine existing security or quality of service measures on the arXiv platform.
- A feedback collection mechanism of some kind for end users is recommended. 

## Submit Your Proposal

The following steps will guide you in submitting an arXivLabs proposal: 

- Submit an arXivLabs proposal in the [Labs support portal](https://arxiv-org.atlassian.net/servicedesk/customer/portal/6).
- Next, [submit your Pull Request (PR) to the arXiv-browse repository](https://github.com/arXiv/arxiv-browse) using GitHub. 
  - Request a review of your PR by selecting arXiv/labs-moderators as your reviewer.
  - Create a fork to your organization, create a branch on the fork, and then create a PR against arXiv’s repository. This is a standard practice for creating a PR to suggest a change to other organizations. Please [consult this documentation](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request-from-a-fork) if you’d like more detailed information. 
- Your PR should only make changes in the labs area. Any changes in other parts of the abstract page will likely result in rejection of the PR.
- If possible, please run the tests in the upstream repository as well as yours. Including test results in the PR is very helpful to understand the nature of change and PR.
- Please see this well-defined [project example](https://github.com/arXiv/arxiv-browse/pull/197) to use as a guide to your PR. 
- Keep in mind, simpler PRs can be reviewed much more quickly than complex PRs.
- PRs are reviewed as resources become available. 
