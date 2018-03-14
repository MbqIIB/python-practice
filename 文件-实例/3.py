#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/14 下午9:00
# @Author  : littlelinghome
# @Site    : 
# @File    : 3.py
# @Software: PyCharm



'''
concat拼接100条SQL，concat本身的语法用单引号，而拼接的SQL语句中含有字符串等时则用双引号括起来，
Python中的字符中（比如这里的str1,str2,str3等）利用双引号括起来，这里存在一个问题就是：
Python语法中的双引号和SQL语句中的双引号可能存在冲突，解决的办法是：把Python语法中的双引号转义符转义下。
最后，100张表的变量下标是通过最后的写文件时的变量实现的。
'''

for i in range(1,100):
        str1 = "select concat('update table_name"
        str2 = "set honordesc=\"',aa.str1,'(',year,'年',month,'月',')',aa.str2,'\"',' where honorid = ',honorid,';') from  (select honorid,DATE_FORMAT(createtime,'%Y') as year,DATE_FORMAT(createtime,'%m') as month, substring(honordesc,1,instr(honordesc,'第')-1) str1,substring(honordesc,instr(honordesc,'第')) str2  from  table_name"
        str3 = "where honortype in(4,23,24) and createtime>'2008-05-01 00:00:00' and honordesc not like '%(%)%' and honordesc not like '%（%）%')aa;"
        #print "%s%d %s%d %s" %(str1,i,str2,i,str3)
        txt = open('tmpresult.txt', 'a')
        txt.write(str1 + str(i) + ' ' +str2 + str(i) + ' ' + str3 + '\n')




