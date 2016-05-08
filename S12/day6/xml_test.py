#!/usr/bin/env python
# -*- coding: utf-8 -*-




import xml.etree.ElementTree as ET

tree = ET.parse("xml_file.xml")
root = tree.getroot()
#print(root.tag)

'''
#遍历xml文档
for child in root:
    print(child.tag, child.attrib)
    for i in child:
       print('     ',i.tag,i.text)

#只遍历year 节点
for node in root.iter('year'):

    print(node.tag,node.text)
'''

'''
#修改
for node in root.iter('year'):
    #print(node.text)
    ny = int(node.text)+1
    node.text = str(ny)

    node.set('update','yes')
    node.set('gengxin','2016/2/20 12:59')
   #print(node.text)
tree.write('output.xml')'''
# 自己创建XML文件
