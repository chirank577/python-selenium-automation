Feature: target search feature steps


  @smoke
  Scenario: verify that user is able to search a product on target main page
    Given open target main page
    When search for a Blanket
    Then Verify that correct product is shown for Blanket


  @smoke
  Scenario: verify user can see target circle page has 10 benefit cells
  Given open target circle page
  Then verify circle page includes 10 benefits


Scenario: Verify user can see all the product name and image
  Given open target main page
  When search for a tshirt for woman
  Then Verify that every product on Target has a product name and product image



  Scenario: verify user can see favourite tooltip for search result
     Given open target main page
     When search for a coffee
     And Hover favourites icon
     Then Favourites tooltip is shown

