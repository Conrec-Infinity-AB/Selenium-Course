from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from time import sleep
import sys

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://conrec-infinity-ab.github.io/Selenium-Course/")

sleep(2)

# Take a screenshot of the browser and saves to disk
#driver.save_screenshot("browser_screenhot.png")

# Take a screenshot of a specific element (and its siblings) and saves to disk
certificate_div = driver.find_element(By.ID, "certificate_div")
#certificate_div.screenshot("certificate_screenshot.png")

# It is also possible to take screenshot without saving. Useful if you want to compare or maniplulate image in memery 
image = driver.get_screenshot_as_png()
print(type(image))
print(sys.getsizeof(image))

driver.quit()
