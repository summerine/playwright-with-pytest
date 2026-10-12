from pathlib import Path

from playwright.sync_api import Page, expect


def test_search_item(page:Page, tmp_path:Path):
    page.goto("/client")
    page.locator("#userEmail").fill("belgianairways@gmail.com")
    page.locator("#userPassword").fill("Athena123!")
    page.locator("#login").click()
    expect(page.get_by_role("textbox", name="Search")).to_be_visible()
    page.get_by_role("textbox", name="Search").fill("ADIDAS ORIGINAL")
    page.get_by_role("textbox", name="Search").press("Enter")
    expect(page.get_by_role("heading", name="ADIDAS ORIGINAL")).to_be_visible()

    #temporary image
    #image = tmp_path/"adidas_image.png"
    #page.screenshot(path=image)
    #assert image.exists()

    page.screenshot(path="output/adidas_shoes_search_result1.png", full_page=True)

