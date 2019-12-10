#-*- coding: utf-8 -*-
import requests
from lxml import etree
import pandas as pd
from sqlalchemy import create_engine
import pymysql
import time
df
# 注意mysql的保留字add容易错误
def get(key,keyword):
    for i in range(1,key):
        url='https://baike.sogou.com/v6750.htm?fromTitle={}'.format(keyword)
        headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        }
        res= requests.get(url,headers=headers)
        resp=res.text
        htm=etree.HTML(resp)
       
        img = htm.xpath('//*[@id="main-content-list"]/div[1]/ul/li/div[1]/div[2]/div[1]/h2/a/text()')
        tb=htm.xpath('//*[@id="baseInfoCol"]/table')
        tb1 = pd.read_html(resp)[0]
        tb2=tb1.drop(index=0)
        sy=htm.xpath('//*[@id="lemma_pic"]/a/@href')
        print(keyword)
        print(sy)
        # title = htm.xpath('//*[@id="main-content-list"]/div[1]/ul/li/div[1]/div[2]/div[1]/h2/a/text()')
        # url = htm.xpath('//*[@id="main-content-list"]/div[1]/ul/li/div[1]/div[2]/div[1]/h2/a/@href')
        # class1=htm.xpath('//*[@id="main-content-list"]/div[1]/ul/li/div[1]/div[2]/div[2]/span[1]/text()')
        # area =htm.xpath('//*[@id="main-content-list"]/div[1]/ul/li/div[1]/div[2]/div[2]/span[2]/text()')
        # price=htm.xpath('//*[@id="main-content-list"]/div[1]/ul/li/div[2]/p[1]/text()')
        # time =htm.xpath('//*[@id="main-content-list"]/div[1]/ul/li/div[2]/p[2]/text()')
        # engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/diy?charset=utf8')#mydb?编码
        # df = pd.DataFrame({'name':title,'class':class1,'area':area,'price':price,'time':time,'url':url})
        # df.to_sql('liebiaowang', engine,if_exists='append')
def get58(key):
    keya=0#计页数
    for i in range (1,key):
        url='https://cd.58.com/shangpucz/pn{}/?PGTID=0d306b31-0006-698c-e4bf-adacba4d7a56&ClickID=2'.format(i)
        headers = {
                'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
                'cookie': 'f=n; commontopbar_new_city_info=102%7C%E6%88%90%E9%83%BD%7Ccd; 58home=cd; f=n; id58=e87rZl2EhzoTzr6aAyl/Ag==; city=cd; 58tj_uuid=9b88d2a0-f6b3-4dd2-ba82-e81f29444969; als=0; xxzl_deviceid=L8GsANQlwLg6xcuOoO1HCBb8VQfVbqGKs5OxcwE06ozgGv51%2BFsI1ZNWwCa2h6lf; commontopbar_new_city_info=102%7C%E6%88%90%E9%83%BD%7Ccd; new_uv=2; utm_source=; spm=; init_refer=; commontopbar_ipcity=cd%7C%E6%88%90%E9%83%BD%7C0; JSESSIONID=C17414DB4CB4F865BB7183FCBB311A6F; new_session=0; sessionid=76d769f6-f891-40b4-b3cc-b94a67f2e10f; wmda_uuid=0d20c75d6f3995bdd4b8e9700e7bc664; wmda_session_id_1731916484865=1569028416397-36c71979-fcfc-e70c; wmda_visited_projects=%3B1731916484865%3B2385390625025%3B4166008487938%3B1409632296065%3B1731918550401%3B6333604277682%3B7790950805815%3B3846682473985; ppStore_fingerprint=787FBF498AD50A90C1B3C2862D994A68FA57F219BD71E33C%EF%BC%BF1569028417199; Hm_lvt_b2c7b5733f1b8ddcfc238f97b417f4dd=1569028417; Hm_lpvt_b2c7b5733f1b8ddcfc238f97b417f4dd=1569028417; gr_user_id=b35c29dc-39a5-477d-b32b-27abdcc67765; gr_session_id_b4113ecf7096b7d6=be4c806f-6600-4577-83d3-ead6406ee887; gr_session_id_b4113ecf7096b7d6_be4c806f-6600-4577-83d3-ead6406ee887=true'
            }
        res=requests.get(url,headers=headers)
        resp = res.text
        htm=etree.HTML(resp)
        title = htm.xpath('//*[@id="house-list-wrap"]/li/h2/a/span/text()')
        urli = htm.xpath('//*[@id="house-list-wrap"]/li/h2/a/@href')
        address = htm.xpath('//*[@id="house-list-wrap"]/li/div[2]/p[1]/span[1]/text()')
        dtile =htm.xpath('//*[@id="house-list-wrap"]/li/div[2]/p[1]/span[2]/text()')#详细地址
        zhuangtai = htm.xpath('//*[@id="house-list-wrap"]/li/div[2]/p[1]/span[3]/text() ')
        dtile2 =htm.xpath('//*[@id="house-list-wrap"]/li/div[2]/p[2]/text()')
        manger =htm.xpath('//*[@id="house-list-wrap"]/li/div[2]/p[3]/span[2]/text()')
        price=htm.xpath('//*[@id="house-list-wrap"]/li/div[3]/p[1]/span[1]/text()')
        pri2 =htm.xpath('//*[@id="house-list-wrap"]/li/div[3]/p[1]/span[2]/text()')
        area =htm.xpath('//*[@id="house-list-wrap"]/li/div[4]/p[1]/span[1]/text()')
        time1 =htm.xpath('//*[@id="house-list-wrap"]/li/div[5]/text()')
        pr=[]#价格单位转换
        for x in price:
            if str(x) =='面议':
                pr.append(0)
            elif float(x)<80:
                a=float(x)*10000
                b= int(a)
                pr.append(b)
            else:
                pr.append(x)
        tm=[]#转换今天为日期
        for x in time1:
            if str(x)=='今天':
                a='09-21'
                tm.append(a)
            else:
                tm.append(x)
        print(len(title),len(urli),len(address),len(dtile),len(zhuangtai),len(pr),len(area),len(tm))
        print(keya)
        for title,address,area,price,tm,zhuangtai,manger,url in  zip(title,address,area,pr,tm,zhuangtai,manger,urli):
            sqlc = "INSERT INTO  58shangpu2 (name,address,area,price,time,zhuangtai,manger,url) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sqlc,[title,address,area,price,tm,zhuangtai,manger,url])
            conn.commit()
        time.sleep(1)
        keya+=1
        

if __name__ == '__main__':
    get(2,'中国')
    # conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='diy',charset='utf8')
    # cursor = conn.cursor()
    # get58(2)
    # cursor.close()
    # conn.close()