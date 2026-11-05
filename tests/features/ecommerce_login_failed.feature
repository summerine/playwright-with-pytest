Feature: Ecommerce Failed Login
    The user unable to login to their account

Scenario Outline: Login with invalid credentials
    Given I access the ecommerce landing page
    When I enter "<user_email>" and "<user_password>"
    And I click Login button
    Then An error notification "<error_message>" should be displayed

    Examples: Incorrect email
        | user_email         | user_password | error_message                |
        | belgiana@gmail.com | Athena123!    | Incorrect email or password. |

    Examples: Incorrect password
        | user_email               | user_password | error_message                |
        | belgianairways@gmail.com | Athena        | Incorrect email or password. |

    Examples: Incorrect email and password
        | user_email               | user_password | error_message                |
        | belgiana@gmail.com       | Athena        | Incorrect email or password. |
