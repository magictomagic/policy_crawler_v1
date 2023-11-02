from unittest import TestCase

from domain.rule.detail_filter.raw2detail import r2d_lishui


class Test(TestCase):
    # def test_extract_details(self):
    #     self.fail()

    def test_r2d_lishui(self):
        with open("raw_content/lishui_detail.html", "r", encoding='utf-8') as f:
            html_content = f.read()
        result = r2d_lishui(html_content)
        assert len(result.get("title")) > 4
        assert len(result.get("content")) > 40


