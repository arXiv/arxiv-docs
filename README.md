# info.arxiv.org pages

Help, about, policy and other pages for arXiv.

## Overview

This is where to make edits to the about, help, labs, new and other pages at
info.arxiv.org. These are written in
[markdown](https://daringfireball.net/projects/markdown/) and turned into HTML
pages with [mkdocs-material](https://squidfunk.github.io/mkdocs-material/).

## How to do a Quick Edit on github

To make a quick edit, use this is a 3 step process:

1. Make your edit and commit to a new branch.

2. Make a PR from your branch to develop, get that reviewed.

3. Merge the PR to develop.

### 1. Make your edit on github
- To edit a page first go to the info.arxiv.org page you want to edit. Ex https://info.arxiv.org/help/gzip.html

- Click on the pencil icon to edit the page. That will take you to the corresponding page in github.

<kbd>![Screenshot of a page on info.arxiv.org and the location of the edit icon](/non-info/02-help-info-page.png)</kbd>

- On the page you want to edit in github, click the pencil to edit the page contents right in github.

<kbd>![Screenshot of a page in Github and the location of the edit icon](/non-info/01-help-github1a.png)</kbd>

- After you have made changes, click preview to see how it will look when completed. 
**Please note:** Github uses "Github flavored markdown" which is different from the markdown we use to create our documentation. There may be small variations in how the markdown appears due to these differences.

<kbd>![Screenshot of the location of the preview button on the edited page in Github](/non-info/03-help-preview-github.png)</kbd>

- Review your work in preview mode. To return to editing, click on "edit" in the header.

<kbd>![Screenshot displaying the preview of your edits in Github](/non-info/12-help-preview-page.png)</kbd>

- Once you are happy with your changes you can save by clicking on the blue "Commit changes" button in the upper right hand corner.
Commit is the term github and git use for saving.

<kbd>![Screenshot of the location of the commit button on the edited page in Github](/non-info/04-help-commit-github.png)</kbd>

- Add a brief note in the "Commit message" area summarizing your edit. You may add longer
note in the `Extended description` area if you have more to say about your changes.

- Make sure you have your email associated with your commits.

- Note that a "new branch for this request and start a pull request" will be selected.
- Name your branch after your JIRA ticket (if applicable) to link it. Ex `arxivce-1503-update-arxiv-docs-readme`.

<kbd>![Screenshot of how to create a new branch for the edits made in Github](/non-info/05-help-newBranch.png)</kbd>

If you have more changes to make at this time you may make and commit them all to the branch you created. The additional changes you commit will be grouped together when you make your pull request in the next step.

### 2. Make a Pull Request from your branch to `develop`
Once you have completed all of your changes, you need to have your changes reviewed. This is done by "creating a PR." PR stands for pull request.

- To make a PR click the "Pull Requests" link in the header of the github page.

- On the right hand side, click the blue button that says "New pull request"

<kbd>![Screenshot how to compare changes in the pull request in github](/non-info/11-help-newPR-compare.png)</kbd>

- Compare your changes by clicking on the "compare:develop" dropdown and type in your branch name and then select your branch.
- This will compare your branch to the develop branch.
- Click "Create pull request"

<kbd>![Screenshot how to compare changes in the pull request in github](/non-info/12-help-newPR-compare.png)</kbd>

- To the right, click on the gear icon to the right of "Reviewers".
- A dropdown will appear and request people to review your PR.
- If you are unsure who to ask to review your changes, check with your manager.

<kbd>![Screenshot of how to select reviewers of your PR and create the PR in Github](/non-info/07-help-openPR.png)</kbd>

- After selecting reviewers, click the blue "Create pull request" button.

<kbd>![Screenshot of the location of the create pull request button in Github](/non-info/08-help-createPR.png)</kbd>

- Reviewers will receive an email from Github prompting them to review your PR.
  

### 3. Merge the PR to `develop`
- Once your PR has been reviewed and approved you can merge your PR to 'develop'.
- Open your PR and scroll down and click on "Merge pull request".

<kbd>![Screenshot of how to merge your pull request in Github](/non-info/09-help-mergePR.png)</kbd>

- You will be prompted to confirm you decision, click "Confirm merge".

  <kbd>![Screenshot of how to confirm merging your PR in Github](/non-info/10-help-confirmMerge.png)</kbd>

- **Please note:** The above step will only put your changes on `develop` and they will not be viewable on the live site: info.arxiv.org. At this point you have only saved the edit(s) in github.
- You can review your changes on the develop site at [info.dev.arxiv.org](info.dev.arxiv.org).

### 4. Make a Pull Request from `develop` to `master`
- Now that your PR has been merged to develop, you need to deploy these changes to 'master'. 
- To make a new PR click the "Pull Requests" link in the header of the github page.



- Add a title for your pull request and a description if the title is not self explanatory.
- To the right, click on the gear icon to the right of "Reviewers"
- A dropdown will appear and you can request people to review your PR.



- After selecting reviewers, click the blue "Create pull request" button.
- Reviewers will receive an email from Github prompting them to review your PR.

## Authoring Markdown
See [AUTHORING.md](AUTHORING.MD)

## Building on your local machine

Instead of using github to edit you can check all the files for arxiv-docs to
your laptop to edit and preview.

```bash
git clone git@github.com:arXiv/arxiv-docs.git
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

Commits or merges to `arxiv-docs` `master` branch will deploy the site.

The cloud build YAML files combined with CloudBuild triggers in
`arxiv-production` comprise the deployment pipeline for `arxiv-docs`.

# Previews of PRs

PRs that will merge to the branch `develop` on the github repo
`arxiv-docs` will deploy previews at
https://storage.googleapis.com/arxiv-docs-prs/YOUR_BRANCH_NAME/about/index.html

Note that the home page specifically does not exist, but any other page can be accessed with its URL path.
This preview can been seen by the public, everything in the github
arxiv-docs repo can also be seen by the public.

Direct commits to the `develop` branch will not generate a preview.

## Historical site content
See https://github.com/arXiv/arxiv-docs/releases for branches prior to 2023 when content was shifted to the source/ directory.
