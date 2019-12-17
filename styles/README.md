# Style options for markdown pages

Use the following css snippets inline on your markdown pages below your page header but above the content you want to style. To clear a float use a single ``#`` (an empty header) on its own line.


## Images
Add more style options for your images.

### Example:
[Governance Model](../about/governance)

### Syntax
Note that more than one class can be applied to an image.

- make an image 100% width of content area :
```
![Alt tag here](images/image_name.jpg){.mkd-img-full}
```
- make an image 60% width of content area (100% on mobile) and center it:
```
![Alt tag here](images/image_name.jpg){.mkd-img-60}
```
- make a small thumbnail image:
```
![Alt tag here](images/image_name.jpg){.mkd-img-thumb}
```
- add a grey border:
```
![Alt tag here](images/image_name.jpg){.mkd-img-border}
```
- float an image left and make it 50% width:
```
![Alt tag here](images/image_name.jpg){.mkd-img-left}
```
- float an image right and make it 50% width:
```
![Alt tag here](images/image_name.jpg){.mkd-img-right}
```
- place two images side by side, each 50% width of content area (will stack at 100% width on mobile), with borders:
```
![Alt tag here](images/image_name.jpg){.mkd-img-left .mkd-img-border}
![Alt tag here](images/image_name.jpg){.mkd-img-left .mkd-img-border}
```

### CSS
```
<style>
.mkd-img-border {
  margin:1em 0px;
  padding:10px;
  border:.25em solid #ededed;
}
.mkd-horz-spacing {
  margin-right:1em;
  margin-left:1em;
}
.mkd-img-left {
  float:left;
  width:100%;
  margin-top:0;
}
.mkd-img-right {
  float:right;
  width:100%;
  margin-top:0;
}
.mkd-img-full {
  width:100% !important;
}
.mkd-img-60 {
  width:100% !important;
  margin:0 auto;
  display:block;
}
.mkd-img-thumb {
  max-width:250px !important;
}
.mkd-img-icon {
  border-radius:25%;
  width:150px;
  float:left;
  margin:0 .5em;
}
@media (min-width: 576px) {
  .mkd-img-left {
    width:calc(50% - 1.25em);
    margin-right:1em;
  }
  .mkd-img-right {
    width:calc(50% - 1.25em);
    margin-left:1em;
  }
  .mkd-img-60 {
    width:60% !important;
    margin:0 auto;
    display:block;
  }
}
</style>
```

## Ordered Lists
The following styles will be automatically applied to any ordered lists, or ordered lists within a blockquote, on your page. A normal ordered list will produce a condensed list of items separated horizontally by some padding and a red bullet. Enclosing the ordered list within a blockquote will produce a 2-column list of bordered items with box shadows. Stacks to a single column on mobile.

### Example:
[Our Members](../about/ourmembers)

### Syntax
#### ordered list:
```
1. item goes here
1. another item here
1. final list item
```
#### ordered list within a blockquote:
```
> 1. item goes here
> 1. another item here
> 1. final list item
```

### CSS
#### ordered list
```
<style>
ol {
  list-style:none;
  margin-left:0 !important;
  margin:0;
  padding:0;
}
ol li {
  display: inline;
}
ol li::after {
  content: " \2022 ";
  margin: 0 .15em 0 .45em;
  color: #b31b1b;
  font-weight: 900;
}
ol li:last-child::after {
  content: "";
  margin: 0;
}
h2, h2, h4, h5 {
  clear:both;
}
aside {
  float:left; clear:both; width:100%;
}
</style>
```

#### ordered list within a blockquote
```
<style>
blockquote {
  border-left:0;
  margin:0;
  padding:0;
}
blockquote ol {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-between;
  align-items: center;
}
blockquote ol li {
  width: 100%;
  padding:1em;
  -webkit-box-shadow: 0px 3px 8px 0px rgba(0,0,0,0.1);
  -moz-box-shadow: 0px 3px 8px 0px rgba(0,0,0,0.1);
  box-shadow: 0px 3px 8px 0px rgba(0,0,0,0.1);
  min-height:90px;
  display: flex;
  align-items: center;
  justify-content: center;
}
blockquote ol li img {
  height:40px;
  display:block;
  margin:1em auto 0 auto;
}
@media (min-width: 576px) {
  blockquote ol li {
    width: calc(50% - 10px);
  }
}
h2, h2, h4, h5 {
  clear:both;
}
aside {
  float:left;
  clear:both;
  width:100%;
}
</style>
```

## Unordered Lists within a Blockquote
The following styles will be automatically applied to any unordered lists within a blockquote on your page. They will reproduce a 'card' style layout with 4 cards in a row on desktop, 2 in a row on tablet, and a single stack on mobile.

### Example:
[Scientific Advisory Board](../about/people/scientific_ad_board)

### Syntax
```
> - First item
> - This is a second item
> - Third item here
```

### CSS
```
<style>
blockquote {
  border-left:0;
  margin:0;
  padding:0;
}
blockquote ul {
  list-style: none;
  margin: 0;
  padding: 0;
  display: flex;
  flex-direction: row;
  flex-wrap: wrap;
  justify-content: space-between;
}
blockquote ul li {
  width: 100%;
  padding:1em;
  margin:1%;
  -webkit-box-shadow: 0 10px 25px -10px rgba(0,0,0,0.25);
  -moz-box-shadow: 0 10px 25px -10px rgba(0,0,0,0.25);
  box-shadow: 0 10px 25px -10px rgba(0,0,0,0.25);
}
blockquote ul li img {
  height:40px;
  display:block;
  margin:1em auto 0 auto;
}
@media (min-width: 576px) {
  blockquote ul li {
    width: 48%;
  }
}
@media (min-width: 986px) {
  blockquote ul li {
    width: 23%;
  }
}
</style>
```

## Blockquotes
Use the following styles to add a subtle box-shadow around some content.

### Example:
[Accessibility at arXiv](../about/accessibility)

### Syntax
```
> This content will appear in a blockquote.
> So will this line. Be sure to add a carrot to each line in a blockquote even...
>
> ... blank lines.
```

### CSS
```
<style>
blockquote {
  border-left: 0;
  -webkit-box-shadow: 0px 3px 8px 0px rgba(0,0,0,0.12);
  -moz-box-shadow: 0px 3px 8px 0px rgba(0,0,0,0.12);
  box-shadow: 0px 3px 8px 0px rgba(0,0,0,0.12);
  padding:1em;
  margin-bottom:1.5em;
}
@media (min-width: 576px) {
  blockquote {
    padding: 2em;
  }
}
</style>
```
