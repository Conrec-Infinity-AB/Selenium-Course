from behave import *
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


@given("I am on the main page")
def launch_browser(context):
    context.driver = webdriver.Chrome(
        service=Service(ChromeDriverManager("").install())
    )
    context.driver.get("https://conrec-infinity-ab.github.io/Selenium-Course/")


@when('I enter valid "{username}" and "{password}"')
def valid_username_password_parameter(context, username, password):
    context.driver.find_element(By.ID, "navbarEmail").send_keys("letmein@gmail.com")
    context.driver.find_element(By.ID, "navbarPassword").send_keys("secretpassword")


@when("I click the login button")
def click_login(context):
    context.driver.find_element(By.ID, "loginButton").click()


@then("I should see the login status page")
def verify_successful(context):
    statusText = context.driver.find_element(By.ID, "checklogin-text").text
    assert statusText == "Logged in!"


@when("I enter invalid username and password")
def invalid_username_password(context):
    context.driver.find_element(By.ID, "navbarEmail").send_keys("bademail@gmail.com")
    context.driver.find_element(By.ID, "navbarPassword").send_keys(
        "notsosecretpassword"
    )


@then("I should see an error message")
def verify_unsuccessful_login(context):
    statusText = context.driver.find_element(By.ID, "checklogin-text").text
    assert statusText == "Wrong credentials!"


@then("I close the browser")
def teardown(context):
    context.driver.quit()
