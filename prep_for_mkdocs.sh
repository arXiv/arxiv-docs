set -eu
# script to setup for mkdocs
if [ ! -e ".git" ]
   then
       echo "Must run in root of arxiv-docs repo"
       exit 1
fi
   
# install py packages
pip3 install -q -r requirements.txt
echo "Installed requirements.txt"

# use arxiv-base to build mkdocs custom theme
mkdir -p mkdocs/arxiv_doc_theme
cd theme_generator
FLASK_APP=app.py flask generate mkdocs_template > ../mkdocs/arxiv_doc_theme/main.html
cd ..

echo "If successful the template is now in mkdocs/arxiv_doc_theme/main.html"

