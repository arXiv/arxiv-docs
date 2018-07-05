from typing import List
from . import sitemap, content
from ...domain import Page

from .exceptions import PageNotFound, PageLoadFailed


def load_page(path: str) -> Page:
    """Load a :class:`.Page` from ``path``."""
    # path = path.strip('/')
    full_path, elem = sitemap.find_page(path)
    elem['markdown'] = content.load(elem['content_path'])
    elem['parents'] = _get_parents(path)
    return Page(path=full_path, **elem)


def _get_parents(path: str) -> List[Page]:
    parents = []
    if path != '':
        fpath = ''
        for part in path.rstrip('/').split('/'):
            fpath = f'{fpath}/{part}'.strip('/')
            ppath, pelem = sitemap.find_page(fpath)
            pelem['parents'] = None
            pelem['markdown'] = None
            parents.append(Page(path=ppath, **pelem))
    return parents
