"""Build a site."""

import os
import shutil
from typing import List

from arxiv.base.globals import get_application_config
from docs.factory import create_web_app
from docs.domain import IndexablePage, Page
from docs.services import site, index
from docs.render import render

import bleach


def index_site() -> None:
    """Index the entire site."""
    app = create_web_app()
    with app.app_context():
        config = get_application_config()
        site_path = config['SITE_PATH']
        site_name = config['SITE_NAME']
        print(f'Building site from {site_path}')
        index.create_index()
        print('Created index')

        index.add_components(site.load_components(site_path))
        print('Added components')

        index.add_documents((
            (page, bleach.clean(render(page.content), strip=True, tags=[]))
            for page in site.load_all(site_path)
        ))
        print('Added pages')

        # Copy static files into Flask's static directory. If we're deploying
        # to a CDN, this should happen first so that Flask knows what it's
        # working with.
        static_root = app.blueprints['docs'].static_folder

        for path, source_path in site.load_static(site_path):
            target_path = os.path.abspath(os.path.join(static_root, path))

            # Make sure that the directory into which we're putting this static
            # file actually exists.
            target_dir, _ = os.path.split(target_path)
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)

            # This will overwrite whatever is already there.
            shutil.copy(os.path.abspath(source_path), target_path)
        print('Added static files')

        temp_root = os.path.join(
            app.root_path,
            os.path.split(app.blueprints['docs'].template_folder)[0]
        )
        print(f'Copy templates to {temp_root}')
        for path, source_path in site.load_templates(site_path):
            target_path = os.path.join(temp_root, site_name, path)
            print(temp_root, site_name, path, target_path)

            # Make sure that the directory into which we're putting this
            # template actually exists.
            target_dir, _ = os.path.split(target_path)
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
            print(path, target_path)
            # This will overwrite whatever is already there.
            shutil.copy(os.path.abspath(source_path), target_path)
        print('Added templates')


if __name__ == '__main__':
    index_site()
