#!/usr/bin/evn python
#-*- coding:utf-8 -*-
import pymongo
from string import punctuation
import charts
client = pymongo.MongoClient('localhost',27017)
urls = client['urls']
item_info = urls['item_info']
for i in item_info.find():
    if i['area']:
        area = [i.replace('-','') for i in i['area']]
    item_info.update({'_id':i['_id']},{'$set':{'area':area}})
for i in item_info.find().limit(10):
    print(i['area'])