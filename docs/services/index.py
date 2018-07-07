"""Site index."""

import os

from typing import List, Iterable
from docs.domain import IndexablePage, SearchResults, SearchResult, Page
from arxiv.base.globals import get_application_config

from whoosh import fields, index
from whoosh.qparser import QueryParser


SCHEMA = fields.Schema(
    title=fields.TEXT(stored=True),
    path=fields.ID(stored=True),
    parents=fields.IDLIST(stored=True),
    slug=fields.ID(stored=True),
    content=fields.TEXT(stored=True),
    content_path=fields.TEXT(stored=True)
)


class PageDoesNotExist(Exception):
    """Page does not exist."""


class DuplicateSlug(Exception):
    """Two pages with the same slug were encountered!."""


def create_index() -> index.Index:
    """Initialize the index."""
    index_path = _get_index_path()
    if not os.path.exists(index_path):
        os.mkdir(index_path)
    index.create_in(index_path, SCHEMA)


def add_documents(pages: Iterable[IndexablePage]) -> None:
    """
    Add :class:`.IndexablePage`s to the search index.

    Parameters
    ----------
    pages : iterable
        An iterable that yields :class:`.IndexablePage` tuples.

    Raises
    ------
    :class:`DuplicateSlug`
        Raised if the same slug is encountered twice.

    """
    idx = _get_index(_get_index_path())
    writer = idx.writer()
    slugs = set()
    for page, content in pages:
        # Slugs must be unique, so we want to complain as early as possible
        # if that does not appear to be the case.
        if page.slug in slugs:
            raise DuplicateSlug('More than one page has slug `%s`' % page.slug)
        slugs.add(page.slug)

        writer.add_document(
            title=page.title,
            path=page.path,
            slug=page.slug,
            content=content,
            content_path=page.content_path,
            parents=page.parent_paths,
        )
    writer.commit()


def get_by_path(path: str, get_parents: bool = True,
                get_children: bool = True) -> Page:
    """
    Load a :class:`.Page` by its path.

    Parameters
    ----------
    path : str
        The relative path of the page.
    get_parents : bool
        Whether or not to load the parents of this page.
    get_children : bool
        Whether or not to load the children of this page.

    Returns
    -------
    :class:`.Page`
    """
    idx = _get_index(_get_index_path())
    with idx.searcher() as searcher:
        result = searcher.document(path=path)
    if result is None:
        raise PageDoesNotExist('No such page')

    return Page(
        title=result['title'],
        path=result['path'],
        content_path=result['content_path'],
        slug=result['slug'],
        parents=_get_parents(result) if get_parents else None,
        children=_get_children(result) if get_children else None,
    )


def get_by_slug(slug: str, get_parents: bool = True,
                get_children: bool = True) -> SearchResult:
    """
    Load a :class:`.Page` by its unique slug.

    Parameters
    ----------
    path : str
        The relative path of the page.
    get_parents : bool
        Whether or not to load the parents of this page.
    get_children : bool
        Whether or not to load the children of this page.

    Returns
    -------
    :class:`.Page`
    """
    idx = _get_index(_get_index_path())
    with idx.searcher() as searcher:
        result = searcher.document(slug=slug)
    if result is None:
        raise PageDoesNotExist('No such page')

    return Page(
        title=result['title'],
        path=result['path'],
        content_path=result['content_path'],
        slug=result['slug'],
        parents=_get_parents(result) if get_parents else None,
        children=_get_children(result) if get_children else None,
    )


def find(query: str) -> SearchResults:
    """
    Perform a simple text search against the site index.

    Parameters
    ----------
    query : str
        Free text with which to perform a full-text query.

    Returns
    -------
    :class:`.SearchResults`
    """
    qp = QueryParser("content", schema=SCHEMA)
    q = qp.parse(query)

    idx = _get_index(_get_index_path())
    with idx.searcher() as searcher:
        results = searcher.search(q)

        return SearchResults(
            total_hits=len(results),
            scored_hits=results.scored_length(),
            results=[SearchResult(
                Page(
                    title=result['title'],
                    path=result['path'],
                    content_path=result['content_path'],
                    slug=result['slug'],
                    parents=_get_parents(result),
                    children=_get_children(result),
                ),
                str(result.highlights('content'))
            ) for result in results]
        )


def _get_parents(result: dict) -> List[Page]:
    return [get_by_path(parent, False, False) for parent in result['parents']]


def _get_children(result: dict) -> List[Page]:
    idx = _get_index(_get_index_path())
    with idx.searcher() as searcher:
        results = searcher.documents(parents=result['path'])
        return [
            Page(
                title=result['title'],
                path=result['path'],
                content_path=result['content_path'],
                slug=result['slug'],
            ) for result in results
        ]


def _get_index_path() -> str:
    """Get the index path from the current application."""
    config = get_application_config()
    return config.get('INDEX_NAME', 'idx')


def _get_index(index_path: str) -> index.Index:
    """Get the index in ``index_path``."""
    if not os.path.exists(index_path):
        raise ValueError(f"{index_path} does not exist")
    return index.open_dir(index_path)
