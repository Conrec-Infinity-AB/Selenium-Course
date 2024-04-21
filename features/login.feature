Feature: Login functionality
  As a user,
  I want to be able to log in to the application,
  So that I can access my account.
  
  Background:
    Given I am on the main page

  Scenario: Valid credentials
    When I enter valid "letmein@gmail.com" and "secretpassword"
    And I click the login button
    Then I should see the login status page
    And I close the browser

  Scenario: Invalid credentials
    When I enter invalid username and password
    And I click the login button
    Then I should see an error message
    And I close the browser


  Scenario Outline: Multiple credentials
    When I enter valid "<username>" and "<password>"
    And I click the login button

    Examples:
      |username                   |password           |
      |letmein@gmail.com          |secretpassword     |
      |letmein@gmail.com          |wrongpassword      |
      |admin@gmail.com            |secretpassword     |
       