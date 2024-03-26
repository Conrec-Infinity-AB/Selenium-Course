from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://conrec-infinity-ab.github.io/Selenium-Course/companyinfo.html")

# Dropdown example
# Find the Dropdown element
person_dropdown = driver.find_element(By.ID, "dropdown_persons")
dropdown = Select(person_dropdown)

# Click on it to expand to see values
person_dropdown.click()
sleep(1)

# Select by the value="text"
#dropdown.select_by_value("ElonHusk")
#sleep(2)

# Select by the index
#dropdown.select_by_index(4) # Tom Holland 
# Disabled value will give an error
#dropdown.select_by_index(3) 
#sleep(2)

# Select by visible text in dropdown
#dropdown.select_by_visible_text("Chris Hemswirth")

# Loop through the dropdown options and check some values
dropdown_options = person_dropdown.find_elements(By.TAG_NAME, 'option')

# Print the visible texts
#print([option.text for option in dropdown_options])
#print()

# Print if an option is selected
#print([option.is_selected() for option in dropdown_options])
#print()

# Print if an option is disabled
#print([option.is_enabled() for option in dropdown_options])
#print()

sleep(3)
driver.quit()

