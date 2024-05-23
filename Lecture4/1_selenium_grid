# Selenium grid
If you want to run tests in parallel across multiple machines? Then, Grid is for you.

Selenium Grid allows the execution of WebDriver scripts on remote machines by routing commands sent by the client to remote browser instances.

Grid aims to:

* Provide an easy way to run tests in parallel on multiple machines
* Allow testing on different browser versions
* Enable cross platform testing

So if you want to run tests on a Mac with Safari its possible to set up a Selenium server on MacOSX and in the driver options specify that we want to run on Safari on a Mac. 

Or If you want to run several tests in parallel we can setup a Selenim Grid Hub with nodes on different operating systems and browsers.

We will not test the Hub - Node infrastructure. It can be quite complexed. Instead we will test with a Selenium Standalone server which handles all requests.

[Documentation](https://www.selenium.dev/documentation/grid/)

## Installation
1. Make sure you have a newer version of Java installed (v11+) on the computer which should host the Selenium grid instance

2. Browsers to run tests on should be installed on the host

3. Download [Selenium grid jar file](https://www.selenium.dev/downloads/)

## Running a Stand alone Selenium server
1. Open up a terminal and go to the folder where the `selenium-server-<version>.jar` file was saved

2. enter `java -jar selenium-server-<version>.jar standalone --selenium-manager true` 

The server should start, but might take a while first time. So wait and look for some text like the one below:

`[Standalone.execute] - Started Selenium Standalone 4.21.0 (revision 79ed462ef4): http://192.168.0.2:4444`

The `--selenium-manager true` argument is used to download the webdrivers used instead of downloading them manually and added to the **_PATH_**

3. Verify that the setup is working locally by opening a web browser and browse to `http://localhost:4444. A Selenium grid page shoudl be visible which shows some info about the server. 

4. Now you can connect to the Selenium server on the IP used and run your tests. But we need to modify tests to use the remote web driver instead of using the normal driver in earlier lessions.

Example usage:

```
# Imports as usual
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options

# To which server do we want to connect
selenium_grid = "http://127.0.0.1:4444"

# Initiate the driver by using webdriver.remote and select the server 
# If we have any options we can set them before and then use them here
driver = webdriver.Remote(options=chrome_options, command_executor=selenium_grid)

driver.get("https://conrec-infinity-ab.github.io/Selenium-Course/")
```
