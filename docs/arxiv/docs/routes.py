"""UI routes for the documents service."""

import os
from typing import Callable, Union, Dict, Mapping
from flask import Blueprint, render_template, Markup, request, url_for, Flask
from werkzeug.exceptions import HTTPException, NotFound, InternalServerError

from arxiv.base import logging
from flask import render_template_string, current_app
import jinja2

from .services import index, site
from . import render
from .domain import Page, Component


logger = logging.getLogger(__name__)


docs = Blueprint('docs', __name__, url_prefix='/_docs',
                 static_folder='static',
                 template_folder='templates/docs')


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


class ComponentLoader(object):
    """Recursive attr-loader for components."""

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


class SchemaLoader(object):
    """Recursive attr-loader for schemas."""

    def __init__(self, key: str) -> None:
        """Initialize a loader with a key (path partial)."""
        self._key = key

    def __getattr__(self, key: str) -> Union['SchemaLoader', Component]:
        """Attempt to load a component by path."""
        path = '/'.join([self._key, key]).lstrip('/')
        try:
            schema = index.get_schema_by_path(path)
        except index.SchemaDoesNotExist:
            logger.debug(f'Could not load schema at {path}')
            return SchemaLoader(path)
        logger.debug(f'Loaded schema at {path}')
        return schema


def inject_components() -> Dict[str, ComponentLoader]:
    """Add a root-level component loader to the rendering context."""
    return {'components': ComponentLoader('')}


def inject_schemas() -> Dict[str, SchemaLoader]:
    """Add a root-level schema loader to the rendering context."""
    return {'schemas': SchemaLoader('')}


def get_blueprint(app: Flask) -> Blueprint:
    """Generate a blueprint for the site based on the app config."""
    site_name = app.config["SITE_NAME"]
    static_url_path = f'{app.static_url_path}/{site_name}'
    blueprint = Blueprint(site_name, __name__, url_prefix='',
                          static_folder=app.config['STATIC_ROOT'],
                          template_folder=app.config['TEMPLATE_ROOT'],
                          static_url_path=static_url_path)

    @blueprint.route('/search', methods=['GET'])
    def search():
        """Handle a search request."""
        q = request.args.get('q')
        results = index.find(q)
        try:
            return render_template(f'{site_name}/search.html',
                                   results=results, q=q)
        except jinja2.exceptions.TemplateNotFound:
            return render_template('docs/search.html', results=results, q=q)

    @blueprint.route('/', defaults={'path': ''})
    @blueprint.route('/<path:path>')
    def from_sitemap(path: str):
        """Route the request dynamically, based on the indexed site map."""
        logger.debug('Request for path: %s', path)
        try:
            page = index.get_by_path(path)
        except index.PageDoesNotExist as e:
            logger.debug('Page does not exist')
            raise NotFound('Page does not exist') from e

        try:
            content = site.content(page)
        except site.PageLoadFailed as e:
            raise InternalServerError('Could not load page') from e

        # We'll re-use this as part of the final template context, in case we
        # need it elsewhere.
        def _render_markdown(s: str) -> Markup:
            return Markup(render.render(s, get_link_dereferencer(page),
                                        get_static_dereferencer(page)))

        context = {
            'page': page,
            'pagetitle': page.title,
            'render_markdown': _render_markdown
        }
        rendered = render_template_string(_render_markdown(content), **context)

        context.update({'content': Markup(rendered)})
        if page.template is not None:
            template = page.template
        else:
            template = f'{site_name}/page.html'

        try:
            return render_template(template, **context)
        except jinja2.exceptions.TemplateNotFound:
            return render_template('docs/page.html', **context)

    blueprint.context_processor(inject_components)
    blueprint.context_processor(inject_schemas)
    return blueprint
