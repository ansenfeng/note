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
# 例子
    #coding=utf-8
    # 改变浏览器窗口大小、前进后退
    
    from selenium import webdriver
    import time
    
    driver = webdriver.Firefox()
    driver.maximize_window() #浏览器最大化
    
    driver.get("http://www.runoob.com/html/html-tutorial.html")
    time.sleep(2)
    
    driver.set_window_size(480,800) #改变窗口大小。这个网站做了响应式布局，分别看到三栏、两栏、一栏
    time.sleep(2)
    
    driver.set_window_size(900,1000)
    time.sleep(2)
    
    driver.get("http://www.runoob.com") #访问第二个网页，练习前进后退
    time.sleep(2)
    
    driver.back()#后退
    print("back to url :"+driver.current_url)
    time.sleep(2)
    driver.forward() #前进
    print("forward to url :"+driver.current_url)
    time.sleep(2)
    
    driver.quit()
