#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/29 下午5:53
# @Author  : littlelinghome
# @Site    : 
# @File    : 13.py
# @Software: PyCharm

Python使用logging模块记录日志涉及四个主要类

logger提供了应用程序可以直接使用的接口
handler将（logger创建的）日志记录发送到合适的目的输出
filter提供了细度设备来决定输出哪条日志记录
formatter决定日志记录的最终输出格式


import logging
#1. 生成 logger 对象
logger = logging.getLogger("wb")

#2. 生成 handler 对象，把 handler 对象绑定到logger
ch = logging.StreamHandler()
fh = logging.FileHandler("/Users/caolingjun/daily/web.log")
logger.addHandler(ch)
logger.addHandler(fh)

#3. 生成 formatter 对象，把formatter对象绑定到handler对象
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(lineno)d - %(message)s')
ch.setFormatter(console_formatter)
fh.setFormatter(file_formatter)



logger.debug("test.log")     #没有结果
logger.info("test log 2")    #没有结果

logger.warning("test.log")   #文件，屏幕都有结果
logger.error("test.log")     #文件，屏幕都有结果

#所以，当你不设置日志级别的时候，默认是只显示warning及以上级别的日志








#1. 生成 logger 对象，并且设置日志级别
logger = logging.getLogger("wb")
logger.setLevel(logging.INFO)

#2. 生成 handler 对象，把 handler 对象绑定到logger。对 handler 也设置级别（输出到屏幕的为debug模式，输出到文件的为warning模式）
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
fh = logging.FileHandler("/Users/caolingjun/daily/web.log")
fh.setLevel(logging.WARNING)

logger.addHandler(ch)
logger.addHandler(fh)

#3. 生成 formatter 对象，把formatter对象绑定到handler对象
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(lineno)d - %(message)s')
ch.setFormatter(console_formatter)
fh.setFormatter(file_formatter)



注意了，此时相当于设置了3个地方的日志级别,分别为
global: info
console: debug
file: warning
会发现，其中全局的日志级别最高


但是，如果我们此时把全局的日志级别注释掉，以为屏幕会输出debug级别的日志，结果发现啥也没有，
这是因为全局的默认级别是warning,低于warning级别都不会再输出了.
那么单独设置屏幕的日志级别有什么用？
当全局的日志设置为最低级别，输出的屏幕的时候会参考屏幕的级别的日志


logger.debug("test.log")
logger.info("test log 2")
logger.warning("test.log")
logger.error("test.log")










日志过滤
class IgnoreBackupLogFilter(logging.Filter):
    """忽略db backup的日志"""
    def filter(self, record):#这是固定写法
        return "db backup" not in record.getMessage()


logger = logging.getLogger("wb")
logger.setLevel(logging.DEBUG)
#把filter对象添加到logger中
logger.addFilter(IgnoreBackupLogFilter())

ch = logging.StreamHandler()
fh = logging.FileHandler("/Users/caolingjun/daily/web.log")

logger.addHandler(ch)
logger.addHandler(fh)

file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(lineno)d - %(message)s')
ch.setFormatter(console_formatter)
fh.setFormatter(file_formatter)


logger.debug("test.log")
logger.debug("test log db backup 3")
logger.info("test log 2")
logger.warning("test.log")
在屏幕上只会输出3条日志，以为第二条日志被过滤掉了









#日志截断（按大小分割）
from logging import handlers

logger = logging.getLogger("wb")
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
fh = handlers.RotatingFileHandler("/Users/caolingjun/daily/web.log",maxBytes=10,backupCount=3)

logger.addHandler(ch)
logger.addHandler(fh)

file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(lineno)d - %(message)s')
ch.setFormatter(console_formatter)
fh.setFormatter(file_formatter)


logger.debug("test.log")
logger.debug("test log db backup 3")
logger.info("test log 2")
logger.warning("test.log")









#日志截断（按时间分割）
from logging import handlers

logger = logging.getLogger("wb")
logger.setLevel(logging.DEBUG)

ch = logging.StreamHandler()
fh = handlers.TimedRotatingFileHandler("/Users/caolingjun/daily/web.log",when="S",interval=5,backupCount=3)

logger.addHandler(ch)
logger.addHandler(fh)

file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(lineno)d - %(message)s')
ch.setFormatter(console_formatter)
fh.setFormatter(file_formatter)


logger.debug("test.log")
logger.debug("test log db backup 3")
logger.info("test log 2")
logger.warning("test.log")

