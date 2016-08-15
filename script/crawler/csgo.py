#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from lxml import etree
import json

file_object = open('csgo.txt', 'w')


url = 'http://www.igxe.cn/treasure/get/orders-3'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
headers['X-CSRFToken'] = 'erUlBU7IuNZMmkpyH1jxchk8zIofKDPJ'
headers['X-Requested-With'] = 'XMLHttpRequest'
headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'

Cookie = {"__cfduid":"db5a5320d9d476d22e66c68a4933e821f1469677111", "csrftoken":"zhJbIM3vaYGEnNFYo2CEjcxp6Rkcx1ge",
          "sessionid":"xi5dbm9u04427hn70bwmdm4yefsz0kut", "_ga":"GA1.2.1757933044.1469677111",
          "_gat_UA-73155637-1": "1"}

name_dict = dict()
buy_num_dict = dict()
TOTAL_PAGE = 39
for x in range(1, TOTAL_PAGE):
    response = requests.post(url=url, data={"page_no": x}, headers=headers, cookies=Cookie)
    try:
        result = json.loads(response.content)
        user_list = result.get('result_orders')
        if user_list:
            for user in user_list:
                if user.get('personaname') in name_dict:
                    num = name_dict.get(user.get('personaname'))
                    num += 1
                    name_dict[user.get('personaname')] = num

                    buy_number = buy_num_dict.get(user.get('personaname'))
                    buy_number += user.get('buy_number')
                    buy_num_dict[user.get('personaname')] = buy_number
                else:
                    name_dict[user.get('personaname')] = 1
                    buy_num_dict[user.get('personaname')] = user.get('buy_number')
    except BaseException as e:
        print e

for k, v in name_dict.items():
    if buy_num_dict.get(k) < 100:
        continue
    print '%s' % (k.encode('utf-8')), v, buy_num_dict.get(k), '\n'
    file_object.write('%-20s %s %s \n' % (k.encode('utf-8'), v, buy_num_dict.get(k)))

file_object.close()