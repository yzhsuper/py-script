#!/usr/bin/python
# -*- coding:UTF-8 -*-
import json

from elasticsearch import Elasticsearch


ES_CONFIG = [
    {'host': 'localhost', 'port': 9200},
    {'host': '172.16.20.141', 'port': 9200},
]

es = Elasticsearch(ES_CONFIG)


query_body = """
{
  "query": {
    "bool": {
      "must": [
        { "match": { "name_en":   {"query":"awp StatTrak", "operator": "and"}}}
      ],
      "filter": [
        { "terms":  { "rarity_id": [600, 608]}}
      ]
    }
  }
}
"""


query_body = """
{
  "query": {
    "bool": {
      "must": [
        { "match": { "name_en": "awp"}},
        { "terms":  { "rarity_id": [600, 608, 621]}}
      ]
    }
  },
  "from": 0,
  "size": 5,
  "sort":{
    "unit_price": "desc"
  }
}
"""
# ,
#       "filter": [
#         { "terms":  { "rarity_id": ["600", "608", "621"]}}
#       ]

# query_body = """
# {
#   "query": {
#      "match": { "name_en": "awp"}
#   }
# }
# """


def get(id):
    res = es.get(index="csgointl", doc_type='product-trade', id=id, _source=['id', 'name_en', 'rarity_id', 'unit_price', 'status'])
    return res


def es_format(res):
    print 'time:', res.get('took')
    hits = res.get('hits')
    print 'total:', hits.get('total')
    result = hits.get('hits')
    return result


body = {}

try:
    must = {'match': {'name_en': 'awpWorm'}}
    body['filter'] = {'bool': {'must': must}}
    query_body = json.loads(query_body)
    res = es.search(index="csgointl", doc_type='product-trade', body=query_body, _source=['id', 'name_en', 'rarity_id', 'unit_price', 'status'])
    # res = get(1271178)
    res = es_format(res)
    for r in res:
        data = r.get('_source')
        print data
except BaseException as e:
    print e


