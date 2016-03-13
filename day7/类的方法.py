#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Animal:
    count = 10
    def __int__(self,name):
        self.name = name
        self.num = None
    hobbie = 'meat'

    @classmethod   #类方法,不能访问实例变量
    def talk(self):
        print('%s is taling...' % self.hobbie)

    @staticmethod   #静态方法,不能访问类变量及实例变量
    def walk():
        print(' is walking')

    @property       #把方法变成属性
    def habit(self):
        print('%s habit is balabala' %self.name)

    @property
    def total_players(self):
        return self.num

    @total_players.setter
    def total_players(self,num):
        self.num = num
        print('total players:',self.num)
'''
    @total_players.deleter
    def total_players(self):
        print('total player got deleted.'),
        del self.num
'''
#Animal.hobbie
#Animal.talk()

d = Animal('Daniel')
print(d.total_players)
d.total_players = 3

#del d.total_players

print(d.total_players)


