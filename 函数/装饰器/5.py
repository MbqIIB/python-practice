#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/9 下午8:53
# @Author  : littlelinghome
# @Site    : 
# @File    : 5.py
# @Software: PyCharm


# _*_coding:utf-8_*_
user_status = False  # 用户登录了就把这个改成True
def login(func):  # 把要执行的模块从这里传进来

    def inner(*args, **kwargs):  # 这里传入非固定参数，实现调用函数的时候添加参数的功能
        _username = "alex"  # 假装这是DB里存的用户信息
        _password = "abc123"  # 假装这是DB里存的用户信息
        global user_status

        if user_status == False:
            username = input("user:")
            password = input("pasword:")

            if username == _username and password == _password:
                print("welcome login....")
                user_status = True
            else:
                print("wrong username or password!")

        if user_status == True:
            func(*args, **kwargs)  # 这里传入非固定参数，实现调用函数的时候添加参数的功能

    return inner  # 用户调用login时，只会返回inner的内存地址，下次再调用时加上()才会执行inner函数


def home():
    print("---首页----")


@login
def america(name):
    print("----欧美专区----")
    print("he is %s" % name)
america("qqq")


@login
def henan(name):
    print("----河南专区----")
    print("she is %s" % name)
henan("ppp")

### 对有参数的函数进行装饰 ###