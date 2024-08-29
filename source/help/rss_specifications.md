# RSS feed Specifications

For optimal RSS feed results, please review our RSS channel elements, definitions and examples. 

## RSS Channel Elements

**&lt;title&gt;**  
Title of the feed  
```
<title>math.OC updates on arXiv.org</title>
```

**&lt;link&gt;**  
Link to the feed  
```
<link>http://rss.arxiv.org/rss/math.OC</link>
```

**&lt;description&gt;** 
Description of the subject classification  
```
<description>math.OC updates on the arXiv.org e-print archive.</description>
```

**&lt;atom:link&gt;**  
Another link to the specific feed
```
<atom:link href="http://rss.arxiv.org/rss/math.OC" rel="self" type="application/rss+xml"/>
```

**&lt;docs&gt;**  
Link to RSS 2.0 specification documentation
```
<docs>http://www.rssboard.org/rss-specification</docs>
```

**&lt;language&gt;**  
Language the feed is published in
```
<language>en-us</language>
```

**&lt;lastBuildDate&gt;**  
The last date/time the content in the channel updated
```
<lastBuildDate>Fri, 23 Feb 2024 05:00:11 +0000</lastBuildDate>
```

**&lt;managingEditor&gt;**  
Email for the person(s) responsible for technical issues
```
<managingEditor>rss-help@arxiv.org</managingEditor>
```

**&lt;pubDate&gt;**  
Announcement date for the content in the channel
```
<pubDate>Fri, 23 Feb 2024 00:00:00 -0500</pubDate>
```

**&lt;skipDays&gt;**   
arXiv has an empty feed on Saturday/Sundays and on occasional arXiv holidays  
```
<skipDays>  
      <day>Saturday</day>  
      <day>Sunday</day>  
</skipDays>
```
## RSS Item Elements  

**&lt;title&gt;**  
Title of the article
```
<title>Mass concentration in rescaled first order integral functionals</title>
```

**&lt;link&gt;**  
Link to the abstract
```
<link>https://arxiv.org/abs/2203.01250</link>
```

**&lt;description&gt;**  
arXiv ID (the article’s canonical name); Announce Type describing if the paper is new to arXiv, a replacement or update to an already existing paper, or cross listing; Abstract of the article.  
```
<description>arXiv:2203.01250v3 Announce Type: replace-cross 
Abstract: We consider first order local minimization problems of the form $\min \int_{\mathbb{R}^N}f(u,\nabla u)$ under a mass constraint $\int_{\mathbb{R}^N}u=m$. We prove that the minimal energy function $H(m)$ is always concave, and that relevant rescalings of the energy, depending on a small parameter $\varepsilon$, $\Gamma$-converge towards the $H$-mass, defined for atomic measures $\sum_i m_i\delta_{x_i}$ as $\sum_i H(m_i)$. We also consider Lagrangians depending on $\varepsilon$, as well as space-inhomogeneous Lagrangians and $H$-masses. Our result holds under mild assumptions on $f$, and covers in particular $\alpha$-masses in any dimension $N\geq 2$ for exponents $\alpha$ above a critical threshold, and all concave $H$-masses in dimension $N=1$. Our result yields in particular the concentration of Cahn-Hilliard fluids into droplets, and is related to the approximation of branched transport by elliptic energies.</description>
```

**&lt;guid isPermaLink="false'&gt;**  
Unique Identifier of the article  
```
<guid isPermaLink="false">oai:arXiv.org:2203.01250v3</guid>
```

**&lt;category&gt;**
Subject classifications. Articles can be classified under more than one category  
```
<category>math.AP</category>  
<category>math.OC</category>
```

**&lt;pubDate&gt;**
Publish date for the update on the article. For new announcements this is the date the paper was officially announced on arXiv, for all other its the date of the official announcement of the update.  
```
<pubDate>Fri, 23 Aug 2024 00:00:00 -0400</pubDate>
```

**&lt;arxiv:announce_type&gt;**  
Announce types defined: 

*  New listings are papers that are released for the first time on arXiv   
*  Replacement listings are updated versions of papers that are released  
*  Cross listings are papers that are announced as new to categories that are not their primary category
```
<arxiv:announce_type>replace-cross</arxiv:announce_type>
```

**&lt;dc:rights&gt;**  
Link to the paper’s copyright license on arXiv  
```
<dc:rights>http://creativecommons.org/licenses/by/4.0/</dc:rights>
```

**&lt;arxiv:DOI&gt;** *optional element*  
DOI of a paper that is already published in a journal  
```
<arxiv:DOI>10.5802/jep.257</arxiv:DOI>
```  

**&lt;arxiv:journal_reference&gt;** *optional element*  
Name, date, issue of journal if the paper is already published  
```
<arxiv:journal_reference>Journal de l'\'Ecole polytechnique - Math\'ematiques, Tome 11 (2024), pp. 431-472</arxiv:journal_reference>
```

**&lt;dc:creator&gt;**  
List of the paper's author orauthors separated by comma  
```
<dc:creator>Antonin Monteil, Paul Pegon</dc:creator>
```



