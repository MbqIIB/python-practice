#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/28 下午8:59
# @Author  : littlelinghome
# @Site    : 
# @File    : 12.py
# @Software: PyCharm

很多程序都有记录日志的需求，并且日志中包含的信息既有正常的程序访问日志，还可能有错误，警告等信息的输出，
Python的logging的日志可以分为debug(),info(),warning(),error() and critical() 5个级别



import logging
信息直接输出在屏幕上
logging.warning("user [alex] attempted wrong password more than 3 times")
logging.critical("server is down")



信息输出到文件
logging.basicConfig(filename='/Users/caolingjun/daily/logtest.log',level=logging.INFO)
logging.debug('this message should go to the log file')
logging.info('so should this')
logging.warning('and this,too')
注：此时文件/Users/caolingjun/daily/logtest.log里面只有info,warning的两行数据。原因是level=logging.INFO，那么只会记录INFO和比INFO更高的记录



输出的日志没有时间
logging.basicConfig(filename='/Users/caolingjun/daily/logtest.log',
                    level=logging.INFO,
                    format='%(asctime)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
logging.debug('this message should go to the log file')
logging.info('so should this')
logging.warning('and this,too')



输出数字级别的日志形式
logging.basicConfig(filename='/Users/caolingjun/daily/logtest.log',
                    level=logging.INFO,
                    format='%(asctime)s -%(levelno)s- %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
logging.debug('this message should go to the log file')
logging.info('so should this')
logging.warning('and this,too')



输出文本形式的日志形式
logging.basicConfig(filename='/Users/caolingjun/daily/logtest.log',
                    level=logging.INFO,
                    format='%(asctime)s -%(levelname)s- %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
logging.debug('this message should go to the log file')
logging.info('so should this')
logging.warning('and this,too')



调用日志输出函数模块的完整路径，有时候没有显示
logging.basicConfig(filename='/Users/caolingjun/daily/logtest.log',
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(pathname)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
logging.debug('this message should go to the log file')
logging.info('so should this')
logging.warning('and this,too')



输出函数的模块文件名
logging.basicConfig(filename='/Users/caolingjun/daily/logtest.log',
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(filename)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
logging.debug('this message should go to the log file')
logging.info('so should this')
logging.warning('and this,too')



输出模块名,其实 filename 和 module 只需要保留一个就可以了，前者带有.py后缀，后者没有后缀
logging.basicConfig(filename='/Users/caolingjun/daily/logtest.log',
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(filename)s:%(module)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
def sayhi():
    logging.error("from sayhi....")
sayhi()

logging.debug('this message should go to the log file')
logging.info('so should this')
logging.warning('and this,too')




输出函数名
logging.basicConfig(filename='/Users/caolingjun/daily/logtest.log',
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(filename)s:%(funcName)s %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
def sayhi():
    logging.error("from sayhi....")
sayhi()

logging.debug('this message should go to the log file')
logging.info('so should this')
logging.warning('and this,too')



输出函数的语句所在的代码行
logging.basicConfig(filename='/Users/caolingjun/daily/logtest.log',
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(filename)s:%(funcName)s:%(lineno)d %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')
def sayhi():
    logging.error("from sayhi....")
sayhi()

logging.debug('this message should go to the log file')
logging.info('so should this')
logging.warning('and this,too')



输出进程ID
logging.basicConfig(filename='/Users/caolingjun/daily/logtest.log',
                    level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(filename)s:%(funcName)s:%(lineno)d:%(process)d %(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p')

def sayhi():
    logging.error("from sayhi....")
sayhi()

logging.debug('this message should go to the log file')
logging.info('so should this')
logging.warning('and this,too')

