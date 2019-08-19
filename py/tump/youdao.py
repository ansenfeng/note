import requests        #导入requests包
from bs4 import    BeautifulSoup
url='http://www.cntour.cn/'
proxies={
    "http":"http://10.10.1.10:3128",
    "https":"http://10.10.1.10:1080",
}
response = requests.get(url, )
strhtml=requests.get(url,proxies)
soup=BeautifulSoup(strhtml.text,'lxml')
data = soup.select('#main>div>div.mtop.firstMod.clearfix>div.centerBox>ul.newsList>li>a')

import re
for item in data:
    result={
        "title":item.get_text(),
        "link":item.get('href'),
        'ID':re.findall('\d+',item.get('href'))
    }
print(result)
print (data)