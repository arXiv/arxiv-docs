# helm-upgrade-labs.sh
# Upgrade the content of labs.arxiv.org

# The docker image tag, generally a git commit tag.
#export TAG=...

export HELM_CHART=arxiv/marxdown
export HELM_RELEASE=labs-static
export NAMESPACE=default

helm upgrade $HELM_RELEASE $HELM_CHART \
--set=imageName=arxiv/labs \
--set=imageTag=$TAG \
--set=deploymentName=arxiv-$HELM_RELEASE \
--set=serviceName=arxiv-$HELM_RELEASE \
--set=ingressName=$HELM_RELEASE \
--set=host=labs.arxiv.org \
--set=namespace=$NAMESPACE \
--namespace $NAMESPACE \
--recreate-pods

