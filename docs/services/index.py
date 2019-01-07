"""
Site index.

This module is responsible for loading site content at request time, using a
Whoosh document index.
"""

import os
import json
from typing import List, Iterable
from ..domain import IndexablePage, SearchResults, SearchResult
from arxiv.base.globals import get_application_config

from whoosh import fields, index
from whoosh.qparser import QueryParser
from whoosh.system import emptybytes

from arxiv.base import logging


logger = logging.getLogger(__name__)


class JSON(fields.TEXT):
    def to_bytes(self, value: dict) -> bytes:
        return super(JSON, self).to_bytes(json.dumps(value))

    def from_bytes(self, bs: bytes) -> dict:
        return json.loads(super(JSON, self).from_bytes(bs))

    def index(self, value: dict, **kwargs) -> Iterable:
        yield (self.to_bytes(value), 1, 1.0, emptybytes)
        return


SCHEMA = fields.Schema(
    title=fields.TEXT(stored=True),
    path=fields.ID(stored=True),
    parents=fields.IDLIST(stored=True),
    content=fields.TEXT(stored=True)
)

STATIC_SCHEMA = fields.Schema(
    path=fields.ID(stored=True)
)


class PageDoesNotExist(Exception):
    """A requested :class:`Page` does not exist."""


class SchemaDoesNotExist(Exception):
    """A requested :class:`Schema` does not exist."""


def create_index() -> index.Index:
    """Initialize the index."""
    index_path = _get_index_path()
    static_index_path = _get_static_index_path()
    for path in [index_path, static_index_path]:
        if not os.path.exists(path):
            os.makedirs(path)
    index.create_in(index_path, SCHEMA)
    index.create_in(static_index_path, STATIC_SCHEMA)


def add_documents(pages: Iterable[IndexablePage]) -> None:
    """
    Add :class:`.IndexablePage`s to the search index.

    Parameters
    ----------
    pages : iterable
        An iterable that yields :class:`.IndexablePage` tuples.

    """
    idx = _get_index(_get_index_path())
    writer = idx.writer()
    for page, content in pages:
        writer.add_document(
            title=page.title,
            path=page.page_path,
            content=content,
            parents=[parent['page_path'] for parent in page.parents]
        )
        logger.debug('Added page %s', page.page_path)
    writer.commit()


def add_static_file(path: str) -> None:
    idx = _get_index(_get_static_index_path())
    writer = idx.writer()
    writer.add_document(path=path)
    logger.debug('Indexed static file: %s', path)
    writer.commit()


def get_by_path(path: str, get_parents: bool = True,
                get_children: bool = True) -> SearchResult:
    """
    Load a :class:`.SearchResult` by its path.

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
    :class:`.SearchResult`
    """
    idx = _get_index(_get_index_path())
    logger.debug('Searching with index %s', idx)
    with idx.searcher() as searcher:
        logger.debug('Searching with path=%s', path)
        result = searcher.document(path=path)
    if result is None:
        logger.debug('Result is None')
        raise PageDoesNotExist('No such page')
    logger.debug('Found page for path=%s', path)
    return SearchResult(
        title=result['title'],
        page_path=result['path']
    )


def get_static_file_by_path(path: str) -> str:
    idx = _get_index(_get_static_index_path())
    logger.debug('Searching with index %s', idx)
    with idx.searcher() as searcher:
        logger.debug('Searching for static file with path=%s', path)
        result = searcher.document(path=path)
    if result is None:
        logger.debug('Result is None')
        raise PageDoesNotExist('No such static file')
    logger.debug('Found static file for path=%s', path)
    return path


def find(query: str, page_number: int = 1, limit: int = 20) -> SearchResults:
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
        results = searcher.search_page(q, page_number, pagelen=limit)
        start = (page_number - 1) * limit + 1
        total = len(results)
        end = min(total, start + limit - 1)
        previous_page = page_number - 1 if page_number > 1 else None
        next_page = page_number + 1 if end < total else None

        return SearchResults(
            total_hits=len(results),
            previous_page=previous_page,
            current_page=page_number,
            next_page=next_page,
            limit=limit,
            start=start,
            end=end,
            total=total,
            scored_hits=results.scored_length(),
            results=[SearchResult(
                title=result['title'],
                page_path=result['path'],
                highlights=str(result.highlights('content'))
            ) for result in results]
        )


def _get_index_path() -> str:
    """Get the index path from the current application."""
    config = get_application_config()
    return os.path.join(config['BUILD_PATH'], config.get('INDEX_NAME', 'idx'))


def _get_static_index_path() -> str:
    """Get the index path from the current application."""
    config = get_application_config()
    _name = config.get('INDEX_NAME', 'idx')
    return os.path.join(config['BUILD_PATH'], f'{_name}_static')


def _get_index(index_path: str) -> index.Index:
    """Get the index in ``index_path``."""
    if not os.path.exists(index_path):
        raise ValueError(f"{index_path} does not exist")
    return index.open_dir(index_path)
