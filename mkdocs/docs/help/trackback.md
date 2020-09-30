Trackbacks
==========

arXiv.org supports the
[Trackback](http://en.wikipedia.org/wiki/Trackback) standard. By sending
a trackback, you can notify arXiv.org that you've created a web page
that references a particular paper. You can view [recent
trackbacks.](https://arxiv.org/tb/recent)

You can send a trackback to our system by giving your blogging software
the following *trackback URL*:

`https://arxiv.org/trackback/paper_id`

Our abstract pages support trackback autodiscovery: some software such as
[Movable Type](http://www.sixapart.com/movabletype/) can send trackbacks automatically
when you link to our abstract pages. Note that [WordPress](http://www.wordpress.org) only
is capable of sending "pingbacks" automatically, which are not supported by arXiv. Instead see
[their help page](https://make.wordpress.org/support/user-manual/building-your-wordpress-community/trackbacks-and-pingbacks/#trackbacks)
 for proper configuration of your blog.

-   Trackbacks will not be immediately visible. Because of widespread
    [Trackback
    spam](http://www.theregister.co.uk/2005/01/31/link_spamer_interview/)
    we have a semi-automated *editorial process* that approves
    trackbacks for display. Trackbacks from known blogs should become
    visible in a few minutes, but it may take longer for us to recognize
    new blogs.
-   We reserve the right to reject trackbacks for any reason.
-   Trackback autodiscovery is only implemented on URLs of the form
    `https://arxiv.org/abs/article_id` and NOT on URLs of the format
    `https://arxiv.org/paper_id` or on PDF or other full-text formats.
    Bloggers will get best results if they link only to the official
    abstract page.
-   Trackbacks recorded for an article may be seen from URIs of the form
    <https://arxiv.org/tb/0704.0002> where [0704.0002](/abs/0704.0002) is
    the article id.

Trackback Data [data]
--------------

Data for all accepted trackbacks can be downloaded in RDF serialized as
[Turtle](http://www.w3.org/TR/turtle/) according to the [Open Annotation
Data Model](http://www.openannotation.org/spec/core/) for machine
consumption. The data is organized by the article id that the trackback
or trackbacks apply to, according to the URI pattern:

`http://export.arxiv.org/data/trackbacks/trackback_paper_id.ttl`

For example, for [0704.0002](/abs/0704.0002) the URI is:

<http://export.arxiv.org/data/trackbacks/trackback_0704.0002.ttl>.

To enable harvesting of the complete set of trackback data there is a
[ResourceSync](http://www.openarchives.org/rs/1.0/resourcesync)
compatible sitemap listing the complete set of trackback data files at:
<http://export.arxiv.org/data/trackbacks/resourcelist.xml>. One easy way
to synchronize the set of data is with the
[`resync`](https://pypi.python.org/pypi/resync) client. For example, to
copy or sync to a local directory called `arxiv_trackbacks` one may use:
```
    > resync http://export.arxiv.org/data/trackbacks arxiv_trackbacks
    Status:     NOT IN SYNC (same=28835, to create=1951, to update=0, to delete=0)
    Will GET 1951 resources
    Status:          SYNCED (same=28835, created=1951, updated=0, deleted=0)
```
(where in the example above the data had previously been copied to the
`arxiv_trackbacks` directory but 1951 new resources were downloaded to
bring the copy into sync.)
