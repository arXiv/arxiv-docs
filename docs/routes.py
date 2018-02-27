import os

from flask import Blueprint, render_template, Markup, request
from werkzeug.exceptions import HTTPException, NotFound, InternalServerError

from docs.services import site, index


blueprint = Blueprint('docs', __name__, url_prefix='')


@blueprint.route('/search', methods=['GET'])
def search():
    """Handle a search request."""
    q = request.args.get('q')
    results = index.find(q)
    return render_template('docs/search.html', results=results, q=q)


@blueprint.route('/', defaults={'path': ''})
@blueprint.route('/<path:path>')
def from_sitemap(path: str):
    """Route the request dynamically, based on the site map."""
    try:
        page = site.load_page(path)
    except site.PageNotFound as e:
        raise NotFound('Nope') from e
    except site.PageLoadFailed as e:
        raise InternalServerError('Nope') from e
    context = dict(page=page, content=Markup(page.markdown),
                   pagetitle=page.title)
    return render_template('docs/page.html', **context)
