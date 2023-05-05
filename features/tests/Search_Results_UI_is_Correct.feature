Feature: Search Results UI is correct


  Scenario: First result correct when search "Cure"
    Given User navigates to search results from url
    Then Verify the first product has a name, image, and price
