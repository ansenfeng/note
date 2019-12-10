import requests
import time
from lxml import etree
import re
import pymysql
import time

keya = 0
def get_html(page):
    """获取网站html代码"""
    url = "https://cd.ke.com/ershoufang/pg{}co41/".format(page)
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    response = requests.get(url, headers=headers,timeout=180).text
    return response 
def getdata(html):
    global keya
    print(keya)
    keya+=1
    content = etree.HTML(html)
    results = content.xpath('//*[@id="beike"]/div[1]/div[4]/div[1]/div[4]/ul/li')
    for r2 in results:
        title = r2.xpath('*//div/div/a/@title')  
        urlq = r2.xpath('*//div/div[@class="title"]/a/@href') 
        urlw = r2.xpath('*//div/div[2]/div/div/a/@href')      
        address = r2.xpath('*//div/div[2]/div/div/a/text()')
        area = r2.xpath('*//div/div[2]/div[2]/text()')
        time3 = r2.xpath('*//div/div[2]/div[3]/text()')
        price = r2.xpath('*//div/div[2]/div[5]/div/span/text()')
        # hot = re.findall("\d+\w*",str(time))[::2]
        # time2 = re.findall("\d+\w*",str(time))[1::2]
        # price1 = re.findall("\w*\S\d+\D",str(price))[0::2]
        # price2 = re.findall("\w*\S\d+\D",str(price))[1::2]
        # ceng = re.findall("\w*\d+\w*",str(area))[::5]
        # start = re.findall("\w*\d+\w*",str(area))[::1]
        # geju = re.findall("\w*\d+\w*",str(area))[::2]
        # print(len(ceng),len(start),len(geju))
        # sq2 = re.findall("\w*\d+\w*\S\d+\w*",str(area))[::3]
        ting= re.findall('.室.厅',str(area),re.S)
        area2=re.findall('\d?\d?\d?...平米',str(area),re.S)
        lv= re.findall('\S?楼层..\d?\d?..',str(area),re.S)
        tm2= re.findall('\d?\d?..年建',str(area),re.S)
        tm= re.findall('\d?...发布',str(time3),re.S)
        hot= re.findall('\d?\d?\d?\d?..关注',str(time3),re.S)
        price1 = price[0::2]
        price2 = price[1::2]
        
        time.sleep(1)
        print(len(title),len(address),len(area2),len(price1),len(price2),len(ting),len(lv),len(tm2),len(tm),len(urlq))

        for title,address,area,price1,price2,ting,tm,urlq in zip (title,address,area2,price1,price2,ting,tm,urlq):
            sqlc = "INSERT INTO  beike_1_15 (name,address,area,price1,price2,ting,tm,url) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sqlc,[title,address,area,price1,price2,ting,tm,urlq])
            conn.commit()
        #     print(title,address,area,price1,price2,ting,lv,tm2,tm,urlq)
            

def creattable():
    sql ="""
    CREATE TABLE if not exists `beike_1_15`(
    `id`    INT UNSIGNED AUTO_INCREMENT,
    `name`    VARCHAR(255)  NULL,
    `address` VARCHAR(255)  NULL,
    `area`    VARCHAR(255)  NULL,
    `price1` VARCHAR(255)  NULL,
    `price2` VARCHAR(255)  NULL,
    `ting`   VARCHAR(255)  NULL,
    `lv`     VARCHAR(255)  NULL,
    `tm2`    VARCHAR(255)  NULL,
    `tm`    VARCHAR(255)  NULL,
    `url`    VARCHAR(255) NULL,
    `Time1` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
    )ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """
    cursor.execute(sql)
    conn.commit()

def jsonc():
    for a,b,c,d,e in zip(title,address,price1,area1,urlw):
        item = [a,b,c,d,e]
        cont = json.dumps(item,ensure_ascii=False)+",\n"
        with open("txt4.json","a",encoding="utf-8") as f:
            f.write(cont)
def main():
    all_datas = []
    for page in range(1,101):
        html = get_html(page)
        getdata(html)
    
if __name__ == '__main__':
    
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='diy',charset='utf8')
    cursor = conn.cursor()
    main()
    #creattable()
    cursor.close()
    conn.close()
