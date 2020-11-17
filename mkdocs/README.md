# Static Site Generation with mkdocs

## How to generate and preview
  python -m venv /tmp/mkdocsvenv
  source /tmp/mkdocsvenv/bin/activate
  ./prep_for_mkdocs.sh
  cd mkdocs
  mkdocs serve
  # At this point the static sites are in mkdics/docs
