## INTRODUCTION

- HTML is the standard markup language for creating Web pages.
- HTML stands for Hyper Text Markup Language
```
    The <!DOCTYPE html> declaration defines that this document is an HTML5 document
    The <html> element is the root element of an HTML page
    The <head> element contains meta information about the HTML page
    The <title> element specifies a title for the HTML page (which is shown in the browser's title bar or in the page's tab)
    The <body> element defines the document's body, and is a container for all the visible contents, such as headings,paragraphs, images, hyperlinks, tables, lists, etc.
    The <h1> element defines a large heading
    The <p> element defines a paragraph
```
## ELEMENTS

- The <!DOCTYPE> declaration is not case sensitive.

- HTML headings are defined with the ```<h1>``` to ```<h6>``` tags.

```<h1>``` defines the most important heading. ```<h6>``` defines the least important heading

HTML links are defined with the ```<a>``` tag:
```
 <a href="https://www.w3schools.com">This is a link</a> 
```

HTML images are defined with the <img> tag.
  <img src="w3schools.jpg" alt="W3Schools.com" width="104" height="142"> 

Some HTML elements will display correctly, even if you forget the end tag:

<html>
<body>

<p>This is a paragraph
<p>This is a paragraph

</body>
</html> 

HTML elements with no content are called empty elements.

The <br> tag defines a line break, and is an empty element without a closing tag:
 <p>This is a <br> paragraph with a line break.</p> 

HTML is Not Case Sensitive

HTML tags are not case sensitive: <P> means the same as <p>.

The HTML standard does not require lowercase tags, but W3C recommends lowercase in HTML, and demands lowercase for stricter document types like XHTML.

## ATTRIBUTES

HTML Attributes

    All HTML elements can have attributes
    Attributes provide additional information about elements
    Attributes are always specified in the start tag
    Attributes usually come in name/value pairs like: name="value"

You should always include the lang attribute inside the <html> tag, to declare the language of the Web page. This is meant to assist search engines and browsers.

The following example specifies English as the language:
<!DOCTYPE html>
<html lang="en">
<body>
...
</body>
</html>

Country codes can also be added to the language code in the lang attribute. So, the first two characters define the language of the HTML page, and the last two characters define the country.

The following example specifies English as the language and United States as the country:
<!DOCTYPE html>
<html lang="en-US">
<body>
...
</body>
</html>

The title attribute defines some extra information about an element.

The value of the title attribute will be displayed as a tooltip when you mouse over the element:
 <p title="I'm a tooltip">This is a paragraph.</p> 

The title attribute (and all other attributes) can be written with uppercase or lowercase like title or TITLE.

Double quotes around attribute values are the most common in HTML, but single quotes can also be used.

In some situations, when the attribute value itself contains double quotes, it is necessary to use single quotes:

## HEADINGS

Search engines use the headings to index the structure and content of your web pages.

Users often skim a page by its headings. It is important to use headings to show the document structure.

<h1> headings should be used for main headings, followed by <h2> headings, then the less important <h3>, and so on.

## PARAGRAPH 

With HTML, you cannot change the display by adding extra spaces or extra lines in your HTML code.

The browser will automatically remove any extra spaces and lines when the page is displayed:

The <hr> tag defines a thematic break in an HTML page, and is most often displayed as a horizontal rule.

The <hr> element is used to separate content (or define a change) in an HTML page:

The <hr> tag is an empty tag, which means that it has no end tag.

Use <br> if you want a line break (a new line) without starting a new paragraph:

The HTML <pre> element defines preformatted text.

The text inside a <pre> element is displayed in a fixed-width font (usually Courier), and it preserves both spaces and line breaks:

## STYLE ATTRBUTE 
Setting the style of an HTML element, can be done with the style attribute.

The HTML style attribute has the following syntax:

<tagname style="property:value;">
The property is a CSS property. The value is a CSS value.

- background-color: property defines the background color for an HTML element.
- color: property defines the text color for an HTML element.
- font-family: property defines the font to be used for an HTML element.
- font-size: property defines the text size for an HTML element.
- text-align: property defines the horizontal text alignment for an HTML element.
