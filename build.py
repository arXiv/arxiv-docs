"""Helper script for building a site; used in Docker build process."""

from arxiv.base.globals import get_application_config
from arxiv.docs.factory import create_web_app
from arxiv.docs.build import index_site

if __name__ == '__main__':
    app = create_web_app()
    with app.app_context():
        config = get_application_config()
        index_site(config['SITE_PATH'], config['SITE_NAME'], app.root_path,
                   app.blueprints['docs'].static_folder,
                   app.blueprints['docs'].template_folder)
