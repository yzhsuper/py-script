#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from lxml import etree

login_url = "https://passport.csdn.net/account/login?ref=toolbar"

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'}


def send_request(url):
    res = requests.get(url)
    print res
    print res.cookies

if __name__ == '__main__':
    session = requests.Session()
    login_response = session.get(login_url, headers=headers)
    html = etree.HTML(login_response.text)
    random_code_ele = html.xpath('//*[@id="fm1"]/input[3]')[0]
    print random_code_ele
    print random_code_ele.get('value')