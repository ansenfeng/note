#-*- coding: utf-8 -*-
import requests 
from lxml import etree
import csv
import json
import re
import pyttsx3 # 朗读和停止朗读快捷键 Option-Esc
engine = pyttsx3.init()
def get(url):
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    }
    response = requests.get(url)
    response.encoding = response.apparent_encoding#解决乱码
    responsed =response.text
    htm = etree.HTML(responsed)
    time = htm.xpath('//*[@id="top_bar"]/div/div[2]/span/text()')[0]
    title=htm.xpath('//*[@id="article"]/p/text()')
    #print(responsed)
    print(title[0].replace('原标题：',''))
    print(time)
    a=[]
    a1=''.join(title[1:-1])
    print(a1)
    print('　　'+title[-1])
    # for x in title[1:-1]:
    #     #print(x)
    #     a.append(x)
    # b=str(a).replace(r'\u3000',r'')#前缀u表示ununicode编码，r不转译字符，b，bytles
    # c=b.replace(r'\xa0','')
    #print(c)
    engine.say(a1)
import datetime
today1 = datetime.datetime.today()
astmonth = datetime.datetime(today1.year, (today1.month - 1), today1.day, today1.hour, today1.minute,today1.second)
print(today1,astmonth)
a='16:00'
b='15:00'
def tm(time):
    date = datetime.datetime.strptime(time,"%H:%M")
    return date
print(tm(a),tm(b),)
if tm(a)>tm(b):
    print(str(tm(a))+'>'+str(tm(b)))
else:
    print(str(tm(a))+'<'+str(tm(b)))
f='03月23日 16:33'.replace('月','-')
g=f.replace('日','')
dd = '03-17 11:00:00'
dd = datetime.datetime.strptime(g, "%m-%d %H:%M")
print(dd)
with open("time.csv","w",encoding="utf-8") as f:
    f.write(str(dd))
with open("time.csv", 'r') as tm3:
    ds = datetime.datetime.strptime(tm3.read(), "%Y-%m-%d %H:%M:%S")
    print(ds)
if __name__ == '__main__':
    #get('https://news.sina.com.cn/w/2019-11-23/doc-iihnzhfz1205555.shtml')
    engine.runAndWait()
    engine.stop()
