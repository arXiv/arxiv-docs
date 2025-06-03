# info.arxiv.org pages

Help, about, policy and other pages for arXiv.

## Overview

This is where to make edits to the about, help, labs, new and other pages at
info.arxiv.org. These are written in
[markdown](https://daringfireball.net/projects/markdown/) and turned into HTML
pages with [mkdocs-material](https://squidfunk.github.io/mkdocs-material/).

## How to do a Quick Edit on github

To make a quick edit, use this is a 4 step process:

1. Make your edit and commit to a new branch.

2. Make a PR from your branch to develop, get that reviewed.

3. Merge the PR to develop.

4. Merge changes on develop to master.<br><br>

### 1. Make your edit on github
- To edit a page first go to the info.arxiv.org page you want to edit.  
Example: https://info.arxiv.org/help/gzip.html

- Click on the pencil icon to edit the page. That will take you to the corresponding page in github.

<kbd>![Screenshot of a page on info.arxiv.org and the location of the edit icon](/non-info/01-help-info-page.png)</kbd><br><br>

- On the page you want to edit in github, click the pencil to edit the page contents right in github.

<kbd>![Screenshot of a page in Github and the location of the edit icon](/non-info/02-help-github-edit-page.png)</kbd><br><br>

- After you have made changes, click preview to see how it will look when completed.  
**Please note:** Github uses "Github flavored markdown" which is different from the markdown we use to create our documentation. There may be small variations in how the markdown appears due to these differences.

<kbd>![Screenshot of the location of the preview button on the edited page in Github](/non-info/03-help-preview-github.png)</kbd><br><br>

- Review your work in preview mode. To return to editing, click on "edit" in the header.

<kbd>![Screenshot displaying the preview of your edits in Github](/non-info/12-help-preview-page.png)</kbd><br><br>

- Once you are happy with your changes you can save by clicking on the "Commit changes" button in the upper right hand corner.
Commit is the term github and git use for saving.

<kbd>![Screenshot of the location of the commit button on the edited page in Github](/non-info/04-help-commit-github.png)</kbd><br><br>

- Add a brief note in the "Commit message" area summarizing your edit. You may add longer
note in the "Extended description" area if you have more to say about your changes.

- Make sure you have your email associated with your commits.

- Note that a "new branch for this request and start a pull request" will be selected.
- Name your branch after your JIRA ticket (if applicable) or after your github username and brief description.  
Examples:  
 `arxivce-1503-update-arxiv-docs-readme`  
 `alisonhofer-update-arxiv-docs-readme`

<kbd>![Screenshot of how to create a new branch for the edits made in Github](/non-info/05-help-newBranch.png)</kbd><br><br>

>If you have more changes to make at this time you may make and commit them all to the branch you created. The additional changes you commit will be grouped together when you make your pull request in the next step.

<br>

### 2. Make a Pull Request from your branch to `develop`
Once you have completed all of your changes, you need to have your changes reviewed. This is done by "creating a PR." PR stands for pull request.

- At the top of your page you will notice a yellow box that will have the name of your commit and a button to the right of it that says "Compare & pull request".

- Click on Compare & pull request

<kbd>![Screenshot how to compare changes in the pull request in github](/non-info/06-help-comparePR.png)</kbd> <br><br>

>> In the event that you have made a commit and were unable to complete or create your pull request at the time, you will not have the same yellow box interface if you return to the page the next day.  
>>
>>>You will have to make a pull request by clicking on the "Pull requests" link in the header of the github  
>>>Next, click the button to the right that says "New pull request"
>>
>><kbd>![Screenshot how to compare changes in the pull request in github](/non-info/11-help-newPR-compare.png)</kbd>

<br>

- Compare your changes by clicking on the "compare:develop" dropdown and type in your branch name and then select your branch.
- This will compare your branch to the `develop` branch.

<kbd>![Screenshot how to compare changes in the pull request in github](/non-info/12-help-newPR-compare.png)</kbd><br><br>

- Click on the "Files Changed" tab to view a comparison of the `develop` branch you are planning to merge into master.

<kbd>![Screenshot how to compare changes in the pull request in github](/non-info/compareFiles.png)</kbd><br><br>

- Click "Create pull request"
- Add a title for your pull request and a description if the title is not self explanatory.
- To the right, click on the gear icon to the right of "Reviewers".
- A dropdown will appear and request people to review your PR.
- If you are unsure who to ask to review your changes, check with your manager.

<kbd>![Screenshot of how to select reviewers of your PR and create the PR in Github](/non-info/07-help-openPR.png)</kbd><br><br>

- After selecting reviewers, click the blue "Create pull request" button.

<kbd>![Screenshot of the location of the create pull request button in Github](/non-info/08-help-createPR.png)</kbd>
- Reviewers will receive an email from Github with a link to the PR to review.
- Additionally, you can slack your reviewers with a link to your PR to give them a heads up.

<br>

### 3. Merge the PR to `develop`
- Once your PR has been reviewed and approved you will receive an email notification with a link to your PR. 
- Now you can merge your PR to `develop`.
- Open your PR and scroll down and click on "Merge pull request".

<kbd>![Screenshot of how to merge your pull request in Github](/non-info/09-help-mergePR.png)</kbd><br><br>

- You will be prompted to confirm you decision, click "Confirm merge".

  <kbd>![Screenshot of how to confirm merging your PR in Github](/non-info/10-help-confirmMerge.png)</kbd>

- **Please note:** The above step will only put your changes on `develop` and they will not be viewable on the live site: info.arxiv.org. At this point you have only saved the edit(s) in github.
- You can review your changes on the `develop` site at [info.dev.arxiv.org](info.dev.arxiv.org).

<br>

### 4. Make a Pull Request from `develop` to `master`
> **Please note:** Once you have merged your changes to `develop`, it is important to deploy them as soon as possible. Lingering commits on on the `develop` branch can cause unintentional problems when they are deployed with other code. If you notice commits other than your own in the PR you make, please be sure to check in with the owners of those commits to ensure they are ready to go live. 

- Now that your PR has been merged to `develop`, you need to deploy these changes to `master`. 
- To make a new PR click the "Pull requests" link in the header of the github page.
- On the right hand side, click the blue button that says "New pull request"

<kbd>![Screenshot how to compare changes in the pull request in github](/non-info/11-help-newPR-compare.png)</kbd><br><br>

- Compare your changes by clicking on the "base:develop" dropdown on the left and type in "master" and then select it.
- This will compare your branch to the `develop` branch.

<kbd>![Screenshot how to compare changes in the pull request in github](/non-info/compareToMaster.png)</kbd><br><br>

- Click on the "Files Changed" tab to view a comparison of the `develop` branch you are planning to merge into `master`.

<kbd>![Screenshot how to compare changes between the develop branch and the master branch in github](/non-info/filesChanged-createPR.png)</kbd><br><br>
- Click "Create pull request"

- Add a title for your pull request and a description if the title is not self explanatory.
- To the right, click on the gear icon to the right of "Reviewers"
- A dropdown will appear and you can request people to review your PR.
- After selecting reviewers, click the blue "Create pull request" button.
- Ping your reviewers in slack with a link to your PR and ask them to review it.

- Once your PR has been reviewed and approved you can merge your PR to `master`.
- Open your PR and scroll down and click on "Merge pull request".
- You will be prompted to confirm you decision, click "Confirm merge".
- You will see your changes on production about 15 minutes after you have confirmed your merge.

<br>

## Authoring Markdown
See [AUTHORING.md](AUTHORING.MD)

## Building on your local machine

Instead of using github to edit you can check all the files for arxiv-docs to
your laptop to edit and preview.

```bash
git clone git@github.com:arXiv/arxiv-docs.git
cd arxiv-docs
python --version
# 3.11.12
python -m venv docs-venv
source docs-venv/bin/activate
pip install -r requirements.txt
mkdocs serve
google-chrome https://localhost:8000/index.html
```
Then you will have the site served locally with hot reloading on edits. In your
browser, go to http://localhost:8000/index.html

To clean up when you're done: 
```bash
deactivate
python -m venv docs-venv --clear
```


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
