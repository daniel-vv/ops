#!/usr/bin/env python
# _*_ coding:utf-8 _*_
#f = open('test.txt','a+')
#f.write('This is zheshisha line\n')
#f.close()
#fid = f.fileno()
#fflush = f.flush()       #刷新文件内部缓冲区
#print(f.isatty())        #判断是否是tty设备
#print(f.read())
#print(fid)
#print(f.__next__())

'''with open('test.txt','a+') as f:
    for i in range(20):
        f.write('This is %s line\n' %i)
'''
#r = open('test.txt','r')
#print(r.readline())             #读取若干行，n表示读入的最长字节数
#for i in r:
#    print(i,)
#print(r.readline())
#print(r.tell())    #获取当前指针的位置，受seek, readline, read, readlines影响，但是不受truncate影响
#print(r.truncate(4))
#r.close()
#f = open('test.txt','w')
#f.write('first line\n')
#print(f.truncate(4))
#f.seek(2,0)
#print(f.tell())
#f.close()

#!/usr/bin/python
# -*- coding: UTF-8 -*-

'''
# 打开文件
fo = open("foo.txt", "r+")
print("文件名为: ", fo.name)

line = fo.readline()
print("读取第一行: %s" % (line))
print(fo.tell())

# 截断剩下的字符串
fo.truncate(10)

# 尝试再次读取数据
line = fo.readline()
print("读取数据: %s" % (line))
print(fo.tell())

# 截取剩下的字符串
#fo.truncate()

# 再次读取
line = fo.readline()
print("第三次读取数据: %s" %line)
print(fo.tell())

# 截取剩下的字符串
#fo.truncate()

# 再次读取
line = fo.readline()
print("第四次读取数据: %s" %line)
print(fo.tell())

# 关闭文件
fo.close()
'''

#writelines练习
f = open('test.txt','a')
list_str = ['my name is daniel','Male','30']
#print(f.writelines('my name is daniel\n'))
list_str = [line+'\n' for line in list_str]    #默认加入的列表没有换行，需要在列表中加入换行符\n，遍历一下列表，而后再次用writelines写入即可
f.writelines(list_str)
f.close()


