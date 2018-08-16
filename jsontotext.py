# -*- coding:utf-8 -*-
import json
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
f = open('item.json', 'r')
jstr = f.read()
dic = json.loads(jstr)
t = dic['json_str']
print t
print type(t)
for i in t:
    responsibility = i['responsibility']
    f = file("responsibility.txt", 'a+')
    f.write(responsibility)




