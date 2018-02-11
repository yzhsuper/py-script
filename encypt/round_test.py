# -*- coding: utf-8 -*-

import random

for x in range(10000):
    a = random.uniform(0, 100)
    if a <= 0.06:
        print a