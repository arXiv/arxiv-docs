import os
import copy
from typing import List, Tuple, Dict

from flask import url_for

import yaml

from docs.domain import Page
from arxiv.base.globals import get_application_config
from .exceptions import PageNotFound


SITEMAP: Dict[str, Dict] = {}
"""Maps relative paths to page data."""

SLUGMAP: Dict[str, str] = {}
"""Maps page slugs to relative paths for persistent linking."""


def slug_path(slug: str) -> str:
    """Get the full path to a page bug slug."""
    if slug not in SLUGMAP:
        raise KeyError('No such path')
    return _full_path(SLUGMAP[slug])


def _unpack(path: str, elem: dict) -> None:
    if 'content_path' in elem:
        SITEMAP[path] = elem
    if 'slug' in elem:
        SLUGMAP[elem['slug']] = path
    if 'pages' in elem:
        for key, sub_elem in elem['pages'].items():
            _unpack(f'{path}/{key}'.strip('/'), sub_elem)


def _load_sitemap() -> None:
    config = get_application_config()
    site_path = config.get('SITE_PATH', 'site')
    sitemap_path = os.path.join(site_path, 'sitemap.yaml')
    with open(sitemap_path) as f:
        site = yaml.safe_load(f)
        for key, elem in site.items():
            _unpack(key, elem)


def _full_path(local_path: str) -> str:
    """Generate the full path (including app and blueprint root) to a page."""
    try:
        base_path = url_for('docs.from_sitemap').rstrip('/')
    except RuntimeError:
        base_path = '/'
    local_path = local_path.lstrip('/')
    return f'{base_path}/{local_path}'


def find_page(path: str) -> Tuple[str, dict]:
    try:
        elem = copy.copy(SITEMAP[path.strip('/')])
    except KeyError as e:
        raise PageNotFound('Nope') from e
    elem['pages'] = elem.get('pages', {})
    return _full_path(path), elem


def list_paths() -> List[str]:
    return list(SITEMAP.keys())


_load_sitemap()
