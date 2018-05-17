#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 下午3:44
# @Author  : littlelinghome
# @Site    : 
# @File    : views.py
# @Software: PyCharm




包（Package)
当你的模块文件越来越多，就需要对模块文件进行划分，比如把负责和数据库交互的放一个文件夹，把与页面交互相关的放一个文件夹



python3 manage.py  可以正常导入，但是python manage.py 执行却会报错
Q:为啥python3可以正常运行，但是python2运行的时候却会报错
A:crm本质上就是一个文件夹，并不是一个包。只是python3优化之后可以识别它，所以我们需要添加个文件__init__.py（空文件）
  把这个文件夹初始化为一个包，这样在python2的环境下也可以正常运行。文件__init__.py是放在crm的路径下的
  注：在pycharm里面，当一个文件夹变成一个包之后，它会在原来的文件图像中间加个洞
##############################################################################################

from proj import settings
def sayhi():
    print('hello world!')


注意了，按照之前我们所说的，proj/settings.py和views不在一级目录下，即它不在views模块的当前路径下，也不在系统路径下，是不能直接导入的
但是，我们在命令行下执行 python3 manage.py 是可以得到正确答案的。
因为，我们执行的是python3 manage.py ，而manage.py模块所在路径已经添加的系统路径下（sys.path）
所执行是哪个模块，那么那个文件所在的路径就是总入口，这个路径会添加到系统路径下，其他内部模块再多次调用都是不予考虑的



##############################################################################################


这次需要将proj路径下settings模块导入到views模块内，并且直接运行views模块，此时当前路径是当前路径是
/Users/caolingjun/PycharmProjects/untitled/python/模块/cross_module/crm
而导入的模块路径是/Users/caolingjun/PycharmProjects/untitled/python/模块/cross_module/proj
此时就需要将上一级目录/Users/caolingjun/PycharmProjects/untitled/python/模块/cross_module添加到系统路径下
import sys
sys.path.append('/Users/caolingjun/PycharmProjects/untitled/python/模块/cross_module')
     注意,不能是'/Users/caolingjun/PycharmProjects/untitled/python/模块/cross_module/proj'
     否则，我们就不要from proj import settings，而是直接import settings
from proj import settings
def sayhi():
    print('hello world!')


##############################################################################################
#上面我们采用的方法是在系统路径里面添加绝对路径，那么接下来我们来看看相对路径的情况

import sys,os
print(dir())
print(__file__) #打印到当前文件的绝对路径
BASE_DIR_1 = os.path.dirname(__file__)
print(BASE_DIR_1)
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
print(BASE_DIR)

把上面动态获取到的路径BASE_DIR添加到系统变量里面
sys.path.append(BASE_DIR)
from proj import settings



###############################################################################################
以上相对路径的例题在pycharm里面可以正常运行，但是到了命令行里运行：python3 views.py却会报错。。。
因为，print(__file__)在pycharm里面打印的是绝对路径，在命令行里面打印的是相对路径

import sys,os
print(__file__)
print(os.path.abspath(__file__))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)

sys.path.append(BASE_DIR)
from proj import settings


##############################################################################################
相对导入,执行manage.py（它导入了views），在views里面导入了models模块，按道理views和models属于同一级别
那么在views里面可以直接导入models，但是要注意的是我们运行的是manage模块，所以当前路径应该以此为准
from . import models
等价于 from crm import models
def sayhi():
    print('hello world!')



##############################################################################################
相对导入
from proj import settings
不等价于from ..proj import settings
会报错：ValueError: attempted relative import beyond top-level package
注：涉及到相对导入时，package所对应的文件夹必须正确地被python 解释器视作package,
而不是普通的文件夹，否则由于不被视作package，无法利用package之间的嵌套关系实现python中包的相对导入


文件夹被python解释器视作package需要满足两个条件：
1. 文件夹中必须要__init__.py文件，该文件可以为空，但必须存在该文件
2. 不能作为顶层模块来执行该文件夹中的py文件（即不能作为主函数的入口）

注：from ..proj import settings含义是：当前模块views.py所在路径的上两级目录，然后再进入到proj这个路径下面找settings模块
正确的模块架构可以是这样的：


                              --__init__.py
                        --core
                              --views.py
    --cross_module
                  -crm        --__init__.py
                        --proj
                              --settings
                        --manage.py