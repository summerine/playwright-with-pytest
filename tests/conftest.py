import pytest
import os
from dotenv import load_dotenv
from playwright.sync_api import Page

load_dotenv()

BASE_URL = os.getenv["BASE_URL"]
CLIENT_USEREMAIL = os.getenv["CLIENT_USEREMAIL"]
CLIENT_USERPASSWORD = os.getenv["CLIENT_USERPASSWORD"]

@pytest.fixture
def login_page(page:Page):
    page.goto(BASE_URL)
    return page

@pytest.fixture
def logged_in_page(login_page:Page):
    login_page.locator("#userEmail").fill(CLIENT_USEREMAIL)
    login_page.locator("#userPassword").fill(CLIENT_USERPASSWORD)
    login_page.locator("#login").click()
    return login_page

