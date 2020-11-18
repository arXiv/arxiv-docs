set -e

# Gets required python libraries and builds labs site.

if [ ! -e ".git" ]
then
    echo "Must run in root of arxiv-docs repo"
    exit 1
fi

if [ -f "/etc/debian_version" ]
then
    # install some build tools needed in GCP
    sudo apt-get install python3-dev python3-pip python3-venv python3-wheel -y
fi

VIRTUAL_ENV=/tmp/arxiv-docs-venv
python3 -m venv $VIRTUAL_ENV
PATH="$VIRTUAL_ENV/bin:$PATH"

. prep_for_mkdocs.sh

cd mkdocs
mkdocs build --config-file ./mkdocs-labs.yml
cd ..
echo "*** mkdocs is now in $(pwd)/labs-site"
