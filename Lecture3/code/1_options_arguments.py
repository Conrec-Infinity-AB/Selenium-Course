from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

# Create the Options object which will be used to change Chrome behaviour
chrome_options = Options()

chrome_options.add_argument("--headless")
# chrome_options.add_argument("--start-maximized")
# chrome_options.add_argument("--start-fullscreen")

# Make sure we use the options we set
driver = webdriver.Chrome(chrome_options)

driver.get("https://conrec-infinity-ab.github.io/Selenium-Course/index.html")

print("Title is: " + driver.title)

sleep(3)
driver.quit()
