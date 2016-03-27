#!/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
name = str('daniel {0} as {1}')
result = name.format('nb','znb')
print(result)
'''
#s = 'daniel	samtom'
#result = s.capitalize()  #首字母大写
#result = s.center(100,' ') #字符串居中,100表示总共多少个字符,后面内容可选,表示空白处填充的内容,默认为无
#result = s.count('a',5,9) #统计子序列出现的次数,后面两个参数可选,第一个是开始位,后一个是结束位
#s.encode('utf8')   #编码,针对Unicode
#result = s.decode('utf8')  #解码
#result = s.endswith('a') #是否以xxx结束,可选开始结束位
#result = s.expandtabs()
s = 'tom\nand\ndaniel'
str = 'daniel'
#result = s.expandtabs(4) #将tab换成空格
#result = s.find('z') #查找序列的位置,不存在的话返回-1
#result = s.format() #字符串格式化
#result = s.index('l') #查找子序列位置,和find不同的地方是,如果没找到则报错
#result = s.isalnum()  #是否是数字和字母
#result = s.isalpha() # 是否是字母
#result = s.isdigit() #是否是数字
#result = s.islower()  #是否是小写
#result = s.isspace()  #是否是空格
#result = s.istitle()  #是否是标题
#result = s.isupper()   #是否大写
# result = s.join(str)  #连接
#result = s.ljust(20,'#')  #左对齐,右侧填充
#result = s.lower() #变小写
#result = s.lstrip() #移除左侧空白
#result = s.partition('and')  #分割,前中后三段,需要指定一个分割的符号或者字符,而且分割后会变成一个元组的类型
#result = s.replace('and','or')  #替换
#result = s.split('and') #按照指定的字符分割,之后会变成一个列表类型
#result = s.splitlines() #根据换行分割
#result = s.startswith('t') #是否起始
#result = s.strip() #移除两边空白
#result = s.swapcase()  #大写变小写,小写变大写
#result = s.title()
#intab = 'and'
#outab = '123'
#trantab = s.maketrans(intab,outab)
#result = s.translate(trantab)   #转换,需要先指定一个对应表,最后一个表示删除字符集合,如上面两部
#result = s.upper() #变大写
#result = s.zfill(1) #返回指定长度的字符串,原来的字符串右对齐,前面填充0,如果指定少了,会返回原有的字符串
#还有一个写rsplit, rstrip, rfind等从右往左匹配的方法,就不一一列举

print(result)
'''
print('Original string: ' + result)
print('Default exapanded tab: ' + result.expandtabs())
print('Double exapanded tab: ' + result.expandtabs(8))
'''
