import re
def demo_re():
    str1 = 'abc123def12gh15'
    p1 = re.compile('\d+')
    p2 = re.compile('[\d]+')
    p3 = re.compile('\d')
    print 1, p1.findall(str1)
    print 2, p2.findall(str1)
    print 3, p3.findall(str1)

    str2 = 'a@163.com ; b@gmail.com ; c@qq.com ; e0@163.com ; z@qq.com'
    p4 = re.compile('\w+@163\.com')
    p5 = re.compile('[\w]+@163+\.com')
    p6 = re.compile('[\w]+@[163|qq]+\.com')
    print 4, p4.findall(str2)
    print 5, p5.findall(str2)
    print 6, p6.findall(str2)

    str3 = '<html><h>title</h><body>xxx</body></html>'
    p7 = re.compile('<h>[^<]+</h>')
    p8 = re.compile('<h>([^<]+)</h>')
    p9 = re.compile('<h>([^<]+)</h><body>([^<]+)</body>')
    print 7, p7.findall(str3)
    print 8, p8.findall(str3)
    print 9, p9.findall(str3)
if __name__ == '__main__':
    demo_re()


