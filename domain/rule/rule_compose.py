import asyncio
from typing import Callable
import httpx
import bs4.element
import logging
from domain.rule.abstract_filter.json2obj import construct_absolute_url
from infrastructure.config.field_name import pg_href, pg_abstract_entrance
from infrastructure.entity.policy import NewsAbstract, NewsDetail

logger = logging.getLogger(__name__)

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}


def compose2dict(raw_response_text: str,
                 raw2pro: Callable[[str], bs4.element.Tag],
                 pro2raw_list: Callable[[bs4.element.Tag], list[bs4.element.Tag]],
                 raw2json: Callable[[bs4.element.Tag], dict]) -> list[dict]:
    processible_tag = raw2pro(raw_response_text)
    raw_list = pro2raw_list(processible_tag)
    abstr_entrance_list = []
    for raw in raw_list:
        abstr_json = raw2json(raw)
        abstr_entrance_list.append(abstr_json)
    return abstr_entrance_list


def url2model(url: str,
              raw2pro: Callable[[str], bs4.element.Tag],
              pro2raw_list: Callable[[bs4.element.Tag], list[bs4.element.Tag]],
              raw2json: Callable[[bs4.element.Tag], dict]) -> list[NewsAbstract]:
    response = httpx.get(url, headers=headers)
    response.encoding = 'utf-8'
    abstr_entrance_list = compose2dict(response.text, raw2pro, pro2raw_list, raw2json)
    news_abstract_list = []
    for abstr_entrance in abstr_entrance_list:
        abstr_entrance[pg_href] = construct_absolute_url(url, abstr_entrance[pg_href])
        abstr_entrance[pg_abstract_entrance] = url
        news_abstract_list.append(NewsAbstract(**abstr_entrance))

    print(abstr_entrance_list)
    print(len(abstr_entrance_list))
    return news_abstract_list


async def aurl2abstract_models(url: str,
                               raw2pro: Callable[[str], bs4.element.Tag],
                               pro2raw_list: Callable[[bs4.element.Tag], list[bs4.element.Tag]],
                               raw2json: Callable[[bs4.element.Tag], dict]) -> list[NewsAbstract]:
    """
    rule config at domain/rule/abstract_filter

    :param url:
    :param raw2pro:
    :param pro2raw_list:
    :param raw2json:
    :return:
    """
    async with httpx.AsyncClient(http2=True) as client:
        response = await client.get(url, headers=headers)
        response.encoding = 'utf-8'
        abstr_entrance_list = compose2dict(response.text, raw2pro, pro2raw_list, raw2json)
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
        logger.info("url", url)
        return NewsDetail(**dtl, href=url)


async def aurl2detail_models(urls: list[str],
                             raw2dtl: Callable[[str], dict]) -> list[NewsDetail]:
    tasks = [aurl2detail_model(url, raw2dtl) for url in urls]
    return await asyncio.gather(*tasks)


def compose2model(json2obj: Callable[[dict], NewsAbstract]) -> NewsAbstract:
    pass
