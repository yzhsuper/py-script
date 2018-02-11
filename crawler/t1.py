#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from lxml import etree
import json


url = 'http://www.igxe.cn/treasure/publish/record?page_no=%s'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'}

name_dict = dict()
file_object = open('csgo.txt', 'w')
for x in range(1, 10):
    url_x = url % x
    response = requests.get(url=url_x, headers=headers)

    a = etree.HTML(response.content)
    nodes = a.xpath("//*[@id='center']/div[2]/div/div[1]/div[2]/ul/li/div/div[3]/span[2]/a/span")
    if not nodes:
        break
    for b in nodes:
        if b.text in name_dict:
            num = name_dict.get(b.text)
            num += 1
            name_dict[b.text] = num
        else:
            name_dict[b.text] = 1
    # d = str(x.attrib).replace('u', '').replace('\'', '"').replace('\\', '\\\\')
    # print d
    # try:
    #     dd = json.loads(d)
    # except BaseException as e:
    #     print e

print name_dict
for k, v in name_dict.items():
    print '%s' % (k.encode('utf-8')), v, '\n'
    #file_object.write('%20s %s\n' % (k.encode('utf-8'), v))
file_object.close()