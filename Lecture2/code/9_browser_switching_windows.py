from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from time import sleep

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get("https://conrec-infinity-ab.github.io/Selenium-Course/")

# Get window handle
# You can get the window handle of the current window by using:

saved_handle = driver.current_window_handle

#Opens a new tab and switches to new tab
#driver.switch_to.new_window('tab')

#Opens a new window and switches to new window and load a page
driver.switch_to.new_window('window')
driver.get("https://wikipedia.org/")

sleep(3)

#Close the current tab or window
#driver.close()

#Switch back to the old tab or window. Always switch back to original tab or window or webdriver will try to execute commands on the closed tab/window
driver.switch_to.window(saved_handle)

#If we want to list all window handles then we can use
all_handles = driver.window_handles
for handle in all_handles:
    print(handle)

sleep(3)
# Closes all open windows and tabs in the session
driver.quit()