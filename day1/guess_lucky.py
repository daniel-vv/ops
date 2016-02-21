#!/usr/bin/env python
# coding:utf-8

lucky_num = 30
count = 0

while count < 3:
    input_num = int(input('Please input your lucky number?'))
    if input_num < lucky_num:
        print('The real nums is smaller!')
    elif input_num > lucky_num:
        print('The real nums is bigger')
    elif input_num == lucky_num:
        print('Bingo')
        break
    count += 1
else:
    print('Too many errors to try!\n Bye!')

