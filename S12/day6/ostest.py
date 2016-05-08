#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil

d = '/Users/daniel/test'


#shutil.copyfile('/Users/daniel/test/src','/Users/daniel/test/haha')
#print(os.listdir(d))

shutil.make_archive('/Users/daniel/test/haha','gztar','/Users/daniel/test')
print(os.listdir(d))