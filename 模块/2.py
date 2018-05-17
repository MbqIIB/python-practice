#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 上午9:15
# @Author  : littlelinghome
# @Site    : 
# @File    : 2.py
# @Software: PyCharm


time模块
time.strftime('%y-%m-%d')
time.strftime('%y-%m-%d %H:%M:%S')

把当前时间（字符串形式）转化为时间戳形式
s = time.strftime('%y-%m-%d %H:%M:%S') #找出当前时间
s2 = time.strptime(s,'%y-%m-%d %H:%M:%S') #把当前时间转化为时间对象
time.mktime(s2) #把时间对象转化为时间戳

把时间戳格式转化为字符串形式
time.gmtime(1526540899.0)  #把时间戳转化为时间对象
time.strftime('%y-%m-%d %H:%M:%S',time.gmtime()) #把时间对象转化为时间字符串





datetime模块
快速的拿到一个时间戳的年月日
datetime.date.fromtimestamp(time.time())

datetime模块最重要的作用是进行时间运算
当前时间：      datetime.datetime.now()
昨天的当前时间： datetime.datetime.now() - datetime.timedelta(1)
4天前的当前时间: datetime.datetime.now() - datetime.timedelta(days = 4)
其中，timedelta的参数可以为hours,minutes,seconds

时间的替换
d = datetime.datetime.now()
d.replace(year = 2016)
d.replace(year = 2016,month = 8)
d.replace(year = 2016,month = 8,day=21)





random模块
随机整数
random.randint(1,100)    #从1到100之间随机取个数,可以包含100
random.randrange(1,100)  #从1到100之间随机取个数,不包含100
随机浮点数
random.random()
随机字符串
random.choice('wefhurefg78043477&&')
随机返回列表
random.sample('se&*sefg8934',3)
洗牌打乱
d = list(range(100))
random.shuffle(d)





os模块
os.getcwd()  #得到当前工作目录，即当前python脚本工作的目录路径
os.listdir()  #返回指定目录下的所有文件和目录名
os.system()  #运行shell命令
shell命令 env 返回所有操作系统的环境变量
os.getenv('HOME') #读取操作系统环境变量HOME值
os.environ  #返回所有的环境变量,字典形式

设置系统的环境变量
export TEST = 33333
然后再env查看当前系统的系统变量

在Python中改变系统变量
import os
os.environ.setdefault('TEST','123')

注意以上2种方式添加的系统变量只在当前terminal下有效，每个终端只相当于一个命名空间


os.linesep #返回当前操作系统的换行符
os.stat('/Users/caolingjun/.oh-my-zsh')   #获取文件属性





sys模块
sys.argv    #命令行参数list，第一个元素是程序本身路径
sys.exit(n)  #退出程序，正常退出时exit
sys.stdout.write('wefer')  #标准输出，往屏幕上输出所打印的
sys.stdin.read()  #从屏幕上读取内容，读取多行
sys.stdin.readline()  #从屏幕上读取内容，只读取一行
sys.getdefaultencoding()   #获取内存数据存在文件里的默认编码