# Selenium #

## Browsers ##
> driver.get("URL")
> driver.navigate.to("") -- Kolla java kod
> driver.current_url
> driver.title

> driver.set_page_load_timeout() 

> driver.manage()
> driver.back()
> driver.forward()
> driver.refresh()
> driver.page_source

> driver.get_attribute("attributename")

## Elements ##
> element.clear()
> element.click()
> element.sendKeys("")
> element.submit()
> element.getAttribute("type")
> element.getproperty()
> element.value_of_css_property('background-color')
> element.text
> element.isEnabled()
> element.isDisplayed()
> element.isSelected()


## Screenshots ##
Returns and base64 encoded string into image
element.screenshot('./image.png')  

## Cookies ##
driver.get_cookies()
driver.add_cookie({'name': 'CookieName', 'value': 'CookieValue'}) -- use dictionary with name and value

## Find elements ##
findElement() returns a WebElement object based on a specified search criteria or ends up throwing an exception if it does not find any element matching the search criteria.
findElements() returns a list of WebElements matching the search criteria. If no elements are found, it returns an empty list.

## Elements with multiple attributes ##
> driver.find_element(By.CSS_SELECTOR, "button[title='Subscribe'][type='submit']")

## Chaining locators together ##

## Relative CSS Selector ##
Relative CSS Selectors are used to select elements based on their relationship with other elements or attributes on the page. These selectors provide a way to select elements that match a certain pattern or attribute value. Relative CSS Selectors include attribute selectors with special characters that starts with ^, ends with $, and contain * & ~. These selectors allow you to target elements that have specific attribute values or patterns, as given:
^ Selects elements that have an attribute value that starts with a specific string. Example select all input elements that have a name attribute starting with the string "username"
> input[name^="username"]
~ Selects elements that have an attribute value that contains a specific string. Example select all all div elements that have a class attribute containing the word "example"
> div[class~="example"] 

$ Selects elements that have an attribute value that ends with a specific string. Example select all elements that have an href attribute ending with the string ".pdf"
> a[href$=".pdf"]

* Selects elements that have an attribute value that contains a specific substring. Example select all img 
elements that have an alt attribute containing the text button 
> img[alt*="button"]

Locating Child Elements(Direct Child):
Syntax: parentLocator>childLocator
> div#buttonDiv>button
Explanation: ‘div#buttonDiv>button’ will first go to div element with id ‘buttonDiv’ and then select its child
element – ‘button’

Locating elements inside other elements (child or sub-child): Syntax: parentLocator>locator1 locator2
CSS Locator: div#buttonDiv button
Explanation: ‘div#buttonDiv button’ will first go to div element with id ‘buttonDiv’ and then select ‘button’
element inside it (which may be its child or sub child)
Locating nth Child:
To locate the element with text ‘QTP’, we have to use “nth-of-type”
css="ul#automation li:nth-of-type(2)"
Similarly, To select the last child element, i.e. ‘Sikuli’, we can use
css="ul#automation li:last-child"

## Executing Javascript ##
> driver.excecute_script('Javascript code')
> driver.excecute_script('window.open();')

## Element interactions ##
## ActionChains ##
Used to chain user actions/input together, like moving or clikcing the mouse, pressing keys, drag n drop ...

Need to import the ActionChains classes
> from selenium.webdriver.common.action_chains import ActionChains
Instantiate the new action chain object to use
> action = ActionChains(driver) 

Perform some actions. We need to run perform for every action to execute them
> action.context_click(element).perform() / action.context_click(on_element=element).perform() 

> action.click_and_hold(element).perform()
> action.release().perform()

Pause between actions
> clickable = driver.find_element(By.ID, "clickable")
>    ActionChains(driver)
>        .move_to_element(clickable)
>        .pause(1)
>        .click_and_hold()
>        .pause(1)
>        .send_keys("abc")
>        .perform()

An important thing to note is that the driver remembers the state of all the input items throughout a session. Even if you create a new instance of an actions class, the depressed keys and the location of the pointer will be in whatever state a previously performed action left them.

There is a special method to release all currently depressed keys and pointer buttons. This method is implemented differently in each of the languages because it does not get executed with the perform method.

> ActionBuilder(driver).clear_actions()

## Buttons ##
> button = driver.find_element(By.CSS_SELECTOR, 'button#id')
> button.click()

## Input elements ##
> input_field = driver.find_element(By_ID, '#id')
> input_field.clear()
> input_field.send_keys('text')

## Radio buttons and checkboxes ##
Radio buttons can only be clicked once, so need to click another radio button to unselect it. WHile Checkboxes can be toggled by clicking a checkbox several times

> radio_buttons = driver.find_elements()
> check_boxes = driver.find_elements()
> radio_buttons[0].isSelected()
> radio_buttons[0].click()
> radio_buttons[1].click()
> radio_buttons[1].getAttribute('value')
> radio_buttons[1].text -- fungerar?

> check_boxes[1].isSelected()
> check_boxes[1].click()
> check_boxes[1].click()

## Dropdown menus ##
Dropdowns are using <select/> and <option/> tags.
Several values can be selected

> from selenium.webdriver.support.ui import Select
> select_element = driver.find_element(By.id, '#id')
> select = select(select_element)

> select.select_by_index(2)
> select_by_value('value1')
> select.select_by_visible_text('Google')
> select.deselect_by_index(2) 
> select.deselect_by_value('Bing')
> select.deselect_all() -- Only for multiselects

Disabled values cannot be selected
>  with pytest.raises(NotImplementedError):
>        select.select_by_value('disabled')

> option_elements = find_elements(By.TAGNAME, 'option')
> option_elements[1].click() 
> option_elements[-1].click() -- sista valet 

Kan använda Seleniums select.options för att få texterna eller valda element
> print([option.text for option in select.options])
> selected_option_list = select.all_selected_options



## Sliders ##

> slider_element.click()
> action = ActionChains(driver)
> actions.move_to_element_with_offset(slider_element, x, y).click().perform()
> actions.move_to_element_with_offset(slider_element, 50, 0).click().perform()
> actions.move_to_element_with_offset(slider_element, -50, 0).click().perform()

> actions.drag_and_drop_by_offset(slider_element, x, y).perform()
> actions.drag_and_drop_by_offset(slider_element, 100, 0).perform()

## Mouse / Key events ##
Keys
https://github.com/SeleniumHQ/selenium/blob/selenium-4.2.0/py/selenium/webdriver/common/keys.py#L23

.key_down()
.key_up()
.send_keys()
.send_keys_to_element(text_input, "abc")

> from selenium.webdriver.common.keys import Keys
> ActionChains(driver)
>        .key_down(Keys.SHIFT)
>        .send_keys("abc")
>        .perform()

> action = ActionChains(driver)
> element.send_keys('Text to enter')
> action.key_down(Keys.CONTROL).send_keys('d').release().perform()
> action.key_down(Keys.CONTROL).send_keys('d').key_up(Keys.CONTROL).perform()
> action.send_keys(Keys.ESCAPE).perform()

Mouse
Click and hold 
This method combines moving the mouse to the center of an element with pressing the left mouse button. This is useful for focusing a specific element
> action.click_and_hold(clickable_element).perform

Click and release
This method combines moving to the center of an element with pressing and releasing the left mouse button
> action.click(clickable_element).perform()

Doubleclick
> action.double_click(clickable_element).perform()

Move to element
This method moves is known as “hovering.” Note that the element must be in the viewport or else the command will error.
> action.move_to_element(hoverable_element).perform()

Drag and Drop on Element
This method firstly performs a click-and-hold on the source element, moves to the location of the target element and then releases the mouse
> action.drag_and_drop(draggable_elemebt, droppable_element).perform()

## Scroll to element ##
