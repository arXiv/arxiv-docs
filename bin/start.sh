#!/bin/bash
set -e

/usr/bin/uwsgi -H $(pipenv --venv) --static-map /images=/var/www/img "$@"
