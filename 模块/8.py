#!/usr/bin/env python3
# -*- coding: utf-8 -*-

xml的例题
<bookstore>
	<book category="COOKING">
		<title lang="en">Everyday Italian</title>
		<author>Giada De Laurentiis</author>
		<year attr_test="yes">2006</year>
		<price>30.00</price>
	</book>
	<book category="CHILDREN">
		<title lang="en">Harry Potter</title>
		<author>J K. Rowling</author>
		<year attr_test="yes">2006</year>
		<price>29.99</price>
	</book>
	<book category="WEB">
		<title lang="en">Learning XML</title>
		<author>Erik T. Ray</author>
		<year attr_test="yes">2004</year>
		<price>39.95</price>
	</book>
</bookstore>


import xml.etree.ElementTree as ET
#相当于打开xml文件
tree = ET.parse("/Users/caolingjun/daily/www.xml")
root = tree.getroot()
print(root)
print(dir(root))

#打印整个xml的标签
print(root.tag)


#遍历xml文件
tree = ET.parse("/Users/caolingjun/daily/www.xml")
root = tree.getroot()
for child in root:
    print(child.tag,child.attrib)
    for i in child:
        print(i.tag,i.text)


#过滤取出自己想要的信息
for node in root.iter('price'):
    print(node.tag,node.text)


#修改xml，把里面的每个year加1
tree = ET.parse("/Users/caolingjun/daily/www.xml")
root = tree.getroot()
for node in root.iter('year'):
    new_year = int(node.text) + 1
    node.text = str(new_year)
    node.set("attr_test","yes")
tree.write("/Users/caolingjun/daily/www.xml")



#删除xml
tree = ET.parse("/Users/caolingjun/daily/www.xml")
root = tree.getroot()
for book in root.findall('book'):
    year = int(book.find('year').text)
    if year < 2005:
        root.remove(book)
tree.write("/Users/caolingjun/daily/www2.xml")

