#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/23 下午7:49
# @Author  : littlelinghome
# @Site    : 
# @File    : 5.py
# @Software: PyCharm

import json
data = {
    'role':[
        {'role':'monster','type':'pig','life':50},
        {'role':'hero','type':'关羽','life':80},
    ]
}
#dumps仅仅是转化为字符串,loads做相反的操作
d = json.dumps(data)
print(d,type(d))

d2 = json.loads(d)
print(d2['role'])



#dump不仅仅是转化为字符串，而且可以存放到文件里，它传入的参数不是文件名，而要是文件对象
f = open('/Users/caolingjun/daily/www.json','w')
json.dump(data,f)

f = open('/Users/caolingjun/daily/www.json','r')
data = json.load(f)
print(data)

注：一般，我们不多次进行dump到一个文件，然后再多次从文件load回来。因为多次dump到一个文件里面，多个数据类型之前无法分割