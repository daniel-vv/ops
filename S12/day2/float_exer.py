#!/usr/bin/env python
# -*- coding: utf-8 -*-

f = 1.2

#result = f.as_integer_ratio()   #返回改值的最简比
#result = f.conjugate()  #共轭复数
#result = float.fromhex(f)  #将十六进制字符串转换成浮点数
#result = f.hex()  #返回当前值的十六进制表示方式
#result = f.is_integer() #判断当前值是否是一个整数
#result = f.__abs__()  #返回当前值的绝对值
#result = f.__divmod__(2) #除,返回商和余数
#result = f.__float__()  #转换为浮点数格式
#result = f.__getformat__('float') #
result = f.__hash__()
#result = f.__neg__()  #正变负 负变正
#result = f.__pow__(2)  #平方
#result = f.__truediv__(3)  #x/y

print(result)
