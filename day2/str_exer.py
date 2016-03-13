#!/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
name = 'danielasdfasldkfjalkdf'
#result = name.capitalize()   #首字母大写
#result = name.format(tuple)    #
#result = name.center(50,'#')      #居中
#result = name.encode('utf8')   #转换字符编码
#result = name.count('df',1,10)   #统计字符出现次数
result = name.endswith('df')    #验证对象是否以某个字符结尾
print(result)
'''
name = str('daniel {0} as {1}')
result = name.format('nb','znb')
print(result)