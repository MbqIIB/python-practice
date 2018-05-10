#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/10 上午10:02
# @Author  : littlelinghome
# @Site    : 
# @File    : 6.py
# @Software: PyCharm


#_*_coding:utf-8_*_

user_status = False #用户登录了就把这个改成True

def login(auth_type): #把要执行的模块从这里传进来
    def auth(func):
        def inner(*args,**kwargs):#再定义一层函数
            if auth_type == "qq":
                _username = "alex" #假装这是DB里存的用户信息
                _password = "abc123" #假装这是DB里存的用户信息
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
                    return func(*args,**kwargs) # 看这里看这里，只要验证通过了，就调用相应功能
            else:
                print("only support qq ")
        return inner #用户调用login时，只会返回inner的内存地址，下次再调用时加上()才会执行inner函数

    return auth

def home():
    print("---首页----")
home()

@login('qq')
### 等价于：america=login(america)('qq') --> america=auth('qq') --> america=inner
def america():
    print("----欧美专区----")
america()

@login('weibo')
### 等价于：henan=login(henan)('weibo') --> henan=auth('weibo') --> henan=inner
def henan(style):
    print("----河南专区----")
henan("3p")


### 让装饰器带参数 ###



