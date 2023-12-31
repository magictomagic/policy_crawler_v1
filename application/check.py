import asyncio
import logging
from datetime import datetime
from typing import Callable

from feedgenerator import Atom1Feed
from tortoise.transactions import atomic

from domain.rule.detail_filter.raw2detail import r2d_jiaxing
from domain.rule.mapping.abstract_mapping import filter_rule_lishui, \
    filter_rule_fzggw, filter_rule_jiaxing
from domain.rule.rule_compose import aurl2detail_models, aurl2abstract_models1
from infrastructure.entity.policy import NewsAbstract, NewsDetail

logger = logging.getLogger(__name__)


@atomic()
async def check_inert_abstracts(mapping_rule: dict, detail_rule: Callable[[str], dict]):
    logger.info("mapping_rule: " + str(mapping_rule))
    stored_abstract_list, online_abstract_list = await asyncio.gather(
        NewsAbstract.filter(abstract_entrance=mapping_rule.get("url")),
        aurl2abstract_models1(**mapping_rule)
    )
    isto_update_abstract_list = list(set(online_abstract_list) - set(stored_abstract_list))
    if len(isto_update_abstract_list) == 0:
        return None
    await asyncio.gather(
        NewsAbstract.bulk_create(isto_update_abstract_list),
        inert_details(isto_update_abstract_list, detail_rule)
    )
    return isto_update_abstract_list


async def inert_details(news_abstracts: list[NewsAbstract], raw2detail: Callable[[str], dict]):
    news_abstracts = await aurl2detail_models([news_abstract.href for news_abstract in news_abstracts], raw2detail)
    await NewsDetail.bulk_create(news_abstracts)


async def test111():
    model = await aurl2abstract_models1(**filter_rule_lishui)
    await asyncio.gather(NewsAbstract.bulk_create(model))
    # print(model)
    # if model is not None:
    #     await NewsAbstract.bulk_create(model)
    # else:
    #     print("No models to create.")
    return
    # await NewsAbstract.bulk_create(model)


async def test_on_get():

    # await check_inert_abstracts(test_filter_rule)
    # await check_inert_abstracts(filter_rule_fzggw, r2d_fzggw_1)
    # await check_inert_abstracts(filter_rule_lishui, r2d_lishui)
    # await check_inert_abstracts(filter_rule_jinhua, r2d_jinhua)
    await check_inert_abstracts(filter_rule_jiaxing, r2d_jiaxing)


async def show_atom3():
    feed = Atom1Feed(
        title="News Abstracts",
        link="http://example.com/news/",
        description="A feed of news abstracts.",
        language="en",
    )
    news_abstracts = await NewsAbstract.filter(abstract_entrance=filter_rule_fzggw.get("url"))
    for news in news_abstracts:
        feed.add_item(
            title=news.title,
            link=news.href,
            description=news.abstract_entrance,
            pubdate=news.created_at if news.created_at else datetime.now(),
            updateddate=news.update_at if news.update_at else datetime.now(),
        )
    atom_string = feed.writeString('utf-8')
    return atom_string
