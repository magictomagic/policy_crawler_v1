from domain.rule.abstract_filter.fetch_contents import fetch_content_lishui, fetch_content_fzggw
from domain.rule.abstract_filter.parse_content import parse_content_lishui, parse_content_fzggw

lishui_filter_rule = {
    "url": "https://www.lishui.gov.cn/col/col1229265119/index.html?df=/col/col1229283449/index.html&isgk=1",
    "afetch_content": fetch_content_lishui,
    "parse_content": parse_content_lishui
}

filter_rule_fzggw = {
    "url": "https://fzggw.zj.gov.cn/col/col1599545/index.html",
    "afetch_content": fetch_content_fzggw,
    "parse_content": parse_content_fzggw
}