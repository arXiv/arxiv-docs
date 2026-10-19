"""Generate the mkdocs theme override (overrides/main.html) with the design-system chrome.

The shared head/header/footer come from the arxiv-brand-templates package, pinned by
design-system SHA in prep_for_mkdocs.sh; mkdocs itself needs no design-system dependency.
Two Jinja levels: this plain Jinja environment expands the chrome now, writing its hosts
and asset route as mkdocs expressions; the `{% raw %}` blocks of templates/main.html are
evaluated later, by mkdocs build.

Usage (from make_arxiv_theme/):  python3 app.py > ../overrides/main.html
"""
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

import arxiv_brand


def main() -> int:
    env = Environment(loader=FileSystemLoader(Path(__file__).parent / "templates"))
    # The site-wide values are mkdocs expressions, written verbatim (no autoescape) and
    # resolved by each `mkdocs build` from mkdocs.yml's extras (ARXIV_HOST / INFO_HOST /
    # BRAND_STATIC_BASE), so one committed override serves prod, dev and a local preview.
    arxiv_brand.init_env(
        env,
        static_base="{{ config.extra.brand_static_base }}",
        base_url="{{ config.extra.arxiv_host }}",
        auth_url="{{ config.extra.arxiv_host }}",
        help_url="{{ config.extra.info_host }}",
    )
    sys.stdout.write(env.get_template("main.html").render(**arxiv_brand.context(
        # material's class keeps its search CSS working inside the shared header.
        header_variant="md-header",
        # info.arxiv.org has its own navigation and search.
        hide_nav=True,
    )))
    return 0


if __name__ == "__main__":
    sys.exit(main())
