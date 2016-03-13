#!/usr/bin/env python
# _*_ coding:utf-8 _*_
'''
dic = {'k1':'v1','k2':'v2'}
#new_dic = dic.fromkeys(['k1','k2','k3'],'balabala')
#print(new_dic)
#print(dic['k1'])
#print(dic['k2'])
'''
#print(dic.get('k1'))
#print(dic.get('k2'))
#print(dic.get('k3','haha'))
'''
print(dic.keys())
print(dic.values())
print(dic.items())


for k in dic.keys():
    print(k)

for v in dic.values():
    print(v)

for i in dic.items():
    print(i)

for k,v in dic.items():
    print(k,v)
'''
'''
l1 = [11,22,33,44,55,66,77,88,99,90]
dic = {}
v1 = []
v2 = []

for j in l1:
    if j > 66:
        v1.append(j)
    else:
        v2.append(j)
        #print(dic.items())
dic['k1'] = v1
dic['k2'] = v2
print(dic.items())
'''

list_all = [11,22,33,44,55,66,77,88,99,90]
dic = {}
for i in list_all:
    if i > 66:
        if 'k1' in dic:
            dic['k1'].append(i)
        else:
            dic['k1'] = [i,]
    else:
         if 'k2' in dic:
            dic['k2'].append(i)
         else:
            dic['k2'] = [i,]
else:
    print(dic.items())






