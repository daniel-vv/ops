#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging

'''
#
logging.warning('哎呀,打印出来日志了!')
logging.critical('服务器宕掉了!')
'''
'''
# 写日志到文件中去
logging.basicConfig(filename='example.log',level=logging.INFO)
logging.debug('这是debug信息')
logging.info('这是info级别的消息')
logging.warning('这是warn级别的消息')


# 加上时间,格式化日志
logging.basicConfig(filename='example.log',level=logging.INFO,format='%(asctime)s %(message)s',datefmt='%Y-%m-%d %H:%M:%S')
logging.debug('这是debug信息')
logging.info('这是info级别的消息')
logging.warning('这是warn级别的消息')
'''


# 同时打印日志到屏幕上和日志里
# 创建logger
logger = logging.getLogger('ABC')
logger.setLevel(logging.DEBUG)

# 创建一个console handle
c = logging.StreamHandler()
c.setLevel(logging.DEBUG)

# 创建一个文件handle
f = logging.FileHandler('access.log')
f.setLevel(logging.WARN)

# 创建日志格式
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 添加格式到控制台输出和日志输出
c.setFormatter(formatter)
f.setFormatter(formatter)

# 添加c和f到 logger
logger.addHandler(c)
logger.addHandler(f)

# 日志消息
logger.debug('debug message')
logger.info('info message')
logger.warn('warning message')
logger.error('error message')
logger.critical('critical message')



