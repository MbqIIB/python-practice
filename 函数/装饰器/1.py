#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/9 下午5:07
# @Author  : littlelinghome
# @Site    : 
# @File    : 1.py
# @Software: PyCharm

# _*_coding:utf-8_*_
user_status = False  # 用户登录了就把这个改成True


def login():
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
    else:
        print("用户已登录，验证通过...")


def home():
    print("---首页----")


def america():
    login()  # 执行前加上验证
    print("----欧美专区----")


def henan():
    login()  # 执行前加上验证
    print("----河南专区----")


home()
america()
henan()

#### 每个独立函数运行的时候都需要添加认证模块 ###




