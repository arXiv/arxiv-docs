# Proprietary fonts and/or their free equivalents

arXiv's TeX installation does not have any proprietary fonts. Only fonts
which are available at no charge and with non-restrictive licenses can
be used within arXiv's TeX system.

There are partial solutions for some popular fonts, in particular some
from Adobe, either via use of free subsets thereof, via substitutions,
or via a combination of both. This applies in particular to Minion Pro,
Myriad Pro, Utopia, Garamond, and possibly others.

## MinonPro Fonts

Update: Due to lack of demand in the past 3 years we do no longer
support MinionPro. arxiv switched to a **texlive 2009** based system on
12/31/2009 and MinionPro is not part of texlive.

Old News: arXiv does support the base set of MinionPro fonts, i.e. the
**Regular**, **Italic**, **Bold**, and **BoldItalic** shapes, however
the "semi", "mid", or "optical" shapes are not available. Thus in
particular the class option `[opticals]` is not supported at arXiv.

See <http://www.ctan.org/tex-archive/fonts/minionpro/> for more details.
