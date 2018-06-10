OpenURL linking services
========================

arXiv supports OpenURL linking services by allowing users to set a
cookie which instructs arXiv to add an OpenURL link to the abstract
pages. We support both the OpenURL
[0.1](http://www.exlibrisgroup.com/sfx_openurl_syntax.htm) and
[1.0](http://library.caltech.edu/openurl/Standard.htm) specifications.

You may [enable or disable OpenURL links](/openurl-cookie). This service
is currently available only for the main site and the LANL mirror (the
link will not work on other mirrors, 24Sep2002). Note that OpenURL
settings are specific to both the machine your browser is running on and
to the arXiv site you are accessing.

Policy
------

Current arXiv policy allows individual users to set a cookie to enable
OpenURL links for their local or preferred linking service. If you have
difficulty getting arXiv's OpenURL links to work with a particular
linking service, please contact the operators or vendors of that linking
service in the first instance. If problems remain, be sure to include
all appropriate technical details in any communication with arXiv.

We do not have any facilities to support institution or department wide
OpenURL settings. We suggest that any institution wishing to encourage
its members to use local OpenURL-based services do so by providing links
to our [OpenURL cookie](/openurl-cookie) page within their own menus
(see [click-through](#click-through) notes below) and perhaps by direct
communication with appropriate departments/groups (Physics, Mathematics,
Computer Science).

<span id="click-through"></span>

Setting cookies by click-through
--------------------------------

Our OpenURL cookie setting facility allows an automatic redirect after
setting the cookie. This may be used to provide a facility to allow
users to make appropriate resolver settings by simply clicking on a link
on a local web page. For example, the following link will set your arXiv
OpenURL cookie to use the resolver `http://arXiv.org/openurl-resolver`
and then send you to the arXiv homepage, `http://arXiv.org/`:

    http://arXiv.org/openurl-cookie
      ?baseURL=http://arXiv.org/openurl-resolver
      &icon=http://arXiv.org/icons/hand.gif
      &newWindow=yes
      &Redirect=http://arXiv.org/

The URL has been split over multiple lines to make it more readable. The
parameters are:

-   `baseURL` - the base URL of the resolver or service that OpenURL
    links will point to;
-   `icon` - { URL, not set } the URL that should be used for the link
    icon. If not set this will default to baseURL/sfx.gif in accord with
    the v0.1 specification;
-   `newWindow` - {'yes', 'no', not set} will open OpenURL link in new
    window (called 'SFXmenu') if 'yes';
-   `version` - {'0.1', '1.0', not set} add both v0.1 and v1.0
    parameters unless the version is explicitly set;
-   `Redirect` - { URL, not set } redirect to the specified URL after
    setting the cookie, display settings if not set.

<span id="resolver"></span>

OpenURL resolver
----------------

A trial resolver is available at `http://arXiv.org/openurl-resolver`.
This is somewhat trivial at present as it will resolve only arXiv
identifiers, it may later be extended. Example URLs for the resolver
are:

-   OpenURL v0.1:
    `http://arXiv.org/openurl-resolver?id=oai%3AarXiv.org%3Acs.DL%2F0106057`
    (uses `id` parameter)
-   OpenURL v1.0:
    `http://arXiv.org/openurl-resolver?rft_id=ori%3Aoai%3AarXiv.org%3Acs.DL%2F01060577&url_ver=Z39.88-2004`
    (uses `rft_id` parameter)

The resolver will simply redirect requests to the appropriate abstract
page on arXiv or print a failure message otherwise.
