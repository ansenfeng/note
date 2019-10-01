# 获取key
    官网：https://www.quandl.com/
    我注册使用 gmail和vpn，才出现验证码
    邮箱验证 --> 
    account settings(账户设置)
    YOUR API KEY 就是我们需要的key了，可以在python中使用。
    
# 数据库使用方法
    import pandas as pd
    import quandl
    quandl.ApiConfig.api_key = "5PYAiWNi3hH3b415rFy2"
    test = quandl.get('WWDI/CHN_IS_AIR_PSGR')
    print(test)
#  举例命名规则
    WWDI/{COUNTRY}_{INDICATOR}
    其中，WWDI代表Quandl数据库代码，{COUNTRY}是相关国家/地区的ISO 3字母代码，并且{INDICATOR}是指标代码。
#  代码获取
    请打开数据库页，
    DATA(数据)：数据库页面
    DOCUMENTATION(文档):包含具体数据库介绍，命名规则，和详细数据参数，国家代码的说明和下载
    USAGE api以及各语言的使用方法介绍
