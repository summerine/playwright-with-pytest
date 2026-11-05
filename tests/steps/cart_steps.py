
from playwright.sync_api import expect, Page
import re


def test_access_cart(logged_in_page:Page):
    cart_button = logged_in_page.get_by_role("button", name="Cart").filter(has_not_text="Add To Cart")
    cart_button.click()
    my_cart = logged_in_page.get_by_role("heading", name="My Cart")
    expect(my_cart).to_be_visible()
    expect(logged_in_page.get_by_role("heading", name="No Products")).to_be_visible()
    #go back to the dashboard page
    continue_shopping_button = logged_in_page.get_by_role("button", name="Continue Shopping")
    continue_shopping_button.click()
    expect(logged_in_page.locator(".card-body").filter(has_text="ADIDAS ORIGINAL")).to_be_visible()

def test_add_item_to_cart(logged_in_page:Page):
    adidas_item = logged_in_page.locator(".card-body").filter(has_text="ADIDAS ORIGINAL")
    adidas_item.get_by_role("button", name="Add To Cart").click()
    cart_button = logged_in_page.get_by_role("button", name="Cart").filter(has_not_text="Add To Cart")
    expect(cart_button.locator("label")).to_have_text("1")
    expect(cart_button).to_contain_text("1")


