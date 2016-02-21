#!/usr/local/env python

from backend.db.sql_api import select
def home():
  print ("Welcome to home page")
  q_data = select('user','123')
def tv():
  print ("Welcome to tv page")
  q_data = select('user','123')
def movie():
  print ("Welcome to movie page")
  q_data = select('user','123')
