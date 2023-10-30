import bs4
from bs4 import BeautifulSoup


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
        "content": content
    }
