#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/14 下午5:04
# @Author  : littlelinghome
# @Site    : 
# @File    : 1.py
# @Software: PyCharm


'''逐行处理1000行文件，对每一行的第一例数据进行处理，处理之后就写入的到新文件中。
需要注意的是，这里的文件内部信息并没有改变，而只是重新排列组合而已。
新生成的文件下标是按照需求生成的新的数字。
'''

import io
for i in range(0,1000):
        with io.open(r'/data/littlelinghome/aaa' + str(i) +'.txt','r',encoding='utf8') as f:
                for line in f:
                        var1 = int(line.split('\t')[0])/1000%1000
                        fileName = 'bbb' + str(var1)
                        print fileName
                        txt = open(u'/data/littlelinghome/' + fileName + '.txt', 'a')
                        txt.write(line + '\n')