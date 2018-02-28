products = [['iphone8',6888],['macpro',14800],['小米6',2499],['coffee',31],['book',80],['nike shoes',799]]
while True:
    print ('-------------------商品列表-------------------')
    for index,i in enumerate(products):
        print ("%s. %s   %s" % (index,i[0],i[1]))
    choice = int(input('输入想买的商品编号：'))
    print (products[choice])