#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/6/14 上午10:31
# @Author  : littlelinghome
# @Site    : 
# @File    : 2.py
# @Software: PyCharm

DB_FILE = 'staff.db'
COLUMNS = ['id','name','age','phone','dept','enrolled_date']


def print_log(msg,log_type="info"):
    """
    设置颜色的格式：
    \033[0m  关闭所有属性
    \033[1m   设置高亮度
    \033[30m   --   \033[37m   设置前景色
    \033[40m   --   \033[47m   设置背景色

    \e[背景色;前景色;高亮m
    \033[背景色;前景色;高亮m

    第一个参数(终端颜色)：0 透明,1 高亮 40 黑, 41 红, 42 绿, 43 黄, 44 蓝 45 紫, 46 青绿, 47白（灰）---(可省略)
    第二个参数(文本的颜色): 30 黑 31 红, 32 绿, 33 黄, 34 蓝, 35 紫, 36 青绿, 37 白（灰）
    第三个参数：高亮是1，不高亮是0
    第四个参数为m: 注意m后面紧跟字符串。

    :param msg:
    :param log_type:
    :return:
    """
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
    return data

STAFF_DATA = load_db(DB_FILE)

############ 以上是实现把文件按列划分存放到字典中 #################
def op_gt():
    pass
def op_lt():
    pass
def op_eq():
    pass
def op_like():
    pass

def syntax_where(clause):
    """
    -gt  ： (greater than) 大于
    -lt  ： (less than) 小于
    -ge  ： (greater than or equal) 大于或等于
    -le  ： (less than or equal)小于或等于

    解析where条件，并过滤数据
    :param clause:
    :return:
    """
    # if '>' in clause:
    #     column,operator,condition = clause.split('>')
    # elif '<' in clause:
    #     column, operator, condition = clause.split('<')

#在这里有一个小技巧，要判断where后面的条件是什么符号（>,<,=等等）,那么我们可能就需要多个if条件，显得很low

    operators = {
        '>':op_gt,
        '<':op_lt,
        '=':op_eq,
        'like':op_like
    }
    for op_key,op_func in operators.items():
        if op_key in clause:
            column,val = clause.split(op_key)
            break
    else:#只有在for执行完成，且没有被break的情况下，才执行
        print_log("语法错误：where条件只能支持[>,<,=,like]",'error')






def syntax_parser(cmd):
    """
    解析语句并执行
    :param cmd:
    :return:
    """
    #find name,age from staff_table where age>22
    if cmd.split()[0] in ('find','add','del','update'):
        query_clause,where_clause = cmd.split("where")
        print(query_clause,where_clause)
        syntax_where(where_clause)
    else:
        print_log("语法错误:\n[find\\add\del\\update] [column1,...] from [staff_table] [where] [column][>...][condition]",'error')


def main():
    """
    让用户数据语句，并执行
    :return:
    """
    while True:
        cmd = input("[staff_db:]").strip()
        if not cmd:continue  #cmd非空，那么not cmd为假，此句不执行；只有当cmd为空时，not cmd为真，if条件为真，此句执行
        syntax_parser(cmd)


main()