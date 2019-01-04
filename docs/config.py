import os

SECRET_KEY = os.environ.get('SECRET_KEY', 'asdf1234')
# INDEX_NAME = os.environ.get('INDEX_NAME', 'idx')

SERVER_NAME = os.environ.get('DOCS_SERVER_NAME')

LOGLEVEL = os.environ.get('LOGLEVEL', 10)

VERSION = os.environ.get('VERSION')
SOURCE = os.environ.get('SOURCE')
"""GitHub repo containing the documentation source."""
BUILD_TIME = os.environ.get('BUILD_TIME')

STATIC_ROOT = os.environ.get('STATIC_ROOT', 'static')
TEMPLATE_ROOT = os.environ.get('TEMPLATE_ROOT', 'templates')

EXTERNAL_URL_SCHEME = os.environ.get('EXTERNAL_URL_SCHEME', 'https')
BASE_SERVER = os.environ.get('BASE_SERVER', 'arxiv.org')
URLS = [
    ("archive", "/archive/<archive>", BASE_SERVER),
    ("search_box", "/search", BASE_SERVER),
    ("clickthrough", "/ct", BASE_SERVER),
    ("search_archive", "/search/<archive>", BASE_SERVER),
    ("search_advanced", "/search/advanced", BASE_SERVER),
]


"""
Flask-S3 plugin settings.

See `<https://flask-s3.readthedocs.io/en/latest/>`_.
"""
FLASKS3_BUCKET_NAME = os.environ.get('FLASKS3_BUCKET_NAME', 'some_bucket')
# FLASKS3_CDN_DOMAIN = os.environ.get('FLASKS3_CDN_DOMAIN', 'static.arxiv.org')
FLASKS3_USE_HTTPS = os.environ.get('FLASKS3_USE_HTTPS', 1)
FLASKS3_FORCE_MIMETYPE = os.environ.get('FLASKS3_FORCE_MIMETYPE', 1)
FLASKS3_ACTIVE = int(os.environ.get('FLASKS3_ACTIVE', 0))

# AWS credentials.
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID', 'nope')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY', 'nope')
AWS_REGION = os.environ.get('AWS_REGION', 'us-east-1')

SOURCE_PATH = os.environ.get('SOURCE_PATH')
BUILD_PATH = os.environ.get('BUILD_PATH')
SITE_NAME = os.environ.get('SITE_NAME', 'arxiv')
SITE_URL_PREFIX = os.environ.get('SITE_URL_PREFIX', '/')
SITE_HUMAN_NAME = os.environ.get('SITE_HUMAN_NAME', 'arXiv Static Pages')
