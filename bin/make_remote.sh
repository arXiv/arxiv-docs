#!/bin/bash

rm -rf ${BUILD_DIR}
mkdir ${BUILD_DIR}
cd ${BUILD_DIR}
git clone ${TARGET_REPO} .
git checkout ${SOURCE_REF}
ls -la
