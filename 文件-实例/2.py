#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/14 下午5:39
# @Author  : littlelinghome
# @Site    : 
# @File    : 2.py
# @Software: PyCharm




'''
逐行读取文件，对含有id的行，取出该行的第二列放入到一个列表中，
对于含有tagName的行，取出改行的第二列放入到另外一个空列表中，
以追加的方式打开一个文件，循环把2个列表内的数据写入到这个文件中。
'''

#!/usr/bin/python
# -*- coding:utf-8 -*-
import io
import sys
id_num = []
tagName = []
result = []
with io.open(r'/littlelinghome/aaa.txt','r',encoding='utf8') as f:
    for line in f:
        if 'id' in line:
            id_num.append(line.split('=>')[1])
        if 'tagName' in line:
            tagName.append(line.split('=>')[1])
txt = open(u'tmpresult.txt', 'a')
for index in range(len(id_num)):
    txt.write(id_num[index].strip().encode("utf8") + tagName[index].strip()[1:-2].encode("utf8")+'\n')