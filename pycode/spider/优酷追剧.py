import requests
import re
from lxml import etree
import pandas as pd
import numpy as np
import json

import csv

pd.options.display.max_columns = None
pd.options.display.max_rows = None
pd.set_option('display.float_format',lambda x : '%.0f' % x)
def get(key):
    for i in range(1,key):
        url='https://list.youku.com/category/page?c=97&s=1&d=1&a=%E4%B8%AD%E5%9B%BD%E9%A6%99%E6%B8%AF&type=show&p={}'.format(i)
        headers = {
     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
        }
        res= requests.get(url,headers=headers)
        resp=res.text
        htm=etree.HTML(resp)
        #print(resp)
        js=json.dumps(res.json(),ensure_ascii=False)
        #print(js)
        print(i)
        info = json.loads(js)
        print(info)
        #js=json.dumps(file.read(),ensure_ascii=False)
        # for x in info:
        #     # print (x)
        # #print(info['data'])
        for x in info['data']:
            print(x['title'],x['summary'],x['videoLink'])
            with open("优酷港剧.csv","a") as csvfile: 
                writer = csv.writer(csvfile) #先写入columns_name
                writer.writerow([x['title'],x['summary'],x['videoLink']])
      
        # url = htm.xpath('//*[@id="main-content-list"]/div[1]/ul/li/div[1]/div[2]/div[1]/h2/a/@href')
        # class1=htm.xpath('//*[@id="main-content-list"]/div[1]/ul/li/div[1]/div[2]/div[2]/span[1]/text()')
        # area =htm.xpath('//*[@id="main-content-list"]/div[1]/ul/li/div[1]/div[2]/div[2]/span[2]/text()')
        # price=htm.xpath('//*[@id="main-content-list"]/div[1]/ul/li/div[2]/p[1]/text()')
        # time =htm.xpath('//*[@id="main-content-list"]/div[1]/ul/li/div[2]/p[2]/text()')
        # engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/diy?charset=utf8')#mydb?编码
        # df = pd.DataFrame({'name':title,'class':class1,'area':area,'price':price,'time':time,'url':url})
        # df.to_sql('liebiaowang', engine,if_exists='append')


# import numpy as np

# filepath='/Users/anson/Desktop/page.json'
# file = open(filepath, "rb")
# info = json.load(file)
# #js=json.dumps(file.read(),ensure_ascii=False)
# for x in info:
#     print (x)
# #print(info['data'])
# for x in info['data']:
#     print(x['title'],x['title'],x['summary'],x['videoLink'])
# resa = requests.get('https://list.youku.com/category/page?c=97&s=1&d=1&a=%E7%BE%8E%E5%9B%BD&type=show&p=2')
# #resa.decode('gb2312').encode('utf-8')
# result = json.dumps(resa.json(),ensure_ascii=False) #若不指定ensure_ascii=False，输出的是中文的ascii 字符码，而不是真正的中
# print(result)


def getxinwen():

    url='http://finance.sina.com.cn/7x24/'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'}
    res= requests.get(url,headers=headers)
    res.encoding = res.apparent_encoding#解决乱码
    resp=res.text
    htm=etree.HTML(resp)
    # print(resp)
    # print(res.apparent_encoding)
    #js=json.dumps(res.json(),ensure_ascii=False)
    #print(js)
    s='/Users/anson/Desktop/feed.json'
    with open(s,'r') as load_f:
        load_dict = json.load(load_f)
        print(load_dict)
   

getxinwen()






#if __name__ == '__main__':
  #getxinwen()