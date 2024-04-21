from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from time import sleep

# Create the Options object which will be used to change Chrome behaviour
chrome_options = Options()

# Remove the banner about browser is used by automation
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
# Disable popup blocker
chrome_options.add_experimental_option("excludeSwitches", ["disable-popup-blocking"])

# Make sure we use the options we set
driver = webdriver.Chrome(chrome_options)

# Webbrowser should now start headless
driver.get("https://conrec-infinity-ab.github.io/Selenium-Course/index.html")

print("Title is: " + driver.title)

sleep(3)
driver.quit()
