import requests        #导入requests包
# from bs4 import    BeautifulSoup
from lxml import etree
import csv
temp = r"/Users/anson/Desktop/py"+'\\'
url='https://tieba.baidu.com/p/3138733512?see_lz=1&pn=1'
proxies={
    "http":"http://10.10.1.10:3128",
    "https":"http://10.10.1.10:1080",
}
response = requests.get(url.format("转让",1))
response.encoding = "utf8"
responsed =response.text
print(responsed)