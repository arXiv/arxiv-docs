# Theme generator
This will use arxiv-base to generate a theme for mkdocs-material

# Instructions
To make changes to arxiv's mkdocs override.html make the changes to 
make_arxiv_theme/templates/main.html and then run the following commands:

```bash
cd arxiv-docs
./make_arxiv_theme/prep_for_mkdocs.sh
```

That will recreate the `overrides/main.html` with the changes.

# IMPORTANT: mkdocs and mkdocs-material are different
`mkdocs` and `mkdocs-material` use different themes and these themes are
organized differently. Make sure you are looking at the documentation for
`mkdocs-material` when you are looking for features or solutions.
