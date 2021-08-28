from playwright.sync_api import Page

def test_rakuten(page: Page):
    page.goto("https://www.rakuten-sec.co.jp/")
    index = 0
    page.screenshot(path=f'example-{index}.png')