"""UI routes for the documents service."""

import os
from typing import Callable
from flask import Blueprint, render_template, Markup, request, url_for
from werkzeug.exceptions import HTTPException, NotFound, InternalServerError

from docs.services import index, site
from docs.render import render
from .domain import Page


blueprint = Blueprint('docs', __name__, url_prefix='', static_folder='static')


def link_dereferencer(href: str) -> str:
    """Link dereferencer for use during HTML rendering."""
    if not href or href.startswith('http'):
        return href
    try:
        path = index.get_by_slug(href).path
    except index.PageDoesNotExist:
        try:
            path = index.get_by_path(href).path
        except index.PageDoesNotExist:
            return href
    return url_for('docs.from_sitemap', path=path)


def get_static_dereferencer(page: Page) -> Callable:
    """Generate a dereferencer function for static files relative to a page."""
    def static_deferencer(src: str) -> str:
        """Static URL dereferencer for use during HTML rendering."""
        if not src or src.startswith('http'):
            return src
        filename = "/".join(page.path.split('/')[:-1] + [src])
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

    static_dereferencer = get_static_dereferencer(page)
    rendered = render(content, link_dereferencer, static_dereferencer)

    context = dict(page=page, content=Markup(rendered), pagetitle=page.title)
    return render_template('docs/page.html', **context)
