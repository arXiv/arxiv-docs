# References to and in arXiv Documents

## References to arXiv Documents

You should use references of the form:

  - `arXiv:YYMM.NNNNv# [category]` for new paper identifiers (April 2007
    onward), e.g.  
    `arXiv:0706.1234v1 [math.FA]`.

  - `arXiv:arch-ive/YYMMNNNv#` or `arXiv:arch-ive/YYMMNNNv# [category]`
    for papers submitted before April 2007. The second form should be
    used for archives that have subject classes (`math.XX`, `cs.XX`
    etc.), e.g.  
    `arXiv:hep-th/9901001v3`  
    or  
    `arXiv:math/9910001v1 [math.AT]`.

- For information regarding arXiv’s automatic DOI assignment to papers, see [Understanding arXiv's Assigned DOI's](../doi.md)

These forms are shown on the abstract web pages labeled `Cite as:`, and
the identifier part is linked to the correct URL for the abstract page.

If you include the specific version number as above then when someone
follows your reference to an arXiv paper they will see the specific
version intended (they will also see whether a new version has since
been submitted, e.g. `arXiv:hep-th/9901001v2`). If you wish to be less
specific, you may omit the explicit version number by omitting the `v#`
part of the identifier in which case the latest version will be shown,
for example:

  - `arXiv:0706.1234 [math.FA]`
  - `arXiv:hep-th/9910001`

There should not be any spaces or punctuation other than as shown above.
We encourage the inclusion of the primary subject area in square
brackets after references to papers with new identifiers; this isn't
necessary to identify the paper but may help readers understand a
citation more easily.

In TeX/LaTeX source these identifiers should not be split up with
typeface specifications and such. For example, it is fine to use:

  - `{\tt arXiv:0706.1234 [math.FA]}`
  - `{\tt arXiv:hep-th/9910001}`

but **do not use**:

  - `arXiv:{\tt 0706.1234 [math.FA]}`
  - `arXiv:{\tt hep-th/9910001}`

The motivation for this is that by keeping the identifier as one
contiguous string it may be automatically recognized for linking and
citation extraction.

*Note:* Identifiers should not be immediately preceded by "{". It is
fine to use:

  - `{\tt arXiv:0706.1234 [math.FA]}`

but **do not use**:

  - `\texttt{arXiv:0706.1234 [math.FA]}`

## References in arXiv Documents

References to other arXiv documents should include the arXiv identifier
in the format given above. References to other material should follow
normal conventions and provide an unambiguous way for readers to locate
the material referred to.

In fields covered by [INSPIRE](http://inspirehep.net/), we encourage
authors submitting LaTeX to use the [LaTeX or BibTeX output from
INSPIRE](http://inspirehep.net/info/faq/references_citations?ln=en#ensure_full_reference_extraction).
This not only provides a quick and convenient way to get the citation
information, but ensures that the references in your article can be
extracted cleanly by INSPIRE. For an explicit listing of the fields 
covered by INSPIRE, please see [their info page](http://inspirehep.net/info/hep/collection-policy) on this topic. 

See also the notes in our [TeX submission help](../../help/submit_tex.md#refs).

## Supplying a Publication Reference for an arXiv Document

To supply an alternate publication reference for an arXiv article (in a
paper journal, for example) you should use the `Journal-ref` and/or
`DOI` fields. A `Journal-ref` should contain full publication
information, including page number, without any additional comments. A
`DOI` will have the form `10.NNNN/some-string` and will be hyperlinked
when presented on arXiv pages. These fields may be added to an arXiv
document at any time after initial acceptance, see [To add a journal
reference, DOI or report number to an article](../../help/jref.md).
