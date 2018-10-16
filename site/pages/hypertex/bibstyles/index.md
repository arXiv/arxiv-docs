# BibTeX and Eprints


Bibtex styles can be easily converted to support the **eprint** field for referring to eprints. You can add eprint entries to your bibtex database like this,
```
 @Article{Beneke:1997hv,
      author    = "M. Beneke and G. Buchalla and I. Dunietz",
      title     = "{Mixing induced CP asymmetries in inclusive B decays}",
      journal   = "Phys. Lett.",
      volume    = "B393",
      year      = "1997",
      pages     = "132-142",
      **eprint        = "hep-ph/9609357"**
 }
```
The change is backwards compatible. The eprint field is just ignored when you use a style which doesn't support eprints, and the references are formatted as normal.

For the new style arXiv identifiers (April 2007 and onwards) we recommend these bib-style extensions:

     **archivePrefix = "arXiv"**,
     **eprint        = "0707.3168"**,
     **primaryClass  = "hep-th"**,

With one of the enhanced styles below, the eprint identifier would automatically appear in your references in our recommended standard form (see the [references section of the submit help](/help/submit_tex#refs) for details), e.g,

> \[1\] M. Beneke and G. Buchalla and I. Dunietz, _Mixing induced CP asymmetries in inclusive B decays_, Phys. Lett. B393, 132-142, 1997, hep-ph/9609357.

Papers downloaded from the archive are produced with [HyperTeX](/hypertex). With HyperTeX the string **hep-ph/9609357** becomes a clickable hyperlink to the on-line abstract of that paper at [arXiv:hep-ph/9609357](/abs/hep-ph/9609357) when viewed with a suitable program. Such programs include PDF viewers e.g. Acroread or OmniPDF, or a modified versions of ghostview.

Note that the eprint field is automatically included in the bibtex output of the [SLAC SPIRES](http://www.slac.stanford.edu/spires/hep) database listings (Select Output Format: BIBTEX). Using SPIRES is an easy way to collect bibtex references without having to type them by hand (and the concomitant possibility of error).

The following bibtex styles have been modified to support an eprint field,

*   [h-elsevier.bst](h-elsevier.bst) Nuclear Physics style with e-print and collaboration fields by Jonathan Flynn
*   [h-physrev.bst](h-physrev.bst) Phys Rev style with e-print and collaboration fields by Jonathan Flynn
*   [hep.bst](hep.bst) combination of alpha.sty and report.sty with e-print and collaboration fields from Burkhard Klaus.
*   Simple extensions of the basic bibstyles to allow an eprint field,
    *   [habbrv.bst](habbrv.bst) base bibstyle abbrv.bst with eprint field
    *   [hacm.bst](hacm.bst) base bibstyle acm.bst with eprint field
    *   [halpha.bst](halpha.bst) base bibstyle alpha.bst with eprint field
    *   [hapalike.bst](hapalike.bst) base bibstyle apalike.bst with eprint field
    *   [hieeetr.bst](hieeetr.bst) base bibstyle ieeetr.bst with eprint field
    *   [hplain.bst](hplain.bst) base bibstyle plain.bst with eprint field
    *   [hplainyr.bst](hplainyr.bst) base bibstyle plainyr.bst with eprint field
    *   [hsiam.bst](hsiam.bst) base bibstyle siam.bst with eprint field
    *   [hunsrt.bst](hunsrt.bst) base bibstyle unsrt.bst with eprint field
    *   [hunsrtnat.bst](hunsrtnat.bst) base bibstyle unsrtnat.bst with eprint field
    *   [hapj.bst](hapj.bst) base bibstyle apj.bst with eprint field by Varendra (Alvin) Das

A gzipped tar file of all the bibstyles is also available ([bibstyles.tar.gz](bibstyles.tar.gz))

You can also find some other eprint bibtex styles written by Jacques Distler, which support both old and new arXiv identifiers, at

*   [http://golem.ph.utexas.edu/~distler/TeXstuff/utphys.bst](http://golem.ph.utexas.edu/~distler/TeXstuff/utphys.bst)
*   [http://golem.ph.utexas.edu/~distler/TeXstuff/utcaps.bst](http://golem.ph.utexas.edu/~distler/TeXstuff/utcaps.bst)

Kasper Peeters' style also supports both old and new arXiv identifiers

*   [kp.bst](kp.bst)

These two styles will use hypertex's \\href command if available.

If you find bugs in the bibtex styles or have any other e-print bibstyles to add to this list please [contact arXiv administrators](/help/contact).