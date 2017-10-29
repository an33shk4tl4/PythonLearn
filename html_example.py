import xml.etree.ElementTree as et
import pprint

filepath = r'testxml.xml'

xfile = et.ElementTree(file=filepath)
root = et.Element
root = xfile.getroot()
print root.tag

for e in root:
    print e.tag, e.attrib, e.text,
    for ee in e:
        print ee.tag , ee.attrib , ee.text
