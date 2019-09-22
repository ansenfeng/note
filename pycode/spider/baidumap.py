import requests
import time
#百度地图API搜索
def baidu_search(query, region):
    url = 'http://api.map.baidu.com/place/v2/search?'
    output = 'json'
    ak = 'T6NXaAPDKnQfW6vzyeDcooG0t1jeBFao'
    uri = url + 'query=' + query + '&region='+region+'&output=' + output + '&ak=' + ak
    r = requests.get(uri)
    response_dict = r.json()
    results = response_dict["results"]
    for adr in results:
        name = adr['name']
        location= adr['location']
        lng = float(location['lng'])
        lat = float(location['lat'])
        address = adr['address']
        if 'telephone' in adr:
            telephone = adr['telephone']
        else:
            telephone = ''
        print('名称：'+name)
        print('坐标：%f,%f' %(lat,lng))
        print('地址：'+address)
        print('电话：'+telephone+'\n')

def baidu_search2(query,location,radius):
    url = 'http://api.map.baidu.com/place/v2/search?'
    output = 'json'
    ak = 'T6NXaAPDKnQfW6vzyeDcooG0t1jeBFao'
    uri = url + 'query=' + query + '&location='+location+'&radius='+ radius + '&output='+output + '&ak=' + ak
    r = requests.get(uri)
    response_dict = r.json()
    #print(uri)
    results = response_dict["results"]
    for adr in results:
        name = adr['name']
        location= adr['location']
        lng = float(location['lng'])
        lat = float(location['lat'])
        address = adr['address']
        #设置电话不存在为空，不然会报错
        if 'telephone' in adr:
            telephone = adr['telephone']
        else:
            telephone = ''
        # print('名称：'+name)
        # print('坐标：%f,%f' %(lat,lng))
        # print('地址：'+address)
        # print('电话：'+telephone+'\n')
        print(name,address,telephone,sep=':')
# baidu_search('盲人推拿','成都')
#baidu_search2('街电','30.665974,104.059308','500')

tag= ('美食','酒店','购物','生活服务','丽人','旅游景点','休闲娱乐','运动健身','教育培训','文化传媒','医疗','汽车服务','交通设施','金融','房地产','公司企业','政府机构','出入口','自然地物')
def quanbu():   
    for x in tag:
        print(x)
        baidu_search2(x,'30.665974,104.059308','500')
        time.sleep(5)
quanbu()
# 查找了下大家获取百度POI数据的方法，知道了百度地图的地点检索api做了几个限制：
# 1非认证个人开发者2k每日请求量，认证后个人开发者3w日请求量
# 2检索接口最大返回670条结果 地点检索api分两类接口，一类是区域检索，第二类是详情检索，也就是说，如果我需要对每个地点去做详情检索，那就算3w的日请求量也远远不够了。好在我看区域检索接口内也可以返回较为详细的内容，基本够用。还有一个坑是区域检索接口是分页返回的，每页最多20条，所以这会消耗请求量。这里不考虑这些限制，大不了多跑几天。
# 实施方法
# 由于检索接口一次最多能返回670条数据，所以有个策略就是使用矩形检索接口，将矩形区域缩小到一定程度后，该区域的返回条目数不超过670条就可以，当然也不要太小，太小浪费请求量。

# 我先用一个大矩形划定我关心的区域，然后找到左上角和右下角的坐标：（这个可以手动从百度地图web站上获取到） 左下角，石门村：13312800.93，3357744.44 右上角，横山村：13334828.53，3373640.97

# 我们先设计10*10个小矩形来扫描。为了第二天继续爬取，每次移动记录当前矩形的位置。为了观察是否可能由于矩形过小导致数据丢失，记录每个矩形的获取数目，当等于670条时，可以重新细分扫描该类矩形区域。

# 注意 ：上面拿到的坐标是百度地图米制坐标，需要转换成百度经纬度坐标才能用于检索api，转换api地址：webapi/guide/changeposition - Wiki
# # -*- coding: utf-8 -*- 
# # 第一行必须有，否则报中文字符非ascii码错误

# import urllib.request
# from urllib.parse import quote
# import string
# import json
# import time

# #ak需要在百度地图开放平台申请
# ak = "T6NXaAPDKnQfW6vzyeDcooG0t1jeBFao"

# #关键词
# query=["社会福利院"]
# page_size=20
# page_num=0
# scope=1

# #范围：
# #左下坐标 30.379,114.118
# #右上坐标 30.703,114.665
# #中间坐标 30.541,114.3915

# bounds=[
#     [30.379,114.118,30.541,114.3915],
#     [30.379,114.3915,30.541,114.665],
#     [30.541,114.118,30.703,114.3915],
#     [30.541,114.3915,30.703,114.665]
# ]

# new_bounds = []
# # col_row 将bounds的每一小块继续细分为3行3列，可以防止区域内的搜索数量上限400
# col_row = 3 
# for lst in bounds:
#     distance_lat = (lst[2] - lst[0])/col_row
#     distance_lon = (lst[3] - lst[1])/col_row
#     for i in range(col_row):
#         for j in range(col_row):
#             lst_temp = []
#             lst_temp.append(lst[0]+distance_lat*i)
#             lst_temp.append(lst[1]+distance_lon*j)
#             lst_temp.append(lst[0]+distance_lat*(i+1))
#             lst_temp.append(lst[1]+distance_lon*(j+1))
#             new_bounds.append(lst_temp)

# queryResults = []

# for bound in new_bounds:
#     np=True
#     a=[]
#     while np==True:
#         #使用百度提供的url拼接条件
#         url="http://api.map.baidu.com/place/v2/search?ak="+str(ak)+"&output=json&query="+str(query[0])+"&page_size="+str(page_size)+"&page_num="+str(page_num)+"&bounds="+str(bound[0])+","+str(bound[1])+","+str(bound[2])+","+str(bound[3])
#         url = quote(url, safe=string.printable)
        
#         #请求url读取，创建网页对象
#         jsonf = urllib.request.urlopen(url)
#         page_num=page_num+1
        
#         #判断查询翻页进程
#         jsonfile=jsonf.read()
#         s=json.loads(jsonfile)
#         total=int(s["total"])
#         a.append(total)
        
#         queryResults.append(s)

#         max_page=int(a[0]/page_size)+1
#         #防止并发过高，百度地图要求并发小于120
#         time.sleep(1) 
        
#         if page_num>max_page:
#             np=False
#             page_num=0
#             print("search complete")
#             print("output: "+str(bound))
#             print("total: "+str(a[0]))
#             print("")

# results=open("esults2.txt",'a')
# results.write(str(queryResults).encode('utf-8').decode('utf-8'))
# results.close()
# print("ALL DONE!")