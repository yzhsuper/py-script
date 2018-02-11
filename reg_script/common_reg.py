# -*- coding: utf-8 -*-

import re


a = u'我草123asdfasf去尼玛'

print 'oriing .....', (len(a))

c = u'[\u4e00-\u9fa5]'

p = re.compile(c)

n = p.sub('aa', a)

print 'faater .....', (len(n))

m = p.findall(a)

print m

d = p.match(a.encode('utf-8'))

print d


re_words = re.compile(u"[\u4e00-\u9fa5]+")
m = re_words.search(a, 1)

print m.group()
