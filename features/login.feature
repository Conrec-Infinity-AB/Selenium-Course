Feature: Login functionality
  As a user,
  I want to check so invalid logins does not log in the user in to the application,
  
  Background:
    Given I am on the main page

   Scenario: Invalid credentials
    When I enter invalid username and password
    And I click the login button
    Then I should see an error message
    And I close the browser


  Scenario Outline: Multiple invalid credentials
    When I enter invalid "<username>" and "<password>"
    And I click the login button
    Then I should see an error message
    And I close the browser

    Examples:
      |username                   |password           |
      |letmein@gmail.com          |wrongpassword      |
      |admin@gmail.com            |secretpassword     |
       