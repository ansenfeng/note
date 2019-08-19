import requests        #导入requests包
# from bs4 import    BeautifulSoup
from lxml import etree
import csv
import json
temp = r"/Users/anson/Desktop/py"+'\\'
for  i in range(0,300,50):
    url='https://tieba.baidu.com/f?kw=残疾人征婚&ie=utf-8&pn='
    proxies={
        "http":"http://10.10.1.10:3128",
        "https":"http://10.10.1.10:1080",
    }
    response = requests.get(url+str(i), proxies)
    response.encoding = "utf8"
    responsed =response.text
    htm = etree.HTML(responsed)
    re = htm.xpath('//*[@id="thread_list"]/li/div/div/div/div/a/text()')
    re2 = htm.xpath('//*[@id="thread_list"]/li/div/div/span/text()')
    re3 = htm.xpath('//*[@id="thread_list"]/li/div/div/div/div/a/@href')
    
    for re,re2,re3 in zip(re,re2,re3):
        url = "https://tieba.baidu.com"+re3
        # print(re+"\t",re2+"\t",url)
        item = [re,url,re2]
        cont = json.dumps(item,ensure_ascii=False)+",\n"
        with open("txt4.json","a",encoding="utf-8") as f:
            f.write(cont)

