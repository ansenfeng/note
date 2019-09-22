#-*- coding: utf-8 -*-
import requests 
# from bs4 import    BeautifulSoup
from lxml import etree
import csv
import json
import pandas as pd
from sqlalchemy import create_engine
def savesql(title,hot,urli):
    engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/diy?charset=utf8')#    mydb?编码
    sql="""charset=utf8
        select * from gdp2;
        """
    df = pd.DataFrame({'name':title,'hot':hot,'url':urli,})
    df.to_sql('gdp2', engine,if_exists='append')
    df2 = pd.read_sql_query(sql, engine)
    # print(df2)
tlist=[]
def get(key):
    for  i in range(0,150,50):
        url='https://tieba.baidu.com/f?kw={}&ie=utf-8&pn='.format(key)
        headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        }
        tlist.clear()
        response = requests.get(url+str(i))
        responsed =response.text
        htm = etree.HTML(responsed)
        title = htm.xpath('//*[@id="thread_list"]/li/div/div/div/div/a/text()')
        hot = htm.xpath('//*[@id="thread_list"]/li/div/div/span/text()')
        urli = htm.xpath('//*[@id="thread_list"]/li/div/div/div/div/a/@href')
        if len(hot)!=len(title):#减去多余长度
            for x in range(1,len(hot)-len(title)+1):
                hot.pop()
        # for i in hot:
        #     if i ==''
        for i in  urli:#拼接url
            urlq = "https://tieba.baidu.com"+i
            tlist.append(urlq)     
        #存入数据库
        # engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/diy?charset=utf8')#mydb?编码
        # df = pd.DataFrame({'name':title,'hot':hot,'url':tlist})
        # df.to_sql('baidutieba5', engine,if_exists='append')
        # print(len(tlist),len(title),len(hot))
        # print(hot)
        # print(df)
        # data2=[]
        for re,re2,re3 in zip(title,hot,urli):
            print(re+"\t",re2+"\t",re3)
        #     # item = [re,url,re2]
        #     # cont = json.dumps(item,ensure_ascii=False)+",\n"
        #     # with open("txt4.json","a",encoding="utf-8") as f:
        #     #     f.write(cont)
        # #print(data2)
if __name__ == '__main__':
    get('历史')
