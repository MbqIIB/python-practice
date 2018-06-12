#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/30 下午5:49
# @Author  : littlelinghome
# @Site    : 
# @File    : 14.py
# @Software: PyCharm

contact = []
with open("/Users/caolingjun/daily/re.txt",'r',encoding='utf-8') as f:
    for line in f:
        createtime,count,type,name,phone,level = line.split()
        if phone.isdigit():
            contact.append(phone)
print(contact)


#用正则方法匹配文件中的数据（取代了文件循环查找的方法）
import re
f = open("/Users/caolingjun/daily/re.txt",'r')
data = f.read()
print(re.findall("[0-9]{11}" , data))


re 的匹配语法有以下几种
1）re.match  从头开始匹配，这要求被匹配的字符串的第一个字符必须是符合前面匹配规则的字符(应用场景：比如匹配手机号，身份证号等)
2）re.search 匹配包含
3）re.findall 把所有匹配到的字符放到以列表中的元素返回
4）re.split 以匹配到的字符当做列表分隔符
5) re.sub 匹配字符并替换
6）re.fullmatch 全部匹配
例题：
>>> re.search('[0-9]','abc1d3e')
<_sre.SRE_Match object; span=(3, 4), match='1'>
>>>
>>> re.search('[0-9]','abc1d3e').group()
'1'
但是上面的做法一定是字符串中有要匹配的字符，否则就会报错，因为如果匹配不到则返回none，此时group()肯定报错

>>> match_res = re.search('[0-9]','abc1d3e')
>>> if match_res:
...     print(match_res.group())
...
1



常用的表达式规则

'.'     默认匹配除\n之外的任意一个字符，若指定flag dotall则匹配任意字符，包括换行
'^'     匹配字符开头，若指定 flags MULTILINE,这种也可以匹配上(r"^a","\nabc\neee")
'$'     匹配字符结尾，若指定 flags MULTILINE,re.search('foo.$','foo1\nfoo2\r')
'*'     匹配*号前的字符0次或多次，re.search('a*','aaaaabac'),结果'aaaaa'
'+'     匹配前一个字符1次或多次，re.findall("ab+","ab+cd+abb+bba"),结果['ab',]
'?'     匹配前一个字符1次或多次，re.search('b?',"alex").group() 匹配b 0次
'{m}'   匹配前一个字符m次，re.search(b{3},'alexbbbs').group() 匹配到'bbb'
'{n,m}' 匹配前一个字符n到m次，re.findall("ab{1,3}","abb abc abbcbbb") 结果
'|'     匹配|左或|右的字符，re.search("abc|ABC","ABCBabcCD").group() 结果
'(...)' 分组匹配，re.search("(abc){2}a(123|45)","abcabca456c").group() 结果

例题：
>>> re.search('^a','abc1d3e')
<_sre.SRE_Match object; span=(0, 1), match='a'>
>>> re.match('a','abc1d3e')
<_sre.SRE_Match object; span=(0, 1), match='a'>

例题：
>>> re.search('b$','adb')
<_sre.SRE_Match object; span=(2, 3), match='b'>
>>> re.match('b$','adb')
>>> re.match('b$','bob')
>>> re.match('b$','b')
<_sre.SRE_Match object; span=(0, 1), match='b'>
注：一般用$去匹配一般是不用match方法的

例题：
>>> re.search('.+','asdfd')
<_sre.SRE_Match object; span=(0, 5), match='asdfd'>


例题：
>>> re.search('[a|A]lex','alex')
<_sre.SRE_Match object; span=(0, 4), match='alex'>


例题：
>>> re.search('([a-z]+)([0-9]+)','23al45ex')
<_sre.SRE_Match object; span=(2, 6), match='al45'>
>>> re.search('([a-z]+)([0-9]+)','23al45ex').group()
'al45'
>>> re.search('([a-z]+)([0-9]+)','23al45ex').groups()
('al', '45')
>>> re.search('([0-9]+)([a-z]+)','23al45ex').groups()
('23', 'al')



'\A' 只从字符开头匹配，re.search("\Aabc","alexabc") 是匹配不到的，相当于re.match('abc',"alexabc")
'\Z' 匹配字符结尾，同$
'\d' 匹配数字0-9
'\D' 匹配非数字
'\w' 匹配[A-Za-z0-9]
'\W' 匹配非[A-Za-z0-9]
'\s'  匹配空白字符、\t、\n、\r,re.search("\s+","ab\tc1\n3").group() 结果'\t'
'(?<name>...)' 分组匹配



例题：
>>> re.search('\s','alex\n kdf\tvdf\r ')
<_sre.SRE_Match object; span=(4, 5), match='\n'>
>>> re.findall('\s','alex\n kdf\tvdf\r ')
['\n', ' ', '\t', '\r', ' ']


例题：
>>> s = '34260119890602622x'
>>> re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<year>\d{4})',s).group()
'3426011989'
>>> re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<year>\d{4})',s).groups()
('342', '601', '1989')
>>> res = re.search('(?P<province>\d{3})(?P<city>\d{3})(?P<year>\d{4})',s)
>>> res.
res.end(       res.expand(    res.groupdict( res.lastgroup  res.pos        res.regs       res.start(
res.endpos     res.group(     res.groups(    res.lastindex  res.re         res.span(      res.string
>>> res.groupdict()
{'province': '342', 'city': '601', 'year': '1989'}




################################## re.split ###################################

>>> s = 'alex22jack23rain31jinxin50'
>>> s.split()
['alex22jack23rain31jinxin50']
>>> re.split('\d',s)
['alex', '', 'jack', '', 'rain', '', 'jinxin', '', '']
>>> re.split('\d+',s)
['alex', 'jack', 'rain', 'jinxin', '']
>>> re.findall('\d+',s)
['22', '23', '31', '50']


>>> s = 'alex22jack23rain31jinxin50#mack-oldboy'
>>> re.split('\d+|#|-',s)
['alex', 'jack', 'rain', 'jinxin', '', 'mack', 'oldboy']


>>> s = '9-2*5/3+7/3*99/4*2998+10*568/14'
>>> s
'9-2*5/3+7/3*99/4*2998+10*568/14'
>>> re.split('[-\*/+]',s)
['9', '2', '5', '3', '7', '3', '99', '4', '2998', '10', '568', '14']
>>> re.split('[-\*/+]',s,maxsplit=2)
['9', '2', '5/3+7/3*99/4*2998+10*568/14']


转义：
>>> s = 'alex22jack23rain31jinxin50|mack-oldboy'
>>> re.split('\d+|\|',s)
['alex', 'jack', 'rain', 'jinxin', '', 'mack-oldboy']





################################## re.sub ###################################
用于替换匹配的字符串
re.sub(pattern,repl,string,count=0,flags=0)

>>> s
'alex22jack23\rain31jinxin50|mack-oldboy'
>>> re.sub('\d+','**',s)
'alex**jack**\rain**jinxin**|mack-oldboy'

>>> re.sub('\d+','**',s,count=2)
'alex**jack**\rain31jinxin50|mack-oldboy'





################################## re.fullmatch ###################################
整个字符串匹配成功就返回re object,否则返回None
re.fullmatch(pattern,string,flags=0)

>>> re.fullmatch('\w+@\w+\.(com|cn|edu)',"alex@oldboyedu.com")
<_sre.SRE_Match object; span=(0, 18), match='alex@oldboyedu.com'>





################################## re.compile ###################################
re.compile(pattern,flags=0)

>>> re.compile('\w+@\w+\.(com|cn|edu)')
re.compile('\\w+@\\w+\\.(com|cn|edu)')
>>> pattern = re.compile('\w+@\w+\.(com|cn|edu)')
>>> pattern
re.compile('\\w+@\\w+\\.(com|cn|edu)')
>>> pattern.fullmatch('alex@oldboyedu.com')
<_sre.SRE_Match object; span=(0, 18), match='alex@oldboyedu.com'>

注：先编译好规则，并赋值给一个变量，再通过变量去fullmatch一个字符串
   这样的做法与直接fullmatch一个字符串是没有区别的，只不过这样做对于大批量的正则匹配会提高效率




################################## flags标志符 ###################################
re.I(re.IGNORECASE)：忽略大小写
M(MULTILINE):多行模式，改变'^'和'$'的行为
S(DOTALL)：改变'.'的行为，
X(re.VERBOSE)可以给你的表达式写注释，使其更可读


例题：
>>> re.search('a','alex')
<_sre.SRE_Match object; span=(0, 1), match='a'>
>>> re.search('a','Alex')
>>> re.search('a','Alex',re.I)
<_sre.SRE_Match object; span=(0, 1), match='A'>


例题：
>>> re.search('foo.$','foo1\nfoo2\n')
<_sre.SRE_Match object; span=(5, 9), match='foo2'>

>>> re.search('foo.$','foo1\nfoo2\n',re.MULTILINE)
<_sre.SRE_Match object; span=(0, 4), match='foo1'>


例题：
>>> re.search('.','\n')
>>> re.search('.','\n',re.S)
<_sre.SRE_Match object; span=(0, 1), match='\n'>


例题：
>>> re.search('. #test','alex')
>>> re.search('. #test','alex',re.X)
<_sre.SRE_Match object; span=(0, 1), match='a'>