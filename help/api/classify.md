---
title: API for arXiv Categorization
---

<div id="myheader">

# API for arXiv Categorization

<div id="toc">

<div id="toctitle">

Table of Contents

</div>

**JavaScript must be enabled in your browser to display the table of
contents.**

</div>

</div>

<div id="preamble">

<div class="sectionbody">

</div>

</div>

## 1\. Preface

<div class="sectionbody">

<div class="paragraph">

This API allows for automatic **text classification** according to the
[categorization scheme](http://arxiv.org/help/prep#subj) used by
[arXiv](http://arxiv.org/).

</div>

</div>

## 2\. The arXiv Categorization scheme

<div class="sectionbody">

<div class="paragraph">

Research articles submitted to [arXiv](http://arxiv.org/) are
categorized according to a [classification
scheme](http://arxiv.org/help/prep#subj) that has slowly evolved out of
requirements of the involved research communities, user and moderator
feedback, and input from the arXiv [scientific advisory
board](http://arxiv.org/help/scientific_ad_board). This scheme allows
for targeted browsing of subsections of new submissions, subscription to
particular channels, higher relevance of specific listings to the user’s
interests. It also allows to narrow down searches, etc..

</div>

</div>

## 3\. Automatic Classification

<div class="sectionbody">

<div class="paragraph">

So far arXiv has relied on appropriate author self classification of new
submissions with guidance and occasional correction by
[moderators](http://arxiv.org/help/moderation) and other feedback
mechanisms. Recently automatic classification of new submissions via
comparison to the existing body of nearly 600,000 previously classified
research articles in arXiv’s holdings has become feasible with
sufficient accuracy.

</div>

<div class="paragraph">

arXiv has implemented two algorithms to provide a best match
classification and accompanying score based on the full text of an
article. These are based on the common TF-IDF-cosine distance measure
and the asymmetric Kullback–Leibler divergence. We decided to make these
publicly available via a simple API, so that third parties and in
particular authoring tools supporting submission to arXiv can determine
the likely classification of a piece of text or intended submission.

</div>

</div>

## 4\. Description of the API

<div class="sectionbody">

<div class="paragraph">

Both the [arXiv API](http://arxiv.org/help/api/index) and the
[SWORD/APP](http://arxiv.org/help/submit_sword) submission interface are
using [Atom](http://tools.ietf.org/html/rfc4287), and we decided to
build on that and provide classification information via an Atom feed
response to a standard **HTTP POST** of a PDF file or a (fragment of)
plain text to

</div>

<div class="listingblock">

<div class="content">

    http://export.arxiv.org/api/classify

</div>

</div>

<div class="paragraph">

For demonstration purposes [**this
link**](http://export.arxiv.org/api/classify?text=kinematics%20and%20dynamics%20of%20stellar%20disks)
issues a sample query for text="kinematics and dynamics of stellar
disks" and returns the corresponding categorization feed.

</div>

<div class="paragraph">

The response is a feed which contains Atom entries encoding the likely
classification in an *\<atom:category\>* element, e.g.

</div>

<div class="listingblock">

<div class="content">

    <category term="http://arxiv.org/terms/arXiv/astro-ph.CO"
              scheme="http://arxiv.org/terms/arXiv/"
              label="Physics - Cosmology and Extragalactic Astrophysics"/>

</div>

</div>

<div class="paragraph">

and the numerical **score** in a score extension element in the arxiv
namespace \_xmlns:arxiv="http://arxiv.org/schemas/atom", e.g.

</div>

<div class="listingblock">

<div class="content">

    <arxiv:score>0.02412488927537541</arxiv:score>

</div>

</div>

<div class="paragraph">

In addition the *\<atom:title\>* element of the entry contains the rank,
a human readable form of the category, and the score in parentheses,
e.g.

</div>

<div class="listingblock">

<div class="content">

    <title>4: Astrophysics - Cosmology and Extragalactic Astrophysics (0.024)</title>

</div>

</div>

<div class="paragraph">

The category element has the same form as used in the SWORD/APP deposit
api. This should allow for straightforward integration with (existing)
SWORD clients, which can directly use the classification term(s) for the
category element(s) of a submission in progress.

</div>

<div class="paragraph">

Users who are registered for access to the arXiv SWORD API can obtain a
list of available classifications from the [SWORD
Servicedocument](https://arxiv.org/sword-app/servicedocument)

</div>

</div>

## 5\. Optional Parameters

<div class="sectionbody">

<div class="paragraph">

There are 2 optional parameters which can be specified as **key-value**
pairs in the request URI. They control the scoring method and the number
of results returned.

</div>

<div class="ulist">

<div class="title">

Parameters

</div>

  - scoring\_method Currently arxiv supports 2 different scoring
    methods. The asymmetric Kullback Leibler divergence (*asymKL*) and
    the TF-IDF (Term Frequency Inverse Document Frequency) cosine
    distance (*tfidfcosine*). The default is *asymKL*.

  - max\_entries This determines the maximum number of entries returned
    in the feed. The default is *10*.

</div>

<div class="paragraph">

A query with no parameters is equivalent
    to:

</div>

<div class="listingblock">

<div class="content">

    POST http://export.arxiv.org/api/classify?scoring_method=asymKL&max_entries=10

</div>

</div>

</div>

## 6\. Full Example

<div class="sectionbody">

<div class="paragraph">

POSTing a PDF file with optional
    parameters

</div>

<div class="listingblock">

<div class="content">

    lwp-request -m POST -c application/pdf  'http://export.arxiv.org/api/classify?scoring_method=asymKL&max_entries=3' < 1002.0386.pdf

</div>

</div>

<div class="listingblock">

<div class="content">

    <?xml version="1.0" encoding="utf-8"?>
    <feed xmlns="http://www.w3.org/2005/Atom">
      <title>arXiv Categorization Query: 25de8ccafdbac09ac16c83660ae3b5609219cadfa912101db82fad6b4e526feb</title>
      <id>info:arxiv/api/classify/25de8ccafdbac09ac16c83660ae3b5609219cadfa912101db82fad6b4e526feb</id>
      <link type="application/xhtml+xml" rel="related" href="http://arxiv.org/api/classify"/>
      <author>
        <name>arXiv.org API</name>
        <uri>http://arxiv.org/help/contact</uri>
      </author>
      <updated>2010-04-28T19:56:51Z</updated>
      <entry>
        <id>info:arxiv/api/classify/25de8ccafdbac09ac16c83660ae3b5609219cadfa912101db82fad6b4e526feb/1</id>
        <title>1: Astrophysics - Cosmology and Extragalactic Astrophysics (50.446)</title>
        <category term="http://arxiv.org/terms/arXiv/astro-ph.CO"
                  scheme="http://arxiv.org/terms/arXiv/"
                  label="Astrophysics - Cosmology and Extragalactic Astrophysics"/>
        <arxiv:score xmlns:arxiv="http://arxiv.org/schemas/atom">50.446393287699216</arxiv:score>
        <link rel="alternate" href="http://arxiv.org/archive/astro-ph.CO" type="application/xhtml+xml"/>
        <summary>Classisification of the supplied full text or text fragment based on comparison
                 to the existing body of papers on "http://arxiv.org/" via distance measure "asymKL"</summary>
        <updated>2010-04-28T19:56:51Z</updated>
      </entry>
      <entry>
        <id>info:arxiv/api/classify/25de8ccafdbac09ac16c83660ae3b5609219cadfa912101db82fad6b4e526feb/2</id>
        <title>2: Astrophysics - Galaxy Astrophysics (40.402)</title>
        <category term="http://arxiv.org/terms/arXiv/astro-ph.GA"
                  scheme="http://arxiv.org/terms/arXiv/"
                  label="Astrophysics - Galaxy Astrophysics"/>
        <arxiv:score xmlns:arxiv="http://arxiv.org/schemas/atom">40.401517718239226</arxiv:score>
        <link rel="alternate" href="http://arxiv.org/archive/astro-ph.GA" type="application/xhtml+xml"/>
        <summary>Classisification of the supplied full text or text fragment based on comparison
                 to the existing body of papers on "http://arxiv.org/" via distance measure "asymKL"</summary>
        <updated>2010-04-28T19:56:51Z</updated>
      </entry>
      <entry>
        <id>info:arxiv/api/classify/25de8ccafdbac09ac16c83660ae3b5609219cadfa912101db82fad6b4e526feb/3</id>
        <title>3: Astrophysics (34.663)</title>
        <category term="http://arxiv.org/terms/arXiv/astro-ph"
                  scheme="http://arxiv.org/terms/arXiv/"
                  label="Astrophysics"/>
        <arxiv:score xmlns:arxiv="http://arxiv.org/schemas/atom">34.66288499269639</arxiv:score>
        <link rel="alternate" href="http://arxiv.org/archive/astro-ph" type="application/xhtml+xml"/>
        <summary>Classisification of the supplied full text or text fragment based on comparison
                 to the existing body of papers on "http://arxiv.org/" via distance measure "asymKL"</summary>
        <updated>2010-04-28T19:56:51Z</updated>
      </entry>
    </feed>

</div>

</div>

</div>
