"""Domain classes for arxiv-docs service."""

from typing import Any, Optional, Type, NamedTuple, List
import markdown


class IndexablePage(NamedTuple):
    title: str
    path: str
    content: str


class Page(NamedTuple):
    title: str
    path: str
    content_path: str
    parents: Optional[List]
    pages: Optional[dict]
    markdown: Optional[markdown.markdown]


class SearchResult(NamedTuple):
    title: str
    path: str
    highlights: str
    """May contain markup to highlight matching text."""


class SearchResults(NamedTuple):
    total_hits: int
    scored_hits: int
    results: List[SearchResult]
