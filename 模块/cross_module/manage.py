#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/16 下午3:36
# @Author  : littlelinghome
# @Site    : 
# @File    : manage.py
# @Software: PyCharm


# from cross_module.crm import views  不用这么写，因为crm是和manage.py属于同一级别的

# 一定要从当前可执行文件manage.py所在的路径下开始寻找你所要导入的模块，如果找不到的话就要从当前路径下的下一级查找

from crm import views
views.sayhi()







