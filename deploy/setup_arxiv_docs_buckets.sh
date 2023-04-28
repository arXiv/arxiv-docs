# Script to setup the arxiv-docs and arxiv-docs-prs buckets

PROJECT=arxiv-production
LOCATION=us-east1
gsutil mb -l $LOCATION -p $PRJECT gs://arxiv-docs
gsutil mb -l $LOCATION -p $PRJECT gs://arxiv-docs-prs

gsutil iam ch allUsers:objectViewer gs://arxiv-docs
gsutil iam ch allUsers:objectViewer gs://arxiv-docs-prs

# The bucket needs to be configured to use index.html pages for bare
# paths (that is /about is redirected to /about/index.html) and the 404
# page:

gsutil web set -m index.html -e 404.html gs://arxiv-docs
gsutil web set -m index.html -e 404.html gs://arxiv-docs-prs
