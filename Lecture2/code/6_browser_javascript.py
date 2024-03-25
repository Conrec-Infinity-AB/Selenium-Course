from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://conrec-infinity-ab.github.io/Selenium-Course/")

sleep(2)
# Execute some Javascript to show an alert()
driver.execute_script('alert("This is from Javascript");')

sleep(3)
# Execute some Javascript to open a window 
driver.execute_script('window.open();')

sleep(3)
driver.quit()
