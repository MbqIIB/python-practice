#-*- coding:utf8 -*-
#dic  = {'k1':'v1','k2':'v2','k3':'v3'}

#循环打印
# for k in dic:
#     print k,dic[k]

#添加
# dic['k4'] = 'v4'
# print dic

#删除指定键值
# dic.pop('k1')
# print dic

#获取不存在的键值
# print dic.get('v5')
# print 'v5' in dic
# print dic['v5']

#字典update方法的使用
# dic2 = {'k1':'v111','a':'b'}
# dic2.update(dic)
# print dic2

# lis = ['k',['qwe',20,{'k1':['tt',3,'1']},89],'ab']
# lis[1][2]['k1'][0] = 'TT'
# print lis

li = [1,2,3,'a','b',4,'c']
dic = {'k1':'v1'}
lista = []
listb = []
if dic.get('k1') == None:
    for index,i in enumerate(li):
        if index % 2 ==1:
            lista.append(i)
    dic1 = {'k1':lista}
    dic.update(dic1)
    print dic
else:
    if isinstance(dic.get('k1'),list):
        for index,v in enumerate(li):
            if index % 2 == 1:
                listb.append(v)
        dic.setdefault('k1',[]).extend(listb)
        print dic
    else:
        print "%s" % dic.get('k1')








