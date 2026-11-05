from playwright.sync_api import Page, expect
from pytest_bdd import scenarios, given, when, then, parsers

scenarios("../features/ecommerce_login_failed.feature")


@given('I access the ecommerce landing page')
def ecommerce_login_page(page: Page):
    page.goto("/client")
    return page

@when(parsers.parse('I enter "{user_email}" and "{user_password}"'))
def enter_credentials(login_page: Page, user_email: str, user_password: str):
    login_page.locator("#userEmail").fill(user_email)
    login_page.locator("#userPassword").fill(user_password)

@when('I click Login button')
def click_login_button(login_page: Page):
    login_page.get_by_role("button", name="Login").click()
    

@then(parsers.parse('An error notification "{error_message}" should be displayed'))
def verify_error_notification(login_page: Page, error_message: str):
    expect(login_page.get_by_role("alert")).to_contain_text(error_message)