import os

from docs.domain import IndexablePage, SearchResults, SearchResult
from docs.context import get_application_config

from whoosh import fields, index
from whoosh.qparser import QueryParser


SCHEMA = fields.Schema(
    title=fields.TEXT(stored=True),
    path=fields.ID(stored=True),
    content=fields.TEXT(stored=True)
)


def _get_index_path() -> str:
    """Get the index path from the current application."""
    config = get_application_config()
    return config.get('INDEX_NAME', 'help')


def _get_index(index_path: str) -> index.Index:
    """Get the index in ``index_path``."""
    if not os.path.exists(index_path):
        raise ValueError(f"{index_path} does not exist")
    return index.open_dir(index_path)


def create_index() -> index.Index:
    """Initialize the index."""
    index_path = _get_index_path()
    if not os.path.exists(index_path):
        os.mkdir(index_path)
    index.create_in(index_path, SCHEMA)


def add_documents(*documents: IndexablePage) -> None:
    """Add :class:`.IndexablePage`s to the search index."""
    idx = _get_index(_get_index_path())
    writer = idx.writer()
    for document in documents:
        writer.add_document(title=document.title, path=document.path,
                            content=document.content)
    writer.commit()


def find(query: str) -> SearchResults:
    """Perform a simple text search against the site index."""
    qp = QueryParser("content", schema=SCHEMA)
    q = qp.parse(query)

    idx = _get_index(_get_index_path())
    with idx.searcher() as searcher:
        results = searcher.search(q)

        return SearchResults(
            total_hits=len(results),
            scored_hits=results.scored_length(),
            results=[
                SearchResult(
                    title=str(result['title']),
                    path=str(result['path']),
                    highlights=str(result.highlights('content'))
                ) for result in results
            ]
        )
