from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://conrec-infinity-ab.github.io/Selenium-Course/")

sleep(2)

# Take a screenshot of the browser
driver.save_screenshot("browser_screenhot.png")

certificate_div = driver.find_element(By.ID, "certificate_div")

certificate_div.screenshot("certificate_screenshot.png")

driver.quit()
