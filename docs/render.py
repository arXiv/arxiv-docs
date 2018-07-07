"""Responsible for rendering markdown content to HTML."""

from typing import Callable, Optional, Mapping
import xml.etree.ElementTree as ET
from markdown import markdown, Markdown
from markdown.extensions import Extension
from markdown.treeprocessors import Treeprocessor


def render(content: str, dereferencer: Optional[Callable] = None,
           static_dereferencer: Optional[Callable] = None) -> str:
    """
    Render markdown content to HTML.

    Parameters
    ----------
    content : str
        Markdown content.
    dereferencer : function
        Used for generating URLs from internal paths and slugs. Should accept
        a HREF value (str), and return a URL (str). Optional.
    static_dereferencer : function
        Used for generating URLs for static files. Should accept
        a src value (str), and return a URL (str). Optional.

    Returns
    -------
    str
        Rendered HTML.

    """
    extensions = []
    if dereferencer is not None:
        extensions.append(ReferenceExtension('a', 'href', dereferencer))
    if static_dereferencer is not None:
        extensions.append(
            ReferenceExtension('img', 'src', static_dereferencer)
        )
    return markdown(content, extensions=extensions)


class ReferenceProcessor(Treeprocessor):
    """Convert internal links to full paths."""

    def __init__(self, tag: str, attr: str,
                 dereferencer: Optional[Callable] = None) -> None:
        """Set the link dereferencer for use during processing."""
        self.dereferencer = dereferencer
        self.tag = tag
        self.attr = attr

    def run(self, root: ET.ElementTree) -> None:
        """Perform link conversion on ``root``."""
        if self.dereferencer is not None:
            self.translate_anchors(root)

    def translate_anchors(self, element: ET.Element) -> None:
        """Traverse ``element`` looking for and updating anchor elements."""
        for child in element:
            if child.tag == self.tag:
                value = child.attrib.get(self.attr)
                try:
                    child.attrib[self.attr] = self.dereferencer(value)
                except KeyError:
                    continue
            self.translate_anchors(child)


class ReferenceExtension(Extension):
    """Adds :class:`.ReferenceProcessor` to the markdown processor."""

    def __init__(self, tag: str, attr: str, dereferencer: Optional[Callable]) -> None:
        """Set the link dereferencer for use during processing."""
        self.tag = tag
        self.attr = attr
        self.dereferencer = dereferencer

    def extendMarkdown(self, md: Markdown, md_globals: Mapping) -> None:
        """Add :class:`.ReferenceProcessor` to the markdown processor."""
        inst = ReferenceProcessor(self.tag, self.attr, self.dereferencer)
        md.treeprocessors[f'{self.tag}_{self.attr}_reference_processor'] = inst
