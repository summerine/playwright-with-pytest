from playwright.sync_api import Page, expect


def test_ecommerce_page_login(page:Page):
    page.goto("/client")

    expect(page).to_have_title("Let's Shop")
    print("Page Title:", page.title())
    expect(page.get_by_role("heading", name="Log in")).to_be_visible()

    page.screenshot(path="output/loginpage.png", full_page=True)
    page.get_by_role("heading", name="Log in").first.screenshot(path="output/login.png")
