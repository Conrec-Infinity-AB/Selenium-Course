*** Keywords ***
Open Application
    Open Browser                browser=chrome

User is able to navigate to the application main page
    Goto                        ${url}

Verify that there is a new employee named Taylor Kwift
    Sleep                       1s
    Element Should Contain      class:employees_container                   Taylor Kwift

User Clicks on Company info button
    Click Element               class:companyinfo-button

Verify Company Info page is visible
    Wait Until Page contains    Company Info

Verify that checkbox button Tom Halland is disabled
    Element Should Be Disabled  CheckboxPersons_2