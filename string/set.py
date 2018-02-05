# -*- coding:utf-8 -*-

# 集合的最主要的任务就是对比两批数据：交集，并集，差集
#1。去重
#2。关系测试
#3. 集合是无序

# iphone7 = ['alex','rain','jack','old_driver']
# iphone8 = ['alex','shanshan','jack','old_boy']

#取二者交集
# for i in iphone7:
#     for v in iphone8:
#         if v == i:
#             print v
#取二者交集
# both = []
# for i in iphone7:
#     if i in iphone8:
#         both.append(i)
# print both

#取iphone7有但是iphone8没有的数据
# diff = []
# for i in iphone7:
#     if i not in iphone8:
#         diff.append(i)
# print diff



#交集
iphone7 = {'alex','rain','jack','old_driver'}
iphone8 = {'alex','shanshan','jack','old_boy'}
#print iphone7.intersection(iphone8)
#print iphone7 & iphone8

#差集
print iphone7.difference(iphone8)
print iphone7 - iphone8

#并集
print iphone8.union(iphone7)
print iphone8 | iphone7

#取交集相反的集合
print (iphone7 | iphone8) - (iphone7 & iphone8)

#对称差集：只买了iphone7 或者 只买了iphone8的人
print iphone7.symmetric_difference(iphone8)
print iphone7 ^ iphone8


#超集，子集
print iphone8.issubset(iphone7)
print iphone8 >= iphone7
print iphone8.issuperset(iphone7)
print iphone8 <= iphone7

#是否相交,False代表相交
print iphone7.isdisjoint(iphone8)


menu = {'a':1,'b':2,'c':3}
