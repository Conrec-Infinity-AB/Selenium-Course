from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://magento.softwaretestingboard.com/customer/account/login")

# https://www.selenium.dev/selenium/docs/api/py/webdriver_support/selenium.webdriver.support.relative_locator.html

# above
#passwordField = driver.find_element(By.ID, "pass")
#emailAddressField = driver.find_element(locate_with(By.TAG_NAME,  "input").above(passwordField))

#emailAddressField.send_keys('nisse.hult@hotmail.com')

# below
#emailAddressField = driver.find_element(By.ID, "email")
#passwordField = driver.find_element(locate_with(By.TAG_NAME, "input").below(emailAddressField))

#passwordField.send_keys('SecretPassword')

# to the left of
emailAddressField = driver.find_element(By.ID, "email")
emailAddressLabel = driver.find_element(locate_with(By.TAG_NAME, "input").below(emailAddressField))

signinButton.click()

# to the right of
#cancelButton = driver.find_element(By.ID, "cancel")
#submitButton = driver.find_element(locate_with(By.TAG_NAME, "button").to_right_of(cancelButton))

# near
#emailAddressLabel = driver.find_element(By.ID, "lbl-email")
#emailAddressField = driver.find_element(locate_with(By.TAG_NAME, "input").near(emailAddressLabel))
sleep(5)
driver.quit()