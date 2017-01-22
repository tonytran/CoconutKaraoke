Feature: Index page Testing
  In order to test pages
  as a user
  I need to demo the app

  Scenario: Choose Genre
    Given I am on the homepage
    When I choose a genre
    And click the submit button on the homepage
    Then I am redirected to the lyrics page

