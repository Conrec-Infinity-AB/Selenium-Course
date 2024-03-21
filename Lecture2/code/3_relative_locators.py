from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://magento.softwaretestingboard.com")

# above
passwordField = driver.find_element(By.ID, "password")
emailAddressField = driver.find_element(locate_with(By.TAG_NAME,  "input").above(passwordField))

# below
emailAddressField = driver.find_element(By.ID, "email")
passwordField = driver.find_element(locate_with(By.TAG_NAME, "input").below(emailAddressField))

# to the left of
submitButton = driver.find_element(By.ID, "submit")
cancelButton = driver.find_element(locate_with(By.TAG_NAME, "button").to_left_of(submitButton))

# to the right of
cancelButton = driver.find_element(By.ID, "cancel")
submitButton = driver.find_element(locate_with(By.TAG_NAME, "button").to_right_of(cancelButton))

# near
emailAddressLabel = driver.find_element(By.ID, "lbl-email")
emailAddressField = driver.find_element(locate_with(By.TAG_NAME, "input").near(emailAddressLabel))
sleep(2)
driver.quit()