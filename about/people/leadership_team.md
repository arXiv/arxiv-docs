---
title: 'Leadership Team'
template: 'docs/team.html'
people:
  erick:
    name: Erick Peirson
    position: Lead Software Architect
    orcid: https://orcid.org/0000-0002-0564-9939
    twitter: undercaffeinatd
    thumbnail: images/erick.jpg
    bio: |
      Erick is responsible for high-level technical decisions, planning, and collaboration related to the arXiv software system. His main focus is the arXiv-NG project, which moves the arXiv.org software system into a modern, cloud-native architectural paradigm. Erick’s background is in software development for information systems and computational research, and he also holds a PhD in History & Philosophy of Science.
  jim:
    name: Jim Entwood
    position: Operations Manager
    thumbnail: images/jim.jpg
    bio: |
      Jim coordinates the efforts of the volunteer moderators and arXiv administrators on the daily flow of papers and user support, and works with the Scientific Director to develop and improve arXiv's operations policies. His background is in volunteer management and website development for research groups with a Masters in Leadership Studies.
  martin:
    name: Martin Lessmeister
    position: IT Lead
    thumbnail: images/martin.jpg
    bio: |
      Martin is responsible for overseeing the day-to-day technical operations of the arXiv services and is supervisor to the members of the development team. He works closely with our Lead Software Architect in planning and executing the migration of arXiv’s legacy software system to the next generation architecture. His background is in web development with a focus on distributed systems, with an M.Eng. in Computer Science (Cornell University).
  janelle:
    name: Janelle Morano
    position: Community Engagement and Development Coordinator
    orcid: https://orcid.org/0000-0001-5950-3313
    twitter: janellelmorano
    thumbnail: images/janelle.jpg
    bio: |
      Janelle is responsible for the outreach and marketing program and communication strategies. She engages educational institutions in arXiv’s membership program and implements fundraising strategies, including grant writing and giving campaigns. Her background is in animal communication and ecology, with an M.S. in biology.
  oya:
    name: Oya Y. Rieger
    position: Program Director
    orcid: https://orcid.org/0000-0001-6175-5157
    twitter: OyaRieger
    thumbnail: images/oya.jpg
    bio: |
      Oya has been leading the arXiv operation and spearheaded the development of the governance and sustainability model since 2010. She has provided leadership in several national and international scholarly communication and digital preservation initiatives and holds a Ph.D. in Human-Computer Interaction (Cornell University).
  steinn:
    name: Steinn Sigurdsson
    position: Scientific Director
    orcid: https://orcid.org/0000-0002-8187-1144
    twitter: steinly0
    thumbnail: images/steinn.jpg
    bio: |
      Steinn is a Professor of Astrophysics at Penn State University.  He holds a doctorate in theoretical physics from the California Institute of Technology. His research interests include astrophysics and related areas, ranging from cosmology, large scale dynamics and black holes, to formation and evolution of planets, and the prospects for discovering non-terrestrial life.
---

arXiv Leadership Team
=====================

$jinja {{ render_columns_open() }} jinja$
$jinja {{ render_person(people.oya) }} jinja$
$jinja {{ render_person(people.steinn) }} jinja$
$jinja {{ render_columns_closed() }} jinja$
$jinja {{ render_columns_open() }} jinja$
$jinja {{ render_person(people.martin) }} jinja$
$jinja {{ render_person(people.erick) }} jinja$
$jinja {{ render_columns_closed() }} jinja$
$jinja {{ render_columns_open() }} jinja$
$jinja {{ render_person(people.jim) }} jinja$
$jinja {{ render_person(people.janelle) }} jinja$
$jinja {{ render_columns_closed() }} jinja$
