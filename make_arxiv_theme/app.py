"""Provides application for getting header and footer."""

import sys

import logging
logger = logging.getLogger(__file__)

if sys.version_info.major != 3 and sys.version_info.minor < 11:
    logger.error("****************************** ERROR ******************************")
    logger.error("You must use python version 3.11 to match the version used by arxiv-base")
    logger.error("Changed from 3.10 to 3.11 2025-01-15 by Brian Caruso")
    logger.error("****************************** ERROR ******************************")
    sys.exit(1)

from flask import Flask, Blueprint, render_template, current_app
from arxiv.base import Base, routes, config
from flask_s3 import FlaskS3

s3 = FlaskS3()
config.FLASKS3_ACTIVE = True
config.FLASKS3_DEBUG = False
config.FLASKS3_BUCKET_NAME = 'arxiv-web-static1'
config.FLASKS3_CDN_DOMAIN = 'static.arxiv.org'
config.FLASKS3_USE_HTTPS = True
config.BASE_SERVER = 'arxiv.org'

app = Flask('browse')
app.config.from_object(config)
app.config['RELATIVE_STATIC_PATHS'] = 0
app.config['SERVER_NAME'] = 'arxiv.org'
app.config['APP_VERSION'] = '0.3.4'  # Forces a version for the static cdn
app.name = 'browse'
Base(app)
app.register_blueprint(routes.blueprint)
blueprint = Blueprint('generate', __name__)

@blueprint.cli.command('mkdocs_template')
def mkdocs_template():
    """Render the template for use in mkdocs from arxiv-base."""
    try:
        with app.test_request_context(''):
            class fakemacros:
                compactsearch = lambda a,b: ''

            print(render_template('main.html', macros=fakemacros()))
    except Exception:
        logger.exception("Problem making template")
        sys.exit(1)

app.register_blueprint(blueprint)
s3.init_app(app)
