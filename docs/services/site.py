"""Provides an interface to the built site at runtime."""

import os
import json

from arxiv.base.globals import get_application_config as config
from ..domain import Page


class PageNotFound(Exception):
    """A non-existant page was requested."""


def create_all(site_path: str) -> None:
    """Create all build paths required for the site."""
    for path in [get_static_path(), get_data_path(), get_pages_path(),
                 get_templates_path()]:
        if not os.path.exists(path):
            os.makedirs(path)


def get_static_path() -> str:
    """Get the absolute path for the site static directory."""
    return os.path.abspath(os.path.join(
        config()['BUILD_PATH'],
        'static',
        get_site_name()
    ))


def get_site_name() -> str:
    """Get the name of this site."""
    return config().get('SITE_NAME', 'arxiv')


def get_url_prefix() -> str:
    """Get the URL prefix for this site."""
    return config().get('SITE_URL_PREFIX', '/')


def get_site_human_name() -> str:
    """Get the URL prefix for this site."""
    return config().get('SITE_HUMAN_NAME', 'arXiv static pages')


def get_data_path() -> str:
    """Get the absolute path for the site data directory."""
    return os.path.abspath(os.path.join(config()['BUILD_PATH'], 'data'))


def get_templates_path() -> str:
    """Get the absolute path for the site templates directory."""
    return os.path.abspath(os.path.join(config()['BUILD_PATH'], 'templates'))


def get_pages_path() -> str:
    """Get the absolute path for the site pages directory."""
    return os.path.abspath(os.path.join(config()['BUILD_PATH'], 'pages'))


def get_page_filename(page_path: str) -> str:
    """Generate a filename for a rendered page."""
    return f'{page_path}.j2'


def get_path_for_page(page_path: str) -> str:
    """Generate an absolute path for a rendered page."""
    return os.path.join(get_pages_path(), get_page_filename(page_path))


def get_path_for_static(static_path: str) -> str:
    return os.path.join(get_static_path(), static_path)


def get_path_for_template(template_path: str) -> str:
    return os.path.join(get_templates_path(), template_path)


def get_path_for_data(page_path: str) -> str:
    return os.path.join(get_data_path(), f'{page_path}.json')


def store_metadata(page_path: str, data: dict) -> None:
    parent_dir, _ = os.path.split(get_path_for_data(page_path))
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)
    with open(get_path_for_data(page_path), 'w') as f:
        json.dump(data, f)


def store_page_content(page_path: str, content: str) -> None:
    parent_dir, _ = os.path.split(get_path_for_page(page_path))
    if not os.path.exists(parent_dir):
        os.makedirs(parent_dir)
    with open(get_path_for_page(page_path), 'w') as f:
        f.write(content)


def load_page_content(page_path: str) -> str:
    if get_pages_path() not in os.path.normpath(get_path_for_page(page_path)):
        raise PageNotFound(f'Page {page_path} not found')

    with open(get_path_for_page(page_path), 'r') as f:
        return f.read()


def load_metadata(page_path: str) -> dict:
    if not os.path.exists(get_path_for_data(page_path)):
        return {}
    with open(get_path_for_data(page_path), 'r') as f:
        return json.load(f)


def load_page(page_path: str) -> Page:
    if not os.path.exists(get_path_for_page(page_path)):
        index_path = os.path.join(page_path, 'index')
        if os.path.exists(get_path_for_page(index_path)):
            page_path = index_path
        else:
            raise PageNotFound(f'Page {page_path} not found')
    return Page(
        page_path=page_path,
        content=load_page_content(page_path),
        metadata=load_metadata(page_path)
    )
