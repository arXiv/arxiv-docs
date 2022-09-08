To Subscribe to the E-Mail Alerting Service
===========================================

If you would like to receive regular daily listings of the abstracts of
new submissions by email, then you can subscribe to this service as
follows. Note that the email must be sent as **plain text**. Richtext format 
emails will be ignored by the system.

1.  Determine which archive is of interest to you, and obtain its e-mail
    address from the [list of available archives](/category_taxonomy).

2.  **For archives divided into subject classes:**  
    If the archive to which you are subscribing requires distinct
    subject classes (such as the `math`, `physics`, `cs`, `q-bio` and
    `q-fin` archives; but *not `astro-ph`, `cond-mat` or `nlin`*, see
    [handling subscriptions to all physics archives through
    physics](#physics) below), then you (un)subscribe to a specific
    category, indicating the categories in the body of the message. Here
    is an example
```
To: physics@arxiv.org 
Subject: subscribe John Smith 
    
add Biophysics 
del Plasma Physics
```
You may alternatively use the short subject class codes, for example
to subscribe to the Risk Management category (`q-fin.RM`) in
Quantitative Finance:
```
To: q-fin@arxiv.org 
Subject: subscribe John Smith 

add RM
```

3.  **For archives not divided into subject classes:**  
    Send an e-mail message to the archive(s) of interest, in the
    following form
```
To: arch-ive@arxiv.org 
Subject: subscribe Your Full Name
```

You should give your name as you wish it to appear on the
distribution list. Here is an example:
```
To: quant-ph@arxiv.org 
Subject: subscribe John Smith
```
(note that subscribing to subdivided archivies, such as `cond-mat`, in this way will subscribe you to all
subject classes within that archive.)

4.  **<span id="physics">Handling subscriptions to all physics archives
    through `physics`</span>**  
    The `physics` archive can be used to subscribe to any combination of
    existing physics archives, e.g. to something like \`General
    Relativity', \`Astrophysics', and \`High Energy Physics -
    Experimental'. This is also the only way to subscribe to a subset of
    the subject classes within the `astro-ph`, `cond-mat` and `nlin`
    archives. For example, to subscribe only to the `cond-mat` subject
    classes \`Soft Condensed Matter' and \`Superconductivity', the email
    would read:
```
To: physics@arxiv.org 
Subject: subscribe John Smith 

add Soft Condensed Matter 
add Superconductivity
```
If you want to change from, say, subscribing to all of `astro-ph` to
subscribing to just `astro-ph.EP` then you must first
[cancel](#cancel) the subscription to `astro-ph`, and then subscribe
to `EP` through the `physics` archive.

------------------------------------------------------------------------

<span id="cancel"></span>

To Cancel Your Subscription
===========================

If you want to cancel your receipt of the regular listings, you can do
so as follows.

1.  Find the e-mail address of the archive for which you are receiving
    the listings.
2.  Send an e-mail message to the archive, in the following form
```
To: arch-ive@arxiv.org 
Subject: cancel
```
Here is an example:
```
To: quant-ph@arxiv.org 
Subject: cancel
```
If you want to cancel your subscription to a particular subject
class in an archive that supports subject classes, then see the
example use of **`del`** in the **`subscribe`** command above.

Note that you may be subscribed through a remote listserv, or through
some local preprint distribution list at your end. You can determine the
origin of your subscription by examining the header from the daily
mailing you receive. You will have to deal with this through the
administrator of the remote distribution list.
