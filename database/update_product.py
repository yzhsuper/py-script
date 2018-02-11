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

sql = '''
INSERT INTO product(icon_url, icon_url_large, name, market_hash_name, market_name, tradable, marketable, commodity, descriptions,
last_updated, product_category_id, product_type_id, tags_exterior_id, tags_rarity_id, is_stattrak, tags_sticker_capsule_id,
market_price, steam_price, app_id) values("{0}", "{1}", "{2}", "{3}", "{4}" , 1, 1, 0, "{5}", "{6}", -1, -1, -1, -1, %s, %s, 0, 0 , 578080)
'''

now = datetime.now()

format_time = now.strftime("%Y-%m-%d %H:%M:%S")
try:
    product_list = []
    with open('/home/pengfei/product.json') as data:
        products = json.load(data)
        product_list = products.get('RECORDS')

    conn = MySQLdb.connect(host=default['HOST'], user=default['USER'], passwd=default['PASSWORD'], db=default['NAME'], port=3306, charset='utf8')
    cursor = conn.cursor()

    for x in product_list:
        market_hash_name = x.get('market_hash_name').encode('utf-8').replace('"', '""')

        q_sql = 'select name from product where market_hash_name="{name}"'.format(name=market_hash_name)
        cursor.execute(q_sql)
        pd = cursor.fetchone()
        if pd:
            print pd
            continue

        name = x.get('name').encode('utf-8').replace('"', '""')
        market_name = x.get('market_name').encode('utf-8').replace('"', '""')
        descriptions = x.get('descriptions')
        if descriptions and descriptions != 'null':
            descriptions = descriptions.encode('utf-8').replace('"', '""')
        elif descriptions == 'null':
            descriptions = ''

        insert_sql = sql.format(x.get('icon_url'), x.get('icon_url_large'), name, market_hash_name, market_name,
                                descriptions, format_time)

        insert_sql = insert_sql % (x.get('is_stattrak'), x.get('tags_sticker_capsule_id'))
        try:
            cursor.execute(insert_sql)
            cursor.fetchone()
        except BaseException as e:
            print 'Insert fail', market_hash_name, e.message

    conn.commit()
    cursor.close()
    conn.close()
except MySQLdb.Error, e:
    print e
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])

except BaseException as e:
    print 'exception:', e.message


sys.exit(1)

