import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        for browser_type in [p.chromium, p.firefox, p.webkit]:
            # Dockerでは画面描画する機能はないので、Docker上で開発するのは現実的ではない
            browser = await browser_type.launch(headless=True)
            page = await browser.new_page()
            await page.goto('http://whatsmyuseragent.org/')
            await page.screenshot(path=f'example-{browser_type.name}.png')
            await browser.close()

asyncio.run(main())