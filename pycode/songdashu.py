import requests
from lxml import etree
import csv
import json
import pandas as pd
urlc=[]
def geturl():
    for page in range(1, 4):
        url = 'http://www.songdashu.cn/news1.asp?page={}&word=&lm=&lm2=106&lmname=0&open=1&n=30&hot=0&tj=0'.format(page)
        proxies={
               "http":"http://10.10.1.10:3128",
               "https":"http://10.10.1.10:1080",
           }
        resp = requests.get(url,proxies)
        resp.encoding= 'gbk'
        respd =resp.text
        htm = etree.HTML(respd)
        rurl = htm.xpath('//table/a/@href')
        table = htm.xpath('//table[@id="table4"]')#获取表格
        for x2 in table: #循环便利表格
            x3= x2.xpath('//a/font/text()')#每一个都是一个列表list
            xurl= x2.xpath('///tr/td[1]/a/@href')
            xurl2= x2.xpath('///tr/td[1]/a/text()')
            xu3 = 'http://www.songdashu.cn/'+str(xurl)
        # print(results)
        del xurl[0]#删除第一个
        print (len(xurl),len(x3))#检测长度是否一致
        urlc= []#建立空列表
        for i in range(0,len(xurl)):
        	url2c = 'http://www.songdashu.cn/'+str(xurl[i])
        	urlc.append(url2c)#推入列表
        print(urlc)
        for i in range(0,len(urlc)):
        	getdata(urlc[i])
def getdata(url5):
	url=url5
	resp = requests.get(url)
	resp.encoding='gbk'
	respd=resp.text
	htm=etree.HTML(respd)
	title=htm.xpath('//*[@id="table4"]//td/b/font/font/text()')
	url2=htm.xpath('//*[@id="table4"]//a/@href')
	url3= 'http://www.songdashu.cn'+str(url2[0])
	print(str(title[0]+url3[-4:]),url3)
	f=requests.get(url3)
	with open(str(title[0]+url3[-4:]),"wb") as code:
		code.write(f.content)
geturl()

