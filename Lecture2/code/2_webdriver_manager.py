# More detailed example for webdriver-manager. See documentation at https://pypi.org/project/webdriver-manager/

from selenium import webdriver
from time import sleep

# By default, all driver binaries are saved to user.home/.wdm folder. You can override this setting and save binaries to project.root/.wdm.
# import os
# os.environ['WDM_LOCAL'] = '1'

from selenium.webdriver.chrome.service import Service as ChromeService
#from selenium.webdriver.firefox.service import Service as FirefoxService
#from selenium.webdriver.edge.service import Service as EdgeService

from webdriver_manager.chrome import ChromeDriverManager
#from webdriver_manager.firefox import GeckoDriverManager
#from webdriver_manager.microsoft import EdgeChromiumDriverManager

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
#driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
#driver = webdriver.Edge(service=EdgeService(EdgeChromiumDriverManager().install()))

# Its possible to specify the version of webdriver in case a specific version is needed
# driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager(driver_version="119.0").install()))

driver.get("https://conrec-infinity-ab.github.io/Selenium-Course/")

sleep(3)
driver.quit()
