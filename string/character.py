# -*- coding:utf-8 -*-
names = ['oldboy','rain','jack','shanshan','blackgirl']
names.insert(4,'alex')
names[3] = '姗姗'
print names
print str(names).decode('string_escape')
#假如有一个GBK的字符aa='\\xC1\\xBD',要输出中文，那么就要利用decode("string_escape")命令，去掉转义字符\