import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        for browser_type in [p.chromium]:
            page = None
            try:
                # Dockerでは画面描画する機能はないので、Docker上で開発するのは現実的ではない
                browser = await browser_type.launch(headless=True)
                page = await browser.new_page()
                # await page.goto('http://whatsmyuseragent.org/')
                # await page.screenshot(path=f'example-{browser_type.name}.png')

                await page.goto('https://github.com/hirotoKirimaru')
                index=0
                await page.screenshot(path=f'example-{index}.png')

                await page.click("//a[contains(@href, 'repositories')]")
                index+=1
                await page.screenshot(path=f'example-{index}.png')

                await page.fill("//input[@id='your-repos-filter']", 'practice')
                index+=1
                await page.screenshot(path=f'example-{index}.png')
                

                await page.click('xpath=(//a[contains(@href,"practice")])[2]')
                index+=1
                await page.screenshot(path=f'example-{index}.png')




                await browser.close()
            except Exception as e: 
                print(e)
                await page.screenshot(path=f'error.png')


asyncio.run(main())