from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from time import sleep

# Where should the tests run
selenium_grid = "http://127.0.0.1:4444/wd/hub"

# Create the Options object which will be used to change Chrome behaviour
chrome_options = Options()
# chrome_options.add_argument("--headless")

# Old way to inform a Selenium grid where tests should run was to use Desired Capabilities. This has been removed from Selenium 4.
# Instead options should be used
chrome_options.browser_version = "120"
chrome_options.platform_name = "Windows 10"

driver = webdriver.Remote(options=chrome_options, command_executor=selenium_grid)
