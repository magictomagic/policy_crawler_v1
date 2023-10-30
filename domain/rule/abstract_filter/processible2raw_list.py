import bs4.element


def p2r_fzggw_1(processible: bs4.element.Tag) -> list[bs4.element.Tag]:
    data_content = processible.find_all('record')
    return data_content


def p2r_test_1(processible: bs4.element.Tag) -> list[bs4.element.Tag]:
    data_content = processible.find_all('p')
    return data_content