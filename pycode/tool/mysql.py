#-*- coding: utf-8 -*-
import pandas as pd
from sqlalchemy import create_engine
import pymysql
import re
import json
# engine = create_engine('mysql+pymysql://root:feanset9@49.235.85.164:3306/economic')#mydb?编码
# sql="""
# 	select * from population;
# 	"""
# df2 = pd.read_sql_query(sql, engine)
# print(df2)
# excel = pd.read_excel("/Users/anson/Desktop/py/djangotest/世界人口数据.xls",enconding='utf8',dtype=str)
# pd.set_option('display.max_columns', None)#取消列隐藏
# print(excel)
# df1.to_sql('population', engine)#index 自动排序

# df2 = pd.read_excel("/Users/anson/Desktop/py/djangotest/GDP.xls")
# df2.to_sql('gdp', engine)#index 自动排序

# 新建pandas中的DataFrame, 只有id,num两列
# df = pd.DataFrame({'name':[1,2,3],'chinese':[12,34,56],'mathematics':[126,88,94],'english':[42,69,130]})

# # 将新建的DataFrame储存为MySQL中的数据表，不储存index列
# df.to_sql('student', engine, index= False)
# df = pd.DataFrame({'phonename':[1,2,3,4,5,6,7,8,9,10,11,12,13,14],'pnum':[1299,3499,5699,799,8899,1399,2899,2999,3099,18069,5999,8998,9300,1199],})

# # 将新建的DataFrame储存为MySQL中的数据表，不储存index列
# df.to_sql('phone2', engine, index= False)
# sql = '''DROP TABLE baidutieba5;
# '''

                          
# a=['\n                ', '\n                1192人关注\n                / 2月前发布               ', '\n                ', '\n                9人关注\n                / 9天前发布               ', '\n                ', '\n                53人关注\n                / 1月前发布               ', '\n                ', '\n                25人关注\n                / 2月前发布               ', '\n                ', '\n                14人关注\n                / 20天前发布               ', '\n                ', '\n                82人关注\n                / 3月前发布               ', '\n                ', '\n                10人关注\n                / 1月前发布               ', '\n                ', '\n                13人关注\n                / 1月前发布               ', '\n                ', '\n                17人关注\n                / 3月前发布               ', '\n                ', '\n                94人关注\n                / 1年前发布               ', '\n                ', '\n                13人关注\n                / 1月前发布               ', '\n                ', '\n                86人关注\n                / 1年前发布               ', '\n                ', '\n                7人关注\n                / 2月前发布               ', '\n                ', '\n                100人关注\n                / 1年前发布               ', '\n                ', '\n                53人关注\n                / 11月前发布               ', '\n                ', '\n                17人关注\n                / 30天前发布               ', '\n                ', '\n                1人关注\n                / 1月前发布               ', '\n                ', '\n                6人关注\n                / 3月前发布               ', '\n                ', '\n                206人关注\n                / 1年前发布               ', '\n                ', '\n                129人关注\n                / 1年前发布               ', '\n                ', '\n                29人关注\n                / 6月前发布               ', '\n                ', '\n                107人关注\n                / 1年前发布               ', '\n                ', '\n                8人关注\n                / 3月前发布               ', '\n                ', '\n                7人关注\n                / 1月前发布               ', '\n                ', '\n                3人关注\n                / 2月前发布               ', '\n                ', '\n                26人关注\n                / 4月前发布               ', '\n                ', '\n                5人关注\n                / 3月前发布               ', '\n                ', '\n                6人关注\n                / 1月前发布               ', '\n                ', '\n                9人关注\n                / 5月前发布               ', '\n                                ', '\n                            ']

# tm= re.findall('\d?...发布',str(a),re.S)
# hot= re.findall('\d?\d?\d?\d?..关注',str(a),re.S)
# print(len(tm),len(hot))

# e=['35', '单价11808.4元/平米', '38', '单价9036.9元/平米', '28', '单价6089.6元/平米', '38', '单价15200元/平米', '35.5', '单价9332.3元/平米', '38', '单价7700.1元/平米', '38', '单价10555.6元/平米', '33', '单价18272.4元/平米', '33.5', '单价10250.9元/平米', '33', '单价9792.3元/平米', '35', '单价12220.7元/平米', '32.1', '单价9556.4元/平米', '29.5', '单价14482.1元/平米', '35.8', '单价11187.5元/平米', '29', '单价8257.4元/平米', '36', '单价11149元/平米', '31', '单价9518元/平米', '32.8', '单价9257.7元/平米', '29', '单价7123.6元/平米', '30', '单价10925元/平米', '36', '单价10720.7元/平米', '38', '单价9051.9元/平米', '31.5', '单价9270.2元/平米', '36', '单价13835.5元/平米', '30', '单价8542.1元/平米', '29', '单价8192.1元/平米', '39', '单价10546.2元/平米', '30', '单价8467.4元/平米', '35', '单价9809.4元/平米']

# price1 = e[0::2]
# price2 = e[1::2]
# print(price1,price2)

# f=['\n                ', '\n                                  高楼层(共13层)\n                                                    | 2005年建 | \n                                1室0厅 | 29.64平米\n                                  | 南\n                                \n              ', '\n                ', '\n                                  高楼层(共12层)\n                                                    | 2003年建 | \n                                1室0厅 | 42.05平米\n                                  | 东南\n                                \n              ', '\n                ', '\n                                  高楼层(共7层)\n                                                    | 1990年建 | \n                                1室0厅 | 45.98平米\n                                  | 东\n                                \n              ', '\n                ', '\n                                  低楼层(共3层)\n                                                    | 2005年建 | \n                                1室1厅 | 25平米\n                                  | 南\n                                \n              ', '\n                ', '\n                                  中楼层(共17层)\n                                                    | 2011年建 | \n                                1室0厅 | 38.04平米\n                                  | 东\n                                \n              ', '\n                ', '\n                                  高楼层(共6层)\n                                                1室1厅 | 49.35平米\n                                  | 南\n                                \n              ', '\n                ', '\n                                  中楼层(共7层)\n                                                    | 1999年建 | \n                                1室0厅 | 36平米\n                                  | 东南 南\n                                \n              ', '\n                ', '\n                                  高楼层(共13层)\n                                                    | 2005年建 | \n                                1室0厅 | 18.06平米\n                                  | 东北\n                                \n              ', '\n                ', '\n                                  中楼层(共6层)\n                                                    | 2002年建 | \n                                1室0厅 | 32.68平米\n                                  | 东南\n                                \n              ', '\n                ', '\n                                  中楼层(共6层)\n                                                    | 2002年建 | \n                                1室1厅 | 33.7平米\n                                  | 东\n                                \n              ', '\n                ', '\n                                  中楼层(共13层)\n                                                    | 2005年建 | \n                                1室0厅 | 28.64平米\n                                  | 东南\n                                \n              ', '\n                ', '\n                                  中楼层(共20层)\n                                                    | 2015年建 | \n                                1室0厅 | 33.59平米\n                                  | 北\n                                \n              ', '\n                ', '\n                                  低楼层(共7层)\n                                                1室0厅 | 20.37平米\n                                  | 东南\n                                \n              ', '\n                ', '\n                                  高楼层(共12层)\n                                                    | 2004年建 | \n                                1室0厅 | 32平米\n                                  | 北\n                                \n              ', '\n                ', '\n                                  中楼层(共13层)\n                                                    | 2007年建 | \n                                1室0厅 | 35.12平米\n                                  | 东南\n                                \n              ', '\n                ', '\n                                  中楼层(共13层)\n                                                    | 2005年建 | \n                                1室0厅 | 32.29平米\n                                  | 东北\n                                \n              ', '\n                ', '\n                                  中楼层(共13层)\n                                                    | 2014年建 | \n                                1室0厅 | 32.57平米\n                                  | 南\n                                \n              ', '\n                ', '\n                                  高楼层(共6层)\n                                                1室0厅 | 35.43平米\n                                  | 东\n                                \n              ', '\n                ', '\n                                  低楼层(共14层)\n                                                1室1厅 | 40.71平米\n                                  | 西北\n                                \n              ', '\n                ', '\n                                  中楼层(共11层)\n                                                    | 2003年建 | \n                                1室0厅 | 27.46平米\n                                  | 西南\n                                \n              ', '\n                ', '\n                                  高楼层(共20层)\n                                                    | 2015年建 | \n                                1室0厅 | 33.58平米\n                                  | 南\n                                \n              ', '\n                ', '\n                                  高楼层(共6层)\n                                                    | 2002年建 | \n                                1室0厅 | 41.98平米\n                                  | 东南\n                                \n              ', '\n                ', '\n                                  中楼层(共13层)\n                                                    | 2007年建 | \n                                1室0厅 | 33.98平米\n                                  | 东\n                                \n              ', '\n                ', '\n                                  中楼层(共6层)\n                                                    | 2000年建 | \n                                1室0厅 | 26.02平米\n                                  | 西北 南\n                                \n              ', '\n                ', '\n                                  中楼层(共13层)\n                                                    | 2007年建 | \n                                1室0厅 | 35.12平米\n                                  | 东南\n                                \n              ', '\n                ', '\n                                  低楼层(共13层)\n                                                    | 2007年建 | \n                                1室0厅 | 35.4平米\n                                  | 南\n                                \n              ', '\n                ', '\n                                  高楼层(共6层)\n                                                    | 2002年建 | \n                                1室0厅 | 36.98平米\n                                  | 南\n                                \n              ', '\n                ', '\n                                  高楼层(共6层)\n                                                    | 2012年建 | \n                                1室1厅 | 35.43平米\n                                  | 南\n                                \n              ', '\n                ', '\n                                  低楼层(共16层)\n                                                    | 2010年建 | \n                                1室1厅 | 35.68平米\n                                  | 东南\n                                \n              ', '\n                                ', '\n                            ']
# ting= re.findall('.室.厅',str(f),re.S)
# area=re.findall('\d?\d?\d?...平米',str(f),re.S)
# lv= re.findall('\S?楼层..\d?\d?..',str(f),re.S)
# tm2= re.findall('....年建',str(f),re.S)
# tm= re.findall('\d?...发布',str(a),re.S)
# hot= re.findall('\d?\d?\d?\d?..关注',str(a),re.S)
# price1 = e[0::2]
# price2 = e[1::2]

# title =['七一街区酒吧街好利来楼二楼290平直招', '直租无转让费无进场费！', '春熙路西段 展示面广 一铺难求 想要抓紧 尚都对面', '地铁口大面积商铺出租. 适合培训机构 茶楼', '一环路市中心 兰博中心旁 现招大型家宴 娱乐会所 歌舞厅等.', '金荷花2楼1区 主通道 低于市场价几万  仅1万一月', '48元教育培训城 仅一户特价捡漏 带中央空调 舞蹈艺体类优先', '航利中心！正门口第一家带大外摆餐饮商铺急转！！甲级写字楼！！', '武侯区 金牛区 青羊区 锦江区 招教育培训商家 价格美丽！！', '转角低租金铺面 小区5000户 适合做电瓶车修理等业态', '十字路口 全业态 重餐饮 奶茶店 面馆 烧烤店', '春熙路 步行街 银石广场 电梯口 餐饮旺铺出租', '金荷花2楼5区小铺子 16万一年 房东直租', '金牛之心  电梯口  双开门大铺子出租', '七才育中对面！银杏小学旁！适合各类培训教育等！！', '春熙路王府井花车招商 无转让费 旅游区人流量大 适合特色小吃', '美容店母婴店老板看过来 小区门口 人流量大 无转让费', '温江教育培训的老板看过来 学校旁 无转让费', '内金沙一楼双边街旺铺直租，推荐业态生鲜，药房，美发，洗脚保健', '桐梓林中华园别墅底商，适合服装店，奢侈品，眼镜，红酒，虫草，', '人气餐饮综合体 夜宵小吃文化浓厚 旅游写字楼人群多', '开业可满座  公寓楼下缺餐饮业态冒菜，抄手，饺子', '金牛区营门口 十字路口 二楼招租 适合浴足培训网吧', '太升路 恒大广场 顺城大街 全业态 十字路口转角铺 诚意招租', '万象城旁 润街小面积餐饮铺招租 适合快餐 面馆 夜宵 烧烤', '万象城 万年场 华润二十四城二楼临街 近地铁口 餐饮铺', '温江光华大道 学校旁边 临街铺 小面积 人流特别大 可外摆', '8600户成熟社区底商  近地铁口 人流必经之地 超大人流', '（转让）红光超大开间人气旺铺', '（出租）新都万人小区门口 成熟商业级 招特色餐饮生活配套', '青羊工业园区200到3169招租茶楼 教育培训 生鲜', '抚琴西路40米精装转角大开间品牌服装旺铺无转让费出租', '青羊草堂 无转让费 中医理疗馆招租 紧邻西南财大 草堂博物馆', '武侯区 酒店物业直租 带独立电梯 车位充足 随时入场 带大厅', '西华大学广场路十字路口转角铺 人流动向大必经之路 昭示性强', '成渝立交旁 精装写字楼 采光好 面积大 办公 工作室皆可以', '（全新招商）时尚潮流购物娱乐中心品牌小吃花车项目全新招商！！'] 
# address=['新都-新都新城区', '成华-建设路', '锦江-红星路', '成华-二仙桥', '青羊-天府广场', '金牛-荷花池', '金牛-九里堤', '武侯-航空路', '金牛-交大路', '郫都-犀浦', '成华-驷马桥', '锦江-红星路', '金牛-荷花池', '金牛-荷花池', '锦江-三圣乡', '青羊-太升路', '温江-光华大道', '温江-光华大道', '青羊-金沙', '武侯-桐梓林', '成华-动物园', '成华-动物园', '金牛-营门口', '青羊-太升路', '成华-万年场', '成华-万年场', '温江-光华大道', '新都-大丰', '郫都-红光', '新都-新都老城区', '青羊-外光华', '金牛-抚琴小区', '青羊-草堂', '武侯-小天竺街', '郫都-红光', '成华-成渝立交', '青羊-天府广场'] 
# area=['290', '50', '60', '623', '3800', '30', '400', '80', '500', '78', '50', '22', '13', '40', '323', '10', '73', '308', '120', '130', '50', '47', '1314', '2140', '45', '140', '17', '35.5', '135', '200', '400', '466', '60', '1413', '25', '104', '10']
# price=['4.35', '7000', '20.67', '3.1', '30.4', '1', '2', '1.13', '2.75', '5500', '1.2', '1.2', '1.2', '2', '2.26', '2500', '6570', '9240', '1.92', '4', '1.2', '6100', '8', '8.8', '1.71', '1.57', '2450', '7500', '1.45', '1.4', '6', '10', '4000', '9', '9166', '3800', '面议'] 
# tm=['2天前', '08-12', '09-21', '09-21', '09-21', '09-21', '09-21', '09-21', '09-21', '09-21', '09-21', '09-21', '09-21', '09-21', '09-21', '09-21', '09-21', '09-21', '09-21', '09-21', '09-21', '09-21', '09-21', '09-21', '09-21', '09-21', '09-21', '09-21', '09-21', '09-21', '09-21', '09-21', '09-21', '09-21', '09-21', '09-21', '09-21'] 
# zhuangtai=['空置中', '空置中', '经营中', '空置中', '空置中', '空置中', '空置中', '经营中', '空置中', '空置中', '空置中', '经营中', '空置中', '空置中', '空置中', '空置中', '空置中', '空置中', '空置中', '空置中', '经营中', '空置中', '经营中', '空置中', '经营中', '经营中', '空置中', '空置中', '经营中', '空置中', '经营中', '经营中', '空置中', '空置中', '空置中', '空置中', '空置中'] 
# manger =['成都房产经纪', '千城万家', '基业常青', '优铺联行', '金润合房地产', '圣菲房产', '金润合房地产', '千城万家', '金润合房地产', '优铺联行', '优铺联行', '大兴业房地产', '圣菲房产', '圣菲房产', '金润合房地产', '千城万家', '铺天下商业管理', '铺天下商业管理', '臻盛房地产', '盛合宜家', '优铺联行', '优铺联行', '基业常青', '基业常青', '优铺联行', '优铺联行', '优铺联行', '高宅房地产', '优铺联行', '金润合房地产', '玛雅房屋成都总部', '成都房产经纪', '成都房产经纪', '基业常青', '优铺联行', '亿盛源地产', '千城万家'] 
# urli=['https://cd.58.com/shangpu/39500815273768x.shtml', 'https://cd.58.com/shangpu/39116904061335x.shtml', 'https://cd.58.com/shangpu/39558237077893x.shtml', 'https://cd.58.com/shangpu/39556533928602x.shtml', 'https://cd.58.com/shangpu/39558313590286x.shtml', 'https://cd.58.com/shangpu/39556406071438x.shtml', 'https://cd.58.com/shangpu/39556022226717x.shtml', 'https://cd.58.com/shangpu/39558162081064x.shtml', 'https://cd.58.com/shangpu/39558091177354x.shtml', 'https://cd.58.com/shangpu/39556601303041x.shtml', 'https://cd.58.com/shangpu/39557978390296x.shtml', 'https://cd.58.com/shangpu/39557971032477x.shtml', 'https://cd.58.com/shangpu/39556421569829x.shtml', 'https://cd.58.com/shangpu/39556425396127x.shtml', 'https://cd.58.com/shangpu/39556917632780x.shtml', 'https://cd.58.com/shangpu/39557696514185x.shtml', 'https://cd.58.com/shangpu/39557547500677x.shtml', 'https://cd.58.com/shangpu/39557596465950x.shtml', 'https://cd.58.com/shangpu/39557586289156x.shtml', 'https://cd.58.com/shangpu/39557383468293x.shtml', 'https://cd.58.com/shangpu/39557083587237x.shtml', 'https://cd.58.com/shangpu/39557178785026x.shtml', 'https://cd.58.com/shangpu/39556860820115x.shtml', 'https://cd.58.com/shangpu/39556920555163x.shtml', 'https://cd.58.com/shangpu/39556773702657x.shtml', 'https://cd.58.com/shangpu/39556871680027x.shtml', 'https://cd.58.com/shangpu/39556863775261x.shtml', 'https://cd.58.com/shangpu/39556849557653x.shtml', 'https://cd.58.com/shangpu/39556742189337x.shtml', 'https://cd.58.com/shangpu/39556540943756x.shtml', 'https://cd.58.com/shangpu/39556722734097x.shtml', 'https://cd.58.com/shangpu/39556679639568x.shtml', 'https://cd.58.com/shangpu/39556589628681x.shtml', 'https://cd.58.com/shangpu/39556349618051x.shtml', 'https://cd.58.com/shangpu/39556560315142x.shtml', 'https://cd.58.com/shangpu/39556018328091x.shtml', 'https://cd.58.com/shangpu/39556409304867x.shtml']
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='diy',charset='utf8')
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
# cursor = db.cursor(cursor=pymysql.cursors.DictCursor)
# sql = """
# CREATE TABLE USER1 (
# id INT auto_increment PRIMARY KEY ,
# name CHAR(10) NOT NULL UNIQUE,
# age TINYINT NOT NULL
# )ENGINE=innodb DEFAULT CHARSET=utf8;
# """address,area,price1,price2,ting,lv,tm2,tm,urlq
sql ="""
CREATE TABLE if not exists `beike42`(
`id`    INT UNSIGNED AUTO_INCREMENT,
`name`    VARCHAR(255)  NULL,
`address` VARCHAR(255)  NULL,
`area`    VARCHAR(255)  NULL,
`price1` VARCHAR(255)  NULL,
`price2` VARCHAR(255)  NULL,
`ting`   VARCHAR(255)  NULL,
`lv`     VARCHAR(255)  NULL,
`tm2`    VARCHAR(255)  NULL,
`tm`    VARCHAR(255)  NULL,
`url`    VARCHAR(255) NULL,
`Time1` TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
PRIMARY KEY (`id`)
)ENGINE=MyISAM DEFAULT CHARSET=utf8;
"""
sql2="""INSERT INTO  beike42 (name,address)VALUES(%s,%s)"""
sql3=""" select * from test"""
cursor.execute(sql3)

resp=cursor.fetchall()
print(len(resp))
f=json.dumps(resp,ensure_ascii=False)
print(type(f))
d={'test1':"1",'test2':'nihao','data':resp}
e=json.dumps(d,ensure_ascii=False)
print(type(d),type(e))
print(e)
# s =[]
# b= []
# c= []
# d=[]
# for a in resp:
# 	s.append(a[1])
# 	b.append(a[2])
# 	c.append(a[3])
# 	d.append(a[0])
# 	e=json.dumps(a[0])
# 	print(e)
# print(len(s),len(b),len(c),len(d))
# print(type(s),type(b),type(c))
#print(s,b,c,d,sep='\n')
conn.commit()

# for title,address,area,price,tm,zhuangtai,manger,url in  zip(title,address,area,price,tm,zhuangtai,manger,urli):
#     sqlc = "INSERT INTO  58shangpu (name,address,area,price,time,zhuangtai,manger,url) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
#     cursor.execute(sqlc,[title,address,area,price,tm,zhuangtai,manger,url])
#     conn.commit()
cursor.close()
conn.close()
# engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/diy?charset=utf8')#
# conn = engine.connect()
# conn.execute(sql,([title,area]))
# engine.connect() 
# df=pd.read_sql(sql,engine)
# print(df.shape)