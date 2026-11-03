Feature: Ecommerce Landing Page
    The landing page title and Login button should be displayed

Scenario: Observe the landing page
    Given I access the landing page
    When I view the landing page
    Then the landing page title should be displayed
    And the Login button should be displayed

