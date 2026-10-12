import pytest, re
from playwright.sync_api import Page, expect

login_url = "/client"

@pytest.fixture
def login_page(page:Page):
    #fixture can be used repeatedly
    page.goto(login_url)
    return page

@pytest.mark.smoke
def test_successful_login(login_page:Page):
    #Arrange
    page = login_page

    #Act
    page.locator("#userEmail").fill("belgianairways@gmail.com")
    page.locator("#userPassword").fill("Athena123!")
    page.locator("#login").click()

    #Assert
    expect(page.get_by_role("button", name=re.compile("HOME"))).to_be_visible()

@pytest.mark.parametrize(
    ("user_email", "user_password", "error_message"),
    [
        ("belgianairways@gmail.com", "Athena", "Incorrect email or password."),
        ("belgian@gmail.com", "Athena123!", "Incorrect email or password.")

    ],
    ids=["incorrect_password", "incorrect_email"],

)

def test_failed_login(login_page: Page, user_email: str, user_password: str, error_message: str):
    page = login_page
    page.locator("#userEmail").fill(user_email)
    page.locator("#userPassword").fill(user_password)
    page.locator("#login").click()
    expect(page.get_by_role("alert")).to_contain_text(error_message)

def test_empty_fields(login_page:Page):
    page = login_page
    page.locator("#userEmail").fill("")
    page.locator("#userPassword").fill("")
    page.locator("#login").click()
    expect(login_page.get_by_text("Email is required")).to_be_visible()
    expect(login_page.get_by_text("Password is required")).to_be_visible()
