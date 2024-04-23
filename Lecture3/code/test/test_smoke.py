from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from time import sleep

import pytest

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


# Add an setup fixture which we want to use for our tests
@pytest.fixture
def setup():
    print("\nIn setup")
    driver.get("https://conrec-infinity-ab.github.io/Selenium-Course/")


@pytest.mark.smoke
def test_checkPageTitle(setup):
    print("In test checkPageTitle")
    assert driver.title == "Selenium Course - Start page"


@pytest.mark.smoke
def test_checkHeader(setup):
    print("In test checkHeader")
    assert driver.find_element(By.TAG_NAME, "H1").text == "Selenium Course test page"
