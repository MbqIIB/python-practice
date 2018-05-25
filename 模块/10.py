#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/25 上午10:28
# @Author  : littlelinghome
# @Site    : 
# @File    : 10.py
# @Software: PyCharm

import configparser

conf = configparser.ConfigParser()

#打印配置文件的标题，配置文件内部形式必须是等式形式，不能直接是个表达式
conf.read("/Users/caolingjun/daily/mysql_config.ini")
print(conf.sections())

#但是这样的打印方式没有default模块
print(conf.default_section)


#取某个模块内部的所有参数（不包括数值）
for k in conf["client"]:
    print(k)

#取某个模块的所有参数
for k,v in conf["client"].items():
    print(k,v)


#判断有没有某个参数
if 'port' in conf["mysqld"]:
    print('有这个参数')





caolingjun@panpandeMacBook-Pro ~/daily$ cat config_test.ini
[group1]
k1 = v1
k2:v2

[group2]
k1 = v1

#读配置文件
conf.read("/Users/caolingjun/daily/config_test.ini")
print(dir(conf))
print(conf.options("group1"))
print(conf["group1"]["k2"])


#增配置文件
conf.read("/Users/caolingjun/daily/config_test.ini")
conf.add_section("group3")
conf["group3"]["name"] = "Alex Li"
conf["group3"]["age"] = "22"
conf.write(open("/Users/caolingjun/daily/config_test_new.ini","w"))


#删除配置文件
conf.read("/Users/caolingjun/daily/config_test.ini")
conf.remove_option("group1","k2")
conf.remove_section("group1")
conf.write(open("/Users/caolingjun/daily/config_test2.ini","w"))