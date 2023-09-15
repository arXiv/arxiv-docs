# info.arxiv.org pages

Help, about, policy and other pages for arXiv.

## Overview

This is where to make edits to the about, help, labs, new and other pages at
info.arxiv.org. These are written in
[markdown](https://daringfireball.net/projects/markdown/) and turned into HTML
pages with [mkdocs-material](https://squidfunk.GitHub.io/mkdocs-material/).

## How to do a Quick Edit on GitHub

To do a quick edit, use this is a 3-step process:

1st: Make your edit and commit to the develop branch

2nd: Make a GitHub pull request from develop to master, get that reviewed

3rd: Merge your pull request to master

This commits directly to the `develop` branch. If you are doing a more involved
group of edits or changes, please use a process like git flow. If you are not
familiar with this ask a dev or an admin to help you.

### 1st: Make your edit on GitHub
To edit a page first go to the info.arxiv.org page you want to edit. Ex https://info.arxiv.org/help/gzip.html

![gzip page](non-info/help-info-page.png)

There click on the pencil icon to edit the page. That will take you to the corresponding page in GitHub.

![gzip page](non-info/help-github1.png)

There click "edit" and you can edit contents of the page in GitHub. Once you
have made changes you can click preview to see how it will look when completed
There are slight differences between the markdown we use and what
GitHub uses.

![gzip page](non-info/help-github2.png)

Once you are happy with your changes you can save the by going to the bottom of
the edit and "Commit changes". Commit is the term GitHub and git use for
saving. You should put a brief note in the first text area. You may add longer
note in the larger text area if you have more to say about your changes. Then
you can commit your changes to the branch `develop`.

The above step will not put your changes live on info.arxiv.org. At that point
you have only saved the edit in GitHub.

If you have more changes that are grouped with this change make them in GitHub
and commit them.

### 2nd: Make a Pull Request from `develop` to `master`
Once you have done all the changes you wanted you need to get your changes
reviewed. This is done by "creating a PR." PR stands for pull request.

To make a new PR click the "Pull Requests" tab on the top of a GitHub page. Then
click the green "New Pull Request." You want changes from the branch `develop` to get put
into the branch called `master`.

![gzip page](non-info/help-pr1.png)

From there you can give your PR a title and add a note about it. Also add
reviewers on the left. Then click the green "Create Pull Request"

GitHub will email all the reviewers.

### 3rd: Merge the PR to `master` to Deploy Changes

To get your changes deployed, merge it to the branch called `master`. This will
cause automated scripts to deploy the changes to info.arxiv.org.  If you are
unsure how to do this, ask a dev or admin to do it for you.

## Authoring Markdown
See [AUTHORING.md](AUTHORING.MD)

## Building on your local machine

Instead of using GitHub to edit you can check all the files for arxiv-docs to
your laptop to edit and preview.

```bash
git clone git@GitHub.com:arXiv/arxiv-docs.git
cd arxiv-docs
python --version
# 3.8.12
python -m venv docs-venv
source docs-venv/bin/activate
pip install -r requirements.txt
mkdocs serve
google-chrome https://localhost:8000/index.html
```

Then you will have the site served locally with hot reloading on edits. In your
browser, go to http://localhost:8000/index.html

# Deployment to info.arxiv.org

Commits or merges to the `arxiv-docs/master` branch will deploy the site https://info.arxiv.org .

The cloud build YAML files combined with CloudBuild triggers in `arxiv-production` comprise the deployment 
pipeline for `arxiv-docs`.

# Deploy to info.dev.arxiv.org

Similar to `arxiv-docs/master` and  https://info.arxiv.org, changes committed to or prs merged to the `arxiv-docs/develop` 
branch wil be deployed to https://info.dev.arxiv.org 

# Previews of Pull Requests

PRs that will merge to the branch `arxiv-docs/develop` will deploy previews at
https://storage.googleapis.com/arxiv-docs-prs/YOUR_PR_NAME/index.html
This preview can be seen by the public, everything in the GitHub
arxiv-docs repo can also be seen by the public.

Direct commits to the `develop` branch will not generate a preview.

## Historical site content
See https://GitHub.com/arXiv/arxiv-docs/releases for branches prior to 2023 when content was shifted to the source/ directory.
