#!/usr/bin/python
# -*- coding:UTF-8 -*-

import re
import json
import os
import requests

log_file = '/data/htdocs/csgointl/logs/elk_order.log'

search_list = ['payment_id', 'order_id', 'transaction_id', 'payment_method']
target_log_txt = "grep 'payment result' %s | tail -n 1" % log_file
txt = os.popen(target_log_txt).read()
print txt

json_data = {"status": "SUCCESS"}

for s in search_list:
    index = re.search(s, txt)
    if index:
        cur_txt = txt[index.end():]
        index = re.search(',', cur_txt)
        json_data[s] = cur_txt[:index.end()-1].replace(' ', '').replace('"', '').replace(':', '')


print json_data
# json_data['payment_id'] = '53306329eceb4b16a83beef277d835d4'
# json_data['transaction_id'] = '1712a3df4f72424db2999bd0af0a7374'
# json_data['order_id'] = 'CSGODEV10399922I10294'
# json_data['payment_method'] = 'EBANX_BOLETO'

response = requests.post('http://127.0.0.1:8000/pay/callback', json=json_data)
print response.content
