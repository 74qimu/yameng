# a=1
# b=2
# print(a+b)
# from selenium import webdriver #从selenium工具里导入webdriver库
# import time  #导入time这个模块 --python自带的
# driver=webdriver.Chrome() #选择chrome这个浏览器，初始化driver
# driver.implicitly_wait(10)
#1.打开一个网址
# driver.get("http://120.78.128.25:8765")  #打开一个网址
#2.浏览器窗口最大化
# driver.maximize_window()
#3.打开新页面
#4.等待sleep
# time.sleep(3)  #睡了3秒
# driver.get("http://erp.lemfix.com")
#4.向前  向后  刷新
# time.sleep(3)  #睡了3秒
# driver.back()  #向后
# time.sleep(3)  #睡了3秒
# driver.forward() #向前
# time.sleep(3)  #睡了3秒
# driver.refresh() #刷新
#5、退出
#driver.close()  #关闭当前窗口，不会退出会话
# driver.quit() #关闭驱动  会话session关闭

#找元素
# driver.find_element_by_id("username").send_keys("test123")
# driver.find_element_by_id("password").send_keys("123456")
# driver.find_element_by_id("btnSubmit").click()

# driver.find_element_by_xpath("//input[@id='username']").send_keys("test123")
# page_text=driver.find_element_by_xpath("//div[@class='login-logo']//b").text
# if page_text=="柠檬ERP":
#     print("这个页面的标题是:{}".format(page_text))
# else:
#     print("这个条件测试用例不通过！")

import time
def login_page(username,password,driver):   # 形参   -参数化  --提高代码复用率
    driver.find_element_by_id("username").send_keys(username)  # 找到了有username这个id的元素--点击,输入内容
    driver.find_element_by_id("password").send_keys(password)
    driver.find_element_by_id("btnSubmit").click()
def open_url(url,driver):   # 打开网页
    driver.get(url)
    driver.maximize_window()

def search_key(url,driver,username,password,s_key):
    open_url(url,driver)
    login_page(username,password,driver)
    driver.find_element_by_xpath("//span[text()='零售出库']").click()
    P_id = driver.find_element_by_xpath("//div[text()='零售出库']/..").get_attribute("id")
    F_id = P_id+"-frame"
    driver.switch_to.frame(1)
    driver.find_element_by_id("searchNumber").send_keys(s_key)
    driver.find_element_by_id("searchBtn").click()
    time.sleep(1)
    num = driver.find_element_by_xpath("//tr[@id='datagrid-row-r1-2-0']//td[@field='number']/div").text
    return num   # 返回值
