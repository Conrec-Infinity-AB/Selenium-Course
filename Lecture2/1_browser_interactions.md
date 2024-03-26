# Browser interactions #

## Browsers navigation ##
Go to an URL in the browser opened for the WebDriver session 
> driver.get("URL")

Get the active browser tab / window URL
> driver.current_url

Get the active browser tab / window title
> driver.title

Sets the amount of time to wait for a page load to complete before throwing an error. Default value is 300 seconds.
> driver.set_page_load_timeout(30) 

If you have followed one or more links in the current tab or browser, then its possible to navigate back  
> driver.back()

The same applies if you have navigated back and want to go forward again
> driver.forward()

If we need to refresh the current page we can do that too
> driver.refresh()

It is possible to save the current page rendered HTML to an object or file, just save the output to an variable and then use it in the code.  
> driver.page_source

## Browser window sizes ##

Maximaize the browser window 
> driver.maximize_window()

Minimize the window
> driver.minimize_window()

Set window to full screen
> driver.fullscreen_window()

Get the window dimension
> size = driver.get_window_size()

> width = driver.get_window_size().get("width")

> height = driver.get_window_size().get("height")

Set the browser window size. Note it does not change the screen resolution
> driver.set_window_size(1024, 768)

Get window positions (x, y values)
> position = driver.get_window_position()

> xPos = driver.get_window_position().get('x')

> yPos = driver.get_window_position().get('y')

Move the window to a specific position on the primary monitor
> driver.set_window_position(x, y)

## Screenshots ##
Its possible to take screenshots of the browser, both the full browser window but also on individual elements

Take a browser screenshot. The fuction saves the screenshot as an .PNG file
> driver.save_screenshot('/path/browser_screenshot.png')

And on a specific element which is visible
> element.screenshot('/path/element_screenshot.png')  

## Cookies ##
Get all cookies used on the tested page. Returns an dictionary with names and values
> driver.get_cookies()

Print the cookies
> for cookie in driver.get_cookies():  
>       print(cookie)

Add a cookie by giving it a name and a dictionaty of name and key values 
> driver.add_cookie({'name': 'CookieName', 'value': 'CookieValue'})

## Executing Javascript ##
It is possible to interact with the browser with Javascript and also modify the DOM tree if needed

For example to open a new window with Javascript
> driver.execute_script('window.open();')

## Alerts ##
These are standard browser alerts and there are three different ones we can use in HTML. We have to run Javascript to show them. 

First we have the standard alert which just informs us about something. There are only one button to click and thats the Close button. HTML code:
> \<input type="button" onClick="alert('An alert')"\>

The second one is for asking questions where you can respond with Cancel or OK.
> \<input type="button" onClick="confirm('An alert with Cancel & OK buttons')"\>

The third one is used when we need the user to enter som repsone text. It also uses Cancel and OK buttons.
> \<input type="button" onClick="prompt('An alert with inputbox and Cancel & OK buttons','Pre-filled text')"\>

### Note ###
Many times developers builds their own alerts by using popup windows/modals, then these alert commands does not work. Instead we have to handle the popup as a web page and find the buttons and field to interact with.

To interact with an alert we first need to switch to its context or we will not be able to interact with the alert.
> alert = driver.switch_to.alert

If we import below then we can use Alert(driver) instead of driver.switch_to.alert
> from selenium.webdriver.common.alert import Alert
> alert = Alert(driver)

To interact with the alert we can use either to click the OK button
>alert.accept()

Or click the Cancel button
alert.dismiss()

And we can get the text which is visible in the alerts. It will not get the text from the input fields in prompts. You will need to use some HTML/Javascript code in the page your testing. See example code i this lecture 2 
> alert.text

And to enter some inputs in a prompt we use the .sendKeys() method. Note The text in the input field does not seem to update eventhough it does when you click OK.
> alert.sendKeys("The text to enter in a prompt")

## IFrames ##
Page Navigation
Frames or iFrames loads other HTML pages inside a web page.  
Elements inside an iFrame can't be selected directly with Selenium, instead, you have to switch from the main HTML into the iframe.

Same problem in reverse - the main HTML is not accessible within the iFrame

So we need to do some steps to find an element in an iFrame: 

Switch to Frame
> driver.switch_to.frame(iframe_element)

Find element of interest within iFrame
> driver.find_element(element_to_find)

Switch back to main (parent) HTML 
> driver.switch_to.default_content()

A page can include multiple iframes and it is possible to switch to an iframe in two ways:
Switch iframe by its id/class and so on
> iframe = driver.find_element(By.ID, "content_frame")

> driver.switch_to.frame(iframe)

Switching to an iframe based on its index
> iframe = driver.find_elements(By.TAG_NAME,'iframe')[1]

> driver.switch_to.frame(iframe)

## Windows and tabs ##
WebDriver does not make any distinction between windows and tabs. When we are testing web pages where we have multiple browsers or tabs we need to change focus to the window we want to interact with.

Every window and tab has an uinque id called a handle which is persistent in the browser session. So if we want to switch to a window or tab we need to know these handles.
 
Get window handle  
You can get the window handle of the current window by using:  
> saved_handle = driver.current_window_handle

Opens a new tab and switches to new tab
> driver.switch_to.new_window('tab')

Opens a new window and switches to new window
> driver.switch_to.new_window('window')

Close the tab or window
> driver.close()

Switch back to the old tab or window.
Always switch back to original tab or window or webdriver will try to execute commands on the closed tab/window
> driver.switch_to.window(saved_handle)

If we want to list all window handles then we can use
> all_handles = driver.window_handles

### Difference between driver.close() and driver.quit() ###
We have used driver.close() in most examples and its fine when were only running Selenium tests in a single tab or browser window. But there is also driver.quit(). So what is the difference between them?

> driver.close()  

Will only close the current window or tab in the WebDriver session used by the browser process.

>driver.quit()  

Goes further and closes all windows and tabs associated with the WebDriver session. It will also close the browser process and background driver process. 

If remote webdriver is used with a Selenium Grid, then the Grid is notified that the browser is no longer in use so it can be used by another session.
 
So make sure to end Selenium test sessions correctly by using driver.quit(). Then WebDriver background processes and ports are not running in background and blocks new connections.
