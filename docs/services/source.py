"""API for loading content from a markdown site source."""

import os

import frontmatter

from functools import lru_cache
from typing import NamedTuple
from typing import Optional, List, Tuple, Iterable, Dict

from arxiv.base.globals import get_application_config as config

from ..domain import SourcePage


def get_source_path() -> str:
    """Get the absolute path to the site source."""
    return os.path.abspath(config()['SOURCE_PATH'])


def get_templates_path() -> str:
    """Get the absolute path to the templates in the site source."""
    return os.path.join(get_source_path(), '_templates')


def get_path_for_page(page_path: str) -> str:
    """Get the absolute path for a source page based on its relative path."""
    return os.path.join(get_source_path(), f'{page_path}.md')


@lru_cache(maxsize=1024)
def page_exists(page_path: str) -> bool:
    """Check whether a source page exists."""
    return os.path.exists(get_path_for_page(page_path))


def get_parents(page_path: str) -> List[Dict[str, str]]:
    """Get the paths for a source page's parent pages."""
    path_parts = page_path.split('/')
    parents = []
    for i in range(1, len(path_parts)):
        path = '/'.join(path_parts[:i])
        if page_exists(path):
            parent_page = load_page(path, False)
            parents.append({'page_path': path,
                            'title': parent_page.title})
        elif page_exists(f'{path}/index'):
            parent_page = load_page(f'{path}/index', False)
            parents.append({'page_path': f'{path}/index',
                            'title': parent_page.title,
                            'path_for_reference': path})
    return parents


@lru_cache(maxsize=1024)
def load_page(page_path: str, parents: bool = True) -> SourcePage:
    """Load content and data for a source page."""
    page_data = frontmatter.load(get_path_for_page(page_path))
    if parents:
        parents = get_parents(page_path)
    else:
        parents = []
    metadata = {k: v for k, v in page_data.metadata.items()}
    metadata['parents'] = parents
    metadata['title'] = _get_title(page_data, page_path)

    return SourcePage(
        page_path=page_path,
        title=_get_title(page_data, page_path),
        content=page_data.content,
        metadata=metadata,
        template=page_data.get('template'),
        parents=parents
    )


def load_pages() -> Iterable[SourcePage]:
    """(Lazily) load all pages in the site source."""
    source_path = get_source_path()
    for dirpath, dirnames, filenames in os.walk(source_path):
        for filename in filenames:
            if filename.endswith('.md'):
                full_path = os.path.join(dirpath, filename)
                page_path = full_path.split(source_path, 1)[1][1:-3]
                yield load_page(page_path)


def load_static_paths() -> List[Tuple[str, str]]:
    """
    Get all of the paths to static files in the site source.

    Returns
    -------
    list
        Items are Tuple[str, str], where the first element is the relative
        path (key) for the static file, and the second element is the absolute
        path to the static file in the site source.

    """
    source_path = get_source_path()
    files = []
    for dirpath, dirnames, filenames in os.walk(source_path):
        rdir = os.path.abspath(dirpath).split(source_path, 1)[1].lstrip('/')
        if rdir.startswith('_'):
            continue

        for filename in filenames:
            if filename.endswith('.md') or filename.startswith('.'):
                continue
            content_path = os.path.join(dirpath, filename)
            page_path = content_path[len(source_path):].strip('/')
            files.append((page_path, content_path))
    return files


def load_template_paths() -> List[Tuple[str, str]]:
    """
    Get all of the paths to templates in the site source.

    Returns
    -------
    list
        Items are Tuple[str, str], where the first element is the relative
        path (key) for the template, and the second element is the absolute
        path to the template file in the site source.

    """
    templates_path = get_templates_path()
    if not os.path.exists(templates_path):
        return []
    files = []
    for dirpath, dirnames, filenames in os.walk(templates_path):
        for filename in filenames:
            if not filename.endswith('.html') or filename.startswith('.'):
                continue
            content_path = os.path.join(dirpath, filename)
            template_path = content_path[len(templates_path):].strip('/')
            files.append((template_path, content_path))
    return files


def _get_title(page_data: dict, page_path: str) -> str:
    """Get the title of a source page."""
    title = page_data.get('title')
    if title is None:
        for line in page_data.content.split('\n'):
            cleaned = line.replace('#', '').strip()
            if cleaned:
                title = cleaned
                break
    if title is None:
        title = os.path.split(page_path)[1]
    return title
