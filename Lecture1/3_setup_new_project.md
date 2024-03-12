# Lecture 1 - Setup a new Selenium project from scratch with Python # 

## Project location ##
Create a folder where you want to save your Selenium project

In Visual Studio Code open the recently created Selenium project folder. An empty project is created. So now we need to start setup the Python environment to work with. 

## Setup a local Python virtual environment ## 
As we seen in the README file, we created a virtual environment for our Selenium project. It's always a good practise to create a virtual environment for the project we are working with so we don't install Python packages globally. Here we will use Visual Studio again to create the virtual environment. But it is also possible to create a virtual environment in the Console/Terminal. We will look at that later on.

In visual Studio Code, open the Command Palette by using **_CTRL + SHIFT + P_** or selecting it in the **_View Menu_** 

Search for **_Python: Create Environment.._** and select it.

In the dropdown select the option **_Venv_** 

Select the **_Python 3.x.y_** Python interpreter.

Visual Studio Code will start to setup the new virtual environment and after a while a message is visible that the virtual environment is created and used. 

The difference this time is that we do not get any question about loading a requirements.txt file because it does not exist yet. We will add packages manually to our project.

## Install Selenium related Python packages ##
Make sure the Terminal in Visual Studio is visible else open it in the View menu.

In the terminal enter the folowing command:
> pip list

Result should be something like the following:

Package Version  
pip     24.0

This indicates that there are no Python packages installed in the projects virtual environment except for *_pip_* which we will use to install new packages.

### Python Package Repository - Selenium package ###
We will start by installing the Selenium package. Open up a web browser and go to the following URL https://pypi.org/project/selenium/

This page is the official Python package reository. When working with Python this repository will be used a lot.

The specific page we opened is for the Selenium package. Here you can read how to install the package and it's documentation.

Copy the command *_pip install selenium_* in the page and paste in Visual Studio Codes terminal and run it.

Python will start downloading the Selenium package and all referenced packages which Selenium is depending on. It will take a few seconds to install all the packages.

When done run the following command again:
> pip list

This time the result should be a long list of packages. 

Good everything needed to use selenium should be setup now! 

If you also want to use test framework libraries like *_Pytest*_ https://pypi.org/project/pytest/ then also run  
> pip install pytest

### Verify setup ###
In the VS Code project create a new Python file named *_main.py_*

Copy the contents from Lecture1/code/1_openingPage.py and paste it in the new file and save.
>from selenium import webdriver
>
>driver = webdriver.Chrome()
>
>driver.get("https://magento.softwaretestingboard.com")
>
>print("Title is: " + driver.title)
>
>driver.quit()

Now run the file to see that everything works as expected. Click the Run icon above the code to the right (or menu *_Run/Run without debugging_*) and wait for a Chrome browser to open and runs the Selenium commands. 

After a while the text:  
Title: Home Page  
should be visible in the terminal

Great thats it! You have setup a new Selenium project. 

### Create requirements.txt file ###
If we want to share our project with someone else, or we want to always use the same versions of a package we can use a requirements.txt file.

Packages updates quite often and a bug or change in behaviour can occur between versions. Using a file like requirements.txt which contains the packages and its versions will make sure that we all work with same package setup. Thats why we used the requirements.txt file in the main project setup. 

If we want to create our own requirements.txt file then its a simple command we can use. In the terminal of the project we want to save our packages from, enter the following command
> pip freeze > requirements.txt

Now a new file will be visible in the project folder. If you open it, it will contain all packages and their versions used in the project. So now we can commit and push this file with the project to a repository and when someone else opens the project they can load the requirements.txt file and do not need to manually install packages.

To load the packages, select it when creating a virtual environment in VS Code, or use the command to install all packages in terminal
> pip install -r requirements.txt

More information about pip and its command reference can be found at https://pip.pypa.io/en/stable/cli/pip_install/

### Advanced - Setting up a virtual environment in terminal ###
If you are not using any IDE like VS Code the you can setup a virtual environment in terminal (Powershell). Below we create a virtual environment named *_.venv_* in a folder. Make sure you setup the virtual environment before  you install any packages so the packages will be installed in the virtual environment.
 
> python -m venv .venv

Activate the new virtual environment
>  .\.venv\scripts\activate 

The terminal will now indicate that you use the new virtual environment by prefixing the prompt with (.venv)

To decativate a virtual environment use the following command	
> deactivate

Now the terminal prompt will change back to normal prompt without the (.env)

More information about virtual environments can be found at https://docs.python.org/3/library/venv.html