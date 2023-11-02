# Define the function to wrap your provided code
import asyncio

import httpx
from pyppeteer import launch
from pyppeteer.browser import Browser
from pyppeteer.page import Page

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


async def fetch_content_lishui(url: str) -> str:
    browser: Browser = await launch()
    page: Page = await browser.newPage()
    await page.goto(url)
    frames = page.frames
    # TODO: paramize rule
    iframe = next(frame for frame in frames if frame.name == 'xxgk_col_iframe')
    content = await iframe.content()
    await browser.close()
    return content


async def fetch_content_fzggw(url: str) -> str:
    async with httpx.AsyncClient(http2=True) as client:
        response = await client.get(url, headers=headers)
        response.encoding = 'utf-8'
    return response.text


async def fetch_content_jinhua(url: str) -> str:
    async with httpx.AsyncClient(http2=True) as client:
        response = await client.get(url, headers=headers)
        response.encoding = 'utf-8'
    return response.text


if __name__ == '__main__':
    # run first to download core
    asyncio.run(fetch_content_lishui(
        'https://www.lishui.gov.cn/col/col1229265119/index.html?df=/col/col1229283449/index.html&isgk=1'))
