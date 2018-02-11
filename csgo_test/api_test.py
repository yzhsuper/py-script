#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import random
import threading

import requests
import sys

url = 'http://172.16.12.38:8000/activity/share/3'
num = 10

if sys.argv and len(sys.argv) > 1:
    num = sys.argv[1]

Cookie = {"sessionid": "miu88gxea2bfsickv362jpsk5b7291b5"}


def box_api_test():
    response = requests.get(url=url, cookies=Cookie)
    return json.loads(response.content)


def box_item_api_test():
    response = requests.get(url=url, cookies=Cookie)
    return json.loads(response.content)


class CommonThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        response = box_item_api_test()
        try:
            print response, response.get('message')
        except:
            print 'format error'
        # print response.content.decode('unicode_escape').encode('utf-8')

threads = []

for x in range(1, int(num)):
    threads.append(CommonThread())

for t in threads:
    t.start()
