from infrastructure.entity.policy import NewsAbstract
from infrastructure.config.field_name import pg_href
from urllib.parse import urljoin, urlparse


def construct_absolute_url(base, link):
    # First, check if the link is already an absolute URL
    if bool(urlparse(link).netloc):
        return link

    # If not, join the base URL with the relative link to create the absolute URL
    return urljoin(base, link)






def fzggw_1(raw_json: dict) -> NewsAbstract:
    raw_json.get(pg_href)
    pass