# DOM Tree - (Document Object Model) #

## Definition from Wikipedia ##

A Document Object Model (DOM) tree is a hierarchical representation of an HTML or XML document. It consists of a root node, which is the document itself, and a series of child nodes that represent the elements, attributes, and text content of the document. Each node in the tree has a parent node, except for the root node, and can have multiple child nodes.

Elements in an HTML or XML document are represented as nodes in the DOM tree. Each element node has a tag name, attributes, and can contain other element nodes or text nodes as children. For example below we have an simple HTML document with the following structure:

    <html>
      <head>
        <title>My Website</title>
      </head>
      <body>
        <h1>Welcome</h1>
        <p>This is my website.</p>
        <a href="https://example.com">Link</a>
      </body>
    </html>


In this example the root node is the document object and the most parent node is the \<html> element, and everything below it are child elements. At the same time the \<h1>, \<p> and \<a> elements has \<body> element as their parent.

    - Document (root)
      - html
        - head
          - title
            - "My Website"
        - body
          - h1
            - "Welcome"
          - p
            - "This is my website."
          - a
            - href: "https://example.com"
            - "Link"

Text content within an element is represented as a text node in the DOM tree. Text nodes do not have attributes or child nodes
In the DOM tree the "Welcome", "This is my website." and "Link" are text nodes.

And finally the attributes of an element are represented as properties of the element node in the DOM tree. Here the href is an attribute with the property href: "https://example.com".

### document object ###
The web page being shown in the browser is represented by the document object. It offers methods and attributes that let us interact with various website elements and content. With the document object it is possible edit the content, change the web page's structure and other operations on DOM elements.

### window object ###
In all web pages there is actually another level above the document level which is called the windows object.

The open browser window or tab is represented by the window object in Selenium WebDriver. With it it's possible modify the browser's attributes and behavior. For example manage window resizing, switch between various browser, tabs and pages and more.

The window object can be used to carry out typical tasks like maximizing or minimizing the browser window, scaling it to a certain size, scrolling it to a certain location, opening new tabs or windows, and moving between tabs or windows.

## Understanding the DOM tree ##
Having an understanding of the structure of the DOM tree is important in Selenium. We use it to navigate through the different node levels to find elements and also to modify values in the windows and document objects. 

Also it helps us when we debug our test code when using Google dev tools.

