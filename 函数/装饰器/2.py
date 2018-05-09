#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/9 下午8:06
# @Author  : littlelinghome
# @Site    : 
# @File    : 2.py
# @Software: PyCharm


# _*_coding:utf-8_*_


user_status = False  # 用户登录了就把这个改成True


def login(func):  # 把要执行的模块从这里传进来
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
        func()  # 看这里看这里，只要验证通过了，就调用相应功能


def home():
    print("---首页----")

def america():
    print("----欧美专区----")

def henan():
    print("----河南专区----")


home()
login(america)  # 需要验证就调用 login，把需要验证的功能 当做一个参数传给login
login(henan)


### 这里虽然实现了在调用前进行登录认证，但是在调用每个模块的时候都必须要加上login()方法，并把自己的函数名传给它，
### 试想下，如果有100个模块需要认证，那么100个模块都得改变调用方式


