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

Organizing all tests in a test folder with sub folders is a good practise and Pytest will consider all the files as test files. 

Run all tests in the test folder and its sub folders
> pytest test/

It is also possible to run individual test files by explicitly mentioning thir file names. 
> pytest test/test_login.py test/test_logout.py -v -s

**_-v -s_** is used to show more verbose output and print both stdout and stderr to the terminal.

### Test functions
Pytest also looks for functions with the prefix "test_". 

For example a test function 

> def test_validate_email(): 

This makes it easy to identify and run tests in Pytest.

If we want to run one or more test files we can mention by them by their file names.
> pytest test/test_login.py test/test_logout.py -v -s

And if we want to find and run all tests with some text in their their names or function names, we can do that too. 

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
@pytest.mark.xfail(reason="Expected to fail until we fix the bug."
def test_login_username():
    ... assert something ...   
```


## Behave

## Robot Framework
