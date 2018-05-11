#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/8 下午6:02
# @Author  : littlelinghome
# @Site    : 
# @File    : 9.py
# @Software: PyCharm


方括号中的列表解析会一次在内层中产生结果列表。圆括号中的列表解析，实际上是生成器表达式，它们有类似的意义，但不会一次产生结果列表。
与之相对比的是：生成器表达式会返回一个生成器对象，用在迭代环境中时，一次产生结果中的一个元素。


1).在遍历一个列表时，如何用range来修饰它。与for循环一起使用，列表解析是最常应用迭代协议的环境之一
L = [1, 2, 3, 4, 5]
for i in range(len(L)):
    L[i] += 10

2).列表解析概念。列表解析产生一个新的列表对象
L = [1, 2, 3, 4, 5]
L = [x + 10 for x in L]

注：列表解析和for循环语句一样，是一个迭代环境

注：列表生成器可以写为：
>> > L = [1, 2, 3]
         >> > L = (i + 10 for i in L)
                  >> > L
                  < generator
object < genexpr > at
0x10a04dc30 >

3).可以用一个for循环手动地构建一个表达式结果的列表，该for循环像下面这样添加结果
res = []
for x in L:
    res.append(x + 10)

range迭代器
在python2中，它返回的是一个列表
          >> > range(10)
          [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
在python2中想要和在python3中的效果一样，需要写成这样的形式：
>> > xrange(10)
xrange(10)

在python3，它返回一个迭代器(生成器)
         >> > range(10)
range(0, 10)

所以：列表生成器可以写为：
>> > a = (i for i in range(10))
         >> > a
         < generator
object < genexpr > at
0x10a04daf0 >
>> > for i in a:
    ...
print(i)
但是，与
   >> >
for i in range(10):
    ...
print(i)
有什么区别？


总结：
python2
range: list
xrange: 生成器

python3
range: 生成器
xrange: 不存在

斐波那契数列用列表生成式写不出来，但是用函数把它打印出来却很容易：
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'


注意，赋值语句：
a, b = b, a + b
不等价于
a = b, b = a + b
>> > a, b = 1, 2
>> > a, b = b, a + b
>> > a, b
(2, 3)

>> > a, b = 1, 2
>> > a = b
>> > b = a + b
>> > a, b
(2, 4)


def fib1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b  # 把函数的执行过程冻结在这一步，并且把b的值返回给外部的next()
        a, b = b, a + b
        n = n + 1

>> > for i in fib1(10):
    ...
    print(i)

注：这是函数生成器

注：函数有了yield之后
1.
函数名加（）就得到了一个生成器，
2.
return 在生成器里，代表生成器的终止，直接报错

利用函数生成器的方式实现range函数


def range2(n):
    count = 0
    while count < n:
        print(count)
        count += 1


def range3(n):
    count = 0
    while count < n:
        print(count)
        count += 1
        yield count

>> > a = range3(10)
>> > next(a)
0
1
>> > next(a)
1
2

yield vs
return
return 返回并终止function
yield 返回数据，并冻结当前的执行过程，next唤醒冻结的函数执行过程，继续执行，直到遇到下一个yield


def range3(n):
    count = 0
    while count < n:
        print(count)
        count += 1
        sign = yield count
        print('----sign----', sign)


a = range3(10)
next(a)
a.send('qqqq')
执行之后的结果是：
0
----sign - --- qqqq
1

注：生成器首次使用必须使用next启动，不能用send传值。send把参数传递给yield后的变量

send
语法及作用：
1.
唤醒并继续执行
2.
发生一个信息到生成器内部