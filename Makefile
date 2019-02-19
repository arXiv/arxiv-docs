REPO_ORG?=arxiv
REPO_NAME?=arxiv-docs
REPO_PATH?=.
TARGET_REPO?=git@github.com:${REPO_ORG}/${REPO_NAME}.git
SOURCE_REF?=0.0.0
SOURCE_DIR?=help
SITE_NAME?=help
SITE_HUMAN_NAME?="arXiv Help Pages"
SITE_HUMAN_SHORT_NAME?=Help
SITE_SEARCH_ENABLED?=1
IMAGE_NAME?=arxiv/help
BUILD_TIME?=$(date)
NOCACHE?=`date +%s`

local: Makefile
	echo "Build locally at "${BUILD_TIME}
	rm -rf ./build
	mkdir ./build
	mkdir ./build/${SOURCE_DIR}
	cp -R ${REPO_PATH}/${SOURCE_DIR}/* ./build/${SOURCE_DIR}/
	cp -R ${REPO_PATH}/.git ./build
	docker build . \
		--build-arg NOCACHE=${NOCACHE} \
		--build-arg VERSION=${SOURCE_REF} \
		--build-arg BUILD_TIME="${BUILD_TIME}" \
		--build-arg SOURCE=${REPO_ORG}/${REPO_NAME} \
		--build-arg SOURCE_DIR=${SOURCE_DIR} \
		--build-arg SITE_SEARCH_ENABLED=${SITE_SEARCH_ENABLED} \
		--build-arg SITE_NAME=${SITE_NAME} \
		--build-arg SITE_HUMAN_NAME='${SITE_HUMAN_NAME}' \
		--build-arg SITE_HUMAN_SHORT_NAME=${SITE_HUMAN_SHORT_NAME} \
		-f ./Dockerfile -t ${IMAGE_NAME}:${SOURCE_REF}
	rm -rf ./build
