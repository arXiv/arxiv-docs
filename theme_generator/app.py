"""Provides application for getting header and footer."""

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

app = Flask('base_test')
app.config.from_object(config)
app.config['RELATIVE_STATIC_PATHS'] = 0
app.config['SERVER_NAME'] = 'arxiv.org'
Base(app)
app.register_blueprint(routes.blueprint)
blueprint = Blueprint('generate', __name__)


@blueprint.cli.command('mkdocs_template')
def mkdocs_template():
    """Render the template for use in mkdocs from arxiv-base."""
    with app.test_request_context(''):
        print(render_template('generate_mkdocs_template.html'))

@blueprint.cli.command('mkdocs_material_template')
def mkdocs_material_template():
    """Render the template for use in mkdocs-material from arxiv-base."""
    with app.test_request_context(''):
        print(render_template('generate_mkdocs_material_template.html'))

@blueprint.cli.command('mkdocs_material_footer')
def mkdocs_material_footer():
    """Render the template for use in mkdocs-material from arxiv-base."""
    with app.test_request_context(''):
        print(render_template('generate_mkdocs_footer.html'))

app.register_blueprint(blueprint)
s3.init_app(app)
