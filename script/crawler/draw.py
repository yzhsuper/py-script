#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
import sys

url = 'http://www.igxe.cn/treasure/order_zero'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'}
headers['X-Requested-With'] = 'XMLHttpRequest'
headers['Content-Type'] = 'application/x-www-form-urlencoded; charset=UTF-8'

Cookie = {"__cfduid": "d6738eaa899c8c3e7c00bda2b9e90f68b1476841788", "csrftoken": "NSZykMCMn7rcQ7fTMKT9SQop9OOckWbp",
          "sessionid": "u5x8v5ccy13hl0zreargacxlmzjvocis"}

id_str = 9121

if sys.argv and len(sys.argv) > 1:
    id_str = sys.argv[1]


post_data = {"treasure_id": id_str, 'csrfmiddlewaretoken': 'NSZykMCMn7rcQ7fTMKT9SQop9OOckWbp'}

limit = 2
i = 1

if sys.argv and len(sys.argv) > 2:
    limit = int(sys.argv[2])

while i <= limit:
    response = requests.post(url=url, data=post_data, headers=headers, cookies=Cookie)
    print id_str, response.content.decode('unicode_escape').encode('utf-8')
    i += 1