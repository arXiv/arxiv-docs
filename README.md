# info.arxiv.org pages

Help, about, policy and other pages for arXiv.

## Overview

This is where to make edits to the about, help, labs, new and other pages at
info.arxiv.org. These are written in
[markdown](https://daringfireball.net/projects/markdown/) and turned into HTML
pages with [mkdocs-material](https://squidfunk.github.io/mkdocs-material/).

## How to do a Quick Edit on github

To do a quick edit, use this is a 4 step process:

1st: Make your edit and commit to a new branch.

2nd: Make a PR from your branch to develop, get that reviewed.

3rd: Merge the PR to develop.

4th: Create a PR to deploy your changes to master.

### 1st: Make your edit on github
- To edit a page first go to the info.arxiv.org page you want to edit. Ex https://info.arxiv.org/help/gzip.html

- Click on the pencil icon to edit the page. That will take you to the corresponding page in github.

<kbd>![Screenshot of a page on info.arxiv.org and the location of the edit icon](/non-info/02-help-info-page.png)</kbd>

- On the page you want to edit in github, click the pencil to edit the page contents right in github.

<kbd>![Screenshot of a page in Github and the location of the edit icon](/non-info/01-help-github1a.png)</kbd>

- After you have made changes, click preview to see how it will look when completed. 
**Please note:** Github uses "Github flavored markdown" which is different from the markdown we use to create our documentation. There may be small variations in how the markdown appears due to these differences.

<kbd>![Screenshot of the location of the preview button on the edited page in Github](/non-info/03-help-preview-github.png)</kbd>

- Once you are happy with your changes you can save by clicking on the blue "Commit changes" button in the upper right hand corner.
Commit is the term github and git use for saving.

<kbd>![Screenshot of the location of the commit button on the edited page in Github](/non-info/04-help-commit-github.png)</kbd>

- Add a brief note in the "Commit message" area summarizing your edit. You may add longer
note in the `Extended description` area if you have more to say about your changes.

- Make sure you have your email associated with your commits.

- Create a "new branch for this request and start a pull request" will be selected
- Name your branch after your JIRA ticket (if applicable) to link it. Ex `arxivce-1503-update-arxiv-docs-readme`.

<kbd>![Screenshot of how to create a new branch for the edits made in Github](/non-info/05-help-newBranch.png)</kbd>

If you have more changes to make at this time you may make and commit them all on the branch you created. The additional changes you commit will be grouped together when you make your pull request in the next step.

### 2nd: Make a Pull Request from your branch to `develop`
Once you have completed all of your changes, you need to have your changes reviewed. This is done by "creating a PR." PR stands for pull request.

- To make a new PR click the "Pull Requests" link in the header of the github page.

- Your pull request will appear at the top of the page in a yellow box. Click on the blue button "Compare & pull request".

<kbd>![Screenshot how to compare changes in the pull request in github](/non-info/06-help-comparePR.png)</kbd>

- Add a title for your pull request and a description if the title is not self explanatory.
- To the right, click on the gear icon to the right of "Reviewers".
- A dropdown will appear and request people to review your PR.
- If you are unsure who to ask to review your changes, check with your manager.

<kbd>![Screenshot of how to select reviewers of your PR and create the PR in Github](/non-info/07-help-openPR.png)</kbd>

- After selecting reviewers, click the blue "Create pull request" button.

<kbd>![Screenshot of the location of the create pull request button in Github](/non-info/08-help-createPR.png)</kbd>

- Reviewers will receive an email from Github prompting them to review your PR.
  

### 3rd: Merge the PR to `develop`
- Once your PR has been reviewed and approved you can merge your PR to 'develop'.
- Open your PR and scroll down and click on "Merge pull request".

<kbd>![Screenshot of how to merge your pull request in Github](/non-info/09-help-mergePR.png)</kbd>

- You will be prompted to confirm you decision, click "Confirm merge".

  <kbd>![Screenshot of how to confirm merging your PR in Github](/non-info/10-help-confirmMerge.png)</kbd>

- **Please note:** The above step will only put your changes on `develop` and they will not be viewable on info.arxiv.org. At this point you have only saved the edit in github.


### 4th: Create a PR to deploy your changes to `master`

- Once you have merged your PR into `develop`, click on the "Pull Requests" link in the header of the github page.
- Next click on the "New pull request" button.

<kbd>![Screenshot of how create a new PR to deploy your changes in Github](/non-info/11-help-newPR-compare.png)</kbd>

- Next you will compare the changes between the `master` branch and the `develop` branch so you can create a PR to merge your changes into production.
- Click on "base:develop" and a dropdown will open, type in "master" and select "master".

  <kbd>![Screenshot of how to compare differences between develop and production branches in Github](/non-info/12-help-compare-master.png)</kbd>


- Now you can compare and review the changes between the "master" and "develop" branches.
- **Please note:** If you see there are other commits _that are not your own_ waiting to be merged to "master", check in with the owners of those commits before you make a PR to make sure
the commits are ready to go into production.
- If you only your changes are there, go ahead and click on "Create pull request".

 <kbd>![Screenshot of how to create your PR in Github](/non-info/13-help-compare-changes-createPR.png)</kbd>

- You have seen the following steps before with your previous PR.
- Add your title (referencing your ticket if applicable).
- In the description add any additional details.
- Select your reviewers.
- Click "Create pull request".

 <kbd>![Screenshot of how to fill out the information in your PR and create the PR in Github](/non-info/14-help-PR-master-deploy.png)</kbd>

- When your PR is approved, you may deploy your changes by merging it to the branch called `master`. This will
cause automated scripts to deploy the changes to info.arxiv.org.

- If you are unsure how to do this, ask a dev or admin to do it for you.

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
