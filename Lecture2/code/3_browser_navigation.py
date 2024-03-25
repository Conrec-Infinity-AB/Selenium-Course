from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

driver.get("https://conrec-infinity-ab.github.io/Selenium-Course/")

# get the current URL and page title
currentURL = driver.current_url
pageTitle = driver.title
print("Current URL is:" + currentURL)
print("Page title is: " + pageTitle)

# The default time out for loading a page is 300 sec. We might not want to wait that long before continuing our tests. Set a really short time for this example
#driver.set_page_load_timeout(2) 
# Try load a page which is slow (I do not have any good examples... But lowering time to really short helps)
#driver.get("https://www.smithfieldfoods.com/")

# Open a link in the current tab and then go back 
# First wait some so see that the index page has loaded and then lets click on the Certificate image which is also a link
sleep(2)
certificateLink = driver.find_element(By.ID, 'certificates_link')
certificateLink.click()

# Now we should be located on the certificates page
currentURL = driver.current_url
print("Should be certificate.html. Current URL is:" + currentURL)

# Wait some again and go back one page
sleep(3)
driver.back()

# Now were back on index page
currentURL = driver.current_url
print("Should be index.html. Current URL is:" + currentURL)

# Now we can go forward again
sleep(3)
driver.forward()

currentURL = driver.current_url
print("Should be certificate.html. Current URL is:" + currentURL)

### Question: Do you see any problems with the code above? ###

# If we want to see or use the rendered HTML code. Sometimes it can be useful to save the source as an object. Example if you want to scrape some pages and save the html 
htmlPage = driver.page_source
print(htmlPage)

sleep(3)
driver.quit()
