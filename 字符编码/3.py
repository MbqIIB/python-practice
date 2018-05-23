#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 下午5:12
# @Author  : littlelinghome
# @Site    : 
# @File    : 3.py
# @Software: PyCharm


字符串拼接
unicode和str类型通过+拼接时，输出结果是unicode类型，相当于先将str类型的字符串通过decode()方法解码成unicode，再拼接。此时如果解码时没有明确指明编码类型，可能会出现错误。

>>> a = '啊哈哈'
>>> a
'\xe5\x95\x8a\xe5\x93\x88\xe5\x93\x88'
>>> b = u'哟呵呵'
>>> b
u'\u54df\u5475\u5475'
>>> a + b
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeDecodeError: 'ascii' codec can't decode byte 0xe5 in position 0: ordinal not in range(128)

>>> a.decode('utf-8') + b
u'\u554a\u54c8\u54c8\u54df\u5475\u5475'

错误提到'ascii' codec can't decode byte 0xe5，这是因为自动将str类型的变量按照默认的编码格式sys.getdefaultencoding()来解码，默认编码即ascii，而这个字符不在ascii的范围内，就出现了错误。

>>> import sys
>>> reload(sys)
<module 'sys' (built-in)>
>>> sys.setdefaultencoding('utf-8')
>>> a + b
u'\u554a\u54c8\u54c8\u54df\u5475\u5475'





文件读取和json解析

读文件得到的结果是str类型，以\x开头的十六进制表示。

caolingjun@panpandeMacBook-Pro ~/daily$ cat www.txt
# -*- coding: utf-8 -*-
b = u'哟呵呵'
bb = b.encode('utf-8')
print b
print bb

>>> f = open('/Users/caolingjun/daily/www.txt')
>>> r = f.read()
>>> r
"# -*- coding: utf-8 -*-\nb = u'\xe5\x93\x9f\xe5\x91\xb5\xe5\x91\xb5'\nbb = b.encode('utf-8')\nprint b\nprint bb\n"

而经过json解析后会自动转为unicode。






输出到文件
str类型可以输出到文件，而unicode类型必须先编码成str。

>>> a = '啊哈哈'
>>> a
'\xe5\x95\x8a\xe5\x93\x88\xe5\x93\x88'
>>> b = u'哟呵呵'
>>> b
u'\u54df\u5475\u5475'
>>> f = open('/Users/caolingjun/daily/abc.txt','w')
>>> f.write(a)
>>> f.write(b)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
UnicodeEncodeError: 'ascii' codec can't encode characters in position 0-2: ordinal not in range(128)


unicode输出到文件时的错误是由于默认编码为ascii，无法自动完成编码过程。如果将sys.getdefaultencoding()编码设置成了utf-8就可以自动完成转换过程了。


>>> import sys
>>> reload(sys)
<module 'sys' (built-in)>
>>> sys.setdefaultencoding('utf-8')
>>> f.write(b)

可成功插入数据
