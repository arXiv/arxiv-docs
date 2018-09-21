"""
Site loader.

This module is responsible for loading site content at build time.
"""

import os
from collections import defaultdict
from typing import List, Tuple, Dict, Callable, Iterable
from ..domain import Page, Component

import frontmatter
from flask import current_app

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

    for dirpath, dirnames, filenames in os.walk(pages_path):
        for filename in filenames:
            if filename.endswith('.md'):
                yield _load_page(pages_path, dirpath, filename)


def load_components(site_path: str) -> Iterable[Component]:
    components_path = os.path.join(site_path, 'components')
    for dirpath, dirnames, filenames in os.walk(components_path):
        for filename in filenames:
            if filename.endswith('.md'):
                yield _load_component(components_path, dirpath, filename)


def load_static(site_path: str) -> List[Tuple[str, str]]:
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


def load_templates(site_path: str) -> List[Tuple[str, str]]:
    files = []
    pages_path = os.path.join(site_path, 'templates')
    for dirpath, dirnames, filenames in os.walk(pages_path):
        for filename in filenames:
            if not filename.endswith('.html') or filename.startswith('.'):
                continue
            content_path = os.path.join(dirpath, filename)
            path = content_path[len(pages_path):].strip('/')
            files.append((path, content_path))
    return files


def _load_page(rootpath: str, dirpath: str, filename: str) -> Page:
    content_path = os.path.join(dirpath, filename)
    path = content_path[len(rootpath):].strip('/')
    if path.endswith('.md'):
        path = path[:-3]
    if path.split('/')[-1] == 'index':
        path = '/'.join(path.split('/')[:-1])

    page_data = frontmatter.load(content_path)
    parents = path.split('/')[:-1]
    title = _get_title(page_data, filename)
    template = page_data.get('template')

    site_name = current_app.config['SITE_NAME']
    if template is not None:
        template = f'{site_name}/{template}'
    page = Page(
        title=title,
        path=path,
        content_path=content_path,
        slug=page_data.get('slug', slugify(path)),
        content=page_data.content,
        parents=parents,
        template=template
    )
    return page


def _load_component(rootpath: str, dirpath: str, filename: str) -> Component:
    content_path = os.path.join(dirpath, filename)
    path = content_path[len(rootpath):].strip('/')
    if path.endswith('.md'):
        path = path[:-3]
    page_data = frontmatter.load(content_path)
    component = Component(
        title=_get_title(page_data, filename),
        path=path,
        content_path=content_path,
        slug=page_data.get('slug', slugify(path)),
        content=page_data.content,
        data=page_data.to_dict()
    )
    print(component.path)
    return component


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
