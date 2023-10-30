from domain.rule.abstract_filter.processible2raw_list import p2r_fzggw_1, p2r_test_1
from domain.rule.abstract_filter.raw2json import r2j_fzggw_1, r2j_test_1
from domain.rule.abstract_filter.raw2processible import r2p_fzggw_1, r2p_test_1
from domain.rule.detail_filter.raw2detail import r2d_fzggw_1

fzggw_filter_rule = {
    "url": "https://fzggw.zj.gov.cn/col/col1599545/index.html",
    "raw2pro": r2p_fzggw_1,
    "pro2raw_list": p2r_fzggw_1,
    "raw2json": r2j_fzggw_1
}

test_filter_rule = {
    "url": "http://127.0.0.1:8003/sql1",
    "raw2pro": r2p_test_1,
    "pro2raw_list": p2r_test_1,
    "raw2json": r2j_test_1
}