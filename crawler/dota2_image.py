#!/usr/bin/python
# -*- coding: utf-8 -*-

import requests
from lxml import etree
import json

file_object = open('csgo.txt', 'w')


url = 'https://www.igxe.cn/dota2'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.62 Safari/537.36'}

Cookie = {"__cfduid":"db5a5320d9d476d22e66c68a4933e821f1469677111", "csrftoken":"gBQbxrspNHuxqXuV1z8latsnylsUdEAV",
          "sessionid":"xi5dbm9u04427hn70bwmdm4yefsz0kut", "_ga":"GA1.2.1757933044.1469677111",
          "_gat_UA-73155637-1": "1"}

DOMAIN = 'https://www.igxe.cn/'

one_xpath = '//*[@id="js-dota-searbar"]/div[1]/div/ul[2]/li/a/img'
second_xpath = '//*[@id="js-dota-searbar"]/div[2]/div/ul[2]/li/a/img'
third_xpath = '//*[@id="js-dota-searbar"]/div[3]/div/ul[2]/li/a/img'

session = requests.session()
response = session.get(url=url, headers=headers)
html = etree.HTML(response.content)
nodes = html.xpath(third_xpath)
for node in nodes:
    src = node.attrib.get('src')
    temp = src.split('/')
    file_name = temp[-1]
    image_url = '%s%s' % (DOMAIN, src)
    html = session.get(image_url)
    dist = '%s%s' % ('/home/pengfei/PycharmProjects/py-script/script/crawler/images2/', file_name)
    print dist
    with open(dist, 'wb') as img_file:
        img_file.write(html.content)