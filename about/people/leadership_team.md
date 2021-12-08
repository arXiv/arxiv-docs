---
title: 'Leadership Team'
template: 'docs/team.html'
people:
  jim:
    name: Jim Entwood
    position: Head of Content
    thumbnail: images/jim.jpg
    bio: |
      Jim coordinates the efforts of the volunteer moderators and arXiv administrators on the daily flow of papers and user support and works with the Scientific Director to develop and improve arXiv's operations policies. His background is in volunteer management and website development for research groups, and he holds an M.A. in Leadership Studies.
  martin:
    name: Martin Lessmeister
    position: Head of Technology
    thumbnail: images/martin.jpg
    bio: |
      Martin oversees the technical operations of the arXiv services and supervises the development team. He coordinates the migration of arXiv’s legacy systems to the next generation architecture in the cloud. His background is in web development with a focus on distributed systems, with an M.Eng. in Computer Science from Cornell University.
  alison:
    name: Alison Fromme
    position: Community Engagement and Development Coordinator
    thumbnail: images/alison.jpg
    bio: |
      Alison leads arXiv's communications and fundraising efforts, including the membership program for academic and research institutions. Alison's background is in science writing, nonprofit fundraising, and teaching. She is a Cornell University alum and holds an M.S. in Zoology from Washington State University.
  helen:
    name: Helen Wang
    position: Product Manager
    thumbnail: images/helen.JPG
    bio: |
      Helen synthesizes arXiv strategic and technical goals to plan internal feature and platform development and coordinates external collaborations. Her background in software spans product management, business development, and data analysis. She holds a B.A. in English with honors from Yale University.
  steinn:
    name: Steinn Sigurdsson
    position: Scientific Director
    orcid: https://orcid.org/0000-0002-8187-1144
    twitter: steinly0
    thumbnail: images/steinn.jpg
    bio: |
      Steinn is Professor of Astrophysics at Penn State University. He holds a Ph.D. in Theoretical Physics from the California Institute of Technology. His research interests include astrophysics and related areas, ranging from cosmology, large scale dynamics and black holes, to formation and evolution of planets and the prospects for discovering non-terrestrial life.
---

arXiv Leadership Team
=====================

$jinja {{ render_columns_open() }} jinja$
$jinja {{ render_person(people.jim) }} jinja$
$jinja {{ render_person(people.steinn) }} jinja$
$jinja {{ render_columns_closed() }} jinja$
$jinja {{ render_columns_open() }} jinja$
$jinja {{ render_person(people.helen) }} jinja$
$jinja {{ render_person(people.martin) }} jinja$
$jinja {{ render_columns_closed() }} jinja$
$jinja {{ render_columns_open() }} jinja$
$jinja {{ render_person(people.alison) }} jinja$
$jinja {{ render_columns_closed() }} jinja$
