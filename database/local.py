#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import sys

limit = 20
order_numbers = []

HOST = '127.0.0.1'
MYSQL_USER = 'root'
MYSQL_PASSWD = 'root'
DATABASE = 'common'


def query():
    sql = 'select id, create_date, product_trade_id from activity_product'
    try:
        conn = MySQLdb.connect(host=HOST, user=MYSQL_USER, passwd=MYSQL_PASSWD, db=DATABASE, port=3306)
        cur = conn.cursor()
        cur.execute(sql)
        data = cur.fetchall()
        for d in data:
            print d
        return data
    except MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)
    finally:
        cur.close()
        conn.close()