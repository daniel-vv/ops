#!/usr/bin/env python
# coding:utf-8


'''
猜lucky number，n = 6
猜的数字比6大，提示说你打印的小一点
猜的数字比6小，提示说你打印的大一点
猜的数字等于6，提示Bingo


lucky_num = 6
input_num = int(input('Please input your lucky num: ').strip())
if input_num == lucky_num:
    print('Bingo!')
elif input_num > lucky_num:
    print('The real nums is bigger!')
else:
    print('The real nums is smaller!')

#循环
lucky_num = 6
input_num = 1
while lucky_num != input_num:
    input_num = int(input('Please input your lucky num: ').strip())
    #if input_num == lucky_num:
        #print('Bingo!')
        #break
    if input_num > lucky_num:
        print('The real nums is bigger!')
    elif input_num < lucky_num:
        print('The real nums is smaller!')
print('Bingo!')

'''

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
else:     #当上面的条件不满足之后，就走这块，上面的循环没有被正常退出，else不会执行；
    print('Too many errors to try!\nBye!')

