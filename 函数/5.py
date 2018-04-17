#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 下午2:13
# @Author  : littlelinghome
# @Site    : 
# @File    : 5.py
# @Software: PyCharm


menu = {
    '北京':{
        '海淀':{'五道口':{'soho':{},'google':{}},'中关村':{'爱奇艺':{},'汽车之家':{}},'上地':{'百度':{},'联想':{}}},
        '昌平':{'回龙观':{'新浪':{},'网易':{}},'东小口':{'中科软':{},'中软':{}},'朱辛庄':{'智联':{},'拉钩':{}}},
        '朝阳':{'三里屯':{'太极华青':{},'北京云财':{}},'国贸':{'北京华志信':{},'北京伟业前程':{}},'望京':{'北京佰加星':{},'北京智达方通':{}}}
    },
    '上海':{
        '浦东':{'金桥':{'上海求步':{},'上海驰亚':{}},'合庆':{'中国电信':{},'上海顶通':{}}},
        '虹口':{'江湾':{'上海伦伟':{},'上海津腾':{}},'提篮桥':{'上海芒橙':{},'上海直达':{}}}
    },
    '广州':{
        '黄埔':{'板桥':{'恒大地产':{},'广州市蒲公英':{}},'官洲':{'广州动点网络':{},'广州玖维':{}}},
        '海珠':{'客村':{'广州海度':{},'广州艾秀':{}},'新港':{'广州优识':{},'广州合光':{}}}
    }
}
print("您可以输入'dir’来查看当前菜单下的子菜单,输入'cd ..'返回上一级目录,输入'cd /'返回一级菜单,输入'path'查看当前菜单路径,输入'quit’来退出程序\n")
level = 0 #当前数据项的级别,比如北京为1级
menus = [menu] #存储当前从0-5级的各级的字典'
path = [] #存放当前菜单路径
while(True):
    value = input('>>')
    if(value == 'dir'):
        print(list(menus[level]))
    elif(value == 'cd ..'): #返回上级
        if(level > 0):
            level -= 1
            menus.pop()
            path.pop()
    elif(value == 'cd /'): #返回根路径
        menus = [menu]
        level = 0
        path = []
    elif(value == 'quit'): #退出
        break
    elif(value == 'path'): #查看当前菜单路径
        paths = ''
        for item in path:
            paths = paths + '-' + item
        print(paths[1:])
    elif(value.startswith('cd ')): #进入输入的下一级菜单
        value = value[3:]
        if(value not in menus[level]):
            print('找不到当前项下的子菜单',value)
        else:
            level += 1
            menus.append(menus[level-1][value])
            path.append(value)
    else:
        print('不是查看菜单的命令')