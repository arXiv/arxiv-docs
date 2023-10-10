# Error messages in HTML papers

HTML papers on arXiv.org are a work in progress and will sometimes display errors. As we work to improve accessibility we share with you the causes of these errors and what authors can do to help minimize them.
{ .intro }

The errors that you have seen when viewing papers in HTML after submission or on arXiv.org are caused when the LaTeXML converter is unable to translate certain TeX and LaTeX software packages. TeX and LaTeX, pronounced ‘tek’ and ‘LAH-tek’, are open source software packages used to accurately display complex mathematical formulae, symbols and tables in research papers. Due to the open source nature of TeX and LaTeX and its popularity, there are many packages available to choose from. This makes supporting all of them very difficult. NIST is routinely assessing and adding LaTeX packages in an effort to provide greater versatility to the LaTeXML converter.


## HTML errors you may see:

When browsing and reading HTML papers on arXiv.org, you may see formatting errors in red like below: 

![html processing error](images/author_submssn_error.png){.mkd-img-full alt='Error message in a red box stating, This paper uses packages, listed below, that do not yet convert to HTML. These issues are known and are being worked on. View the list of unsupported packages.'}

![HTML LaTeX processing error for online id](images/reader-error-01.png){.mkd-img-border alt='Errors are displayed in red markup interpersed with the text. Errors are: forward slash online ID, foward slash v.g.t.c. category, forward slash author footer, foward slash system name, foward slash system name, foward slasch author orcid.'}

![HTML LaTeX processing error for tik Z library](images/reader-error-02.png){.mkd-img-border alt='Tik Z errors are displayed in red markup. Errors are: foward slash use tik z library, foward slash p.g.f. declare decorations simple line initial'}

![HTML LaTeX processing error for system name and revision](images/reader-error-03.png){.mkd-img-border alt='System name errors are displayed in red markup. Errors are: forward slash system name, foward slash revision'
}

## Steps authors can take to minimize HTML errors
Authors and proxies who submit papers to arXiv can help minimize HTML errors by formatting submissions using one of the LateX packages fully supported by LaTeXML. [Please view the list of fully supported LaTeX packages](https://corpora.mathweb.org/corpus/arxmliv/tex_to_html/info/loaded_file).

## Frequently Asked Questions

### What is TeX?
TeX is a text formatting and markup language first released in late 1970s by [D. Knuth](https://en.wikipedia.org/wiki/TeX#Hyphenation_and_justification). It was originally created for [typesetting](https://en.wikipedia.org/wiki/Typesetting) complex mathematical formulae for print production in books and journals. In later versions of TeX, Knuth developed a system of literate programming, where a computer program written in natural language is embedded within the TeX typeset documentation allowing for the source code to be compiled and document to be printed from one file. TeX was designed for two primary purposes: to enable anybody to print high-quality books with minimal effort and to provide a system that delivers precisely the same results on all computers. 

### What is LaTeX?
LaTeX is a software system for document layout and preparation developed in the early 1980s by [Leslie Lamport](https://en.wikipedia.org/wiki/LaTeX#cite_note-Lamport1986-4). LaTeX is designed to provide a descriptive markup language that harnesses the power of TeX in a more user-friendly way. It consists of a collection of TeX macros and a program to process LaTeX documents providing authors with convenient commands to format different layout requirements such as section headers, footnotes, graphics and bibliographies.

### What is TeXML? 
TeXML is an open source XML vocabulary for TeX. Since TeX was designed for typesetting tangible books and journals, it was necessary to create a processor to transfrom TeXML markup into TeX markup in order to utilize LaTeX defined macros to publish XML data having customizable layout options as digital portable document formats aka PDFs.

### What is LaTeXML?

LaTeXML was developed at the [Digital Library of Mathematical Functions at NIST](https://math.nist.gov/) (National Institute of Standards and Technology) and is authored by Bruce Miller and Deyan Ginev. It's primary output is XML and a postprocessor can convert these XML documents into HTML with mathematical forumulas as images or XHTML, HTML5, EPUB with formulas as MathML. 

### What is MathML?
MathML is mathematical markup language and is an XML based application. MathML is used to describe and encode mathematical notation and scientific content for distribution on the web and other applications such as scientific software, print typesetting and voice synthesis. 

### Why are TeX and LaTeX so popular? 
They are beloved by academic communities for their ability to easily display complex mathematical formulae, symbols, charts and graphs that common word processing programs have difficulty rendering.

TeX and LaTeX are open source software programs  that  are platform independent which allows for the ability to view documents regardless of the operating system or software set-up making collaboration simple. These programs are maintained and iterated upon by the communities that use them, and as a result, there are many packages available offering a myriad of features to format research papers. 

### Why are TeX and LaTeX so difficult to support?
In progress...

### Which TeX/LaTeX packages are supported?
- Please see our list of [supported packages](https://corpora.mathweb.org/corpus/arxmliv/tex_to_html/info/loaded_file)
- Please see our list of [unsupported packages](https://github.com/brucemiller/LaTeXML/wiki/Porting-LaTeX-packages-for-LaTeXML)

### Is TikZ supported?
Partially, please see 'What are partially supported packages?' below.

### What are ‘partially’ supported packages? 

A partially supported package is a package that has select features NIST has chosen to support in LaTeXML. For example, TikZ offers the ability to … (need to add list of features) and LaTeXML supports …. (add list of features supported) However, TikZ also provides the ability to… which LaTeXML does not support.

