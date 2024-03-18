# Example how to load browser web drivers if WebDriverManager is not working

from selenium import webdriver

# Which browser service should we use?
from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.firefox.service import Service
# from selenium.webdriver.chromium.service import ChromiumService

# Which webdriver do we want to download? 
# We need to manually download the specific browser driver and unzip it to a folder on your computer. Eg C:\webdrivers
# The downloaded webdriver should match the browser version on the computer/server where you will run your tests on
# Download links
# Chrome/Chromium 
# version >= 115 -> https://googlechromelabs.github.io/chrome-for-testing/
# version < 115 -> https://chromedriver.chromium.org/downloads
# Firefox -> https://github.com/mozilla/geckodriver/releases 
# Edge Chromium -> https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver

# Create the webdriver service objects and drivers for the browser we will use
# Chrome/Chromium
chrome_obj = Service("C:\webdrivers\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_obj)

# Firefox
# firefox_obj = Service("C:\webdrivers\geckodriver.exe")
# driver = webdriver.Firefox(service=firefox_obj)

# edge_obj = Service("C:\webdrivers\msedgedriver.exe")
# driver = webdriver.ChromiumEdge(service=edge_obj)

# Test driver by opening a page
driver.get("https://magento.softwaretestingboard.com")