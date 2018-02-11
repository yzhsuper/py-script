# -*- coding: utf-8 -*-

import struct

a = struct.pack('c', 'yangzhuo')
print a

# with open('/home/pengfei/ffff88000f797e00', 'r') as f:
#     print f.read(64)
#     a, b = struct.unpack('i', f.read(64))
#     print a, b
