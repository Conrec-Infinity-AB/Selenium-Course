from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://conrec-infinity-ab.github.io/Selenium-Course/meetings.html")

# First lets see what happens if we try to interact with an element which is located in an iframe
# Because the default context is main/parent page we will not find the element

# Locate an element in the iframe to interact with
driver.find_element(By.CLASS_NAME, "iframe_button").click()

# Now lets switch to the iframe. There are several ways to switch
# Switch to the iframe by using its "name" tag
#driver.switch_to.frame("meeting_iframe")

# Switch to the iframe by using its element so it is our current context
#iframe = driver.find_element(By.ID, "meeting_iframe")
#driver.switch_to.frame(iframe)

# Switch to the iframe by using the index. In our setup we only have one iframe, so its the first
#driver.switch_to.frame(0)

# Switch to the first iframe by locating it by TAG_NAME
#driver.switch_to.frame(driver.find_elements(By.TAG_NAME, "iframe")[0])

sleep(3)

# Locate an element to interact with
#driver.find_element(By.CLASS_NAME, "iframe_button").click()
driver.find_element(By.ID, "Radio1").click()

sleep(3)
# When we are done working in the iframe and we need to interact with an element in the parent frame then we need to switch back to the parent frame again.
# There are two ways to do that, either use driver.switch_to.parent_frame() which goes up one level in frame hierachy. Because there can be frames within frames 
#driver.switch_to.parent_frame()
# Or use driver.switch_to.default_content() which goes back to the main/highets level frame
driver.switch_to.default_content()

pageheader = driver.find_element(By.TAG_NAME, "h1")
print(pageheader.text)

sleep(3)
driver.quit()