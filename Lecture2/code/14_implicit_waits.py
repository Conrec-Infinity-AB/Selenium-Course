from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# Implicit waits
# We want to change the time when searching for individual elements in our session so change the wait time to 30 sec from default 0
driver.implicitly_wait(30) 

driver.get("https://conrec-infinity-ab.github.io/Selenium-Course/")

sleep(2) # Just so we have time to see page

# Example how we can find all New Employee images and names
# Find the section with all employees
employee_section = driver.find_element(By.CLASS_NAME, "employees_container")

# When we have the section we can chain the elements and iterate all images within that section and save as a list. This way we know we only get images of the New employees
employees_images = employee_section.find_elements(By.TAG_NAME, "img")

print(f'There are {len(employees_images)} new employees:\n')
for employee in employees_images:
    print("Persona: " + employee.get_attribute("title") + ", image = " + employee.get_attribute("src") + "\n")

# Explicit waits

driver.quit()