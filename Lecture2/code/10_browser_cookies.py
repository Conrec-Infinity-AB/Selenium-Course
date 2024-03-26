from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from time import sleep
from datetime import datetime

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://conrec-infinity-ab.github.io/Selenium-Course/")

# Get an individual cookie
cookie = driver.get_cookie("selenium_text")

# Get all cookies
cookies = driver.get_cookies()

# Print the cookies. In our example there will not be any set
print("Cookies set in site?")
for cookie in cookies:
    print(cookie)

print("\nDone checking cookies...\n\n")
# So let us set some cookies, using dictionaries

print("Cookies set in site?")
driver.add_cookie({'name': 'selenium_text', 'value': 'This is the first cookie'})    

# get the current date and time and set the fomrat as a string so we can use it in a cookie
current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
driver.add_cookie({'name': 'selenium_date', 'value': current_date})

# Get the cookies
print("Individual cookie: ")
print(driver.get_cookie("selenium_text"))
      
cookies = driver.get_cookies()

# Print the cookies again. Now there should be two of them
print("\nAll cookies: ")
for cookie in cookies:
    print(cookie)

print("\nDone checking cookies...\n\n")


# We can delete all cookies we set for the page, either individually by the cookie name or all at once
# Individual
driver.delete_cookie('selenium_text')

# All at once
#driver.delete_all_cookies()

# Get the cookies
cookies = driver.get_cookies()

# Print the cookies again. Now there should be two of them
for cookie in cookies:
    print(cookie)

print("\nDone checking cookies...\n\n")



driver.quit()