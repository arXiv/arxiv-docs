set -eu
# script to setup for mkdocs
if [ ! -e "arxiv_doc_theme" ]
   then
       echo "Must run in directory arxiv-docs/mkdocs"
       exit 1
fi
   
# install py packages
pip3 install -q -r requirements.txt
echo "Installed requirements.txt"

# use arxiv-base to build mkdocs custom theme
mkdir -p arxiv_doc_theme
cd theme_generator
FLASK_APP=app.py flask generate mkdocs_template > ../arxiv_doc_theme/main.html
cd ..

# mkdocs-material theme customizations via overrides
# https://squidfunk.github.io/mkdocs-material/customization/#overriding-blocks
mkdir -p overrides
cd theme_generator
FLASK_APP=app.py flask generate mkdocs_template > ../overrides/main.html
cd ..

echo "If successful the template is now in mkdocs/arxiv_doc_theme/main.html"

