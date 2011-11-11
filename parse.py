#coding =gbk
import urllib
import re
import sys
data = urllib.urlopen('http://www.nuomi.com/shanghai?catalogId=178').read()
#print data


#print data
f = open('D:\data.txt','w')
f.write(data)
data2 = open('D:\data.txt','r').read()
#print data2
p = re.compile(r'<h3>.*')
a= p.findall(data)
for ele in a:
    if len(ele)>=50:
        print ele
