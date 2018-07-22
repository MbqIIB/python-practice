#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/7/22 下午1:08
# @Author  : littlelinghome
# @Site    : 
# @File    : utils.py
# @Software: PyCharm



def print_error(msg):
    print("\033[31;1mError:\033[0m%s" % msg)


def print_warning(msg):
    print("\033[33;1mWarning:\033[0m%s" % msg)


def print_info(msg):
    print("\033[32;1mInfo:\033[0m%s" % msg)