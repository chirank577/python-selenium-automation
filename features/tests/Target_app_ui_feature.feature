# Created by chiranjivisingh at 9/29/24
Feature: test for target terms and condition

  Scenario: User can open and close Terms and Conditions from sign in page
    Given open target main page
    When click on sign in logo and click sign in on account page
    And Store original window
    And Click on Target terms and condition link
    And switch to the newly opened window
    Then Verify terms and condition page is opened
    And  close current window
    And return to original window

