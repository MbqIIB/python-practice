#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/22 下午1:01
# @Author  : littlelinghome
# @Site    : 
# @File    : auth.py
# @Software: PyCharm


from .db_handler import load_account_data
from .utils import print_error

def authenticate(account,password):
    """对用户信息进行验证"""
    account_data = load_account_data(account)
    if account_data['status'] == 0:
        account_data = account_data['data']
        if password == account_data['password']:
            return account_data
        else:
            return None
    else:
        return None

