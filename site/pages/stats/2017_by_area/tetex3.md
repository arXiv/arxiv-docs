Possible problems with arXiv transition to teTeX3
-------------------------------------------------

As of 2 November 2006, arXiv is running teTeX 3 with new tex macros
trees for processing all new submissions and replacements. This
represents a significant improvement over the old automatic TeX system
but will likely be slightly disruptive initially. Submitters may have to
change some of their (bad) habits, and possibly modify some TeX sources.

There follows an incomplete list of common symptoms, errors and fixes:

1.  Bad size declared in binary blocks of PostScript files (
    %%BeginBinary: .... count ). Symptoms:

        dvips: ! premature end of file in binary section

        dvips:  expected to see %%EndBinary at end of data; struggling on
        dvips: ! premature end of file in binary section

    fix: figure must be corrected

2.  Newer AIP macros require certain fields to be declared. Symptoms:

        aip classes: ! Class aipproc Error: Missing \keywords declaration.

    fix: provide the \\keywords{} entry for the article

3.  PoS class uses incorrect check for pdftex, it should do ifpdf
    instead. Symptom:

        ! Undefined control sequence.
                  <argument> \def \hash {}\pdfannotlink

    fix: obtain latest PoS class, if that doesn't help contact www-admin

4.  Authors can't bundle parts of hyperref package, either all or none.
    Symptom:

        (/3/texmf-2006/tex/latex/hyperref/pdfmark.def
        ! Too many }'s.

    fix: either bundle everything or nothing from the hyperref package

5.  Wrong test for pdftex, author needs to use ifpdf. Symptoms:

        ! Incomplete \ifnum; all text was ignored after line 13.
        <inserted text>

    any test for pdfoutput may fail, because it is typically incomplete
    unless ifpdf macro is used, a common signature is

        ! Undefined control sequence.
          ... \pdfannotlink

    fix: CTAN download ifpdf.sty which does the correct check

6.  Old JHEP.cls will not work, use recent JHEP3 instead.

    fix: don't use or include JHEP.cls, use latest JHEP3.cls or rely on
    arXiv's version.

7.  mn.sty and mn2e.cls (Monthly Notices of the Royal Society) will not
    work. We don't have a fix yet, comments or suggestions to www-admin.
