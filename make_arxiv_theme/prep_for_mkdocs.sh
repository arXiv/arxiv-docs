#!/bin/bash
set -eu

# script to setup for mkdocs
if [ ! -e ".git" ]
   then
       echo "Must run in root of arxiv-docs repo"
       exit 1
fi

BRANCH=${1:-master}
echo "Using template from arxiv-base branch: $BRANCH"

uv pip install git+https://github.com/arXiv/arxiv-base.git@$BRANCH

echo "Installed arxiv-base:$BRANCH"

#mkdir -p generated_arxiv_theme
cd make_arxiv_theme
FLASK_APP=app.py uv run flask generate mkdocs_template > ../overrides/main.html
echo "arxiv-base template is now in overrides/main.html"
