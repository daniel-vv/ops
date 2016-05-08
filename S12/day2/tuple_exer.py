#!/usr/bin/env python
# -*- coding: utf-8 -*-

t1 = ('Tom','Jerry','Jony')
#result = t1.count('Tom')  #统计元组中的数据出现位置,并返回第一此匹配到的下标
#result = t1.index('Tom') #返回匹配到的元组内容的下标
result = t1.__sizeof__()
print(result)


