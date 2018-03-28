#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/3/28 下午8:01
# @Author  : littlelinghome
# @Site    : 
# @File    : 3.py
# @Software: PyCharm


#用户信息
#users={'zhangsan':['张三','123','24',1],'lisi':['李四','456','24',1,'wangwu':['王五','789','24',0]}


import pickle

#注册用户
def regist():
    username = input('请填写登陆账号>>')
    pwd = input('请填写登陆密码>>')
    nickname = input('请填写昵称>>')
    age = input('请填写年龄>>')
    users[username] = [nickname,pwd,age,1]
    f = open('user.pkl','wb')
    pickle.dump(users,f)
    f.close()
    print('注册成功')

#锁定用户
def lockUser(users,username):
    users[username][3] = 0
    f = open('user.pkl','wb')
    pickle.dump(users,f)
    f.close()

#解锁用户
def unLockUser(username):
    fr = open('user.pkl','rb')
    users = pickle.load(fr)
    users[username][3] = 1
    fw = open('user.pkl','wb')
    pickle.dump(users,fw)
    fw.close()


try:
    fi = open('user.pkl','rb')
except FileNotFoundError:
    f = open('user.pkl','wb')
    pickle.dump({},f)
    f.close()

count = 1
flag = True
while(True):
    if(flag):
        name = input('请输入您的用户名：')
        #falg = False
    password = input('请输入您的密码：')
    f = open('user.pkl','rb')
    users = pickle.load(f)
    if(users.get(name) == None ):
        print('该用户还未被注册,是否现在注册?y/n')
        if(input() == 'y'):
            # 注册用户
            regist()
            result = input('是否立即登陆?y立即登陆;n退出')
            if(result == 'n'):
                break
            else:
                flag = True
        else:
            break
    elif(users.get(name)[3] == 0):
        print('该账号已经被锁定,请联系管理员进行解锁！')
        break
    elif(users.get(name)[1] != password):
        if(count == 3):
            # 锁定用户
            lockUser(users,name)
            print('密码三次输入错误,已经锁定该账号,请联系管理员进行解锁')
            break
        else:
            print('密码不正确','还有',str(3-count),'次输入的机会！')
            count += 1
            flag = False
    else:
        print('登陆成功！')
        break




