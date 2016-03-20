#!/usr/bin/env python
# -*- coding: utf-8 -*-


#User = 'sam'
#Password = '123'
'''
User_input = input('Please input you User?').strip()
User_input_pass = input('Please input you password?')

with open('passwd','r') as f:
    for i in f.readlines():
        User = i.split(':')[0]
        Password = i.split(':')[1]
        if User_input == User:
            print(User_input)
            print(User)
            print('User is success')
            if User_input_pass == Password:
                print(type(User_input_pass))
                print(type(Password))
                print('Passwrod is success, welcome to here!')

Flag = False
if not Flag:
    print('balbala')
'''

#s = 'test'
#s = None
s = str(input('Please input your name?')).strip()
if not s:
    print('s is null')