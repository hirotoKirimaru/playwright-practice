from playwright.sync_api import Playwright

def test_rakuten(props, playwright: Playwright):
    browser = playwright.chromium.launch()
    page = browser.new_page(
        screen={"width": props.width, "height": props.height},\
    )

    # print(f"username='{props.username}', password='{props.password}'")
    # page.goto("https://www.rakuten-sec.co.jp/")
    # index = 0
    # page.screenshot(path=f'example-{index}.png')
    

    page.goto(f"{props.url}/tutorial")
    page.screenshot(path=f'tutorial-{props.section}.png', full_page=True)

    # pytest --browser chromium --browser webkit --browser firefox