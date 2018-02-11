# -*- coding: utf-8 -*-

import struct

byte_list = []

byte_length = [(8, 'Q'), (2, 'H'), (1, 'B'), (1, 'B'), (4, 'I'), (2, 'H'), (1, 's')]

point_list = []

# with open('/home/pengfei/ffff88007091eb00', 'rb') as f:
#     while True:
#         temp = f.read(1)
#         if len(temp) == 0:
#             break
#         value = temp.encode('hex')
#         print value,
with open('/home/pengfei/ffff88007091eb00', 'rb') as f:
    context = f.read()
    print type(context)
    # context = context.encode('hex')
    points = context[:8]
    points = points.encode('hex')
    print points[::-1]

    ID, = struct.unpack('H', context[8:10])
    print ID

    eth_list = context[10:16]

    eth_list_str = []
    for x in eth_list:
        value = x.encode('hex')
        eth_list_str.append(value)

    print 'ETH:', ':'.join(eth_list_str)

    ip_list = context[16:20]
    ips = []
    for x in ip_list:
        a, = struct.unpack('>B', x)
        ips.append(str(a))

    print 'IP:', ':'.join(ips)

    PORT, = struct.unpack('H', context[20:22])
    print 'PORT:', PORT

    BRO, = struct.unpack('B', context[22:23])
    print 'BRO:', BRO

    ua = context[23:]
    print 'ua:', ua


exit(1)
with open('/home/pengfei/ffff88007091eb00', 'rb') as f:

    for x in range(8):
        temp = f.read(1)
        value = temp.encode('hex')
        point_list.append(value)

    point_list.reverse()
    print 'POINT:', ''.join(point_list)

    ID, = struct.unpack('H', f.read(2))
    print 'ID:', ID

    eth_list = []
    for x in range(6):
        temp = f.read(1)
        value = temp.encode('hex')
        eth_list.append(value)

    print 'ETH:', ':'.join(eth_list)

    ip_list = []
    for x in range(4):
        a, = struct.unpack('>B', f.read(1))
        ip_list.append(str(a))

    print 'IP:', ':'.join(ip_list)

    PORT, = struct.unpack('H', f.read(2))
    print 'PORT:', PORT

    BRO, = struct.unpack('B', f.read(1))
    print 'BRO:', BRO


