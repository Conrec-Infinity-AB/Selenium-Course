# Example for using the locator By.TAG_NAME

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

# Just print the text from the H1 tag to the console
print("Class is: " + driver.find_element(By.TAG_NAME, 'h1').get_attribute('class'))
print("Text is: " + driver.find_element(By.TAG_NAME, 'h1').text)

driver.quit()