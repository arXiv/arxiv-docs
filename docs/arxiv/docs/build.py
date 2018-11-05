"""Build a site."""

import os
import shutil
from typing import List

from .domain import IndexablePage, Page
from .services import site, index
from .render import render

import bleach


def index_site(site_path: str, site_name: str, root_path: str,
               static_root: str, template_folder: str) -> None:
    """Index the entire site."""
    print(f'Building site from {site_path}')
    index.create_index()
    print('Created index')

    index.add_components(site.load_components(site_path))
    print('Added components')

    index.add_schemas(site.load_schemas(site_path))
    print('Added schemas')

    index.add_documents((
        (page, bleach.clean(render(page.content), strip=True, tags=[]))
        for page in site.load_all(site_path)
    ))
    print('Added pages')

    # Copy static files into Flask's static directory. If we're deploying
    # to a CDN, this should happen first so that Flask knows what it's
    # working with.
    for path, source_path in site.load_static(site_path):
        target_path = os.path.abspath(os.path.join(static_root, path))

        # Make sure that the directory into which we're putting this static
        # file actually exists.
        target_dir, _ = os.path.split(target_path)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        # This will overwrite whatever is already there.
        print(f"Static: copy {source_path} to {target_path}")
        shutil.copy(os.path.abspath(source_path), target_path)
    print('Added static files')

    temp_root = os.path.join(root_path, os.path.split(template_folder)[0])
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
