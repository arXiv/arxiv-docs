Author Identifiers
==================

It is a long-term goal of arXiv to accurately identify and disambiguate
all authors of all articles in arXiv. Such identification would provide
accurate results for queries such as *"show me all the other papers by
the particular John Smith that wrote this paper"*, something that can be
done only approximately with text-based searches. It would also permit
construction of an author-article graph which is useful for relevance
assessment and bibliometric analysis.

Since 2005 arXiv has used [authority records](/help/authority.md) that associate
user accounts with articles authored by that user. These records support
the [endorsement system](/help/endorsement.md). The use of public author
identifiers as a way to build services upon this data is new in 2009.
Initially, users must opt-in to have a public author identifier and to
expose the record of their articles on arXiv for use in other services.
At some later date we hope to be able to improve our authority records
to the point where we can create public author identifiers for all
authors of arXiv articles without needing to enlist the help of each
author to check their record before opting in.

The services we offer based on author identifiers are:

-   simple list of papers as an HTML page you can link to (e.g.
    <https://arxiv.org/a/warner_s_1>)
-   an Atom feed of articles (e.g.
    <https://arxiv.org/a/warner_s_1.atom2> — authors combined, best for
    current feed readers; and <https://arxiv.org/a/warner_s_1.atom> —
    authors in separate atom:author elements)
-   a way to dynamically include the list of your publications in your
    own home page using the JavaScript [`myarticles` widget](None)

The above pages and [`myarticles` widget](None) are now also
accessible via an [ORCID identifier](/help/orcid.md), if you have [linked
an ORCID identifier to your arXiv user account](https://arxiv.org/user/confirm_orcid_id),
e.g.:

-   <https://arxiv.org/a/0000-0002-7970-7855>
-   <https://arxiv.org/a/0000-0002-7970-7855.atom2> and
    <https://arxiv.org/a/0000-0002-7970-7855.atom>

It would also be beneficial to associate author records in arXiv with
author records in other scholarly communication system, for example with
the INSPIRE database in high-energy physics. Association of author
records across different systems would facilitate the creation of
services and tools that operate over multiple repositories, or combine
data from multiple sources.

If you have authored articles on arXiv you may **[link your ORCID
identifier](https://arxiv.org/user/confirm_orcid_id)** or **[create an arXiv author
identifier](https://arxiv.org/set_author_id)** to use with the services listed above.

### Technical details

-   arXiv public author identifiers are not syntactically tied to arXiv
    user ids ("nicknames"). Users should not use their arXiv user id for
    any purpose other than logging in to arXiv or communication with
    arXiv administrators.
-   arXiv public author identifiers are complete URIs that resolve to
    yield representations based on HTTP content-negotiation. If you
    enter an author identifier in a web browser you will receive an HTML
    page listing the articles authored by the identified author (the
    same result is obtained by appending `.html` to the identifier). By
    either requesting Atom format in content-negotiation or explicitly
    appending `.atom` or `.atom2` then an Atom feed is returned using
    the same format as the [arXiv API](/help/index.md).
-   The local part of the author identifier (the part after
    `https://arxiv.org/a/`) is designed to be reasonably short and
    somewhat memorable/typable. It is created by combining the last name
    of the author, the first initial, and a sequence number starting
    at 1. To avoid URI encoding issues all characters in the last name
    and first initial are dumbed-down to lowercase ASCII a-z by
    lowercasing, stripping accents and removing any remaining characters
    not in the set a-z.
-   Linking an ORCID identifier to your arXiv user account is done [via
    the user account page](https://arxiv.org/user/confirm_orcid_id), and is shown on the
    [user account page](https://arxiv.org/user) once linked.
-   The current opt-in to create an arXiv author identifier is done
    through the [create an author identifier](https://arxiv.org/set_author_id) page,
    current status for any account is shown on the [user account
    page](/auth "arXiv user account page").
