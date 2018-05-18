#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/18 上午9:25
# @Author  : littlelinghome
# @Site    : 
# @File    : 3.py
# @Software: PyCharm

shutil模块

高级的 文件、文件夹、压缩包 处理模块

shutil.copyfileobj(fsrc, fdst[, length])
将文件内容拷贝到另一个文件中，可以部分内容

注意，这里如果文件名也叫shutil.py ，那么就有可能会出现一个问题，在一开始导入的时候（import shutil）相当于，自己导入自己了。切记不要把自己的模块名改成和标准库的模块的名字一样！



import shutil
f1 = open('/Users/caolingjun/Downloads/test1.txt','r')
f2 = open('/Users/caolingjun/Downloads/test2.txt','a')
shutil.copyfileobj(f1,f2)
shutil.copyfileobj(f1,f2,length=1)  #每次读入多少个长度，最终还是把f1中所有的内容追加到f2中的


shutil.copytree("/Users/caolingjun/Downloads","/Users/caolingjun/Downloads123")
复制整个路径

shutil.copytree("/Users/caolingjun/Downloads","/Users/caolingjun/Downloads123",ignore = shutil.ignore_patterns('test1.txt','test2.txt'))
忽略某些文件去递归创建一个新的文件




shutil.make_archive(base_name,format,...)
base_name: 压缩包的文件名，也可以是压缩包的路径。只是文件名时，则保存至当前目录，否则保存至指定路径
eg:
www                       =>   保存至当前路径
/Users/caolingjun/www     =>   保存至/Users/caolingjun/
format:  压缩包种类，"zip","tar","bztar","gztar"
root_dir: 要压缩的文件夹路径（默认当前目录）,被压缩的一定要是文件夹不能是文件
owner: 用户，默认当前用户
group: 组，默认当前组
logger: 用于记录日志，通常是logging.logger对象

eg:
shutil.make_archive("/Users/caolingjun/Downloads/wwwwwwww",'zip','/Users/caolingjun/PycharmProjects/untitled/python/模块/cross_module',owner='root')
压缩整个路径




压缩文件(zip)
import zipfile
z = zipfile.ZipFile('/Users/caolingjun/Downloads/wwwwwww.zip','w')
z.write('/Users/caolingjun/Downloads/test1.txt')
z.write('/Users/caolingjun/Downloads/test2.txt')
z.close()


解压刚刚压缩的文件(zip)
import zipfile
z = zipfile.ZipFile('/Users/caolingjun/Downloads/wwwwwww.zip','r')
z.extractall()
z.close()
注意，这里解压之后的文件是存放在当前程序所执行的路径下的


压缩文件(tar)
import tarfile
t = tarfile.open('/Users/caolingjun/Downloads/wwwwwww.tar','w')
t.add('/Users/caolingjun/Downloads/test1.txt')
t.add('/Users/caolingjun/Downloads/test2.txt')
t.close()

解压刚刚压缩的文件
import tarfile
z = tarfile.open('/Users/caolingjun/Downloads/wwwwwww.tar','r')
z.extractall('/Users/caolingjun/Downloads/123') #设置了解压路径
z.close()

