from playwright.sync_api import Page

import configparser

# --------------------------------------------------
# configparserの宣言とiniファイルの読み込み
# --------------------------------------------------
config_ini = configparser.ConfigParser()
config_ini.read('config.ini', encoding='utf-8')

read_default = config_ini['DEFAULT']
username = read_default.get('username')
password = read_default.get('password')

print(f"username='{username}', password='{password}'")


def test_rakuten(page: Page):
    page.goto("https://www.rakuten-sec.co.jp/")
    index = 0
    page.screenshot(path=f'example-{index}.png')