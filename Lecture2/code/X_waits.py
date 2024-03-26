from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# The default time out for loading a page is 300 sec. We might not want to wait that long before continuing our tests. Set a really short time for this example
driver.set_page_load_timeout(10) 

# Set Network conditions if we want to emulate different speeds
driver.set_network_conditions(offline = False, latency = 50, download_throughput = 100 * 1024, upload_throughput = 100 * 1024, )

# Get the current network conditions
print (driver.get_network_conditions())

# Will load very slow
driver.get("https://conrec-infinity-ab.github.io/Selenium-Course/")

sleep(5)

# Delete our custom config
driver.delete_network_conditions() 
# print(driver.get_network_conditions()) # Error because custom config is deleted

# Should load fast now
driver.get("https://conrec-infinity-ab.github.io/Selenium-Course/aboutus.html")


# Implicit waits


# Explicit waits


sleep(5)
driver.quit()