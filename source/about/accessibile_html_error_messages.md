# Error messages in HTML papers

The process of converting our papers to HTML is a work in progress and as we improve the process you will see fewer errors and formatting issues. 
{ .intro }

The errors that you have seen when viewing  papers in HTML after submission or on arXiv.org are caused by our inability to translate certain Tex and LaTex software packages into HTML. TeX and LaTeX, pronounced ‘tek’ and ‘LAH-tek’, are open source software packages used to accurately display complex mathematical formulae, symbols and tables in research papers. Due to the open source nature of TeX and LaTeX and its popularity, there are an inordinate number of packages available to choose from. This makes supporting all of them very difficult. We are continuously reviewing which features and packages are most popular in an effort to provide error free, accessible HTML papers.

Please note: These errors are only the result of our  inability to properly translate and display certain TeX and LaTex packages as HTML. These errors are not an indication of a larger system failure.

## HTML errors readers may encounter

When browsing and reading HTML papers on arXiv.org, you may see formatting errors in red like below: 

![HTML LaTeX processing error for online id](images/reader-error-01.png)

![HTML LaTeX processing error for tik Z library](images/reader-error-02.png)

![HTML LaTeX processing error for system name and revision](images/reader-error-03.png)



## HTML errors authors and submitters may encounter

After you have submitted your paper and it has been processed, you will receive a link to preview the HTML version of your paper. You may see an error message alerting you that the TeX/LaTeX packages used to format your paper are not fully supported by our conversion process. Therefore your paper may display red TeX/LaTeX code and other formatting irregularities. 

Please see an example of a HTML processing error below:
![html processing error](images/author_submssn_error.png){.mkd-img-full alt='Error message in a red box stating, This paper uses packages, listed below, that do not yet convert to HTML. These issues are known and are being worked on. View the list of unsupported packages.'}

## Frequently Asked Questions

### What is Tex?
TeX is a text formatting and markup language first released in late 1970s by [D. Knuth](https://en.wikipedia.org/wiki/TeX#Hyphenation_and_justification). It was created to properly configure and visualize mathematical formulae, tables and symbols in printed documents such as journals and books. 

### What is LaTex?
LaTeX is a TeX macro package developed in the early 1980s by [Leslie Lamport](https://en.wikipedia.org/wiki/LaTeX#cite_note-Lamport1986-4). It provides the ability to structure a document to meet different layout requirements such as section headers, footnotes, graphics and bibliographies.

### Why are TeX and LaTex  so popular? 
They are beloved by academic communities for their ability to easily display complex mathematical formulae, symbols, charts and graphs that common word processing programs have difficulty with. 

TeX and LaTex are open source software programs and are supported, maintained and iterated upon by the communities that use them. As a result, there are many packages available offering a myriad of features to format research papers. 

TeX and LaTex packages are platform independent which allows for the ability to view documents regardless of the operating system or software set up making collaboration simple.

### Why are TeX and LaTex so difficult to support?
Due to the robust open source community supporting and developing TeX and LaTex packages, there are an enormous number of packages in use. We are continuously reviewing which features and packages are most popular in an effort to provide error free, accessible HTML papers.

### Which TeX/LaTeX packages do you or do not support?
- Please see our list of supported packages
- Please see our list of [unsupported packages](https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML)

## Do you support TikZ?
See What are 'partially' supported packages?

## What are ‘partially’ supported packages? 

A partially supported package is a package that has select features we support in research papers.

For example, TikZ offers the ability to … and we support …. However, TikZ also provides the ability to… which we currently do not support.
