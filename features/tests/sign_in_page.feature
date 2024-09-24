Feature: target main page sign in 


  Scenario: verify that a logged out user can navigate to Sign In page
    Given open target main page
    When click on sign in logo
    And click Sign In
    Then Verify Sign In form opened

