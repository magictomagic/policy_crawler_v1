from domain.rule.abstract_filter.fetch_contents import fetch_content_lishui, fetch_content_fzggw, fetch_content_jinhua, \
    fetch_content_jiaxing
from domain.rule.abstract_filter.parse_content import parse_content_lishui, parse_content_fzggw, parse_content_jinhua, \
    parse_content_jiaxing

filter_rule_lishui = {
    "url": "https://www.lishui.gov.cn/col/col1229265119/index.html?df=/col/col1229283449/index.html&isgk=1",
    "afetch_content": fetch_content_lishui,
    "parse_content": parse_content_lishui
}

filter_rule_fzggw = {
    "url": "https://fzggw.zj.gov.cn/col/col1599545/index.html",
    "afetch_content": fetch_content_fzggw,
    "parse_content": parse_content_fzggw
}

filter_rule_jinhua = {
    "url": "http://www.jinhua.gov.cn/col/col1229160382/index.html",
    "afetch_content": fetch_content_jinhua,
    "parse_content": parse_content_jinhua
}

filter_rule_jiaxing = {
    "url": "https://www.jiaxing.gov.cn/col/col1229567741/index.html",
    "afetch_content": fetch_content_jiaxing,
    "parse_content": parse_content_jiaxing
}
