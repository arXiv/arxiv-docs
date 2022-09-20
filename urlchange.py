"""Script to alter the links in the markdown files to go from
`membership` to be absolute links md files like `/about/membership.md`.

This is used with the mkdocs plugin `abs-to-rel` so these become
relative links in the HTML.

The goal here is to facilitate easy .md link editing. To make a link
just use the full path below `docs` as it appers in your file
system. Ex. `/about/reports/2010_usage.md` or `/corr/index.md`. Do not
use relative link.

There is no need to add `../` to link to content in parent
directories. There is no need to consider how the name of the file
you'd like to link to need to be changed, `reports`, `reports.html`,
or `reports/index.html`.

Links to non-arXiv or `arxiv.org` pages outside of docs, use URLs with
protocols and domain names.  Ex. `https://home.cern/cheeses`

"""
from os import environ
from pathlib import PurePath
import sys
from collections import defaultdict
import glob
import re
from functools import reduce
from dataclasses import dataclass
from os.path import commonpath


arxiv = 'https://arxiv.org'


# MD files in docs. Created with find -f
# This is the list of files to scan for links and alter
mdfiles = [
"source/labs/criteria.md",
"source/labs/project-proposal.md",
"source/labs/index.md",
"source/labs/showcase.md",
"source/index.md",
"source/corr/subjectclasses.md",
"source/corr/index.md",
"source/new/nlin.md",
"source/new/94-96.md",
"source/new/index.md",
"source/new/econ_announce.md",
"source/new/math.md",
"source/new/condreorg.md",
"source/new/q-fin_announce.md",
"source/new/nlinsub.md",
"source/new/91-94.md",
"source/new/eess_announce.md",
"source/new/q-bio_announce.md",
"source/new/stat_announce.md",
"source/help/authority.md",
"source/help/otherformats.md",
"source/help/config_browser.md",
"source/help/toc.md",
"source/help/submit_index.md",
"source/help/misuse.md",
"source/help/trackback.md",
"source/help/unpack.md",
"source/help/moderation/index.md",
"source/help/moderation/appeals.md",
"source/help/statistics/index.md",
"source/help/orcid.md",
"source/help/license/index.md",
"source/help/license/reuse.md",
"source/help/passwords.md",
"source/help/bib_feed.md",
"source/help/submit_ps.md",
"source/help/bulk_data.md",
"source/help/api/index.md",
"source/help/api/user-manual.md",
"source/help/api/tou.md",
"source/help/api/classify.md",
"source/help/api/faq.md",
"source/help/api/basics.md",
"source/help/policies/index.md",
"source/help/policies/code_of_conduct_enforcement.md",
"source/help/policies/instructions_for_submission.md",
"source/help/policies/submission_agreement.md",
"source/help/policies/privacy_policy.md",
"source/help/policies/code_of_conduct.md",
"source/help/ssl.md",
"source/help/index.md",
"source/help/pstypeI.md",
"source/help/email-protection.md",
"source/help/stats/2017_by_area/index.md",
"source/help/stats/2013_by_area/index.md",
"source/help/stats/index.md",
"source/help/stats/2018_by_area/index.md",
"source/help/stats/2014_by_area/index.md",
"source/help/stats/2016_by_area/index.md",
"source/help/stats/2015_by_area/index.md",
"source/help/stats/2019_by_area/index.md",
"source/help/stats/2012_by_area/index.md",
"source/help/registerhelp.md",
"source/help/accesskeys.md",
"source/help/pscm.md",
"source/help/sizes.md",
"source/help/support.md",
"source/help/q-bio/index.md",
"source/help/math/index.md",
"source/help/submission-policy.md",
"source/help/type1linux.md",
"source/help/submit_status.md",
"source/help/not-registered.md",
"source/help/myarticles.md",
"source/help/submit_html.md",
"source/help/submit_tex.md",
"source/help/my_arxiv.md",
"source/help/web_accessibility.md",
"source/help/pdf.md",
"source/help/bulk_data_s3.md",
"source/help/mirrors.md",
"source/help/hypertex/extensions.md",
"source/help/hypertex/index.md",
"source/help/hypertex/binaries/index.md",
"source/help/hypertex/bibstyles/index.md",
"source/help/hypertex/bugs.md",
"source/help/hypertex/X/index.md",
"source/help/whytex.md",
"source/help/robots.md",
"source/help/mathjax.md",
"source/help/sciencewise.md",
"source/help/myarticles_ex2.md",
"source/help/openurl.md",
"source/help/replace.md",
"source/help/terms_of_submission.md",
"source/help/primer.md",
"source/help/ancillary_files.md",
"source/help/general.md",
"source/help/ir.md",
"source/help/submit_pdf.md",
"source/help/cross.md",
"source/help/tex.md",
"source/help/find.md",
"source/help/translations.md",
"source/help/q-fin/index.md",
"source/help/q-fin/announcement.md",
"source/help/overlap.md",
"source/help/author_identifiers.md",
"source/help/physics/index.md",
"source/help/withdraw.md",
"source/help/tar.md",
"source/help/econ/index.md",
"source/help/econ/announcement.md",
"source/help/endorsement.md",
"source/help/gzip.md",
"source/help/donate.md",
"source/help/versions.md",
"source/help/third_party_submission.md",
"source/help/prep.md",
"source/help/view.md",
"source/help/announcement.md",
"source/help/jref.md",
"source/help/ps.md",
"source/help/macro_list.md",
"source/help/faq/texlive.md",
"source/help/faq/freefonts.md",
"source/help/faq/feynmf.md",
"source/help/faq/landscape.md",
"source/help/faq/browsergunzip.md",
"source/help/faq/today.md",
"source/help/faq/mistakes.md",
"source/help/faq/references.md",
"source/help/faq/amslatex2000.md",
"source/help/faq/textures.md",
"source/help/faq/statfaq.md",
"source/help/faq/dvips.md",
"source/help/faq/index.md",
"source/help/faq/doublesubscript.md",
"source/help/faq/cache.md",
"source/help/faq/whytex.md",
"source/help/faq/revtex.md",
"source/help/faq/psbad.md",
"source/help/faq/srcfaq.md",
"source/help/faq/psjunk.md",
"source/help/faq/texprobs.md",
"source/help/faq/pstricks.md",
"source/help/faq/aaclass.md",
"source/help/faq/whynostamp.md",
"source/help/faq/pdfrotate.md",
"source/help/faq/texhyphenation.md",
"source/help/faq/pd1enc.md",
"source/help/faq/tetex3.md",
"source/help/faq/multilang.md",
"source/help/faq/citelinks.md",
"source/help/submit.md",
"source/help/contact.md",
"source/help/eess/index.md",
"source/help/eess/announcement.md",
"source/help/psvariants.md",
"source/help/arxiv_identifier_for_services.md",
"source/help/mimetypes.md",
"source/help/bitmap/index.md",
"source/help/bitmap/procedure.md",
"source/help/bitmap/software.md",
"source/help/bitmap/advanced.md",
"source/help/bitmap/faq.md",
"source/help/bitmap/problems.md",
"source/help/oa/metadataPolicy.md",
"source/help/oa/dataPolicy.md",
"source/help/oa/index.md",
"source/help/oa/rfc1807.md",
"source/help/oa/sfc_oams.md",
"source/help/oa/sfc_data_provider.md",
"source/help/oa/arXiv_meta_format.md",
"source/help/arxiv_identifier.md",
"source/help/utilities.md",
"source/help/00README.md",
"source/help/datasets.md",
"source/help/subscribe.md",
"source/help/data_conservancy.md",
"source/help/semanticscholar.md",
"source/help/availability.md",
"source/help/rss.md",
"source/help/submit_sword.md",
"source/about/give.md",
"source/about/brand.md",
"source/about/governance.md",
"source/about/reports/2012_usage.md",
"source/about/reports/2020_institution_downloads.md",
"source/about/reports/2019_usage.md",
"source/about/reports/arxiv_busplan_Jan2012.md",
"source/about/reports/2020_usage.md",
"source/about/reports/2020_institution_submissions.md",
"source/about/reports/2021_institution_submissions.md",
"source/about/reports/2014_usage.md",
"source/about/reports/2019_update.md",
"source/about/reports/2020_downloads_top_250_institutions.md",
"source/about/reports/2020_institution_downloads_by_year.md",
"source/about/reports/2021_usage.md",
"source/about/reports/2016_usage.md",
"source/about/reports/2011_supporters.md",
"source/about/reports/index.md",
"source/about/reports/2010_usage.md",
"source/about/reports/arxiv_busplan_Apr2011.md",
"source/about/reports/2011_usage.md",
"source/about/reports/2013_usage.md",
"source/about/reports/2020_update.md",
"source/about/reports/2020_institution_downloads_by_archive.md",
"source/about/reports/whitepaper.md",
"source/about/reports/arxiv_busplan_July2011.md",
"source/about/reports/2015_usage.md",
"source/about/reports/2018_usage.md",
"source/about/reports/2019_roadmap.md",
"source/about/reports/arxiv_busplan_Oct2011.md",
"source/about/reports/2010_supporters.md",
"source/about/reports/2020_roadmap.md",
"source/about/reports/arxiv_busplan_Dec2010.md",
"source/about/reports/arxiv_busplan_July2010.md",
"source/about/reports/2012_supporters.md",
"source/about/reports/2017_usage.md",
"source/about/reports/submission_category_by_year.md",
"source/about/reports/sustainability_advisory_group.md",
"source/about/reports/2009_usage.md",
"source/about/index.md",
"source/about/reports-financials.md",
"source/about/membership.md",
"source/about/supporters.md",
"source/about/email_sign_up.md",
"source/about/brand_use.md",
"source/about/support_confirm.md",
"source/about/accessibility.md",
"source/about/mab_bylaws.md",
"source/about/principles.md",
"source/about/user-testing-api.md",
"source/about/donate.md",
"source/about/user-testing.md",
"source/about/membership_confirm.md",
"source/about/people/scientific_ad_board.md",
"source/about/people/index.md",
"source/about/people/technical_ad_group.md",
"source/about/people/leadership_team.md",
"source/about/people/member_ad_board.md",
"source/about/people/staff.md",
"source/about/people/developers.md",
"source/about/sab_bylaws.md",
"source/about/ourmembers.md",
"source/about/funding.md",
]

# Files generated by mkdocs. Created by doing mkdocs build then find -f in the site directory.
paths_in_docs = [
    "/hypertex/extensions.html",
    "/hypertex/bugs.html",
    "/hypertex/index.html",
    "/sitemap.xml.gz",
    "/corr/subjectclasses.html",
    "/corr/home.html",
    "/corr/index.html",
    "/corr/advisorycommittee.html",
    "/search.html",
    "/about/sab_bylaws.html",
    "/about/images/arxiv_roles-respns.jpeg",
    "/about/images/jim.jpg",
    "/about/images/eleonora.jpg",
    "/about/images/logo_mps.png",
    "/about/images/erick.jpg",
    "/about/images/martin.jpg",
    "/about/images/alison.jpg",
    "/about/images/janelle.jpg",
    "/about/images/ohio-state-logo.png",
    "/about/images/orcid_32x32.png",
    "/about/images/logo-aps.gif",
    "/about/images/eleanora.jpg",
    "/about/images/arxiv_org_chart.jpeg",
    "/about/images/oya.jpg",
    "/about/images/org_governance.jpeg",
    "/about/images/steinn.jpg",
    "/about/give.html",
    "/about/reports/2018_usage.html",
    "/about/reports/2016_usage.html",
    "/about/reports/2012_usage.html",
    "/about/reports/arXivfive-yearmemberpledges-August2016.pdf",
    "/about/reports/2015_usage.html",
    "/about/reports/2018_CY_arXiv_budget.pdf",
    "/about/reports/2010_CY_arXiv_budget.pdf",
    "/about/reports/2019_usage.html",
    "/about/reports/2013_usage.html",
    "/about/reports/arxiv_busplan_July2011.html",
    "/about/reports/arXivfive-yearmemberpledges-Jan2014.pdf",
    "/about/reports/arXiv_update_January_2014.pdf",
    "/about/reports/arXivfive-yearmemberpledges-Dec2017.pdf",
    "/about/reports/arXiv_update_January_2016.pdf",
    "/about/reports/arXivfive-yearmemberpledges-March2015.pdf",
    "/about/reports/arxiv_busplan_Jan2012.html",
    "/about/reports/2011_CY_arXiv_budget.pdf",
    "/about/reports/2019_supporters_Dec.pdf",
    "/about/reports/arxiv_busplan_Oct2011.html",
    "/about/reports/2014_CY_arXiv_budget.pdf",
    "/about/reports/arXivfive-yearmemberpledges-Feb2017.pdf",
    "/about/reports/2017_CY_arXiv_budget.pdf",
    "/about/reports/2019_supporters_July.pdf",
    "/about/reports/2014_usage.html",
    "/about/reports/2014_roadmap.pdf",
    "/about/reports/2012_supporters.html",
    "/about/reports/2010_supporters.html",
    "/about/reports/2017_usage.html",
    "/about/reports/2011_supporters.html",
    "/about/reports/arXiv_Reserve_Funds_Policy.pdf",
    "/about/reports/arxiv_busplan_July2010.html",
    "/about/reports/2019_roadmap.html",
    "/about/reports/whitepaper.html",
    "/about/reports/2011_usage.html",
    "/about/reports/arXivfive-yearmemberpledges-May2017.pdf",
    "/about/reports/index.html",
    "/about/reports/2016_roadmap.pdf",
    "/about/reports/2010_usage.html",
    "/about/reports/arxiv_busplan_Dec2010.html",
    "/about/reports/2016_UserSurveyReport.pdf",
    "/about/reports/2015_CY_arXiv_budget.pdf",
    "/about/reports/arXiv_update_January_2018.pdf",
    "/about/reports/arXivfive-yearmemberpledges-May2018.pdf",
    "/about/reports/2009_usage.html",
    "/about/reports/sustainability_advisory_group.html",
    "/about/reports/arXivfive-yearmemberpledges-January2016.pdf",
    "/about/reports/arxiv_busplan_Apr2011.html",
    "/about/reports/2018_roadmap.pdf",
    "/about/reports/2013_CY_arXiv_budget.pdf",
    "/about/reports/2012_CY_arXiv_budget.pdf",
    "/about/reports/2017_roadmap.pdf",
    "/about/reports/2020_roadmap.html",
    "/about/reports/arXivfive-yearmemberpledges-August2015.pdf",
    "/about/reports/arXivfive-yearmemberpledges-Jan2015.pdf",
    "/about/reports/2016_CY_arXiv_budget.pdf",
    "/about/reports/arXiv_update_January_2015.pdf",
    "/about/reports/2019_update.html",
    "/about/reports/arXiv_CY19_midyear.pdf",
    "/about/reports/arXiv_update_January_2017.pdf",
    "/about/reports/2013_roadmap.pdf",
    "/about/reports/arXivfive-yearmemberpledges-December2016.pdf",
    "/about/reports/2020_update.html",
    "/about/ourmembers.html",
    "/about/principles.html",
    "/about/reports-financials.html",
    "/about/people/scientific_ad_board.html",
    "/about/people/staff.html",
    "/about/people/leadership_team.html",
    "/about/people/index.html",
    "/about/people/developers.html",
    "/about/people/technical_ad_group.html",
    "/about/people/member_ad_board.html",
    "/about/governance.html",
    "/about/donate.html",
    "/about/index.html",
    "/about/mab_bylaws.html",
    "/about/user-testing.html",
    "/about/membership.html",
    "/about/user-testing-api.html",
    "/about/accessibility.html",
    "/help/submit_pdf.html",
    "/help/hypertex/emdual.tar.gz",
    "/help/hypertex/hharvsamp.tex",
    "/help/hypertex/binaries/xhdvi_iris_5.2.tar.gz",
    "/help/hypertex/binaries/index.html",
    "/help/hypertex/binaries/xhdvi_hpux_9.05.tar.gz",
    "/help/hypertex/binaries/xhdvi_sun_4.1.tar.gz",
    "/help/hypertex/lanlmac.tex",
    "/help/hypertex/extensions.html",
    "/help/hypertex/test.ps",
    "/help/hypertex/pdfcomments.txt",
    "/help/hypertex/xhdvi_0.6.tar.gz",
    "/help/hypertex/link.ps",
    "/help/hypertex/bugs.html",
    "/help/hypertex/wcf_final.ps",
    "/help/hypertex/hypertasi92.tar.gz",
    "/help/hypertex/xhdvi_0.4c.tar.gz",
    "/help/hypertex/index.html",
    "/help/hypertex/link.dvi",
    "/help/hypertex/link.pdf",
    "/help/hypertex/HyperTeXview.tar.gz",
    "/help/hypertex/xhdvi_0.5a.tar.gz",
    "/help/hypertex/hypertex.gif",
    "/help/hypertex/hharvsamp.dvi",
    "/help/hypertex/bibstyles/hapj.bst",
    "/help/hypertex/bibstyles/halpha.bst",
    "/help/hypertex/bibstyles/hieeetr.bst",
    "/help/hypertex/bibstyles/hunsrt.bst",
    "/help/hypertex/bibstyles/Makefile",
    "/help/hypertex/bibstyles/hunsrtnat.bst",
    "/help/hypertex/bibstyles/hacm.bst",
    "/help/hypertex/bibstyles/kp.bst",
    "/help/hypertex/bibstyles/h-physrev.bst",
    "/help/hypertex/bibstyles/hplainyr.bst",
    "/help/hypertex/bibstyles/habbrv.bst",
    "/help/hypertex/bibstyles/index.html",
    "/help/hypertex/bibstyles/junk/utcaps.bst",
    "/help/hypertex/bibstyles/junk/utphys.bst",
    "/help/hypertex/bibstyles/bibstyles.tar.gz",
    "/help/hypertex/bibstyles/hep.bst",
    "/help/hypertex/bibstyles/hapalike.bst",
    "/help/hypertex/bibstyles/h-elsevier.bst",
    "/help/hypertex/bibstyles/hplain.bst",
    "/help/hypertex/bibstyles/hsiam.bst",
    "/help/hypertex/hypertex.css",
    "/help/hypertex/sources/dvihpsk.tar.gz",
    "/help/hypertex/sources/gv1.5gs5.50hack.tar.gz",
    "/help/hypertex/sources/macros/cites.hty",
    "/help/hypertex/sources/macros/hyperncwebmac.tex",
    "/help/hypertex/sources/macros/book.hty",
    "/help/hypertex/sources/macros/espart.hty",
    "/help/hypertex/sources/macros/ichep.hty",
    "/help/hypertex/sources/macros/aaspp4.hty",
    "/help/hypertex/sources/macros/vanilla.hty",
    "/help/hypertex/sources/macros/espcrc2.hty",
    "/help/hypertex/sources/macros/amsart.hty",
    "/help/hypertex/sources/macros/article.hty",
    "/help/hypertex/sources/macros/amsart11.hty",
    "/help/hypertex/sources/macros/report.hty",
    "/help/hypertex/sources/macros/hlatex.tex",
    "/help/hypertex/sources/macros/citesort.hty",
    "/help/hypertex/sources/macros/lsalike.hty",
    "/help/hypertex/sources/macros/laa.hty",
    "/help/hypertex/sources/macros/amsbook.hty",
    "/help/hypertex/sources/macros/cite.hty",
    "/help/hypertex/sources/macros/named.hty",
    "/help/hypertex/sources/macros/aasms.hty",
    "/help/hypertex/sources/macros/aasms4.hty",
    "/help/hypertex/sources/macros/aaspp.hty",
    "/help/hypertex/sources/macros/rangecite.hty",
    "/help/hypertex/sources/macros/aaspptwo.hty",
    "/help/hypertex/sources/macros/elsart.hty",
    "/help/hypertex/sources/macros/revtex.hty",
    "/help/hypertex/sources/macros/hyperwebmac.tex",
    "/help/hypertex/sources/macros/hyperlatex.tex",
    "/help/hypertex/sources/macros/prabib.old.hty",
    "/help/hypertex/sources/macros/prabib.hty",
    "/help/hypertex/sources/macros/prbbib.hty",
    "/help/hypertex/sources/macros/world_sci.hty",
    "/help/hypertex/sources/macros/fleqn.hty",
    "/help/hypertex/sources/macros/ioplppt.hty",
    "/help/hypertex/sources/macros/amsart12.hty",
    "/help/hypertex/sources/macros/hypercwebmac.tex",
    "/help/hypertex/sources/macros/aps.hty",
    "/help/hypertex/sources/macros/hypertest.tex",
    "/help/hypertex/sources/macros/hyperbasics.tex",
    "/help/hypertex/sources/macros/ijcai95.hty",
    "/help/hypertex/hyperlh88.tar.gz",
    "/help/hypertex/X/Mosaic",
    "/help/hypertex/X/index.html",
    "/help/hypertex/X/newpg.c",
    "/help/hypertex/X/callmosaic",
    "/help/hypertex/dospecial.c",
    "/help/whytex.html",
    "/help/contact.html",
    "/help/eess.html",
    "/help/ancillary_files.html",
    "/help/versions.html",
    "/help/scientific_ad_board.html",
    "/help/submit.html",
    "/help/announcement.html",
    "/help/ssl.html",
    "/help/orcid.html",
    "/help/faq/whytex.html",
    "/help/faq/texhyphenation.html",
    "/help/faq/doublesubscript.html",
    "/help/faq/psbad.html",
    "/help/faq/textures.html",
    "/help/faq/freefonts.html",
    "/help/faq/statfaq.html",
    "/help/faq/aaclass.html",
    "/help/faq/pstricks.html",
    "/help/faq/cache.html",
    "/help/faq/today.html",
    "/help/faq/mistakes.html",
    "/help/faq/wget_patch.txt",
    "/help/faq/browsergunzip.html",
    "/help/faq/texprobs.html",
    "/help/faq/arXiv-texsize.ps.gz",
    "/help/faq/squid.conf",
    "/help/faq/texlive.html",
    "/help/faq/feynmf.html",
    "/help/faq/doublesubscript.png",
    "/help/faq/references.html",
    "/help/faq/citelinks.html",
    "/help/faq/index.html",
    "/help/faq/pd1enc.html",
    "/help/faq/landscape.html",
    "/help/faq/daily.sh",
    "/help/faq/multilang.html",
    "/help/faq/whynostamp.html",
    "/help/faq/srcfaq.html",
    "/help/faq/revtex.html",
    "/help/faq/amslatex2000.html",
    "/help/faq/tetex3.html",
    "/help/faq/psjunk.html",
    "/help/faq/dvips.html",
    "/help/faq/pdfrotate.html",
    "/help/faq/bulk_data_s3_patch.txt",
    "/help/gzip.html",
    "/help/trackback.html",
    "/help/api/faq.html",
    "/help/api/arXiv_api_xml.png",
    "/help/api/user-manual.html",
    "/help/api/tou.html",
    "/help/api/examples/perl_arXiv_simple_example.txt",
    "/help/api/examples/python_arXiv_simple_example.txt",
    "/help/api/examples/ruby_arXiv_paging_example.txt",
    "/help/api/examples/perl_arXiv_paging_example.txt",
    "/help/api/examples/ruby_arXiv_parsing_example.txt",
    "/help/api/examples/python_arXiv_paging_example.txt",
    "/help/api/examples/php_arXiv_simple_example.txt",
    "/help/api/examples/php_arXiv_paging_example.txt",
    "/help/api/examples/python_arXiv_parsing_example.txt",
    "/help/api/examples/php_arXiv_parsing_example.txt",
    "/help/api/examples/perl_arXiv_parsing_example.txt",
    "/help/api/examples/ruby_arXiv_simple_example.txt",
    "/help/api/index.html",
    "/help/api/arXiv_smiley.png",
    "/help/api/classify.html",
    "/help/support.html",
    "/help/scientific_ad_board",
    "/help/robots.html",
    "/help/macro_list.html",
    "/help/econ/announcement.html",
    "/help/econ/index.html",
    "/help/general.html",
    "/help/translations.html",
    "/help/rss.html",
    "/help/terms_of_submission.html",
    "/help/datasets.html",
    "/help/submit_html.html",
    "/help/utilities.html",
    "/help/bib_feed.html",
    "/help/accesskeys.html",
    "/help/email-protection.html",
    "/help/sciencewise.html",
    "/help/tex.html",
    "/help/bulk_data.html",
    "/help/bitmap/faq.html",
    "/help/bitmap/advanced.html",
    "/help/bitmap/index.html",
    "/help/bitmap/software.html",
    "/help/bitmap/problems.html",
    "/help/bitmap/procedure.html",
    "/help/pdf.html",
    "/help/moderation.html",
    "/help/ps.html",
    "/help/math/index.html",
    "/help/sizes.html",
    "/help/authority.html",
    "/help/submit_status.html",
    "/help/type1linux.html",
    "/help/withdrawal-examplev2.png",
    "/help/psvariants.html",
    "/help/mimetypes.html",
    "/help/endorsement.html",
    "/help/withdraw.html",
    "/help/q-fin/announcement.html",
    "/help/q-fin/index.md~",
    "/help/q-fin/index.html",
    "/help/submission-policy.html",
    "/help/withdrawal-examplev1.png",
    "/help/openurl.html",
    "/help/arxiv_identifier.html",
    "/help/web_accessibility.html",
    "/help/announcement.md~",
    "/help/semanticscholar.html",
    "/help/submit_ps.html",
    "/help/donate.html",
    "/help/index.html",
    "/help/mirrors.html",
    "/help/registerhelp.html",
    "/help/oa/sfc_oams.html",
    "/help/oa/sfc_data_provider.html",
    "/help/oa/arXiv_meta_format.html",
    "/help/oa/index.html",
    "/help/oa/metadataPolicy.html",
    "/help/oa/rfc1807.html",
    "/help/oa/dataPolicy.html",
    "/help/arxiv_identifier_for_services.html",
    "/help/unpack.html",
    "/help/q-bio/index.html",
    "/help/find.html",
    "/help/mathjax.html",
    "/help/00README.html",
    "/help/myarticles.html",
    "/help/not-registered.html",
    "/help/tar.html",
    "/help/jref.html",
    "/help/my_arxiv.html",
    "/help/toc.html",
    "/help/license.html",
    "/help/submit_index.html",
    "/help/submit_sword.html",
    "/help/submit_tex.html",
    "/help/pstypeI.html",
    "/help/pscm.html",
    "/help/third_party_submission.html",
    "/help/view.html",
    "/help/bulk_data_s3.html",
    "/help/statistics/index.html",
    "/help/cross.html",
    "/help/config_browser.html",
    "/help/otherformats.html",
    "/help/overlap.html",
    "/help/ir.html",
    "/help/eess/announcement.html",
    "/help/eess/announcement.md~",
    "/help/eess/index.html",
    "/help/author_identifiers.html",
    "/help/physics/index.html",
    "/help/myarticles_ex2.html",
    "/help/prep.html",
    "/help/policies/privacy_policy.html",
    "/help/policies/code_of_conduct.html",
    "/help/policies/index.md~",
    "/help/policies/submission_agreement.html",
    "/help/policies/index.html",
    "/help/policies/instructions_for_submission.html",
    "/help/primer.html",
    "/help/passwords.html",
    "/help/subscribe.html",
    "/help/data_conservancy.html",
    "/help/stats/2018_by_area/math_yearly.png",
    "/help/stats/2018_by_area/cond-mat_yearly.png",
    "/help/stats/2018_by_area/nucl_yearly.png",
    "/help/stats/2018_by_area/nlin_yearly.png",
    "/help/stats/2018_by_area/newsubs.png",
    "/help/stats/2018_by_area/gr-qc_yearly.png",
    "/help/stats/2018_by_area/stat_yearly.png",
    "/help/stats/2018_by_area/eess_yearly.png",
    "/help/stats/2018_by_area/phys_yearly.png",
    "/help/stats/2018_by_area/hep_yearly.png",
    "/help/stats/2018_by_area/cs_yearly.png",
    "/help/stats/2018_by_area/econ_yearly.png",
    "/help/stats/2018_by_area/q-bio_yearly.png",
    "/help/stats/2018_by_area/index.html",
    "/help/stats/2018_by_area/q-fin_yearly.png",
    "/help/stats/2018_by_area/physics_yearly.pdf",
    "/help/stats/2018_by_area/quant-ph_gr-qc_yearly.png",
    "/help/stats/2018_by_area/astro-ph_yearly.png",
    "/help/stats/2018_by_area/cumsubs.png",
    "/help/stats/2018_by_area/physics_yearly.png",
    "/help/stats/2018_by_area/quant-ph_yearly.png",
    "/help/stats/2014_by_area/math_yearly.png",
    "/help/stats/2014_by_area/cond-mat_yearly.png",
    "/help/stats/2014_by_area/nucl_yearly.png",
    "/help/stats/2014_by_area/nlin_yearly.png",
    "/help/stats/2014_by_area/newsubs.png",
    "/help/stats/2014_by_area/gr-qc_yearly.png",
    "/help/stats/2014_by_area/stat_yearly.png",
    "/help/stats/2014_by_area/hep_yearly.png",
    "/help/stats/2014_by_area/cs_yearly.png",
    "/help/stats/2014_by_area/q-bio_yearly.png",
    "/help/stats/2014_by_area/index.html",
    "/help/stats/2014_by_area/q-fin_yearly.png",
    "/help/stats/2014_by_area/astro-ph_yearly.png",
    "/help/stats/2014_by_area/cumsubs.png",
    "/help/stats/2014_by_area/physics_yearly.png",
    "/help/stats/2014_by_area/quant-ph_yearly.png",
    "/help/stats/2013_by_area/math_yearly.png",
    "/help/stats/2013_by_area/cond-mat_yearly.png",
    "/help/stats/2013_by_area/nucl_yearly.png",
    "/help/stats/2013_by_area/nlin_yearly.png",
    "/help/stats/2013_by_area/newsubs.png",
    "/help/stats/2013_by_area/gr-qc_yearly.png",
    "/help/stats/2013_by_area/stat_yearly.png",
    "/help/stats/2013_by_area/hep_yearly.png",
    "/help/stats/2013_by_area/cs_yearly.png",
    "/help/stats/2013_by_area/q-bio_yearly.png",
    "/help/stats/2013_by_area/index.html",
    "/help/stats/2013_by_area/q-fin_yearly.png",
    "/help/stats/2013_by_area/astro-ph_yearly.png",
    "/help/stats/2013_by_area/cumsubs.png",
    "/help/stats/2013_by_area/physics_yearly.png",
    "/help/stats/2013_by_area/quant-ph_yearly.png",
    "/help/stats/2012_by_area/math_yearly.png",
    "/help/stats/2012_by_area/cond-mat_yearly.png",
    "/help/stats/2012_by_area/nucl_yearly.png",
    "/help/stats/2012_by_area/nlin_yearly.png",
    "/help/stats/2012_by_area/newsubs.png",
    "/help/stats/2012_by_area/gr-qc_yearly.png",
    "/help/stats/2012_by_area/stat_yearly.png",
    "/help/stats/2012_by_area/hep_yearly.png",
    "/help/stats/2012_by_area/cs_yearly.png",
    "/help/stats/2012_by_area/q-bio_yearly.png",
    "/help/stats/2012_by_area/index.html",
    "/help/stats/2012_by_area/q-fin_yearly.png",
    "/help/stats/2012_by_area/astro-ph_yearly.png",
    "/help/stats/2012_by_area/cumsubs.png",
    "/help/stats/2012_by_area/physics_yearly.png",
    "/help/stats/2012_by_area/quant-ph_yearly.png",
    "/help/stats/index.html",
    "/help/stats/2017_by_area/math_yearly.png",
    "/help/stats/2017_by_area/cond-mat_yearly.png",
    "/help/stats/2017_by_area/nucl_yearly.png",
    "/help/stats/2017_by_area/nlin_yearly.png",
    "/help/stats/2017_by_area/newsubs.png",
    "/help/stats/2017_by_area/stat_yearly.png",
    "/help/stats/2017_by_area/hep_yearly.png",
    "/help/stats/2017_by_area/cs_yearly.png",
    "/help/stats/2017_by_area/q-bio_yearly.png",
    "/help/stats/2017_by_area/index.html",
    "/help/stats/2017_by_area/q-fin_yearly.png",
    "/help/stats/2017_by_area/quant-ph_gr-qc_yearly.png",
    "/help/stats/2017_by_area/astro-ph_yearly.png",
    "/help/stats/2017_by_area/cumsubs.png",
    "/help/stats/2017_by_area/physics_yearly.png",
    "/help/stats/2015_by_area/math_yearly.png",
    "/help/stats/2015_by_area/cond-mat_yearly.png",
    "/help/stats/2015_by_area/nucl_yearly.png",
    "/help/stats/2015_by_area/nlin_yearly.png",
    "/help/stats/2015_by_area/newsubs.png",
    "/help/stats/2015_by_area/gr-qc_yearly.png",
    "/help/stats/2015_by_area/stat_yearly.png",
    "/help/stats/2015_by_area/hep_yearly.png",
    "/help/stats/2015_by_area/cs_yearly.png",
    "/help/stats/2015_by_area/q-bio_yearly.png",
    "/help/stats/2015_by_area/index.html",
    "/help/stats/2015_by_area/q-fin_yearly.png",
    "/help/stats/2015_by_area/astro-ph_yearly.png",
    "/help/stats/2015_by_area/cumsubs.png",
    "/help/stats/2015_by_area/physics_yearly.png",
    "/help/stats/2015_by_area/quant-ph_yearly.png",
    "/help/stats/2016_by_area/math_yearly.png",
    "/help/stats/2016_by_area/cond-mat_yearly.png",
    "/help/stats/2016_by_area/nucl_yearly.png",
    "/help/stats/2016_by_area/nlin_yearly.png",
    "/help/stats/2016_by_area/newsubs.png",
    "/help/stats/2016_by_area/gr-qc_yearly.png",
    "/help/stats/2016_by_area/stat_yearly.png",
    "/help/stats/2016_by_area/hep_yearly.png",
    "/help/stats/2016_by_area/cs_yearly.png",
    "/help/stats/2016_by_area/q-bio_yearly.png",
    "/help/stats/2016_by_area/index.html",
    "/help/stats/2016_by_area/q-fin_yearly.png",
    "/help/stats/2016_by_area/astro-ph_yearly.png",
    "/help/stats/2016_by_area/cumsubs.png",
    "/help/stats/2016_by_area/physics_yearly.png",
    "/help/stats/2016_by_area/quant-ph_yearly.png",
    "/help/stats/#index.md#",
    "/help/stats/2019_by_area/math_yearly.png",
    "/help/stats/2019_by_area/cond-mat_yearly.png",
    "/help/stats/2019_by_area/nucl_yearly.png",
    "/help/stats/2019_by_area/nlin_yearly.png",
    "/help/stats/2019_by_area/newsubs.png",
    "/help/stats/2019_by_area/stat_yearly.png",
    "/help/stats/2019_by_area/eess_yearly.png",
    "/help/stats/2019_by_area/phys_yearly.png",
    "/help/stats/2019_by_area/hep_yearly.png",
    "/help/stats/2019_by_area/cs_yearly.png",
    "/help/stats/2019_by_area/econ_yearly.png",
    "/help/stats/2019_by_area/q-bio_yearly.png",
    "/help/stats/2019_by_area/index.html",
    "/help/stats/2019_by_area/q-fin_yearly.png",
    "/help/stats/2019_by_area/quant-ph_gr-qc_yearly.png",
    "/help/stats/2019_by_area/astro-ph_yearly.png",
    "/help/stats/2019_by_area/cumsubs.png",
    "/help/stats/2019_by_area/physics_yearly.png",
    "/help/misuse.html",
    "/help/replace.html",
    "/index.html",
    "/new/nlin.html",
    "/new/physics.html",
    "/new/stat.html",
    "/new/condreorg.html",
    "/new/nlinsub.html",
    "/new/math.html",
    "/new/q-bio.html",
    "/new/q-fin_announce.html",
    "/new/94-96.html",
    "/new/index.html",
    "/new/econ_announce.html",
    "/new/stat_announce.html",
    "/new/econ.html",
    "/new/q-bio_announce.html",
    "/new/eess_announce.html",
    "/new/91-94.html",
    "/css/brand_guide.css",
    "/sitemap.xml",
    "/brand/images/brand-icon-logos.jpg",
    "/brand/images/brand-swag-shirt-3.jpg",
    "/brand/images/brand-fonts-example-2.jpg",
    "/brand/images/brand-tagline-3.jpg",
    "/brand/images/Screen Shot 2022-03-23 at 2.35.52 PM.png",
    "/brand/images/brand-icon-typography.jpg",
    "/brand/images/brand-logo-primary.jpg",
    "/brand/images/brand-icon-images.jpg",
    "/brand/images/brand-logo-labs.jpg",
    "/brand/images/brand-image-colorized-salmon.jpg",
    "/brand/images/brand-fonts-example-5.jpg",
    "/brand/images/brand-icon-swag.jpg",
    "/brand/images/brand-logomark-primary.jpg",
    "/brand/images/brand-logo-primary-spacing.jpg",
    "/brand/images/brand-logomark-dark-mode.jpg",
    "/brand/images/brand-swag-card.jpg",
    "/brand/images/brand-logo-salmon.jpg",
    "/brand/images/brand-image-tagline.jpg",
    "/brand/images/brand-logo-check.jpg",
    "/brand/images/brand-image-illustration-4.jpg",
    "/brand/images/brand-tagline-1.jpg",
    "/brand/images/brand-icon-voice.jpg",
    "/brand/images/brand-fonts-freightsans.jpg",
    "/brand/images/brand-logo-dark-mode.jpg",
    "/brand/images/brand-image-illustration-3.jpg",
    "/brand/images/brand-fonts-freighttext.jpg",
    "/brand/images/brand-icon-quotes.jpg",
    "/brand/images/brand-swag-shirt-2.jpg",
    "/brand/images/brand-color-map.jpg",
    "/brand/images/brand-icon-fonts.jpg",
    "/brand/images/brand-fonts-example-1.jpg",
    "/brand/images/brand-logo-red.jpg",
    "/brand/images/brand-icon-guidelines.jpg",
    "/brand/images/brand-fonts-larabie.jpg",
    "/brand/images/brand-fonts-example-4.jpg",
    "/brand/images/brand-logomark-primary-large.jpg",
    "/brand/images/brand-tagline-2.jpg",
    "/brand/images/brand-swag-shirt-5.jpg",
    "/brand/images/brand-quotes-example-1.jpg",
    "/brand/images/brand-icon-tagline.jpg",
    "/brand/images/brand-logo-labs-spacing.jpg",
    "/brand/images/brand-image-illustration-6.jpg",
    "/brand/images/brand-logo-black.jpg",
    "/brand/images/brand-fonts-example-3.jpg",
    "/brand/images/brand-image-portrait.jpg",
    "/brand/images/brand-swag-stickers.jpg",
    "/brand/images/brand-tagline-header.jpg",
    "/brand/images/brand-swag-mug-2.jpg",
    "/brand/images/brand-icon-colors.jpg",
    "/brand/images/brand-swag-shirt-1.jpg",
    "/brand/images/brand-swag-mug.jpg",
    "/brand/images/brand-logomark-black.jpg",
    "/brand/images/brand-logomark-salmon.jpg",
    "/brand/images/brand-image-illustration-1.jpg",
    "/brand/images/brand-icon-pillars.jpg",
    "/brand/images/brand-color-contrast.jpg",
    "/brand/images/brand-swag-shirt-4.jpg",
    "/brand/images/sketch-abstract-concepts.jpg",
    "/brand/images/brand-swag-veni-vidi.jpg",
    "/brand/images/brand-color-contrast-largetype.jpg",
    "/brand/images/brand-image-illustration-5.jpg",
    "/brand/images/brand-fonts-IBM-plex.jpg",
    "/brand/images/brand-image-portrait-2.jpg",
    "/brand/images/brand-image-illustration-2.jpg",
    "/brand/images/brand-logomark-red.jpg",
    "/brand/images/brand-supergraphic.jpg",
    "/brand/quotes.html",
    "/brand/brand-guidelines.html",
    "/brand/voice.html",
    "/brand/typography.html",
    "/brand/_templates/brand/custom.html",
    "/brand/index.html",
    "/brand/brand-pillars.html",
    "/brand/colors.html",
    "/brand/tagline.html",
    "/brand/fonts.html",
    "/brand/swag.html",
    "/brand/logos.html",
    "/brand/images.html",
    "/search/lunr.js",
    "/search/worker.js",
    "/search/main.js",
    "/search/search_index.json",
]

def mdfile_to_path(file):
    return "/" + file.replace('source/', '').replace('.md','.html')

paths_in_docs = [mdfile_to_path(file) for file in mdfiles]

urlp = re.compile(r'\]\((?!http|#|mailto|ftp)([^ ")]*)')

def urlsindata(mdfile, data):
    return [(mdfile, m) for m in urlp.findall(data)]

testline = """Please see the descriptions of the subject categories and access papers from <a href="/archive/eess">https://arxiv.org/archive/eess</a>. New readers and authors to arXiv should see our help pages for [registration](/help/registerhelp), [submission](/help/submit) and [subscription](/help/subscribe)."""
assert len(urlsindata('assert_on_testline', testline)) == 3, urlsindata('assert_on_testline', testline)


def getlinks(urls, mdfile):
    with open(mdfile) as ff:
        print(mdfile)
        data = ff.read()
        data = data.replace("\n", ' ')
        urls.extend( urlsindata(mdfile, data))

    return urls


dont_fix_file_types = ['.jpg', '.pdf', '.png', '.txt', '.bst', '.gz'
                       ,'.sh' ,'.conf' ,'.jpeg' ,'.svg', '.dvi', '.c' ]

def dont_fix(url):
    if any([ftyp in url for ftyp in dont_fix_file_types]):
        return "nothing needed"

def file_to_prefix(file):
    """ docs/foo/bar/index.md -> /foo/bar """
    parts = file.replace('docs/', '').split('/')
    return '/' + '/'.join(parts[:-1])

assert file_to_prefix('') == '/'
assert file_to_prefix('docs/new/q-fin_announce.md') == '/new', file_to_prefix('docs/new/q-fin_announce.md')
assert file_to_prefix('docs/new/index.md') == '/new'
assert file_to_prefix('docs/corr/subjectclasses.md') == '/corr'
assert file_to_prefix('docs/new/cool/super/index.md') == '/new/cool/super'

def hasprotocol(url):
    return 'http:' in url or 'https:' in url or 'ftp:' in url or 'mailto:' in url

def ispathfragement(url):
    return not hasprotocol(url)

def isarxivorgpath(url):
    """Path prefixes that are on arxiv.org but not part of docs"""
    return any([url.startswith(prf) for prf in ['/abs/', '/list',
                                                '/ps', '/format/',
                                                '/auth/',
                                                '/stats/monthly_downloads',
                                                '/openurl-cookie',
                                                '/stats/monthly_submissions',
                                                '/set_author_id',
                                                '/find/',
                                                '/pdf', '/archive',
                                                '/cookie', '/user',
                                                '/moderators']])

def pathandanchor(url):
    parts = url.split('#')
    return (parts[0], f"#{parts[1]}" if len(parts) == 2 else '')

assert pathandanchor('bob') == ('bob','')
assert pathandanchor('/cure/bob') == ('/cure/bob','')
assert pathandanchor('cure/bob') == ('cure/bob','')
assert pathandanchor('bob#smith') == ('bob','#smith')
assert pathandanchor('/bob#smith') == ('/bob','#smith')
assert pathandanchor('/bob.html#smith') == ('/bob.html','#smith')

def levels(path):
    if path == '':
        return 0
    if path == '/':
        return 1
    else:
        return len(path.split('/'))-1

assert levels('/new') == 1
assert levels('/new/hat') == 2

def absolute2rel(path,url):
    """Something like /help and /help/cross => cross.html """
    if url.startswith(path):
        common = commonpath([path,url])
        return url.replace(common,'')[1:]
    else:
        if '../' in path:
            return path  # just give up
        else:
            ups = '../' * levels(path)
            return f"{ups}{url[1:]}"


assert absolute2rel('/help', '/help/index') == 'index',  absolute2rel('/help', '/help/index')
assert absolute2rel('/help/api/faq', '/help/api/faq') == '', absolute2rel('/help/api/faq', '/help/api/faq')
assert absolute2rel('/help', '/help') == ''
assert absolute2rel('/new', '/help/reg') == '../help/reg'


def htmlandanchor(url,anchor):
    if '.html' in url:
        return url + anchor
    else:
        return f"{url}.html{anchor}"

def dedotdot(inpath, inurl):
    url, anchor = pathandanchor(inurl)
    url, path = PurePath(url), PurePath(inpath)
    if '..' in url.parts:
        to_remove = len([pt for pt in url.parts if pt == '..'])
        url = '/'.join(url.parts[to_remove:])
        path = '/'.join(path.parts[:-to_remove])

        return (path[1:], url+anchor)
    else:
        return (inpath, inurl)

assert dedotdot('/a/b/c', '../d') == ('/a/b', 'd')
assert dedotdot('/a/b/c', '../../d') == ('/a', 'd')
assert dedotdot('/about/reports', '../support') == ('/about', 'support')
assert dedotdot('/a/b/c', 'd') == ('/a/b/c', 'd'),  dedotdot('/a/b/c', 'd')
assert dedotdot('/a/b/c', 'd#e') == ('/a/b/c', 'd#e')

def guess(paths_in_docs, path, inurl):
    """With the knolwege of all the paths in /docs, try to guess which one
    a url is targeting"""
    ddpath, ddurl = dedotdot(path, inurl)
    aurl, anchor = pathandanchor(ddurl)
    if aurl == '':
        aurl = 'index'
    url, path = PurePath(aurl), PurePath(ddpath)

    if len(path.parts) > 0:
        guess_formats =[
            f"{path.parts[-1]}/{url}/index",
            f"{path.parts[-1]}/{url}",
            f"{path.parts[-1]}/{url.stem}",
            f"{url}/index",
            url.stem]
    else:
        guess_formats =[ url.stem+".html", f"{url}/index"]
    if len(url.parts) > 1:
        guess_formats.insert(0, f"{url.parts[-2]}/{url.parts[-1]}")
    if url.as_posix() in ['./' , '.', '']:
        guess_formats.insert(0, f"{path.parts[-1]}")
        guess_formats.insert(0, f"{path.parts[-1]}/index")
    if url.is_absolute():
        guess_formats.insert(0, aurl)
        guess_formats.insert(0, aurl+'.html')

    guess_formats.insert(0, path.as_posix()+'/'+aurl)
    guess_formats.insert(0, path.as_posix()+'/'+aurl+'.html')
    guess_formats.insert(0, '/'+aurl+'.html')

    for g in guess_formats:
        guess = [p for p in paths_in_docs if g in p]
        if len(guess) == 1:
            return (guess[0] + anchor).replace('.html','.md')

def fix_href(path, inurl):
    #import pdb; pdb.set_trace()
    url,anchor = pathandanchor(inurl)
    if url == '/':
        return arxiv
    if '/help/hypertex/X' in path:
        return path + '/' + inurl
    abs_m = re.compile(r'.*(/abs/.*)').match(url)
    if abs_m:
        return arxiv + abs_m.group(1)
    if hasprotocol(inurl):
        return inurl + anchor
    if isarxivorgpath(inurl):
        return arxiv + inurl + anchor
    return guess(paths_in_docs, path, inurl)

assert fix_href('/help/api', '../rss') == '/help/rss.md'
assert fix_href('/help', 'myarticles') is not None, fix_href('/help', 'myarticles')
assert fix_href('/help', '/auth/request-ownership') is not None, fix_href('/help', '/auth/request-ownership')
#assert fixedv2('/about/reports', '/help/support/2011_budget') is not None, fixedv2('/about/reports', '/help/support/2011_budget') # Actual missing file
assert fix_href('/help/stats', '/stats/monthly_downloads') is not None, fix_href('/help/stats', '/stats/monthly_downloads')
#assert fixedv2('/new', '/help/pswindows') is not None, fixedv2('/new', '/help/pswindows') # Actual missing
#assert fixedv2('/new', '/new/q-fin_announcement') is not None, fixedv2('/new', '/new/q-fin_announcement') # Actual Missing
assert fix_href('/help', 'bulk_data') is not None, fix_href('/help', 'bulk_data')
assert fix_href('/help/faq', '../submit#availability') is not None, fix_href('/help/faq', '../submit#availability')
assert fix_href('/help', 'submit') is not None, fix_href('/help', 'submit')
#assert fixedv2('/help', '../cookies') is not None, fixedv2('/help', '../cookies')  # intended to go to the arxiv.org/cookies page
#assert fixedv2('/new', '/blurb/sep96news') is not None, fixedv2('/new', '/blurb/sep96news') # missing
#assert fixedv2('/help/hypertex/X', 'Mosaic') is not None, fixedv2('/help/hypertex/X', 'Mosaic') # Not sure
assert fix_href('/help', '/openurl-cookie') is not None, fix_href('/help', '/openurl-cookie')
assert fix_href('/new', '/') is not None, fix_href('/new', '/')
assert fix_href('/about/reports', '../support') is not None, fix_href('/about/reports', '../support')
assert fix_href('/help', '/') is not None, fix_href('/help', '/')
assert fix_href('/about/reports', '../support') is not None, fix_href('/about/reports', '../support')
#assert fixedv2('/about/reports', '/help/policies/code\_of\_conduct') is not None, fixedv2('/about/reports', '/help/policies/code\_of\_conduct') # odd
#assert fixedv2('/about/reports', '/help/support/2010_budget') is not None, fixedv2('/about/reports', '/help/support/2010_budget') # missing
#assert fixedv2('/help', 'faq/landscape "arXiv landscape help page"') is not None, fixedv2('/help', 'faq/landscape "arXiv landscape help page"') # odd
assert fix_href('/help', 'bulk_data') is not None, fix_href('/help', 'bulk_data')
assert fix_href('/help/stats', '/stats/monthly_submissions') is not None, fix_href('/help/stats', '/stats/monthly_submissions')
assert fix_href('/help', 'arxiv_identifier') is not None, fix_href('/help', 'arxiv_identifier')
# assert fixedv2('/new', '/help/psvms') is not None, fixedv2('/new', '/help/psvms') # missing
#assert fixedv2('/new', '/help/submit_docx') is not None, fixedv2('/new', '/help/submit_docx') # missing
assert fix_href('/about/reports', '../support') is not None, fix_href('/about/reports', '../support')
#assert fixedv2('/new', '/help/psmacs') is not None, fixedv2('/new', '/help/psmacs') # missing
assert fix_href('/about/reports', '../support') is not None, fix_href('/about/reports', '../support')
#assert fixedv2('/new', '/servers') is not None, fixedv2('/new', '/servers') # missing
assert fix_href('/help', 'arxiv_identifier') is not None, fix_href('/help', 'arxiv_identifier')
#assert fixedv2('/new', '/help/psnonunix') is not None, fixedv2('/new', '/help/psnonunix') # missing
assert fix_href('/help', '/set_author_id') is not None, fix_href('/help', '/set_author_id')
#assert fixedv2('/new', '/x-eprint') is not None, fixedv2('/new', '/x-eprint') # missing
assert fix_href('/help', '/auth/need-paper-password') is not None, fix_href('/help', '/auth/need-paper-password')
assert fix_href('/about/reports', '../support') is not None, fix_href('/about/reports', '../support')
assert fix_href('/help', '/auth/need-paper-password') is not None, fix_href('/help', '/auth/need-paper-password')
#assert fixedv2('/new', '/help/search') is not None, fixedv2('/new', '/help/search') # Need new search via mkdocs
assert fix_href('/help/hypertex/X', 'callmosaic') is not None, fix_href('/help/hypertex/X', 'callmosaic')
assert fix_href('/help', '/auth/change-author-status') is not None, fix_href('/help', '/auth/change-author-status')
assert fix_href('/help/hypertex/binaries', '../#xhdvisource') is not None, fix_href('/help/hypertex/binaries', '../#xhdvisource')
assert fix_href('/help', '/auth/email-change-form') is not None, fix_href('/help', '/auth/email-change-form')
#assert fixedv2('/new', 'interruption') is not None, fixedv2('/new', 'interruption') # missing
#assert fixedv2('/new', 'physsub') is not None, fixedv2('/new', 'physsub') # missing
assert fix_href('/help', 'submit#availability') is not None, fix_href('/help', 'submit#availability')
assert fix_href('/help', 'arxiv_identifier') is not None, fix_href('/help', 'arxiv_identifier')
#assert fixedv2('/new', '/help/support/faq') is not None, fixedv2('/new', '/help/support/faq') # missing
assert fix_href('/help', '/auth/request-ownership') is not None, fix_href('/help', '/auth/request-ownership')
#assert fixedv2('/new', '/help/faq/y2k') is not None, fixedv2('/new', '/help/faq/y2k') #missing
assert fix_href('/help', '/auth/need-paper-password') is not None, fix_href('/help', '/auth/need-paper-password')
assert fix_href('/new', 'nlin') is not None, fix_href('/new', 'nlin')
assert fix_href('/new', '/find/math/1/au:+Perelman_G/0/1/0/all/0/1') is not None, fix_href('/new', '/find/math/1/au:+Perelman_G/0/1/0/all/0/1')
assert fix_href('/new', '/') is not None, fix_href('/new', '/')
# assert fixedv2('/new', '/help/uploads') is not None, fixedv2('/new', '/help/uploads') # missing
#assert fixedv2('/', '{{ page.edit_url }}') is not None, fixedv2('/', '{{ page.edit_url }}') # intended jinja template
assert fix_href('/help', 'arxiv_identifier') is not None, fix_href('/help', 'arxiv_identifier')
assert fix_href('/about/reports', '../support') is not None, fix_href('/about/reports', '../support')
assert fix_href('/about/reports', '../support') is not None, fix_href('/about/reports', '../support')
assert fix_href('/help', 'submit') is not None, fix_href('/help', 'submit')
assert fix_href('/help', 'bulk_data') is not None, fix_href('/help', 'bulk_data')
assert fix_href('/corr', './') is not None, fix_href('/corr', './')
assert fix_href('/help', '/stats/monthly_submissions') is not None, fix_href('/help', '/stats/monthly_submissions')
assert fix_href('/about/reports', '../support') is not None, fix_href('/about/reports', '../support')
assert fix_href('/help/policies', '../submit') is not None, fix_href('/help/policies', '../submit')
assert fix_href('/help', 'submit') is not None, fix_href('/help', 'submit')
#assert fixedv2('/new', '/help/submit_nb') is not None, fixedv2('/new', '/help/submit_nb') # missing
assert fix_href('/help/hypertex/binaries', '../') is not None, fix_href('/help/hypertex/binaries', '../')
# assert fixedv2('/about/reports', '/about/reports/2019roadmap') is not None, fixedv2('/about/reports', '/about/reports/2019roadmap') # missing
#assert fixedv2('/about/reports', '/help/support/2012_budget') is not None, fixedv2('/about/reports', '/help/support/2012_budget') # missing
assert fix_href('/help', 'myarticles') is not None, fix_href('/help', 'myarticles')
assert fix_href('/about/reports', '../support') is not None, fix_href('/about/reports', '../support')
assert fix_href('/help/faq', '../ps') is not None, fix_href('/help/faq', '../ps')
# assert fixedv2('/help', '/auth "arXiv user account page"') is not None, fixedv2('/help', '/auth "arXiv user account page"') # fixed at regex level
assert fix_href('/help', '/auth/request-ownership') is not None, fix_href('/help', '/auth/request-ownership')
assert fix_href('/new', '/') is not None, fix_href('/new', '/')
#assert fixedv2('/about/reports', '/help/support/2010_budget') is not None, fixedv2('/about/reports', '/help/support/2010_budget') #
assert fix_href('/help', 'myarticles#config') is not None, fix_href('/help', 'myarticles#config')
assert fix_href('/about/reports', '../support') is not None, fix_href('/about/reports', '../support')

@dataclass
class item():
    file:str
    prefix:str
    orig: str
    replacement: str

todo = defaultdict(list)


links = []
_=[getlinks(links, file) for file in mdfiles]
links = set(links)

import os
doit =  bool(os.environ.get('DOIT', False)=='1')

for file,url in links:
    if not dont_fix(url):
        prefix = file_to_prefix(file)
        fx = fix_href(prefix, url)
        todo[file].append(item(file, prefix, url, fx))
        if not doit:
            if fx == None:
                print(f"{file:<50}| prefix:{prefix:<20}\t\t\t  url:{url:<20} \t\t -> \t {fx}")
            print(f"assert guess(paths_in_docs, '{prefix}', '{url}') is not None, guess(paths_in_docs, '{prefix}', '{url}')")

if not doit:
    print("\nThe above list is only the fixes that failed")
    print(f"Total fixes: {len(todo)}")
    print("Run with DOIT=1 env var to alter .md files in docs")
else:
   print("Doing edit of MD files in docs")
   for file in todo.keys():
       with open(file, 'r') as fh:
           data = fh.read()

       for change in todo[file]:
            data = data.replace(f"({change.orig})", f"({change.replacement})")

       with open(file, 'w') as fh:
           fh.write(data)
