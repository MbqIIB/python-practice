#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/22 下午1:00
# @Author  : littlelinghome
# @Site    : 
# @File    : main.py
# @Software: PyCharm


from .auth import authenticate
from .utils import print_error
from .logger import logger
from atm import logics

transaction_logger = logger("transaction")
access_logger = logger("access")

features = [
    ('账户信息',logics.view_account_info),
    ('取现',logics.with_draw),
    ('还款',logics.pay_back)
]

def controller(user_obj):
    while True:
        for index,feature in enumerate(features):
            print(index,feature[0])
        choice = input("ATM>>:").strip()
        if not choice:continue
        if choice.isdigit():
            choice=int(choice)
            if choice < len(features) and choice>=0:
                features[choice][1](user_obj,transaction_logger=transaction_logger,access_logger=access_logger)
        if choice == 'exit':
            exit("Bye.")


def entrance():
    user_obj = {
        'is_authenticated':False,
        'data':None
    }
    retry_count = 0
    while user_obj['is_authenticated'] is not True:
        account = input("\033[32;1maccount:\033[0m").strip()
        password = input("\033[32;1mpassword:\033[0m").strip()
        auth_data = authenticate(account,password)
        if auth_data:
            user_obj['is_authenticated'] = True
            user_obj['data'] = auth_data
            print("welcome")
            access_logger.info("user %s just logged in" % user_obj['data']['id'])

            controller(user_obj)

        else:
            print_error("wrong username or password!")
        retry_count += 1

        if retry_count == 3:
            msg = "user %s tried wrong password reached 3 times" % account
            print_error(msg)
            access_logger.info(msg)
            break

