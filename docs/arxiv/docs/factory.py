"""Application factory for references service components."""

import logging

from flask import Flask

from arxiv.base import Base
from . import routes


def create_web_app() -> Flask:
    """Initialize an instance of the static pages application."""
    from . import config

    app = Flask(config.SITE_NAME)
    app.config.from_object(config)

    Base(app)

    app.register_blueprint(routes.docs)
    # app.register_blueprint(routes.blueprint)
    app.register_blueprint(routes.get_blueprint(app))
    return app
