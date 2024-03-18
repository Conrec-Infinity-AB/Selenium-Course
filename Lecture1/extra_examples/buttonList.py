from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:5500/Lecture1/extra_examples/exampleButtons.html") # Change port to match your live servers port

# Find all buttons with class name "button", will be saved in a list named buttons
buttons = driver.find_elements(By.CLASS_NAME, 'button')

# Using driver.find_element(...): What happens when we click directly on the elements found - Will work. Selenium will find the first element matching the By clause and does not look further. We will then be able to click on the found element
driver.find_element(By.CLASS_NAME, 'button').click()

# Using driver.find_elements(...): What happens when we click directly on the elements found - Will not work because we get a list of elements
#driver.find_element(By.CLASS_NAME, 'button').click()

# Instead we need to iterate the elements list and click on the indivual buttons in the list
#for button in buttons:
#    sleep(0.5)
#    button.click()

sleep(3)
driver.quit()