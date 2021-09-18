from playwright.sync_api import Playwright
import os

def test_rakuten(props, playwright: Playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page()
    # print(f"username='{props.username}', password='{props.password}'")
    # page.goto("https://www.rakuten-sec.co.jp/")
    # index = 0
    # page.screenshot(path=f'example-{index}.png')

    print("*******")
    print(os.environ.get('ENV'))
    print(os.environ.get('ENV2'))
    

    page.goto("http://7dc9-240f-6d-3fea-1-d095-fe1c-71d9-3d7b.ngrok.io/tutorial")
    page.screenshot(path=f'test.png', full_page=True)

    # pytest --browser chromium --browser webkit --browser firefox