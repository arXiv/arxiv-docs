"""Install arXiv Docs package."""

from setuptools import setup, find_packages

setup(
    name='arxiv-docs',
    version='0.1.0',
    packages=[f'arxiv.{package}' for package
              in find_packages('./arxiv', exclude=['*test*'])],
    install_requires=[
        "flask",
        "markdown",
        "pyyaml",
        "whoosh",
        "arxiv-base",
        "bleach",
        "uwsgi",
        "python-frontmatter",
        "python-slugify",
        "Pygments"
    ],
    zip_safe=False,
    include_package_data=True
)
