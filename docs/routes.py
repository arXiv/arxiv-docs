"""UI routes for the documents service."""

import os
from typing import Callable, Union, Dict
from flask import Blueprint, render_template, Markup, request, url_for
from werkzeug.exceptions import HTTPException, NotFound, InternalServerError

from arxiv.base import logging
from flask import render_template_string, current_app
import jinja2

from docs.services import index, site
from . import render
from .domain import Page, Component


logger = logging.getLogger(__name__)


blueprint = Blueprint('docs', __name__, url_prefix='', static_folder='static',
                      template_folder='docs/templates/docs')


def get_link_dereferencer(page: Page) -> Callable:
    """Generate a dereferencer function for paths relative to a page."""

    def link_dereferencer(href: str) -> str:
        """Link dereferencer for use during HTML rendering."""
        if not href or href.startswith('http'):
            logger.debug('not an internal link: %s', href)
            return href
        try:
            path = index.get_by_slug(href).path
            logger.debug('got path by slug: %s', href)
        except index.PageDoesNotExist:
            abspath = '/'.join([page.path, href])
            try:
                path = index.get_by_path(abspath).path
                logger.debug('got path by abspath: %s', href)
            except index.PageDoesNotExist:
                logger.debug('could not dereference path: %s', href)
                return href
        return url_for('docs.from_sitemap', path=path)
    return link_dereferencer


def get_static_dereferencer(page: Page) -> Callable:
    """Generate a dereferencer function for static files relative to a page."""
    def static_deferencer(src: str) -> str:
        """Static URL dereferencer for use during HTML rendering."""
        if not src or src.startswith('http'):
            return src
        if page.is_index_page:
            path_parts = page.path.split('/')
        else:
            path_parts = page.path.split('/')[:-1]
        filename = "/".join(path_parts + [src])
        return url_for('static', filename=filename)
    return static_deferencer


@blueprint.route('/search', methods=['GET'])
def search():
    """Handle a search request."""
    q = request.args.get('q')
    results = index.find(q)
    return render_template('docs/search.html', results=results, q=q)


@blueprint.route('/', defaults={'path': ''})
@blueprint.route('/<path:path>')
def from_sitemap(path: str):
    """Route the request dynamically, based on the indexed site map."""
    try:
        page = index.get_by_path(path)
    except index.PageDoesNotExist as e:
        raise NotFound('Page does not exist') from e

    try:
        content = site.content(page)
    except site.PageLoadFailed as e:
        raise InternalServerError('Could not load page') from e

    site_path = current_app.config['SITE_PATH']

    static_dereferencer = get_static_dereferencer(page)
    link_dereferencer = get_link_dereferencer(page)
    rendered = render.render(content, link_dereferencer, static_dereferencer)
    rendered = render_template_string(rendered)
    context = dict(page=page, content=Markup(rendered), pagetitle=page.title)
    if page.template is not None:
        template = f'{site_path}/{page.template}'
    else:
        template = 'docs/page.html'
    return render_template(template, **context)


class ComponentLoader(object):
    def __init__(self, key: str) -> None:
        """Initialize a loader with a key (path partial)."""
        self._key = key

    def __getattr__(self, key: str) -> Union['ComponentLoader', Component]:
        """Attempt to load a component by path."""
        path = '/'.join([self._key, key]).lstrip('/')
        try:
            component = index.get_component_by_path(path)
        except index.ComponentDoesNotExist:
            logger.debug(f'Could not load component at {path}')
            return ComponentLoader(path)
        logger.debug(f'Loaded component at {path}')
        return component


@blueprint.context_processor
def inject_components() -> Dict[str, ComponentLoader]:
    return {'components': ComponentLoader('')}
