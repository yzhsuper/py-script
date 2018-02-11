#!/usr/bin/python
# -*- coding:UTF-8 -*-

import MySQLdb
import sys
from elasticsearch import Elasticsearch

ES_CONFIG = [
    {'host': 'localhost', 'port': 9200},
    # {'host': '172.16.20.142', 'port': 9200},
    {'host': '172.16.20.141', 'port': 9200},
]

try:
    conn = MySQLdb.connect(host='172.16.20.70', user='xzj', passwd='xzj2016', db='csgointl', port=3306)
    count = 58992
    size = 500
    start = 0
    for x in range(1, 100):
        start = (x - 1) * size
        sql = 'select * from product_trade order by id limit %s,%s'
        cur = conn.cursor()
        cur.execute(sql, (start, size))
        data = cur.fetchall()
        es = Elasticsearch(ES_CONFIG)
        for d in data:
            document = {"steam_pid": d[1], "steam_oid": d[2], "steam_uid": d[3], "status": d[5]}
            document['last_updated'] = d[6]
            document['title'] = d[7]
            document['descriptions'] = d[8]
            document['unit_price'] = d[9]
            document['currency_id'] = d[10]
            document['product_id'] = d[11]
            document['purchase_price'] = d[12]
            document['date_created'] = d[13]
            document['is_sticker'] = d[14]
            document['sales_channel'] = d[15]
            document['source'] = d[16]
            document['source_object_id'] = d[17]
            document['premium_rate'] = d[18]
            document['curr_price'] = d[19]
            document['last_trade_id'] = d[20]
            document['sales_site'] = d[21]
            es.index(index="csgo_intel", doc_type="product_type", id=d[0], body=document)
    cur.close()
    conn.close()
except MySQLdb.Error, e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)
