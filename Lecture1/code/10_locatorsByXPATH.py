# Example for using the locator By.XPATH

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

# Example one by finding an element by using an absolut XPath
driver.find_element(By.XPATH, '/html/body/form/div[1]/input').send_keys('ABSOLUT')
time.sleep(2)

# Example two by finding the same element by using an relative XPATH. Here 
# // Defines the current path that we start at the input element and then find the element where ID = email
# Note we use @ to specify the elements attribute
driver.find_element(By.XPATH, '//input[@id="email"]').clear()
time.sleep(2) 

driver.quit()