<pre>
#!/bin/sh
#
# Script to preload Squid caching proxy with new context from 
# arXiv.org. See: http://arxiv.org/help/faq/cache
# $Id: daily.sh,v 1.3 2007/09/12 22:24:44 arxiv Exp $

LOCAL_SITE="www.your.proxy"       # ** the name of the site where you're running squid
EMAIL_CONTACT="email@your.domain" # ** fill in contact email in even of trouble

TMPDIR="/tmp/proxy-$$"            # ** change to other local tmp dir if necessary

mkdir -p $TMPDIR
cd $TMPDIR || exit

# Note: Don't increase the level above 2. Going beyond 2 links would try to
# download the whole site every night!
#
# If you have problems understanding what is going on, use the -d and -v flags
# to get (very) verbose debugging information.

wget -U 'SQUID_configured_as_described_at_/help/faq/cache' \
     --header="From: $EMAIL_CONTACT" \
     --wait=20 --tries=1 --level=2 -r -nd \
     -I '/abs,/list,/pdf' --delete-after http://$LOCAL_SITE/

rm -f $TMPDIR/*
cd .. ; rmdir $TMPDIR
</pre>
