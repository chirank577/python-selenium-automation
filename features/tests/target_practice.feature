# Created by chiranjivisingh at 9/12/24
Feature: target main page testing

  Scenario: user can verify if cart is empty
    Given open target main page
    When click on cart icon
    Then Your cart is empty message is shown



  Scenario: verify that a logged out user can navigate to Sign In page
    Given open target main page
    When click on sign in logo
    And click Sign In
    Then Verify Sign In form opened





