# -*- coding: utf-8 -*-
import re
from requests_html import HTMLSession


def get_V2EX():
    session = HTMLSession()
    url = "https://www.v2ex.com/?tab=hot"
    try:
        h = session.get(url=url, timeout=5)
    except TimeoutError:
        return []
    mes_list = re.findall('class="topic-link">(.*?)</a></span>', h.text)
    return mes_list




# if __name__ == '__main__':
#     get_V2EX()