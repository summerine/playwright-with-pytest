from playwright.sync_api import Page, expect
from pytest_bdd import scenarios, given, when, then

scenarios("../features/ecommerce_landing_page.feature")


@given('I access the landing page')
def access_landing_page(page:Page):
    page.goto("/client")

@when('I view the landing page')
def observe_landing_page(page:Page):
    page.screenshot(path="output/loginpage.png", full_page=True)

@then('the landing page title should be displayed')
def verify_landing_page_title(page:Page):
    expect(page).to_have_title("Let's Shop")

@then('the Login button should be displayed')
def verify_login_button(page:Page):
    login_button = page.get_by_role("button", name="Login")
    expect(login_button).to_be_visible()
    login_button.first.screenshot(path="output/login_button.png")
