#!/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
#t1 = (1,2,3,4)
t1 = (1,2,3,4,{'k1':'v1'})
t1[4]['k1'] = 2
#del t1[4]['k1']
print(t1)
'''

a = 20
b = 40
'''
print(a.__abs__())
print(abs(a))

print(a.__eq__(b))
print(a.__add__(b))
print(a.__divmod__(b))
print(a/b)
print('%s and %s: %s' % (a,b,a.__ge__(b)))
print(a.__rdivmod__(b,2))
'''
'''
name = ['d','a','n','i''e','l']
result = "".join(name)
print(result.capitalize())
'''
'''
name = 'danielisdbq'
#result = name.partition('is')
result = name.split('is')
#print(type(result))
print(result)
'''

'''
name = dbq
daniel
jerry
tom
#result1, result2, result3, result4 = name.split('\n')
#print(result1, result2, result3, result4)
result = name.split('\n',2)
print(result)
'''

#s = ['my','name','is','daniel']
#result = ' '.join(s)          #链接对象
#print(result)

a = 'index'
b = 4
#result = s.swapcase()           #小写转换为大写
#result = s.bit_length()         # 返回该数字占用的最少位数
#result = s.conjugate()         #返回共轭复数
#result = a.__add__(b)           #相加
#result = a.__and__(b)           #与运算，二进位都为1时，结果为1，否则为0
#result = a.__abs__()      #取绝对值
# result = a.__divmod__(b)
#result = a.__float__()   #转换为浮点数
#result = a.__floordiv__(b)      #只返回整除的结果，也就是只返回整数部分
#result = a.format( n='daniel', f='Shan Xi')    #格式化字符串，类似于%s
#result = a.__getattribute__('name')
#result = a.__hash__()     #返回对象的hash值
#result1 = b.__hash__()
#result = a.__hex__()
# result = a.__index__()
#result = a.__repr__()   #转化为解释器可读取的形式
#result1 = a.__str__()
#result = a.__rmod__(b)
#result = a.__mod__(b)
#result = a.__mul__(b)
#result = a.__neg__()
#result = a.__or__(b)
#result = a.__pow__(b)  #次方
#result = a.__pos__()
#result = a.__truediv__(b)
#result = a.__trunc__()    #返回数值为整型的值，在整数中没有意义
#result = a.__index__()
result = property(lambda self: object(), lambda self, v: None, lambda self: None)
print(result)

