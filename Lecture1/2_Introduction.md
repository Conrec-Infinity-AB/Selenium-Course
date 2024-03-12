# Lecture 1 - Test automation and Selenium #
It might be easy to think its straight forward to to implement automation as part of the testing process. But there are some things to think about which should be taken in consideration. 
  
## What should we automate ##
We should strive to automate tasks that are repeating and tedious such as regression testing. 

Find those areas which has the biggest risk to fail.

Other tests which are hard to do manually, such as performance testing. 

## Benefits of automated testing ##
We save effort and time, and we reduce risks by having better coverage. Test automation allows more test cases to be run and reduces repetitive work. Easier and faster testing allows for running more tests, achieving better test coverage. 

Another benefit is consistency and repeatability. Test tools improve testing consistency and repeatability. For example tests can be executed in the same order and frequency.

## When should automated testing not be used ##
Unstable applications. The cornerstone of test automation is the premise that the expected application behavior is known. When this is not the case, it is usually better not to automate. 

If the person/people writing the tests are not sufficiently experienced their tests will have doubtful value. An automated test is only as good as the person who created it. If you don't have enough time or resources to manually complete your testing in the short term, don't expect test automation to help you.

Look at automation for the longer term. Remember that automation is a strategic solution, not a short-term fix.

## How not to automate ##
Unrealistic expectations in organizations with limited experience with test automation. Make sure people have proper expectations. Time savings come only when automated tests can be executed more than once.

Underestimating time, cost and effort required to implementing test automation. The test framework should be built and integrate with other tools like CI/CD pipelines. Test data setup should be reset after runs.
Do not forget to set code standards and guidelines for the automation solution. Training of those who will use the test framework. 

Underestimate maintenance. It can require a big effort to maintain tests. Budget for test maintenance is not always included. This can lead to running tests that result in false positives and negatives when theres no time to update tests.

You should be careful which test cases you automate. There might be existing manual tests that are incomplete or incorrect. Always double-check manual test cases and test data.

Automation is more than test execution. You need to document, manage and maintain the tests. Use tools for executing the testa and also have a good way of reporting the results to the organisation.

Do not to create tests which is dependent of other tests. This is especially important when test executions are done in parallell. Tests will fail when some criterias are not fullfilled, or when dependent tests are run in different browser threads.

Test flakiness might be a problem. Do not add new tests directly to production environment tests. Make sure you have tested the new tests in different environments and browsers and not just one time before approving to add them to a test suite. A test can work 99% of the time but when a test fails 1% of the time because of flakiness it can make the developers and team not trust the tests.

Expecting UI components / elements are always located in the same place. Changes to UI might move elements. This relates mostly to XPath selectors.

## The Selenium project ## 
In this course we are focusing on Browser UI test automation with Selenium. But Selenium is not just one tool or API, it consists of many tools.

Here are the different definitions about the Selenium project from the official Selenium page. We will mostly focus on the Selenium Webdriver in this course and later on dive in some how to setup a Selenium Grid to run tests remotly. 

### The Selenium Browser Automation Project ###
Selenium is an umbrella project for a range of tools and libraries that enable and support the automation of web browsers. It provides extensions to emulate user interaction with browsers, a distribution server for scaling browser allocation, and the infrastructure fo implementing the W3C WebDriver specification that lets you write interchangeable code for all major web browsers. The project is made possible by volunteer contributors. 

### Selenium IDE ###
Integrated Development Environment is the tool you use to develop your Selenium test cases. It's an easy-to-use Chrome and Firefox extension and is generally the most efficient way to develop test cases. It records the users' actions in the browser for you, using existing Selenium commands, with parameters defined by the context of that element. This is not only a time-saver but also an excellent way of learning Selenium script syntax.

### Selenium WebDriver ###
If you are beginning with desktop website or mobile website test automation, then you are going to be using WebDriver APls. WebDriver uses browser automation APls provided by browser vendors to control browser and run tests. This is as if a real user is operating the browser. Since WebDriver does not require its API to be compiled with application code, it is not intrusive. Hence, you are testing the same application which you push live.

### Selenium Grid ###
Selenium Grid allows you to run test cases in different machines across different platforms. The control of triggering the test cases is on the local end, and when the test cases are triggered, they are automatically executed by the remote end. After developing the WebDriver tests, you may face the need to run your tests on multiple browser and operating system combinations. This is where Grid comes into the picture.

## Selenium Webdriver ##

![Selenium Webdriver](./Lambdatest%20JSON-Wire-Protocol-in-Selenium-WebDriver.png)

WebDriver is responsible for running and executing the the webdriver steps you define in your Python code.

WebDriver W3C is the newly introduced protocol for Selenium 4. WebDriver W3C Protocol replaces the older Webdriver using JSON Wire protocol which was used in older versions of Selenium. Webdriver W3C has been developed with regards of standards from World Wide Web Consortium, the community which works on web standards development.

Now WebDriver and browsers share the same protocol which means that tests will be executed more consistently between different browsers. With the introduction of the new protocol will considerably reduce test flakiness. Also, this means that the same test code can be used to run tests on all browsers.

The WebDriver is available for many programming languages such as C#, Java, Python, JavaScript, and others. All these language bindings implement the same API. So we have the same methods and commands on all supported languages. 

The WebDriver talks to the Browser driver we define to use in code. It is responsible for controlling the actual browser. Most of the drivers are developed and maintained by the browser vendors. Browser drivers are executable modules that run on the system with the browser itself, not on the system executing the test suite. So the system executing the tests also need to have the specific browser installed to work.

The drivers are specific to the browsers such as ChromeDriver for Google's Chrome, GeckoDriver for Mozilla Firefox, etc. 

Languge specific test frameworks are used together with WebDriver, such as JUnit, NUnit and Pytest. They are used to make assertions, integrate with test runners and visualize test results. 

On top of them, we might create additional high-level test automation frameworks that give us much more power to maintain, write faster, and troubleshoot tests. We will come back to this in a later lecture.

### Webdriver Manager ###
Python library is used to automatically manage browser drivers without having to download and provide the path.  
For now, it supports ChromeDriver, GeckoDriver, lEDriver, OperaDriver, and EdgeChromiumDriver.  
Before Webdriver manager existed we had to manually download the browser drivers and save somewehere on our test machine. Usually in the test project folder or somewehere in the system path.  

So by using the Webdriver Manager it helps us saving time by not manually download new browser driver everytime the browser updates.
It downloads the correct browser driver and version, that is the browser and version you have installed on the system your run the tests on. 


