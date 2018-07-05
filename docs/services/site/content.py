"""Markdown extensions."""
import os
from typing import Mapping
import xml.etree.ElementTree as ET
from markdown import markdown, Markdown
from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor

from arxiv.base.globals import get_application_config
from . import sitemap
from .exceptions import PageLoadFailed


def load(content_path: str) -> str:
    """Load the page at a relative path."""
    try:
        with open(_abs_path(content_path)) as f:
            content = markdown(f.read(), extensions=[SlugAnchorExtension()])
    except IOError as e:
        raise PageLoadFailed('Failed to load page') from e
    return content


def _abs_path(relative_path: str) -> str:
    root = get_application_config()['SITE_PATH']
    return os.path.join(root, relative_path)


class SlugAnchorProcessor(Treeprocessor):
    """Convert slug links to full paths."""

    def run(self, root: ET.ElementTree) -> None:
        """Perform link conversion on ``root``."""
        self.translate_slug_anchors(root)

    def translate_slug_anchors(self, element: ET.Element) -> None:
        """Traverse ``element`` looking for and updating anchor elements."""
        for child in element:
            if child.tag == "a":
                href = child.attrib.get('href')
                try:
                    child.attrib['href'] = sitemap.slug_path(href)
                except KeyError:
                    continue
            self.translate_slug_anchors(child)


class SlugAnchorExtension(Extension):
    """Adds :class:`.SlugAnchorProcessor` to the markdown processor."""

    def extendMarkdown(self, md: Markdown, md_globals: Mapping) -> None:
        """Add :class:`.SlugAnchorProcessor` to the markdown processor."""
        md.treeprocessors['slugAnchorProcessor'] = SlugAnchorProcessor()
