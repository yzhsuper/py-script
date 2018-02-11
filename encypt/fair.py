# -*- coding: utf-8 -*-
from __future__ import division

import os

import decimal
from decimal import Decimal
from Crypto.Hash import SHA256
import hashlib
import hmac
import struct
import binascii


MP = pow(2, 32)


# 4294967296


def decimal_round(value, precision):
    # prestr = Decimal(1.0 / (10**int(precision)))
    value = Decimal(str(value))
    prestr = ''
    while (True):
        if precision - 1 > len(prestr):
            prestr = prestr + '0'
        else:
            prestr = prestr + '1'
            break
    prestr = '0.' + prestr
    return value.quantize(Decimal(prestr), rounding=decimal.ROUND_HALF_EVEN)


def decimal_div(obj1, obj2, precision):
    obj1 = Decimal(str(obj1))
    obj2 = Decimal(str(obj2))
    result = decimal_round(obj1 / obj2, precision)
    return result


def decimal_mul(obj1, obj2, precision):
    obj1 = Decimal(str(obj1))
    obj2 = Decimal(str(obj2))
    result = decimal_round(obj1 * obj2, precision)
    return result


class FairGenerator(object):
    """
    https://csgogem.com/ 算法
    """

    def __init__(self, server_seed, client_seed):
        self.server_seed = server_seed
        self.client_seed = client_seed

    def server_hash(self):
        h = SHA256.new()
        h.update(self.server_seed)

        sha = hashlib.sha256()
        sha.update(self.server_seed)

        print h.hexdigest()
        print '......', sha.hexdigest()
        return h.hexdigest()

    def round_result(self):
        h = hmac.new(self.server_seed, digestmod=hashlib.sha512)
        # h.update(self.client_seed)
        # h = hmac.new(self.server_seed, self.client_seed, digestmod=hashlib.sha512)
        buf = h.digest()
        h, = struct.unpack(">I", buf[:4])

        # print h
        # abc = decimal_div(h, MP, 6)
        # abc = decimal_mul(abc, 100, 4)
        r = h * 100 / MP
        return r


def gen_random_seed():
    """
    生成随机32
    :return:
    """
    seed = binascii.hexlify(os.urandom(16))
    # print type(seed)
    return seed
    # return hashlib.md5(seed).hexdigest()


# for x in range(5):
#     print gen_random_seed()
#
# exit(1)


def get_area(b):
    a = int(b / 2) + 1
    return a

area_dict = {}

count = 0
round_list = []
for x in range(10000):
    a = gen_random_seed()
    fg = FairGenerator(a, a)
    b = fg.round_result()
    round_list.append(b)
    if b <= 0.06:
        print b

    # # print b
    # #
    # if b >= 99.99:
    #     print 'linjie', b
    #
    # area = get_area(b)
    # if area_dict.get(area):
    #     area_dict[area] = area_dict.get(area) + 1
    # else:
    #     area_dict[area] = 1
# round_list.sort()
# print round_list
# print area_dict

# for key in sorted(area_dict.keys()):
#     print key, area_dict[key]

# print '-----------------'
# print len(area_dict)



