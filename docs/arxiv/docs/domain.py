"""Domain classes for arxiv-docs service."""

from typing import Any, Optional, Type, NamedTuple, List, Tuple
import bleach
import markdown


class Page(NamedTuple):
    title: str
    path: str
    content_path: str
    slug: str
    parents: Optional[List] = None
    children: Optional[List] = None
    content: Optional[str] = None
    template: Optional[str] = None

    @property
    def parent_paths(self) -> Optional[List[str]]:
        if self.parents is None:
            return None
        return [parent for parent in self.parents]

    @property
    def child_paths(self) -> Optional[List[str]]:
        if self.children is None:
            return None
        return [child.path for child in self.children]

    @property
    def is_index_page(self):
        return self.content_path.endswith('/index.md')


class SearchResult(NamedTuple):
    page: Page
    highlights: str


class SearchResults(NamedTuple):
    total_hits: int
    scored_hits: int
    results: List[SearchResult]


class IndexablePage(NamedTuple):
    page: Page
    indexable_content: str


class Component(NamedTuple):
    title: str
    path: str
    content_path: str
    slug: str
    data: dict
    content: Optional[str] = None


class Schema(NamedTuple):
    title: str
    path: str
    content_path: str
    slug: str
    data: dict
