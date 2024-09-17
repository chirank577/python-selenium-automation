# Created by chiranjivisingh at 9/13/24
Feature: cart tests features



  Scenario: user can verify if cart is empty
    Given open target main page
    When click on cart icon
    Then Your cart is empty message is shown


  Scenario: verify user can add product into the cart
    Given open target main page
    When search for a tea
    And click add to cart button
    And click on view cart & check out
    Then verify cart has 1 items or total price