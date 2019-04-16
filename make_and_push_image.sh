#!/bin/bash

set -o pipefail
set -o errexit
set -o nounset

# Used to deploy

export SOURCE_DIR=$1
export LOGLEVEL=40
export SITE_NAME=$SOURCE_DIR
export IMAGE_NAME=arxiv/${SOURCE_DIR}
if [ -z "${TRAVIS_TAG}" ]; then
    export SOURCE_REF=${TRAVIS_COMMIT}
else
    export SOURCE_REF=${TRAVIS_TAG}
fi

git fetch --unshallow || echo "Repository is already complete"
docker login -u "$DOCKERHUB_USERNAME" -p "$DOCKERHUB_PASSWORD"
make local
docker push ${IMAGE_NAME}:${SOURCE_REF}
