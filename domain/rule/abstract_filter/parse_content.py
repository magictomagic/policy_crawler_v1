import re

import bs4.element
from bs4 import BeautifulSoup

from infrastructure.config.field_name import pg_title, pg_href, pg_time

title_pattern = re.compile(r'title="([^"]+)"')
href_pattern = re.compile(r'href="([^"]+)"')
time_pattern = re.compile(r'(\d{4}-\d{2}-\d{2})')


def parse_content_lishui(content: str) -> list[dict]:
    soup = BeautifulSoup(content, 'lxml')
    element = soup.find(name='div', id='8022060').find(name='table', class_="xxhk_gfx_list")
    data_list = element.find_all('tr')
    return list_raw2dict(data_list)


def parse_content_fzggw(content: str) -> list[dict]:
    soup = BeautifulSoup(content, 'lxml-xml')
    ancestor_div = soup.find(name='div', id='4892867')
    data_content = ancestor_div.find_all('record')
    return list_raw2dict(data_content)


def parse_content_jinhua(content: str) -> list[dict]:
    soup = BeautifulSoup(content, 'lxml-xml')
    ancestor_div = soup.find(name='div', id='7723124')
    data_content = ancestor_div.find_all('record')
    return list_raw2dict(data_content)


def parse_content_jiaxing(content: str) -> list[dict]:
    soup = BeautifulSoup(content, 'lxml-xml')
    ancestor_div = soup.find(name='div', id='5623865')
    data_content = ancestor_div.find_all('record')
    return list_raw2dict(data_content)


def list_raw2dict(data_list: list[bs4.element.Tag]) -> list[dict]:
    result = []
    for item in data_list:
        text = str(item)
        title_match = title_pattern.search(text)
        href_match = href_pattern.search(text)
        time_match = time_pattern.search(text)
        data = {}
        href_group = None
        if title_match:
            data[pg_title] = title_match.group(1)
        if href_match:
            href_group = href_match.group(1)
            data[pg_href] = href_group
        if time_match:
            data[pg_time] = time_match.group(1)
        if href_group:
            result.append(data)
    return result
