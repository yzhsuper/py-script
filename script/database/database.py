#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import sys
import urllib
import urllib2
import re
import threading
from datetime import datetime

url = 'http://192.168.196.129:8000/get_gift?a=1'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = {'User-Agent': user_agent}

limit = 20
if not sys.argv:
    limit = sys.argv[1]

order_numbers = []
sql = 'select order_number from `order` LIMIT ' + str(limit)
sql = 'select DISTINCT order_number from `order` where order_object_id in ' \
      '(SELECT product_trade_id from activity_product) LIMIT ' + str(limit)

try:
    conn = MySQLdb.connect(host='172.16.20.70', user='xzj', passwd='xzj2016', db='csgodb', port=3306)
    cur = conn.cursor()
    cur.execute(sql)
    data = cur.fetchall()
    for d in data:
        order_numbers.append(d[0])
        print order_numbers
    cur.close()
    conn.close()
except MySQLdb.Error, e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

# class DrawThread(threading.Thread):
# 	def __init__(self, order):
# 		threading.Thread.__init__(self)
# 		self.order = order
#
# 	def run(self):
# 		newurl = url + '&order=' + str(self.order)
# 		request = urllib2.Request(newurl,headers = headers)
# 		response = urllib2.urlopen(request)
# 		content = response.read().decode('unicode_escape').encode('utf-8')
# 		print "时间：%s，结果：%s" % (datetime.now(), content)
#
# if order_numbers:
# 	threads = []
# 	for num in order_numbers:
# 		threads.append(DrawThread(num))
# 	for t in threads:
# 		t.start()
