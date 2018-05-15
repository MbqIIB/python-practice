#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 下午2:23
# @Author  : littlelinghome
# @Site    : 
# @File    : 1.py
# @Software: PyCharm

在mac上安装Python下的模块管理工具pip的方法
https://blog.csdn.net/mike__lee/article/details/72593684


模块的好处
1. 提高可维护性
2. 可重用
3. 避免函数名和变量名冲突

模块分为三种：
1. 内置标准模块（又称为标准库），执行help('modules')可查看Python自带的所有自带模块列表
2. 第三方开源模块，可通过pip install 模块名联网安装
3. 自定义模块


模块调用
1. import module
2. from module import xxx
   eg: from os import rmdir,rename
3. from module.xxx.xxx import xxx as rename
   eg: from djando.core import handler
4. from module.xxx.xxx import * (不推荐这种方式)
   eg: from socket import *
   dir() 会发现有非常多的模块,此时需要用socket里面的某个模块是不需要socket.XXX，而直接XXX就可以了


模块一旦被调用，即相当于执行了另外一个py文件里的代码

my_module
def sayhi(name):
    print('hello',name)
sayhi('qqqq')

在交互器模式下导入，即相当于执行这个函数(此时我们是在文件所在路径下执行命令)
>> import my_module
hello qqqq


注意：模块名称不能是数字



如果我们在任意的路径下执行导入命令会报错
>>> import my_module
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'my_module'

但是，为什么我们在导入sys,os等模块的时候，可以在任意路径下导入
>>> import sys
>>> sys.path
['', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python36.zip', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/lib-dynload', '/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages']
你所需要导入的文件在以上这个路径下面才能正确导入，下面分别解释下以上路径
1. 第一个空字符串即代表是当前路径下
2. 第二个.zip文件是Python自带安装包里面的文件，几乎用不到
3. 第三个lib/python3.6 放的是Python与C语言相关的文件，几乎用不大
4. 第四个同上，几乎用不到
5. site-packages文件，第三方&内置的模块都存放在这里




开源模块安装，使用
eg:
https://pypi.python.org/ 是Python的开源模块库，在里面可与搜索到武沛齐的的代码模块pytyrion

下载源码安装
1. 下载，解压，cd PyTyrion-1.0.1
2. python3 setup.py build , 此时当前路径下就多了个build路径
3. python3 setup.py install , 其中这里有个需要注意的地方就是，这里有显示安装的地点
   Installed /Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/site-packages/PyTyrion-1.0.1-py3.6.egg
4. 将路径切换到以上路径下，发现确实有个文件PyTyrion-1.0.1-py3.6.egg , 有了这个.egg文件就表示可以正常导入了
5. 此时可以进行导入操作了
caolingjun@panpandeMacBook-Pro ~$ python3
Python 3.6.3 (v3.6.3:2c5fed86e0, Oct  3 2017, 00:32:08)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import Tyrion
>>> Tyrion.
Tyrion.Bottle(           Tyrion.Flask(            Tyrion.FrameworkFactory( Tyrion.Tornado(
Tyrion.Django(           Tyrion.Framework         Tyrion.setup(


删除已安装的模块
pip3 uninstall PyTyrio
此时再导入就会发现报错
>>> import Tyrion
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ModuleNotFoundError: No module named 'Tyrion'


在线安装
pip3 install PyTyrion
安装完了之后，再导入模块
>>> import Tyrion
>>> Tyrion.
Tyrion.Bottle(           Tyrion.Flask(            Tyrion.FrameworkFactory( Tyrion.Tornado(
Tyrion.Django(           Tyrion.Framework         Tyrion.setup(

