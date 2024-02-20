# Test automation with Selenium
_This is the main repository for the course Test automation with Selenium created by Conrec Infinity_

Main programming language in this course will be Python. In some of the lectures there will be examples in other languages too.

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
