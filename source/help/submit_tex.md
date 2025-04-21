# TeX Submissions

*   [Changes  to (La)TeX processing](#newtex)
*   [Submission 1.0 and 1.5 Comparison](#comparison)


* * *

<span id="newtex"></span>
### (La)TeX processing changes &mdash; coming Early 2025

We will soon be rolling out changes to how arXiv process (La)TeX submissions. These changes should not be noticable to most of our users. We will retire the long-used "AutoTeX" (Submission 1.0) system that we have used for decades in favor of a simpler, more straightfoward process of converting (La)TeX submissions to PDFs in Submission 1.5.

<span id="comparison"></span>
### Submission 1.0 and 1.5 Comparison
For a quick overview of the changes to our Submission system view our chart below. 

| **Feature** | **Submission System 1.0** | **Submission System 1.5** |
| :---------  | :-----------------------  | :------------------------ |
|**Bundled LaTeX Packages**| Supplied ~70 LaTeX packages and class files (many outdated) | Only provides packages included in the current [TeX Live release](faq/texlive.md). Authors with journal style files must now include them with their TeX source. |
|**PDF Compilation**| Tried multiple TeX processors to compile | Uses only the specific TeX processor set in the Review Files step |
|**TeX Versioning**| Infrequent updates (years between updates) | Follows annual TeX Live releases going forward dependent upon arXiv resources |
|**File Detection**| Detects toplevel files by looking for `\documentclass` or `\bye`. All `.tex` files attempted, if none found. | Scan for toplevel files using upt to 40 standard commands.|
|**Extraneous  File Detection**| Did not detect files unrelated to the submission | Detects potentially unused files; flagging them for review |
|**Handling Multiple .tex Files**| Compiled all `.tex` files with `\documentclass` and appended extraneous postscripts figures at the end. Plain TeX, processed by looking for `\bye.` | At the start, assumes just one top-level TeX file.  Submitter can add additional top-level TeX files in the Review Files interface. These will be compiled and the results appended to the output document.  It is preferred that the submitter use `\include` or `\input` directives to embed other TeX files in a document.  For special cases not supported by either of those options please refer to: [The `00README.XXX` file format](00README.md). |
|**Image Files (JPG, PNG, PDF)**| Appended image files verbatim to final PDF in postscript mode, otherwise image files remain in source directory | Images must be included using standard [TeX commands](https://latex-tutorial.com/tutorials/figures/).|
|**hyperref Package**| Automatically added if not present, skipped if there is an error |  No longer modifies IDs; authors should use `\href{}` explicitly, or packages that define it. |
|**Maintenance**| Complex, opaque process | Simpler, more transparent and maintainable system |
|**Transparency**| Opaque and convoluted. It was nearly impossible for authors to build the documents locally in the same manner as arXiv. | The 00README.json file documents all the details used to build a paper, and other services can make use of this format. |
