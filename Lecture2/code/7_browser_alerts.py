from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://conrec-infinity-ab.github.io/Selenium-Course/companyinfo.html") 

sleep(1)

# 1. Alert button. Find the button and click it to open the first alert
button = driver.find_element(By.ID, "alert_button")
button.click()
sleep(1)

#switch to alert box
alert = driver.switch_to.alert
sleep(1)

# Print the text in the alert
print("Alert text: " + alert.text)

# Accept the alert
alert.accept()

sleep(2)

# 2. Confirm button. Find the button and click it to open the first alert
button = driver.find_element(By.ID, "confirm_button")
button.click()
sleep(1)

#switch to confirm box
confirm = driver.switch_to.alert
sleep(1)

# Print the text in the confirmation alert
print("Confirmation text: " + confirm.text)

# Accept the alert
#confirm.accept()
# Cancel the alert
confirm.dismiss()

sleep(2)

# 3. Prompt button. Find the button and click it to open the first alert
button = driver.find_element(By.ID, "prompt_button")
button.click()

sleep(1)
#switch to prompt box
prompt_name = Alert(driver)
#prompt_name = driver.switch_to.alert
sleep(1)

prompt_name.send_keys("Lennart Swan")
sleep(1)

# Print the text in the confirmation alert
print("prompt text: " + prompt_name.text)
prompt_name.accept()
#prompt_name.dismiss()

sleep(5)
driver.quit()