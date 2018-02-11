#!/usr/bin/python
# -*- coding:UTF-8 -*-
import json

from elasticsearch import Elasticsearch


ES_CONFIG = [
    {'host': 'localhost', 'port': 9200},
    {'host': '172.16.20.141', 'port': 9200},
]

es_client = Elasticsearch(ES_CONFIG)
DEFAULT_INDEX = 'index_ina_alias'
DEFAULT_TYPE = 'product_trade'


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
      ],
      "filter":[
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
query_body = json.loads(query_body)

name_match = {"match": {"name_en": "awp Redline"}}
status_term = {"terms": {"status": [2]}}
must_list = [name_match]
filter_list = [status_term]
should_list = [{"terms": {"rarity_id": ["600", "608", "621"]}}]

# must_list.append({"match": {"name_en": "Redline"}})

comp_dict = {"must": must_list, "filter": filter_list, 'should': should_list}
bool_dict = {"bool": comp_dict}
query_body = {"query": bool_dict}

filter_body = {'filter': status_term}
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
    res = es_client.get(index="csgointl", doc_type='product-trade', id=id, _source=['id', 'name_en', 'rarity_id', 'unit_price', 'status'])
    return res


def es_format(res):
    print 'time:', res.get('took')
    hits = res.get('hits')
    print 'total:', hits.get('total')
    result = hits.get('hits')
    return result


try:
    fields = ['id', 'name_en', 'rarity_id', 'unit_price', 'status']
    res = es_client.search(index=DEFAULT_INDEX, doc_type=DEFAULT_TYPE, body={"term" : { "status" : 2}}, _source_include=fields)
    # res = get(1271178)
    res = es_format(res)
    for r in res:
        print r
        # data = r.get('_source')
        # print data
except BaseException as e:
    print e


