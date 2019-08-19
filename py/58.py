import requests
from lxml import etree
import csv
temp = r"/Users/anson/Desktop/py"+'\\'
url='https://cd.58.com/jianzhi/1/pn1'
proxies={
    "http":"http://10.10.1.10:3128",
    "https":"http://10.10.1.10:1080",
}
response = requests.get(url, proxies)
response.encoding = "utf8"
responsed =response.text
htm = etree.HTML(responsed)
re = htm.xpath('/html/body/div[3]/div/div/div/div/div/div/h2/a/text()')
re2 = htm.xpath('/html/body/div[3]/div/div/div/div/div/div/p/text()')
re3 = htm.xpath('/html/body/div[3]/div/div/div/div/div/div/div/span/em/text()')

print(re)
print(re2)
print(re3)
# import requests
# import time
# from bs4 import BeautifulSoup
# url = "https://cd.58.com/jianzhi/1/pn{}"
# def spider():
#     for i in range(1, 9):
#         req = requests.get(url.format(str(i + 1)))
#         req.encoding = "utf8" #设置成网页的编码
#         soup = BeautifulSoup(req.text, "lxml")
#         items = soup.select("li.job_item")
#         for item in items:
#             address = item.select("div.item_con span.address")[0].text #select()返回的是list类型
#             name = item.select("div.item_con span.name")[0].text
#             salary = item.select("div.item_con p.job_salary")[0].text
#             if len(item.select("div.item_con div.job_wel")) > 0:
#                 welfare = item.select("div.item_con div.job_wel")[0].text
#             company = item.select("div.item_con div.comp_name a.fl")[0].text
#             href = item.select("div.item_con div.comp_name a.fl")[0].get("href")
#             print("%s\t%s\t%s\t%s\t%s\t%s"%(address, name, salary, company,welfare,href))
#             # time.sleep(2)
# if __name__ == '__main__':
#     spider()
