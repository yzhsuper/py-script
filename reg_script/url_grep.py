# -*- coding: utf-8 -*-

import re

a = "<div style=\"white-space: nowrap; margin: 10px\"><div style=\"white-space: nowrap; padding: 3px;\">" \
    "<div style=\"width: 60px; height: 32px; vertical-align: top; display: inline-block;\"><div style=\"position:" \
    " relative; width: 48px; height: 32px; vertical-align: top; display: inline-block; border: 2px solid rgb(255, 2" \
    "55, 255);\"><div style=\"position: absolute; width: 48px; height: 32px; vertical-align: top; display: inline-block;" \
    " background-size: contain; background-image: url(https://steamcdn-a.akamaihd.net/apps/570/icons/econ/sockets/gem_stat." \
    "30d7935c1f0a1b9e8e28c691c2bd28f7d5f471bc.png)\"></div></div></div><div style=\"vertical-align: top; display: inline-block; " \
    "margin-left: 12px padding: 2px\"><span style=\"font-size: 18px; white-space: normal; color: rgb(255, 255, 255)\">Wards " \
    "Purchased: 80</span><br><span style=\"font-size: 12px\">Inscribed Gem</span></div></div><div style=\"white-space: nowrap; " \
    "padding: 3px;\"><div style=\"width: 60px; height: 32px; vertical-align: top; display: inline-block;\"><div style=\"position: " \
    "relative; width: 48px; height: 32px; vertical-align: top; display: inline-block; border: 2px solid rgb(255, 255, 255);\">" \
    "<div style=\"position: absolute; width: 48px; height: 32px; vertical-align: top; display: inline-block; background-size: co" \
    "ntain; background-image: url(https://steamcdn-a.akamaihd.net/apps/570/icons/econ/sockets/gem_stat.30d7935c1f0a1b9e8e28c691c" \
    "2bd28f7d5f471bc.png)\"></div></div></div><div style=\"vertical-align: top; display: inline-block; margin-left: 12px padding: 2p" \
    "x\"><span style=\"font-size: 18px; white-space: normal; color: rgb(255, 255, 255)\">Roshan Kills: 2</span><br><span style=\"fon" \
    "t-size: 12px\">Inscribed Gem</span></div></div></div>"


rr = re.compile(r'(?<=url\().+?gem.+?(?=\))')
results = rr.findall(a)
print type(results)
for x in results:
    print x


# tt = "Tina is a good girl, she is cool, clever, and so on..."
# rr = re.compile(r'\w*oo\w*')
# print(rr.findall(tt))
# print(re.findall(r'(\w)*oo(\w)',tt))#()表示子表达式

# results = re.findall('url(\.+)', a)
# print results
#
# results = re.search('(url(\.+))', a)
# print results.group()
