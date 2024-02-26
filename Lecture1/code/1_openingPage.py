# Import the webdriver to use
from selenium import webdriver

# Which browser/driver should be used 
# In earlier versions of Selenium we need to download and setup the webdriver before usage. In Selenium 4 we do not need this. Web driver manager downloads the correct driver and version for browser used 
 
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.ChromiumEdge()

# Open the page we want to test
driver.get("https://magento.softwaretestingboard.com")

# Just get the title of the page and print to the console
print("Title is: " + driver.title)

# Best practices is to always end the webdriver session eventhough it will quit when the file ends
driver.quit()