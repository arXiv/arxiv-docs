set -eu
# script to setup for mkdocs

# install py packages
pip3 install -q -r requirements.txt
echo "Installed requirements.txt"

# mkdocs-material theme customizations via overrides
# https://squidfunk.github.io/mkdocs-material/customization/#overriding-blocks
mkdir -p overrides
cd theme_generator
FLASK_APP=app.py flask generate mkdocs_material_template > ../overrides/main.html
#FLASK_APP=app.py flask generate mkdocs_material_footer > ../overrides/partials/footer.html
cd ..

echo "If successful the template is now in ./overrides/"
