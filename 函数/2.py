#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/27 下午7:54
# @Author  : littlelinghome
# @Site    : 
# @File    : 2.py
# @Software: PyCharm


#程序有2个分支，当满足某种条件时就一直执行该函数，当跳出这个条件时就返回我们所需要的最终结果
#此处，递归内层函数后面没有其他语句，若是有的话，需要从内层一步一步把递归函数后面的语句执行完，整个程序才能算完成。

def calc(n,count):
    print(n,count)
    if count < 5:
        return calc(n/2,count + 1)
    else:
        return n
res = calc(188,1)
print('res = ',res)

