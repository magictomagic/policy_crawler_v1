from bs4 import BeautifulSoup

from infrastructure.config.field_name import PG_MAX_DETAIL_CONTENT_LENGTH, PG_MAX_DETAIL_TITLE_LENGTH


def r2d_fzggw_1(raw: str) -> dict:
    soup = BeautifulSoup(raw, 'lxml')
    title_element = soup.find(class_='con-title')
    title = "title not extracted"
    if title_element:
        title = title_element.text.strip()
    content_element = soup.find(id='zoom')
    content = "content not extracted"
    if content_element:
        content = content_element.text.strip()
    return {
        "title": title,
        "content": content[:PG_MAX_DETAIL_CONTENT_LENGTH - 1]
    }


def r2d_lishui(raw: str) -> dict:
    soup = BeautifulSoup(raw, 'lxml')
    title_element = soup.find(class_='xl_title')
    title = "title not extracted"
    if title_element:
        title = title_element.text.strip()
    content_element = soup.find(class_='zoom')
    content = "content not extracted"
    if content_element:
        content = content_element.text.strip()
    return {
        "title": title,
        "content": content[:PG_MAX_DETAIL_CONTENT_LENGTH - 1]
    }


def r2d_jinhua(raw: str) -> dict:
    soup = BeautifulSoup(raw, 'lxml')
    title_element = soup.find(class_='jh_xl_m1').find('h1')
    title = "title not extracted"
    if title_element:
        title = title_element.text.strip()
    content_element = soup.find(class_='jh_xl_m2')
    content = "content not extracted"
    if content_element:
        content = content_element.text.strip()
    return {
        "title": title,
        "content": content[:PG_MAX_DETAIL_CONTENT_LENGTH - 1]
    }


def r2d_jiaxing(raw: str) -> dict:
    soup = BeautifulSoup(raw, 'lxml')
    title_element = soup.find('head').find('title')
    title = "title not extracted"
    if title_element:
        title = title_element.text.strip()
    content_element = soup.find(id='zoom')
    content = "content not extracted"
    if content_element:
        content = content_element.text.strip()
    return {
        "title": title[:PG_MAX_DETAIL_TITLE_LENGTH - 1],
        "content": content[:PG_MAX_DETAIL_CONTENT_LENGTH - 1]
    }