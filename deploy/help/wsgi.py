"""Web Server Gateway Interface entry-point."""

import os

from arxiv.marxdown.factory import create_web_app


__flask_app__ = create_web_app(
    build_path='/opt/arxiv/help/build',
    with_search=False,
    instance_path='/opt/arxiv/help/instance',
    static_url_path='/help/static'
)


def application(environ, start_response):
    """WSGI application factory."""
    for key, value in environ.items():
        if key == 'SERVER_NAME':
            continue
        os.environ[key] = str(value)
        __flask_app__.config[key] = str(value)
    return __flask_app__(environ, start_response)
