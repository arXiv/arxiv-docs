"""
Site index.

This module is responsible for loading site content at request time, using a
Whoosh document index.
"""

import os
import json
from typing import List, Iterable
from ..domain import IndexablePage, SearchResults, SearchResult, Page, \
    Component, Schema
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
    slug=fields.ID(stored=True),
    content=fields.TEXT(stored=True),
    content_path=fields.TEXT(stored=True),
    template=fields.TEXT(stored=True)
)

COMPONENT_SCHEMA = fields.Schema(
    title=fields.TEXT(stored=True),
    path=fields.ID(stored=True),
    data=JSON(stored=True),
    slug=fields.ID(stored=True),
    content=fields.TEXT(stored=True),
    content_path=fields.TEXT(stored=True)
)

SCHEMA_SCHEMA = fields.Schema(
    title=fields.TEXT(stored=True),
    path=fields.ID(stored=True),
    data=JSON(stored=True),
    slug=fields.ID(stored=True),
    content_path=fields.TEXT(stored=True)
)


class PageDoesNotExist(Exception):
    """A requested :class:`Page` does not exist."""


class ComponentDoesNotExist(Exception):
    """A requested :class:`Component` does not exist."""


class SchemaDoesNotExist(Exception):
    """A requested :class:`Schema` does not exist."""


class DuplicateSlug(Exception):
    """Two pages with the same slug were encountered!."""


def create_index() -> index.Index:
    """Initialize the index."""
    index_path = _get_index_path()
    components_index_path = _get_component_index_path()
    schema_index_path = _get_schema_index_path()
    for path in [index_path, components_index_path, schema_index_path]:
        if not os.path.exists(path):
            os.mkdir(path)
    index.create_in(index_path, SCHEMA)
    index.create_in(components_index_path, COMPONENT_SCHEMA)
    index.create_in(schema_index_path, SCHEMA_SCHEMA)


def add_components(components: Iterable[Component]) -> None:
    idx = _get_index(_get_component_index_path())
    writer = idx.writer()
    for component in components:
        writer.add_document(
            title=component.title,
            path=component.path,
            slug=component.slug,
            content=component.content,
            content_path=component.content_path,
            data=component.data
        )
        logger.debug('Added component %s', component.path)
    writer.commit()


def add_schemas(schemas: Iterable[Schema]) -> None:
    idx = _get_index(_get_schema_index_path())
    writer = idx.writer()
    for schema in schemas:
        writer.add_document(
            title=schema.title,
            path=schema.path,
            slug=schema.slug,
            content_path=schema.content_path,
            data=schema.data
        )
        logger.debug('Added schema %s', schema.path)
    writer.commit()


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
            raise DuplicateSlug(
                'More than one page has slug `%s`; check the page at %s'
                % (page.slug, page.path)
            )
        slugs.add(page.slug)

        writer.add_document(
            title=page.title,
            path=page.path,
            slug=page.slug,
            content=content,
            content_path=page.content_path,
            parents=page.parent_paths,
            template=page.template
        )
        logger.debug('Added page %s', page.path)
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
    logger.debug('Searching with index %s', idx)
    with idx.searcher() as searcher:
        logger.debug('Searching with path=%s', path)
        result = searcher.document(path=path)
    if result is None:
        logger.debug('Result is None')
        raise PageDoesNotExist('No such page')
    return Page(
        title=result['title'],
        path=result['path'],
        content_path=result['content_path'],
        template=result.get('template'),
        slug=result['slug'],
        parents=_get_parents(result) if get_parents else None,
        children=_get_children(result) if get_children else None,
    )


def get_component_by_path(path: str) -> Component:
    """
    Load a :class:`.Component` by its path.

    Parameters
    ----------
    path : str
        The relative path of the component.

    Returns
    -------
    :class:`.Component`
    """
    idx = _get_index(_get_component_index_path())
    with idx.searcher() as searcher:
        result = searcher.document(path=path)
    if result is None:
        raise ComponentDoesNotExist('No such component')
    return Component(
        title=result['title'],
        path=result['path'],
        content_path=result['content_path'],
        slug=result['slug'],
        data=result['data']
    )


def get_schema_by_path(path: str) -> Schema:
    """
    Load a :class:`.Schema` by its path.

    Parameters
    ----------
    path : str
        The relative path of the schema.

    Returns
    -------
    :class:`.Schema`
    """
    idx = _get_index(_get_schema_index_path())
    with idx.searcher() as searcher:
        result = searcher.document(path=path)
    if result is None:
        raise SchemaDoesNotExist('No such schema')
    return Schema(
        title=result['title'],
        path=result['path'],
        content_path=result['content_path'],
        slug=result['slug'],
        data=result['data']
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
    return [get_by_path('/'.join(result['parents'][:i+1]), False, False)
            for i in range(len(result['parents']))]


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


def _get_component_index_path() -> str:
    """Get the index path from the current application."""
    config = get_application_config()
    _path = config.get('INDEX_NAME', 'idx')
    return f'{_path}_components'


def _get_schema_index_path() -> str:
    """Get the schema index path from the current application."""
    config = get_application_config()
    _path = config.get('INDEX_NAME', 'idx')
    return f'{_path}_schemas'


def _get_index(index_path: str) -> index.Index:
    """Get the index in ``index_path``."""
    if not os.path.exists(index_path):
        raise ValueError(f"{index_path} does not exist")
    return index.open_dir(index_path)
