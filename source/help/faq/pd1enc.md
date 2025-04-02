---
title: Why do my user defined symbols display incorrectly
---

# Why do my user defined symbols (e.g., `\i, \l, \L, \o, \ae,` etc.) display incorrectly in the processed document?

Papers submitted before arXiv Submission version 1.5 will retain the hyperlink behavior as outlined below. For submissions made using the version 1.5 system that include the hyperref package, the default hyperlink behavior will follow the TeXlive default version of hyperref.

By default, our system processes documents using
[HyperTeX](http://arXiv.org/hypertex), which includes the `pd1enc.def`
macro. Since the macro is called late in the preamble, it will overwrite
previous definitions, including author defined single character
definitions using `\i, \l, \o, \ae,` and some common composites:

``` 
  \DeclareTextCommand{\L}{PD1}{L} % Lslash, \225
  \DeclareTextCommand{\OE}{PD1}{\226} % OE
  \DeclareTextCommand{\IJ}{PD1}{\230}
  \DeclareTextCommand{\i}{PD1}{i} % dotlessi, \232
  \DeclareTextCommand{\l}{PD1}{l} % lslash, \233
  \DeclareTextCommand{\oe}{PD1}{\234} % oe
  \DeclareTextCommand{\AE}{PD1}{\306} % AE
  \DeclareTextCommand{\DH}{PD1}{\320} % Eth
  \DeclareTextCommand{\DJ}{PD1}{\320} % Eth
  \DeclareTextCommand{\O}{PD1}{\330} % Oslash
  \DeclareTextCommand{\TH}{PD1}{\336} % Thorn
  \DeclareTextCommand{\ss}{PD1}{\337} % germandbls
  \DeclareTextCommand{\ae}{PD1}{\346} % ae
  \DeclareTextCommand{\dh}{PD1}{\360} % eth
  \DeclareTextCommand{\o}{PD1}{\370} % oslash
  \DeclareTextCommand{\th}{PD1}{\376} % thorn
  \DeclareTextCommand{\ij}{PD1}{\377}
  \DeclareTextCommand{\SS}{PD1}{SS}
```

To circumvent this problem, you should either avoid using the
abbreviations above, or [disable
HyperTeX](mistakes.md#nohypertex).
