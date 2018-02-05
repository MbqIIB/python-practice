# -*- coding:utf-8 -*-
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

while True:
    for k in menu:
        print k
    choice = raw_input(">>:").strip()
    if not choice:continue

    if choice in menu:
        for k in menu[choice]:
            print k