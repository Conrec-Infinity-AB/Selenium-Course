from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from time import sleep
from datetime import datetime

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("http://127.0.0.1:5500/docs/index.html")

# Get all cookies
cookies = driver.get_cookies()

# Print the cookies. In our example there will not be any set
for cookie in cookies:
    print(cookie)

# So let us set some cookies, using dictionaries

driver.add_cookie({'name': 'Selenium_text', 'value': 'This is the first cookie'})    

# get the current date and time and set the fomrat as a string so we can use it in a cookie
current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
driver.add_cookie({'name': 'Selenium_date', 'value': current_date})

# Get the cookies
cookies = driver.get_cookies()

# Print the cookies again. Now there should be two of them
for cookie in cookies:
    print(cookie)

driver.quit()