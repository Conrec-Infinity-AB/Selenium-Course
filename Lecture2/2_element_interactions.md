# Elemets
When we have found an element in the web page we have some commands to use for interacting with the element

Clicks on the element if its clickable. Usually buttons, links, text fields and more
> element.click()

Sends some text to an input field like text boxes
> element.sendKeys("Some text") 

It's possible to clear texts in input fields
> element.clear()

## Get text and info for an element
Get the text of the element
> element.text

Get the tag name of the element a selected element
> element.tag_name

Returns height, width, x and y coordinates
> element.text.rect

### Attributes and Properties
An attribute is a static attribute for an element while a property is a computed property. 

An example of a property would be the checked state of a checkbox, or value or an input field. As where an attribute would be href of an anchor tag.

Get the value of a CSS property for an element. An example could be type = checkbox or href  
> element.getAttribute("type")

Get the property of an element. 
> element.getproperty("property_name")

An example could be we have a link with several class properties 
```
<a class="nav-link dropdown-toggle">  href="index.html">...</a>  

element.getproperty("class") 
```
Outputs: nav-link dropdown-toggle

Get the value of a CSS property for an element 
> element.value_of_css_property("background-color")

## Check state of an element
Get the enabled status of an element. If an element is disabled then we can not interact with it
> element.isEnabled()

Check if the element is displayed in the viewable browser context. If the element is outside the viewable area we need to scroll into the view first.  
> element.isDisplayed()

Check if the element is selected or not. Uually for Check boxes, radio buttons, input elements, and option elements.
> element.isSelected()