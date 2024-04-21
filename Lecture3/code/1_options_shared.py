from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

# Create the Options object which will be used to change Chrome behaviour
chrome_options = Options()

# chrome_options.browser_version = "119" # Used when we run tests against a remote webdriver (Selenium grid)
# chrome_options.platform_name = "Windows 11" # Used when we run tests against a remote webdriver (Selenium grid)
chrome_options.accept_insecure_certs = True
chrome_options.page_load_strategy = "eager"

# Make sure we use the options we have set
driver = webdriver.Chrome(chrome_options)

driver.get("https://conrec-infinity-ab.github.io/Selenium-Course/index.html")

print("Title is: " + driver.title)

driver.quit()
