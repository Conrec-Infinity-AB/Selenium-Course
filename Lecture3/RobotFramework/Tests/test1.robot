*** settings ***
Library                 SeleniumLibrary
Resource                ../Resources/resource1.resource
Test Setup              Open Application
Test Teardown           Close Browser

*** variables ***
${url}                  https://conrec-infinity-ab.github.io/Selenium-Course/
${username}             letmein@gmail.com
${password}             secretpasssword

*** Test Cases ***
Validate there exist a new employee named taylor Kwift
    Given User is able to navigate to the application main page
    Then Verify that there is a new employee named Taylor Kwift
    [Teardown] 
    Close Browser

Validate that we have a card Company info and we can navigate to the Company Info page 
    Given User is able to navigate to the application main page
    When User Clicks on Company info button
    Then Verify Company Info page is visible
    And Verify that checkbox button Tom Halland is disabled
    [Teardown] 
    Close Browser
