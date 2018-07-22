#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/22 下午1:05
# @Author  : littlelinghome
# @Site    : 
# @File    : db_handler.py
# @Software: PyCharm


import json,time,os
from conf import settings

def load_account_data(account):
    """根据account id 找打对应的账户文件，并加载"""
    account_file = os.path.join(settings.DB_PATH,"%s.json" % account)
    if os.path.isfile(account_file):
        f = open(account_file)
        data = json.load(f)
        f.close()
        return {'status':0,'data':data}
    else:
        return {'status':-1,'error':"account file does not exist."}


def save_db(account_data):
    account_file = os.path.join(settings.DB_PATH,"%s.json" % account_data['id'])
    if os.path.isfile(account_file):
        f = open("%s.new" % account_file,"w")
        data = json.dump(account_data,f)
        f.close()
        os.rename("%s.new" % account_file,account_file)
        return {'status':0,'data':data}
    else:
        return {'status':-1,'error':"account file does not exist."}