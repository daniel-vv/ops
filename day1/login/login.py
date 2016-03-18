#!/usr/bin/env python
# -*- coding: utf-8 -*-


def deny_user(username):
    print('您的用户已被锁定,请联系管理员')
    f = open('locked','w+')
    f.write(username)
    f.close()
'''
def Locked(username,input_user):
定义一个判断用户是否锁定的函数
    with open('locked','a') as Locked_info:
        for i in Locked_info.readlines():
            if i.strip() == username:
                print('抱歉，%s已经锁定' %s username)
                break
'''


Count = 0
Flag = False
while Count < 3:
    user_input_user = str(input('\033[32;1m请输入你的用户名:\033[0m')).strip()
    # 判断用户是否存在黑名单内,如在直接拒绝,否则的话,继续下面认证判断
    #Locked user_input_user
    with open('locked','r') as Locked_info:
        for i in Locked_info.readlines():
            if i.strip() == user_input_user:
                print('抱歉，%s已经锁定,请联系管理员，谢谢' % user_input_user)
                Flag = True
                break
    if not Flag:
        user_input_password = str(input('\033[32;1m请输入密码：\033[0m')).strip()
        with open('passwd','r') as f:
            for u in f.readlines():
                if u.split(':')[0] == user_input_user: #and u.split(':')[1] == user_input_password:
                    print('哇，登录成功，欢迎来到这里')
                    Flag = True
                    break
    if Flag:
        break
    else:
        continue





