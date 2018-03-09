#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 下午2:43
# @Author  : littlelinghome
# @Site    : 
# @File    : 6.py
# @Software: PyCharm


#混合模式，既能写也能读,写读模式，意思是以写的模式打开文件（这个文件中之前的内容将被清空），几乎没有什么应用场景
f = open('/Users/caolingjun/lufeixuecheng.txt','w+',encoding='utf-8')
data = f.read()
print("content",data)

f.write('\nnewline 1!')
f.write('\nnewline 2')
f.write('\nnewline 3')
f.write('\nnewline 4')

print('new content',f.read())

f.close()