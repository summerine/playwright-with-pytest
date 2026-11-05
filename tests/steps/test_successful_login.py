from playwright.sync_api import Page, expect
from pytest_bdd import scenarios, given, when, then
import re


scenarios("../features/ecommerce_login_successful.feature")


@given('I access the ecommerce landing page')
def ecommerce_login_page(page:Page):
    page.goto("/client")
    return page


@when('I enter a valid email and a valid password')
def do_login_proces(login_page:Page, client_useremail, client_userpassword):
    login_page.locator("#userEmail").fill(client_useremail)
    login_page.locator("#userPassword").fill(client_userpassword)


@when('I click Login button')
def click_login_button(login_page:Page):
    login_page.get_by_role("button", name="Login").click()


@then('I should be redirected to the homepage')
def verify_successful_login(login_page:Page):
    expect(login_page.get_by_role("button", name=re.compile("HOME"))).to_be_visible()