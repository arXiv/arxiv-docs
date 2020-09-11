---
title: 'arXiv Labs showcase'
template: 'labs/showcase.html'
projects:
  bibliographic_overlay:
    title: arXiv Bibliographic Explorer
    repo: https://github.com/mattbierbaum/arxiv-bib-overlay
    thumbnail: images/bib-explorer.png
    collaborators:
    - name: Matt Bierbaum
      association: Cornell Computing and Information Science
    summary: |
      arXiv Bibliographic Explorer displays information about works that cite
      and are cited by arXiv papers and their published versions. The primary
      objective of the project is to enable discovery of relevant research and
      context by providing user-friendly navigation of an article's citation
      tree.
  HTML5_readability:
    title: arXiv HTML5 & Readability
    repo: https://github.com/cul-it/arxiv-readability
    thumbnail: images/readability.png
    collaborators:
    - name: Michael Kohlhase
      association: Friedrich-Alexander Universität Erlangen-Nürnberg
    - name: Ben Firschman
      association: arXiv-Vanity
    - name: Deyan Ginev
      association: Friedrich-Alexander Universität Erlangen-Nürnberg
    summary: |
      Our top priority is to provide a high-quality service to all arXiv authors
      and readers. The overarching objective of this project is to significantly
      improve the usability and accessibility of arXiv papers. While providing
      HTML is not a panacea, it is a first step in the right direction.
  core_recommender:
    title: CORE Recommender
    thumbnail: images/core-recommender.png
    more_info:
    - name: arXiv:1705.00578
      link: https://arxiv.org/abs/1705.00578
    - name: Research outputs by CORE
      link: https://core.ac.uk/about/research-outputs/
    collaborators:
    - name: CORE Team
      link: https://core.ac.uk/about/#team
    summary: |
      Explore relevant open access papers from across a global network of
      research repositories while browsing arXiv. Research papers are
      recommended from both arXiv and other over 10 thousand open access data
      providers and brought to you by
      <a href="https://core.ac.uk/" target="_blank" rel="noopener">CORE</a>,
      the world’s largest aggregator of open access research.
  pwc_links:
    title: arXiv Links to Code
    repo: https://github.com/arXiv/arxiv-browse/tree/develop/browse/static/js/paperswithcode.js
    thumbnail: images/pwc-logo.png
    collaborators:
    - name: Robert Stojnic
      association: Papers with Code / Facebook AI Research
    - name: Viktor Kerkez
      association: Papers with Code / Facebook AI Research
    - name: Ludovic Viaud
      association: Papers with Code / Facebook AI Research
    summary: |
      arXiv Links to Code aims to provide an easy and convenient way to
      find relevant code for a paper. It is using data from
      <a href="https://paperswithcode.com" target="_blank" rel="noopener">
      Papers with Code</a> - a free resource that links papers, code and
      results in Machine Learning. Papers with Code is the biggest such resource and is licensed under an open license.
---
# arXiv Labs

arXiv is surrounded by a community of researchers and developers working at the cutting edge of information science and technology.

While the arXiv team is focused on our core mission—providing rapid dissemination of research findings at no cost to readers and submitters—we are excited to be experimenting with a small number of collaborators on projects that add value for our stakeholders and advance research.

Here are some of the projects that our collaborators are working on right now.

$jinja {{ render_project(projects.pwc-links) }} jinja$
$jinja {{ render_project(projects.core_recommender) }} jinja$
$jinja {{ render_project(projects.bibliographic_overlay) }} jinja$

We are grateful to the [volunteer developers](https://arxiv.org/about/people/developers) who contribute to the arXiv codebase and invite you to get involved. Please see our [guidelines for contributors](https://github.com/arXiv/.github/blob/master/CONTRIBUTING.md), or contact nextgen@arxiv.org, for more information about contributing to arXiv software development.
