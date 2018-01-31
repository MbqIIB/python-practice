# # -*- coding:utf-8 -*-
# names = ['alex','jack',2,'rain','mack',2,'racheal','shanshan',2,'longting']
# # 不加索引值的打印
# for i in names:
#     print i
#
# # count 计算器循环打印
# count = 0
# for i in names:
#     print count,i
#     count += 1
#
# # enumerate 枚举
# for i in enumerate(names):
#     print i
#
# # enumerate 枚举
# for index,i in enumerate(names):
#     print index,i
#
# #把枚举值为偶数的值改成-1
# for index,i in enumerate(names):
#     if index % 2 == 0:
#         names[index] = -1
# print names


# 选取相同数值的第二个值的索引值
# names = ['alex','jack',2,'rain','mack',2,'racheal','shanshan',2,'longting']
# print names.index(2)
# first_index = names.index(2)
# new_list = names[first_index + 1 :]
# print new_list
# second_index = new_list.index(2)
# print second_index
# second_val = names[first_index + second_index + 1]
# print second_val
# print first_index + second_index + 1

# products = [['iphone8',6888],['macpro',14800],['小米6',2499],['coffee',31],['book',80],['nike shoes',799]]
# print str(products).decode('string_escape')
# print '-------------------商品列表-------------------'
# for index,i in enumerate(products):
#     #print index,i[0],i[1]
#     #格式化打印结果值
#     print "%s. %s   %s" % (index,i[0],i[1])


products = [['iphone8',6888],['macpro',14800],['小米6',2499],['coffee',31],['book',80],['nike shoes',799]]
#1.先实现不断的询问购买什么
# while True:
#     print '-------------------商品列表-------------------'
#     for index,i in enumerate(products):
#         print "%s. %s   %s" % (index,i[0],i[1])
#     choice = input('输入想买的商品编号：')
#     print products[choice]

#2.把购买的商品存放到购物车内
# shopping_cat = []
# while True:
#     print '-------------------商品列表-------------------'
#     for index,i in enumerate(products):
#         print "%s. %s   %s" % (index,i[0],i[1])
#     choice = input('输入想买的商品编号：')
#     shopping_cat.append(products[choice])
#     print "added product %s into shopping cat." %(products[choice])

#3.输入 q 退出循环，判断字符串是否是数字
# shopping_cat = []
# while True:
#     print '-------------------商品列表-------------------'
#     for index,i in enumerate(products):
#         print "%s. %s   %s" % (index,i[0],i[1])
#     choice = raw_input('输入想买的商品编号：')
#     if str(choice).isdigit():
#         choice = int(choice)
#         shopping_cat.append(products[choice])
#         print "added product %s into shopping cat." %(products[choice])
#     elif choice == 'q':
#         print "----------你已购买一下产品------------"
#         for index,i in enumerate(shopping_cat):
#             print "%s. %s   %s" % (index, i[0], i[1])
#         break


#4.除了 break 退出循环外，也可以利用标志物退出循环
# shopping_cat = []
# run_flag = True
# while run_flag:
#     print '-------------------商品列表-------------------'
#     for index,i in enumerate(products):
#         print "%s. %s   %s" % (index,i[0],i[1])
#     choice = raw_input('输入想买的商品编号：')
#     if str(choice).isdigit():
#         choice = int(choice)
#         shopping_cat.append(products[choice])
#         print "added product %s into shopping cat." %(products[choice])
#     elif choice == 'q':
#         print "----------你已购买一下产品------------"
#         for index,i in enumerate(shopping_cat):
#             print "%s. %s   %s" % (index, i[0], i[1])
#         #break
#         run_flag = False


#5.再优化，输入的索引在原有产品的索引范围之外
# shopping_cat = []
# run_flag = True
# while run_flag:
#     print '-------------------商品列表-------------------'
#     for index,i in enumerate(products):
#         print "%s. %s   %s" % (index,i[0],i[1])
#     choice = raw_input('输入想买的商品编号：')
#     if str(choice).isdigit():
#         choice = int(choice)
#         if choice >= 0 and choice < len(products):
#             print choice
#             shopping_cat.append(products[choice])
#             print "added product %s into shopping cat." %(products[choice])
#         else:
#             print "商品不存在"
#     elif choice == 'q':
#         print "----------你已购买一下产品------------"
#         for index,i in enumerate(shopping_cat):
#             print "%s. %s   %s" % (index, i[0], i[1])
#         run_flag = False

#6. 当什么也没有购买的时候也会显示"----------你已购买一下产品------------"。打印前做下判断，看看购物车里面有没有东西
shopping_cat = []
run_flag = True
while run_flag:
    print '-------------------商品列表-------------------'
    for index,i in enumerate(products):
        print "%s. %s   %s" % (index,i[0],i[1])
    choice = raw_input('输入想买的商品编号：')
    if str(choice).isdigit():
        choice = int(choice)
        if choice >= 0 and choice < len(products):
            print choice
            shopping_cat.append(products[choice])
            print "added product %s into shopping cat." %(products[choice])
        else:
            print "商品不存在"
    elif choice == 'q':
        if len(shopping_cat) > 0:
            print "----------你已购买一下产品------------"
            for index,i in enumerate(shopping_cat):
                print "%s. %s   %s" % (index, i[0], i[1])
        run_flag = False

