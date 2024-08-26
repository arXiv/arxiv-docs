# ATOM feed Specifications

For optimal ATOM feed results, please review our RSS channel elements, definitions and examples. 

## ATOM Channel Elements

**&lt;id&gt;**  
Feed identifier  
```
<id>http://rss.arxiv.org/atom/</id>
```

**&lt;title&gt;**  
Title of the subject classification  
```
<title>math.OC updates on arXiv.org</title>
```

**&lt;updated&gt;**  
The last time the feed was generated. arXiv updates the feed content every day at midnight Eastern Standard Time.  
```
<updated>2024-02-23T16:08:30.941605+00:00</updated>
```

**&lt;link href&gt;**  
Link to the feed  
```
<link href="http://rss.arxiv.org/atom/math.OC" rel="self" type="application/atom+xml"/>
```

**&lt;subtitle&gt;**  
Description or subtitle of the feed  
```
<subtitle>math.OC updates on the arXiv.org e-print archive.</subtitle>
```

## ATOM Entry Elements

**&lt;id&gt;**  
arXiv ID representing the article's canonical name
```
<id>oai:arXiv.org:2203.01250v3</id>
```

**&lt;title&gt;**  
Title of the article  
```
<title>Mass concentration in rescaled first order integral functionals</title>
```

**&lt;updated&gt;**  
The last time the feed was generated. arXiv updates the feed content every day at midnight Eastern Standard Time.  
```
<updated>2024-02-23T16:08:30.942190+00:00</updated>
```

**&lt;link href&gt;**  
Link to the article abstract  
```
<link href="https://arxiv.org/abs/2203.01250" rel="alternate" type="text/html"/>
```

**&lt;summary&gt;**  
arXiv ID (the article’s canonical name); Announce Type describing if the paper is new to arXiv, a replacement or update to an already existing paper, or cross listing; Abstract of the article.  
```
<summary>arXiv:2203.01250v3 Announce Type: replace-cross 
Abstract: We consider first order local minimization problems of the form $\min \int_{\mathbb{R}^N}f(u,\nabla u)$ under a mass constraint $\int_{\mathbb{R}^N}u=m$. We prove that the minimal energy function $H(m)$ is always concave, and that relevant rescalings of the energy, depending on a small parameter $\varepsilon$, $\Gamma$-converge towards the $H$-mass, defined for atomic measures $\sum_i m_i\delta_{x_i}$ as $\sum_i H(m_i)$. We also consider Lagrangians depending on $\varepsilon$, as well as space-inhomogeneous Lagrangians and $H$-masses. Our result holds under mild assumptions on $f$, and covers in particular $\alpha$-masses in any dimension $N\geq 2$ for exponents $\alpha$ above a critical threshold, and all concave $H$-masses in dimension $N=1$. Our result yields in particular the concentration of Cahn-Hilliard fluids into droplets, and is related to the approximation of branched transport by elliptic energies.</summary>
```

**&lt;category term&gt;**  
Subject classifications. Articles can be classified under more than one category.  
```
<category term="math.AP"/>
<category term="math.OC"/>
```
**&lt;published&gt;**
Announcement date for the update on the article. For new papers this is the date the paper was officially announced on arXiv, for all other its the date of the official announcement of the update.  
```
<published>2024-08-23T00:00:00-04:00</published>
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

**&lt;arxiv:journal_reference&gt;** *optional element*  
Name, date, issue of journal if the paper is already published  
```
<arxiv:journal_reference>Journal de l'\'Ecole polytechnique - Math\'ematiques, Tome 11 (2024), pp. 431-472</arxiv:journal_reference>
```

**&lt;arxiv:DOI&gt;** *optional element*  
DOI of a paper that is already published in a journal  
```
<arxiv:DOI>10.5802/jep.257</arxiv:DOI> 
```

**&lt;dc:creator&gt;**  
List of the paper's author orauthors separated by comma  
```
<dc:creator>Antonin Monteil, Paul Pegon</dc:creator>
```
