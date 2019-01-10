import os
import shutil
import bleach
from .services import index, site, source
from . import render
from .domain import SourcePage, IndexablePage


from arxiv.base.globals import get_application_config as config


def generate_template(source_page: SourcePage, rendered_content: str) -> str:
    if source_page.template:
        page_template = source_page.template

    # Support for deleted slug (ARXIVNG-1545).
    elif 'response' in source_page.metadata \
            and source_page.metadata['response'].get('deleted', False):
        page_template = 'docs/deleted.html'
    else:
        page_template = 'docs/page.html'

    return '\n'.join([
        '{%- extends "' + page_template + '" %}',
        '{% block markdown_content %}',
        rendered_content,
        '{% endblock %}'
    ])


def build_site(with_search: bool = True) -> None:
    """Index the entire site."""
    to_index = []
    for source_page in source.load_pages():
        dereferencer = render.get_deferencer(source_page, site.get_site_name())
        rendered_content = render.render(source_page.content, dereferencer)
        template_content = generate_template(source_page, rendered_content)
        indexable_content = bleach.clean(rendered_content, strip=True, tags=[])
        to_index.append(IndexablePage(source_page, indexable_content))
        site.store_page_content(source_page.page_path, template_content)
        site.store_metadata(source_page.page_path, source_page.metadata)

    if with_search:
        index.create_index()
        print('Created index')
        index.add_documents(to_index)
        print('Added pages')

    # Copy static files into Flask's static directory. If we're deploying
    # to a CDN, this should happen first so that Flask knows what it's
    # working with.
    for static_path, source_path in source.load_static_paths():
        target_path = site.get_path_for_static(static_path)

        # Make sure that the directory into which we're putting this static
        # file actually exists.
        target_dir, _ = os.path.split(target_path)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        # This will overwrite whatever is already there.
        print(f"Static: copy {static_path} to {target_path}")
        shutil.copy(source_path, target_path)
        if with_search:
            index.add_static_file(static_path)
    print('Added static files')

    for template_path, source_path in source.load_template_paths():
        target_path = site.get_path_for_template(template_path)

        # Make sure that the directory into which we're putting this template
        # file actually exists.
        target_dir, _ = os.path.split(target_path)
        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        # This will overwrite whatever is already there.
        print(f"Template: copy {template_path} to {target_path}")
        shutil.copy(source_path, target_path)
    print('Added templates')
