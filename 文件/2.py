#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 下午8:29
# @Author  : littlelinghome
# @Site    : 
# @File    : 2.py
# @Software: PyCharm

#逐行读取文件
f = open('/Users/caolingjun/111.py','r')
for line in f:
    print(line)
f.close()