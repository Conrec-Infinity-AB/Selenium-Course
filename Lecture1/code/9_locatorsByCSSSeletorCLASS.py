# Example for using the locator By.CSS_SELECTOR (CLASS)

# This example requires the Visual Studio plugin "Live Server". Install it from plugins menu
# Right click on the /Lecture1/code/locators.html file and select "Open with Live Server". The page will open in browser and you can run this code example


from selenium import webdriver
# Here we import By so we can use it to find locators in the page  
from selenium.webdriver.common.by import By

# Time is not a Selenium package, its used for setting a delay in code before quiting.
import time

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:5500/Lecture1/code/locators.html")

# Lets wait a few seconds so we have time to see the page
time.sleep(2) 

# Example one by finding the class by "."
driver.find_element(By.CSS_SELECTOR, '.input-text').send_keys('Example 1')
time.sleep(2)
# Example two by finding the class by tag[class="CLASSNAME"]
driver.find_element(By.CSS_SELECTOR, 'input[class="input-text"]').send_keys('Example 2')
time.sleep(2)
# Example two by finding the class by tag.CLASSNAME and clear the input
driver.find_element(By.CSS_SELECTOR, 'input.input-text').clear()

time.sleep(2) 

driver.quit()