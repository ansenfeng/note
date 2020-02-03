mac 
# chrome 版本
    chrome://version/
# mac 
    驱动文件夹：/usr/bin
    驱动：
    http://npm.taobao.org/mirrors/chromedriver/
# 手机模式
    mobile_emulation = {"deviceName":"iPhone 6"}
    options = Options()
    options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(chrome_options=options)
