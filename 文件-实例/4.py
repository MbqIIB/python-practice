#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/15 下午12:09
# @Author  : littlelinghome
# @Site    : 
# @File    : 4.py
# @Software: PyCharm


#替换原文件中的某个字符串，并且存放在新文件中（占用磁盘的方式）

f_old_name = '/Users/caolingjun/mydocument/aaa.txt'
f_new_name = '/Users/caolingjun/mydocument/bbb.txt'

old_str = '乔一飞'
new_str = '乔二飞'

f_old = open(f_old_name,'r',encoding='utf-8')
f_new = open(f_new_name,'w',encoding='utf-8')

for line in f_old:
    if old_str in line:
        line = line.replace(old_str,new_str)
    f_new.write(line)
f_old.close()
f_new.close()





