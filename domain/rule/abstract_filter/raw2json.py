import re

import bs4.element

from infrastructure.config.field_name import pg_time, pg_title, pg_href

title_pattern = re.compile(r'title="([^"]+)"')
href_pattern = re.compile(r'href="([^"]+)"')
time_pattern = re.compile(r'(\d{4}-\d{2}-\d{2})')


def r2j_fzggw_1(text_tag: bs4.element.Tag):
    text = str(text_tag)
    title_match = title_pattern.search(text)
    href_match = href_pattern.search(text)
    time_match = time_pattern.search(text)

    data = {}

    if title_match:
        data[pg_title] = title_match.group(1)

    if href_match:
        data[pg_href] = href_match.group(1)

    if time_match:
        data[pg_time] = time_match.group(1)

    return data


def r2j_test_1(text_tag: bs4.element.Tag):
    data = {}
    data[pg_title] = text_tag.a.string
    data[pg_href] = text_tag.find('a').get('href')
    return data