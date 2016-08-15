#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from lxml import etree
import json
from bs4 import BeautifulSoup

url = 'http://music.baidu.com/artist/9319'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'}
response = requests.get(url=url, headers=headers)

soup = BeautifulSoup(response.content, 'lxml')
# print soup.title
# song_list = soup.find_all('span', class_='song-title')
# for x in song_list:
#     print x, '\r\n'

a_list = soup.select('span.song-title a')
for x in a_list:
    if x.string:
        print x.string, x.attrs.get('href'), '\r\n'