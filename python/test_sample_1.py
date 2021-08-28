from playwright.sync_api import Page

def test_rakuten(props, page: Page):
    print(f"username='{props.username}', password='{props.password}'")
    page.goto("https://www.rakuten-sec.co.jp/")
    index = 0
    page.screenshot(path=f'example-{index}.png')