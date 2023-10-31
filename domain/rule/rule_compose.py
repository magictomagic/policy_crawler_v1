import asyncio
from typing import Callable, Coroutine, Awaitable
import httpx
import bs4.element
import logging
from infrastructure.config.field_name import pg_href, pg_abstract_entrance
from infrastructure.entity.policy import NewsAbstract, NewsDetail
from urllib.parse import urljoin, urlparse

logger = logging.getLogger(__name__)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


def construct_absolute_url(base, link):
    # First, check if the link is already an absolute URL
    if bool(urlparse(link).netloc):
        return link

    # If not, join the base URL with the relative link to create the absolute URL
    return urljoin(base, link)


async def aurl2abstract_models1(url: str,
                                afetch_content: Callable[[str], Awaitable[str]],
                                parse_content: Callable[[str], list[dict]]) -> list[NewsAbstract]:
    abstr_entrance_list = parse_content(await afetch_content(url))
    news_abstract_list = []
    for abstr_entrance in abstr_entrance_list:
        abstr_entrance[pg_href] = construct_absolute_url(url, abstr_entrance[pg_href])
        abstr_entrance[pg_abstract_entrance] = url
        news_abstract_list.append(NewsAbstract(**abstr_entrance))
    return news_abstract_list


async def aurl2detail_model(url: str,
                            raw2dtl: Callable[[str], dict]) -> NewsDetail:
    """
    rule config at domain/rule/detail_filter

    :param raw2dtl:
    :param url:
    :return:
    """
    async with httpx.AsyncClient(http2=True, follow_redirects=True) as client:
        response = await client.get(url, headers=headers)
        response.encoding = 'utf-8'
        dtl = raw2dtl(response.text)
        return NewsDetail(**dtl, href=url)


async def aurl2detail_models(urls: list[str],
                             raw2dtl: Callable[[str], dict]) -> list[NewsDetail]:
    tasks = [aurl2detail_model(url, raw2dtl) for url in urls]
    return await asyncio.gather(*tasks)
