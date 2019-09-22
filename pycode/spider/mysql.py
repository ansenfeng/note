import pandas as pd
from sqlalchemy import create_engine
engine = create_engine('mysql+pymysql://root:feanset9@49.235.85.164:3306/economic')#mydb?编码
sql="""
	select * from population;
	"""
df2 = pd.read_sql_query(sql, engine)
# print(df2)
excel = pd.read_excel("/Users/anson/Desktop/py/djangotest/世界人口数据.xls",enconding='utf8',dtype=str)
pd.set_option('display.max_columns', None)#取消列隐藏
print(excel)
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