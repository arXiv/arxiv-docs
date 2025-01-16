set -eu
# script to setup for mkdocs
if [ ! -e ".git" ]
   then
       echo "Must run in root of arxiv-docs repo"
       exit 1
fi
   
TMPVENV=./.template_venv
python3 -m venv $TMPVENV
. $TMPVENV/bin/activate
echo "Made temp venv and activated"

pip3 install git+https://github.com/arXiv/arxiv-base.git@656c8e841a2c610019f19fff8cc8d13d0983e377

echo "Installed arxiv-base"

mkdir -p generated_arxiv_theme
cd make_arxiv_theme
FLASK_APP=app.py flask generate mkdocs_template > ../overrides/main.html
cd ..

rm -rf $TMPVENV

echo "If successful the arxiv-base template is now in overrides/main.html"
