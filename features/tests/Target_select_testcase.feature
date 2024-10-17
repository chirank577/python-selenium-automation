# Created by chiranjivisingh at 10/3/24
Feature: Test case for drop down on target Help page

  Scenario: User can select Help topic Partner Programs
#    Given open target Help page
    Given open target main page
    When Click on Target Help at the bottom of the page
    When scroll down on Holiday Help
    And Click on Holiday Help under holiday help
    Then Verify Holiday Help page is open
    When Select Help topic Target Account
    Then Verify Create account page is open
#
    Scenario: User can select Promotions & Coupons option
#    Given open target Help page
    Given open target main page
    When Click on Target Help at the bottom of the page
    When scroll down on Holiday Help
    And Click on Holiday Help under holiday help
    Then Verify Holiday Help page is open
    When Select Help topic Promotions & Coupons
    Then Verify Current promotions page is open
