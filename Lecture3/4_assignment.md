# Assignment 2 #
## What we learned ##
We did not have any assignment after session 2 so in this assignment try combine what we learned up till todays session.

## Assignment ##
This assignment will use either Behave (BDD) or Robot Framework to create some tests. 
Make sure assertions are used in the tests

1. Create a new projects and import relevant libraries/packages for BDD or Robot framework and a assert library you want to use 

2. Create the tests below using any of the above test frameworks

3. Run all testa and create a report of the test result using pytest-html

4. Zip your project for the assignment and send to me or if you rather want to use a Github/Bitbucket repository, give me the link so i can check the code. 

### Test scenario ###
As a user I want to login to my member page and check my messages and when I have checked my messages i should successfully log out again
1. Open the page "https://conrec-infinity-ab.github.io/Selenium-Course/"

2. Login to the page with my username: letmein@gmail.com and password: secretpassword 
   
3. Verify that its a sucessful login by checking the text on signin.html page which your user will land on.  

4. Verify that the members section on the main page index.html is visible after the redirect. 

5. Check if there are any new messages for the user. Check so there are no new messages.

6. Then log out the user again. Check if the user is logged out sucessfully and the members area is not visible any longer

### Advanced ###
**_This assignment you do not need to use any test framework_**

On the main page find all new employees and 
* Print out the names of the new employees to the terminal/console
* Print out the sum of the new employees to the terminal. It should equal 9.

**_Tip_**
Find the main div where all New employees are located start from it to find all employees



Any questions or errors in text, please get back to Peter!



