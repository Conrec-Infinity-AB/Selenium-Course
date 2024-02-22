# Test automation with Selenium
_This is the main repository for the course Test automation with Selenium created by Conrec Infinity where we will learn how to use Selenium and Python to test web pages._

Installation instructions will be targeted for the Windows platform but using Mac OSX or Linux will also work. Some instruktions will need som tweaking. The examples and lectures will focus on Python but can be applied to other languages like C# and Java too.

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

After we have openend our Selenium_Course project In visual Studio Code, open the Command Palette by using **_CTRL + SHIFT + P_** or selecting it in the **_View Menu_** 

Search for **_Python: Create Environment.._** and select it.

In the dropdown select the option **_Venv_** 

Select the **_Python 3.x.y_** Python interpreter.

Select the **_requirements.txt_** file and **_OK_**

The virtual environment will be created and the Python packages used in this course will be downloaded.

