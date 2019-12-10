import requests
import time
from lxml import etree
import re
import pymysql
import time

keya = 0
def get_html(page):
    """获取网站html代码"""
    url = "https://cd.ke.com/xiaoqu/pg2p1p2/".format(page)
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
    title = content.xpath('//*[@id="beike"]/div[1]/div[4]/div[1]/div[3]/ul/li/div[1]/div[1]/a/text()')
    urli = content.xpath('//*[@id="beike"]/div[1]/div[4]/div[1]/div[3]/ul/li/div[1]/div[1]/a/@href')
    chengjiao =content.xpath('//*[@id="beike"]/div[1]/div[4]/div[1]/div[3]/ul/li/div[1]/div[2]/a[1]/text()')
    chuzu = content.xpath('//*[@id="beike"]/div[1]/div[4]/div[1]/div[3]/ul/li/div[1]/div[2]/a[2]/text()')
    address =content.xpath('//*[@id="beike"]/div[1]/div[4]/div[1]/div[3]/ul/li/div[1]/div[3]/a[1]/text()')
    xiaoqu = content.xpath('//*[@id="beike"]/div[1]/div[4]/div[1]/div[3]/ul/li/div[1]/div[3]/a[2]/text()')
    tm20 = content.xpath('//*[@id="beike"]/div[1]/div[4]/div[1]/div[3]/ul/li/div[1]/div[3]/text()')
    price2 = content.xpath('//*[@id="beike"]/div[1]/div[4]/div[1]/div[3]/ul/li/div[2]/div[1]/div[1]/span/text()')
    nums = content.xpath('//*[@id="beike"]/div[1]/div[4]/div[1]/div[3]/ul/li/div[2]/div[2]/a/span/text()')
    tm2= re.findall('\d?\d?..年建',str(tm20),re.S)

    time.sleep(1)
    print(len(title),len(urli),len(chengjiao),'c'+str(len(chuzu)),len(address),len(xiaoqu),len(tm2),len(price2),len(nums))

    for title,address,xiaoqu,price2,tm2,chengjiao,nums,urli in zip (title,address,xiaoqu,price2,tm2,chengjiao,nums,urli):
        sqlc = "INSERT INTO  beike_xiaoqu_08 (name,address,xiaoqu,price2,tm2,chengjiao,nums,url) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sqlc,[title,address,xiaoqu,price2,tm2,chengjiao,nums,urli])
        conn.commit()
       
            

def creattable():
    sql ="""
    CREATE TABLE if not exists `beike_xiaoqu_08`(
    `id`    INT UNSIGNED AUTO_INCREMENT,
    `name`    VARCHAR(255)  NULL,
    `address` VARCHAR(255)  NULL,
    `xiaoqu`   VARCHAR(255)  NULL,
    `chuzu` VARCHAR(255)  NULL,
    `price2` VARCHAR(255)  NULL,
    `chengjiao`    VARCHAR(255)  NULL,
    `nums`     VARCHAR(255)  NULL,
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
    for page in range(44,82):
        html = get_html(page)
        getdata(html)
    
if __name__ == '__main__':
    
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='diy',charset='utf8')
    cursor = conn.cursor()
    main()
    #creattable()
    cursor.close()
    conn.close()
