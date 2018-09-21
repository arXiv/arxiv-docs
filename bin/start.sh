#!/bin/bash
set -e

/usr/bin/uwsgi -H $(pipenv --venv) "$@"
