#!/bin/bash
set -e

/usr/bin/uwsgi -H $(pipenv --venv) --static-map /static=${BUILD_PATH}/static --static-map /_docs/static=/opt/arxiv/docs/static "$@"
