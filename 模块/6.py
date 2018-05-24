#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 下午9:06
# @Author  : littlelinghome
# @Site    : 
# @File    : 6.py
# @Software: PyCharm

import pickle
d = {'name':'alex','age':22}
l = [1,2,3,'rain']

#dumps不存放到文件内，直接把对象转化为字节（不转化为字符）
print(pickle.dumps(d))

#dump存放到文件内，因为是二进制的数据，所以这个文件打开这个文件显示不友好
pk = open('/Users/caolingjun/daily/www.pkl','wb')
pickle.dump(d,pk)

f = open('/Users/caolingjun/daily/www.pkl','rb')
d = pickle.load(f)
print(d)



json能序列化的数据类型包括：str,int,tuple,list,dict
pickle支持python里所有的数据类型，但是它只能在python里面使用，不能跨平台使用


