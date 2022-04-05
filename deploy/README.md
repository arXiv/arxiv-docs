# Deploy to dev.labs.arxiv.org and labs.arxiv.org on GCP

## Initial setup
1. In GCP, create a project (arxiv-labs)
1. sh deploy/labsongcp.sh
1. Then in the GCP console, create a build trigger in cloud build that
   triggers on changes to arxiv-docs develop. Skip the default trigger.
   The create a trigger that is only for develop.
1. Follow the tutoral for setting up a bucket as a web site.
1. Change the CNAME of labs.arxiv.org in AWS route53 to point at the
   load balancer IP for the master bucket and the CNAME for
   dev.labs.arxiv.org at the load balancer IP for the develop bucket.

# How to build the image
1. cd arxiv-docs
1. export TAG=  ...Find a commit tag in git for the docker image tag.
1. docker build . -t arxiv/labs:$TAG -f ./Dockerfile-labs
1. docker push arxiv/labs:$TAG
1. docker run -it -p 8000:8000 arxiv/labs:$TAG
