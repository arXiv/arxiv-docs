class PageLoadFailed(Exception):
    """Could not load the content of a page."""


class PageNotFound(Exception):
    """Attempted to load a page that does not exist."""
