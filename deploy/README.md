# Deploy

## Deploy to labs.arxiv.org

### Build the image
1. cd arxiv-docs
1. export TAG=  ...Find a commit tag in git for the docker image tag.
1. docker build . -t arxiv/labs:$TAG -f ./Dockerfile-labs
1. docker push arxiv/labs:$TAG
1. docker run -it -p 8000:8000 arxiv/labs:$TAG

### Deploy the image
1. ssh arxiv-bastion
1. helm ls | grep labs-static
1. export TAG=  ...the docker image tag.
1. sh deploy/helm_upgrade_labs.sh

## Deploy to dev.labs.arxiv.org

### Initial setup
In GCP, create a project (arxiv-labs), create a bucket
(labs-dev-website), add public permission to that bucket, and set that
bucket to be a website.

    gsutil cp -r mkdocs/labs-site gs://labs-dev-website/
    gsutil web set -m index.html gs://labs-dev-website
    gsutil iam ch allUsers:objectViewer gs://labs-dev-website

Then in the GCP console, create a build trigger in cloud build that
triggers on changes to arxiv-docs develop. Skip the default trigger.
The create a trigger that is only for develop.

