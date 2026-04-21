"""WCAG 2.2 patches for Material-theme markup that can't be reached via config.

Material renders five <label for="__drawer"|"__search"> elements that back a
CSS-only disclosure pattern. Three are mouse-only click catchers / visual state
indicators and should be hidden from the a11y tree; two are real icon buttons
and need accessible names. Applied via an on_post_page hook so no template
overrides are frozen against the theme.
"""

PATCHES = {
    # Material ships aria-label="Header" on this landmark, which just restates
    # the tag. Give it a name a landmarks-list user can actually distinguish.
    '<nav class="md-header__inner md-grid" aria-label="Header">':
        '<nav class="md-header__inner md-grid" aria-label="arXiv documentation">',
    '<label class="md-overlay" for="__drawer">':
        '<label class="md-overlay" for="__drawer" aria-hidden="true">',
    '<label class="md-search__overlay" for="__search">':
        '<label class="md-search__overlay" for="__search" aria-hidden="true">',
    '<label class="md-search__icon md-icon" for="__search">':
        '<label class="md-search__icon md-icon" for="__search" aria-hidden="true">',
    '<label class="md-header__button md-icon" for="__drawer">':
        '<label class="md-header__button md-icon" for="__drawer" aria-label="Open navigation menu">',
    '<label class="md-header__button md-icon" for="__search">':
        '<label class="md-header__button md-icon" for="__search" aria-label="Search">',
}


def on_post_page(output, page, config):
    for old, new in PATCHES.items():
        output = output.replace(old, new)
    return output
