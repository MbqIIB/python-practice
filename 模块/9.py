#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2018/5/24 下午9:18
# @Author  : littlelinghome
# @Site    : 
# @File    : 9.py
# @Software: PyCharm

import xml.etree.ElementTree as ET
#创建根节点
root = ET.Element("namelist")
#在根节点root下面创建name子节点，它的属性是attrib
name = ET.SubElement(root,"name",attrib={"enrolled":"yes"})
#在name节点下面存放几个参数
age = ET.SubElement(name,"age",attrib={"checked":"no"})
sex = ET.SubElement(name,"sex")
n = ET.SubElement(name,"name")  #最后一个需求
n.text = "Alex Li"  #最后一个需求
sex.text = "male"


#在根节点root下面创建第二个子节点name2
name2 = ET.SubElement(root,"name",attrib={"enrolled":"no"})
#在第二个子节点name2下面创建参数
age = ET.SubElement(name2,"age")
age.text="19"

#生成文档对象
et = ET.ElementTree(root)
et.write("/Users/caolingjun/daily/build_out.xml",encoding="utf-8",xml_declaration=True)


#此时执行之后，发现build_out.xml文件已经生成，但是我们发现每个人都没有名字，我再添加name参数



