#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 上午10:50
# @Author  : littlelinghome
# @Site    : 
# @File    : 2.py
# @Software: PyCharm


Unicode是字符集，UTF-8是Unicode的一种编码方式
某个字符的Unicode通过查询标准得到，其UTF-8编码由Unicode码计算得到。


str和unicode是两个不同的类。

str存储的是已经编码后的字节序列，输出时看到每个字节用16进制表示，以\x开头。每个汉字会占用3个字节的长度。
控制台运行：
>>> a = '啊哈哈'
>>> a
'\xe5\x95\x8a\xe5\x93\x88\xe5\x93\x88'
>>> type(a)
<type 'str'>
>>> a
'\xe5\x95\x8a\xe5\x93\x88\xe5\x93\x88'
>>> len(a)
9
>>> a[3]
'\xe5'

命令行运行：
caolingjun@panpandeMacBook-Pro ~/daily$ cat www.txt
# -*- coding: utf-8 -*-
a = '我们他们'
aa = len(a)
print aa
bb = a[3]
print bb
caolingjun@panpandeMacBook-Pro ~/daily$ python www.txt
12
�



unicode是“字符”串，存储的是编码前的字符，输出是看到字符以\u开头。每个汉字占用一个长度。定义一个Unicode对象时，以u 开头。
控制台运行：
>>> b = u'哟呵呵'
>>> type(b)
<type 'unicode'>
>>> b
u'\u54df\u5475\u5475'
>>> len(b)
3
>>> b[2]
u'\u5475'

命令行运行
caolingjun@panpandeMacBook-Pro ~/daily$ cat www.txt
# -*- coding: utf-8 -*-
a = u'我们他们'
aa = len(a)
print aa
bb = a[3]
print bb
caolingjun@panpandeMacBook-Pro ~/daily$ python www.txt
4
们




str可以通过decode()方法转化为unicode对象，参数指明编码方式。
控制台运行：
>>> a
'\xe5\x95\x8a\xe5\x93\x88\xe5\x93\x88'
>>> a.decode('utf-8')
u'\u554a\u54c8\u54c8'

命令行运行：
caolingjun@panpandeMacBook-Pro ~/daily$ cat www.txt
# -*- coding: utf-8 -*-
a = '啊哈哈'
b = a.decode('utf-8')
print a
print b
caolingjun@panpandeMacBook-Pro ~/daily$ python www.txt
啊哈哈
啊哈哈

注：在命令行运行的时候，直接打印a就可以显示字符串，而不用进行解码操作是因为print本身就是封装了这层功能



unicode可以通过encode()方法转化为str对象，参数指明编码方式。
控制台运行：
>>> b
u'\u54df\u5475\u5475'
>>> b.encode('utf-8')
'\xe5\x93\x9f\xe5\x91\xb5\xe5\x91\xb5'

命令行运行：
caolingjun@panpandeMacBook-Pro ~/daily$ cat www.txt
# -*- coding: utf-8 -*-
b = u'哟呵呵'
bb = b.encode('utf-8')
print b
print bb
caolingjun@panpandeMacBook-Pro ~/daily$ python www.txt
哟呵呵
哟呵呵

