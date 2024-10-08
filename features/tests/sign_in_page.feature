Feature: target main page sign in 


  Scenario: verify that a logged out user can navigate to Sign In page
    Given open target main page
    When click on sign in logo and click sign in on account page
    Then Verify Sign In form opened


  Scenario: verify that user can sign in using Id and Password
    Given open target main page
    When click on sign in logo and click sign in on account page
    And click on email chirank577@gmail.com and enter email address
    And click on password **********  enter valid password
    And click on sign in with password
    Then Verify user can sign in using valid email address and password

Scenario: verify that user is unable to sign in using invalid Id or invalid Password
    Given open target main page
    When click on sign in logo and click sign in on account page
    And click on email chirank57@gmail.com and enter invalid email address
    And click on password *********** enter invalid password
    And click on sign in with password
    Then Verify user can not sign in using invalid email address or password