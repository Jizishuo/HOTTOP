# -*- coding: utf-8 -*-
import re
from requests_html import HTMLSession


def GET_v2ex():
    session = HTMLSession()
    url = "https://www.v2ex.com/?tab=hot"
    try:
        h = session.get(url=url, timeout=5)
    # except requests.exceptions.ReadTimeout:
    except:
        return []
    mes_list = re.findall('<a href="(.*?)" class="topic-link">(.*?)</a></span>', h.text)
    mes_list = [["https://www.v2ex.com" + mes[0], mes[1]] for mes in mes_list]
    return mes_list

def GET_ithome():
    session = HTMLSession()
    url = 'https://www.ithome.com/'
    try:
        h = session.get(url=url, timeout=5)
    except:
        return []
    h.encoding = 'utf-8'
    mes_list = re.findall('<li class="new"><span class="date">今日</span><span class="title"><a target="_blank" href="(.*?)">(.*?)</a></span></li>', h.text)
    return [[mes[0], mes[1]] for mes in mes_list]

# if __name__ == '__main__':
#     print(i_home())
    # print(get_V2EX())