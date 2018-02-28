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
        print(k)
    choice = input(">:").strip()
    if not choice:continue #如果用户输入的是回车，空格等。那么跳出此层循环，让用户再重新输入
    if choice in menu:
        while True:#进入第二层
            for k in menu[choice]:
                print(k)
            choice2 = input('>>:').strip()
            if not choice2: continue
            if choice2 in menu[choice]:
                print('go to',menu[choice][choice2])
                while True: #进入第3层
                    for k in menu[choice][choice2]:
                        print(k)
                    choice3 = input('>>>:').strip()
                    if not choice3:continue
                    if choice3 in menu[choice][choice2]:
                        print('go to',menu[choice][choice2][choice3])
                    else:
                        print('节点不存在')

            else:
                print('节点不存在')