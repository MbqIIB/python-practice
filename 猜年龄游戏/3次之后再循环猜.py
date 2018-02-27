# -*- coding:utf-8 -*-
count = 0
age = 26
while count < 3:
    user_guess = int(input('your guess:'))
    if user_guess == age:
        print ('恭喜你答对了:')
        break
    elif user_guess < age:
        print ('try bigger')
    else:
        print ('try smaller')
    count += 1
    if count == 3:
        choice = input('不好意思，你猜错了，还想再猜嘛？（y|Y)')
        if choice == 'y' or choice == 'Y':
            count = 0

