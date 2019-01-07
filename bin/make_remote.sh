#!/bin/bash

rm -rf ${TMP_DIR}
mkdir ${TMP_DIR}
cd ${TMP_DIR}
git clone ${TARGET_REPO} .
git checkout ${SOURCE_REF}
ls -la
