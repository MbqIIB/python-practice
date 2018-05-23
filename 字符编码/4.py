#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 下午5:40
# @Author  : littlelinghome
# @Site    : 
# @File    : 4.py
# @Software: PyCharm


计算md5
同样，md5计算也要求输入的unicode先编码。

>>> a = '啊哈哈'
>>> b = u'哟呵呵'
>>> import hashlib
>>> hashlib.md5(a).hexdigest()
'f38b302e2993ec3fdad79c4d76074b21'
>>> hashlib.md5(b).hexdigest()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-2: ordinal not in range(128)
>>> hashlib.md5(b.encode('utf-8')).hexdigest()
'c02dc06719bafeaf60505b11d3c0c90a'





输出到stdout
输出到stdout时，默认编码是sys.stdout.encoding，默认值取决于系统环境变量，所以print输出汉字时才可以不用指定utf-8。
>>> import sys
>>> sys.stdout.encoding
'UTF-8'
>>> print u'\u54a9'
咩


而在zh_CN.GB2312的环境中，默认值不是utf-8，就不能正常输出了。
>>> import sys
>>> sys.stdout.encoding
'ANSI_X3.4-1968'
>>> print u'\u54a9'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeEncodeError: 'ascii' codec can't encode character u'\u54a9' in position 0: ordinal not in range(128)







命令行参数读取
通过sys.argv或argparse得到的命令行参数都是编码后的str类型，以\x开头的十六进制表示。可以通过sys.stdin.encoding得到命令行传入的编码类型，解码成unicode。


caolingjun@panpandeMacBook-Pro ~/daily$ cat hello.py
#/usr/bin/env
# -*- coding: utf-8 -*-
import sys
print repr(sys.argv[1])
print sys.stdin.encoding
print repr(sys.argv[1].decode(sys.stdin.encoding))
caolingjun@panpandeMacBook-Pro ~/daily$ python hello.py "我们"
'\xe6\x88\x91\xe4\xbb\xac'
UTF-8
u'\u6211\u4eec'






带\u的字符串转unicode
可能会遇到汉字被转换成unicode编码的形式表示的情况，即一个汉字被表示成了\u????的形式。

>>> a = u'咩'
>>> a
u'\u54a9'
>>> b = '\u54a9'
>>> b
'\\u54a9'

上述b就是这样的情况。此时b是一个长度为6的字符串，而不是一个汉字。


要把b表示为汉字编码有两种方法。

1. unicode-escape编码。
>>> unicode(b, 'unicode-escape')
u'\u54a9'
或
>>> b.decode('unicode-escape')
u'\u54a9'


2. eval拼接。
>>> eval('u"' + b.replace('"', r'\"')+'"')
u'\u54a9'


