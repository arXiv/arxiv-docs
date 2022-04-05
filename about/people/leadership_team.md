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
  brian:
    name: Brian Caruso
    position: Interim Head of Technology
    thumbnail: images/brianc.jpg
    bio: |
      Brian oversees the technical operations of the arXiv services and supervises the development team. He coordinates operations and
maintenance of arXiv’s systems. He holds a B.A. in Computer Science from Clark University.
  alison:
    name: Alison Fromme
    position: Community Engagement Manager
    thumbnail: images/alison.jpg
    bio: |
      Alison leads arXiv's communications and fundraising efforts, including the membership program for academic and research institutions. Alison's background is in science writing, nonprofit fundraising, and teaching. She is a Cornell University alum and holds an M.S. in Zoology from Washington State University.
  shamsi:
    name: Shamsi Brinn
    position: UX Lead 
    thumbnail: images/shamsi.JPG
    bio: |
      Shamsi brings the experiences of arXiv’s diverse users to the forefront of organizational planning. Her role includes gathering feedback and testing product experiences with users, disseminating research findings, and using feedback to inform design and development across the arXiv platform. Her experience spans design, user experience, user research, and innovation strategy.
  noga:
    name: Noga Ginzburg
    position: Special Projects Lead
    thumbnail: images/noga.JPG
    bio: |
      Noga... 
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
$jinja {{ render_person(people.shamsi) }} jinja$
$jinja {{ render_person(people.brian) }} jinja$
$jinja {{ render_columns_closed() }} jinja$
$jinja {{ render_columns_open() }} jinja$
$jinja {{ render_person(people.alison) }} jinja$
$jinja {{ render_columns_closed() }} jinja$
$jinja {{ render_columns_open() }} jinja$
$jinja {{ render_person(people.noga) }} jinja$
$jinja {{ render_columns_closed() }} jinja$
