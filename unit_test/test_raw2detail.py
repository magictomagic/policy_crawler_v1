import os
from unittest import TestCase

from domain.rule.detail_filter.raw2detail import r2d_lishui


def read_html_file(filename):
    """
    must read file from absolute path to make sure both testable in local and cloud

    :param filename:
    :return:
    """
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Construct the absolute path to the file
    file_path = os.path.join(script_dir, 'raw_content', filename)

    # Open the file, read its content, and return the content
    with open(file_path, "r", encoding='utf-8') as f:
        html_content = f.read()

    return html_content


# Usage:
html_content = read_html_file('lishui_detail.html')


class Test(TestCase):
    # def test_extract_details(self):
    #     self.fail()

    def test_r2d_lishui(self):
        result = r2d_lishui(read_html_file('lishui_detail.html'))
        assert len(result.get("title")) > 4
        assert len(result.get("content")) > 40


