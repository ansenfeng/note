import tushare as ts

# r=ts.get_hist_data('sh')
# print(r)
# r.to_csv('sh.csv',sep='\t')


r=ts.get_industry_classified()
r.to_csv('行业分类.csv',sep='\t')