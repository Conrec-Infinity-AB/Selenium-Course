# Selenium Locators #
Selenium locators helps identifying web elements within the tested web page. Every Selenium locator command provides Selenium information about the type of element it looks for, like text, button, checkbox and so on.  

## Different types of locators in Selenium ##
Web elements can be uniquely located by one of the Selenium locators below. Selenium provides a "By" class, to locate elements in the DOM.

### Locating Element using ID ###
Locates elements matching search value with the id attribute of the object.

Finding an element using the "id" attribute of an object. ID Locator is mostly reliable, safe, and less likely to be impacted by a change. It is more preferred compared to other locators. If multiple elements with the same IDs is found, then the first matched ID is returned.
 
Example Selenium code:
    driver.find_element(By.ID, 'send').click()

### Locating Element using Class Name ###
Locates elements matching the search value with the object's class attribute.

Finding an element using the "class" attribute. Often a class name is common across different elements in a web page and using the class name attribute can then be unreliable. If we use the class name to locate the element and multiple elements are returned, then Selenium will do the action on the first element. The class name locator is usually very useful when trying to find multiple web elements in the web page.

Example Selenium code:  
>driver.find_element(By.CLASS_NAME, 'primary').click()

### Locating Element using Name Attribute ###
Locates elements matching search value with the Name attribute of the object.

Finding an element using the "name" attribute of the object. The name attribute may or may not be unique for an element.
The name attribute is usually added to the input text field or button. An example could be a Login name input field loginName[username] and the password input field name is loginPassword[password]. Which is unique for the input username and password text fields.

Example Selenium code:  
>driver.find_element(By.NAME, 'login[userName]').send_keys("user1")

### Locating Element using Link Text ###
Locates elements matching search value with the anchor tag "a" and the link text.

Elements with the anchor tag \<a> are link elements. The element in the anchor tag will have a href attribute with a link to a page.

The Link Text locator locates the element by exactly matching the link text available on the web page. The Link text is case-sensitive.

Example Selenium code:  
>driver.find_element(By.LINK_TEXT, 'Forgot your password').click()

### Locating Element using Partial Link Text ###
Locates elements matching search value with the anchor tag "a" and partially matches the text.

Locating elements using Partial Link Text similar to Link text locator. However partial link text matches the link element partial text. We can pass the substring from the text in the anchor tag in the web page. The partial link text is also case-sensitive.

Example Selenium code:  
>driver.find_element(By.PARTIAL_LINK_TEXT, 'Forgot').click()

### Locating Element using Tag Name ###
Locates elements matching the search value with the tag name.

Web element tags are different for different elements. If the tag name is unique for a given element, it can be used to identify the element. The tag name locator is also used to find multiple web elements in the web page. 

Example Selenium code:  
>driver.find_element(By.TAG_NAME, 'body').get_attribute('class')

### Locating Element using CSS Selector ###
Locates elements matching the search value with CSS selector.

CSS stands for Cascading Style Sheets. It is the component that makes HTML pages more attractive and organized. 

CSS Selector can be used to find complex elements on the web page. CSS is more flexible with locating web elements and more reliable, as it can be constructed by combining element attributes.

**ID:** 
CSS Selector with the id attribute uses the "#" symbol is used between tag Name and ID, the tag Name is optional and can be used to locate an element with "#" followed by id.

The Syntax for CSS Selector with ID is: tagName#Id" or "#Id" or tagName[id='idValue']

Example Selenium code:  
>driver.find_element(By.CSS_SELECTOR, '#email').send_keys('User2')

**CLASS:** 
CSS Selector with a class attribute. The "." symbol is used for identifying elements with CSS selector using class.

The Syntax for CSS Selector with Class is: tagName.class" or " className" or tagName[class='classValue']

Example Selenium code, all below do the same thing:  
>driver.find_element(By.CSS_SELECTOR, '.input-text').send_keys('password')  
>driver.find_element(By.CSS_SELECTOR, 'input[class="input-text"]').send_keys('password')  
>driver.find_element(By.CSS_SELECTOR, 'input.input-text').send_keys('password')

### Locating Element using XPath Locator ###
Locates elements using a XPath expression.

XPath defines a XML path. XML path expressions is used to locate nodes via elements and attributes in the HTML DOM structure. XPath is an address of the element. 

Using XPath can be very useful especially when an element has no attributes assigned to it. Then it becomes very difficult to locate such elements in another way.

XPath can be of two types to locate web elements either an absolute XPath or a relative XPath.

**Absolute XPath**
An absolute XPath is a method in which elements are located navigating from the root node, \<html> in a hierarchical order. The nodes is indicated by a "/". 

The absolute XPath for an element can be copied in the browsers Inspect Element tool by using Copy full XPath.
Following is an example of absolute Path. This is not reliable as it is more prone to failure even if a minor change occurs on the web page.

>/html/body/form/div[1]/input

**Relative XPath**
The web elements are located by referring to the elements that need to be identified and not from the root node. This makes relative XPaths less prone to failures in case of changes. 
The relative XPath for an element can be copied in the browsers Inspect Element tool by using Copy XPath. 

Relative XPaths uses the // to define the current node or tag in HTML to start from. 

Example of the relative XPath 

>//input[@id="email"]

## Challenges ##
Finding an element uniquely can sometimes be challenging. Usage of Selenium locators also requires a strategy to ensure that the tests are stable, fast and reliable.

As an example on a page there can be a link with a name link text that appears 5 times and our Selenium code should click on the third link. If the web page then is modified and the same link text is added one more time in the second position then the click is using the wrong link text and the test will fail. So it is important to find the element uniquely.
