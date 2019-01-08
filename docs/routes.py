from typing import Dict, Callable
from urllib.parse import urljoin, urlparse, parse_qs, urlencode, urlunparse
from werkzeug.urls import Href, url_encode, url_parse, url_unparse, url_encode

from flask_s3 import url_for as s3_url_for
from flask import Blueprint, render_template_string, request, \
    render_template, Response, current_app, url_for
import jinja2
from werkzeug.exceptions import NotFound

from arxiv import status
from . import render
from .services import site, index


def from_sitemap(page_path: str = ''):
    try:
        page = site.load_page(page_path)
    except site.PageNotFound:
        raise NotFound('No such page')

    if current_app.config['FLASKS3_ACTIVE']:
        this_url_for = s3_url_for
    else:
        this_url_for = url_for

    # Support for response parameters in page frontmatter. This is to support
    # stubs for deleted/moved pages (ARXIVNG-1545).
    code: int = status.HTTP_200_OK
    deleted: bool = False
    headers = {}
    if 'response' in page.metadata:
        code = page.metadata['response'].get('status', status.HTTP_200_OK)
        if 'location' in page.metadata['response']:
            linker = render.get_linker(page, site.get_site_name())
            route, kwarg, name = linker(page.metadata['response']['location'])
            headers['Location'] = this_url_for(route, **{kwarg: name})
        deleted = page.metadata['response'].get('deleted', False)
        if deleted:
            code = status.HTTP_404_NOT_FOUND

    context = dict(page.metadata)
    context.update({
        'page_path': page_path,
        'page': page,
        'site_name': site.get_site_name(),
        'url_for': this_url_for
    })

    if deleted:
        content = render_template('docs/deleted.html', **context)
    else:
        content = render_template_string(page.content, **context)
    return content, code, headers


def search():
    """Handle a search request."""
    q = request.args.get('q')
    limit = min(int(request.args.get('l', 20)), 50)
    page_number = int(request.args.get('p', 1))
    if q:
        results = index.find(q, page_number=page_number, limit=limit)
    else:
        results = None
    site_name = site.get_site_name()
    context = dict(results=results, q=q, site_name=site_name)
    try:
        return render_template(f'{site_name}/search.html', **context)
    except jinja2.exceptions.TemplateNotFound:
        return render_template('docs/search.html', **context)


def url_for_page_builder() -> Dict[str, Callable]:
    """Add a page URL builder function to the template context."""
    def url_for_page(page: int) -> str:
        """Build an URL to for a search result page."""
        rule = request.url_rule
        parts = url_parse(url_for(rule.endpoint))
        args = request.args.copy()
        args['p'] = page
        parts = parts.replace(query=url_encode(args))
        url: str = url_unparse(parts)
        return url
    return dict(url_for_page=url_for_page)


def get_blueprint(site_path: str) -> Blueprint:
    blueprint = Blueprint(site.get_site_name(), __name__,
                          url_prefix=site.get_url_prefix(),
                          static_folder=site.get_static_path(),
                          template_folder=site.get_templates_path(),
                          static_url_path='static')
    blueprint.route('/')(from_sitemap)
    blueprint.route('/<path:page_path>')(from_sitemap)
    blueprint.route('/search', methods=['GET'])(search)
    blueprint.context_processor(url_for_page_builder)
    blueprint.context_processor(
        lambda: {'site_human_name': site.get_site_human_name()}
    )
    return blueprint


docs = Blueprint('docs', __name__, url_prefix='/_docs',
                 static_folder='static',
                 template_folder='templates',
                 static_url_path='static')
