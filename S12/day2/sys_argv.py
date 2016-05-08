#!/usr/bin/env python
# _*_ coding:utf-8 _*_
import sys
Argv = sys.argv
A = 1
for i in Argv:
    if len(Argv) >= 3:
        print('Argv is too many, please input two argvs, thanks！')
        break
    else:
        print('This is %s argv:' %A, i)
    A += 1


