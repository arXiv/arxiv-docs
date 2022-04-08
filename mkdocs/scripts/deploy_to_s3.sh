#!/bin/bash
set -e
if [  -e ".git" ]
then
       cd mkdocs
fi

if [ ! -e "mkdocs.yml" ]
then
   echo "Cannot find mkdocs.yml file, run this script in arxiv-docs or in arxiv-docs/mkdocs"
   exit 1
fi

if [ -z "$AWS_S3_BUCKET" ]; then
  echo "AWS_S3_BUCKET is not set."
  exit 1
fi

if [ -z "$AWS_ACCESS_KEY_ID" ]; then
  echo "AWS_ACCESS_KEY_ID is not set."
  exit 1
fi

if [ -z "$AWS_SECRET_ACCESS_KEY" ]; then
  echo "AWS_SECRET_ACCESS_KEY is not set."
  exit 1
fi

# Default to eu-west-1 if AWS_REGION not set.
if [ -z "$AWS_REGION" ]; then
  AWS_REGION="eu-west-1"
  echo "Using default region eu-west-1."
fi

echo "About to prep for mkdocs by building the theme"
./prep_for_mkdocs.sh
echo "Built the theme"

mkdocs build

pip install aws

# # Create a dedicated profile for this action to avoid conflicts
# # with past/future actions.
# aws configure --profile s3-sync-action <<-EOF > /dev/null 2>&1
# ${AWS_ACCESS_KEY_ID}
# ${AWS_SECRET_ACCESS_KEY}
# ${AWS_REGION}
# text
# EOF

SOURCE_DIR=site

# Sync using our dedicated profile and suppress verbose messages.
# All other flags are optional via the `args:` directive.
# might need --acl public-read in ENDPOINT_APPEND
aws s3 sync ${SOURCE_DIR:-.} s3://${AWS_S3_BUCKET}/${DEST_DIR} \
              --profile s3-sync-action \
              --no-progress \
              --acl public-read 

# Clear out credentials after we're done.
# We need to re-run `aws configure` with bogus input instead of
# deleting ~/.aws in case there are other credentials living there.
# https://forums.aws.amazon.com/thread.jspa?threadID=148833
# aws configure --profile s3-sync-action <<-EOF > /dev/null 2>&1
# null
# null
# null
# text
# EOF
