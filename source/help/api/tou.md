# Terms of Use for arXiv APIs

Our mission is to provide rapid dissemination of scientific results at no cost
to authors or readers. Providing free Application Programming Interfaces (APIs)
helps us to advance that mission by enabling platforms and projects that extend
the discoverability of arXiv e-prints and provide valuable services to
scientists and interested readers. Our APIs include our [OAI-PMH
interface](../../help/oa/index.md), [RSS feeds](../../help/rss.md), the [legacy arXiv API](index.md), [bulk
data downloads](../../help/bulk_data_s3.md), and [SWORD bulk deposit API](../../help/submit_sword.md).
Understanding and observing the following terms of use will help us to ensure
that arXiv continues to be able to fulfill its mission. For more information,
see arXiv’s [Operating
Principles](https://confluence.cornell.edu/display/arxivpub/arXiv+Public+Wiki?preview=/340902451/340902455/arXivPrinciplesMarch12.pdf).

By using arXiv APIs, you are agreeing to the terms and conditions outlined on
this page.

- You understand that e-prints from arXiv are subject to all applicable
  copyright protections. The redistribution of e-prints requires permission
  from the copyright holder, which may be the author(s) or publisher. arXiv is
  not the copyright holder on any of the e-prints available through the API. In
  some cases, submitters have provided permission in advance by submitting
  their e-print under a permissive Creative Commons license. The vast majority
  of e-prints are submitted under the [arXiv.org non-exclusive right to
  distribute](https://arxiv.org/licenses/nonexclusive-distrib/1.0/license.html).
  For more information about licenses, see https://arxiv.org/help/license.
- You are free to use descriptive
  [metadata](https://arxiv.org/help/prep)<sup>1</sup> about arXiv e-prints
  under the terms of the [Creative Commons Universal (CC0 1.0) Public Domain
  Declaration](https://creativecommons.org/publicdomain/zero/1.0/). Metadata
  are provided by authors, volunteer moderators, arXiv staff, and external
  partners.
- You agree to abide by the arXiv [Code of
  Conduct](../../help/policies/code_of_conduct.md) in all of your interactions with arXiv
  staff and those involved in its operation, and understand that if you violate
  the CoC we may prohibit you from using arXiv APIs.
- You agree to respect limitations on use of arXiv APIs, including rate limits
  and authorization mechanisms. If we think that you are attempting to
  circumvent those limitations, that your use of arXiv APIs threatens normal
  operation or availability of the arXiv platform, or that you are doing
  something illegal or unethical, we may further limit or block your access.
- You understand that we will make changes to arXiv APIs that may lead to
  compatibility issues with your code. We will do our best to provide advance
  notice of such changes via our [website](https://api.arxiv.org) and the
  [arXiv API group](https://groups.google.com/forum/#!forum/arxiv-api). It is
  up to you to keep track of changes that might affect your use of arXiv APIs
  and to make any required changes.
- In order to provide support and improvements for developers who use arXiv
  APIs, you understand that we will collect certain private information about
  you, such as your name and email address. Please see the [arXiv Privacy
  Policy](../../help/policies/privacy_policy.md) for information about how we use and
  protect your information. In order to promote use of arXiv APIs and showcase
  your work, we may give you the option to make information about you or your
  project publicly available.

## Limitations

### Rate limits

Please note that the following rate limits apply to all of the machines under
your control as a whole. You should not attempt to overcome these limits by
increasing the number of machines used to make requests. If your use-case
requires a higher request rate, please [contact our support team](http://arxiv.org/support/general_help).

- When using the legacy APIs (including OAI-PMH, RSS, and the arXiv API), make
  no more than one request every three seconds, and limit requests to a single
  connection at a time.

These limits may change in the future.

## Things that you can (and should!) do

- Retrieve, store, transform, and share **descriptive metadata** about arXiv
  e-prints.
- Retrieve, store, and use the **content** of arXiv e-prints for your own
  personal  use, or for research purposes.
- Provide tools and services to users that helps them to discover or be
  notified about arXiv e-prints. For example:
  - A better search interface;
  - A mobile app that notifies users about e-prints that might be of interest
    to them;
  - A visualization of topics in arXiv e-prints over time;
  - A citation graph using bibliographic references from e-prints.
- Build other kinds of interfaces that help users to interact with arXiv in new
  and useful ways, leveraging our APIs.
- Direct users to arXiv.org to retrieve e-print content (PDF, source files,
  etc). We encourage you to link to the abstract page.

## Things that you must not do
- Store and serve arXiv e-prints (PDFs, source files, or other content) from
  your servers, unless you have the permission of the copyright holder or are
  permitted to do so by the license with which the e-print was submitted. Note
  that a very small subset of arXiv e-prints are submitted with licenses that
  permit redistribution.
- Represent your project as endorsed or supported by arXiv.org without our
  permission.
- Attempt to circumvent rate limits.
- Use someone else’s credentials to access arXiv APIs.

If you have questions about what uses of arXiv APIs and content are acceptable,
please contact our user support team through our [arXiv user support portal](http://arxiv.org/support/general_help).

<sup>1</sup>Descriptive metadata includes information for discovery and
identification purposes, and includes fields such as title, abstract, authors,
identifiers, and classification terms. For details about arXiv metadata, see
[our help page on metadata prep](https://info.arxiv.org/help/prep.html).
