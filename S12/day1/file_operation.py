#!/usr/bin/env python
# _*_ coding:utf-8 _*_

'''
f = open('test.log','w')
f.write('This is the first line\n')
f.write('This is the second line\n')
f.write('This is the 3 line\n')
f.write('This is the 4 line\n')
'''

'''
f = open('test.log','r')
#print(f.readlines())
#print(f.read())
for line in f:
    if '3' in line:
        print('This is the third line')
    else:
        print(line)
'''
'''
f = open('test.log','w+')
f.write('This is the new line\n')
print('Data:')
print(f.read())
'''
#f = open('test.log','a')
#f.write('This is the 2 line\n')
#f.write('This is the 3 lien\n')
f = open('test.log','r')
print(f.read())
f.close()




