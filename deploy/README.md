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
