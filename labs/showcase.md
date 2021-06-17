---
title: 'arXiv Labs Showcase'
projects:
  bibliographic_overlay:
    title: arXiv Bibliographic Explorer
    repo: https://github.com/mattbierbaum/arxiv-bib-overlay
    thumbnail: ../images/bib-explorer.png
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
    thumbnail: ../images/readability.png
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
    thumbnail: ../images/core-recommender.png
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
    thumbnail: ../images/pwc-logo.png
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
  connected_papers:
    title: Connected Papers
    repo: https://github.com/arXiv/arxiv-browse/tree/develop/browse/static/js/connectedpapers.js
    thumbnail: ../images/connected-papers.png
    more_info:
    - name: About Connected Papers
      link: https://www.connectedpapers.com/about
    collaborators:
    - name: Alex Eitan Tarnavsky
      association: Connected Papers
    - name: Eddie Smolyansky
      association: Connected Papers
    - name: Itay Knaan Harpaz
      association: Connected Papers
    - name: Sahar Perets
      association: Connected Papers
    summary: |
      <a href="https://www.connectedpapers.com" target="_blank" rel="noopener">Connected Papers</a>
      is a unique, visual tool to help researchers and applied scientists find and explore papers relevant to their field of work.

      You can use Connected Papers to:
      <ul>
        <li>Get a visual overview of a new academic field</li>
        <li>Create a bibliography to your thesis</li>
        <li>Discover the most relevant prior and derivative works</li>
        <li>Or simply explore paper-space!</li>
        </ul>
  litmaps:
    title: Litmaps
    thumbnail: ../images/litmaps-logo-square-white.png
    more_info:
    - name: About Litmaps
      link: https://www.litmaps.co/about
    collaborators:
    - name: Kyle Webster
      association: Litmaps
    - name: Axton Pitt
      association: Litmaps
    - name: Digl Dixon
      association: Litmaps
    - name: Hamish Huggard
      association: Litmaps
    - name: Racheal Reeves
      association: Litmaps
    summary: |
      <a href="https://www.litmaps.co" target="_blank" rel="noopener">Litmaps</a>
      is an innovative research discovery tool. It combines interactive
      citation maps, modern search tools, and targeted updates to create a
      cohesive research discovery experience. It can visualize your research
      topic with everything from articles, patents, books, pre-prints, and
      e-prints. From arXiv abstract pages, you can build a literature map from
      the arXiv article you are viewing, visualizing the top connected
      articles, and browse the citation network around it.
---
<style>
h1#arxivlabs {
  margin-top: 0;
}
</style>
{% macro render_project(project) %}
<article class="card">
  <div class="card-content">
    <div class="columns">
      <div class="column is-narrow-tablet">
        <p class="image is-128x128" style="border: 1px solid gray"><img src="{{project.thumbnail}}" alt="" /></p>
      </div>
      <div class="column is-one-third-desktop is-one-half-tablet">
        <h2>{{ project.title }}</h2>
        <span class="label">Collaborator{%- if project.collaborators|length > 1 -%}s{%- endif -%}: </span>
        {% for collaborator in project.collaborators %}
        <p>{% if collaborator.link %}<a href="{{ collaborator.link }}" target="_blank" rel="noopener">{{ collaborator.name }}</a>{% else %}{{ collaborator.name }}{% endif %}<br />
        {%- if collaborator.association -%}
        <em>{{ collaborator.association }}</em></p>
        {%- endif -%}
        {% endfor %}
      </div>
      <div class="column">
        <p>{{ project.summary|safe }}</p>
      </div>
    </div>
    {%- if project.repo -%}
    <p class="has-text-right"><span class="has-text-weight-bold">
      Code: </span>{{ project.repo }}</p>
    {%- endif -%}
    {%- if project.more_info -%}
    <p class="has-text-right"><span class="has-text-weight-bold">
      More Information: </span><br/>
      {%- for info in project.more_info -%}
      <a href="{{ info.link}}" target="_blank" rel="noopener">{{ info.name }}</a><br/>
      {%- endfor -%}
    </p>
    {%- endif -%}
  </div>
</article>
{% endmacro %}


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
# arXivLabs: Showcase

arXiv is surrounded by a community of researchers and developers working at the cutting edge of information science and technology.

While the arXiv team is focused on our core mission—providing rapid dissemination of research findings at no cost to readers and submitters—we are excited to be experimenting with a small number of collaborators on projects that add value for our stakeholders and advance research.

Below are some of the projects that our collaborators are working on right now.

Interested in proposing a new arXiv Labs project?

<a href="/project-proposal" class="button-fancy">Click to submit your idea <span> </span></a>

{{ render_project(page.meta.projects.litmaps) }}
{{ render_project(page.meta.projects.connected_papers) }}
{{ render_project(page.meta.projects.pwc_links) }}
{{ render_project(page.meta.projects.core_recommender) }}
{{ render_project(page.meta.projects.bibliographic_overlay) }}
<br/>
We are grateful to the [volunteer developers](https://arxiv.org/about/people/developers) who contribute to the arXiv codebase and invite you to get involved. Please see the [arXivLabs invitation to collaborate](/) and [guidelines for contributors](https://github.com/arXiv/.github/blob/master/CONTRIBUTING.md), or contact nextgen@arxiv.org, for more information about contributing to arXivLabs.
