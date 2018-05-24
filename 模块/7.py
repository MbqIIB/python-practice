#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/24 下午2:29
# @Author  : littlelinghome
# @Site    : 
# @File    : 7.py
# @Software: PyCharm

#shelve与json,pickle模块的不同是，他可以多次dump(dumps),多次load(loads)
import shelve

names = ["alex","rain","test"]
info = {"name":"alex","age":22}
#利用shelve模块往文件里面写数据的时候，不需要给文件定义后缀，系统会自动给文件加个后缀.db
f = shelve.open('/Users/caolingjun/daily/shelve_test')

f["name"] = names
f["info_dic"] = info

f.close()


此时，打开刚刚生成的模块文件，会发现它是一个字典形式存放的数据
>>> import shelve
>>> f = shelve.open('shelve_test')
>>> f
<shelve.DbfilenameShelf object at 0x102a83c50>
>>> f.
f.cache       f.dict        f.keyencoding f.popitem(    f.update(
f.clear(      f.get(        f.keys(       f.setdefault( f.values(
f.close(      f.items(      f.pop(        f.sync(       f.writeback
>>> f.keys()
KeysView(<shelve.DbfilenameShelf object at 0x102a83c50>)
>>> list(f.keys())
['name', 'info_dic']
>>> list(f.items())
[('name', {'test', 'alex', 'rain'}), ('info_dic', {'name': 'alex', 'age': 22})]
>>> f.get('name')
{'test', 'alex', 'rain'}
>>> f.get('info_dic')
{'name': 'alex', 'age': 22}


修改模块字典内的数据
>>> f['name']
['alex', 'rain', 'test']
>>> f['name'] = ['alex1', 'rain2', 'test3']
>>> f['name']
['alex1', 'rain2', 'test3']

不过需要注意的是，要是更改数据的话，必须直接更改整个字典key的value，而不能修改字典的列表的内部元素，即只能修改整个列表的数据，而不能修改列表的内部元素





