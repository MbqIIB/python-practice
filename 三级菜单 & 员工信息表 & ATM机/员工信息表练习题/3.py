#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/14 下午5:42
# @Author  : littlelinghome
# @Site    : 
# @File    : 3.py
# @Software: PyCharm


DB_FILE = 'staff.db'
COLUMNS = ['id','name','age','phone','dept','enrolled_date']


def print_log(msg,log_type="info"):
    if log_type == 'info':
        print(msg)
    elif log_type == 'error':
        print("\033[31;1m%s\033[0m"%msg)


def load_db(db_file):
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
    #print_log(data)
    return data

STAFF_DATA = load_db(DB_FILE)



def op_gt(column,condition_val):
    """
    :param column: eg.age
    :param condition_val: eg:22
    :return:
    """
    matched_records = []
    for index,val in enumerate(STAFF_DATA[column]):#"age":[22,245,2,5,2]
        if float(val) > float(condition_val):#匹配上了
            #print("match",val)
            #怎样获取匹配到的age所对应的行，下面的做法批量添加，但是若字段非常多，则显得冗余
            # matched_records.append(STAFF_DATA['id'][index])
            # matched_records.append(STAFF_DATA['name'][index])
            # matched_records.append(STAFF_DATA['age'][index])
            record = []
            for col in COLUMNS:
                record.append(STAFF_DATA[col][index])
            matched_records.append(record)
    #print("match records",matched_records)
    return matched_records

def op_lt(column,condition_val):
    matched_records = []
    for index,val in enumerate(STAFF_DATA[column]):#"age":[22,245,2,5,2]
        if float(val) < float(condition_val):#匹配上了
            record = []
            for col in COLUMNS:
                record.append(STAFF_DATA[col][index])
            matched_records.append(record)
    #print("match records",matched_records)
    return matched_records

def op_eq(column,condition_val):
    matched_records = []
    for index,val in enumerate(STAFF_DATA[column]):#"age":[22,245,2,5,2]
        if val == condition_val:#匹配上了
            record = []
            for col in COLUMNS:
                record.append(STAFF_DATA[col][index])
            matched_records.append(record)
    #print("match records",matched_records)
    return matched_records

def op_like(column,condition_val):
    matched_records = []
    for index,val in enumerate(STAFF_DATA[column]):#"age":[22,245,2,5,2]
        if condition_val in val:#匹配上了
            record = []
            for col in COLUMNS:
                record.append(STAFF_DATA[col][index])
            matched_records.append(record)
    #print("match records",matched_records)
    return matched_records


def syntax_where(clause):
    operators = {
        '>':op_gt,
        '<':op_lt,
        '=':op_eq,
        'like':op_like
    }
    for op_key,op_func in operators.items():
        if op_key in clause:
            column,val = clause.split(op_key)
            matched_data = op_func(column.strip(),val.strip()) #真正的查询数据
            print_log(matched_data)
            break
    else:
        print_log("语法错误：where条件只能支持[>,<,=,like]",'error')

"""
在for循环完整完成后才执行else;如果中途从break跳出，则连else一起跳出
"""



def syntax_parser(cmd):
    if cmd.split()[0] in ('find','add','del','update'):
        query_clause,where_clause = cmd.split("where")
        #print(query_clause,where_clause)
        syntax_where(where_clause)
    else:
        print_log("语法错误:\n[find\\add\del\\update] [column1,...] from [staff_table] [where] [column][>...][condition]",'error')


def main():
    while True:
        cmd = input("[staff_db:]").strip()
        if not cmd:continue
        syntax_parser(cmd)

main()


