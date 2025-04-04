# Test automation with Selenium
_This is the main repository for the course Test automation with Selenium created by Conrec Infinity where we will learn how to use Selenium and Python to test web pages._

Installation instructions will be targeted for the Windows platform but using Mac OSX or Linux will also work. Some instructions will need some tweaking. The examples and lectures will focus on Python but can be applied to other languages like C# and Java too.

## Python and tools setup for Windows

### Python 3

Download the Python executable from http://python.org and run setup. 

Select **_Install Now_** to install and use default installation path and options or select Customize installation if you want to customize the settings. Select the option **_Add python.exe to PATH_** so we can use Python from any folder location later on.

Verify Python setup by opening a Command prompt or Powershell terminal and write the following commands:

> python --version

Result: Python 3.x.y

> pip --version

Result: pip 2x.y.z

### GIT
Download GIT (64-bit version) from https://www.git-scm.com and run setup. There is a lot of options but I recommend to use default options for now.

Verify GIT setup by opening a command prompt or Powershell terminal and write the following commands:

> git --version

Result: git version 2.x.y

Optional - Setup your name and e-mail to use when pushing code to a repository:

> git config --global user.name "Your name"

> git config --global user.email your@email.xyz

### Visual Studio Code
Download the VSCode executable from https://code.visualstudio.com and run setup. 

Default options is enough but if you want to start VS Code from any folder location then select the option **_Add to PATH (requires shell restart)_**.

Start Visual Studio Code and click on the extensions to the left of VS Code window and search for **_Python_** and install the Python extension from Microsoft - IntelliSense (Pylance) ... 

Also install the **_Live Server_** extension which will be used to test local web pages.

## Clone and open repository
Open a command prompt or Powershell terminal and create a folder where you want the Selenium project to reside:

> mkdir ConrecInfinity

> cd ConrecInfinity

Run the following command to download this repository:

> git clone https://github.com/Conrec-Infinity-AB/Selenium-Course.git

A warning will appear, just answer **_Yes_** to the question.

_The authenticity of host 'github.com (140.82.121.3)' can't be established._

_Are you sure you want to continue connecting (yes/no/[fingerprint])?_

In VS Code select Open folder and select the folder **_Selenium-Course_** where the repository was cloned to.

If a warning is visible about trust of the files and folder is visible then select **_Yes, I trust the authors_**.

## Setup a local Python virtual environment and download Selenium related packages
When we work with different Python projects it's always a good practise to create a virtual environment for the project we are working with so we don't install Python packages globally.

After we have openend our Selenium-Course project In visual Studio Code, open the Command Palette by using **_CTRL + SHIFT + P_** or selecting it in the **_View Menu_** 

Search for **_Python: Create Environment.._** and select it.

In the dropdown select the option **_Venv_** 

Select the **_Python 3.x.y_** Python interpreter.

Select the **_requirements.txt_** file and **_OK_**

The virtual environment will be created and the Python packages used in this course will be downloaded.

## Test setup
Open the file **_./Lecture1/code/1_openingPage.py_** and run it by selecting **_Run / Run without debugging_** in the menu. If everything is setup correct then a Chrome web browser should open and close.

The text below should be visible in Viual Studio Code terminal:

> Title is: Home Page

## Links ##
- [Course recordings](https://conrecinfinity2021.sharepoint.com/sites/Education/_layouts/15/SeeAll.aspx?Page=%2Fsites%2FEducation%2FSitePages%2FSelenium-med-Python-3.aspx&InstanceId=ab3b5721-f10c-4d97-8b34-a64e8647eaae) Here you find all the recordings from lessons 1-3(4). Note that you need to be logged in to Conrec Office 365.  
 
- [Our test site online](https://conrec-infinity-ab.github.io/Selenium-Course) This is hosted on Githubs pages. Will be redeployed every time we check in code in this repository. This is the site we will run our test on.
- [Our test site offline](http://127.0.0.1:5500/docs/index.html) Use the extension Live Server and start index.html page in the ./docs folder. Use this one if you are offline or want to test changes locally before commiting to the repository. 

- [Selenium documentation](https://www.selenium.dev/documentation/) Everything related to Selenium APi and Grid and more
- [Python language bindings for Selenium WebDriver](https://www.selenium.dev/selenium/docs/api/py/api.html#) Python bindings for Selenium 4
- [Selenium with Python](https://selenium-python.readthedocs.io/index.html) Good site for more examples, API calls and exceptions and more

- [Python documentation](https://docs.python.org/3/) Everything related to the Python language 
- [Python Package Index](https://pypi.org) The repository for Python packages which can be imported, including instructions how to install them with the **_pip_** command
- [Pytest documentation](https://docs.pytest.org/en/8.0.x/how-to/index.html) Here you find everything related to Pytest

- [Selenium Package](https://pypi.org/project/selenium/) Selenium Pip install instructions and basic usage examples
- [Virtual environments](https://docs.python.org/3/library/venv.html) How to setup and use virtual environments in Python 

- [Google DevTools](https://developer.chrome.com/docs/devtools) Googles developer tool used in Chrome webbrowser. A tool you should be comfortable with when writing Selenium tests
- [Google Chrome command switches](https://peter.sh/experiments/chromium-command-line-switches/) A comprehensive list of command options for Google Chrome

- [Softwaretestingboard](https://magento.softwaretestingboard.com) A site which can be used for tests 
- [Saucedemo](https://www.saucedemo.com/) Another site which can be used for running tests against 


