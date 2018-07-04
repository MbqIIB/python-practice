#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/13 下午5:28
# @Author  : littlelinghome
# @Site    : 
# @File    : 1.py
# @Software: PyCharm

DB_FILE = 'staff.db'
COLUMNS = ['id','name','age','phone','dept','enrolled_date']

def load_db(db_file):
    """
    加载员工信息表，并转成指定的格式
    :param db_file:
    :return:
    """
    data = {}
    for i in COLUMNS:
        data[i] = []
    f = open(db_file,'r')
    for line in f:
        staff_id,name,age,phone,dept,enroll_date = line.strip().split(',')
        data['id'].append(staff_id)
        data['name'].append(name)
        data['age'].append(age)
        data['phone'].append(phone)
        data['dept'].append(dept)
        data['enrolled_date'].append(enroll_date)
    print(data)

load_db(DB_FILE)

