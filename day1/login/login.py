#!/usr/bin/env python
# -*- coding: utf-8 -*-


def deny_user(username):
    print('您的用户已被锁定,请联系管理员')
    f = open('blanklist','w+')
    f.write(username)
    f.close()


count = 0
while count < 3:
    user_input_user = input('\033[32;1m请输入你的用户名:\033[0m').strip()
    # 判断用户是否存在黑名单内,如在直接拒绝,否则的话,继续下面认证判断
    if user_input_user in blanklist:
        print('您的账户信息尝试错误超限,请联系管理员解锁')
        break
    User = fuser.read()
    if user_input_user in User:
        user_input_passwd = input('请输入你的密码:').strip()
        #User = f.readlines()
        #if user_input_user == ''
    else:
        print('账户不存在,或者密码不正确!')
        count += 1
        continue
    count += 1





