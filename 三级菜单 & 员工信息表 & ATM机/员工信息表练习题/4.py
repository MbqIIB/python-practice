#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/15 下午5:00
# @Author  : littlelinghome
# @Site    : 
# @File    : 4.py
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
    """
    解析查询语句并从data_set打印指定的列
    :param data_set: eg.['1', 'Alex Li', '22', '13651054608', 'IT', '2013-04-01']
    :param query_clause: eg.find name.age from staff_table
    :return:
    """
    filter_cols_tmp = query_clause.split("from")[0][4:].split(',')
    #print_log(filter_cols_tmp)
    filter_cols = [i.strip() for i in filter_cols_tmp] #获得没有没有空格的字段(使用的语法现象是：列表解析)
    #print_log(filter_cols)

    reformat_data_set = []
    for row in data_set:
        filtered_vals = [] #把要打印的字段放在这个列表里
        for col in filter_cols:
            col_index = COLUMNS.index(col)  #拿到列的索引，依此取出每条记录里对应索引的值
            filtered_vals.append(row[col_index])
            #print(col,row[col_index])
        reformat_data_set.append(filtered_vals)
    #print(reformat_data_set)
    for r in reformat_data_set:
        print(r)


def syntax_delete(data_set,query_clause):
    pass

def syntax_update(data_set,query_clause):
    pass

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

        #这里有需要分成多个分支去选择，同样我们可以写一个总的方法供调用
        # if query_clause.split()[0] == 'find':
        #     syntax_find()
        # elif query_clause.split()[0] == 'delete':
        #     syntax_delete()

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


