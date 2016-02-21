#!/usr/bin/env python
# _*_ coding:utf-8 _*_

#t1 = (1,2,3,4)
t1 = (1,2,3,4,{'k1':'v1'})
t1[4]['k1'] = 2
#del t1[4]['k1']
print(t1)