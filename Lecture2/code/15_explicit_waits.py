from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
import selenium.common.exceptions as EX

from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Explicit waits
driver.get("https://conrec-infinity-ab.github.io/Selenium-Course/")

meetings_div = driver.find_element(By.CLASS_NAME, "companyinfo")
meetings_link = meetings_div.find_element(By.TAG_NAME, "a").click()

# Now we should be on the meetings page. First let us verify that it is teh right page
assert driver.title == "Selenium Course - Company Info", "Title is: " + driver.title

# Let us find an element but using explicit wait

confirm_button = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, 'confirm_button'))).click()

confirm_alert = WebDriverWait(driver, 5).until(EC.alert_is_present())
sleep(2)

confirm_alert.dismiss()

# Now an wait for an element to be invisible (which will not happen) to show exceptions
try:
    confirm_button = WebDriverWait(driver, 5).until(EC.invisibility_of_element((By.ID, 'confirm_button')))
except EX.WebDriverException:
    print("Button is visible!")

driver.quit()