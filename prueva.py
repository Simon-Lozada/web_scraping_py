#!/usr/bin/env python
#_*_ coding: utf8 _*_

from proxy_tor import ConnectionManager

cm = ConnectionManager()
for j in range(5):
    for i in range(3):
        print ("\t\t" + cm.request("http://icanhazip.com/").read())
    cm.new_identity()
