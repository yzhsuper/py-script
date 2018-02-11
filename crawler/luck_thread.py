#!/usr/bin/python
# -*- coding: utf-8 -*-
import threading

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
    "__cfduid": "db5a5320d9d476d22e66c68a4933e821f1469677111",
    "csrftoken": "649ga9Pmnv2zCuCyyg5cp8q2fAihBUTH",
    "sessionid": "dt4s9cccb313mhl5pt5x3r1ep9lvisdi",
    "_ga": "GA1.2.1757933044.1469677111",
    "_gat_UA-73155637-1": "1"
}


name_dict = {}

TOTAL_PAGE = 21
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

for k, v in name_dict.items():
    print '%-20s' % (k.encode('utf-8')), v, '\n'
    file_object.write('%-20s %s\n' % (k.encode('utf-8'), v))

file_object.close()

name_list = []


# class DrawThread(threading.Thread):
#     def __init__(self, page):
#         threading.Thread.__init__(self)
#         self.page = page
#
#     def run(self):
#         url_x = url % self.page
#         response = requests.get(url=url_x, headers=headers, cookies=Cookie)
#         html = etree.HTML(response.content)
#         nodes = html.xpath('//*[@id="center"]/div[2]/div/div[1]/div[2]/ul/li/div/div[3]/span[2]/a/span')
#         for node in nodes:
#             # print node.text
#             name_list.append(node.text)
#             # if node.text in name_dict:
#             #     num = name_dict.get(node.text)
#             #     num += 1
#             #     name_dict[node.text] = num
#             # else:
#             #     name_dict[node.text] = 1
#
# threads = []
#
# for x in range(1, TOTAL_PAGE):
#     threads.append(DrawThread(x))
#
# for t in threads:
#     t.start()
#
# if num == 0:
#     for a in name_list:
#         print a


