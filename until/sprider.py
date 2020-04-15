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

def GET_zhihu():
    session = HTMLSession()
    url = "https://www.zhihu.com/hot"

    try:
        h = session.get(url=url,
                        timeout=5,
                        headers={
                                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36",
                                "cookie": '_zap=e385324b-9627-4a6b-a56f-b81fad3c1ba0; d_c0="AJAicE284g6PTtFmF6iiqkXKRPThE4EeFiM=|1548514134"; __gads=ID=b9260609c15027f3:T=1554031522:S=ALNI_MZYqo91mACoWo9TKIdKIteUkB-C8A; __utmv=51854390.100-1|2=registration_date=20141102=1^3=entry_date=20141102=1; __utma=51854390.956905189.1562305476.1577263520.1578706223.14; __utmz=51854390.1578706223.14.9.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/topic/19550376/hot; z_c0=Mi4xNzRXYkFBQUFBQUFBa0NKd1RiemlEaGNBQUFCaEFsVk5hYW9hWHdCWGFxeWJiTzliYVRUc0Zza0w3STRIYlU4N3Jn|1580031081|b30b5e36e9df6abf05704e7e2b4bb5162195de46; _ga=GA1.2.956905189.1562305476; _xsrf=4QF9CzqGlDXlv9cPO4peqxEaaZS9IF8t; q_c1=839b488ec8004ccdada761ef8ecdace8|1584367896000|1548914354000; tshl=; _gid=GA1.2.1151961666.1586739082; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1586922078,1586928440,1586930762,1586935108; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1586935108; _gat_gtag_UA_149949619_1=1; tst=h; KLBRSID=0a401b23e8a71b70de2f4b37f5b4e379|1586935110|1586935108; SESSIONID=tq9HEa2KLLlWd3EfUKjVRLpMbHUbE3GJefeVNSUcRv7; JOID=VF8SAkgojGA7LwAWJi9oMAOZRw02Xf1fcW9gJGthwQxqSTZSQG8_8mIrARAik8Me2Cn_QZf8P7u3m5XXj38uA44=; osd=VV8cBkkpjG4_LgEWKCtpMQOXQww3XfNbcG5gKm9gwAxkTTdTQGE782MrDxQjksMQ3Cj-QZn4Prq3lZHWjn8gB48='
                            })
    except:
        return []

    else:
        mes_list = re.findall('titleArea":{"text":"(.*?)"},"excerptArea":{"text":"(.*?)"},"imageArea".*?"link":{"url":"(.*?)"}},"cardId"', h.text)


        return [["https://www.zhihu.com/question/" + mes[2][-9:], mes[0], mes[1]] for mes in mes_list]

# if __name__ == '__main__':
#     # dd = GET_ithome()
#     # print(dd)
#     GET_zhihu()
