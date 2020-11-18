PROJECT=arxiv-labs
LOCATION=us-east1
gsutil mb -l $LOCATION -p $PRJECT gs://labs-develop-website/
gsutil mb -l $LOCATION -p $PRJECT gs://labs-master-website/

gsutil iam ch allUsers:objectViewer gs://labs-develop-website
gsutil iam ch allUsers:objectViewer gs://labs-master-website

gsutil web set -m index.html gs://labs-develop-website
gsutil web set -m index.html gs://labs-master-website

if [ -e "mkdocs/labs-site" ]
   then
       gsutil cp -r mkdocs/labs-site gs://labs-develop-website/
fi
if [ -e "mkdocs/labs-site" ]
   then
       gsutil cp -r mkdocs/labs-site gs://labs-master-website/
fi
