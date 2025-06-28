# Submission of PDF

If you are submitting a PDF document, please make sure to follow these
guidelines:

-   Submit one PDF file including all text and figures. PDF can
    efficiently include photographs imported in JPEG format. We do not
    permit submissions that include multiple PDF files, or PDF files in
    combination with other file types.
-   You must ensure that all standard and non-standard fonts are included and that
    outline (TrueType/Type1) rather than bitmap (Type3) fonts are used.
    In Adobe Distiller and many other products this is referred to as
    *compatibility mode* and will ensure that the PDF document is as
    portable as possible.
-   Note: a PDF file created from a TeX/LaTeX file will typically be rejected, with exceptions granted on a case-by-case basis.
    There are [good reasons](faq/whytex.md) why arXiv insists on
    TeX/LaTeX source if it is available. arXiv produces PDF
    automatically from all TeX submitted source. For information on
    viewing the PDF provided by arXiv, see our [PDF browsing
    help](pdf.md).

While PDF can be very useful, it has some limitations. Including large figures in PDF can hamper the
display of the document so that it is unusable. Authors should keep in
mind that not everyone will have a high-end machine, and they should
compose their documents accordingly with efficient figures.

### Creating PDF ###

Many authoring applications can directly create or export as PDF. Freely
available examples include [OpenOffice.org](http://www.openoffice.org/),
[Google Docs](http://docs.google.com), or [Microsoft Office](https://www.microsoft.com/en-us/microsoft-365/microsoft-office).

Below are guidelines to assist you with exporting an accessible and machine readable PDF:

#### Save a PDF from Word on a Mac ####

- Open your document in Microsoft Word.
- Go to the File tab and select ***Save As***.
- Choose a location to save your PDF.
- Under the File Format dropdown menu select ***PDF***.
- Next select the option: ***Best for electronic distribution and accessibility (uses Microsoft online service)***.
- Please note: when using Microsoft online service, the only font that Microsoft has legal rights to can be used. If your document contains custom fonts, they will be substituted and your text may not appear as intended. To avoid this issue, [embed your fonts into the document](https://support.microsoft.com/en-us/office/benefits-of-embedding-custom-fonts-cb3982aa-ea76-4323-b008-86670f222dbc#OfficeVersion=macOS&officeversion=macos). 
- Click ***Export***.
- ***Avoid*** using ***Print to PDF***. This may rasterize your document which will convert it to a bitmapped image.

#### Save a PDF from Word on a PC ####

- Open your document in Microsoft Word.
- Go to the File tab and select ***Save As***.
- Choose a location to save your PDF.
- Under the ***Save as type*** dropdown menu select ***PDF***.
- Next click the ***Options*** button.
    - Select ***Document structure tags*** for accessibility.
This option makes the document easier for screen-reading software to read.
    - Select ***ISO 19005-1 compliant (PDF/A)***
This option saves the document as the archiving standard and ensures the document will look the same when it is opened on a different computer.
Please note: when using when saving as PDF, the only font that Microsoft has legal rights to can be used. If your document contains custom fonts, they will be substituted and your text may not appear as intended. To avoid this issue, embed your fonts into the document. 
- Select ***Save***.
- ***Avoid*** using ***Print to PDF***. This may rasterize your document which will convert it to a bitmapped image.

#### Save a PDF from Google ####

- Open your document in Google Docs.
- Go to ***File*** and select ***Download***.
- Select ***PDF Document***.
The PDF will be automatically downloaded to your computer.
- ***Please note***: While the text is technically “readable”, Google Docs PDF export does not include document structure tags (for headings, paragraphs, lists, table headers, etc.). 
    - ***Screen readers and assistive technologies*** rely on document structure tags to understand the logical flow and structure of the document.
    - ***Complex text extraction*** requires document structure tags to correctly interpret the different parts of the document and how they relate to each other.
    - ***Create a machine readable PDF with structure tags*** by using an add-on designed specifically for this purpose. [Grackle Docs](https://workspace.google.com/marketplace/app/grackle_docs/1085622905455) is a widely recommended add-on for Google Workspace that checks for accessibility and can export tagged PDFs.


### Avoid Embedded JavaScript ###

Do not include embedded JavaScript such as animated gifs, movies, or HTML in your PDF. Submissions with embedded JavaScript are automatically rejected due to the potential security risks posed to arXiv systems. 

- Submit all movies and animated GIFS as separate(non-JavaScript) ancillary files.
- Remove or disable JavaScript when building your PDF or generate PDFs using standard tools such as Adobe Distiller or one of the free conversion utilities mentioned above. 

### Fonts within Musig2 stable E7 PDF ###


**Caution when using pre-unicode fonts**  
In order to increase the accessibility of our papers, we attempt to detect PDFs that contain non-standard character encoding for ligatures. Ligatures are when a sequence of characters are combined into a single character or glyph to improve their appearance. Characters that have features that would visually run into one another when used next to each other in the process of typesetting, such as ff, ffi, ffl, fi and fl, are commonly converted to ligatures.

![Example of ligatures](../about/images/ligatureExampleResized.png){mkd-border alt='The letters f and i are displayed as individual characters typeset next to one another and then displayed as a ligature combined into one character. The letters f and l are displayed as individual characters typeset next to one another and then displayed as a ligature combined into one character.'}

Ligatures in PDFs may also not encode properly which may cause the ligatures not to display correctly or not at all. This can impact the ability of assistive technology to read or pronounce words correctly. You can check your PDF by asking a screen reader (there is one built into the Microsoft Edge browser) to read your paper aloud; if words like "different", "first", or "official" are pronounced incorrectly, your PDF uses a font which has this issue. Another way to check your paper is by copying and pasting sections of text from the PDF into a text editor, and look for missing strings such as “ff”, “fi”, “fl”, etc.  If you enable spell checking in your text editor, words with missing glyphs should be highlighted as spelling errors.

**Embedding non-standard fonts**  
Fonts used in PDF files may be embedded or non-embedded. PDF viewers silently attempt to render non-embedded fonts, potentially resulting in documents looking different for different users. Non-embedded fonts, especially fonts with non-standard characters,  may render differently on different machines. To avoid errors in text rendering, we recommend using PDF tools which embed all of the fonts used in your PDF. arXiv may reject PDF submissions because of non-standard, non-embedded fonts. For more information, see [https://helpx.adobe.com/acrobat/using/pdf-fonts.html](https://helpx.adobe.com/acrobat/using/pdf-fonts.html).

### PDF must be machine readable ###

arXiv relies on our submitters to provide a PDF which is *machine readable*
to facilitates **discovery and access**. This means we can build tools around your work to provide content discovery (e.g. full text search), and readers can still understand its contents using tools such as screen readers.

Elements that prevent a PDF machine readability and text extraction include: 
- Bitmaps of the entire paper generated from TeX, examples include: 
    - Scanned documents converted to PDFs
    - OCR created documents converted to PDFs 
- Use of PostScript Type 3 fonts within a tex-produced document
- Exported from Google or Word causing fonts to export improperly

### How to make your PDF machine readable ###

It is important to start with a machine readable document before you export it to PDF. You can improve machine readability of your document by following these recommendations:
- Use standard fonts
- Use standard formatting techniques such as: 
    - Built-in heading styles
    - Built-in structured lists
    - Tables that are properly formatted
    - Alt text with images

### Copyright within PDF ###


Copyright statements of the author are permitted within the pdf. Copyright
statements which prohibit or impair arXiv's [redistribution license](license/index.md) will be rejected. If explicit permission is
given for open access redistribution, these are permissible.
Users should contact [arXiv user support](https://arxiv.org/support) if they have questions.

Note on IEEE submissions. Please note arXiv will currently take the
'Accepted' IEEE version but not the 'Published' IEEE version. For more
information on IEEE policies please see:

-   [IEEE
    FAQ](https://www.ieee.org/content/dam/ieee-org/ieee/web/org/pubs/author_version_faq.pdf)
-   [IEEE Rights
    Policy](http://www.ieee.org/publications_standards/publications/rights/rights_policies.html)
-   [IEEE Third Party
    Servers](http://www.ieee.org/publications_standards/publications/rights/thirdpartyservers.html#sect2)
