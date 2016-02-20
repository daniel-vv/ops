#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xml.etree.cElementTree as XML
new_xml = XML.Element('data')
name = XML.SubElement(new_xml,'name',attrib={'enrolled':'yes'})
age = XML.SubElement(name,'age',attrib={'checked':'no'})
sex = XML.SubElement(name,'sex')
name.text = 'Daniel'
sex.text = 'Male'
age.text = '29'

et = XML.ElementTree(new_xml)
et.write('create.xml',encoding='utf-8',xml_declaration=True)

XML.dump(new_xml)

