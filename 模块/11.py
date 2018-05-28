#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/25 下午5:40
# @Author  : littlelinghome
# @Site    : 
# @File    : 11.py
# @Software: PyCharm



在Python程序背部实现与系统交互
>>> import os
>>> os.system("ls")


>>> import os
>>> os.popen("df -h")
<open file 'df -h', mode 'r' at 0x10cbfb5d0>
>>> f = os.popen("df -h")
>>> f.read()


在python2上还有这个命令
>>> import commands
>>> commends.getstatusoutput("df -h")


以上都是python与系统交互的方式,但是比较杂乱，官方推出了subprocess,目的是提供统一的模块来实现对系统命令或脚本的调用




subprocess的run方法

>>> import subprocess
>>> subprocess.run(['df','-h'])
Filesystem      Size   Used  Avail Capacity iused      ifree %iused  Mounted on
/dev/disk0s2   233Gi   57Gi  175Gi    25%  762263 4294205016    0%   /
devfs          189Ki  189Ki    0Bi   100%     654          0  100%   /dev
map -hosts       0Bi    0Bi    0Bi   100%       0          0  100%   /net
map auto_home    0Bi    0Bi    0Bi   100%       0          0  100%   /home
/dev/disk0s3   620Mi  502Mi  118Mi    81%      17 4294967262    0%   /Volumes/Recovery HD
CompletedProcess(args=['df', '-h'], returncode=0)

>>> a = subprocess.run(['df','-h'])
>>> a.returncode
0
>>> a.args
['df', '-h']





比如，微信的数据和QQ的数据是相互之间是不能访问的，但是它两却都是寄生在操作系统里面的，通过操作系统过渡下，二者就可以交互了。
那么python和shell之间的关系也是如此。subprocess就是在Python里面开一个独立新的进程来处理shell程序，它是通过一个中间管道来寄存数据的

>>> a = subprocess.run(['df','-h'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
>>> a.stdout
这样就直接拿到所有执行的结果，即在Python的程序里面拿到了所执行的shell命令的结果



>>> a = subprocess.run(['df','-sdfh'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/subprocess.py", line 418, in run
    output=stdout, stderr=stderr)
subprocess.CalledProcessError: Command '['df', '-sdfh']' returned non-zero exit status 64.

注： check=True，这个参数用来显示如果命令有误，则返回提示



如果利用subprocess处理管道命令，就不能再用列表的形式来拼接命令了
>>> a = subprocess.run(['df','-h','|','grep','devfs'],stdout=subprocess.PIPE,stderr=subprocess.PIPE,check=True)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Library/Frameworks/Python.framework/Versions/3.6/lib/python3.6/subprocess.py", line 418, in run
    output=stdout, stderr=stderr)
subprocess.CalledProcessError: Command '['df', '-h', '|', 'grep', 'devfs']' returned non-zero exit status 1.



如果有管道命令就直接把整条命令放到一句话里面,并且需要添加上参数shell=True
>>> a = subprocess.run('df -h |grep disk0s2',stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
然后读取这条记录
>>> a.stdout
b'/dev/disk0s2   233Gi   57Gi  175Gi    25%  762168 4294205111    0%   /\n'







subprocess的call()方法,这个方法不是非常的重要。。。

执行命令，返回命令执行状态，0或非0
>>> subprocess.call(['ls','-lsh'])

执行命令，如果命令结果是0，就正常返回，否则就抛异常
>>> subprocess.check_call(['ls','-l'])

接受字符串格式命令，返回元祖形式，第一个元素是执行状态，第二个是命令结果
>>> subprocess.getstatusoutput('ls /bin/ls')
(0, '/bin/ls')

接受字符串格式命令，并返回结果
>>> subprocess.getoutput('ls /bin/ls')
'/bin/ls'

执行命令，并返回结果，注意是返回结果，不是打印，下例结果返回给res
>>> res = subprocess.check_output(['ls','-l'])
>>> res
b'total 672\n-rw-r--r--   1 root  wheel     515  2 21  2017 afpovertcp.cfg\nlrwxr-xr-x








Popen()方法
args: shell命令，可以是字符串或者序列类型（如：list,元祖）
stdin,stdout,stderr: 分别表示程序的标准输入，输出，错误句柄
preexec_fn:只在unix平台下有效，用于指定一个可执行对象，它将在之前被调用
shell:同上
cwd:用于设置子进程的当前目录
env: 用于指定子进程的环境变量。如果env=None,子进程的环境变量将从父进程中继承

>>> a = subprocess.run('sleep 10',shell=True,stdout=subprocess.PIPE)
与
>>> a = subprocess.Popen('sleep 10',shell=True,stdout=subprocess.PIPE)
>>> a.poll()
>>> a.poll()
>>> a.poll()
0
有什么区别？
答：run方法是一直在当前进程中执行所有的命令，一条一条语句的往下运行
    Popen方法是开辟一个新的进程处理 Popen的这条命令，然后主程序接着往下执行，然后 Popen命令不同的通过poll把执行结果返回给主程序


>>> def sayhi():
...     print('run...haha')
>>> a = subprocess.Popen('sleep 10',shell=True,stdout=subprocess.PIPE,preexec_fn=sayhi)
>>> a.stdout
<_io.BufferedReader name=3>
>>> a.stdout.read()
b'run...haha\n'



>>> a = subprocess.Popen('echo $PWD;sleep 10',shell=True,cwd="/tmp",stdout=subprocess.PIPE,preexec_fn=sayhi)
>>> a.stdout.read()
b'run...haha\n/private/tmp\n'


>>> a = subprocess.Popen('echo $PWD;sleep 10',shell=True,stdout=subprocess.PIPE,preexec_fn=sayhi)
>>> a.stdout.read()
b'run...haha\n/etc\n'

即：如果不设置cwd="/tmp"，则直接显示的是当前命令窗口所在的路径




不停的往文件/Users/caolingjun/daily/sleep.log里面输入数字
>>> a = subprocess.Popen('for i in $(seq 1 100);do sleep 1;echo $i>>/Users/caolingjun/daily/sleep.log;done',shell=True,stdout=subprocess.PIPE)
>>> a.pid
1373
>>> a.terminate()
或者
>>> a.kill()
这样的话，文件/Users/caolingjun/daily/sleep.log就会停止写入

这样的杀死进程的方式等价于
>>> import os
>>> import signal
>>> a = subprocess.Popen('for i in $(seq 1 100);do sleep 1;echo $i>>/Users/caolingjun/daily/sleep.log;done',shell=True,stdout=subprocess.PIPE)
>>> a.pid
1919
>>> os.kill(1919,signal.SIGTERM)





caolingjun@panpandeMacBook-Pro ~/daily$ cat guess_age.py
# -*- coding:utf-8 -*-
age=26
user_guess = int(input('your guess:'))
if user_guess == age:
    print('恭喜你答对了')
elif user_guess < age:
    print('try bigger')
else:
    print('try smaller')

caolingjun@panpandeMacBook-Pro ~/daily$ cat guess_age2.py
# -*- coding:utf-8 -*-
count = 0
age = 25
while count < 3:
    age_guess = int(input('your age:'))
    if age_guess == age:
        print('恭喜你答对了')
        break
    elif age_guess < age:
        print('try bigger')
    else:
        print('try smaller')
    count += 1

>>> import subprocess
>>> a = subprocess.Popen('python3 guess_age.py',shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
>>> a.communicate(b'333')
(b'your guess:try smaller\n', b'')


>>> a = subprocess.Popen('python3 guess_age2.py',shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
>>> a.communicate(b'333')                                                                            (b'your age:try smaller\nyour age:', b'Traceback (most recent call last):\n  File "guess_age2.py", line 5, in <module>\n    age_guess = int(input(\'your age:\'))\nEOFError: EOF when reading a line\n')


即，这种communicate方法只能与系统交互一次，如果是多次交互数据的话，在第一次返回结果后就会报错了








