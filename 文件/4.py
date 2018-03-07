#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/8 上午11:03
# @Author  : littlelinghome
# @Site    : 
# @File    : 4.py
# @Software: PyCharm


#写文件，追加模式
f = open('/Users/caolingjun/lufeixuecheng.txt','ab')
f.write('\n路飞学城!'.encode('utf-8'))
f.close()

