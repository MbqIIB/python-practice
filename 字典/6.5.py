#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 下午7:21
# @Author  : littlelinghome
# @Site    : 
# @File    : 6.5.py
# @Software: PyCharm

menu = {
  '北京':{
      '海淀':{
          '五道口':{
              'soho':{},
              '网易':{},
              'google':{},
          },
          '中关村':{
              '爱奇艺':{},
              '汽车之家':{},
              'youku':{},
          },
          '上地':{
              '百度':{}
          },
      },
      '昌平':{
          '沙河':{
              '老男孩':{},
              '北航':{}
          },
          '天通苑':{},
          '回龙观':{}
      },
      '朝阳':{},
      '东城':{},
  },
  '上海':{
        '闵行':{
            '人民广场':{
                '炸鸡店':{}
            },
        },
        '闸北':{
            '火车站':{
                '携程':{}
            }
        },
        '浦东':{},
   },
  '山东':{},
}


#保存进入的每一层
current_layer = menu
layers = []
while True:
    for k in current_layer:
        print(k)
    choice = input('>:').strip()
    if not choice:
        continue
    if choice in current_layer:
        layers.append(current_layer)
        #print(layers)
        current_layer = current_layer[choice]
    elif choice == 'b':
        if len(layers) != 0:
            current_layer = layers.pop()
        else:
            print('已经是顶层了')



