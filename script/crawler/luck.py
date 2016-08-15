#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from lxml import etree
import json

file_object = open('csgo.txt', 'w')


url = 'http://www.igxe.cn/treasure/publish/record?page_no=%s'

headers = {}
headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36' \
                        ' (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'
headers['X-CSRFToken'] = 'erUlBU7IuNZMmkpyH1jxchk8zIofKDPJ'
headers['X-Requested-With'] = 'XMLHttpRequest'
headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'

Cookie = {
    "__cfduid": "dcade7bcc21a9c2d96e1efc59105e5f2a1470360797",
    "csrftoken": "ekXZ5XV6smpAdPdVaT4tkgtnbk2N5V20",
    "sessionid": "dv3zg7fbc9hdg2e2l8nq1v9hf9wfqbzb",
    "_ga": "GA1.2.1757933044.1469677111",
    "_gat_UA-73155637-1": "1"
}


name_dict = {}

TOTAL_PAGE = 37
for x in range(1, TOTAL_PAGE):
    url_x = url % x
    response = requests.get(url=url_x, headers=headers, cookies=Cookie)
    html = etree.HTML(response.content)
    nodes = html.xpath('//*[@id="center"]/div[2]/div/div[1]/div[2]/ul/li/div/div[3]/span[2]/a/span')
    for node in nodes:
        if node.text in name_dict:
            num = name_dict.get(node.text)
            num += 1
            name_dict[node.text] = num
        else:
            name_dict[node.text] = 1

name_list = sorted(name_dict.iteritems(), key=lambda d: d[1], reverse=True)
for value in name_list:
    print '%-20s' % value[0], value[1]
    file_object.write('%-20s %s\n' % (value[0].encode('utf-8'), value[1]))

# for k, v in name_dict.items():
#     print '%-20s' % (k.encode('utf-8')), v, '\n'
#     file_object.write('%-20s %s\n' % (k.encode('utf-8'), v))

file_object.close()