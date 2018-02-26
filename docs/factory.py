"""Application factory for references service components."""

import logging

from flask import Flask

from arxiv.base import Base
from docs import routes


def create_web_app() -> Flask:
    """Initialize an instance of the extractor backend service."""
    app = Flask('docs')
    app.config.from_pyfile('config.py')
    Base(app)
    app.register_blueprint(routes.blueprint)
    return app
