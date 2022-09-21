# SWORD/APP Deposit API User's Manual

<span id="preface"></span>
## 1. Preface 
----------

The arXiv **SWORD Deposit API** allows programmatic submission of
material for ingestion into the arXiv database hosted at
[arXiv.org](http://arxiv.org/).

[SWORD](http://www.swordapp.org/) defines a web service for repository
deposit based on the Atom Publishing Protocol (**APP**),
[RFC5023](http://tools.ietf.org/html/rfc5023).

The implementation of SWORD/APP at arXiv closely follows the [**SWORD
APP Profile version
1.3**](http://www.swordapp.org/docs/sword-profile-1.3.html) (SWORD/APP)
and is intended to be interoperable with all SWORD client
implementations to the extent possible.

This manual provides detailed documentation of SWORD transactions with
arXiv, mandatory extension elements, error conditions, and usage
examples.

Please review the [Terms of Use for arXiv APIs](./api/tou.md) before using the
SWORD Deposit API.

Sample code in Perl is presented to demonstrate individual steps.

<span id="overview"></span>
## 2. Overview and Control Flow 
----------------------------

The SWORD/APP deposit operation and subsequent ingestion into the arXiv
system are separate processes, with the latter being initiated and
proceeding asynchronously after the SWORD/APP communication is
completed.

In order to keep client side implementation simple, arXiv does not
require or support complex packaging formats.

A SWORD/APP deposit to arXiv consists of two steps.

-   one or more media deposits, containing the main body of the material
    along with any accompanying ancillary material, are made. Deposit of
    a zip file, which conveniently bundles all components, is also
    possible. All accepted deposits are assigned unique identifiers and
    are held in the user’s workspace. The atom entry response to a
    deposit contains a reference link to the corresponding media entry.

-   upon successful deposit of all components of a contribution, an atom
    entry containing the required arXiv metadata and references to the
    previously made media entries is deposited. This entry triggers
    assembly of the referenced media entries and hands off the entire
    package to the arXiv ingest system. The atom entry response from
    arXiv contains a link of “rel=alternate”, which allows to track the
    progression of the submission in the arXiv system.

At this point the SWORD/APP communication is complete.

Problems or errors with a deposit are signified by a [`HTTP
4xx`](http://www.swordapp.org/docs/sword-profile-1.3.html#b.5.5) status
code and accompanied by a
[`<sword:error>`](http://www.swordapp.org/docs/sword-profile-1.3.html#a.5)
response from arXiv providing further information on the particular
error.

Subsequent feedback and alerts from the arXiv ingest system, e.g.
processing problems, moderation issues, reclassification, assigned arXiv
identifier and paper password etc. will be send by email to the primary
contact author specified in the metadata and the registered user, whose
credentials were used for the deposit.

<span id="preconditions"></span>
## 3. Before Using SWORD at arXiv 
------------------------------

This interface is primarily intended for use by conference organizers,
proceedings and journal editors, etc. for programmatic bulk upload of
pre-vetted material to arXiv for long term archival and dissemination.
It is assumed that this is done with the (implied or explicit) approval
of the authors of individual contributions or on their behalf.

Individual authors may prefer arXiv’s interactive web upload for
personal use, because it provides better feedback mechanisms, but in
principle the deposit API can be used for one-at-a-time deposit to arXiv
by individual authors, too. We envision integration of the deposit
process into authoring tools for efficient upload from the desktop.

<span id="registration"></span>
### 3.1. Registration 

In accordance with general arXiv submission policy, SWORD/APP deposits
require a valid **author registration** with arXiv. Help on how to
obtain a registration is available at
[registerhelp](/help/registerhelp).

In addition, prospective users of the deposit API must request
authorization to do so via email to arXiv administrators
([contact](contact)), at least during the initial
beta phase of the SWORD interface.

<span id="licensing"></span>
### 3.2. Licensing

arXiv requires assurance of [sufficient
rights](/help/license) by the author or submitter to
allow distribution of the deposited material in perpetuity. In order to
submit an article to arXiv, the submitter must

-   grant arXiv.org a non-exclusive and irrevocable license to
    distribute the article, and certify that they have the right to
    grant this license
-   certify that the work is available under either the Creative Commons
    Attribution license, or the Creative Commons
    Attribution-Noncommercial-ShareAlike license, and that they have the
    right to grant this license, or
-   certify that the work is in the public domain (we will store this
    information by associating the Create Commons Public Domain
    Declaration with the submission)

Since license negotiation is outside of the SWORD protocol, arXiv
requires that users register a default license for SWORD deposits at
<https://arxiv.org/sword-license> before using the SWORD API. If no
license for a depositor is on file with arXiv, the API responds with a
HTTP `412 Precondition Failed` status code and a `sword:error` entry
pointing to the license selection page.

<span id="meta"></span>
### 3.3. arXiv Metadata and Classification

It is essential that users are familiar with the arXiv classification
system and general metadata requirements in order to correctly and
usefully describe their submission in terms of arXiv metadata or to
determine a good mapping of their metadata format to arXiv’s metadata
format. This is best accomplished by browsing (the relevant
subcategories of) [arXiv.org](http://arxiv.org/).

<span id="authentication"></span>
### 3.4. SSL/TLS and HTTP Basic Authentication 

The entire SWORD/APP interaction is via `SSL/TLS` (i.e. `https://`),
and requires authentication via **HTTP Basic Authentication** in the
**realm** *"SWORD at arXiv"*. This provides for secure transactions and
also protects the interface from unwanted access. Note however that
authenticity does not imply integrity. To ensure the latter material
deposited via SWORD/APP should use the SWORD HTTP extension header
Content-MD5, which provides for verification of the MD5 checksum of the
payload.

The inlined examples below are presented with the SSL/TLS and
authentication layers (mostly) peeled away for brevity.

arXiv uses a certificate issued and signed by InCommon Server CA. The
fingerprint of arXiv’s server certificate is

    SHA1 Fingerprint=D4:FA:60:66:1D:17:94:B3:D2:EB:1A:A6:8A:DB:0E:34:48:EF:4B:1E

*Notes*: 

 - until 11/16/2011 arXiv used a GeoTrust certificate with `SHA1 Fingerprint=F9:91:88:20:E0:82:EC:89:3A:90:29:C6:2B:F3:76:39:81:1D:76:26`
 - until 12/15/2010 arXiv used its own private certificate authority (CA) which was used to sign the server certificate. The fingerprint of arXiv’s server certificate was `SHA1 Fingerprint=7F:3B:78:D1:5C:CD:4F:C0:35:AC:FB:D9:F7:02:3B:C0:B5:B0:95:C5`

A copy of the CA certificate and fingerprint can be provided on request
to [contact](/help/contact).

<span id="process"></span>
## 4. The SWORD/APP Deposit Process 
--------------------------------

The `BaseURL` for all SWORD/APP interaction with arXiv is

    https://arxiv.org/sword-app/

Typically the first step in a SWORD/APP interaction is service
exploration via retrieval of the servicedocument describing the
workspaces, collections, and capabilities of the SWORD/APP endpoint.

<span id="servicedoc"></span>
### 4.1. The Servicedocument 

arXiv’s servicedocument is specific to the user initiating a
deposit — or via the `X-On-Behalf-Of HTTP header` — the author in whose
name a deposit is being made.

The main reason for customization is that the enumeration of available
collections and primary categories depends on the author’s or
submitter’s privileges.

The servicedocument can be retrieved via a regular GET request:

    GET https://arxiv.org/sword-app/servicedocument HTTP/1.1
    Host: arxiv.org

or with *mediated* user

    GET https://arxiv.org/sword-app/servicedocument HTTP/1.1
    Host: arxiv.org
    X-On-Behalf-Of: <some-registered-user>

Although it is intended for purely programmatic access, the
servicedocument can be retrieved with a regular web browser. With proper
customization of helper rules for mime type `"application/atomsvc+xml"`,
the servicedocument can be displayed inline in a web browser as regular
XML.

The response to a successful request for the servicedocument is similar
to

    HTTP/1.1 200 OK
    Date: Fri, 25 Apr 2008 22:15:08 GMT
    Content-Type: application/atomsvc+xml
    Expires: Sat, 26 Apr 2008 22:15:08 GMT

and the general structure of the returned servicedocument is

    <?xml version="1.0" encoding="utf-8"?>
    <service xmlns="http://www.w3.org/2007/app"
             xmlns:atom="http://www.w3.org/2005/Atom"
             xmlns:sword="http://purl.org/net/sword/"
             xmlns:dcterms="http://purl.org/dc/terms/"
             xmlns:arxiv="http://arxiv.org/schemas/atom/">
      <sword:version>1.3</sword:version>
      <sword:maxUploadSize>10000</sword:maxUploadSize>
      <sword:verbose>true</sword:verbose>
      <sword:noOp>true</sword:noOp>
      <workspace>
        <atom:title>arXiv</atom:title>
        <collection href="https://arxiv.org/sword-app/...-collection">
        ...
        </collection>
        ...
      </workspace>
    </service>

The servicedocument specifies the capabilities of arXiv’s SWORD
implementation, e.g. the maximal allowed size of uploads in kB
(`<sword:maxUploadSize>`), and enumerates the collections for which
the (mediated) user has submission privileges along with collection
specific information, like accepted media-types (`<accept>`), accepted
packaging format (`<acceptPackaging>`), collection policy
(`<collectionPolicy>`), etc. declarations. See
[RFC5023](http://tools.ietf.org/html/rfc5023) for specification and the
SWORD specific extensions described in [SWORD APP Profile version
1.3](http://www.swordapp.org/docs/sword-profile-1.3.html).

<span id="collections"></span>
#### 4.1.1. Collections and arXiv Classification

Each collection comes with its own arXiv specific list of “*primary
categories*”. These are regular atom **category** elements. However to
distinguish them from categories denoting secondary classification, they
are specified via the arXiv extension element `<primary_category xmlns="http://arxiv.org/schemas/atom/">`.

There is also a long list of (optional) secondary categories, which are
regular atom category elements. Specifying appropriate secondary
classification gives submissions visibility in the relevant
sub-communities of arXiv. A special feature of secondary categories for
the Computer Science and Mathematics collections is that they include
the ACM and MSC subject classifications respectively.

*Note:* The available terms for ACM (D.2, F.1.1, etc.) and MSC (43A15, 62M10, etc.) classifications are not spelled out in the servicedocument. Authors have to determine the appropriate classification from publicly available listings and complete the term attribute accordingly.

The servicedocument enumerates the available choices for each
collection.

As described below (see [Initiate Ingestion](#Ingestion)), the atom
entry containing the metadata describing and completing a deposit to
arXiv must have exactly one valid primary\_category and can have zero or
more secondary categories selected from those listed in the
servicedocument.

For example, the servicedocument lists the following choice of
primary\_categories for the *Statistics collection*:

        <collection href="https://arxiv.org/sword-app/stat-collection">
          <atom:title>The Statistics archive</atom:title>
          ....
          <arxiv:primary_categories fixed="yes">
            <arxiv:primary_category term="http://arxiv.org/terms/arXiv/stat.AP"
             scheme="http://arxiv.org/terms/arXiv/" label="Statistics - Applications"/>
            <arxiv:primary_category term="http://arxiv.org/terms/arXiv/stat.CO"
             scheme="http://arxiv.org/terms/arXiv/" label="Statistics - Computation"/>
            <arxiv:primary_category term="http://arxiv.org/terms/arXiv/stat.ML"
             scheme="http://arxiv.org/terms/arXiv/" label="Statistics - Machine Learning"/>
            <arxiv:primary_category term="http://arxiv.org/terms/arXiv/stat.ME"
             scheme="http://arxiv.org/terms/arXiv/" label="Statistics - Methodology"/>
            <arxiv:primary_category term="http://arxiv.org/terms/arXiv/stat.TH"
             scheme="http://arxiv.org/terms/arXiv/" label="Statistics - Theory"/>
          </arxiv:primary_categories>
          ...
        </collection>

and a deposit to */sword-app/stat-collection* must contain **exactly
one** of these.

While arXiv categories are typically stable for months or years,
sometimes existing categories are modified or re-assigned, and new
categories are added. It is therefore recommended to periodically
re-check the servicedocument for additions or modifications (note that
arXiv returns a HTTP Expires header of 1 day).

The Perl script [servicedoc.pl](http://arxiv.org/sword/servicedoc.pl)
provides a sample implementation of arXiv servicedocument retrieval.
With option “*--verbose*” it uses the
[XML::Atom::Service](http://search.cpan.org/perldoc?XML::Atom::Service)
module from [CPAN](http://search.cpan.org/) to demonstrate parsing of
the returned XML. Unless provided on the command-line, user-name and
password will be prompted for.

<span id="media"></span>
### 4.2. Media Deposit

A media deposit (in the parlance of APP) is any deposit of material of
one of the accepted media types to an arXiv collection via SWORD/APP.
The submission privileges of the (mediated) user determine what
collection(s) are permissible for a deposit.

*Note*: In particular for typical TeX submissions it is recommended to create a zip file of the TeX source files, macros, figures, etc and to deposit that as a single package. Other media deposits can be `docx`, `pdf`,`(e)ps`, `jpg`, `png`, etc., and it may be useful to individually deposit large figures or other material of substantial file size, instead of attempting to upload everything at once.

A deposit is performed via *POST* to the appropriate collection URL
selected from the servicedocument, e.g. a deposit of a jpg image to the
Computer Science collection looks like

    POST https://arxiv.org/sword-app/cs-collection
    Host: arxiv.org
    User-Agent: arXiv SWORD demo 1.1
    Content-Type: image/jpeg
    Authorization: Basic .......................=

    data stream
    ....

The payload is the material to be deposited.

Optionally there can be a `X-On-Behalf-Of:` HTTP header to specify the
author of the material as opposed to the user making the deposit, along
with other optional SWORD extensions headers, and in particular a md5
checksum in the `Content-MD5:` header to ensure integrity of the
transferred data:

    POST https://arxiv.org/sword-app/cs-collection
    Host: arxiv.org
    User-Agent: arXiv SWORD demo 1.1
    Content-Type: image/jpeg
    Content-MD5: p1T0tIZT/JyAgwevT+zHKw==
    Authorization: Basic .......................=

    data stream
    ...

The response to a successful deposit is status `201 Created` along
with a Location header, which contains a URL pointing to the created
media link entry (identifier replaced with ellipsis)

    HTTP/1.1 201 Created
    Date: Tue, 29 Apr 2008 18:35:46 GMT
    Location: https://arxiv.org/sword-app/getid/app/........
    Content-Type: application/atom+xml;type=entry

The response content is the associated media link entry created in the
author’s workspace at arXiv.

    <?xml version="1.0" encoding="utf-8"?>
    <entry xmlns="http://www.w3.org/2005/Atom" xmlns:sword="http://purl.org/net/sword/">
      <author>
        <name>A. Editor</name>
      </author>
      <title>Accepted media deposit to arXiv</title>
      <id>info:arxiv/app/........</id>
      <updated>2008-04-29T18:35:46Z</updated>
      <content type="image/jpeg" src="https://arxiv.org/sword-app/edit/........"/>
      <source>
        <generator uri="https://arxiv.org/sword-app/" version="0.9">SWORD@arXiv.org</generator>
      </source>
      <summary>A media deposit of type "image/jpeg" was stored in the author's workspace</summary>
      <sword:treatment>stored in author's workspace</sword:treatment>
      <sword:noOp>false</sword:noOp>
      <sword:userAgent>arXiv SWORD demo 1.1</sword:userAgent>
      <arxiv:primary_category xmlns:arxiv="http://arxiv.org/schemas/atom/"
       scheme="http://arxiv.org/terms/arXiv/"
       term="http://arxiv.org/terms/arXiv/cs">Computer Science</arxiv:primary_category>
      <link rel="edit-media" href="https://arxiv.org/sword-app/edit/........"/>
      <link rel="edit" href="https://arxiv.org/sword-app/edit/.........atom"/>
    </entry>


*Note:* The `term` attribute of the primary_category in the response reflects the collection to which the media was posted. It doesn’t have the full classification, because it is not yet known which subject category of the Computer Science collection the submission will go to.

Failure to verify the MD5 checksum will result in status `412 Precondition Failed` and a SWORD `<sword:error>` entry with attribute
`href="http://purl.org/net/sword/error/ErrorChecksumMismatch"`:

    HTTP/1.1 412 Precondition Failed
    Date: Tue, 29 Apr 2008 19:38:05 GMT
    Content-Type: application/xml

and a corresponding atom entry with human readable [error
message](#errors)

    ?xml version="1.0" encoding="utf-8"?>
    <sword:error xmlns="http://www.w3.org/2005/Atom"
           xmlns:sword="http://purl.org/net/sword/"
           xmlns:arxiv="http://arxiv.org/schemas/atom/"
           href="http://purl.org/net/sword/error/ErrorChecksumMismatch">
      <author>
        <name>SWORD@arXiv</name>
      </author>
      <title>ERROR</title>
      <id>info:arxiv/79652319-FB86-3C12-AC51-46D44EF5A410</id>
      <updated>2008-04-29T19:38:05Z</updated>
      <source>
        <generator uri="http://arxiv.org/sword-app/" version="0.9">SWORD@arXiv.org</generator>
      </source>
      <sword:treatment>processing failed</sword:treatment>
      <sword:userAgent>arXiv SWORD demo 1.1</sword:userAgent>
      <link rel="alternate" href="http://arxiv.org/help" type="text/html"/>
      <arxiv:errorcode>1048576</arxiv:errorcode>
      <summary>MD5 sum did not match</summary>
    </sword:error>

An accepted media deposit is held in the user’s workspace until further
processing. arXiv returns the media link entry created for the deposited
media. The entry has a link of `rel=“edit-media`, which will be used to
reference the deposited material.

The Perl script
[media-deposit.pl](http://arxiv.org/sword/media-deposit.pl) demonstrates
how individual files can be deposited in the user’s SWORD/APP workspace
at arXiv. The simplest invocation is

    $ ./media-deposit.pl --filename=<...> --collection=<...>

The response is parsed and presented like this (filename and identifiers
replaced with ellipsis)

     Deposit of '..........' to arXiv was successful.
     The returned HTTP status and Location:

     Status:         201 Created
     Location:       https://arxiv.org/sword-app/getid/app/........
     --------------------------------------------------------------
     The deposited media resource should be referenced as:
             https://arxiv.org/sword-app/edit/........

See

    $ perldoc media-deposit.pl

for more options.

It is important to take note of the `edit-media` link or the
`identifier` assigned to the media deposit, in order to reference the
deposited material in the next step.

<span id="ingestion"></span>
### 4.3. Metadata and Ingestion Initiation

Once all components of a submission are deposited, the final step is to
provide the metadata describing the content of the submission and
referencing the previously deposited media entries. This is done by
POST-ing a specially crafted **atom entry** with mime-type
`application/atom+xml;type=entry` to the same collection URI as the
previously posted media entries.

The “wrapper” entry is an *atom entry*, as defined by the Atom
Syndication Format ([RFC
4287](http://tools.ietf.org/html/rfc4287#section-4.1.2)), with certain
mandatory and some optional extension elements.

Most arXiv [metadata elements](http://arxiv.org/help/prep) have a direct
mapping to standard atom entry elements, and these are used where
possible. However arXiv metadata is richer than what the standard atom
entry provides for. A detailed description of all arXiv entry elements
can be found in the [arXiv Atom
API](http://export.arxiv.org/api_help/docs/user-manual.html#_entry_metadata)
documentation.

*Note*: A good way to understand the mapping of metadata between arXiv and atom is to look at examples. Compare the rendering of metadata for an arXiv paper as [atom feed (XML)](http://export.arxiv.org/api/query?id_list=0803.2365) with the rendering as [web page (XHTML)](https://arxiv.org/abs/0803.2365)

Apart from other requirements for an atom entry (id, updated, etc), the
wrapper for a arXiv submission must contain

Mandatory Elements

-   `<title>`

-   `<author>`

-   `<contributor>`*

-   `<summary>`

-   `<arxiv:primary_category …>`

-   `<link rel=related …>`*

and may contain additional metadata, where available

Optional Elements

-   `<category>`*

-   `<arxiv:comment>`

-   `<arxiv:journal_ref>`*

-   `<arxiv:doi>`

-   `<arxiv:report_no>`*

-   `<arxiv:affiliation>`*

(* indicates repeatable elements)

The `<author>` element is used for the authenticated user, i.e. the
person who initiates the submission. The repeatable `<contributor>`
element is used to specify the individual authors of the material being
deposited to arXiv.

At least one **/contributor/email** node must be present in order to
inform arXiv of the email address of the primary contact author. If
multiple /contributor/email nodes are found, the first will be used.
Optionally the primary contact author’s (name and) email address can
also be specified in the `X-On-Behalf-Of` HTTP header extension, e.g.:

    X-On-Behalf-Of: "A. Scientist" <ascientist@institution.edu>

This is useful to disambiguate when multiple /contributor/email nodes
are present.

The `<arxiv:primary_category>` must be selected from the list of
available choices for the collection, as given in the servicedocument.

The **link(s)** of relation “*related*” must refer to the previously
deposited material.

**Title** and **summary** have their obvious meaning. The summary must
be at least 20 characters long. The title will be checked against other
recently arXiv-ed papers to avoid inadvertent double submissions.

**Category** element(s) can be used to provide secondary
classification(s), selected from those listed in the servicedocument.

Please refer to the arXiv [submission help](/help/prep)
for explanation of the other optional fields.

The “wrapper” is POST-ed to the same collection URI as the previously
deposited media. For example, a submission of a single PDF file to the
physics collection

    POST https://arxiv.org/sword-app/physics-collection HTTP/1.1
    Host: arxiv.org
    User-Agent: arXiv SWORD demo 1.1
    Content-Type: application/atom+xml;type=entry
    Authorization: Basic .......................=

    <?xml version="1.0" encoding="utf-8"?>
    <entry xmlns="http://www.w3.org/2005/Atom">
      <title>A strangely unique title</title>
      <id>A8A725C2-10E7-11DD-A667-67C33A33DA4A</id>
      <updated>2008-04-23T03:45:04Z</updated>
      <author>
        <name>B. Editor</name>
        <email>conference@example.com</email>
      </author>
      <contributor>
        <name>A. Genius</name>
        <arxiv:affiliation>Institute of Irreproducible Results</arxiv:affiliation>
      </contributor>
      <contributor>
        <name>S. Clown</name>
        <email>clown@example.com</email>
        <uri>http://example.com/~clown</uri>
      </contributor>
      <content type="xhtml">
        <div xmlns="http://www.w3.org/1999/xhtml">SWORD/APP arXiv submission wrapper</div>
      </content>
      <summary>A concise abstract of the important findings herein</summary>
      <category term="http://arxiv.org/terms/arXiv/physics.class-ph"
                scheme="http://arxiv.org/terms/arXiv/"
                label="Physics - Classical Physics"/>
      <category term="http://arxiv.org/terms/arXiv/physics.hist-ph"
                scheme="http://arxiv.org/terms/arXiv/"
                label="Physics - History of Physics"/>
      <arxiv:primary_category xmlns:arxiv="http://arxiv.org/schemas/atom/"
                scheme="http://arxiv.org/terms/arXiv/" label="Physics - Classical Physics"
                term="http://arxiv.org/terms/arXiv/physics.class-ph"/>
      <link href="https://arxiv.org/sword-app/edit/........" type="application/pdf" rel="related"/>
    </entry>

If this is successful the server response is `202 Accepted`

    HTTP/1.1 202 Accepted
    Date: Tue, 29 Apr 2008 18:45:26 GMT
    Location: https://arxiv.org/sword-app/getid/app/........
    Content-Type: application/atom+xml;type=entry

This means that the wrapper passed checks for presence of all mandatory
elements, proper classification, ownership of the referenced media
entries, authorization to post to the specified collection, presence of
a contact email for at least one of the authors of the contribution,
etc..

The returned atom entry confirms the acceptance

    <?xml version="1.0" encoding="utf-8"?>
    <entry xmlns="http://www.w3.org/2005/Atom" xmlns:sword="http://purl.org/net/sword/">
      <author>
        <name>B. Editor</name>
      </author>
      <title>Accepted deposit wrapper to arXiv</title>
      <id>info:arxiv/app/........</id>
      <updated>2008-04-23T04:16:30Z</updated>
      <content type="application/atom+xml;type=entry" src="https://arxiv.org/sword-app/edit/........"/>
      <source>
        <generator uri="https://arxiv.org/sword-app/" version="0.9">SWORD@arXiv.org</generator>
      </source>
      <summary>A concise abstract of the important findings herein</summary>
      <sword:treatment>atom wrapper used to initiate ingestion into arXiv</sword:treatment>
      <sword:noOp>false</sword:noOp>
      <sword:userAgent>arXiv SWORD demo 1.1</sword:userAgent>
      <arxiv:primary_category xmlns:arxiv="http://arxiv.org/schemas/atom/"
         scheme="http://arxiv.org/terms/arXiv/"
         term="http://arxiv.org/terms/arXiv/physics.class-ph"/>
      <category scheme="http://arxiv.org/terms/arXiv/" term="http://arxiv.org/terms/arXiv/physics.class-ph"/>
      <category scheme="http://arxiv.org/terms/arXiv/" term="http://arxiv.org/terms/arXiv/physics.hist-ph"/>
      <link rel="edit-media" href="https://arxiv.org/sword-app/edit/........"/>
      <link rel="edit" href="https://arxiv.org/sword-app/edit/.........atom"/>
      <link rel="alternate" href="http://arxiv.org/resolve/app/........"/>
    </entry>

and contains an “alternate” link, which can be used to look up the
permanent arXiv identifier which will be assigned to this submission
upon release.

*Note*: The arXiv identifier and paper password will also be send by email to the primary contact author.

<span id="verification"></span>
## 5. Verification and Tracking
----------------------------

Once the SWORD/APP transaction is completed, the submission is
automatically queued for ingestion into the arXiv system.

Acceptance of the wrapper does not imply that ingestion will be
successful. Among other things there could be problems with moderator
approval, classification, format conversion (e.g. TeX → PS, .docx → PDF,
etc.), duplication detection, etc..

The eventual success or failure of ingestion will be communicated by
email to the primary contact author (and optionally to the
submitter/authenticated user).

When applicable the email contains the permanent arXiv identifier and
paper password. It is important that the author/submitter closely
inspect the representation of the submission at arXiv and take
corrective action where necessary, see
[checking](/help/submit#correct).

The status of a SWORD deposit may be tracked using the tracking URI
returned in the Atom `<link>` element with `rel="alternate"`, for
example:

    <link rel="alternate" href="http://arxiv.org/resolve/app/10030146"/>

The response to `GET <http://arxiv.org/resolve/app/10030146>` will be a
short XML report on the status of this SWORD submission in the arXiv
workflow. An example initial response is:

    <?xml version="1.0" encoding="UTF-8"?>
    <deposit>
     <tracking_id>http://arxiv.org/resolve/app/10030146</tracking_id>
     <status>submitted</status>
    </deposit>

An example after publication is:

    <?xml version="1.0" encoding="UTF-8"?>
    <deposit>
     <tracking_id>http://arxiv.org/resolve/app/10030146</tracking_id>
     <status>published</status>
     <arxiv_id>1003.9876</arxiv_id>
    </deposit>

The root element will always be `<deposit>` and will always
contain a `<status>` element which contains one of the following:

Status Values

-   `submitted` - The SWORD submission is in the normal arXiv workflow
    and is queued to be announced according to the usual arXiv
    announcement schedule.

-   `published` - The SWORD submission has been accepted and published
    by arXiv. The response will also include the final arXiv identifier
    in the `<arxiv_id>` element.

-   `on hold` - The SWORD submission is in arXiv’s workflow but was
    identified by arXiv administrators or moderators as needing further
    attention.

-   `incomplete` - This status is not expected to be used for SWORD
    submissions. The submission is in process but not yet submitted and
    queued.

-   `unknown` - The tracking URI is not know. More information may be
    given in an `<error>` element.

<span id="replacement"></span>
## 6. Replacement
--------------

arXiv’ed papers can be updated or replaced. The rules for a
[replacement](/help/replace) via the web interface also
apply to a replacement using SWORD. In particular a new version number
will be assigned unless it is a [same day
replacement](/help/replace#sameday), and all [previously
published versions](/help/replace#versions) remain
accessible.

For a replacement of a previously created resource via SWORD/APP arXiv
uses the “Editing Resources with *PUT*” functionality as outlined in the
[SWORD
specification](http://www.swordapp.org/docs/sword-profile-1.3.html#b.9.3)
and specifically [RFC5023 section
9.3](http://tools.ietf.org/html/rfc5023#section-9.3) applied to the
metadata wrapper of the original deposit.

A replacement via SWORD can only be made by a registered [paper
owner](/help/authority) or the author of the original
SWORD deposit when authenticated with the same credentials. There are no
per paper passwords for replacements via SWORD.

Most of the mechanics of the replacement are the same as those of a new
SWORD deposit.

Steps for a replacement

-   First all the **media resources** should be individually
    [posted](#Deposit) or deposited packed together into a zip file.

-   Previously deposited media resources in the workspace of the
    authenticated user can be referenced via their `edit-media` links,
    e.g.

          <link rel="edit-media" href="https://arxiv.org/sword-app/edit/........"/>

    if they have not expired yet. arXiv retains individual media
    deposits via SWORD for at least 30 days.

-   Then a [metadata wrapper](#Ingestion) is *PUT* to the link with
    `rel="edit”` which was part of the atom entry response to the
    original wrapper deposit, e.g.

          <link rel="edit" href="https://arxiv.org/sword-app/edit/09011841.atom"/>

    The metadata wrapper is constructed in similar fashion as for a new
    submission, however it must be deposited using *PUT* to the **link**
    with `rel=“edit”` that was returned upon original submission.

        PUT https://arxiv.org/sword-app/edit/09031234.atom HTTP/1.1
        Host: arxiv.org
        User-Agent: arXiv SWORD demo 1.1
        Content-Type: application/atom+xml;type=entry
        Authorization: Basic .......................=

-   To modify an existing wrapper, authors can first issue a *GET*
    request to the **edit** link of that wrapper, modify the returned
    atom entry and then deposit it via a *PUT* request to the same
    **edit** link.

-   The response to a successful PUT is status `202 Accepted`

        HTTP/1.1 202 Accepted
        Date: Sat, 21 Mar 2009 00:06:27 GMT
        Location: https://arxiv.org/sword-app/getid/app/........
        Content-Type: application/atom+xml;type=entry

    along with an atom entry in the response content confirming
    acceptance.

*Notes*: 

 - To replace a paper using the permanent arXiv identifier (`<id>`), submit the metadata wrapper via **PUT** to `https://arxiv.org/sword-app/edit/<id>` e.g. for `arXiv:0708.0123` use **PUT** to `https://arxiv.org/sword-app/edit/0708.0123` and for `arXiv:cond-mat/9904123` use **PUT** to `https://arxiv.org/sword-app/edit/cond-mat/9904123`
 - arXiv does not permit the classification of an article to be changed during a replacement operation. The `arxiv:primary_category` element must match the existing primary category. The replacment metadata may contain either no `category` elements, or a set of `category` elements that matches the existing categories.
 - The authenticated user **must**> be the paper owner. Ownership can be [claimed with the paper password](https://arxiv.org/auth/need-paper-password.php).

<span id="errors"></span>
## 7. Error Conditions and Error Codes
-----------------------------------

Error handling is outlined in Part A.5 of the [SWORD
specification](http://www.swordapp.org/docs/sword-profile-1.3.html#a.5),
where a SWORD extension element to AtomPub called `sword:error` is
introduced.

This allows for a much more informative error message in addition to the
regular HTTP 4xx and 5xx [status
codes](http://www.swordapp.org/docs/sword-profile-1.3.html#b.5.5) which
are part of the base protocol.

arXiv uses this mechanism to provide informative error messages in the
body of the error response along with a corresponding numeric error code
and a href attribute.

The error response content is a regular atom entry with a root element
of `sword:error`, a `href attribute` containing a URI which identifies
the error, a human readable error presented in the `summary` element
and the numeric error code in the `arxiv:errorcode` extension element.

The HTTP status for all errors not otherwise defined in the [SWORD
spec](http://www.swordapp.org/docs/sword-profile-1.3.html#b.5.5) is
`400 Bad Request`.

The numerical error codes are powers of 2 (for convenient bitmasking,
multiple error indication, etc). The list of all currently defined
`arxiv:errorcodes` is:

|  2\^n| error message                                                            |
|-----:|:-------------------------------------------------------------------------|
|     0| method not supported                                                     |
|     1| unrecognized POST request                                                |
|     2| unrecognized GET request                                                 |
|     3| GET not supported for this request. Use POST instead                     |
|     4| invalid collection                                                       |
|     5| momentary overload. Try again in a few seconds                           |
|     6| service temporarily unavailable                                          |
|     7| No author name                                                           |
|     8| No contact email                                                         |
|     9| invalid contact email                                                    |
|    10| No primary category specified                                            |
|    11| primary category invalid                                                 |
|    12| more than one primary category specified                                 |
|    13| category element(s) invalid                                              |
|    14| No summary or summary too short. A summary is required metadata by arXiv |
|    15| No title                                                                 |
|    16| title conflicting                                                        |
|    17| media type specified is not supported                                    |
|    18| No media entries found in the author’s workspace                         |
|    19| No media entry with specified id                                         |
|    20| MD5 sum did not match                                                    |
|    21| link href could not be parsed                                            |
|    22| MIME type of link could not be parsed                                    |
|    23| No media entries with link attribute rel="related"                       |
|    24| unspecified error, contact the server administrator                      |
|    25| Not Authorized                                                           |
|    26| blog function /edit is currently not supported                           |
|    27| No access, not the owner of the requested entry                          |
|    28| No valid license on file                                                 |

This list may be added to as new or unanticipated errors become
apparent.

For example an attempted deposit to the undefined collection “foobar”
will produce

    HTTP/1.1 400 Bad Request
    Date: Thu, 08 May 2008 21:51:32 GMT
    Server: Apache
    Content-Type: application/atom+xml;type=entry

and the response content is

    <?xml version="1.0" encoding="utf-8"?>
    <sword:error xmlns="http://www.w3.org/2005/Atom"
            xmlns:sword="http://purl.org/net/sword/"
            xmlns:arxiv="http://arxiv.org/schemas/atom/"
            href="http://purl.org/net/sword/error/ErrorContent">
      <author>
        <name>SWORD@arXiv</name>
      </author>
      <title>ERROR</title>
      <id>info:arxiv/B48008EB-F5BF-3827-8ABA-8AB5F04EAAAA</id>
      <updated>2008-05-08T21:45:44Z</updated>
      <source>
        <generator uri="http://arxiv.org/sword-app/" version="0.9">SWORD@arXiv.org</generator>
      </source>
      <sword:treatment>processing failed</sword:treatment>
      <sword:packaging>http://purl.org/net/sword-types/bagit</sword:packaging>
      <sword:userAgent>arXiv SWORD demo 1.1</sword:userAgent>
      <link rel="alternate" href="http://arxiv.org/help" type="text/html"/>
      <arxiv:errorcode>16</arxiv:errorcode>
      <summary>invalid collection: foobar</summary>
    </sword:error>

<span id="example"></span>
## 8. A Complete Example
---------------------

As a practical example, we demonstrate what the submission of an
existing article,
[arXiv:hep-th/0605021](http://arxiv.org/abs/hep-th/0605021) via
SWORD/APP would look like.

The article consists of 3 individual files, a TeX source file and 2
figure files. These are packaged in a zip file (submission.zip), which
is then deposited to the physics collection of the arXiv SWORD endpoint.
To ensure data integrity, the deposit is accompanied by the optional MD5
checksum of the payload

    $ ./media-deposit.pl --collection=physics --filename=submission.zip --verbose --md5
    Enter username for "SWORD@arXiv": demouser
    Password for demouser:

The response status and reference link are displayed

    Deposit of 'submission.zip' to arXiv was successful.
    The returned HTTP status and Location:

    Status:         201 Created
    Location:       https://arxiv.org/sword-app/getid/app/08050001

    The deposited media resource should be referenced as:
                    https://arxiv.org/sword-app/edit/08050001

and the full atom entry returned by the server is:

    <?xml version="1.0" encoding="utf-8"?>
    <entry xmlns="http://www.w3.org/2005/Atom" xmlns:sword="http://purl.org/net/sword/">
      <author>
        <name>schwande</name>
      </author>
      <title>Accepted media deposit to arXiv</title>
      <id>info:arxiv/app/08050001</id>
      <updated>2008-05-06T16:52:58Z</updated>
      <content type="application/zip" src="https://arxiv.org/sword-app/edit/08050001"/>
      <source>
        <generator uri="https://arxiv.org/sword-app/" version="0.9">SWORD@arXiv.org</generator>
      </source>
      <summary>A media deposit of type "application/zip" was stored in the author's workspace</summary>
      <sword:treatment>stored in author's workspace</sword:treatment>
      <sword:noOp>false</sword:noOp>
      <sword:packaging>http://purl.org/net/sword-types/bagit</sword:packaging>
      <sword:userAgent>arXiv SWORD demo 1.1</sword:userAgent>
      <arxiv:primary_category xmlns:arxiv="http://arxiv.org/schemas/atom/"
             scheme="http://arxiv.org/terms/arXiv/"
             term="http://arxiv.org/terms/arXiv/physics">Physics</arxiv:primary_category>
      <link rel="edit-media" href="https://arxiv.org/sword-app/edit/08050001"/>
      <link rel="edit" href="https://arxiv.org/sword-app/edit/08050001.atom"/>
    </entry>

Next comes preparation and POST-ing of the metadata wrapper.

To capture the rich metadata of this article to full extent, the wrapper
contains several optional arXiv extensions to the standard atom entry,
i.e. `arxiv:comment`, `arxiv:journal_ref`, `arxiv:doi`, (two)
`arxiv:report_no`, and an author child element `arxiv:affiliation`:

In this case there is only one media entry to reference via the
“related” link,

     <link href="https://arxiv.org/sword-app/edit/08050001" type="application/zip" rel="related"/>

namely the zip file previously deposited and referenced via the URI
*https://arxiv.org/sword-app/edit/08050001*

    <?xml version="1.0" encoding="utf-8"?>
    <entry xmlns="http://www.w3.org/2005/Atom">
      <title>Superconformal Symmetry in Linear Sigma Model on Supermanifolds</title>
      <id>E102241E-1BA8-11DD-81A6-69C93A33DA4A</id>
      <updated>2008-05-06T20:13:23Z</updated>
      <author>
        <name>A. Editor</name>
        <email>editor@example.com</email>
      </author>
      <contributor>
        <name>Shigenori Seki</name>
        <email>Shigenori Seki &lt;seki@.....phys.kyoto-u.ac.jp&gt;</email>
      </contributor>
      <contributor>
        <name>Katsuyuki Sugiyama</name>
      </contributor>
      <contributor>
        <name>Tatsuya Tokunaga</name>
        <arxiv:affiliation xmlns:arxiv="http://arxiv.org/schemas/atom/">Kyoto Univ.</arxiv:affiliation>
      </contributor>
      <content type="xhtml">
        <div xmlns="http://www.w3.org/1999/xhtml">SWORD/APP arXiv submission wrapper</div>
      </content>
      <summary>We consider a gauged linear sigma model in two dimensions
    with Grassmann odd chiral superfields. We investigate the Konishi anomaly of
    this model and find out the condition for realization of superconformal
    symmetry on the world-sheet. When this condition is satisfied, the theory is
    expected to flow into conformal theory in the infrared limit. We construct
    superconformal currents explicitly and study some properties of this
    world-sheet theory from the point of view of conformal field theories.</summary>
      <category term="http://arxiv.org/terms/arXiv/hep-th"
                scheme="http://arxiv.org/terms/arXiv/"
                label="High Energy Physics - Theory"/>
      <arxiv:primary_category xmlns:arXiv="http://arxiv.org/schemas/atom/"
                scheme="http://arxiv.org/terms/arXiv/"
                label="High Energy Physics - Theory"
                term="http://arxiv.org/terms/arXiv/hep-th"/>
      <arxiv:comment xmlns:arxiv="http://arxiv.org/schemas/atom/">24 pages, 2 figures</arxiv:comment>
      <arxiv:journal_ref xmlns:arxiv="http://arxiv.org/schemas/atom/">Nucl.Phys. B753 (2006) 295-312</arxiv:journal_ref>
      <arxiv:report_no xmlns:arxiv="http://arxiv.org/schemas/atom/">KUNS-2018</arxiv:report_no>
      <arxiv:report_no xmlns:arxiv="http://arxiv.org/schemas/atom/">YITP-06-19</arxiv:report_no>
      <arxiv:doi xmlns:arxiv="http://arxiv.org/schemas/atom/">10.1016/j.nuclphysb.2006.07.013</arxiv:doi>
      <link href="https://arxiv.org/sword-app/edit/08050001" type="application/zip" rel="related"/>
    </entry>

*Note*: In the absence of a `X-On-Behalf-Of` HTTP header, the primary contact author is determined by the first contributor with an email child element.

This is POST-ed to the physics-collection at arXiv’s SWORD endpoint.

The important pieces of the response are:

    Posting to arXiv was successful.
    The returned HTTP status and Location:

    Status:         202 Accepted
    Location:       https://arxiv.org/sword-app/getid/app/08050007

    The submission can be tracked via:
            http://arxiv.org/resolve/app/08050007

The full atom entry response is

    <?xml version="1.0" encoding="utf-8"?>
    <entry xmlns="http://www.w3.org/2005/Atom" xmlns:sword="http://purl.org/net/sword/">
      <author>
        <name>schwande</name>
      </author>
      <title>Accepted deposit wrapper to arXiv</title>
      <id>info:arxiv/app/08050007</id>
      <updated>2008-05-06T20:13:38Z</updated>
      <content type="application/atom+xml;type=entry" src="https://arxiv.org/sword-app/edit/08050007"/>
      <source>
        <generator uri="https://arxiv.org/sword-app/" version="0.9">SWORD@arXiv.org</generator>
      </source>
      <summary>We consider a gauged linear sigma model in two dimensions
    with Grassmann odd chiral superfields. We investigate the Konishi anomaly of
    this model and find out the condition for realization of superconformal
    symmetry on the world-sheet. When this condition is satisfied, the theory is
    expected to flow into conformal theory in the infrared limit. We construct
    superconformal currents explicitly and study some properties of this
    world-sheet theory from the point of view of conformal field theories.</summary>
      <sword:treatment>atom wrapper used to initiate ingestion into arXiv</sword:treatment>
      <sword:noOp>false</sword:noOp>
      <sword:userAgent>arXiv SWORD demo 1.1</sword:userAgent>
      <arxiv:primary_category xmlns:arxiv="http://arxiv.org/schemas/atom/"
             scheme="http://arxiv.org/terms/arXiv/" term="http://arxiv.org/terms/arXiv/hep-th"/>
      <category scheme="http://arxiv.org/terms/arXiv/" term="http://arxiv.org/terms/arXiv/hep-th"/>
      <link rel="edit-media" href="https://arxiv.org/sword-app/edit/08050007"/>
      <link rel="edit" href="https://arxiv.org/sword-app/edit/08050007.atom"/>
      <link rel="alternate" href="http://arxiv.org/resolve/app/08050007"/>
    </entry>

This completes the SWORD/APP process. The submission is now being
processed by arXiv, and assuming it passes all internal checks and is
approved by moderators, it will be entered into the arXiv database.
Notification of acceptance or failure will be send by email to the
primary contact author and the user initiating the submission. If the
submission was successful the URI from the “alternate” link from the
returned atom entry

    <link rel="alternate" href="http://arxiv.org/resolve/app/08050007"/>

can be used to find out what arXiv identifier was assigned to the
submission.

<span id="questions"></span>
## 9. Questions, Concerns, Suggestions
-----------------------------------

Please [contact](/help/contact) arXiv with any questions
or suggestions.

The SWORD interface is currently in beta and there is certainly room for
improvements.

Note that we purposely did not use a complex object format, to keep the
entry threshold low.

<span id="updates"></span>
## 10. API Updates (last update: 2013-01-11)
-----------------------------------------

2013-01-11
:   In 2012-12 the *https://arxiv.org/sword-app/nlin-collection* was
    removed and all *nlin* (Nonlinear Sciences) categories (e.g.
    *http://arxiv.org/terms/arXiv/nlin.AO*) were reorganized within the
    *https://arxiv.org/sword-app/physics-collection* collection. This
    change is reflected in the [Servicedocument](#Servicedocument). This
    corresponds with moving the nlin archive into the physics group in
    the arXiv classification scheme and user-interface.
