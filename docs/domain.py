"""Domain classes for arxiv-docs service."""

from typing import Any, Optional, Type, NamedTuple, List, Tuple, Dict
import bleach
import markdown


class SourcePage(NamedTuple):
    """Represents page data loaded from markdown source."""

    page_path: str
    title: str
    metadata: dict
    content: str
    template: Optional[str]
    parents: List[Dict[str, str]]

    @property
    def path_for_reference(self):
        if self.page_path.endswith('/index'):
            return '/'.join(self.page_path.split('/')[:-1])
        return self.page_path


class Page(NamedTuple):
    """Represents a page in the built site."""

    page_path: str
    content: str
    metadata: dict

    @property
    def path_for_reference(self):
        if self.page_path.endswith('/index'):
            return '/'.join(self.page_path.split('/')[:-1])
        return self.page_path


class SearchResult(NamedTuple):
    """Represents a search result."""

    title: str
    page_path: str
    highlights: Optional[str] = None


class SearchResults(NamedTuple):
    """Represents a set of search results."""

    total_hits: int
    previous_page: Optional[int]
    current_page: int
    next_page: Optional[int]
    limit: int
    start: int
    end: int
    total: int
    scored_hits: int
    results: List[SearchResult]


class IndexablePage(NamedTuple):
    """Representation of a source page suitable for indexing."""

    page: SourcePage
    indexable_content: str
