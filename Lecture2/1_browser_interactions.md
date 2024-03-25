# Browser interactions #
For the 
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
> driver.save_screenshot('browser_screenshot.png')

And on a specific element which is visible
> element.screenshot('element_screenshot.png')  

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
Many times developers builds their own alerts by using popup windows/modals, then these alert commands does not work. Instead we have to handle the popup as a web page and find the buttons and field to interact with.

driver.execute_Script("alert('An anoying alert with Close button')")
driver.execute_Script("confirm('An anoying alert with Cancel & OK buttons')")
driver.execute_Script("prompt('An inputbox with Cancel & OK buttons','Pre-filled text')")

alert = driver.switch_to.alert
alert.accept()
alert.dismiss()

alert.text - Get the text from the alert, will it also get the text from the input field?
alert.sendKeys(“")

## IFrames ##
Page Navigation
*   Frames (inline frame) load other HTML elements inside a web page.
*   Kind of like "HTML within HTML"
*   Elements inside an iFrame can't be selected directly with Selenium.
*   Instead, you have to switch from the "main"HTML into the Frame.
*   Same problem in reverse - main HTML ngt accessible within iFrame

Steps:
*   Find iFrame element
*   Switch to Frame - driver.switch_to.frame(iframe_element)
*   Find element of interest within iFrame
*   Switch back to main HTML - driver.switch_to.default_content()

driver.get('https://www.firsturl.com/')
driver.find_element(By.ID, 'inside-element') # Fails!
iframe_element = driver.find_element(...)
driver.switch_to.frame(iframe_element)
driver.find_element(By.ID, 'inside-element') # Works driver.switch_to.default_content()

Switch iframe by id
> driver.switch_to.frame('buttonframe')

Switching to iframe based on index
> iframe = driver.find_elements(By.TAG_NAME,'iframe')[1]
> driver.switch_to.frame(iframe)

## Windows and tabs ##
Get window handle
WebDriver does not make the distinction between windows and tabs. If your site opens a new tab or window, Selenium will let you work with it using a window handle. Each window has a unique identifier which remains persistent in a single session. You can get the window handle of the current window by using:
> handle = driver.current_window_handle

Opens a new tab and switches to new tab
> driver.switch_to.new_window('tab')

Opens a new window and switches to new window
> driver.switch_to.new_window('window')

Close the tab or window
> driver.close()

Switch back to the old tab or window.
Always switch back to original tab or window or webdriver will try to execute commands on the closed tab/window
> driver.switch_to.window(handle)

### Difference between driver.close() and driver.quit() ###

We have used driver.close() in most examples and its fine when were only running Selenium tests in a single tab or browser window. But there is also driver.quit(). SO whats the difference between them?

> driver.close() 
Will only close the current window or tab in the WebDriver session used by the browser process.

>driver.quit()
Goes further and closes all windows and tabs associated with the WebDriver session. It will also close the browser process and background driver process. 

If remote webdriver is used with a Selenium Grid, then the Grid is notified that the browser is no longer in use so it can be used by another session.

So make sure to end Selenium tests correctly by using driver.quit() so webdriver background processes and ports are not running in background and blocks new connections.
