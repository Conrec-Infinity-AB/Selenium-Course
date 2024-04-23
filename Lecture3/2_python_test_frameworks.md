# Test frameworks
## Pytest
https://docs.pytest.org/en/8.0.x/how-to/index.html

One of the more common test frameworks in Python is Pytest. It is simple to get started with and flexible.

Some of its features are:
*   Supports test automation of functional testing, unit testing and integration testing
*   Supports plugins that extends Pytest functionality
*   Supports data parameterization

### Installation
To use Pytest in a project we need to install its package. This can be done with the pip command as before. In our project the dependency is already included in requirements.txt so we should not need to install it.

To install, it will download all Pytest and all its dependencies:
> pip install pytest

Verify that the project has a version of Pytest installed:
> pytest --version

Output:
> pytest 8.0.1

### Test files
By default, Pytest looks for test files with the prefix "test." or suffix "_test". 

For example we can name test files like the following:
> test_login.py

> login_test.py

Both works and when Pytest executes tests, it will search for test files in the current directory and subdirectories and identifies all of them as test files. 

Organizing all tests in a **_test_** folder with sub folders is a good practise and Pytest will consider all the files as test files. 

To run all tests in the test/ folder and its sub folders
> pytest test/

It is also possible to run individual test files by explicitly mentioning thir file names. 
> pytest test/test_login.py test/test_logout.py -v -s

**_-v -s_** is used to show more verbose output and print both stdout and stderr to the terminal.

### Test functions
Pytest also looks for functions with the prefix "test_". 

For example a test function 

> def test_validate_email(): 

This makes it easy to identify and run tests in Pytest.

If we want to find and run all tests with some text in their their names or function names, we can do that too. 

For exampe if we want to run all tests and functions with **_Login_** in their names we can use the following:
> pytest -k Login -v -s

**_-k_** is the substring we want to look for in test names 

> pytest -k "not Login" -v -s
**_not_** will instead skip all Login tests. We can use **_and, or, not_** to combine tests 

### Markers
It is possible to mark tests for different purposes. This is done with Python decorators **_@_**

For example two different test markers
> @pytest.mark.smoke  

> @pytest.mark.regression  

```
@pytest.mark.smoke
def test_login_username():
    pass  
```

To get it to work we need to add a **_pytest.ini_** file to our project and add the markers to the file
```
[pytest]
markers =
    smoke: marks a test as a smoke test
    regression: marks a test as a regression test
```
Now we can run tests by using their markers. And as with running files above we can use **_and, or, not_** to combine marked tests
> pytest -m regression

And if we want to list all markers in the project
> pytest --markers

Output:
```
@pytest.mark.smoke: marks a test as a smoke test
@pytest.mark.regression: marks a test as a regression test
```

If we want to skip a test we can also mark them with the **_skip** marker
```
@pytest.mark.skip(reason="This test is temporarily disabled.")
def test_login_username():
    ... assert something ...   
```

And if we want to fail a test by purpose
```
@pytest.mark.xfail(reason="Expected to fail until we fix the bug.")
def test_login_username():
    ... assert something ...   
```

### Fixtures
Fixtures in Pytest is a function that will be reused by several tests. An example is a setup function which we want to run before every test.

Like markers we setup fixtures with a Python decorator **_@pytest.fixture_**
``` 
@pytest.fixture
def setup():
    ... code we want to run before actual tests ...
```

Then our test functions we need to call the setup fixture by calling the test with our setup function
```
def test_ourTest(setup):
    ... code ...
```

Now the setup will run everytime a test calls it 

## Assertions
We have used it before but not really talked about the assert function. When writing test cases we need to know if the functionality we are testing are as we expect or not. In Python there is an built in assertion function which is sufficient in most cases. But if we want to have more control over what we test then we can install a third party assert library.

One is **_assertpy_** which is popular and which we will install.
> pip install assertpy

When it has been installed we need to import the package in our Python test. Then we can use all the assert functions we need. See [AssertPy docs](https://assertpy.github.io/docs.html). Now we have more control over what we want to assert on.

```
from assertpy import assert_that

assert_that('foo').starts_with('f')
assert_that('123').is_digit()
assert_that('').is_empty()

... And more ...
```

Another assertion library we can use is for example [Grappa](https://github.com/grappa-py/grappa). 
It uses declarative assertion styles as **_expect_** and **_should_**.

Install it by 
> pip install grappa

```
from grappa import should

3.14 | should.be.lower.than(4)

foo = 'bar'
foo | should.equal('bar')
foo | expect.to.equal('bar')
foo | expect.to.be.a('string')

... And more ...
```






## Behave - Behave is a Behavior Driven Development 
[Behave](https://behave.readthedocs.io/en/latest/)
Behave is a Behavior Driven Development (BDD) framework for Python that enables writing and executing high-level scenarios and feature files in a natural language format. 

Behave is built on top of Gherkin language, which is written using "Given", "When", "And" and "Then" keywords, which are easy to understand by both technical and non-technical stakeholders.

### Behavior Driven Development Keywords
- Given: The Given step is used to describe the preconditions or the initial state of the system. It sets up the context in which the scenario takes place.

- When: The When step is used to describe the action or event that the user performs on the system. It represents the trigger that causes the system to behave in a certain way. 

- Then: The Then step is used to describe the expected outcome or result of the action or event described in the When step. It represents the expected behavior of the system.

- And: The And step is used to concatenate multiple Given, When or Then steps, that belong to the same scenario and create more complex scenarios that involve multiple steps, making it easier to write more comprehensive tests.

### Installation
Install with pip and verify it were installed successfully
```
pip install behave

behave --version
behave 1.2.6
```

Then create a **_features_** folder in the root folder of the project. This folder will contain all features we want to test in our project
> mkdir features

### Example
In the features folder create a features file 
> login.feature

Add the feaatures you want to test
```
Feature: Login functionality
As a user,
I want to be able to log in to the application so I can access my account.
```

```
Scenario: Valid credentials
Given I am on the login page
When I enter valid username and password 
And I click the login button
Then I should see the sucessful login page
```

Then we need to implement some code for the features. So in the features folder create a **_steps_** folder 
> mkdir steps

Then create the Python file for the features implementation
> loginSteps.py
```
from behave import *
... other imports ...

@given("I am on the main page")
def launch_browser(context):
    context.driver = webdriver.Chrome(service=Service(ChromeDriverManager("").install()))
    context.driver.get("https://conrec-infinity-ab.github.io/Selenium-Course/")

@when('I enter valid "{username}" and "{password}"')
def valid_username_password_parameter(context, username, password):
    context.driver.find_element(By.ID, "navbarEmail").send_keys("letmein@gmail.com")
    context.driver.find_element(By.ID, "navbarPassword").send_keys("secretpassword")

@when(u'I click the login button')
def click_login(context):
    context.driver.find_element(By.ID, "loginButton").click()

@then("I should see the login status page")
def verify_successful(context):
    statusText = context.driver.find_element(By.ID, "checklogin-text").text
    assert statusText == "Logged in!"

@then(u'I close the browser')
    def teardown(context):
    context.driver.quit()
```

Then when features and code has been setup we can first check if everything has been implemented.
> behave --dry-run
``` 
0 features passed, 0 failed, 0 skipped, 1 untested
0 scenarios passed, 0 failed, 0 skipped, 5 untested
0 steps passed, 0 failed, 0 skipped, 5 undefined, 14 untested
Took 0m0.000s

You can implement step definitions for undefined steps with these snippets:

@given(u'I am on the main page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I am on the main page')
```

If everything looks good, lets run the tests
> behave

Now the browser should open up and run the scenario and its features.

## Robot Framework
[Robot Framework](https://robotframework.org) and [Robot framework SeleniumLibrary](https://robotframework.org/SeleniumLibrary/)

Another major framework is the open-source Robot framework which can be used for acceptance testing, Acceptance Test Driven Development, Behavior Driven Development and Robotic Process Automation (RPA).

It is designed to write test cases in a keyword-driven testing approach and provides test libraries to implement test automation flows. This way we do not need to write as much code to create test cases.

The Robot Framework is a flexible and powerful test automation framework that can be integrated with a wide range of tools and technologies. It supports various interfaces and protocols, making it possible to automate different types of systems and applications.

_We wont get into detail how to write Robot Framework tests but it is easy to add to Selenium when using Python. Below is how you get started._

### Installation
Install with pip and verify it were installed successfully

pip install robotframework

Verify it was installed
```
pip show robotframework
Name: robotframework
Version: 7.0
...
```

We also need to install the SeleniumLibrary used by Robot Framework
> pip install robotframework-seleniumlibrary

And to verify it was installed
```
pip show robotframework-seleniumlibrary
Name: robotframework-seleniumlibrary
Version: 6.3.0
...
```

### Folder structure
The folder structure in the Robot framework is used to get an organized, and easy to manage structure. The main folders and files added in the robot framework within the root folder are test suites, test cases, test data, resources, config, and library. 

The test files have the extension **_.robot_** and the resources file has the extension **_.resource_**.

- Test Suite folder: The test suite folder contains all the test suite files and contains the test cases to be executed. The test cases contain keywords. When the complete Test suite is executed, all the test cases within the suite are executed

- Resource Folder: The resource folder is where both user-defined and the library reusable keywords are defined. These keywords can be shared across multiple test suites and test cases. To use the keywords in resource files, these files are required to be imported into the test suite using the **_Resource_** keyword

- Test Data Folder: Test Data folder is used to store all the data files required for the automation of the project. It can be API request payload data to access APIs, database query data, or excel sheet data for data parameterization.

- Configs and Libraries: The Python code implementation of user-defined keywords are added in the Python file in the library folder, and test execution configurations such as test environments, environment variables from the config file, and so on, are added in the configs folder.

- Results Folder: When the robot framework is executed, the log and report files are stored in the results folder. By default, these files are created in the root directory, but can be configured to be placed in the results folder. In addition to log file, the results folder can contain screenshots generated by the robot framework.

### Example
The robot test file
> login.robot
```
*** settings ***
Library                         SeleniumLibrary

Resource                        ./code1.resource

Test Setup                      Open Application
Test Teardown                   Close Browser

*** variables ***
S{url}                          https://conrec-infinity-ab.github.io/Selenium-Course/
$(username)                     letmein@gmail.com
${password}                     secretpassword


*** Test Cases ***
Validate User is able to login to the application
    Given User is able to navigate to the application
    And Enter the valid login credentials and submit
    Then Validate user is successfully logged into the application
```
    
The test resource file
> code1.resource
```
*** Keywords ***
Open Application
    Open Browser                browser=chrome

User is able to navigate to the application    
    Goto                       ${url}

Enter the valid login credentials and submit
    Input Text                  navbarEmail       $(username)
    Input Password              navbarPassword    $(password)
    Click Element               loginButton

Validate user is successfully logged into the application
    sleep 5
    ${pageTitle}                GetTitle
    Log                         ${pageTitle}
    Wait Until Page Contains    Logged in!
```

### Running tests
> robot login.robot

>robot path/to/my_tests/

### Locators
When using Robot Framework we can match locators by different strategies. below are some examples

| Strategy | Match based on      | Example       |
| ---------| -----------         |------------   |
| id       | Element id          | id:email      |
| name     | name attrubute      | name:submit   |
| class    | Element class name  | class:button  |
| tag      | Tag name            | tag:div       |
| xpath    | XPath expression    | xpath://div[@id="email"] | 
| css      | CSS selector        | css:div#email |

### Keywords
There are many keywords to use when writing the tests. Both [built in](https://robotframework.org/robotframework/latest/libraries/BuiltIn.html) and in external libraries like [SeleniumLibrary](https://robotframework.org/SeleniumLibrary/SeleniumLibrary.html)

| Keyword           | example / value                   | Comment                             | Library / built in   | 
| ---------         | -----------                       | ------                              | ------------         |
| Get Title         | ${pageTitle}    Get Title         | Saves page title to an variable     | SeleniumLibrary      |
| Sleep             | sleep           5s                | Sleeps 5 sec, can use other formats | Base library      |
| Should Be Equal   | Should Be Equal ${pageTitle} Text | Check if pageTitle is equal to text | Base library         |
| Click Button      | Click Button    id:button         | Click button with id:button         | SeleniumLibrary      |
| Click Element     | Click Element   id:submit         | Click an element with id:submit     | SeleniumLibrary      |
| Get Text          | Get text        tag:h1            | Get the text from H1 tag            | SeleniumLibrary      |
| Input Text        | Input Text      email             | Enter text in an input field email  | SeleniumLibrary      |

**_Note_** in last example **_Input Text_** we do not need to include the **_id:_** if the value is an ID beacuse Robot Framework looks for ID as default

### Advantages of Robot Framework 
- The Robot framework is easy to implement even with little to no programming experience

- Keyword-driven testing: Robot framework allows writing the test cases using high-level, business-friendly language

- Test libraries: There are builtin and custom test libraries which makes it easy to write test with little code. 

- Can be easily integrated with CI/CD pipelines

- Built in logging and reporting