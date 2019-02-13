
export REPO_ORG=arxiv
export REPO_NAME=arxiv-docs
export TARGET_REPO=git@github.com:${REPO_ORG}/${REPO_NAME}.git
export SOURCE_REF=0.0.0
export SOURCE_DIR=help
export SITE_NAME=help
export SITE_HUMAN_NAME="arXiv Help Pages"
export IMAGE_NAME=arxiv/help
export TMP_DIR=/tmp/docs-build
export PROJECT_NAME=arXiv Static
export BUILD_TIME=`date`
export NOCACHE=`date +%s`


remote: Makefile
	./markdown/bin/make_remote.sh && \
		rm -rf ./markdown/source && mkdir ./markdown/source &&  \
		cp -R ${TMP_DIR}/${SOURCE_DIR}/* ./markdown/source && \
		docker build ./markdown/ \
			--build-arg NOCACHE=${NOCACHE} \
			--build-arg VERSION=${SOURCE_REF} \
			--build-arg BUILD_TIME=$(date) \
			--build-arg SOURCE=${REPO_ORG}/${REPO_NAME} \
			--build-arg SITE_NAME=${SITE_NAME} \
			--build-arg SITE_HUMAN_NAME=${SITE_HUMAN_NAME} \
		 	-f ./markdown/Dockerfile -t ${IMAGE_NAME}:${SOURCE_REF} && \
		rm -rf ./markdown/source

local: Makefile
	echo "Build locally at "${BUILD_TIME} && \
	rm -rf ./markdown/source && mkdir ./markdown/source &&  \
	cp -R ${SOURCE_DIR}/* ./markdown/source && \
	ls -la ./markdown/source && \
	docker build ./markdown/ \
		--build-arg NOCACHE=${NOCACHE} \
		--build-arg VERSION=${SOURCE_REF} \
		--build-arg BUILD_TIME="${BUILD_TIME}" \
		--build-arg SOURCE=${REPO_ORG}/${REPO_NAME} \
		--build-arg SITE_NAME=${SITE_NAME} \
		--build-arg SITE_HUMAN_NAME=${SITE_HUMAN_NAME} \
		-f ./markdown/Dockerfile -t ${IMAGE_NAME}:${SOURCE_REF} && \
	rm -rf ./markdown/source
