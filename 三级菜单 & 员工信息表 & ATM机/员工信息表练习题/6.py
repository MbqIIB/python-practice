#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/17 下午11:20
# @Author  : littlelinghome
# @Site    : 
# @File    : 6.py
# @Software: PyCharm
from tabulate import tabulate

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
    matched_records = []
    for index,val in enumerate(STAFF_DATA[column]):#"age":[22,245,2,5,2]
        if float(val) > float(condition_val):#匹配上了
            record = []
            for col in COLUMNS:
                record.append(STAFF_DATA[col][index])
            matched_records.append(record)
    return matched_records

def op_lt(column,condition_val):
    matched_records = []
    for index,val in enumerate(STAFF_DATA[column]):#"age":[22,245,2,5,2]
        if float(val) < float(condition_val):#匹配上了
            record = []
            for col in COLUMNS:
                record.append(STAFF_DATA[col][index])
            matched_records.append(record)
    return matched_records

def op_eq(column,condition_val):
    matched_records = []
    for index,val in enumerate(STAFF_DATA[column]):#"age":[22,245,2,5,2]
        if val == condition_val:#匹配上了
            record = []
            for col in COLUMNS:
                record.append(STAFF_DATA[col][index])
            matched_records.append(record)
    return matched_records

def op_like(column,condition_val):
    matched_records = []
    for index,val in enumerate(STAFF_DATA[column]):#"age":[22,245,2,5,2]
        if condition_val in val:#匹配上了
            record = []
            for col in COLUMNS:
                record.append(STAFF_DATA[col][index])
            matched_records.append(record)
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
            #print_log(matched_data)
            return matched_data
    else:
        print_log("语法错误：where条件只能支持[>,<,=,like]",'error')



def syntax_find(data_set,query_clause):
    filter_cols_tmp = query_clause.split("from")[0][4:].split(',')
    filter_cols = [i.strip() for i in filter_cols_tmp] #获得没有没有空格的字段

    reformat_data_set = []
    for row in data_set:
        filtered_vals = [] #把要打印的字段放在这个列表里
        for col in filter_cols:
            col_index = COLUMNS.index(col)  #拿到列的索引，依此取出每条记录里对应索引的值
            filtered_vals.append(row[col_index])
        reformat_data_set.append(filtered_vals)
    print(tabulate(reformat_data_set))
    print(tabulate(reformat_data_set,tablefmt = 'grid'))
    print(tabulate(reformat_data_set,headers=filter_cols,tablefmt='grid'))

def syntax_delete(data_set,query_clause):
    pass

def syntax_update(data_set,query_clause):
    """
    注意了，这样的update虽然实现了功能，但是它只是在内层里更改里数据，文件内并没有更改。
    另外，不能这么写 where name="Alex Li"，而只能这么写where name=Alex Li
    :param data_set: eg.[['1', 'Alex Li', '22', '13651054608', 'IT', '2013-04-01']...]
    :param query_clause: eg.update staff_table set age=25
    :return:
    """
    formula_raw = query_clause.split('set')
    if len(formula_raw) > 1: # 有set关键字
        col_name,new_val = formula_raw[1].strip().split('=')
        #col_index = COLUMNS.index(col_name)
        #循环data_set，取到每条记录的id，拿着这个id到STAFF_DATA['id']里找到对应的id的索引，再拿这个索引去
        #STAFF_DATA['age']列表里，改对应索引的值
        for matched_row in data_set:
            staff_id = matched_row[0]
            staff_id_index = STAFF_DATA['id'].index(staff_id)
            STAFF_DATA[col_name][staff_id_index] = new_val
        print(STAFF_DATA)
    else:
        print_log("语法错误：未检测到set关键字!","error")

def syntax_add(data_set,query_clause):
    pass



def syntax_parser(cmd):

    syntax_list = {
        'find':syntax_find,
        'delete':syntax_delete,
        'update':syntax_update,
        'add':syntax_add,
    }


    if cmd.split()[0] in ('find','add','del','update'):
        query_clause,where_clause = cmd.split("where")
        matched_records = syntax_where(where_clause)
        cmd_action = query_clause.split()[0]
        if cmd_action in syntax_list:
            syntax_list[cmd_action](matched_records,query_clause)
    else:
        print_log("语法错误:\n[find\\add\del\\update] [column1,...] from [staff_table] [where] [column][>...][condition]",'error')


def main():
    while True:
        cmd = input("[staff_db:]").strip()
        if not cmd:continue
        syntax_parser(cmd.strip())

main()


