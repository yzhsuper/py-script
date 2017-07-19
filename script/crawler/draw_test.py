#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import threading

import requests
import sys

url = 'http://172.16.12.38:8000/activity/gift_draw'
num = 10

if sys.argv and len(sys.argv) > 1:
    num = sys.argv[1]

i = 1
Cookie = {"sessionid": "d8qg32i0kb5u9yze3e2tviwkfupo7oqc"}
while i <= int(num):
    response = requests.get(url=url, cookies=Cookie)
    print i, response.content.decode('unicode_escape').encode('utf-8')
    i += 1


#class DrawThread(threading.Thread):
#    def __init__(self, steam_uid):
#        threading.Thread.__init__(self)
#        self.steam_uid = steam_uid
#
#    def run(self):
#        response = requests.get(url=url % self.steam_uid, cookies=Cookie)
#        print i, response.content.decode('unicode_escape').encode('utf-8')
#
#threads = []
#
#s = [76561198297428101, 76561198267110904, 76561198264280135, 76561198267345094, 76561198267066763]
#
#for x in range(1, int(num)):
#    threads.append(DrawThread(random.choice(s)))
#
#for t in threads:
#    t.start()
