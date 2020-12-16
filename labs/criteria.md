{% macro pendo() %}
<script>
(function(apiKey){
    (function(p,e,n,d,o){var v,w,x,y,z;o=p[d]=p[d]||{};o._q=[];
    v=['initialize','identify','updateOptions','pageLoad','track'];for(w=0,x=v.length;w<x;++w)(function(m){
        o[m]=o[m]||function(){o._q[m===v[0]?'unshift':'push']([m].concat([].slice.call(arguments,0)));};})(v[w]);
        y=e.createElement(n);y.async=!0;y.src='https://content.analytics.arxiv.org/agent/static/'+apiKey+'/pendo.js';
        z=e.getElementsByTagName(n)[0];z.parentNode.insertBefore(y,z);})(window,document,'script','pendo');

        // Call this whenever information about your visitors becomes available
        // Please use Strings, Numbers, or Bools for value types.
        pendo.initialize({
            visitor: {
                id:              'arxiv-labs-user'   // Required if user is logged in
                // email:        // Recommended if using Pendo Feedback, or NPS Email
                // full_name:    // Recommended if using Pendo Feedback
                // role:         // Optional
                // You can add any additional visitor level key-values here,
                // as long as it's not one of the above reserved names.
            },

            account: {
                id:           'ARXIV-LABS' // Highly recommended
                // name:         // Optional
                // is_paying:    // Recommended if using Pendo Feedback
                // monthly_value:// Recommended if using Pendo Feedback
                // planLevel:    // Optional
                // planPrice:    // Optional
                // creationDate: // Optional
                // You can add any additional account level key-values here,
                // as long as it's not one of the above reserved names.
            }
        });
})('d6494389-b427-4103-7c76-03182ecc8e60');
</script>
{% endmacro %}
{{ pendo() }}
# arXivLabs Criteria

## General criteria for all [arXivLabs](https://labs.arxiv.org/) projects:

- All arXiv-affiliated projects are expected to abide by the [arXiv Community Code of Conduct](https://arxiv.org/help/policies/code_of_conduct).
- The project must align with the overall arXiv mission and arXiv values.
- The cost of the project will be carefully considered and weighed against its perceived value related to arXiv’s core mission and development goals. Project costs may be offset with volunteer developers or collaborative grant funding.
- The final decision for approving an arXivLabs project is made by the arXiv management and IT teams.
- Use of the names “arXiv”, “arXiv.org”, “arXiv Labs”, “arXivLabs” and associated logos, web addresses and colors are only allowed with the explicit and written permission and agreement of the arXiv management team.

## **arXivLabs Project Categories**

[Community Projects](#CommunityProjects)

[Platform Projects](#PlatformProjects)

[Core Projects](#CoreProjects)

## **Community Projects**

Community Projects are experimental and developed completely externally from arXiv itself. Community Projects can serve research purposes without any specific objectives to produce user-facing components, but may involve integration with arXiv APIs or other systems. Other Community Projects may have a specific user-facing objective, e.g., rendering arXiv LaTeX sources as HTML, or a mobile application to visualize arXiv articles.
While Community Projects may originate from a variety of internal and external sources, they are differentiated from third-party projects in that an agreement has been reached in advance for specific technical support from the arXiv IT Team, and for permission to use arXiv branding. Agreements will be made for a fixed term, with the possibility of renewal following a review at the end of the term. A cost recovery plan may be required if the project exceeds previously agreed upon support or infrastructure costs. The final decision to grant or revoke branding and support the project as a Community Project is made exclusively by the arXiv management team. arXiv may suspend support for a Community Project at any time, including revoking part or all of a project's access to arXiv APIs, if the project is deemed to violate any applicable terms of use or other agreements, creates an unsustainable and unmitigated burden in terms of time or cost, or if project participants violate the [arXiv Community Code of Conduct](https://arxiv.org/help/policies/code_of_conduct).


### **Responsibilities**

- Project participants are responsible for developing and deploying Labs components themselves.
- The arXiv IT Team provides consultation, and support for accessing required data within the arXiv platform (subject to prior approval).

### **Security and Privacy**

- Except in rare cases, Community Projects will access data in the arXiv system via the API gateway. Access to protected endpoints will be authorized in the same way that we do for any other external API client. The responsible person(s) for the Community Project must agree to the same terms and conditions of use as other users, including any limitations on storage and/or redistribution of data.
- Community Projects must not attempt to circumvent security measures or quality of service measures put in place by the core arXiv IT team.
- In the very rare case that specialized access or data transfer (i.e. outside established APIs) is granted, a data management plan describing how the data will be accessed, stored, protected, and (if necessary) deleted must be provided and approved by the arXiv management team.
- Community Projects should not access any arXiv data that could be used to directly identify arXiv users, such as email addresses, account identifiers, or names. Even anonymized data should be minimal and destroyed as soon as they are no longer useful, and never later than 30 days after the collection.


### **Documentation**

- A basic description of the project and its goals must be made available to the arXiv IT team. For projects requiring minimal/little direct support beyond API access, this need not be more comprehensive than the brief description solicited from any API client. Projects that require more specialized support may entail a commensurate increase in description. We may make project descriptions publicly available, and may edit them.

### **Maintainability**

- Community Projects are encouraged to adopt practices that would facilitate development by others, such as using a public repository such as Github for their code. For projects that are not expected to generate user-facing features deployed on the arXiv site, this is less important. We expect any project that leverages arXiv APIs to make their source code available for unmediated access, and generally observe open source/open science practices. We recommend that one of the following licenses be used with used with Community Projects:
  - MIT License (MIT)
  - Apache License, 2.0 (Apache-2.0)
  - BSD 3-Clause "New" or "Revised" license (BSD-3-Clause)
  - BSD 3-Clause "Simplified" or "FreeBSD" license (BSD-2-Clause)
  - Mozilla Public License 2.0 (MPL-2.0)
  - Creative Commons Zero (CC0)
    Exceptions may be made upon request, as long as the code is offered as open source.


### **UI/UX**

- Community Projects with user-facing components must adopt the basic elements of [WCAG 2.0](https://www.w3.org/TR/WCAG20/) level A from the beginning.
- Any user-facing or promotional content must clearly indicate that the project is an arXiv Community Project.
- As an arXiv-affiliated project, naming, content, and graphical elements must be consistent with the norms of professional conduct, including the [arXiv Community Code of Conduct](https://arxiv.org/help/policies/code_of_conduct) and Brand and Style Guide.

### **Quality**

- Community Projects may be functionally incomplete, and may have numerous bugs. Since Community Projects are not deployed as part of the production arXiv site, the arXiv team assumes no responsibility for tracking or responding to bug reports.

### **Performance/Resources**

- Community Projects that leverage arXiv APIs must follow the terms and conditions of use, which specify allowable request rates and other restrictions.
- The arXiv IT team will work with individuals or projects that require specialized access to arXiv systems, or that require higher request rates via arXiv APIs, to define levels of resource use that are acceptable. If a project requires significant additional resources (including IT team support), cost recovery from the project may be necessary.

## **Platform Projects**

Labs Platform Projects encompass experimental projects that are deployed as part of the production [arXiv.org](https://arxiv.org/) site, most likely in the arXivLabs tabs below the main record page content. Platform Project components have passed quality and security criteria, and have been evaluated/adapted for consistency with the arXiv system architecture. User-facing Platform Project components are visually distinguished from core production components, as all features that live within the arXivLabs tabs are subject to discontinuation or change.

### **Responsibilities**

- Project participants and arXiv IT team partner to establish a development and deployment plan. The relative allocation of development responsibility between the project participants and IT team members will depend on the nature of the component, its maturity, funding considerations, and broader priorities for the arXiv organization.
- Labs components are generally deployed on arXiv's production infrastructure.

### **Additional Platform Project criteria**

- Projects are evaluated for consistency with arXiv policies and procedures. If the project raises new policy questions, those must be identified; such questions must be reviewed by the arXiv management team. In some cases, policy questions may not be fully resolved prior to L4P deployment; in those cases, the issues must be well-understood and provisionally addressed to the satisfaction of the arXiv management team.
- The arXiv operations team must be fully apprised of the planned deployment of an L4P feature; deployment must not proceed without approval from the administrative operations team. It is recommended that Labs projects consult with the arXiv operations team early, to draw on their depth of knowledge and to anticipate any potential problems.
- Projects that interact with external (non-arXiv) APIs must abide by any access policies that are outlined by the platforms that provide them. Dependencies on other platforms must be disclosed.

### **Security & Privacy**

- Projects with UI components are reviewed for vulnerabilities that might put users or the arXiv platform itself at risk, such as cross-site scripting attacks, injection attacks, abuse of cross-origin requests, and denial of service attacks. Any vulnerabilities or concerns surfaced during this review must be addressed to the satisfaction of the arXiv IT team.
- Projects must not circumvent or undermine existing security or quality of service measures on the arXiv.org platform.
- Projects must not introduce new authentication or authorization mechanisms that arXiv does not already support. If a component requires authentication/authorization, it must leverage the existing authnz mechanisms on the arXiv system.
- Except in rare circumstances, projects must not store or transmit personally identifiable information or sensitive personal information. If usage patterns are part of the research or performance goals of the project, this must be understood and approved by the arXiv management team, and data collection must be designed to prevent retention of PII/SPI. For example, client IP addresses must be hashed using a one-way algorithm if usage data collection is approved.

### **Documentation**

- The project must provide and maintain sufficient documentation to make the project comprehensible to the arXiv IT team. Specifically:
  - _What are the technical dependencies of the project?_
  - _Does the project depend on or interact with any external APIs, e.g. data sources?_
  - _Instructions for developing the project, e.g. how to run a development server._
  - _How is the project tested?_
  - _How is the project deployed?_
- Unless there is a good reason not to, project documentation should be made available in the same public repository as the project source code. Rendered documentation may be made available elsewhere.

### **Maintainability**

- Source code and corresponding documentation must be stored in a publicly accessible repository like Github.
- If the project is intended to eventually progress to Core, at this stage the project should adopt frameworks/architectures that are consistent with the arXiv IT team's capabilities.
- Comprehensive metrics (use rates, performance, etc.) will be collected.

### **UI/UX**

- Platform Projects will follow a general arXiv style guide, and all UI components will be reviewed by an arXiv UX specialist. For user-facing components, users will have the option of completely disabling and re-enabling features.
- Projects will initially reside in the arXivLabs tabs on abstract pages, but will be considered for other pages as well.
- Must meet or exceed [WCAG 2.0](https://www.w3.org/TR/WCAG20/) level A or better, passing all automated and manual checks.
- User-facing components must include some iconography that clearly distinguishes it as Platform Project rather than core.
- Text used in user-facing components must be generally consistent in tone, terminology, and style of core arXiv components.

### **Quality**

- Platform Project components are functionally complete, but may have some known bugs. These projects are offered to users "as-is," with no warranty expressed or implied.
- The component must present a coherent and intuitive user interface.

### **Performance/Resources**

- The stability of interactions with outside services and platforms must be evaluated, if relevant.
- The impact on performance from both an end-user perspective and a resource consumption perspective must be evaluated.
  - End user: if the Platform Project is integrated with a core component, it must not degrade the performance (e.g., responsiveness) of that component to outside of acceptable levels as determined by the quality goals for that component.
  - Resource use: if the Platform Project project involves server-side components, resource use (e.g., memory, CPU) will be estimated prior to deployment. If the arXiv IT team determines that resource use is excessive or unusually high, it may be necessary to identify additional funding to recover resource costs.
- The arXiv team reserves the right to discontinue any Platform Project if it results in unmitigated costs or other liabilities.

### **User Feedback**

- A feedback collection mechanism of some kind must be made available to end users. For example, a JIRA feedback collector may be used to collect qualitative feedback.
- Where practicable, a quick-to-use Likert-style or cardinal feedback mechanism should be made available.

### **Note**

- The arXiv IT team may suspend support for a Platform Project at any time, including removing the component from the production platform and suspending access to arXiv APIs, if the project is deemed to violate any applicable terms of use or other agreements, creates an unsustainable and unmitigated burden in terms of time or cost, or if project participants violate the [arXiv Community Code of Conduct](https://arxiv.org/help/policies/code_of_conduct). Platform Project components may also be decommissioned if the original participants are no longer active in the project and the project is not deemed sustainable or sufficiently advantageous to users to justify the cost of maintenance or further development.
- The decision to suspend or decommission a Platform Project from the arXiv production platform will be made at the discretion of the arXiv IT Team lead and/or the Lead System Architect.
- Since Platform Projects are required to make source code available under a permissive open-source license, nothing prevents further development of the codebase itself by external parties.

## **Core Projects**

Core Projects will be considered on a case-by-case basis.
