
export REPO_ORG=cul-it
export REPO_NAME=arxiv-docs
export TARGET_REPO=git@github.com:${REPO_ORG}/${REPO_NAME}.git
export SOURCE_REF=0.0.0
export SOURCE_DIR=site
export TARGET_DIR=site
export IMAGE_NAME=arxiv/site
export BUILD_DIR=/tmp/docs-build
export PROJECT_NAME=arXiv Static
export BUILD_TIME=`date`
export NOCACHE=`date +%s`


remote: Makefile
	./bin/make_remote.sh && \
		cp -R ${BUILD_DIR}/${SOURCE_DIR}/* ./build/${TARGET_DIR} && \
		docker build ./ \
			--build-arg NOCACHE=${NOCACHE} \
			--build-arg VERSION=${SOURCE_REF} \
			--build-arg BUILD_TIME=$(date) \
			--build-arg SOURCE=${REPO_ORG}/${REPO_NAME} \
			--build-arg SITE_NAME=${TARGET_DIR} \
		 	-f ./Dockerfile -t ${IMAGE_NAME}:${SOURCE_REF}

local: Makefile
	echo "Build locally at "${BUILD_TIME} && \
	rm -rf ./build && \
	mkdir ./build && mkdir ./build/${TARGET_DIR} && \
	cp -R ${SOURCE_DIR}/* ./build/${TARGET_DIR} && \
	ls -la ./build && \
	docker build ./ \
		--build-arg NOCACHE=${NOCACHE} \
		--build-arg VERSION=${SOURCE_REF} \
		--build-arg BUILD_TIME="${BUILD_TIME}" \
		--build-arg SOURCE=${REPO_ORG}/${REPO_NAME} \
		--build-arg SITE_NAME=${TARGET_DIR} \
		-f ./Dockerfile -t ${IMAGE_NAME}:${SOURCE_REF}
