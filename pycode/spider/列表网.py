import requests
from lxml import etree
import pandas as pd
from sqlalchemy import create_engine
def get(key):
    for i in range(1,key):
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
#for a,b,c,d,e,f in zip(title,class1,area,price,time,url):
    #print(a+'\t',b+'\t',c+'\t',d+'\t',e+'\t',f)
# print(len(title),len(url),len(class1),len(area),len(price),len(time))
# print(class1)
# for x,y in zip(title,class1):
# 	print(x,y,sep='\t\t\t:::')

if __name__ == '__main__':
	get(26)#页码
