#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import sys


HOST = '172.16.20.70'
HOST = '47.88.85.176'
MYSQL_USER = 'xzj'
MYSQL_USER = 'queryman'
MYSQL_PASSWD = 'xzj2016'
MYSQL_PASSWD = 'N93CQMH#9m,=V^BSDY1gj7puW*zTLCEM'
DATABASE = 'csgointl'

SS = [(76561198113935764,1124877), (76561198090137969,1130100), (76561198102228645,4559), (76561198102956637,915315), (76561198111877954,1130100), (76561198150361894,1023379), (76561198085168344,488924 ), (76561198069118061,1130100), (76561198349225225,915315), (76561198335009515,1134740), (76561198258666024,1128424), (76561198152748345,762155), (76561198260230161,1130100), (76561198202304395,1131234), (76561198111426633,1124877), (76561198307682058,965810), (76561198096453017,915315), (76561198345106486,1131234), (76561198096487681,502063), (76561198166395074, 488924)]
file_object = open('fake_box.sql', 'w')


target_sql = "INSERT INTO `activity_award_record` (`steam_uid`, `avatar`, `product_trade_id`, `icon_url`, `market_hash_name`, `create_date`, `update_date`) VALUES ('%s', '%s', 0, '%s', '%s', '2016-12-09 09:59:00', '2016-12-09 09:59:00');"
conn = MySQLdb.connect(host=HOST, user=MYSQL_USER, passwd=MYSQL_PASSWD, db=DATABASE, port=3306)
sql = 'SELECT avatar FROM steam_user WHERE steam_uid = "%s"'
cur = conn.cursor()
for x in SS:
    new_sql = sql % x[0]
    new_target_sql = target_sql % (x[0], '1', '1', '1')
    file_object.write('%s\r\n' % new_target_sql)
    try:
        cur.execute(new_sql)
        data = cur.fetchone()
        if data:
            print data
    except MySQLdb.Error, e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])
        sys.exit(1)
