from playwright.sync_api import Page

def test_rakuten(props, page: Page):
    # print(f"username='{props.username}', password='{props.password}'")
    # page.goto("https://www.rakuten-sec.co.jp/")
    # index = 0
    # page.screenshot(path=f'example-{index}.png')
    

    page.goto("http://7dc9-240f-6d-3fea-1-d095-fe1c-71d9-3d7b.ngrok.io/tutorial")
    page.screenshot(path=f'test.png', full_page=True)

    # pytest --browser chromium --browser webkit --browser firefox