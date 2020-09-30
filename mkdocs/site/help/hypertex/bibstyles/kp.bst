%
% $Id: kasper.bst,v 1.21 2010/07/06 16:36:43 peekas Exp $
%
% Bibliography style with hyperlinks and arXiv references (handles
% both old and new style arXiv references). Based on utphys.bst and
% unsrtnat.bst.
%
%
% Kasper Peeters <kasper.peeters@durham.ac.uk>
%

ENTRY
  { address
    author
    booktitle
    chapter
    edition
    editor
    howpublished
    institution
    journal
    key
    month
    note
    number
    organization
    pages
    publisher
    school
    series
    title
    type
    volume
    year
    archive
    archivePrefix
    primaryClass
    eprint
    report
    collaboration
    citation
    SLACcitation
  }
  {}
  { label extra.label sort.label short.list }

INTEGERS { output.state before.all mid.sentence after.quote after.sentence
                after.quoted.block after.block }

FUNCTION {init.state.consts}
{ #0 'before.all :=
  #1 'mid.sentence :=
  #2 'after.quote :=
  #3 'after.sentence :=
  #4 'after.quoted.block :=
  #5 'after.block :=
}

STRINGS { s t }

FUNCTION {output.nonnull}
{ 's :=
  output.state mid.sentence =
    { ", " * write$ }
    { output.state after.quote =
        { " " * write$ }
        { output.state after.block =
            { add.period$ write$
              newline$
              "\newblock " write$
            }
            { output.state before.all =
                'write$
                { output.state after.quoted.block =
                    { write$
                      newline$
                      "\newblock " write$
                    }
                    { add.period$ " " * write$ }
                  if$
                }
              if$
            }
          if$
        }
      if$
      mid.sentence 'output.state :=
    }
  if$
  s
}

FUNCTION {output}
{ duplicate$ empty$
    'pop$
    'output.nonnull
  if$
}

FUNCTION {output.check}
{ 't :=
  duplicate$ empty$
    { pop$ "empty " t * " in " * cite$ * warning$ }
    'output.nonnull
  if$
}

FUNCTION {blank.sep}
{ after.quote 'output.state :=
}

FUNCTION {fin.entry}
{ output.state after.quoted.block =
    'skip$
    'add.period$
  if$
  write$
  newline$
}

FUNCTION {new.block}
{ output.state before.all =
    'skip$
    { output.state after.quote =
        { after.quoted.block 'output.state := }
        { after.block 'output.state := }
      if$
    }
  if$
}

FUNCTION {new.sentence}
{ output.state after.block =
    'skip$
    { output.state before.all =
        'skip$
        { after.sentence 'output.state := }
      if$
    }
  if$
}

FUNCTION {not}
{   { #0 }
    { #1 }
  if$
}

FUNCTION {and}
{   'skip$
    { pop$ #0 }
  if$
}

FUNCTION {or}
{   { pop$ #1 }
    'skip$
  if$
}

FUNCTION {new.block.checka}
{ empty$
    'skip$
    'new.block
  if$
}

FUNCTION {new.block.checkb}
{ empty$
  swap$ empty$
  and
    'skip$
    'new.block
  if$
}

FUNCTION {new.sentence.checka}
{ empty$
    'skip$
    'new.sentence
  if$
}

FUNCTION {field.or.null}
{ duplicate$ empty$
    { pop$ "" }
    'skip$
  if$
}

FUNCTION {emphasize}
{ duplicate$ empty$
    { pop$ "" }
    { "{\em " swap$ * "}" * }
  if$
}

INTEGERS { nameptr namesleft numnames }

FUNCTION {format.names}
{ 's :=
  #1 'nameptr :=
  s num.names$ 'numnames :=
  numnames 'namesleft :=
    { namesleft #0 > }
    { s nameptr "{f.~}{vv~}{ll}{, jj}" format.name$ 't :=
      nameptr #1 >
        { namesleft #1 >
            { ", " * t * }
            { numnames #2 >
                { "," * }
                'skip$
              if$
              t "others" =
                { " {\em et~al.}" * }
                { " and " * t * }
              if$
            }
          if$
        }
        't
      if$
      nameptr #1 + 'nameptr :=
      namesleft #1 - 'namesleft :=
    }
  while$
}

FUNCTION {format.authors}
{ author empty$
    { "" }
    { author format.names }
  if$
}

FUNCTION { format.hyperlink }
{ duplicate$ #1 #5 substring$ "arXiv" =
     { #7 #9 substring$  }
     { "" * }
  if$
}

% FUNCTION {format.authors}
% 	 { eprint empty$
% 			{ format.authors2 }
% 			{ "\href{" * eprint  * "}{" * format.authors2 * "}" }
% 		  if$
% 	 }

FUNCTION { format.longeprint }
{ duplicate$ #1 #5 substring$ "arXiv" =
     { #1 #15 substring$  }
     { "" * }
  if$
}

FUNCTION {format.eprint}
{ eprint empty$
		 { ""}
		 { primaryClass empty$
				{" \href{http://xxx.lanl.gov/abs/" eprint format.hyperlink * "}" * 
					"{{\ttfamily " * eprint format.longeprint * "}}" *}
				{ archivePrefix empty$
                {" \href{http://xxx.lanl.gov/abs/" eprint format.hyperlink * "}" * 
				 	   "{{\ttfamily " * archivePrefix * eprint format.longeprint * "}}" *}
                {" \href{http://xxx.lanl.gov/abs/" eprint format.hyperlink * "}" * 
				 	   "{{\ttfamily " * archivePrefix * ":" * eprint format.longeprint * "}}" *}
              if$
            }
			if$
		 }
  if$
}

FUNCTION {format.report}
{ report empty$
     { ""}
     { report}
     if$
}

FUNCTION {format.editors}
{ editor empty$
    { "" }
    { editor format.names
      editor num.names$ #1 >
        { ", eds." * }
        { ", ed." * }
      if$
    }
  if$
}

FUNCTION {format.title}
{ title empty$
    { "" }
    { "``" title "t" change.case$ * "''," * }
  if$
}

FUNCTION {format.title.p}
{ title empty$
    { "" }
    { "``" title "t" change.case$ * "''." * }
  if$
}

FUNCTION {format.full.names}
{'s :=
  #1 'nameptr :=
  s num.names$ 'numnames :=
  numnames 'namesleft :=
    { namesleft #0 > }
    { s nameptr
      "{vv~}{ll}" format.name$ 't :=
      nameptr #1 >
        {
          namesleft #1 >
            { ", " * t * }
            {
              numnames #2 >
                { "," * }
                'skip$
              if$
              t "others" =
                { " et~al." * }
                { " and " * t * }
              if$
            }
          if$
        }
        't
      if$
      nameptr #1 + 'nameptr :=
      namesleft #1 - 'namesleft :=
    }
  while$
}

FUNCTION {author.editor.key.full}
{ author empty$
    { editor empty$
        { key empty$
            { cite$ #1 #3 substring$ }
            'key
          if$
        }
        { editor format.full.names }
      if$
    }
    { author format.full.names }
  if$
}

FUNCTION {author.key.full}
{ author empty$
    { key empty$
         { cite$ #1 #3 substring$ }
          'key
      if$
    }
    { author format.full.names }
  if$
}

FUNCTION {editor.key.full}
{ editor empty$
    { key empty$
         { cite$ #1 #3 substring$ }
          'key
      if$
    }
    { editor format.full.names }
  if$
}

FUNCTION {make.full.names}
{ type$ "book" =
  type$ "inbook" =
  or
    'author.editor.key.full
    { type$ "proceedings" =
        'editor.key.full
        'author.key.full
      if$
    }
  if$
}

FUNCTION {output.bibitem}
{ newline$
  "\bibitem[" write$
  label write$
  ")" make.full.names duplicate$ short.list =
     { pop$ }
     { * }
   if$
  "]{" * write$
  cite$ write$
  "}" write$
  newline$
  ""
  before.all 'output.state :=
}

FUNCTION {n.dashify}
{ 't :=
  ""
    { t empty$ not }
    { t #1 #1 substring$ "-" =
        { t #1 #2 substring$ "--" = not
            { "--" *
              t #2 global.max$ substring$ 't :=
            }
            {   { t #1 #1 substring$ "-" = }
                { "-" *
                  t #2 global.max$ substring$ 't :=
                }
              while$
            }
          if$
        }
        { t #1 #1 substring$ *
          t #2 global.max$ substring$ 't :=
        }
      if$
    }
  while$
}

FUNCTION {format.date}
{  year duplicate$ empty$
       { "empty year in " cite$ * warning$
          pop$ "" }
       'skip$
     if$
     month empty$
       'skip$
       { month
         " " * swap$ *
       }
     if$
     extra.label *
}

FUNCTION {format.date.paren}
{ year duplicate$ empty$
    { "empty year in " cite$ * warning$
       pop$ "" }
    { pop$
      "(" year * ")" * }
  if$
  month empty$
    'skip$
    { month
      " " * swap$ *
    }
  if$
  extra.label *
}


FUNCTION {format.collaboration}
{ collaboration empty$
    { "" }
    { "{\bfseries " collaboration * "} " * "Collaboration" * }
  if$
}

FUNCTION {format.citation}
{ citation empty$
  {""}
  { newline$ citation output "" newline$ }
  if$
}

FUNCTION {format.SLACcitation}
{ SLACcitation empty$
  {""}
  { newline$ SLACcitation output "" newline$ }
  if$
}


FUNCTION {format.btitle}
{ title emphasize
}

FUNCTION {tie.or.space.connect}
{ duplicate$ text.length$ #3 <
    { "~" }
    { " " }
  if$
  swap$ * *
}

FUNCTION {either.or.check}
{ empty$
    'pop$
    { "can't use both " swap$ * " fields in " * cite$ * warning$ }
  if$
}

FUNCTION {format.bvolume}
{ volume empty$
    { "" }
    { "vol.~" volume *
      series empty$
        'skip$
        { " of " * series emphasize * }
      if$
      "volume and number" number either.or.check
    }
  if$
}

FUNCTION {format.number.series}
{ volume empty$
    { number empty$
        { series field.or.null }
        { output.state mid.sentence =
            { "no.~" }
            { "No.~" }
          if$
          number *
          series empty$
            { "there's a number but no series in " cite$ * warning$ }
            { " in " * series * }
          if$
        }
      if$
    }
    { "" }
  if$
}

FUNCTION {format.edition}
{ edition empty$
    { "" }
    { edition "l" change.case$ "~ed." * }
  if$
}


INTEGERS { multiresult }

FUNCTION {multi.page.check}
{ 't :=
  #0 'multiresult :=
    { multiresult not
      t empty$ not
      and
    }
    { t #1 #1 substring$
      duplicate$ "-" =
      swap$ duplicate$ "," =
      swap$ "+" =
      or or
        { #1 'multiresult := }
        { t #2 global.max$ substring$ 't := }
      if$
    }
  while$
  multiresult
}

FUNCTION {format.pages}
{ pages empty$
    { "" }
    { pages multi.page.check
        { "pp.~" pages n.dashify * }
        { "p.~" pages * }
      if$
    }
  if$
}

FUNCTION {format.pages.nopp}
{ pages empty$
    { "" }
    { pages multi.page.check
        { pages n.dashify  }
        { pages }
      if$
    }
  if$
}


FUNCTION {format.volume}
{ volume empty$
    { "" }
    { "{\bfseries " volume * "}" * }
  if$
}

FUNCTION {format.number}
{ number empty$
    { "" }
    { "no.~" number * "," *}
  if$
}

FUNCTION {format.chapter.pages}
{ chapter empty$
    'format.pages
    { type empty$
        { "ch.~" chapter * }
        { type "l" change.case$ chapter tie.or.space.connect }
      if$
      pages empty$
        'skip$
        { ", " * format.pages * }
      if$
    }
  if$
}

FUNCTION {format.in.ed.booktitle}
{ booktitle empty$
    { "" }
    { "in ``" booktitle * "''" *
      editor empty$
        'skip$
        { ", " * format.editors *  }
      if$
    }
  if$
}

FUNCTION {format.thesis.type}
{ type empty$
    'skip$
    { pop$
      output.state after.block =
        { type "t" change.case$ }
        { type "l" change.case$ }
      if$
    }
  if$
}

FUNCTION {empty.misc.check}
{ author empty$ title empty$ howpublished empty$
  month empty$ year empty$ note empty$
  and and and and and
    { "all relevant fields are empty in " cite$ * warning$ }
    'skip$
  if$
}

FUNCTION {format.tr.number}
{ type empty$
    { "Tech. Rep." }
    'type
  if$
  number empty$
    { "l" change.case$ }
    { number tie.or.space.connect }
  if$
}

FUNCTION {format.paddress}
{ address empty$
    { "" }
    { "(" address * ")" * }
  if$
}

FUNCTION {format.article.crossref}
{ key empty$
    { journal empty$
        { "need key or journal for " cite$ * " to crossref " * crossref *
          warning$
          ""
        }
        { "in {\em " journal * "\/}" * }
      if$
    }
    { "in " key * }
  if$
  " \cite{" * crossref * "}" *
}

FUNCTION {format.crossref.editor}
{ editor #1 "{vv~}{ll}" format.name$
  editor num.names$ duplicate$
  #2 >
    { pop$ " {\em et~al.}" * }
    { #2 <
        'skip$
        { editor #2 "{ff }{vv }{ll}{ jj}" format.name$ "others" =
            { " {\em et~al.}" * }
            { " and " * editor #2 "{vv~}{ll}" format.name$ * }
          if$
        }
      if$
    }
  if$
}

FUNCTION {format.book.crossref}
{ volume empty$
    { "empty volume in " cite$ * "'s crossref of " * crossref * warning$
      "In "
    }
    { "Vol.~" volume *
      " of " *
    }
  if$
  editor empty$
  editor field.or.null author field.or.null =
  or
    { key empty$
        { series empty$
            { "need editor, key, or series for " cite$ * " to crossref " *
              crossref * warning$
              "" *
            }
            { "{\em " * series * "\/}" * }
          if$
        }
        { key * }
      if$
    }
    { format.crossref.editor * }
  if$
  " \cite{" * crossref * "}" *
}

FUNCTION {format.incoll.inproc.crossref}
{ editor empty$
  editor field.or.null author field.or.null =
  or
    { key empty$
        { booktitle empty$
            { "need editor, key, or booktitle for " cite$ * " to crossref " *
              crossref * warning$
              ""
            }
            { "in {\em " booktitle * "\/}" * }
          if$
        }
        { "in " key * }
      if$
    }
    { "in " format.crossref.editor * }
  if$
  " \cite{" * crossref * "}" *
}

%---------------------------------------------------------------
% Output functions for each record type.
%---------------------------------------------------------------

FUNCTION {article}
{ output.bibitem
  format.collaboration output
  format.authors "author" output.check
  format.title   "title" output.check
  blank.sep
  crossref missing$
  { journal missing$   
    { eprint missing$ 
        { format.date output }
        {blank.sep}
        if$
      } 
    { journal emphasize "journal" output.check
      volume empty$
        { format.date "year" output.check
        }
        { blank.sep
          format.volume output
          blank.sep 
          format.date.paren "year"  output.check
        }
      if$
      month empty$
                { format.number output }
                'skip$
         if$
      blank.sep
      format.pages.nopp output
      }
      if$
      report missing$
            {format.eprint output}
            {blank.sep format.report output format.eprint output}
            if$
    }
    { format.article.crossref output.nonnull
      format.pages output
      format.eprint output
    }
  if$
  note output
  new.sentence
  format.citation output
  format.SLACcitation output
  fin.entry
}

FUNCTION {book}
{ output.bibitem
  format.collaboration output
  author empty$
    { format.editors "author and editor" output.check }
    { format.authors output.nonnull
      crossref missing$
        { "author and editor" editor either.or.check }
        'skip$
      if$
    }
  if$
  format.title "title" output.check
  blank.sep
  crossref missing$
    { %format.bvolume output
      %new.block
      %format.number.series output
      %new.sentence
      publisher "publisher" output.check
      address output
    }
    { new.block
      format.book.crossref output.nonnull
    }
  if$
  format.edition output
  format.date "year" output.check
  new.block
  note output
  format.SLACcitation output
  fin.entry
}

FUNCTION {booklet}
{ output.bibitem
  format.collaboration output
  format.authors output
  title empty$
    { "empty title in " cite$ * warning$
      howpublished new.sentence.checka
    }
    { howpublished empty$ not
      address empty$ month empty$ year empty$ and and
      or
        { format.title.p output.nonnull }
        { format.title output.nonnull }
      if$
      blank.sep
    }
  if$
  howpublished output
  address output
  format.date output
  new.block
  note output
  fin.entry
}

FUNCTION {inbook}
{ output.bibitem
  format.collaboration output
  author empty$
    { format.editors "author and editor" output.check }
    { format.authors output.nonnull
      crossref missing$
        { "author and editor" editor either.or.check }
        'skip$
      if$
    }
  if$
  format.btitle "title" output.check
  crossref missing$
    { format.bvolume output
      format.chapter.pages "chapter and pages" output.check
      new.block
      format.number.series output
      new.block
      publisher "publisher" output.check
      address output
    }
    { format.chapter.pages "chapter and pages" output.check
      new.block
      format.book.crossref output.nonnull
    }
  if$
  format.edition output
  format.date "year" output.check
  new.block
  format.eprint output
  new.block
  note output
  fin.entry
}

FUNCTION {incollection}
{ output.bibitem
  format.collaboration output
  format.authors "author" output.check
  format.title "title" output.check
  blank.sep
  format.in.ed.booktitle "booktitle" output.check
  format.bvolume output
  format.number.series output
  format.chapter.pages output
  new.block
  publisher "publisher" output.check
  address output
  format.edition output
  format.date "year" output.check
  new.block
  format.eprint output
  new.block
  note output
  format.SLACcitation output
  fin.entry
}

FUNCTION {inproceedings}
{ output.bibitem
  format.collaboration output
  format.authors "author" output.check
  format.title "title" output.check
  blank.sep
  crossref missing$
    { format.in.ed.booktitle "booktitle" output.check
      format.bvolume output
      format.number.series output
      format.pages output
      organization output
      new.block
      publisher output
      address output
      format.date "year" output.check
    }
    { format.incoll.inproc.crossref output.nonnull
      format.pages output
    }
  if$
  new.block
  format.eprint output
  new.block
  note output
  format.SLACcitation output
  fin.entry
}

FUNCTION {conference} { inproceedings }

FUNCTION {manual}
{ output.bibitem
  format.collaboration output
  author empty$
    { organization empty$
        'skip$
        { organization output.nonnull
          address output
        }
      if$
    }
    { format.authors output.nonnull }
  if$
  format.btitle "title" output.check
  author empty$
    { organization empty$
        { address new.block.checka
          address output
        }
        'skip$
      if$
    }
    { organization address new.block.checkb
      organization output
      address output
    }
  if$
  format.edition output
  format.date output
  new.block
  note output
  fin.entry
}

FUNCTION {mastersthesis}
{ output.bibitem
  format.authors "author" output.check
  format.title "title" output.check
  blank.sep
  "Master's thesis" format.thesis.type output.nonnull
  school "school" output.check
  address output
  format.date "year" output.check
  new.block
  note output
  format.SLACcitation output
  fin.entry
}

FUNCTION {misc}
{ output.bibitem
  format.collaboration output
  format.authors output
  title empty$
    { howpublished new.sentence.checka }
    { howpublished empty$ not
      month empty$ year empty$ and
      or
        { format.title.p output.nonnull }
        { format.title output.nonnull }
      if$
      blank.sep
    }
  if$
  howpublished output
  format.date output
  new.block
  note output
  fin.entry
  empty.misc.check
}

FUNCTION {phdthesis}
{ output.bibitem
  format.authors "author" output.check
  format.title "title" output.check
  blank.sep
  "PhD thesis" format.thesis.type output.nonnull
  school "school" output.check
  address output
  format.date "year" output.check
  new.block
  format.eprint output
  new.block
  note output
  format.SLACcitation output
  fin.entry
}

FUNCTION {proceedings}
{ output.bibitem
  editor empty$
    { organization output }
    { format.editors output.nonnull }
  if$
  format.btitle "title" output.check
  format.bvolume output
  format.number.series output
  editor empty$
    'skip$
    { organization output }
  if$
  new.block
  publisher output
  address output
  format.date "year" output.check
  new.block
  note output
  format.SLACcitation output
  fin.entry
}

FUNCTION {techreport}
{ output.bibitem
  format.collaboration output
  format.authors "author" output.check
  format.title "title" output.check
  blank.sep
  format.tr.number output.nonnull
  institution "institution" output.check
  address output
  format.date "year" output.check
  new.block
  note output
  format.SLACcitation output
  fin.entry
}

FUNCTION {unpublished}
{ output.bibitem
  format.collaboration output
  format.authors "author" output.check
  format.title output.nonnull
  blank.sep
  note "note" output.check
  format.date "year" output.check
  "unpublished." output.nonnull
  fin.entry
}

FUNCTION {inpreparation}
{ output.bibitem
  format.collaboration output
  format.authors "author" output.check
  format.title   "title" output.check
  blank.sep
  "in preparation." output.nonnull
  fin.entry
}

FUNCTION {default.type} { misc }



%---------------------------------------------------------------
% Start processing
%---------------------------------------------------------------


READ

FUNCTION {sortify}
{ purify$
  "l" change.case$
}

INTEGERS { len }

FUNCTION {chop.word}
{ 's :=
  'len :=
  s #1 len substring$ =
    { s len #1 + global.max$ substring$ }
    's
  if$
}

FUNCTION {format.lab.names}
{ 's :=
  s #1 "{vv~}{ll}" format.name$
  s num.names$ duplicate$
  #2 >
    { pop$ " et~al." * }
    { #2 <
        'skip$
        { s #2 "{ff }{vv }{ll}{ jj}" format.name$ "others" =
            { " et~al." * }
            { " and " * s #2 "{vv~}{ll}" format.name$ * }
          if$
        }
      if$
    }
  if$
}

FUNCTION {author.key.label}
{ author empty$
    { key empty$
        { cite$ #1 #3 substring$ }
        { key #3 text.prefix$ }
      if$
    }
    { author format.lab.names }
  if$
}

FUNCTION {author.editor.key.label}
{ author empty$
    { editor empty$
        { key empty$
            { cite$ #1 #3 substring$ }
            { key #3 text.prefix$ }
          if$
        }
        { editor format.lab.names }
      if$
    }
    { author format.lab.names }
  if$
}

FUNCTION {author.key.organization.label}
{ author empty$
    { key empty$
        { organization empty$
            { cite$ #1 #3 substring$ }
            { "The " #4 organization chop.word #3 text.prefix$ }
          if$
        }
        { key #3 text.prefix$ }
      if$
    }
    { author format.lab.names }
  if$
}

FUNCTION {editor.key.organization.label}
{ editor empty$
    { key empty$
        { organization empty$
            { cite$ #1 #3 substring$ }
            { "The " #4 organization chop.word #3 text.prefix$ }
          if$
        }
        { key #3 text.prefix$ }
      if$
    }
    { editor format.lab.names }
  if$
}

FUNCTION {calc.short.authors}
{ type$ "book" =
  type$ "inbook" =
  or
    'author.editor.key.label
    { type$ "proceedings" =
        'editor.key.organization.label
        { type$ "manual" =
            'author.key.organization.label
            'author.key.label
          if$
        }
      if$
    }
  if$
  'short.list :=
}

FUNCTION {calc.label}
{ calc.short.authors
  short.list
  "("
  *
  year duplicate$ empty$
     { pop$ "????" }
     'skip$
  if$
  *
  'label :=
}


%---------------------------------------------------------------
% Sorting
%---------------------------------------------------------------

FUNCTION {sort.format.names}
{ 's :=
  #1 'nameptr :=
  ""
  s num.names$ 'numnames :=
  numnames 'namesleft :=
    { namesleft #0 > }
    { nameptr #1 >
        { "   " * }
        'skip$
      if$
      s nameptr "{vv{ } }{ll{ }}{  ff{ }}{  jj{ }}" format.name$ 't :=
      nameptr numnames = t "others" = and
        { "et~al" * }
        { t sortify * }
      if$
      nameptr #1 + 'nameptr :=
      namesleft #1 - 'namesleft :=
    }
  while$
}

FUNCTION {sort.format.title}
{ 't :=
  "A " #2
    "An " #3
      "The " #4 t chop.word
    chop.word
  chop.word
  sortify
  #1 global.max$ substring$
}

FUNCTION {author.sort}
{ author empty$
    { key empty$
        { "to sort, need author or key in " cite$ * warning$
          ""
        }
        { key sortify }
      if$
    }
    { author sort.format.names }
  if$
}

FUNCTION {author.editor.sort}
{ author empty$
    { editor empty$
        { key empty$
            { "to sort, need author, editor, or key in " cite$ * warning$
              ""
            }
            { key sortify }
          if$
        }
        { editor sort.format.names }
      if$
    }
    { author sort.format.names }
  if$
}

FUNCTION {author.organization.sort}
{ author empty$
    { organization empty$
        { key empty$
            { "to sort, need author, organization, or key in " cite$ * warning$
              ""
            }
            { key sortify }
          if$
        }
        { "The " #4 organization chop.word sortify }
      if$
    }
    { author sort.format.names }
  if$
}

FUNCTION {editor.organization.sort}
{ editor empty$
    { organization empty$
        { key empty$
            { "to sort, need editor, organization, or key in " cite$ * warning$
              ""
            }
            { key sortify }
          if$
        }
        { "The " #4 organization chop.word sortify }
      if$
    }
    { editor sort.format.names }
  if$
}

INTEGERS { seq.num }

FUNCTION {init.seq}
{ #0 'seq.num :=}

EXECUTE {init.seq}

FUNCTION {int.to.fix}
{ "000000000" swap$ int.to.str$ *
  #-1 #10 substring$
}

FUNCTION {presort}
{ calc.label
  label sortify
  "    "
  *
  seq.num #1 + 'seq.num :=
  seq.num  int.to.fix
  'sort.label :=
  sort.label *
  #1 entry.max$ substring$
  'sort.key$ :=
}

ITERATE {presort}

STRINGS { longest.label last.label next.extra }

INTEGERS { longest.label.width last.extra.num number.label }

FUNCTION {initialize.longest.label}
{ "" 'longest.label :=
  #0 int.to.chr$ 'last.label :=
  "" 'next.extra :=
  #0 'longest.label.width :=
  #0 'last.extra.num :=
  #0 'number.label :=
}

FUNCTION {forward.pass}
{ last.label label =
    { last.extra.num #1 + 'last.extra.num :=
      last.extra.num int.to.chr$ 'extra.label :=
    }
    { "a" chr.to.int$ 'last.extra.num :=
      "" 'extra.label :=
      label 'last.label :=
    }
  if$
  number.label #1 + 'number.label :=
}

FUNCTION {reverse.pass}
{ next.extra "b" =
    { "a" 'extra.label := }
    'skip$
  if$
  extra.label 'next.extra :=
  extra.label
  duplicate$ empty$
    'skip$
    { "{\natexlab{" swap$ * "}}" * }
  if$
  'extra.label :=
  label extra.label * 'label :=
}


FUNCTION {longest.label.pass}
{ number.label int.to.str$ 'label :=
  number.label #1 + 'number.label :=
  label width$ longest.label.width >
    { label 'longest.label :=
      label width$ 'longest.label.width :=
    }
    'skip$
  if$
}

EXECUTE {initialize.longest.label}

ITERATE {forward.pass}

REVERSE {reverse.pass}

FUNCTION {bib.sort.order}
{ sort.label  'sort.key$ :=
}

ITERATE {bib.sort.order}

SORT

FUNCTION {begin.bib}
{   preamble$ empty$
    'skip$
    { preamble$ write$ newline$ }
  if$
  "\begingroup\raggedright\begin{thebibliography}{" number.label int.to.str$ * "}" *
  write$ newline$
  "\expandafter\ifx\csname natexlab\endcsname\relax\def\natexlab#1{#1}\fi"
  write$ newline$
}


EXECUTE {begin.bib}

EXECUTE {init.state.consts}

ITERATE {call.type$}

FUNCTION {end.bib}
{ newline$
  "\end{thebibliography}\endgroup" write$ newline$
}

EXECUTE {end.bib}
