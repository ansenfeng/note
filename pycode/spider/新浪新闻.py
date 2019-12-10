#-*- coding: utf-8 -*-
import requests,datetime
from lxml import etree
import csv
import json
import re
import pyttsx3 # 朗读和停止朗读快捷键 Option-Esc
engine = pyttsx3.init()
def get():
    url='https://news.sina.com.cn/world/'
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    }
    response = requests.get(url)
    response.encoding = response.apparent_encoding#解决乱码
    responsed =response.text
    htm = etree.HTML(responsed)
    time = htm.xpath('//*/div/div[2]/div[1]/div[2]/div/div/div/div[1]/text()')
    title=htm.xpath('//*/div/div[2]/div[1]/div/div/div/h2/a/text()')
    url2=htm.xpath('//*/div/div[2]/div[1]/div/div/div/h2/a/@href')
    t1=time[0].replace('月','-')
    t2=t1.replace('日','')
    tm2 = datetime.datetime.strptime(t2, "%m-%d %H:%M")
    tm='更新时间'+re.findall(r'\d\d:\d\d',time[0])[0]
    print('快捷键 Option-Esc,若要停止朗读，请再按一次该按键。如果按下按键时已选定文本，则读出选定文本。否则，会读出当前窗口中的可用文本项目.')
    print('------------------------------------------------------')
    print('新浪国际','有'+str(len(title))+'条消息',tm)
    engine.say(tm)
    a=0
    news=[]
    for x in title:
    	a+=1
    	b='\t'+str(a)+':'+x
    	print(b)
    	news.append(b)
    #engine.say(str(news))
    print('\t\t\t\t\t上次更新时间:'+str(retime()).replace('1900-','').replace('-','月'))
    url3=[]
    centent=[]
    for x,y,u in zip(time,title,url2):
        t3=x.replace('月','-')
        t4=t3.replace('日','')
        if tmto(t4)>retime():
            url3.append(u)
    print('有'+str(len(url3))+'条新消息')
    if len(url3)>0:
        step=1
        for i in url3:
            centent.append(getcentant(i))
        for j in centent:
            print(str(step)+':'+j)
            step+=1
        centent1=''.join(centent)
        engine.say(centent1)
        wrtime(tm2)
    else:
        print('\t没有未读新消息')
        engine.say('未更新')
def getcentant(url4):
    headers = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    }
    response = requests.get(url4)
    response.encoding = response.apparent_encoding#解决乱码
    responsed =response.text
    htm = etree.HTML(responsed)
    # time = htm.xpath('//*[@id="top_bar"]/div/div[2]/span/text()')[0]
    title=htm.xpath('//*[@id="article"]/p/text()')
    #print(responsed)
    #print(time)
    a=[]
    a1=''.join(title[1:-1])
    #print(a1)
    # for x in title[1:-1]:
    #     #print(x)
    #     a.append(x)
    # b=str(a).replace(r'\u3000',r'')#前缀u表示ununicode编码，r不转译字符，b，bytles
    # c=b.replace(r'\xa0','')
    #print(c)
    #engine.say(a1)
    return a1
def retime():
    with open("time.csv", 'r') as tm3:
        ds = datetime.datetime.strptime(tm3.read(), "%Y-%m-%d %H:%M:%S")
    return ds
def wrtime(tm2):
    with open("time.csv","w",encoding="utf-8") as f:
        f.write(str(tm2))
def tmto(time):
    date = datetime.datetime.strptime(time,"%m-%d %H:%M")
    return date
if __name__ == '__main__':
    get()
    #getcentant('https://news.sina.com.cn/w/2019-11-23/doc-iihnzhfz1218374.shtml')

    engine.runAndWait()
    engine.stop()
