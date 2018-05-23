#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/22 下午9:25
# @Author  : littlelinghome
# @Site    : 
# @File    : 1.py
# @Software: PyCharm


print sys.getdefaultencoding()    #系统默认编码
print sys.getfilesystemencoding() #文件系统编码
print locale.getdefaultlocale()   #系统当前编码
print sys.stdin.encoding          #终端输入编码
print sys.stdout.encoding         #终端输出编码


>>> import sys
>>> print sys.getdefaultencoding()
ascii
>>> print sys.getfilesystemencoding()
utf-8
>>> import locale
>>> print locale.getdefaultlocale()
('zh_CN', 'UTF-8')
>>> print sys.stdin.encoding
UTF-8
>>> print sys.stdout.encoding
UTF-8



Python2中的默认编码，有多个不同的变量。
1. 代码文件开头的coding
 # -*- coding: utf-8 -*-
或
 # coding=utf-8

指明代码文件中的字符编码，用于代码文件中出现中文的情况。

caolingjun@panpandeMacBook-Pro ~/daily$ cat hello.py
#! /usr/bin/env python
# -*- coding: utf-8 -*-
print '泥壕'
caolingjun@panpandeMacBook-Pro ~/daily$ python hello.py
泥壕

如果不设置，默认是ascii，当出现中文字符时就不能正常识别。
SyntaxError: Non-ASCII character '\xe6' in file hello.py on line 2, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details




2. sys.stdin.encoding和sys.stdout.encoding

sdtin和stdout输入输出使用的编码，包命令行参数和print输出，由locale环境变量决定。
在en_US.UTF-8的系统中，默认值是UTF-8。




3. sys.getdefaultencoding()
文件读写和字符串处理等操作使用的默认编码。
默认值是ascii。
