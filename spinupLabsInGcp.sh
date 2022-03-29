#!/bin/bash


  ### Setup the VM with docker image ###
      # create the VM running the docker image for arxiv labs
      gcloud compute instances create-with-container labs-website-vm \
          --zone=us-east1-d --project=arxiv-labs \
          --container-image arxiv/labs:a0125a5bb5c6717c8d8a2e381b3f9dd0f9a49b42 \

      # add some tags to the VM instance
      gcloud compute instances add-tags labs-website-vm \
           --zone=us-east1-d --project=arxiv-labs \
           --tags=allow-health-check,allow-uwsgi-8000

      # Create the zonal network gorup for labs
      # port 8000 is defined in the uwsgi.ini for the labs docker image
      gcloud compute network-endpoint-groups create labs-website-neg \
          --zone=us-east1-d  --project=arxiv-labs\
          --default-port=8000

      # add the vm to that group
      gcloud compute network-endpoint-groups update labs-website-neg \
         --zone=us-east1-d --project=arxiv-labs \
         --add-endpoint 'instance=labs-website-vm'

      # allow health check from the GCP
      # see https://cloud.google.com/load-balancing/docs/https/ext-https-lb-simple#firewall
      # some how firewall rules don't have zones
      gcloud compute firewall-rules create fw-allow-health-check \
          --project=arxiv-labs \
          --network=default \
          --action=allow \
          --direction=ingress \
          --source-ranges=130.211.0.0/22,35.191.0.0/16 \
          --target-tags=allow-health-check \
          --rules=tcp:80

      # Using the pervious command as an example allow trafic on port 8000 to uwsgi
      gcloud compute firewall-rules create fw-allow-uwsgi-8000 \
          --project=arxiv-labs \
          --network=default \
          --action=allow \
          --direction=ingress \
          --source-ranges=130.211.0.0/22,35.191.0.0/16 \
          --target-tags=allow-uwsgi-8000 \
          --rules=tcp:8000

  ### upload SSL cert to GCP ###
if [ ! -e "labs.arxiv.org.key" ] 
then
  echo "The labs.arxiv.org.key is required. Get it from lastpass."
  exit 1
fi
if [ ! -e "labs.arxiv.org.crt" ] 
then
  echo "The labs.arxiv.org.crt is required. Get it from lastpass."
  exit 1
fi

  gcloud compute ssl-certificates create labs-ssl-cert \
      --project=arxiv-labs \
      --certificate=labs.arxiv.org.crt \
      --private-key=labs.arxiv.org.key \
      --global

  ### Setting up the load balancer ###

    # from https://cloud.google.com/load-balancing/docs/https/ext-https-lb-simple#load-balancer
    # Modified slightly for wsgi at port 8000
    # Also using info on using NEG from
    # https://cloud.google.com/load-balancing/docs/https/setting-up-https-serverless#creating_the_load_balancer

      # Create an IP address
      gcloud compute addresses create lb-ipv4-labs \
          --project=arxiv-labs \
          --ip-version=IPV4 \
          --global

      # Display the created IP
      gcloud compute addresses describe lb-ipv4-labs \
         --project=arxiv-labs \
          --format="get(address)" \
          --global


   # Need a health check for NEG
    gcloud compute health-checks create http labs-wsgi-8000-check \
       --project=arxiv-labs \
       --port 8000

    # Create a backend service.
    gcloud compute backend-services create labs-web-backend-service \
          --project=arxiv-labs \
         --health-checks=labs-wsgi-8000-check \
         --global

    # Create a URL map to route incoming requests to the backend service:
    # This becomes the name of the load balancer in the GCP UI
    gcloud compute url-maps create labs-url-map \
        --project=arxiv-labs \
        --default-service labs-web-backend-service

   # Add NEG as the backend to the backend service.
   gcloud compute backend-services add-backend labs-web-backend-service \
         --project=arxiv-labs \
         --network-endpoint-group=labs-website-neg \
         --network-endpoint-group-zone=us-east1-d \
         --balancing-mode=RATE --max-rate=10000 \
         --global

    # Create a target HTTP(S) proxy to route requests to your URL map.
    # For an HTTPS load balancer, create an HTTPS target proxy. The proxy
    # is the portion of the load balancer that holds the SSL certificate
    # for HTTPS Load Balancing, so you also load your certificate in this
    # step.
    gcloud compute target-https-proxies create labs-target-https-proxy \
      --project=arxiv-labs \
        --ssl-certificates=labs-ssl-cert \
        --url-map=labs-url-map

    # Create a global forwarding rule to route incoming requests to the proxy.
    gcloud compute forwarding-rules create labs-https-forwarding-rule \
       --project=arxiv-labs \
      --address=lb-ipv4-labs \
      --target-https-proxy=labs-target-https-proxy \
      --global \
      --ports=443

      #  Create a target HTTPS proxy to route requests to your URL map. 
      # The proxy is the portion of the load balancer that holds the SSL certificate 
      # for HTTPS Load Balancing, so you also load your certificate before this step.
      gcloud compute target-https-proxies create https-lb-proxy \
             --project=arxiv-labs \
             --url-map labs-url-map --ssl-certificates labs-ssl-cert

      # Create a global forwarding rule to route incoming requests to the proxy.
      gcloud compute forwarding-rules create https-content-rule \
         --project=arxiv-labs \
        --address=lb-ipv4-labs\
        --global \
        --target-https-proxy=https-lb-proxy \
        --ports=443

      # This last command often fails so maybe it is not needed.

      # If the load balancer doesn't work after about 60 sec.
      # to to the GCP UI, go to load balancer, go to the load balancer that
      # this script creates, click edit, click finalize and then save (or update)
