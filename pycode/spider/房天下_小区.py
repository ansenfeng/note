# -*- coding: utf-8 -*-
import requests
# 导入必要模块
from lxml import etree
import pymysql
import time
import re
keya = 0
def get():
    for page in range(34,97):

        global keya 
        print(keya)
        #print(html)
        keya+=1
        time.sleep(1)
        url = "https://cd.esf.fang.com/housing/__0_0_0_10000_{}_0_0_0/".format(page)
        headers = {
            'Referer': 'https://chengdu.anjuke.com/community/m58-p%7B%7D/',
            'Sec-Fetch-Mode': 'no-cors',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.        0.3809.132 Safari/537.36'}
        response = requests.get(url, headers=headers,timeout=180).text
        content = etree.HTML(response)
        aa= content.xpath('/html/body/div[4]/div[5]/div[4]/div')
        for r2 in aa:
        	title = r2.xpath('//*/dl/dd/p[1]/a[1]/text()')
        	urli =r2.xpath ('//*/dl/dd/p[1]/a[1]/@href')
        	leixing = r2.xpath('//*/dl/dd/p[1]/span[1]/text()')
        	shi = r2.xpath('//*/dl/dd/p[2]/a[1]/text()')
        	shi2 =r2.xpath('//*/dl/dd/p[2]/a[2]/text()')
        	address =r2.xpath('//*/dl/dd/p[2]/text()[3]')
        
        	shou = r2.xpath('//*/dl/dd/ul/li[1]/a/text()')
        	zu = r2.xpath('//*/dl/dd/ul/li[2]/a/text()')
        	tm2 = r2.xpath('//*/dl/dd/ul/li[3]/text()')
        	price =r2.xpath('//*/div/p[1]/span[1]/text()')
        
        	address2 =re.findall(r'\s(\w{2,50})[ (]',str(address),re.S)
        	shou2 = re.findall('\d?\d\d?\d?\d?',str(shou))
        	zu2 = re.findall('\d?\d\d?\d?\d?',str(zu))
        	price2 = re.findall('\d?\d?\d\d\d\d?\d?\d?',str(price))
        print(len(title),len(leixing),len(shi),len(shi2),len(address2),len(shou2),len(zu2),len(price2),len(urli))
        #print(title,leixing,shi,shi2,address2,shou2,zu2,tm2,price2,urli,sep='\n\n\n')
        for title,leixing,shi,shi2,address2,shou2,zu2,tm2,price2,urli in zip (title,leixing,shi,shi2,address2,shou2,zu2,tm2,price2,urli):
                sqlc = "INSERT INTO  fang_xiaoqu_10 (name,tm,price1,lu,address,esf_nums,zu_nums,tm2,price2,url) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                cursor.execute(sqlc,[title,leixing,shi,shi2,address2,shou2,zu2,tm2,price2,urli])
                conn.commit()
if __name__ == '__main__':
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='diy',charset='utf8')
    cursor = conn.cursor()
    #main()
    get()
    cursor.close()
    conn.close()