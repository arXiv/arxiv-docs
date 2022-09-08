Example using the `myarticles` widget with `arxiv` format
=========================================================

This page illustrates use of the JavaScript [`myarticles`
widget](myarticles) and the "`arxiv`" display format which mimics the
style of search results and listings on arXiv.

The code used on this page is:

```
<script type="text/javascript">
<!--
var arxiv_authorid="http://arxiv.org/a/warner_s_1";
var arxiv_format="arxiv";
var arxiv_max_entries=0;       //show all articles
var arxiv_includeSummary=1;    //show abstracts (default is 0)
var arxiv_includeComments=0;   //do not show comments (default is 1)
//--></script>
<script type="text/javascript" src="http://arxiv.org/js/myarticles.js"></script>
<div id="arxivfeed">[Loading myarticles...]</div>
```

The output is shown in the shaded box below. Additional [configuration
options](myarticles#config) can be used to further control the layout
and styling.

\[Loading myarticles...\]
