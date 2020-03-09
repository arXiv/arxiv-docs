---
title: 'Leadership Team'
template: 'docs/team.html'
people:
  eleonora:
    name: Eleonora Presani
    position: Executive Director
    thumbnail: images/eleonora.jpg
    bio: |
      As Executive Director, Eleonora oversees daily operations at arXiv, including technical and business planning, governance, and fundraising efforts. Eleonora also facilitates decisions and communications between the Member Advisory Board and the Scientific Advisory Board. After a PhD and postdoc in astroparticle physics, her career moved to scientific publishing and, later, to digital product development, servicing the research community.
  jim:
    name: Jim Entwood
    position: Operations Manager
    thumbnail: images/jim.jpg
    bio: |
      Jim coordinates the efforts of the volunteer moderators and arXiv administrators on the daily flow of papers and user support and works with the Scientific Director to develop and improve arXiv's operations policies. His background is in volunteer management and website development for research groups, and he holds an M.A. in Leadership Studies.
  martin:
    name: Martin Lessmeister
    position: IT Lead
    thumbnail: images/martin.jpg
    bio: |
      Martin oversees the day-to-day technical operations of the arXiv services and supervises the development team. He works closely with our Lead Software Architect in planning and executing the migration of arXiv’s legacy software system to the next generation (arXiv-NG) architecture. His background is in web development with a focus on distributed systems, with an M.Eng. in Computer Science from Cornell University.
  alison:
    name: Alison Fromme
    position: Community Engagement and Development Coordinator
    thumbnail: images/alison.jpg
    bio: |
      Alison coordinates the outreach and marketing program to engage educational institutions in arXiv’s membership program. She also implements fundraising strategies, including grant writing and online campaigns. Alison is a professional science writer with an M.S. in zoology.
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
$jinja {{ render_person(people.martin) }} jinja$
$jinja {{ render_person(people.alison) }} jinja$
$jinja {{ render_person(people.eleonora) }} jinja$
$jinja {{ render_columns_closed() }} jinja$
