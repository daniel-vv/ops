#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import getpass
pwd = getpass.getpass()
User = getpass.getuser()
print('Username: %s\nPassword: %s' %(User,pwd))

