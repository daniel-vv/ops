#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
@Author: Du Baoqiang
Github: https://github.com/daniel-vv/ops/
Create date: 2016/3/20
Blog: http://www.dbq168.com
      http://www.cnblogs.com/dubq/
'''


def deny_user(username):
    '''定义一个锁定用户的函数,在下面调用'''
    print('\033[31;1m您的用户已被锁定,请联系管理员\033[0m')
    f = open('locked','a')
    f.write(username)
    f.write('\n')
    f.close()

Count = 0    #定义一个初始值,进入循环
Flag = False #定义一个标志位,初始值是False,做退出循环用
Retry_count = 2  #定义一个重试值,初始为2,每次密码输错减1,为0时锁定用户
init_user = None  #定义一个用户初始值,用于判定用户输入的用户名是否一致,如若一致并输错三次才会加入黑名单

if __name__ == '__main__':
    while Count < 3:
        user_input_user = input('请输入你的用户名: ').strip()
        # 判断用户是否存在黑名单内,如在直接拒绝,否则的话,继续下面认证判断
        #Locked user_input_user

        with open('locked','r') as Locked_info:       #
            for i in Locked_info.readlines():         #遍历锁文件,查找输入用户是否在锁文件中
                if i.strip() == user_input_user:              #如果在锁定文件中,提示用户,并退出程序
                    print('\033[31;1m抱歉，%s 已经锁定,请联系管理员，谢谢\033[0m' % user_input_user)
                    Flag = True
                    break
        if not Flag and user_input_user:           #判断,如果标志位为假的,即初始值False,并且用户输入的消息不是空值,即原有变量None则进入下面操作
                user_input_password = str(input('请输入密码：')).strip()   #提示用户输入密码
                #验证用户名密码之前,先把用户输入的用户名赋给一个变量,用作后续比较,判定用户多次尝试输入的是否是一个用户
                if user_input_user == init_user:    #判断用户此次输入是否和上一次是一样的,如果一样,则把重试计数器加1
                    Retry_count += 1
                else:
                    init_user = user_input_user    #否则的话,将用户输入的赋值给初始变量init_user,用于下一次判定,并将计数器-1
                    Retry_count -= 1
                with open('./passwd','r') as f:     #用with的方式打开用户密码文件,并别名为f
                    for u in f.readlines():         #遍历整个文件,之前文件的格式
                        User,Password = u.split()   #分别用split分割,并赋值给User和Password变量,用户下面比较用户输入是否正确
                        if user_input_user == str(User) and user_input_password == str(Password):   #判断输入用户名密码是否和文件中匹配
                            print('\033[32;1m用户验证成功,欢迎 %s 来到这里,愿你开心每一天\033[0m' %user_input_user)
                            Flag = True
                            break
                    else:    #正常执行完如果上述判断没有进入,则说明用户输入账号密码不正确,则提示用户错误,而后进入下一次循环
                        if Retry_count == 2:    #Retry_count为初始值2,证明输入错误密码一次,还有两次机会
                            print('用户名或密码验证失败,您还有一次机会,如果失败,用户将被锁定,请重试')
                        else:      #最后一次机会失败了,直接调用上面定义的deny_user函数来打印信息,并锁定用户到Locked文件
                            print('用户名或者密码错误')
        if Flag:     #如果正常验证通过,上面会将标志位置为真,并跳出上面的循环,这里再次判断,如果为真,直接跳出整个循环;
            break
        else:
            Count += 1       #正常执行到这里后循环计数器递增1,而后跳出本次循环;
            continue
    else:
        if user_input_user:      #while循环正常结束后加个判断,用户输入是否为真,才会执行下面的将用户添加到黑名单中,也就是上面定义的函数,否则的话,用户输入三遍回车,也会添加一个回车到黑名单去
            if Retry_count == 3: #根据上面用户输入用户名是否一致的计数器判断是否要锁定用户,计数器为3表示用户输入了三遍错误的用户名和密码
                deny_user(user_input_user) #




