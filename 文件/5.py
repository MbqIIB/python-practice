#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 上午11:24
# @Author  : littlelinghome
# @Site    : 
# @File    : 5.py
# @Software: PyCharm

#混合模式，既能读也能写,读写模式,read()模式有"光标"的概念在里面，每次读都是从上次读的地方开始往下读
f = open('/Users/caolingjun/lufeixuecheng.txt','r+',encoding='utf-8')
data = f.read()
print("content",data)

f.write('\nnewline 1!')
f.write('\nnewline 2')
f.write('\nnewline 3')
f.write('\nnewline 4')

print('new content',f.read())

f.close()
