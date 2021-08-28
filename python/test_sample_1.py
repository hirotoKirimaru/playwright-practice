from playwright.sync_api import Page
from TestProperties import TestProperties

props = TestProperties()

print(f"username='{props.username}', password='{props.password}'")


def test_rakuten(page: Page):
    page.goto("https://www.rakuten-sec.co.jp/")
    index = 0
    page.screenshot(path=f'example-{index}.png')