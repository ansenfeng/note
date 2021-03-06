# 
    删除空行
    df = df.dropna()
    # 可以通过axis参数来删除含有空数据的全部列
    df = df.dropna(axis=1)
    
    # 可以通过subset参数来删除在age和sex中含有空数据的全部行
    df = df.dropna(subset=["age", "sex"])
    df = df.dropna(subset=['age', 'body','home.dest'])
    
    行列翻转  df.T 
    df2.replace(r'.*?万','', inplace=True,regex=True)
    #表达式，替换内容，写入原数据，表达式和字符切换
    df2.replace(r'[()]','', inplace=True,regex=True)  
    df2=df.copy()#复制表
    df2['Unnamed: 21']='-'#改变列的值
    df2.rename(columns={'Unnamed: 21':'tr1', 'Unnamed: 42':'tr2'}, inplace = True)#改变列名   
# 导入数据：
      
      pd.read_csv(filename,dtype='str')：从CSV文件导入数据,读取类型
      pd.read_table(filename)：从限定分隔符的文本文件导入数据
      pd.read_excel(filename)：从Excel文件导入数据
      pd.read_sql(query, connection_object)：从SQL表/库导入数据
      pd.read_json(json_string)：从JSON格式的字符串导入数据
      pd.read_html(url)：解析URL、字符串或者HTML文件，抽取其中的tables表格
      pd.read_clipboard()：从你的粘贴板获取内容，并传给read_table()
      pd.DataFrame(dict)：从字典对象导入数据，Key是列名，Value是数据

# 导出数据：

    df.to_csv(filename)：导出数据到CSV文件
    df.to_excel(filename)：导出数据到Excel文件
    df.to_sql(table_name, connection_object)：导出数据到SQL表
    df.to_json(filename)：以Json格式导出数据到文本文件


# 创建测试对象：

    pd.DataFrame(np.random.rand(20,5))：创建20行5列的随机数组成的DataFrame对象
    pd.Series(my_list)：从可迭代对象my_list创建一个Series对象
    df.index = pd.date_range('1900/1/30', periods=df.shape[0])：增加一个日期索引


# 查看、检查数据：


    df.head(n)：查看DataFrame对象的前n行
    df.tail(n)：查看DataFrame对象的最后n行
    df.shape()：查看行数和列数
    http:// df.info() ：查看索引、数据类型和内存信息
    df.describe()：查看数值型列的汇总统计
    s.value_counts(dropna=False)：查看Series对象的唯一值和计数
    df.apply(pd.Series.value_counts)：查看DataFrame对象中每一列的唯一值和计数



# 数据选取：

    df[col]：根据列名，并以Series的形式返回列
    df[[col1, col2]]：以DataFrame形式返回多列
    s.iloc[0]：按位置选取数据
    s.loc['index_one']：按索引选取数据
    df.iloc[0,:]：返回第一行
    df.iloc[0,0]：返回第一列的第一个元素


# 数据统计：


    df.describe()：查看数据值列的汇总统计
    df.mean()：返回所有列的均值
    df.corr()：返回列与列之间的相关系数
    df.count()：返回每一列中的非空值的个数
    df.max()：返回每一列的最大值
    df.min()：返回每一列的最小值
    df.median()：返回每一列的中位数
    df.std()：返回每一列的标准差



# 数据合并：

    df1.append(df2)：将df2中的行添加到df1的尾部
    df.concat([df1, df2],axis=1)：将df2中的列添加到df1的尾部
    df1.join(df2,on=col1,how='inner')：对df1的列和df2的列执行SQL形式的join


# 数据处理：


    df[df[col] > 0.5]：选择col列的值大于0.5的行
    df.sort_values(col1)：按照列col1排序数据，默认升序排列
    df.sort_values(col2, ascending=False)：按照列col1降序排列数据
    df.sort_values([col1,col2], ascending=[True,False])：先按列col1升序排列，后按col2降序排列数据
    df.groupby(col)：返回一个按列col进行分组的Groupby对象
    df.groupby([col1,col2])：返回一个按多列进行分组的Groupby对象
    df.groupby(col1)[col2]：返回按列col1进行分组后，列col2的均值
    df.pivot_table(index=col1, values=[col2,col3], aggfunc=max)：创建一个按列col1进行分组，并计算col2和col3的最大值的数据透视表
    df.groupby(col1).agg(np.mean)：返回按列col1分组的所有列的均值
    data.apply(np.mean)：对DataFrame中的每一列应用函数np.mean
    data.apply(np.max,axis=1)：对DataFrame中的每一行应用函数np.max



# 数据清理：


    df[df[col] > 0.5]：选择col列的值大于0.5的行
    df.sort_values(col1)：按照列col1排序数据，默认升序排列
    df.sort_values(col2, ascending=False)：按照列col1降序排列数据
    df.sort_values([col1,col2], ascending=[True,False])：先按列col1升序排列，后按col2降序排列数据
    df.groupby(col)：返回一个按列col进行分组的Groupby对象
    df.groupby([col1,col2])：返回一个按多列进行分组的Groupby对象
    df.groupby(col1)[col2]：返回按列col1进行分组后，列col2的均值
    df.pivot_table(index=col1, values=[col2,col3], aggfunc=max)：创建一个按列col1进行分组，并计算col2和col3的最大值的数据透视表
    df.groupby(col1).agg(np.mean)：返回按列col1分组的所有列的均值
    data.apply(np.mean)：对DataFrame中的每一列应用函数np.mean
    data.apply(np.max,axis=1)：对DataFrame中的每一行应用函数np.max



# 其它操作：
    改列名：
    方法1
    a.columns = ['a','b','c']
    a.rename(columns={'A':'a', 'B':'b', 'C':'c'}, inplace = True)
    添加行，并使用正则表达式拆分列
    df2['name2']=None
    df2['gdp1']=None
    df2['gdp2']=None
    df2[['gdp1']]=df2['date'].str.extract('(\d.*?亿)',expand=False)
    df2[['gdp2']]=df2['date'].str.extract('\((.*?)\)',expand=False)
    df2[['name2']]=df2['name'].str.extract('(\d\d\d\d)',expand=False)
# 杂项
      df1=pd.DataFrame({"A":[1,'abc',3,4],"B":[5,6,'ddf',8],"C":[1,1,1,1]})
      随机数组建立
      dates=pd.date_range('20130101', periods=6)
      df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
      
      for i in range(0, len(df)):#输出列i 表示行
          print (df.iloc[i]['A'], df.iloc[i]['B'])
      for index, row in df.iterrows():
    print(row) # 输出每行的索引值
    
    
    
    idx = pd.Index([' jack', 'jill ', ' jesse ', 'frank'])
     dfsql=pd.read_sql(sql,engine)
     print(idx.str.strip())
     print(idx.str.lstrip())
     print(idx.str.rstrip())
     df = pd.DataFrame(np.random.randn(3, 2), columns=[' Column A ', ' Column B '], index=range(3))
     print(df.columns.str.strip())
     print(df.columns.str.lower())
     df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')#删除前后空格，中间用_替换
     s2 = pd.Series(['a_b_c', 'c_d_e', np.nan, 'f_g_h'])
     print(s2.str.split('_'))
     print(s2.str.split('_').str.get(0))
     print(s2.str.split('_').str[1])
     print(s2.str.split('_', expand=True))
     print(s2.str.split('_', expand=True, n=1)) #拆分数量
     print(s2.str.rsplit('_', expand=True, n=1))#从尾往前取
     s3 = pd.Series(['A', 'B', 'C', 'Aaba', 'Baca','', np.nan, 'CABA', 'dog', 'cat'])
     print(s3.str.replace('^.a|dog', 'XX-XX ', case=False))
     print(s3)
     dollars = pd.Series(['12', '-$10', '$10,000'])
     print(dollars.str.replace('$', ''))
     print(dollars.str.replace(r'-\$', '-'))
     print(pd.Series(['f.o(abc)', 'fuz', np.nan]).str.replace('f.', '内容', regex=False))
     print(pd.Series(['f.o(abc)', 'fuz', np.nan]).str.replace(r'\((.*?)\)', r'\((.*?)\)', regex=True))
     pat = r"(?P<one>\w+) (?P<two>\w+) (?P<three>\w+)"
     repl = lambda m: m.group('two').swapcase()
     print(pd.Series(['One Two Three', 'Foo Bar Baz']).str.replace(pat, repl))
     s1 = pd.Series(['Mouse', 'dog', 'house and parrot', '23', np.NaN])
     print(s1.str.contains('og', regex=False))    
