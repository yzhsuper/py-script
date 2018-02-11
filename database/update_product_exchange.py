#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import random
from datetime import datetime

import MySQLdb
import sys

default = {
    'NAME': 'inter_skinupgrade',
    'USER': 'xzj',
    'PASSWORD': 'xzj2016',
    'HOST': '172.16.20.70',
    'PORT': '3306',
}

ex_sql = '''
INSERT INTO product_exchange(product_id, name, market_hash_name, product_category_id, product_type_id, tags_exterior_id,
is_stattrak, be_price, af_price, exchange_rate, status, update_time, app_id)
values({0}, "{1}", "{2}", -1, -1, -1, {3}, 0, 0, 1, 0, "{4}", 578080)
'''


try:
    conn = MySQLdb.connect(host=default['HOST'], user=default['USER'], passwd=default['PASSWORD'], db=default['NAME'], port=3306, charset='utf8')
    q_sql = 'select id, name, market_hash_name, is_stattrak from product where app_id=578080'
    cursor = conn.cursor()
    cursor.execute(q_sql)
    products = cursor.fetchall()

    now = datetime.now()
    format_time = now.strftime("%Y-%m-%d %H:%M:%S")

    for x in products:
        pid = x[0]
        name = x[1].encode('utf-8').replace('"', '""')
        market_hash_name = x[2].encode('utf-8').replace('"', '""')
        is_stattrak = x[3]
        q_sql = 'select name from product_exchange where market_hash_name="{name}"'.format(name=market_hash_name)
        cursor.execute(q_sql)
        pd = cursor.fetchone()
        if pd:
            continue

        new_sql = ex_sql.format(pid, name, market_hash_name, is_stattrak, format_time)
        try:
            cursor.execute(new_sql)
            cursor.fetchone()
        except MySQLdb.Error, e:
            print market_hash_name
            print "Mysql Error %d: %s" % (e.args[0], e.args[1])

    conn.commit()
    cursor.close()
    conn.close()

except BaseException as e:
    print 'exception:', e.message

sys.exit(1)

