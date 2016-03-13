#!/usr/bin/env python
# -*- coding: utf-8 -*-
'这是文档开始部分注释信息'
'''
class Foo():
    '文档注释部分,这里和文档开头的开不太一样,开头的是可以通过help查看的'
    pass
d = Foo.__doc__
print(d)
'''
'''
from libaa import C
obj = C()

print(obj.__module__)

print(obj.__class__)

'''
'''
# 自动执行类中的__init__方法
class Foo:
    def __init__(self,name):
        self.name = name
        self.age = 18
obj = Foo('DBQ')
print(obj)
'''
'''
# 析构方法,当对象在内存中被释放时,自动触发执行
class Foo:
    def __del__(self):
        pass
'''

'''
class Foo:
    def __init__(self):
        pass
    def __call__(self, *args, **kwargs):
        print(__call__)

obj = Foo()
obj()
'''
