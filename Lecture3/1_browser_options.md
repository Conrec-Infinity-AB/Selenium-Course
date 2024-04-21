# Browser options
When using the browsers we might want to have more control of the browser behaviour, for example running the browser headless. There are options which will work in every browser and there are specific options depending on which browser used. 

## How to setup browser options 
To use browser options we need to import Options from the specific browser we will use in the test.

here we import options for the Chrome browser
> from selenium.webdriver.chrome.options import Options 

Then we need to create an Option object where we can set our desired options:
> chrome_options = Options()

Now we can add our specific options we want to use. For example we want Selenium to ignore insecure SSL certificates
> chrome_options.accept_insecure_certs = True

Lastly we need to inform the driver that we will use our options
> driver = webdriver.Chrome(chrome_options)

or specify the options explicity
> driver = webdriver.Chrome(options=chrome_options)


## Shared browser options 
Below are some of the commonly shared options. To read up more of which exist go to [Selenium documentation for Browser options](https://www.selenium.dev/documentation/webdriver/drivers/options/)

- browserName this is set by default by the specific driver, but can be changed when running a remote test 

- browserVersion. This option is used to target a specific version of a browser when running a remote test

For example run only on Chrome version 124:
> chrome_options.browser_version = "124"

- platformName. This option is used to target a specific operating system of a browser when running a remote test 

For example run only on Windows 11:
> chrome_options.platform_name = "Windows 11"

- accept_insecure_certs. Accept insecure SSL certificates (default set to False):
> chrome_options.accept_insecure_certs = True

- pageLoadStrategy. How the browser will handle the page loading. Three different startegies exist, normal, eager and none. See browser option documentation for more info
> chrome_options.page_load_strategy = "eager"

## Browser options for specific browsers
There are also specific options when we run tests in Chrome, Edge and Firefox etc. Every browser has its own way to handle options. So always check specific browser documentation for setting an option. More info at [Selenium browser docs](https://www.selenium.dev/documentation/webdriver/browsers/)

For Chrome we can for example send specific arguments to the browser instance
- Like informing it to run in Headless mode
> chrome_options.add_argument("--headless")

- Starting the browser in full screen, maximized, or at a specific windows size 
> chrome_options.add_argument("--start-maximized")

> chrome_options.add_argument("--start-fullscreen")

> chrome_options.add_argument("--window-size=600,800")

There are a lot of arguments to use for Chrome, check this page for a [summary](https://peter.sh/experiments/chromium-command-line-switches/)   

## Chrome experimental options
There are also some options which is specific to Chrome and are not fully supported in selenium yet. But they can be set using the **_.add_experimental_option_** 

For example Remove the banner about browser is used by automation
> chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

We want to disable the popup blocker which might interfer with our tests
> chrome_options.add_experimental_option("excludeSwitches", ["disable-popup-blocking"])