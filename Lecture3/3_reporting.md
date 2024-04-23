# Reporting in Python
## Pytest-html
There are plenty of test reporting tools in Python but the one we will use here is a simple reporting tool **_pytest-html_**. Its a plugin to Pytest and can be used to quickly create reports from Pytests in HTML format.

-   Test Execution Summary: The html report provides a complete summary of the tests with test status, including passed, failed, skipped, passed, and so on.
-   Screenshots: This is the most powerful feature of the pytest-html report; it can capture screenshots during the test runs and include them in the html report.
-   Test details: The report provides detailed information on each test with status, duration, failure message, screenshots, or traceback information.
-   Logs: The report displays log output from the test.
-   Customization: The report title, report file name, and so on, can be customized for the report output.

### Installation
Start by installing the package
> pip install pytest-html

### Usage
Run the tests with pytest as usual but add the option **_--html=report.html_** which is the name and path of the file to generate the report to
> pytest --html=regressiontest_report.html  

## Allure reports
Another reporting tool which is commonly used is Allure reports. It has more functionality and works with majority of programming languages. 

For Python there is the plugin [Allure-pytest](https://pypi.org/project/allure-pytest/). But for the plugin to work [Allure](https://allurereport.org) also needs to be installed on the computer. Its some more work to do to get all up and running but. Allure produces nice reports. 




