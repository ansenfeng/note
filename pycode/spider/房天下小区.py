import requests
import time
from lxml import etree
import re
import pymysql
import time

keya = 0
def get_html(page):
    """获取网站html代码"""
    url = "https://chengdu.anjuke.com/community/m58-p{}/".format(page)
    headers = {
        'Referer': 'https://chengdu.anjuke.com/community/m58-p%7B%7D/',
        'Sec-Fetch-Mode': 'no-cors',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    response = requests.get(url, headers=headers,timeout=180).text
    return response 
def getdata(html):
    global keya
    print(keya)
    #print(html)
    keya+=1
    content = etree.HTML(html)
    title = content.xpath('//*[@id="list-content"]/div/div[1]/h3/a/text()')
    urli = content.xpath('//*[@id="list-content"]/div/div[1]/h3/a/@href')
    address = content.xpath('//*[@id="list-content"]/div/div[1]/address/text()')
    tm2 = content.xpath('//*[@id="list-content"]/div/div[1]/p[1]/text()[1]')
    esnums = content.xpath('//*[@id="list-content"]/div/div[1]/p[2]/span/a/text()')
    price2 = content.xpath('//*[@id="list-content"]/div/div[2]/p[1]/descendant::text()')

    lu = re.findall('\］(.*?[号路道街])',str(address),re.S)
    tm3 =re.findall('竣工...(..?.?.?)',str(tm2),re.S)
    address2 =re.findall('\［(.*?)\］',str(address),re.S)
    esfnums = re.findall('\((.*?)\)',str(esnums),re.S)
   
    price4=[]
    for x in price2:
        price3 = re.findall('\d?\d\d\d\d?',str(x),re.S)
        if '无' in str(x):
            price4.append('无')
        elif len(price3)==1:
            price4.append(price3[0])
        else:
            pass
        
    time.sleep(2)
    print(len(title),len(address2),len(lu),len(price4),len(esfnums),len(tm3),len(urli))

    for title,address2,lu,price4,esfnums,tm3,urli in zip (title,address2,lu,price4,esfnums,tm3,urli):
        sqlc = "INSERT INTO  anjuke_xiaoqu_58 (name,address,lu,price2,esfnums,tm,url) VALUES(%s,%s,%s,%s,%s,%s,%s)"
        cursor.execute(sqlc,[title,address2,lu,price4,esfnums,tm3,urli])
        conn.commit()
   
            

def creattable():
    sql ="""
    CREATE TABLE if not exists `fang_xiaoqu_10`(
    `id`    INT UNSIGNED AUTO_INCREMENT,
    `name`    VARCHAR(255)  NULL,
    `address` VARCHAR(255)  NULL,
    `lu`    VARCHAR(255)  NULL,
    `price1` VARCHAR(255)  NULL,
    `price2` VARCHAR(255)  NULL,
    `esf_nums`   VARCHAR(255)  NULL,
    `zu_nums`     VARCHAR(255)  NULL,
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
    for page in range(28,51):
        html = get_html(page)
        getdata(html)
    
if __name__ == '__main__':
    
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='diy',charset='utf8')
    cursor = conn.cursor()
    #main()
    creattable()
    cursor.close()
    conn.close()
