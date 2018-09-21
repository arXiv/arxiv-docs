import os
from collections import defaultdict
from typing import List, Tuple, Dict, Callable, Iterable
from ..domain import Page

import frontmatter

from slugify import slugify


class PageLoadFailed(Exception):
    """Could not load the content of a page."""


def content(page: Page) -> str:
    try:
        return frontmatter.load(page.content_path).content
    except IOError as e:
        raise PageLoadFailed('Failed to load page') from e


def load_all(site_path: str) -> Iterable[Page]:
    pages_path = os.path.join(site_path, 'pages')
    pages = {}

    def get_parents(path: str) -> List[Page]:
        return [pages[p] for p in path.split('/') if p in pages]

    for dirpath, dirnames, filenames in os.walk(pages_path):
        for filename in filenames:
            if filename.endswith('.md'):
                page = _load_page(pages_path, dirpath, filename, get_parents)
                pages[page.path] = page
                yield page


def load_static(site_path: str) -> dict:
    files = []
    pages_path = os.path.join(site_path, 'pages')
    for dirpath, dirnames, filenames in os.walk(pages_path):
        for filename in filenames:
            if filename.endswith('.md') or filename.startswith('.'):
                continue
            content_path = os.path.join(dirpath, filename)
            path = content_path[len(pages_path):].strip('/')
            files.append((path, content_path))
    return files


def _load_page(rootpath: str, dirpath: str, filename: str,
               get_parents: Callable) -> Page:
    content_path = os.path.join(dirpath, filename)
    path = content_path[len(rootpath):].strip('/')
    if path.endswith('.md'):
        path = path[:-3]
    if path.split('/')[-1] == 'index':
        path = '/'.join(path.split('/')[:-1])

    page_data = frontmatter.load(content_path)
    parents = path.split('/')[:-1]
    title = _get_title(page_data, filename)
    page = Page(
        title=title,
        path=path,
        content_path=content_path,
        slug=page_data.get('slug', slugify(path)),
        content=page_data.content,
        parents=parents,
        # children=[]
    )
    return page


def _get_title(page_data: dict, filename: str) -> str:
    title = page_data.get('title')
    if title is None:
        for line in page_data.content.split('\n'):
            cleaned = line.replace('#', '').strip()
            if cleaned:
                title = cleaned
                break
    if title is None:
        title = filename.rstrip('.md')
    return title
