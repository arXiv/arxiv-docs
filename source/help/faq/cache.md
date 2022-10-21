# Caching accesses to arXiv.org

Many people have asked how to set up mirror sites of arXiv.org.
Unfortunately, mirror installations require significant maintenance and
we are working to reduce the size of our mirror network. Furthermore,
network "closeness" does not closely match geographical proximity so
geographically dispersed mirrors help far fewer users than one might
naively imagine.

There are other ways, however, to speed up your access. One solution now
is to use the Squid Cache in HTTPD Accelerator mode to pre-fetch new
papers each night and cache them.

When you start out you will get faster access to new papers each day,
since they have been pre-fetched. As time passes the store of papers in
the cache will grow continuously larger. Eventually you should have a
good fraction of the archive available. In principle nothing will be
removed from the cache until you have used up all the available disk
space, and then the least accessed files will be deleted to make room
for new ones.

Some of the advantages of the system are:

  - To the user, it looks like a mirror site, it works with any browser
    and you don't have to configure any PROXY settings.
  - It requires minimal system administration.
  - If you click on a file and then abort the download (e.g. by clicking
    "Stop") Squid will continue downloading the file in the background.
    If you return to the cache later the file should be available.
  - Squid will run comfortably on old hardware (say 10GB of disk space
    (more disk space would be better)).
  - Squid is free software

The disadvantages are:

  - Old papers won't be available from the cache until someone requests
    them once.
  - Searching and other interactive pages can't be cached.

## Setting up Squid as an HTTPD accelerator cache

For information on getting Squid see:

  - [The Squid homepage](http://www.squid-cache.org/)

Before setting up your cache send us e-mail telling us the hostname of
the machine you are using, so that we will recognize it in case of
problems.

It makes sense to have only one cache in each country or in each
network. Please check with other institutions in your country to
coordinate this. In particular, if one institution has a fast dedicated
internet connection to the US, then the cache should be located there.

Here is a suitable squid configuration file, optimized for caching pages
and files from arXiv.org:

  - [Example Squid configuration file](squid.conf)

The lines that you need to change are marked \*\*.

Here is a suitable script for downloading the new papers each night:

  - [Script for daily updates](daily.sh)

Again, lines you'll need to change are marked \*\*. If you think you
need to make other changes to the script it would be a good idea to
check with us before using them. Also please let us know if changes are
necessary for updates to Squid.

You will need GNU `wget` as part of the script and *YOU MUST COMPILE
wget WITH THE FOLLOWING PATCH TO AVOID SETTING OFF OUR ROBOT DETECTION
SYSTEM*:

  - [Patch against wget](wget_patch.txt) (1.10.2) to use correct
    user-agent string when checking `robots.txt` (this patch based on
    posts to the wget mailing list).

Assuming that you start from some directory with the
[wget](http://www.gnu.org/software/wget/) source files and the patch,
you should be able to patch and compile with:

    tmp# ls
    wget-1.10.2.tar.gz  wget_patch.txt
    tmp# tar -zxf wget-1.10.2.tar.gz
    wget-1.10.2.tar.gz   wget-1.10.2/
    tmp# cd wget-1.10.2
    tmp/wget-1.10.2# patch -p0 < ../wget_patch.txt
    patching file src/init.c
    patching file src/res.c
    tmp/wget-1.10.2# ./configure; make; make install
    ...

Set up the script to run on each day where there are new papers. The
news papers are available at 20:00 EDT/EST each Sunday, Monday, Tuesday,
Wednesday and Thursday.

You may want to make a backup of your cache occasionally, otherwise in
the event of a disk crash you would have to start over from scratch.

## Known bugs

The `Last-modified` headers for our postscript URLs are incorrect once
the file has been deleted from our own disk cache. This can be fixed in
principle.
