#!/usr/bin/python
# -*- coding: utf-8 -*-
import json
import random
import threading

import requests
import sys

url = 'https://api.coinbase.com/v2/prices/spot?currency=USD'


def api_test():
    response = requests.get(url=url, timeout=10)
    return json.loads(response.content)

data = api_test()
print data


