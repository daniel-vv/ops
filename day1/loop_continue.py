#!/usr/bin/env python
# _*_ coding:utf-8 _*_

for j in range(5):
    for i in range(10):
        if i < 5:
            continue
        if j > 3:
            break
        print(i)
    print('===================================================')