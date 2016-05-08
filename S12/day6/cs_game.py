#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Role(object):
    def __int__(self,name,role,weapon,life_value):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value

    def buy_weapon(self,weapon):
        print('%s is buying [%s]',%(self.name,weapon))

p1 = Role('Tom','Police','B12',100)
t1 = Role('Jerry','Terrorist','B14',100)

p1.weapon('M16')
t1.weapon('AK47')



