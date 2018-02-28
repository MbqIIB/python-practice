products = [['iphone8',6888],['macpro',14800],['小米6',2499],['coffee',31],['book',80],['nike shoes',799]]
print (products)
print ('-------------------商品列表-------------------')
for index,i in enumerate(products):
    #print index,i[0],i[1]
    #格式化打印结果值
    print ("%s. %s   %s" % (index,i[0],i[1]))