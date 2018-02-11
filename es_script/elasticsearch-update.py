#!/usr/bin/python
# -*- coding:UTF-8 -*-
import json

import MySQLdb
import sys

from elasticsearch import helpers, TransportError
from elasticsearch import Elasticsearch
from elasticsearch.helpers import BulkIndexError

ES_CONFIG = [
    {'host': 'localhost', 'port': 9200},
    {'host': '172.16.20.141', 'port': 9200},
]


es = Elasticsearch(ES_CONFIG)


def bulk_exception_format(errors):
    update_failed_list = []
    for error in errors:
        data = error.get('update')
        if data and data.get('status') == 404:
            update_failed_list.append(data.get('_id'))

    return update_failed_list


def update_product_status(trade_ids, status):
    """
    更新es搜索引擎产品状态
    :param status:
    :param trade_ids:
    :param kwargs:
    :return:
    """

    index = "csgointl"
    doc_type = "product-trade"

    actions = []
    opt = 'update'
    for trade_id in trade_ids:
        actions.append({
            '_op_type': opt,
            '_index': index,
            '_type': doc_type,
            '_id': trade_id,
            'doc': {'status': status}
        })

    helpers.bulk(client=es, actions=actions)


try:
    trade_ids = [12717160, 12726720]
    rs = update_product_status(trade_ids, 5)
    # rs = es.update(index="csgointl", doc_type="product-trade", id=1272053, body={'doc': {'name_en': 'AWP | Worm God'}})
    print rs
except BulkIndexError as e:
    print bulk_exception_format(e.errors)