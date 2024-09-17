Feature: target search feature steps


  Scenario: verify that user is able to search a product on target main page
    Given open target main page
    When search for a Blanket
    Then Verify that correct product is shown for Blanket


Scenario: verify user can see target circle page has 10 benefit cells
  Given open target circle page
  Then verify circle page includes 10 benefits