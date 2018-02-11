#!/usr/bin/python
# -*- coding: utf-8 -*-
import random

import MySQLdb
import sys

import chardet

product_names = ["CS:GO Weapon Case", "P250 | Boreal Forest", "Nova | Polar Mesh",
                 "Shadow Case Key", "USP-S | Torque", "PP-Bizon | Urban Dashed", "MP9 | Storm",
                 "USP-S | Kill Confirmed", "Winter Offensive Case Key"]


def get_names(cursor, box_id):
    query_sql = 'select `name` from unpack_box_item where box_id=%s'
    cursor.execute(query_sql, [box_id])
    _names = cursor.fetchall()
    names = []
    for x in _names:
        names.append(x[0].encode('utf-8').replace('"', '""'))
    return names


def get_total(money_start, money_end, product_names):
    query_sql = """SELECT count(1) FROM unpack_product_trade a
    JOIN product b ON a.product_id = b.id WHERE a.unit_price <= {end} AND a.unit_price >= {start}
    AND a.status = 2 AND a.site=2 AND b.name IN ("{names}")"""
    query_sql = query_sql.format(start=money_start, end=money_end, names='","'.join(product_names))
    cursor.execute(query_sql)
    total = cursor.fetchone()
    return total[0]


def query_random_product(money_start, money_end, product_names, total):

    offset_list = range(0, total, 3)
    offset_list = random.sample(offset_list, 5)
    print offset_list

    sql = """(SELECT a.id, a.product_id, b.name, a.unit_price, a.steam_uid FROM unpack_product_trade a
    JOIN product b ON a.product_id = b.id WHERE a.unit_price <= {end} AND a.unit_price >= {start}
    AND a.status = 2 AND A.site=2 AND b.name IN ("{names}") limit {size} offset %s) UNION ALL """

    sql = sql.format(start=money_start, end=money_end, names='","'.join(product_names), size=3)
    sql *= 5
    sql = sql % tuple(offset_list)
    sql = sql[0:-10]

    return sql


try:
    conn = MySQLdb.connect(host='47.88.85.176', user='queryman', passwd='N93CQMH#9m,=V^BSDY1gj7puW*zTLCEM', db='csgointl', port=3306, charset='utf8')
    cursor = conn.cursor()
    product_names = get_names(cursor, 163)

    total = get_total(0.01, 2.99, product_names)
    print total

    query_sql = query_random_product(0.01, 2.99, product_names, total)
    print query_sql
    cursor.execute(query_sql)
    data = cursor.fetchall()
    data = list(data)
    # random.shuffle(data)

    for d in data:
        print d
    cursor.close()
    conn.close()
except MySQLdb.Error, e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
    sys.exit(1)

