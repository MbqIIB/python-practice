#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 下午8:40
# @Author  : littlelinghome
# @Site    : 
# @File    : 3.py
# @Software: PyCharm


#写文件,注意 w 参数是创建模式，如果文件中本身就有内容，那么相当于清空了文件中所有的内容然后重新写入
f = open('/Users/caolingjun/lufeixuecheng.txt','w',encoding='utf-8')
f.write('路飞学城!')
f.close()