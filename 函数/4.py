#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/4/16 下午8:37
# @Author  : littlelinghome
# @Site    :
# @File    : 4.py
# @Software: PyCharm


goods = {'001':['优衣库裤子',499],'002':['小米手机',2499],'003':['iPhone7',4199],'004':['联想电脑',4999],'005':['智力车厘子',36],'006':['python从入门到放弃',79]}
buyCart = []
try:
    money = int(input('请输入您的金额：'))
except ValueError:
    print('请输入正确的金额格式')
    exit()
print('-----------商品列表---------------')
print('商品编号    名称   价格')
for item in goods:
    s = '%s    \t%s    \t%d' % (item,goods.get(item)[0],goods.get(item)[1])
    print(s)
while(True):
    goodsNO = input('\n请选择要添加的商品编号：')
    if(goodsNO not in goods):
        print('\n选择的商品编号不存在,请重新选择!')
        continue
    if(goods.get(goodsNO)[1] > money):
        print('\n金额不足,无法添加该商品！')
    else:
        buyCart.append(goodsNO)
        money = money - goods.get(goodsNO)[1]
        print('\n当前余额为%d' % money)
    yn = input('\n是否继续添加商品?退出输入n,继续按其他任意键:')
    if yn == 'n':
        print('\n\n-------已购买的商品----------')
        print('商品编号    名称   价格')
        for item in buyCart:
            s = '%s \t %s \t %s' % (item,goods.get(item)[0],goods.get(item)[1])
            print(s)
        print('\n余额为：' + str(money))
        break

