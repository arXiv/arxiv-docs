---
title: 'arXiv Labs showcase'
template: 'labs/showcase.html'
projects:
  bibliographic_overlay:
    title: arXiv Bibliographic Explorer
    repo: https://github.com/mattbierbaum/arxiv-bib-overlay
    thumbnail: labs/images/bib-explorer.png
    collaborators:
    - name: Matt Bierbaum
      association: Cornell Computing and Information Science
    summary: |
      The arXiv bibliographic overlay displays information about works that cite
      and are cited by arXiv papers and their published versions. The primary
      objective of the project is to enable discovery of relevant research and
      context by providing user-friendly navigation of an article's citation
      tree.
  HTML5_readability:
    title: arXiv HTML5 & Readability
    repo: https://github.com/cul-it/arxiv-readability
    thumbnail: labs/images/readability.png
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
---
# arXiv Labs

arXiv is surrounded by a community of researchers and developers working at the
cutting edge of information science and technology.

While the arXiv team is focused on our core mission—providing rapid
dissemination of research findings at no cost to readers and submitters—we are
excited to be experimenting with a small number of collaborators on projects
that add value for our stakeholders and advance research.

Here are some of the projects that our collaborators are working on right now.

{{ render_project(projects.bibliographic_overlay) }}
{{ render_project(projects.HTML5_readability) }}
