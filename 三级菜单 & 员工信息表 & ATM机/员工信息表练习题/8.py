#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/18 下午3:57
# @Author  : littlelinghome
# @Site    : 
# @File    : 8.py
# @Software: PyCharm

from tabulate import tabulate
import os

DB_FILE = 'staff.db'
COLUMNS = ['id','name','age','phone','dept','enrolled_date']


def print_log(msg,log_type="info"):
    if log_type == 'info':
        print("\033[32;1m%s\033[0m"%msg)
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

def save_db():
    """
    这个函数专门是用来针对update，delete等需要把所做的修改存放到硬盘的操作。
    即把内存数据存会硬盘
    :return:
    """
    f = open("%s.new"%DB_FILE,"w",encoding = "utf-8")
    for index,staff_id in enumerate(STAFF_DATA['id']):
        row = []
        for col in COLUMNS:
            row.append(STAFF_DATA[col][index])
        f.write(",".join(row) )
    f.close()
    os.rename("%s.new"%DB_FILE,DB_FILE)

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
    if '*' in filter_cols[0]:
        print(tabulate(data_set, headers=COLUMNS, tablefmt='grid'))
    else:
        reformat_data_set = []
        for row in data_set:
            filtered_vals = [] #把要打印的字段放在这个列表里
            for col in filter_cols:
                col_index = COLUMNS.index(col)  #拿到列的索引，依此取出每条记录里对应索引的值
                filtered_vals.append(row[col_index])
            reformat_data_set.append(filtered_vals)
        print(tabulate(reformat_data_set,headers=filter_cols,tablefmt='grid'))
    print_log("成功匹配到%s条数据!" % len(data_set))


def syntax_delete(data_set,query_clause):
    pass

def syntax_update(data_set,query_clause):

    formula_raw = query_clause.split('set')
    if len(formula_raw) > 1: # 有set关键字
        col_name,new_val = formula_raw[1].strip().split('=')
        for matched_row in data_set:
            staff_id = matched_row[0]
            staff_id_index = STAFF_DATA['id'].index(staff_id)
            STAFF_DATA[col_name][staff_id_index] = new_val
        print(STAFF_DATA)
        save_db() #把修改后的数据刷到硬盘上
        print_log("成功修改了%s条数据!"% len(data_set))
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

