#-*- coding: utf-8 -*-
import requests
from lxml import etree
import pandas as pd
from sqlalchemy import create_engine
import pymysql
import time
# 注意mysql的保留字add容易错误
def get(key):
    for i in range(1,2):
        url='http://chengdu.liebiao.com/shangpu/index{}.html'.format(i)
        headers = {
            'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
        }
        res= requests.get(url,headers=headers)
        resp=res.text
        htm=etree.HTML(resp)
        title = htm.xpath('//*[@id="main-content-list"]/div[1]/ul/li/div[1]/div[2]/div[1]/h2/a/text()')
        url = htm.xpath('//*[@id="main-content-list"]/div[1]/ul/li/div[1]/div[2]/div[1]/h2/a/@href')
        class1=htm.xpath('//*[@id="main-content-list"]/div[1]/ul/li/div[1]/div[2]/div[2]/span[1]/text()')
        area =htm.xpath('//*[@id="main-content-list"]/div[1]/ul/li/div[1]/div[2]/div[2]/span[2]/text()')
        price=htm.xpath('//*[@id="main-content-list"]/div[1]/ul/li/div[2]/p[1]/text()')
        time =htm.xpath('//*[@id="main-content-list"]/div[1]/ul/li/div[2]/p[2]/text()')
        engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/diy?charset=utf8')#mydb?编码
        df = pd.DataFrame({'name':title,'class':class1,'area':area,'price':price,'time':time,'url':url})
        df.to_sql('liebiaowang', engine,if_exists='append')
def get58(key):
    keya=0#计页数
    for i in range (31,key):
        url='https://cd.58.com/zhaojianzhi/pn{}/?PGTID=0d303680-0006-627e-01e7-e69f67a96673&ClickID=1'.format(i)
        headers = {
                'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
                'cookie': 'f=n; commontopbar_new_city_info=102%7C%E6%88%90%E9%83%BD%7Ccd; 58home=cd; f=n; id58=e87rZl2EhzoTzr6aAyl/Ag==; city=cd; 58tj_uuid=9b88d2a0-f6b3-4dd2-ba82-e81f29444969; als=0; xxzl_deviceid=L8GsANQlwLg6xcuOoO1HCBb8VQfVbqGKs5OxcwE06ozgGv51%2BFsI1ZNWwCa2h6lf; commontopbar_new_city_info=102%7C%E6%88%90%E9%83%BD%7Ccd; new_uv=2; utm_source=; spm=; init_refer=; commontopbar_ipcity=cd%7C%E6%88%90%E9%83%BD%7C0; JSESSIONID=C17414DB4CB4F865BB7183FCBB311A6F; new_session=0; sessionid=76d769f6-f891-40b4-b3cc-b94a67f2e10f; wmda_uuid=0d20c75d6f3995bdd4b8e9700e7bc664; wmda_session_id_1731916484865=1569028416397-36c71979-fcfc-e70c; wmda_visited_projects=%3B1731916484865%3B2385390625025%3B4166008487938%3B1409632296065%3B1731918550401%3B6333604277682%3B7790950805815%3B3846682473985; ppStore_fingerprint=787FBF498AD50A90C1B3C2862D994A68FA57F219BD71E33C%EF%BC%BF1569028417199; Hm_lvt_b2c7b5733f1b8ddcfc238f97b417f4dd=1569028417; Hm_lpvt_b2c7b5733f1b8ddcfc238f97b417f4dd=1569028417; gr_user_id=b35c29dc-39a5-477d-b32b-27abdcc67765; gr_session_id_b4113ecf7096b7d6=be4c806f-6600-4577-83d3-ead6406ee887; gr_session_id_b4113ecf7096b7d6_be4c806f-6600-4577-83d3-ead6406ee887=true'
            }
        res=requests.get(url,headers=headers)
        resp = res.text
        htm=etree.HTML(resp)
        title = htm.xpath('//*[@id="infolist"]/dl/dt/a/text()')
        urli = htm.xpath('//*[@id="infolist"]/dl/dt/a/@href')
        name= htm.xpath('//*[@id="infolist"]/dl/dd[2]/text()')
        sex=htm.xpath('//*[@id="infolist"]/dl/dd[3]/text()')
        age=htm.xpath('//*[@id="infolist"]/dl/dd[4]/text()')
        job=htm.xpath('//*[@id="infolist"]/dl/dd[6]/text()')
        time1=htm.xpath('//*[@id="infolist"]/dl/dd[7]/text()')
        print(len(title),len(name),len(sex),len(age),len(job),len(urli),len(time1))
        print(keya)
        for title,name,sex,age,job,urli,time1 in  zip(title,name,sex,age,job,urli,time1):
            sqlc = "INSERT INTO  58_jianzhi (title,name,sex,age,job,urli,time1) VALUES(%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sqlc,[title,name,sex,age,job,urli,time1])
            conn.commit()
        time.sleep(1)
        keya+=1
def creattable():
    sql ="""
    CREATE TABLE if not exists `58_jianzhi`(
    `id`    INT UNSIGNED AUTO_INCREMENT,
    `title`    VARCHAR(255)  NULL,
    `name` VARCHAR(255)  NULL,
    `sex`    VARCHAR(255)  NULL,
    `age` VARCHAR(255)  NULL,
    `job` VARCHAR(255)  NULL,
    `urli` VARCHAR(255)  NULL,
    `time1`   VARCHAR(255)  NULL,
    `Time` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
    )ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """
    cursor.execute(sql)
    conn.commit() 

if __name__ == '__main__':
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='diy',charset='utf8')
    cursor = conn.cursor()
    get58(101)
    #creattable()
    cursor.close()
    conn.close()