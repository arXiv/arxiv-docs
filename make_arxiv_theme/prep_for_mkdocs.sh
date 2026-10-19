#!/usr/bin/env bash
set -eu
# Regenerate overrides/main.html with the design-system chrome from DS_REF (a branch or SHA).
# Run from the arxiv-docs repo root:  ./make_arxiv_theme/prep_for_mkdocs.sh
if [ ! -e ".git" ]; then
    echo "Must run in root of arxiv-docs repo"
    exit 1
fi

# A local preview can take another repo or ref, e.g. DS_REPO=file://$HOME/git/design-system.
DS_REPO="${DS_REPO:-https://github.com/arXiv/design-system.git}"
DS_REF="${DS_REF:-master}"
SHA="$(git ls-remote "$DS_REPO" "refs/heads/$DS_REF" | cut -f1)"; SHA="${SHA:-$DS_REF}"

TMPVENV=./.template_venv
python3 -m venv "$TMPVENV"
. "$TMPVENV/bin/activate"
echo "Made temp venv and activated"

pip3 install --quiet --upgrade pip
pip3 install --quiet "git+${DS_REPO}@${SHA}#subdirectory=templates"  # brings jinja2
echo "Installed arxiv-brand-templates @ ${SHA}"

cd make_arxiv_theme
python3 app.py > ../overrides/main.html
cd ..

deactivate 2>/dev/null || true
rm -rf "$TMPVENV"

echo "Done. overrides/main.html regenerated from design-system ${SHA} (name it in the commit)."
