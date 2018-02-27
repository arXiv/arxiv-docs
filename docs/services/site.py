import os
import copy
from flask import url_for
from typing import List
from docs.domain import Page
from docs.context import get_application_config

import markdown
import yaml


class PageNotFound(Exception):
    """Attempted to load a page that does not exist."""


class PageLoadFailed(Exception):
    """Could not load the content of a page."""


SITEMAP = {}


def _unpack(path: str, elem: dict):
    if 'content_path' in elem:
        SITEMAP[path] = elem
    if 'pages' in elem:
        for key, sub_elem in elem['pages'].items():
            _unpack(f'{path}/{key}'.strip('/'), sub_elem)


def _load_sitemap() -> None:
    config = get_application_config()
    site_path = config.get('SITE_PATH', 'site')
    sitemap_path = os.path.join(site_path, 'sitemap.yaml')
    with open(sitemap_path) as f:
        _unpack('', yaml.safe_load(f))


def _full_path(local_path: str) -> str:
    """Generate the full path (including app and blueprint root) to a page."""
    try:
        base_path = url_for('docs.from_sitemap').rstrip('/')
    except RuntimeError:
        base_path = '/'
    local_path = local_path.lstrip('/')
    return f'{base_path}/{local_path}'


_load_sitemap()


def _find_page(path: str) -> dict:
    try:
        elem = copy.copy(SITEMAP[path.strip('/')])
    except KeyError as e:
        raise PageNotFound('Nope') from e
    elem['pages'] = elem.get('pages', {})
    return elem


def _load_markdown(content_path: str) -> markdown.markdown:
    try:
        with open(os.path.join('site', content_path)) as f:
            content = markdown.markdown(f.read())
    except IOError as e:
        raise PageLoadFailed('Failed to load page') from e
    return content


def load_page(path: str) -> Page:
    """Load a :class:`.Page` from ``path``."""
    elem = _find_page(path)
    elem['markdown'] = _load_markdown(elem['content_path'])
    elem['parents'] = []
    if path != '':
        fpath = ''
        for part in [''] + path.split('/'):
            fpath = f'{fpath}/{part}'
            pelem = _find_page(fpath)
            pelem['parents'] = None
            pelem['markdown'] = None
            elem['parents'].append(Page(path=_full_path(fpath), **pelem))
    return Page(path=_full_path(path), **elem)


def list_paths() -> List[Page]:
    return list(SITEMAP.keys())
