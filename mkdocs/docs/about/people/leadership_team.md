---
title: 'Leadership Team'
people:
  eleonora:
    name: Eleonora Presani
    position: Executive Director
    thumbnail: images/eleonora.jpg
    bio: |
      As Executive Director, Eleonora leads daily operations at arXiv, including technical and business planning, governance, and fundraising efforts. After a PhD and postdoc in astroparticle physics, her career moved to scientific publishing and, later, to digital product development, servicing the research community.
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

{% macro render_person(person) %}
<article class="column is-half">
      <div class="media">
        <div class="media-left is-hidden-mobile">
          <p class="image is-96x96"><img style="border-radius: 50%" src="../../{{person.thumbnail}}" alt="" /></p>
        </div>
        <div class="media-content">
          <p class="image is-48x48 is-hidden-tablet is-pulled-left" style=" margin-right: .5em; margin-top: 1.5em;"><img style="border-radius: 50%;" src="../../{{person.thumbnail}}" alt="" /></p>
          <h2 class="title">{{ person.name }}</h2>
          <p class="subtitle">{{ person.position }}</p>
          <p>{{ person.bio }}</p>
          <ul class="is-marginless">
          {% if person.orcid %}
            <li class="orcid" style="list-style: none"><span class="icon is-small" style="vertical-align: middle"><img src="../../images/orcid_32x32.png" alt="" /></span> <a href="{{ person.orcid }}">{{ person.orcid }}</a></li>
          {% endif %}
          {% if person.twitter %}
            <li class="twit" style="list-style: none"><span class="icon is-small"><i class="fa fa-twitter has-text-link" role="presentation"></i></span><a href="https://twitter.com/{{ person.twitter }}">@{{ person.twitter }}</a></li>
          {% endif %}
          </ul>
        </div>
      </div>
</article>
{% endmacro %}

{% macro render_columns_open() -%}
<div class="columns">
{%- endmacro %}

{% macro render_columns_closed() -%}
</div>
{%- endmacro %}


{{render_columns_open() }} 
{{render_person(page.meta.people.eleonora) }} 
{{render_person(page.meta.people.steinn) }} 
{{render_columns_closed() }} 
{{render_columns_open() }} 
{{render_person(page.meta.people.jim) }} 
{{render_person(page.meta.people.martin) }} 
{{render_columns_closed() }} 
{{render_columns_open() }} 
{{render_person(page.meta.people.alison) }} 
{{render_columns_closed() }} 
