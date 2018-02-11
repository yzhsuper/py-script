#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from lxml import etree
import json
import threading
import Queue
import time


response_queue = Queue.Queue()


def thread_test(url, headers):
    print url, headers
    response = requests.get(url=url, headers=headers)
    print response.content
    # file_object = open('csgo.txt', 'wa')
    # file_object.write(response.content)
    # file_object.close()


class RequestThread(threading.Thread):
    def __init__(self, url, headers):
        threading.Thread.__init__(self)
        self.url = url
        self.headers = headers

    def run(self):
        response = requests.get(url=self.url, headers=self.headers)
        print response.content
        file_object = open('csgo.txt', 'a')
        file_object.write(response.content)
        file_object.close()
        #response_queue.put(response.content)


class WriteThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):
        while True:
            obj = response_queue.get()
            print obj
            if obj:
                file_object = open('csgo.txt', 'a')
                file_object.write(obj)
                file_object.close()


url = 'http://csgointl.igxe.com/profile'
cookie = 'csrftoken=sjNxURwe5tCcNvcNc6bJ7SuSQRG8TAEm; _gat_UA-77997400-1=1; _ga=GA1.3.343563913.1469527067; sessionid=l7j1gxbpeu8xx7cj8n5k7snyj7qya1d2'
Referer = 'http://csgointl.igxe.com/'
Accept = 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
Host = 'csgointl.igxe.com'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) \AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
headers['Cookie'] = cookie
# headers['Accept-Encoding'] = 'gzip, deflate, sdch'
# headers['Referer'] = Referer
# headers['Accept-Language'] = 'zh-CN,zh;q=0.8'
# headers['Cache-Control'] = 'max-age=0'
# headers['Connection'] = 'keep-alive'
# headers['Accept'] = Accept
# headers['Host'] = Host
# response = requests.get(url=url, headers=headers)
# print response.content

threads = []
for x in range(5):
    threads.append(RequestThread(url, headers))
print len(threads)
for t in threads:
    print 'start'
    t.start()
    time.sleep(1)

WriteThread().start()

# a = etree.HTML(response.content)
# nodes = a.xpath("//div[@class='song-item']/span[5]/a[1]")
# for x in nodes:
#     d = str(x.attrib).replace('u', '').replace('\'', '"').replace('\\', '\\\\')
#     print d
#     try:
#         dd = json.loads(d)
#     except BaseException as e:
#         print e
