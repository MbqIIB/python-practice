#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 下午1:39
# @Author  : littlelinghome
# @Site    : 
# @File    : 6.py
# @Software: PyCharm

import logging

def use_logging(func):
    def wrapper(*args,**kwargs):
        logging.warn("%s is running" % func.__name__)
        return func(*args,**kwargs)
    return wrapper

def bar():
    print('i am bar')

bar = use_logging(bar)
bar()


