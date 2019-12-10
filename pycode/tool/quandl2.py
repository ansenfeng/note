# -*- coding:utf-8 -*-
#from datetime import date  
import pandas as pd
import quandl
from sqlalchemy import create_engine
import traceback
import pymysql
quandl.ApiConfig.api_key= "5PYAiWNi3hH3b415rFy2"
# test = quandl.get('WWDI/CHN_IS_AIR_PSGR')
# print(test)
#
#test2.to_csv('afg2.csv',mode='w', encoding='utf8', header=1,sep='\t')

# test3 =quandl.get('WWDI/CHN_NY_GDP_MKTP_CN')
# print(test2)
# print(test3)
# gdplhg= quandl.get('WWDI/AFR_NY_GDP_MKTP_CD')
# print(gdplhg)
def getdata():
    df=pd.read_csv('country_codes.csv',sep='|')
    for x in df['CODE']:
        url ='WWDI/{}_NE_TRD_GNFS_ZS'.format(x)
        try:
            print(url)
            tb=quandl.get(url)
            tb.to_csv(r'NE_TRD_GNFS_ZS/'+x+'.csv',mode='w', encoding='utf8', header=1,sep='\t')
        except:
            print(x+':NaN')
def tosql():
	engine = create_engine('mysql+pymysql://root:123456@127.0.0.1:3306/diy?charset=utf8')
	df=pd.read_csv('country_codes.csv',sep='|')
	a=df.values
	for x in a:
		try:
			df = pd.read_csv(r'NE_TRD_GNFS_ZS/'+x[1]+'.csv',sep='\t')
			df1=df.set_index(['Date'])#设置date列为列索引
			df2=df1.T#翻转行和列
			df2.insert(0,'country',x[0])#插入两列
			df2.insert(1,'code',x[1])
			df3=df2.set_index(['country'])#再次设置列索引
			print(x[1])
			df3.to_sql('IBRD_maoyizhanbi',engine,if_exists='append')
		except  Exception as e :
			print(x[0],x[1]+'：失败')
			print(e.args)

def create_table():
    conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='123456', db='diy',charset='utf8')
    cursor = conn.cursor()
    sql ="""
    CREATE TABLE if not exists `IBRD_maoyizhanbi`(
    `id`    INT UNSIGNED AUTO_INCREMENT,
    `country`    VARCHAR(255)  NULL,
    `code` VARCHAR(255)  NULL,
    `1960-12-31` double  NULL,
    `1961-12-31` double  NULL,
    `1962-12-31` double  NULL,
    `1963-12-31` double  NULL,
    `1964-12-31` double  NULL,
    `1965-12-31` double  NULL,
    `1966-12-31` double  NULL,
    `1967-12-31` double  NULL,
    `1968-12-31` double  NULL,
    `1969-12-31` double  NULL,
    `1970-12-31` double  NULL,
    `1971-12-31` double  NULL,
    `1972-12-31` double  NULL,
    `1973-12-31` double  NULL,
    `1974-12-31` double  NULL,
    `1975-12-31` double  NULL,
    `1976-12-31` double  NULL,
    `1977-12-31` double  NULL,
    `1978-12-31` double  NULL,
    `1979-12-31` double  NULL,
    `1980-12-31` double  NULL,
    `1981-12-31` double  NULL,
    `1982-12-31` double  NULL,
    `1983-12-31` double  NULL,
    `1984-12-31` double  NULL,
    `1985-12-31` double  NULL,
    `1986-12-31` double  NULL,
    `1987-12-31` double  NULL,
    `1988-12-31` double  NULL,
    `1989-12-31` double  NULL,
    `1990-12-31` double  NULL,
    `1991-12-31` double  NULL,
    `1992-12-31` double  NULL,
    `1993-12-31` double  NULL,
    `1994-12-31` double  NULL,
    `1995-12-31` double  NULL,
    `1996-12-31` double  NULL,
    `1997-12-31` double  NULL,
    `1998-12-31` double  NULL,
    `1999-12-31` double  NULL,
    `2000-12-31` double  NULL,
    `2001-12-31` double  NULL,
    `2002-12-31` double  NULL,
    `2003-12-31` double  NULL,
    `2004-12-31` double  NULL,
    `2005-12-31` double  NULL,
    `2006-12-31` double  NULL,
    `2007-12-31` double  NULL,
    `2008-12-31` double  NULL,
    `2009-12-31` double  NULL,
    `2010-12-31` double  NULL,
    `2011-12-31` double  NULL,
    `2012-12-31` double  NULL,
    `2013-12-31` double  NULL,
    `2014-12-31` double  NULL,
    `2015-12-31` double  NULL,
    `2016-12-31` double  NULL,
    `2017-12-31` double  NULL,
    PRIMARY KEY (`id`)
    )ENGINE=InnoDB DEFAULT CHARSET=utf8;
    """
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    tosql()

