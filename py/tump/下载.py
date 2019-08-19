# -*- coding: utf-8 -*-
import urllib3,urllib,time,re,sys,ssl,os
from urllib import request
import urllib.request
import subprocess
"""
Created on Wed Mar 13 10:35:48 2019

@author: fern.xu
"""

#对目标网站进行html源码查看
ssl._create_default_https_context = ssl._create_unverified_context
url = "https://galactic.ink/piano/"
page = request.urlopen(url)
html = page.read().decode('utf-8') 

#使用正则对源码html中匹配.jar的绝对url地址
reg = r'<a href="(.+?\.jar)">' 
imgre = re.compile(reg) 
imglist = re.findall(imgre,html) 

#print (imglist[0])

#从url中提取文件名
url_filename = os.path.basename(imglist[0])
print(url_filename)

#组装在WINDOWS文件要保存路径与名称
winpath = r'D:\work\pywork'
#filename = r'agreement.jar'
#dest_dir = os.path.join(winpath,filename)
#print(dest_dir)

dest_dir = os.path.join(winpath,url_filename)
print(dest_dir)


#对文件进行下载
#方法1
#urllib.request.urlretrieve(imglist[0],dest_dir)
#方法2
response = request.urlopen(imglist[0])
chunk = 16*1024
with open(dest_dir,"wb") as f:
    while True:
        chunk = response.read(chunk)
        if not chunk:
            break
        f.write(chunk)
