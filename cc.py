# -*- coding:UTF-8 -*-
import re
str1 = 'weffkojopjgio'
print str1[::-1]


str2 = 'we  are not  45    a dog'
revwords = re.split('(\d+)',str2)
print 1, revwords
revwords.reverse()
print 2, revwords
print ''.join(revwords)



