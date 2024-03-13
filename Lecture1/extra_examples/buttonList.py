from selenium import webdriver
from selenium.webdriver.common.by import By

from time import sleep

driver = webdriver.Chrome()

driver.get("http://127.0.0.1:5500/Lecture1/extra_examples/exampleButtons.html") # Change port to macth your live servers port

# Find all buttons with class name "button", will be saved in a list named buttons
buttons = driver.find_elements(By.CLASS_NAME, 'button')

# What happens when we click directly on the elements found - NOT WORKING! Uncomment to test
# driver.find_elements(By.CLASS_NAME, 'button').click()

sleep(2)

# This works when we click on the indivual buttons in the list
for button in buttons:
    sleep(0.5)
    button.click()

sleep(3)
driver.quit()