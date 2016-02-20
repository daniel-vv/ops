#!/usr/local/env python

from config import settings

def db_auth(configs)
	if configs.DATABASES['user'] == 'root' and configs.DATABASES['password'] == '123':
		print ('db auth is successfull')
		return True
	else:
		print ('db auth is falure..')

def select(table,column):
	if db_auth(settings):
		if table == 'user':
			user_info = {
			  "01":['tom',22],
			  '02':['jerry',23]
			return user_info
}
