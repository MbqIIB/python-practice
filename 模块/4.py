#!/usr/bin/env python3
# _*_coding: utf-8_*_
# @Time    : 2018/5/18 下午4:21
# @Author  : littlelinghome
# @Site    : 
# @File    : 4.py
# @Software: PyCharm

序列化：
序列化是指把内存里的数据类型转变成字符串，使其能存储到硬盘或通过网络传输到远程，因为硬盘或者网络传输只能接受bytes
字典啊列表啊等等都是内存数据类型，不是硬盘数据类型
把内存数据转成字符，叫序列化
把字符转成内存数据类型，叫反序列化

不同编程语言之间的交互规则
1. 纯文本，坏处：不能共享复杂的数据类型
2. xml，坏处：占空间大
3. json，简单，可读性好

data = {
    'role':[
        {'role':'monster','type':'pig','life':50},
        {'role':'hero','type':'关羽','life':80},
    ]
}

f = open('/Users/caolingjun/daily/www.txt','w')
#f.write(data)
# 此时会报错TypeError: write() argument must be str, not dict
f.write(str(data))



f = open('/Users/caolingjun/daily/www.txt','r')
d = f.read()
d = eval(d)
print(d['role'])
