# Google Chrome Dev tools #

## Shortcuts ##
There are many ways to access the dev tools in Chrome.

Open up Elements tab 
>F12

Open up the console
>CTRL + SHIFT + J

Command palette in the console tab
>CTRL + P

Search in the command palette
> \>
and then search for example: screenshot
## Elements ##
This tab is used to inspect the web page and its DOM tree.  
As a tester who writes Selenium code to interact with the web page, you spend a lot of time here to check how the web page is rendered and to find elements.

## Console ##
Here you can interact with the web page. Like quering the DOM tree, running Javascript code and more.  

There are several ways to find elements in the DOM tree
>document.querySelector('h1')

Find the first H1 element
>\$('h1')

Find all img elements as a list
>\$$('img')

Select specific element from a list and interact with it
>\$$('img')[2].click()

Enter an XPath to show element in page
>$x('/html/body/div[2]/main/div[3]/div/div[3]/div[1]/a/span/span[2]')

## Network ##
Here you can see all network traffic for the page when it loads and what might take long time to load.

Its also possible to emulate different network conditions here to test how a page behaves when theres a slow connection.

## Device toolbar ##
Used for emulating different devices like mobile phones. Good when checking page repsonivness.
But it is also possible to use different sensors like GPS coordinates and more.
> CTRL + SHIFT + M

## Lighthouse ##
Used to analyze the web page for performance and web optimization and more

## Recorder ##
This can be used to record and replay user interactions. 

Its also possible to export the recorded script to different test tools like Cypress, Webdriver.io and more.
