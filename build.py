"""Index the site."""

import os
from typing import List

from docs.factory import create_web_app
from docs.domain import IndexablePage, Page
from docs.services import site, index

import bleach


def index_site() -> None:
    """Index the entire site."""
    app = create_web_app()
    app.app_context().push()
    index.create_index()

    indexable: List[IndexablePage] = []
    for path in site.list_paths():
        page: Page = site.load_page(path)
        content = bleach.clean(page.markdown, strip=True, tags=[])
        indexable.append(IndexablePage(
            title=page.title,
            path=page.path,
            content=content
        ))
    index.add_documents(*indexable)


if __name__ == '__main__':
    index_site()
