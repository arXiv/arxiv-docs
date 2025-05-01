---
title: Why do my citations appear in long form
---

# Why do my citations appear in long form [1,2,3,4] instead of short form [1-4]?

Papers submitted before arXiv Submission version 1.5 will retain the hyperlink behavior as outlined below. For submissions made using the version 1.5 system or later that include the hyperref package, the default hyperlink behavior will follow the TeX Live default version of hyperref.

Some latex packages such as the `cite` package normally show citations
in a condensed form using a range, e.g., [1-4], instead of
[1,2,3,4]. By default, we process papers with
[HyperTeX](http://arxiv.org/hypertex), which automatically adds
hyperlinks from the citations with the body of the text to the
bibliography. To be able to do this on a per-citation basis it is
necessary to use the long form (how would you link to reference 2 in
1-4?), so this is the default behavior.

We argue that the benefit of citation links outweighs the slightly
longer form of the citations. However, if you insist on preserving the
short form for citations then you may [turn off HyperTeX for your
paper](mistakes.md#nohypertex).
