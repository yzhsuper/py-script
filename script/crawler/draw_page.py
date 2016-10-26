#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import sys
from lxml import etree
import json
import os

url = 'http://www.igxe.cn/treasure/index'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
headers['X-Requested-With'] = 'XMLHttpRequest'
headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'

Cookie = {"__cfduid": "d6738eaa899c8c3e7c00bda2b9e90f68b1476841788", "csrftoken": "NSZykMCMn7rcQ7fTMKT9SQop9OOckWbp",
          "sessionid": "u5x8v5ccy13hl0zreargacxlmzjvocis"}

response = requests.get(url=url, headers=headers, cookies=Cookie)
html = etree.HTML(response.content)
nodes = html.xpath('//*[@id="js-hot-zero-swiper"]/div[1]/div/div/div[4]/a[2]')

command = 'python draw.py %s 10'

for node in nodes:
    d = node.attrib.get('treasure_id')
    real_command = command % d
    txt = os.popen(real_command).read()
    print txt