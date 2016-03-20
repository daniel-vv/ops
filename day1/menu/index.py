#!/usr/bin/env python
# -*- coding: utf-8 -*-

d1 = {'k1':'v1','k2':'v2'}
print(d1.get('k1'))
print(d1.get('k2'))
print(d1.get('k3','balabala'))
#print(d1.keys())   #列出所有的key
#print(d1.items())   #列出所有的key和值
print(d1.values())

