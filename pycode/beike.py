import requests
import time
from lxml import etree
import xlsxwriter
import re
import json

def get_html(page):
    """获取网站html代码"""
    url = "https://cd.ke.com/ershoufang/pg{}p1/#contentList".format(page)
    headers = {
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }
    response = requests.get(url, headers=headers,timeout=180).text
    return response 
def getdata(html):
    # page=1
    # html = get_html(page)
    content = etree.HTML(html)
    results = content.xpath('//*[@id="beike"]/div[1]/div[4]/div[1]/div[4]/ul/li')
    print (results[0].text)
    for r2 in results:
        title = r2.xpath('*//div/div/a/@title')  
        urlq = r2.xpath('*//div/div[@class="title"]/a/@href') 
        urlw = r2.xpath('*//div/div[2]/div/div/a/@href')      
        address = r2.xpath('*//div/div[2]/div/div/a/text()')
        area = r2.xpath('*//div/div[2]/div[2]/text()')
        time = r2.xpath('*//div/div[2]/div[3]/text()')
        price = r2.xpath('*//div/div[2]/div[5]/div/span/text()')
        hot = re.findall("\d+\w*",str(time))[::2]
        time2 = re.findall("\d+\w*",str(time))[1::2]
        price1 = re.findall("\w*\S\d+\D",str(price))[0::2]
        price2 = re.findall("\w*\S\d+\D",str(price))[1::2]
        ceng = re.findall("\w*\d+\w*",str(area))[::5]
        start = re.findall("\w*\d+\w*",str(area))[::1]
        geju = re.findall("\w*\d+\w*",str(area))[::2]
        sq2 = re.findall("\w*\d+\w*\S\d+\w*",str(area))[::3]
        area1=[]
        for i in range(1,58,2):
            sc= re.findall("\w*\S\d+\D\D",area[i])
            area1.append(sc)
        for a,b,c,d,e in zip(title,address,price1,area1,urlq):
            item = [a,b,c,d,e]
            cont = json.dumps(item,ensure_ascii=False)+",\n"
            with open("txt1.json","a",encoding="utf-8") as f:
                f.write(cont)

def jsonc():
    for a,b,c,d,e in zip(title,address,price1,area1,urlw):
        item = [a,b,c,d,e]
        cont = json.dumps(item,ensure_ascii=False)+",\n"
        with open("txt4.json","a",encoding="utf-8") as f:
            f.write(cont)
def main():
    all_datas = []
    """网站总共100页，循环100次"""
    for page in range(1,100):
        html = get_html(page)
        getdata(html)
    
if __name__ == '__main__':
    main()
