#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/9 下午8:33
# @Author  : littlelinghome
# @Site    : 
# @File    : 3.py
# @Software: PyCharm

user_status = False  # 用户登录了就把这个改成True
def login(func):  # 把要执行的模块从这里传进来
    def inner():  # 再定义一层函数
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
    return inner  # 用户调用login时，只会返回inner的内存地址，下次再调用时加上()才会执行inner函数

def home():
    print("---首页----")

def america():
    print("----欧美专区----")

def henan():
    print("----河南专区----")


home()
america = login(america)  # 你在这里相当于把america这个函数替换了
henan = login(henan)

# 那用户调用时依然写
america()
henan()

### 使用装饰器的概念优化代码 ###
