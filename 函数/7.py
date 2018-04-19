#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 下午1:59
# @Author  : littlelinghome
# @Site    : 
# @File    : 7.py
# @Software: PyCharm

#第一种情况
# def bar1():
#     def bar():
#         print('i am bar')
#     return bar()
# k = bar1()
# print(k)

###### answer:
# i am bar
# None



#第二种情况
# def bar1():
#     def bar():
#         print('i am bar')
#         return 'qqq'
#     return bar()
# k = bar1()
# print(k)

##### answer:
# i am bar
# qqq



#第三种情况：
def bar1():
    def bar():
        print('i am bar')
    return bar
k = bar1()
print(k)

##### answer:
#<function bar1.<locals>.bar at 0x1022467b8>，返回的是一个函数

