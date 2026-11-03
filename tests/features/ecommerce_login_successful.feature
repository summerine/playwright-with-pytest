Feature: Ecommerce Login
    The user should be able to login to their account

Scenario: Login to the account should be successful
    Given I access the ecommerce landing page
    When I enter a valid email and a valid password
    And I click Login button
    Then I should be redirected to the homepage