#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/15 下午7:51
# @Author  : littlelinghome
# @Site    : 
# @File    : 1.py
# @Software: PyCharm



# 函数递归，递归函数会先一层层的进入的最内层，然后再一层层的出来.
#当满足count < 5,会一直循环执行函数calc，并且在每次执行时，n/2  count+1
#calc(12.5，4)的函数值要看calc(6.25,5)函数的返回值
#calc(25,3)的函数值要看calc(12.5,4)函数的返回值，以此类推下去


def calc(n,count):
    print(n,count)
    if count < 5:
        v = calc(n/2,count + 1)
        print(v,count)
        return v
    else:
        return n
calc(100,1)
