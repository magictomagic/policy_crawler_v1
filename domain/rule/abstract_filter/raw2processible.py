import bs4.element
from lxml import html
import json
from bs4 import BeautifulSoup


def r2p_fzggw_1(raw: str) -> bs4.element.Tag:
    soup = BeautifulSoup(raw, 'lxml-xml')
    ancestor_div = soup.find('div', id='4892867')
    return ancestor_div


def r2p_test_1(raw: str) -> bs4.element.Tag:
    soup = BeautifulSoup(raw, 'lxml')
    ancestor_div = soup.find('div', id='11111')
    return ancestor_div
