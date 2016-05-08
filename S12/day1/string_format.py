#!/usr/bin/env python
# coding:utf-8

name = input("name:")
age = input("age:")
job = input("job:")

#print("Information of []: \nName:["+ name +"]\nAge:["+ age +"]\nJob:["+ job +"]")
#print("Information of []: \nName:[%s] \nAge:[%s] \nJob:[%s]" %(name,age,job))
msg = '''
Information of:
    Name:[%s]
    Age:[%s]
    Job:[%s]
''' %(name,age,job)
print(msg)