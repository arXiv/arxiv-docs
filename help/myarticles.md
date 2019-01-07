Using the `myarticles` widget
=============================

We have created a JavaScript widget that allows you to easily display
your articles on your website, using the magic of JSON and Atom. To the
right of this paragraph you should see an example of what this provides
for arXiv user [Simeon Warner](https://arxiv.org/a/0000-0002-7970-7855).
If you would like to use this functionality, you will need to [link an
ORCID identifier](/user/confirm_orcid_id) to your arXiv user account
**or** create an arXiv public [author identifier](author_identifiers.md)
The quickstart section below will get you up and running rapidly;
complete details follow the quickstart.

Quickstart
----------

First, you will need to figure out where on the webpage you would like
the arXiv atom feed information to be placed and add a
`<div id="arxivfeed"></div>` element. The arXiv data will be inserted
into this element (you may include HTML inside this element which will
be replaced when the data loads, for example this page has
`[Loading myarticles...]`). Next you will need to include the arXiv
JavaScript that will access arXiv, retrieve the list of your articles,
and then format and display the data on your page. Simply insert this:

```
<script type="text/javascript">
<!--
var arxiv_authorid = "yourauthorid";
//--></script>
<script type="text/javascript" src="https://arxiv.org/js/myarticles.js"></script> 
```

either in between the `<head>` and `</head>` tags or soon after the
`<body>` tag in your web page. The first script entry provides
configuration variables that controls what information is rendered on
your web page. The only required element is the **local** part of your
author id variable shown above as `yourauthorid`, such as
0000-0002-7970-7855 or warner\_s\_1. Make sure you leave the semicolon
at the end of that line. When you're ready to go your html should look
something like this:

```
<html>
<head>
<title>Dr. Nate's Page of accomplishments</title>
<script type="text/javascript">
<!--
var arxiv_authorid = "yourauthorid";
//--></script>
<style type="text/css">
div.arxivfeed {margin-bottom: 5px; width:700px;}
</style>
<script type="text/javascript" src="https://arxiv.org/js/myarticles.js">
</script>
</head>
<body>
<h1>Nate Rules!</h1>
<p>Stuff goes here</p>
<div id="arxivfeed"></div>
</body>
</html>
```

This will render the default feed using your authorid, as shown in the
box below aligned to the right side of the page as an example. If you'd
like to change how this looks, read about the configuration options
below. You can also look at the HTML source of this page as a guide.
This page is styled to use the sidebar display format, using a right
floated `div`.

<span id="config">Configuration options</span>
----------------------------------------------

The `myarticles` JavaScript widget has a number of configuration options
that you can set to control how the feed is rendered on your page. The
table below contains the variable names, their meaning and the default
settings. All arguments beside the `arxiv_authorid` variable are
optional.

| Variable name             | What does it do?                                                                                       | Allowed values                                                                                                                                   | Default value                 |
|---------------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------|
| `arxiv_authorid`          | Determines the feed content                                                                            | String that represents the local part of the arXiv ORCID-based identifier or arXiv author identifier (i.e. the part after https://arxiv.org/a/). | None                          |
| `arxiv_format`            | Controls the overall format of the feed                                                                | `arxiv` or `pretty`                                                                                                                              | `pretty`                      |
| `arxiv_max_entries`       | The maximum number of entries from the feed displayed                                                  | Integer 0 or higher (0 means all)                                                                                                                | `10`                          |
| `arxiv_includeTitle`      | If set to `1` displays the feed title                                                                  | `0` or `1`                                                                                                                                       | `1` (show title)              |
| `arxiv_includeSummary`    | If set to `1` displays the summary/abstract for each article                                           | `0` or `1`                                                                                                                                       | `0` (hide summary)            |
| `arxiv_includeComments`   | For `arxiv_format` = "arxiv". If set to `1` displays the comments field associated with each article.  | `0` or `1`                                                                                                                                       | `1` (show comments)           |
| `arxiv_includeSubjects`   | For `arxiv_format` = "arxiv". If set to `1` displays the arXiv subject categories for each article.    | `0` or `1`                                                                                                                                       | `1` (show subjects)           |
| `arxiv_includeJournalRef` | For `arxiv_format` = "arxiv". If set to `1` displays any journal reference associated with an article. | `0` or `1`                                                                                                                                       | `1` (show journal references) |
| `arxiv_includeDOI`        | For `arxiv_format` = "arxiv". If set to `1` displays and links any DOI associated with an article.     | `0` or `1`                                                                                                                                       | `1` (show DOIs)               |
| `arxiv_bg_color`          | For `arxiv_format` = `"pretty"`, background color                                                      | Any 6-digit hex color code                                                                                                                       | `85BC8F` (green)              |
| `arxiv_border_color`      | For `arxiv_format` = `"pretty"`, border color                                                          | Any 6-digit hex color code                                                                                                                       | `006400` (dark green)         |
| `arxiv_entry_color`       | For `arxiv_format` = `"pretty"`, background color of entries                                           | Any 6-digit hex color code                                                                                                                       | `FFFFFF` (white)              |

Setting the format/style with `arxiv_format`
--------------------------------------------

The `arxiv_format` variable sets the overall style of the output. This
may be set to `pretty` (the default if not specified) or to `arxiv`.

The `pretty` setting displays a compressed view of the feed in a 250
pixel (`250px`) wide box, designed primarily for use in a sidebar. The
background color for the heading bar and the border color of the box may
be adjusted with the `arxiv_bg_color` and `arxiv_border_color`
variables. The `arxiv_entry_color` variable refers to the background
color of each article listed. Generally, this format looks best without
the summaries displayed because otherwise the entries become very high
(because of the limited width).

The `arxiv` setting produces a display that looks similar to new
listings displayed on arXiv.org, for instance, the list of [new articles
in Quantitative Biology](/list/q-bio/new). In this format, display of
several fields may be turned on and off using the `includeTitle`,
`includeSummary`, `includeJournalRef` and `includeDOI` variables. This
display will fill the provided space. If you want to limit the width of
the display, apply a `width` style to the `div.arxivfeed` element in
your HTML page. A second [`myarticles` example page](myarticles_ex2.md)
shows the use of this format.

How does the widget get the data?
---------------------------------

arXiv provides an Atom feed for your author identifier which includes
information about all of the articles claimed under that author
identifier. Those Atom documents are available by appending `.atom` to
your author identifier, e.g. `https://arxiv.org/a/yourauthorid.atom`. We
have installed some server-side scripts that processes these feeds into
a [JSON](http://www.json.org/) feed which can then be processed using
Javascript and Direct Script Attachment (DSA). This is one of the data
formats used by Flickr and Yahoo and allows easy embedding of remote
content into a dynamic page. You can take a look at the
[JSONP](https://en.wikipedia.org/wiki/JSONP) feed used by myarticles.js
by going to `https://arxiv.org/a/yourauthorid.js`. If you take a look at
that datastream, you can see that it calls a function called
`jsonarXivFeed` with the contents of feed in an associative array. Our
JavaScript `myarticles.js` include provides the `jsonarXivFeed` function
which processes the HTML into the displayed format.If you prefer to use
unpadded JSON (without the `jsonarXivFeed` function call embedded in the
feed), you can use the following URI instead:
`https://arxiv.org/a/yourauthorid.json`. If you have a unique way you'd
like to process the data, you could write your own `jsonarXivFeed`
function as well! There are several tutorials out there that demonstrate
how to process the Flickr JSON feeds, you may find these helpful if you
decide to undertake processing of the JSON feed yourself. If you come up
with something neat, please let us know about it!

Note that while we intend to persist the author identifier URIs (of the
form `https://arxiv.org/a/yourauthorid`) and the Atom feed URIs (of the
form `https://arxiv.org/a/yourauthorid.atom`), the JSON feed URIs may
change at some stage and we will update the JavaScript to cope with
that.
