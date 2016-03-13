#!/usr/bin/env python
# -*- coding: utf-8 -*-

class A(object):
    n = 'A'
    def f2(self):
        print('F2 from A')
    #print(n)

class B(A):
    n = 'B'
    #def f2(self):
    #    print('F2 from B')
    #print(n)

class C(A):
    n = 'C'
    def f2(self):
        print('F2 from C')
    #print(n)

class D(B,C):
    pass

d = D()
[poiu'g't'h]
d.f2()



