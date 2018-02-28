li = [1,2,3,'a','b',4,'c']
dic = {'k1':[11,22]}
lista = []
listb = []
if dic.get('k1') == None:
    for index,i in enumerate(li):
        if index % 2 ==1:
            lista.append(i)
    dic1 = {'k1':lista}
    dic.update(dic1)
    print(dic)
else:
    if isinstance(dic.get('k1'),list):
        for index,v in enumerate(li):
            if index % 2 == 1:
                listb.append(v)
        dic.setdefault('k1',[]).extend(listb)
        print(dic)
    else:
        print("%s" % dic.get('k1'))