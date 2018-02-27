# -*- coding:utf-8 -*-
age = 26
user_guess = int(input('your guess:'))
if user_guess == age:
    print('恭喜你答对了')
elif user_guess < age:
    print('try bigger')
else:
    print('try smaller')
