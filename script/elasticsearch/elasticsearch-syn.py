#!/usr/bin/python
# -*- coding:UTF-8 -*-

from datetime import datetime

from database import local
import sys

sys.path.append('/home/pengfei/PycharmProjects/py-script/script')
print sys.path
data = local.query()
from elasticsearch import Elasticsearch
# es = Elasticsearch()
#
#
# for x in data:
#     es.index(index="myindex", doc_type="test-type", id=1, body={"timestamp": x[1]})