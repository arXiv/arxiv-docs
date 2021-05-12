What is MathJax?
================

MathJax is a javascript display engine for rendering <span class="mathjax">$\\TeX$</span> or
MathML-coded mathematics in browsers without requiring font installation
or browser plug-ins. Any modern browser with javascript enabled will be
MathJax-ready. For general information about MathJax, visit
[mathjax.org](https://mathjax.org).

Below are questions and answers about the use of MathJax on arXiv.

### Where is MathJax being used on arXiv?

We have enabled MathJax on this help page, article abstract and list
pages, the user account page, the submission preview page and search
result pages. On these pages, MathJax has been configured to render
inline (<span class="ignore_mathjax">$-enclosed</span>) <span
class="mathjax">$\\TeX$</span> only. For example, the expression
<span class="ignore_mathjax">`$P(E) = {n \choose k} p^k (1-p)^{ n-k}$`</span>
will be rendered as <span class="mathjax">$P(E) = {n \choose k} p^k (1-p)^{ n-k}$</span>. 
MathML is not supported in arXiv's MathJax configuration.

In general, MathJax will only attempt to render <span class="mathjax">$\\TeX$</span> in the article
title, abstract and comments fields.

### How do I know if MathJax is being used on an arXiv page?

MathJax-enabled pages may briefly display a small box to indicate that
the MathJax configuration is being loaded, regardless of whether there
is any renderable <span class="mathjax">$\\TeX$</span> on the page. Valid 
<span class="mathjax">$\\TeX$</span> expressions will be
displayed by MathJax as the page is being loaded. On abstract pages, any
<span class="mathjax">$\\TeX$<span> expressions that MathJax cannot render will be displayed in
their original text.

On the user account and submission preview pages, rendering errors or
unknown macros are displayed in red. For example: <span class="mathjax">$\\invalid\_TeX$</span>.

### Can I see the underlying <span class="mathjax">$\\TeX$</span> coding? 

Yes, to access the underlying <span class="mathjax">$\\TeX$</span>,
right- or control-click on a rendered math formula, and choose the
format you want from the `Format` sub-menu.
Then select the `Show Source` menu item to get a pop-up that allows you to copy the math
source into another application.

To try this feature, visit <https://cdn.mathjax.org/mathjax/latest/test/sample-dynamic.html>.

Alternatively, MathJax can be disabled entirely (see below).

### Can I disable MathJax?

Yes, you can disable (and re-enable) MathJax by clicking the following
link to set a cookie:

    <a href="javascript:setMathjaxCookie()" id="mathjax_toggle">Disable MathJax</a>

When MathJax is disabled, mathematical expressions are displayed as text
with the original <span class="mathjax">$\\TeX$</span> delimiters.

Note that on any particular MathJax-enabled page in arXiv, not all
expressions may be renderable. So turning MathJax on or off may have no
effect on the visual appearance of certain math expressions.

### As an arXiv submitter, how can I make the best use of MathJax?

MathJax supports a very large subset of <span class="mathjax">$\\TeX$</span> mathematics, including
AMS math and symbols. arXiv's implementation of MathJax does not support
user-defined macros. For example, if an abstract contains <span class="mathjax">$\\rtwo$</span> as a
shortcut for <span class="mathjax">$\\mathbf{R}\^2$</span>, then MathJax will not be able to render
this expression. Submitters should use only standard <span class="mathjax">La$\\TeX$</span> and
AMS-La<span class="mathjax">$\\TeX$</span> macros in paper titles and abstracts.

Also, since '<' is a reserved character in HTML, special care must be
taken in its use. Usually just adding a space after it will suffice for
it not to be interpreted as the start of an element name (e.g., 'x <
y', not 'x<y'); but if in doubt, use the entity reference '&lt;'.

### Where can I get help regarding MathJax?

The MathJax web site has useful information about browser configuration,
fonts, MathJax features, etc. Please see the [MathJax
documentation](https://docs.mathjax.org/en/latest/index.html) and the
[FAQ](https://docs.mathjax.org/en/latest/misc/faq.html) if you have
questions.

### How do I report a problem?

If you wish to report a problem, or if you have questions about arXiv's
use of MathJax, please first visit the [contact](contact) page.
